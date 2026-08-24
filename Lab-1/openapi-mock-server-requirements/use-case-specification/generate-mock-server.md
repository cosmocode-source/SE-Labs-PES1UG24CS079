# Use Case Specification: Generate Mock Server

## 1. Use Case Name
**Generate Mock Server** (UC-01)

## 2. Summary / Description
This use case describes how a developer loads an OpenAPI specification file (in JSON or YAML format) and generates an active mock HTTP server that simulates the described endpoints, request validations, and response schemas.

## 3. Actors
- **Primary Actor:** Developer
- **Secondary Actor:** Frontend Application / API Client

## 4. Pre-conditions
1. The developer has a syntactically valid OpenAPI 3.0+ specification file (JSON or YAML format).
2. The OpenAPI Mock Server application is installed and running, or accessible via CLI/UI.

## 5. Post-conditions
- A mock HTTP server is instantiated and running on a target host/port.
- Endpoints corresponding to all paths and methods in the OpenAPI spec are reachable.
- Mock responses populated with schema data/examples are returned for valid requests.

## 6. Main Flow (Basic Flow)
1. The Developer provides the path or URL of an OpenAPI specification file to the system.
2. The System parses the specification file and validates its schema syntax.
3. The System builds internal routing tables for all defined paths, HTTP methods, parameters, and schemas.
4. The System starts the HTTP server on the configured port.
5. The System displays a summary of available mock endpoints and logs startup success.
6. The API Client sends HTTP requests to the generated mock endpoints.
7. The System validates incoming requests against parameter specifications and returns appropriate mock responses based on schema examples or type generation.

## 7. Alternative Flows

### Alt-1: Spec Contains Examples
- At step 7, if response schemas include explicit `example` or `examples` objects, the System prioritizes serving those pre-defined examples over random generated dummy data.

### Alt-2: Dynamic Parameter Validation Failure
- At step 7, if the request fails parameter validation (e.g. missing required header or path param), the System responds with a `400 Bad Request` and validation error details.

## 8. Exception Flows

### Exc-1: Invalid OpenAPI Specification
1. At step 2, if the file fails OpenAPI syntax or schema validation:
   - The System stops execution.
   - The System displays specific parsing error logs indicating line numbers and structural errors.
   - The use case ends unsuccessfully.

### Exc-2: Port Already in Use
1. At step 4, if the target port is bound to another process:
   - The System prompts an error message indicating port conflict.
   - The System suggests an alternate port or allows user selection.
