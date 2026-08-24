# Requirements Table

Below is the requirements specification table for the OpenAPI Mock Server system.

| ID | Category | Requirement Description | Priority | Use Case Ref |
| :--- | :--- | :--- | :--- | :--- |
| **FR-01** | Functional | The system shall accept valid OpenAPI 3.0+ specifications (JSON/YAML). | High | UC-01 |
| **FR-02** | Functional | The system shall parse paths, operations, parameters, and response schemas from the specification. | High | UC-01 |
| **FR-03** | Functional | The system shall generate dynamic mock HTTP endpoints matching spec routes. | High | UC-01 |
| **FR-04** | Functional | The system shall generate realistic mock responses based on schema types and example values. | High | UC-01 |
| **FR-05** | Functional | The system shall allow users to override response status codes and dynamic payloads via custom headers or rules. | Medium | UC-02 |
| **FR-06** | Functional | The system shall support response delay/latency simulation. | Low | UC-03 |
| **NFR-01**| Performance| The mock server shall handle at least 500 requests per second with latency < 50ms. | High | N/A |
| **NFR-02**| Usability   | Users shall be able to spin up a mock server via CLI or Web Interface within 3 steps. | Medium | UC-01 |
| **NFR-03**| Reliability| Mock endpoints shall fail gracefully with standard RFC 7807 error responses for invalid spec paths. | High | UC-01 |
