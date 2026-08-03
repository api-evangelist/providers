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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'Schema-driven object API for building clinical applications on Medable: custom objects and typed properties, querying and aggregation, server-side scripting, accounts, connections, notifications, and '
  name: Medable Cortex API
  slug: medable-cortex-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://medable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.medable.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.medable.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medable.com/cortex-api/cortex-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.medable.com/getting-started/cortex-user-guide/first-api-request
- group: operate
  title: ''
  type: Support
  url: https://www.medable.com/company/support
- group: company
  title: ''
  type: Blog
  url: https://www.medable.com/resources/knowledge-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Medable
- group: start
  title: ''
  type: SignUp
  url: https://www.medable.com/find-your-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medable.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medable.com/legal/privacy-center
- group: operate
  title: ''
  type: StatusPage
  url: https://status.medable.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/medable-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medable-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medable-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/medable-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medable-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/medable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/medable-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/medable-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medable-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medable-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/medable-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medable-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medable-domain-security.yml
created: '2026-07-17'
description: Medable operates a clinical trial technology platform for decentralized and hybrid trials, combining eCOA/ePRO data capture, electronic consent, televisit, and a suite of agentic-AI products (Agent Studio, CRA Agent, PI Summary Review, Digital Data Flow agent) for life-sciences sponsors and CROs. Its developer surface is the Cortex API — a schema-driven object platform (custom objects and properties, querying, aggregation, and server-side scripting) addressed over REST at api.<env>.medable.com/<org_code>/v2/, with session-based and request-signature authentication, an mdctl developer CLI, and an iOS/Swift SDK. Backed by Obvious Ventures and Sapphire Ventures.
image: https://cdn.prod.website-files.com/63da4ae4359b4b2bffd2a3b6/64677a1c8fad4c624f57af3c_medable-open-graph-image.png
layout: provider
mcp_servers:
- description: ''
  name: medable-mcp.yml
  slug: medable-mcpyml
modified: '2026-07-20'
name: Medable
nav: Providers
network: true
overview: 'Medable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Health, Clinical Trials, Life Sciences, and eCOA.


  Medable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 34.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Medable Authentication
  slug: medable-authentication
  summary_line: apiKey/http-signature/session · 3 schemes
- kind: domain-security
  name: Medable Domain Security
  slug: medable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: medable
tags:
- Company
- Human Health
- Clinical Trials
- Life Sciences
- eCOA
- Healthcare
- Decentralized Clinical Trials
- Backend as a Service
- Agentic AI
website: https://medable.com
---
