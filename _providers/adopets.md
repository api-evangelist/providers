---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Adopets Agentic Access
  operation_count: 8
  slug: adopets-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 3
apis:
- description: Create and manage adoption payment requests
  name: Adopets payment-request API
  slug: adopets-payment-request-api
- description: Retrieve and refund payment transactions
  name: Adopets payment-transaction API
  slug: adopets-payment-transaction-api
- description: Connect/disconnect an external system user and obtain a session token
  name: Adopets system-auth API
  slug: adopets-system-auth-api
arazzos:
- description: Connect an external system user, create an adoption payment request with line items, then retrieve it to confirm status. Grounded in real operationIds from the Adopets External API.
  name: Create and collect an adoption payment (Adopets External API)
  slug: adopets-create-adoption-payment
- description: Connect a staff user, look up a payment transaction by uuid, then issue a refund. Grounded in real operationIds from the Adopets External API.
  name: Refund an adoption payment transaction (Adopets External API)
  slug: adopets-refund-transaction
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adopets External payment-request API
  slug: open-adopets-payment-request-api
- collection_type: open
  name: Adopets External payment-request payment-transaction API
  slug: open-adopets-payment-transaction-api
- collection_type: open
  name: Adopets External payment-request system-auth API
  slug: open-adopets-system-auth-api
common:
- group: company
  title: ''
  type: Website
  url: https://adopets.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.adopets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.adopets.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.adopets.com/
- group: build
  title: ''
  type: Postman
  url: https://developers.adopets.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adopets
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/adopets-external-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/adopets-external-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adopets-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adopets-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adopets-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adopets-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adopets-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adopets-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adopets-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adopets-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/adopets-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adopets-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adopets-create-adoption-payment.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adopets-refund-transaction.yml
created: '2026-07-17'
description: Adopets is an Adoption Management System (AMS) for animal shelters and rescues that streamlines the entire pet adoption process — online and in-person applications, approval and team collaboration workflows, digital kennel cards with QR codes, secure payment processing for adoption fees, licenses, products and donations, daily reporting and dashboards, and post-adoption communication. Backed by Techstars. Adopets exposes an External API (documented as a public Postman collection) that lets partner systems connect staff users and create, retrieve, change, cancel, and refund adoption payment requests and transactions on behalf of an organization, authenticated with an organization API key plus a per-session JWT bearer token.
image: https://avatars.githubusercontent.com/u/19703738?v=4
layout: provider
mcp_servers:
- description: ''
  name: adopets-mcp.yml
  slug: adopets-mcpyml
modified: '2026-07-17'
name: Adopets
nav: Providers
network: true
overview: 'Adopets publishes 3 APIs on the [APIs.io](https://apis.io/) network: payment-request API, payment-transaction API, and system-auth API. Tagged areas include Pet Adoption, Animal Welfare, Shelters and Rescues, Adoption Management, and Payments.


  Adopets'' developer surface includes documentation, API reference, authentication, sandbox, and 17 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.7
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adopets/refs/heads/main/screenshots/adopets-2026-07-25T181658.png
security:
- kind: authentication
  name: Adopets Authentication
  slug: adopets-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Adopets Domain Security
  slug: adopets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adopets
tags:
- Pet Adoption
- Animal Welfare
- Shelters and Rescues
- Adoption Management
- Payments
- Nonprofit Technology
- SaaS
- Company
website: https://adopets.com/
---
