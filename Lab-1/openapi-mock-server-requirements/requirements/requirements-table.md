# Requirements Table

This document contains the functional and non-functional requirements for the **OpenAPI Mock Server Generator**.

## Functional Requirements

| ID | Type | Requirement Description | Priority | Acceptance Criteria | Rationale | Use Case Ref |
|---|---|---|---|---|---|---|
| **FR-001** | Functional | The system shall accept OpenAPI 3.0 specifications in YAML and JSON formats. | High | **Pass:** A valid OpenAPI 3.0 YAML or JSON file is successfully uploaded and read.<br>**Fail:** A supported valid file is rejected. | The specification is required as input for generating the mock server. | UC-01 |
| **FR-002** | Functional | The system shall validate the uploaded specification and display errors for invalid OpenAPI structures, paths, parameters, and schemas. | High | **Pass:** An invalid specification is rejected with a clear error message and error location.<br>**Fail:** The system generates endpoints from an invalid specification. | Validation prevents incorrect or unusable mock endpoints from being created. | UC-01 |
| **FR-003** | Functional | The system shall dynamically generate mock HTTP endpoints matching the paths and HTTP methods defined in a valid specification. | High | **Pass:** Every defined path and HTTP method is available after starting the mock server.<br>**Fail:** An undefined endpoint returns `200 OK`. | Developers and testers need endpoints that correctly represent the specified API. | UC-01 |
| **FR-004** | Functional | The system shall generate randomized JSON responses that comply with the response schemas and example values defined in the specification. | High | **Pass:** Generated responses contain the required fields and correct JSON data types.<br>**Fail:** A generated response violates the defined schema. | Schema-compliant responses allow development and testing before the real backend is available. | UC-01 |
| **FR-005** | Functional | The system shall allow users to configure simulated response latency for mock endpoint responses. | High | **Pass:** When a latency value is configured, responses are delayed by approximately that duration.<br>**Fail:** The configured delay is ignored. | Configurable latency allows QA Engineers to test application behaviour under slow-network or slow-server conditions. | UC-02 |

## Non-Functional Requirements

| ID | Type | Requirement Description | Priority | Acceptance Criteria | Rationale | Use Case Ref |
|---|---|---|---|---|---|---|
| **NFR-001** | Performance | The mock server shall sustain at least 1,000 mock API requests per second, with configured simulated latency accurate within ±10 milliseconds. | High | **Pass:** A load test confirms that the server handles 1,000 requests per second and maintains the configured latency within ±10 ms.<br>**Fail:** The server cannot maintain the target request rate or latency accuracy. | The mock server must remain responsive and predictable during peak testing loads. | N/A |
| **NFR-002** | Security and Reliability | The system shall safely reject malformed or potentially harmful specification files without crashing or exposing internal server information. | High | **Pass:** Malformed and unsafe test files are rejected with controlled validation errors, and no stack traces or sensitive details are exposed.<br>**Fail:** The server crashes, executes uploaded file content, or exposes internal details. | Safe file handling protects the mock server and its users from malicious or malformed input. | N/A |
