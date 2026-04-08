---
aid: spire
url: https://raw.githubusercontent.com/api-evangelist/spire/refs/heads/main/apis.yml
apis:
- aid: spire:spire-workload-api
  name: SPIRE Workload API
  description: The SPIRE Agent exposes the SPIFFE Workload API as a Unix domain socket, allowing workloads running on the same node to request their X.509-SVIDs and JWT-SVIDs without requiring any credentials. The Workload API also delivers trust bundle updates so that workloads can verify the identity of other workloads.
  humanURL: https://spiffe.io/docs/latest/spire-about/spire-concepts/
  properties:
  - type: Documentation
    url: https://spiffe.io/docs/latest/spire-about/spire-concepts/
  - type: Reference
    url: https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE_Workload_API.md
  - type: AsyncAPI
    url: asyncapi/spire-workload-asyncapi.yml
  - type: GitHubRepository
    url: https://github.com/spiffe/spire
  tags:
  - gRPC
  - Identity
  - JWT
  - Workload
  - X.509
- aid: spire:spire-server-api
  name: SPIRE Server API
  description: The SPIRE Server exposes a gRPC API used by administrators and the SPIRE Agent to manage registration entries, node attestation, bundle federation, and server health. It allows creating and managing workload registration entries that define the SPIFFE IDs issued to workloads matching specified selectors, and supports federation with external SPIFFE trust domains.
  humanURL: https://spiffe.io/docs/latest/deploying/spire_server/
  properties:
  - type: Documentation
    url: https://spiffe.io/docs/latest/deploying/spire_server/
  - type: Reference
    url: https://github.com/spiffe/spire-api-sdk
  - type: JSONSchema
    url: json-schema/spire-registration-schema.json
  - type: GitHubRepository
    url: https://github.com/spiffe/spire-api-sdk
  tags:
  - Administration
  - Attestation
  - gRPC
  - Registration
  - Server
- aid: spire:spire-agent-api
  name: SPIRE Agent API
  description: The SPIRE Agent runs on each node and handles workload attestation, caching SVIDs, and serving the Workload API. It exposes a health check endpoint and communicates with the SPIRE Server via node attestation to establish its own identity before issuing identities to workloads.
  humanURL: https://spiffe.io/docs/latest/deploying/spire_agent/
  properties:
  - type: Documentation
    url: https://spiffe.io/docs/latest/deploying/spire_agent/
  - type: Reference
    url: https://spiffe.io/docs/latest/deploying/spire_agent/
  - type: GitHubRepository
    url: https://github.com/spiffe/spire
  - type: OpenAPI
    url: openapi/spire-health-openapi.yml
  tags:
  - Agent
  - Attestation
  - Identity
  - Node
  - Security
- aid: spire:spire-oidc-discovery-api
  name: SPIRE OIDC Discovery API
  description: SPIRE includes an OIDC Discovery Provider that serves an OpenID Connect discovery document and JSON Web Key Set (JWKS) endpoint, enabling workloads to present JWT-SVIDs to systems that support standard OIDC token validation. This allows SPIRE-issued identities to be used with cloud provider IAM systems such as AWS, GCP, and Azure.
  humanURL: https://spiffe.io/docs/latest/keyless/oidc-federation-aws/
  properties:
  - type: Documentation
    url: https://spiffe.io/docs/latest/keyless/oidc-federation-aws/
  - type: GitHubRepository
    url: https://github.com/spiffe/spire/tree/main/support/oidc-discovery-provider
  - type: OpenAPI
    url: openapi/spire-oidc-discovery-openapi.yml
  tags:
  - Cloud
  - Federation
  - Identity
  - JWT
  - OIDC
name: SPIRE
tags:
- Authentication
- Cloud Native
- Graduated
- Identity
- Security
- Zero Trust
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SPIRE (SPIFFE Runtime Environment) is the reference implementation of the SPIFFE standard, providing a toolchain for establishing trust between software systems across a wide variety of hosting platforms through automated attestation and workload identity distribution. SPIRE manages a certificate authority, performs node and workload attestation, and issues SVIDs to workloads through the SPIFFE Workload API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

