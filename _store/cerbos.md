---
aid: cerbos
name: Cerbos
description: Cerbos is an open-core, language-agnostic, scalable authorization platform that decouples access control from application code by externalizing fine-grained, context-aware permission decisions into policy-as-code. Authorization is expressed in YAML policies supporting RBAC, ABAC, PBAC, and ReBAC, evaluated by a stateless Policy Decision Point (PDP) that delivers sub-millisecond decisions at scale. The platform consists of the open-source Cerbos PDP (Apache 2.0), Cerbos Hub control plane (PAP), Cerbos Synapse enrichment layer, and PEP SDKs for Go, Java, JavaScript / TypeScript, .NET, PHP, Python, Ruby, and Rust. The PDP exposes both REST (port 3592) and gRPC (port 3593) interfaces, an Admin API, and standards- compliant OpenID AuthZEN endpoints, with query-plan adapters for Prisma and SQLAlchemy.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ABAC
  - Access Control
  - Authorization
  - AuthZEN
  - Open Source
  - PBAC
  - PDP
  - Permissions
  - Policy as Code
  - RBAC
  - ReBAC
  - Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/cerbos/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: cerbos:cerbos-pdp-rest-api
    name: Cerbos PDP REST API
    description: The Cerbos PDP REST API is the HTTP/JSON interface for sending authorization requests to a running Cerbos Policy Decision Point. It exposes CheckResources for evaluating principal-against-resource decisions, PlanResources for translating policies into resource-filter query plans, and ServerInfo for runtime metadata. An OpenAPI / Swagger specification is served by every PDP instance.
    humanURL: https://docs.cerbos.dev/cerbos/latest/api/index
    baseURL: http://localhost:3592
    tags:
      - CheckResources
      - PDP
      - PlanResources
      - REST
    properties:
      - type: Documentation
        url: https://docs.cerbos.dev/cerbos/latest/api/index
      - type: OpenAPI
        url: https://docs.cerbos.dev/cerbos/latest/api/swagger.json
      - type: Reference
        url: https://docs.cerbos.dev/cerbos/latest/api/index#api-resources
  - aid: cerbos:cerbos-pdp-grpc-api
    name: Cerbos PDP gRPC API
    description: The Cerbos PDP gRPC API exposes the cerbos.svc.v1.CerbosService and related management services on port 3593, with server reflection enabled. The gRPC interface is the highest-performance way to embed Cerbos as a sidecar or in-process service for service-to-service authorization.
    humanURL: https://docs.cerbos.dev/cerbos/latest/api/index
    baseURL: localhost:3593
    tags:
      - gRPC
      - PDP
      - Protocol Buffers
    properties:
      - type: Documentation
        url: https://docs.cerbos.dev/cerbos/latest/api/index
      - type: Protocol
        url: https://github.com/cerbos/cerbos/tree/main/api/genpb
  - aid: cerbos:cerbos-authzen-api
    name: Cerbos AuthZEN API
    description: Cerbos implements the OpenID AuthZEN authorization API specification, exposing standards-compliant single-evaluation, batch-evaluations, and well-known metadata endpoints so that any AuthZEN-conformant client or Policy Enforcement Point can integrate with Cerbos as the decision engine.
    humanURL: https://docs.cerbos.dev/cerbos/latest/api/index
    tags:
      - AuthZEN
      - OpenID
      - Standards
    properties:
      - type: Documentation
        url: https://docs.cerbos.dev/cerbos/latest/api/index#authzen
      - type: Specification
        url: https://openid.net/specs/authorization-api-1_0.html
      - type: Discovery
        url: https://docs.cerbos.dev/cerbos/latest/api/index#authzen
  - aid: cerbos:cerbos-admin-api
    name: Cerbos PDP Admin API
    description: The Cerbos Admin API provides management capabilities such as policy add/get/list, schema management, and audit log access on the running PDP. It is intended for administrative use and is gated by HTTP Basic Auth.
    humanURL: https://docs.cerbos.dev/cerbos/latest/api/admin_api
    tags:
      - Admin
      - Audit Log
      - Policy Management
    properties:
      - type: Documentation
        url: https://docs.cerbos.dev/cerbos/latest/api/admin_api
  - aid: cerbos:cerbos-hub-api
    name: Cerbos Hub API
    description: Cerbos Hub is the cloud-hosted Policy Administration Point (PAP) that manages policy authoring, versioning, validation, and distribution to Cerbos PDPs across environments. It also provides decision logs, collaborative policy editing, and embedded PDP delivery.
    humanURL: https://docs.cerbos.dev/cerbos-hub/
    tags:
      - Cloud
      - Hub
      - Policy Administration
      - Policy Distribution
    properties:
      - type: Documentation
        url: https://docs.cerbos.dev/cerbos-hub/
      - type: Console
        url: https://hub.cerbos.cloud/
  - aid: cerbos:cerbos-synapse
    name: Cerbos Synapse
    description: Cerbos Synapse is the enrichment and orchestration component that fetches identity, resource, and relationship attributes from external systems and translates infrastructure protocols (HTTP, gRPC, GraphQL) into Cerbos authorization checks for ReBAC and ABAC scenarios.
    humanURL: https://www.cerbos.dev/products/synapse
    tags:
      - Enrichment
      - ReBAC
      - Synapse
    properties:
      - type: Documentation
        url: https://www.cerbos.dev/products/synapse
