---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Cerbos Agentic Access
  operation_count: 22
  slug: cerbos-agentic-access
  summary_line: 22 operations · 12 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: The Cerbos PDP gRPC API exposes the cerbos.svc.v1.CerbosService and related management services on port 3593, with server reflection enabled. The gRPC interface is the highest-performance way to embed
  name: Cerbos PDP gRPC API
  slug: cerbos-pdp-grpc-api
- description: Cerbos implements the OpenID AuthZEN authorization API specification, exposing standards-compliant single-evaluation, batch-evaluations, and well-known metadata endpoints so that any AuthZEN-conforman
  name: Cerbos AuthZEN API
  slug: cerbos-authzen-api
- description: The Cerbos Admin API provides management capabilities such as policy add/get/list, schema management, and audit log access on the running PDP. It is intended for administrative use and is gated by HTT
  name: Cerbos PDP Admin API
  slug: cerbos-admin-api
- description: Cerbos Hub is the cloud-hosted Policy Administration Point (PAP) that manages policy authoring, versioning, validation, and distribution to Cerbos PDPs across environments. It also provides decision l
  name: Cerbos Hub API
  slug: cerbos-hub-api
- description: Cerbos Synapse is the enrichment and orchestration component that fetches identity, resource, and relationship attributes from external systems and translates infrastructure protocols (HTTP, gRPC, Gra
  name: Cerbos Synapse
  slug: cerbos-synapse
- description: Audit and decision log access (Admin API).
  name: Cerbos Admin Audit API
  slug: cerbos-admin-audit-api
- description: Policy management (Admin API).
  name: Cerbos Admin Policies API
  slug: cerbos-admin-policies-api
- description: JSON schema management (Admin API).
  name: Cerbos Admin Schemas API
  slug: cerbos-admin-schemas-api
- description: Policy store administration (Admin API).
  name: Cerbos Admin Store API
  slug: cerbos-admin-store-api
- description: OpenID AuthZEN standards-compliant evaluation endpoints.
  name: Cerbos AuthZEN API
  slug: cerbos-authzen-api
- description: Evaluate authorization decisions.
  name: Cerbos Check API
  slug: cerbos-check-api
- description: Generate query plans for resource filtering.
  name: Cerbos Plan API
  slug: cerbos-plan-api
- description: PDP server metadata.
  name: Cerbos Server API
  slug: cerbos-server-api
artifact_total: 51
collections:
- collection_type: open
  name: Cerbos PDP REST API
  slug: open-cerbos
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cerbos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerbos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerbos-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cerbos.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cerbos.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cerbos.dev/cerbos/latest/quickstart
- group: other
  title: ''
  type: API
  url: https://docs.cerbos.dev/cerbos/latest/api/index
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.cerbos.dev/cerbos/latest/api/swagger.json
- group: other
  title: ''
  type: Hub
  url: https://hub.cerbos.cloud/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cerbos/cerbos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cerbos
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cerbos/cerbos
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cerbos/cerbos/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/cerbos/cerbos/releases
- group: company
  title: ''
  type: Blog
  url: https://www.cerbos.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cerbos.dev/pricing
- group: other
  title: ''
  type: CaseStudies
  url: https://www.cerbos.dev/case-studies
- group: other
  title: ''
  type: Customers
  url: https://www.cerbos.dev/customers
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/cerbos/shared_invite/zt-1a99bp8d6-fJiaY7lpDRRUe4UB1u35Yw
- group: other
  title: ''
  type: X
  url: https://x.com/CerbosDev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerbos
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@cerbos
- group: commercial
  title: ''
  type: License
  url: https://github.com/cerbos/cerbos/blob/main/LICENSE
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.cerbos.dev/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerbos.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerbos.dev/privacy
- group: other
  title: ''
  type: Playground
  url: https://play.cerbos.dev
- group: other
  title: ''
  type: DockerHub
  url: https://hub.docker.com/r/cerbos/cerbos
- group: build
  title: ''
  type: SDKs
  url: ''
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/cerbos/skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cerbos.dev/llms.txt
created: '2026-03-25'
description: Cerbos is an open-core, language-agnostic, scalable authorization platform that decouples access control from application code by externalizing fine-grained, context-aware permission decisions into policy-as-code. Authorization is expressed in YAML policies supporting RBAC, ABAC, PBAC, and ReBAC, evaluated by a stateless Policy Decision Point (PDP) that delivers sub-millisecond decisions at scale. The platform consists of the open-source Cerbos PDP (Apache 2.0), Cerbos Hub control plane (PAP), Cerbos Synapse enrichment layer, and PEP SDKs for Go, Java, JavaScript / TypeScript, .NET, PHP, Python, Ruby, and Rust. The PDP exposes both REST (port 3592) and gRPC (port 3593) interfaces, an Admin API, and standards- compliant OpenID AuthZEN endpoints, with query-plan adapters for Prisma and SQLAlchemy.
features:
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
finops:
- name: Cerbos Finops
  service_category: API
  slug: cerbos-finops
graphqls:
- description: ''
  name: Cerbos GraphQL API
  slug: cerbos-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cerbos.png
layout: provider
modified: '2026-05-19'
name: Cerbos
nav: Providers
network: true
overview: 'Cerbos publishes 9 APIs on the [APIs.io](https://apis.io/) network, including AuthZEN API, Admin Audit API, Admin Policies API, and 6 more. Tagged areas include ABAC, Access Control, Authorization, AuthZEN, and Open Source.


  Cerbos'' developer surface includes authentication, documentation, getting-started guide, GitHub presence, release notes, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Cerbos Plans Pricing
  plan_count: 3
  slug: cerbos-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Cerbos Rate Limits
  slug: cerbos-rate-limits
score:
  band: developing
  composite: 50.2
  delta: -2.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 48.7
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerbos/refs/heads/main/screenshots/cerbos-2026-06-20T174139.png
security:
- kind: authentication
  name: Cerbos Authentication
  slug: cerbos-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cerbos Domain Security
  slug: cerbos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: cerbos-policy
  slug: cerbos-policy
slug: cerbos
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
use_cases:
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
website: https://www.cerbos.dev
---
