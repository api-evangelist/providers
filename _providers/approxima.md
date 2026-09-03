---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/approxima-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://approxima.ai
- group: start
  title: ''
  type: Login
  url: https://approxima.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://approxima.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://approxima.ai/privacy
created: '2026-07-17'
description: 'Approxima is a Y Combinator (Winter 2026) startup building AI agents that test every pull request. Approxima plugs into your CI/CD pipeline and runs autonomous agents on each PR: the agents build your application in an isolated sandbox, exercise it in a real browser, and report exactly what is broken, with screenshots. The company positions itself as a trust layer for AI-assisted software development, letting engineering teams catch regressions and validate fixes end to end before code merges to production. As of this profile Approxima operates a marketing site and private login at approxima.ai and does not yet publish a public API, developer documentation, or an OpenAPI definition; this repo captures its identity and domain-security posture pending a public API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/approxima.png
layout: provider
modified: '2026-07-17'
name: Approxima
nav: Providers
network: true
overview: Approxima is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Development, AI Agents, Testing, and QA.
random_paper: 11
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/approxima/refs/heads/main/screenshots/approxima-2026-07-25T200845.png
security:
- kind: domain-security
  name: Approxima Domain Security
  slug: approxima-domain-security
  summary_line: TLSv1.3 · DMARC
slug: approxima
tags:
- Company
- Software Development
- AI Agents
- Testing
- QA
- CI/CD
- Pull Request
- Developer Tools
- Y Combinator
website: https://approxima.ai
---
