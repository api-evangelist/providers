---
aid: spire
name: SPIRE
description: SPIRE (SPIFFE Runtime Environment) is the reference implementation of the SPIFFE standard, providing a toolchain for establishing trust between software systems across a wide variety of hosting platforms through automated attestation and workload identity distribution. SPIRE manages a certificate authority, performs node and workload attestation, and issues SVIDs to workloads through the SPIFFE Workload API.
url: https://spiffe.io/docs/latest/spire-about/
tags:
  - Authentication
  - Cloud Native
  - Graduated
  - Identity
  - Security
  - Zero Trust
created: '2025'
modified: '2026-03-18'
specificationVersion: '0.19'
type: Index
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
      - type: JSONStructure
        url: json-structure/spire-registration-structure.json
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
      - type: JSONStructure
        url: json-structure/spire-svid-structure.json
    tags:
      - Cloud
      - Federation
      - Identity
      - JWT
      - OIDC
common:
  - type: Website
    url: https://spiffe.io/
  - type: Documentation
    url: https://spiffe.io/docs/latest/
  - type: Getting Started
    url: https://spiffe.io/docs/latest/try/getting-started-k8s/
  - type: GitHub Organization
    url: https://github.com/spiffe
  - type: GitHubRepository
    url: https://github.com/spiffe/spire
  - type: Community
    url: https://spiffe.io/community/
  - type: Slack
    url: https://slack.spiffe.io
  - type: Blog
    url: https://spiffe.io/blog/
  - type: Change Log
    url: https://github.com/spiffe/spire/blob/main/CHANGELOG.md
  - type: Security
    url: https://github.com/spiffe/spire/blob/main/SECURITY.md
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spiffe
  - type: JSONSchema
    url: json-schema/spire-svid-schema.json
  - type: JSONSchema
    url: json-schema/spire-registration-schema.json
  - type: JSONStructure
    url: json-structure/spire-svid-structure.json
  - type: JSONStructure
    url: json-structure/spire-registration-structure.json
  - type: JSON-LD
    url: json-ld/spire-context.jsonld
  - type: SpectralRules
    url: rules/spire-rules.yml
  - type: Capabilities
    url: capabilities/workload-identity.yaml
  - type: Vocabulary
    url: vocabulary/spire-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
