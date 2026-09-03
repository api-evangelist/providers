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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Schema-driven object API for building clinical applications on Medable: custom objects and typed properties, querying and aggregation, server-side scripting, accounts, connections, notifications, and '
  name: Medable Cortex API
  slug: medable-cortex-api
artifact_total: 5
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
  type: X-MCPServerCandidate
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
  type: LLMsTxt
  url: llms/medable-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medable-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.medable.com/platform/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://info.medable.com/Pricing.html
- group: commercial
  title: ''
  type: Plans
  url: plans/medable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medable-rate-limits.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.medable.com/company/support
- group: operate
  title: ''
  type: FAQ
  url: https://www.medable.com/resources/faq
created: '2026-07-17'
description: Medable operates a clinical trial technology platform for decentralized and hybrid trials, combining eCOA/ePRO data capture, electronic consent, televisit, and a suite of agentic-AI products (Agent Studio, CRA Agent, PI Summary Review, Digital Data Flow agent) for life-sciences sponsors and CROs. Its developer surface is the Cortex API — a schema-driven object platform (custom objects and properties, querying, aggregation, and server-side scripting) addressed over REST at api.<env>.medable.com/<org_code>/v2/, with session-based and request-signature authentication, an mdctl developer CLI, and an iOS/Swift SDK. Backed by Obvious Ventures and Sapphire Ventures.
image: https://cdn.prod.website-files.com/63da4ae4359b4b2bffd2a3b6/64677a1c8fad4c624f57af3c_medable-open-graph-image.png
layout: provider
modified: '2026-08-15'
name: Medable
nav: Providers
network: true
overview: 'Medable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Health, Clinical Trials, Life Sciences, and eCOA.


  Medable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Medable Plans Pricing
  plan_count: 0
  slug: medable-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 12
  name: Medable Rate Limits
  slug: medable-rate-limits
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 45.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medable/refs/heads/main/screenshots/medable-2026-08-07T172312.png
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
- Backend-as-a-Service
- Agentic AI
website: https://medable.com
---