common:
  - type: Website
    url: https://www.cerbos.dev
  - type: Documentation
    url: https://docs.cerbos.dev
  - type: GettingStarted
    url: https://docs.cerbos.dev/cerbos/latest/quickstart
  - type: API
    url: https://docs.cerbos.dev/cerbos/latest/api/index
  - type: OpenAPI
    url: https://docs.cerbos.dev/cerbos/latest/api/swagger.json
  - type: Hub
    url: https://hub.cerbos.cloud/
  - type: GitHub
    url: https://github.com/cerbos/cerbos
  - type: GitHubOrganization
    url: https://github.com/cerbos
  - type: SourceCode
    url: https://github.com/cerbos/cerbos
  - type: IssueTracker
    url: https://github.com/cerbos/cerbos/issues
  - type: Releases
    url: https://github.com/cerbos/cerbos/releases
  - type: Blog
    url: https://www.cerbos.dev/blog
  - type: Pricing
    url: https://www.cerbos.dev/pricing
  - type: CaseStudies
    url: https://www.cerbos.dev/case-studies
  - type: Customers
    url: https://www.cerbos.dev/customers
  - type: Slack
    url: https://join.slack.com/t/cerbos/shared_invite/zt-1a99bp8d6-fJiaY7lpDRRUe4UB1u35Yw
  - type: X
    url: https://x.com/CerbosDev
  - type: LinkedIn
    url: https://www.linkedin.com/company/cerbos
  - type: YouTube
    url: https://www.youtube.com/@cerbos
  - type: License
    url: https://github.com/cerbos/cerbos/blob/main/LICENSE
  - type: SecurityPolicy
    url: https://www.cerbos.dev/security
  - type: TermsOfService
    url: https://www.cerbos.dev/terms
  - type: PrivacyPolicy
    url: https://www.cerbos.dev/privacy
  - type: Playground
    url: https://play.cerbos.dev
  - type: DockerHub
    url: https://hub.docker.com/r/cerbos/cerbos
  - name: Features
    type: Features
    data:
      - name: Policy as Code
      - name: YAML Policies
      - name: RBAC
      - name: ABAC
      - name: PBAC
      - name: ReBAC
      - name: Derived Roles
      - name: Sub-Millisecond Decisions
      - name: Stateless PDP
      - name: REST and gRPC APIs
      - name: AuthZEN Standard
      - name: Query Plan Generation
      - name: Audit Logs
      - name: Policy Versioning
      - name: Schema Validation
      - name: Multiple Storage Backends
      - name: Sidecar Deployment
      - name: Embedded PDP
      - name: Apache 2.0 License
  - name: UseCases
    type: UseCases
    data:
      - name: Multi-Tenant SaaS Authorization
      - name: API Authorization
      - name: AI Agent Access Control
      - name: MCP Server Security
      - name: RAG Access Control
      - name: Non-Human Identity Authorization
      - name: Zero Trust Enforcement
      - name: Compliance (SOC 2, HIPAA, GDPR, FedRAMP, PCI DSS)
      - name: Fintech Permissions
      - name: Healthcare Permissions
  - name: Integrations
    type: Integrations
    data:
      - name: Kong
      - name: Gravitee
      - name: Kubernetes
      - name: Envoy
      - name: Neo4j
      - name: Trino
      - name: Model Context Protocol
      - name: Anthropic
      - name: Chroma
      - name: Pinecone
      - name: Okta
      - name: Microsoft Entra ID
      - name: AWS Cognito
      - name: Keycloak
      - name: Auth0
      - name: Clerk
      - name: Stytch
      - name: WorkOS
      - name: Zitadel
      - name: Prisma
      - name: SQLAlchemy
  - name: SDKs
    type: SDKs
    data:
      - name: Go SDK
      - name: Java SDK
      - name: JavaScript / TypeScript SDK
      - name: .NET SDK
      - name: PHP SDK
      - name: Python SDK
      - name: Ruby SDK
      - name: Rust SDK
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
