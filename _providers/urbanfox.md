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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Urbanfox Agentic Access
  operation_count: 14
  slug: urbanfox-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: Fraud case retrieval and updates.
  name: UrbanFox Cases API
  slug: urbanfox-cases-api
- description: End-user account retrieval, creation, updates, and deletion.
  name: UrbanFox End User Accounts API
  slug: urbanfox-end-user-accounts-api
- description: Aggregated tenant metrics and time-series reporting.
  name: UrbanFox Metrics API
  slug: urbanfox-metrics-api
- description: OAuth token generation for machine-to-machine authentication.
  name: UrbanFox OAuth API
  slug: urbanfox-oauth-api
- description: Tenant integration snippet retrieval.
  name: UrbanFox Snippet API
  slug: urbanfox-snippet-api
- description: Tenant details and tenant authentication credentials.
  name: UrbanFox Tenants API
  slug: urbanfox-tenants-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UrbanFox Customer Cases API
  slug: open-urbanfox-cases-api
- collection_type: open
  name: UrbanFox Customer Cases End User Accounts API
  slug: open-urbanfox-end-user-accounts-api
- collection_type: open
  name: UrbanFox Customer Cases Metrics API
  slug: open-urbanfox-metrics-api
- collection_type: open
  name: UrbanFox Customer Cases OAuth API
  slug: open-urbanfox-oauth-api
- collection_type: open
  name: UrbanFox Customer Cases Snippet API
  slug: open-urbanfox-snippet-api
- collection_type: open
  name: UrbanFox Customer Cases Tenants API
  slug: open-urbanfox-tenants-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/urbanfox-customer-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://urbanfox.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.urbanfox.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urbanfox.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.urbanfox.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.urbanfox.io/tutorials/first-api-call
- group: operate
  title: ''
  type: Support
  url: https://docs.urbanfox.io/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.urbanfox.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.urbanfox.io/
- group: start
  title: ''
  type: SignUp
  url: https://2ffr2z.share-eu1.hsforms.com/2wcLUdqqOSWOmGkVadK7V0g
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urbanfox-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbanfox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/urbanfox-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbanfox-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/urbanfox-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/urbanfox-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urbanfox-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/urbanfox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/urbanfox-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/urbanfox-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/urbanfox-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/urbanfox-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/urbanfox-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: UrbanFox is an AI-powered online payment fraud detection and prevention platform that uses generative AI and behavioral intelligence - rather than static rule-sets - to detect payment fraud, account takeover, and bot traffic across transactions, sessions, and accounts. The Techstars-backed company ships a tenant-scoped Customer API (OAuth 2.0 client credentials) for fraud case management, end-user account management, activity metrics, credential rotation, and clickstream collector integration.
image: https://www.urbanfox.io/hubfs/Favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the OpenAPI (no official server)
  slug: candidate-mcp-tool-surface-derived-from-the-openapi-no-official-server
modified: '2026-07-21'
name: UrbanFox
nav: Providers
network: true
overview: 'UrbanFox publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cases API, End User Accounts API, Metrics API, and 3 more. Tagged areas include Fraud Detection, Payment Fraud, Account Takeover, Bot Detection, and Risk Management.


  UrbanFox''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 8
scopes:
- name: Urbanfox Scopes
  scope_count: 13
  slug: urbanfox-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 61.2
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urbanfox/refs/heads/main/screenshots/urbanfox-2026-08-17T082646.png
security:
- kind: authentication
  name: Urbanfox Authentication
  slug: urbanfox-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Urbanfox Domain Security
  slug: urbanfox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urbanfox
tags:
- Fraud Detection
- Payment Fraud
- Account Takeover
- Bot Detection
- Risk Management
- Security
- Artificial Intelligence
- E-Commerce
website: https://urbanfox.io/
---
