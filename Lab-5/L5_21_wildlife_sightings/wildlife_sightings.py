"""Record wildlife sightings and summarise them by zone and species."""

import hashlib
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE sightings "
    "(id INTEGER PRIMARY KEY, species TEXT, zone TEXT, count INTEGER)"
)


def log_sighting(connection, species, zone, count, extras=None):
    """Record a sighting and return updated species totals."""
    if extras is None:
        extras = {}

    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count),
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Return a six-character observer identifier."""
    return hashlib.sha256(observer.encode()).hexdigest()[:6]


def zone_summary(connection, zone):
    """Return the total sightings count for the specified zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?",
        (zone,),
    ).fetchone()
    if row[0] is None:
        return 0
    return row[0]


def rarest(connection):
    """Return the species with the lowest total sighting count."""
    rows = connection.execute(
        "SELECT species, SUM(count) FROM sightings GROUP BY species"
    ).fetchall()
    l=min(rows, key=lambda r: r[1])
    return l[0]


def main():
    """Run the wildlife sightings demonstration."""
    totals = log_sighting(conn, "Leopard", "North", 1)
    log_sighting(conn, "Chital", "North", 24, totals)
    log_sighting(conn, "Hornbill", "East", 3, totals)

    if len(totals) != 3:
        raise ValueError("Expected totals for three species.")

    print(observer_id("Arun"), zone_summary(conn, "North"), rarest(conn))


main()