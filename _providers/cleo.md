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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleo-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleo-ai
- group: company
  title: ''
  type: Website
  url: https://web.meetcleo.com/
- group: company
  title: ''
  type: Blog
  url: https://web.meetcleo.com/blog
- group: operate
  title: ''
  type: Help Center
  url: https://web.meetcleo.com/help
- group: build
  title: ''
  type: GitHub
  url: https://github.com/meetcleo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://web.meetcleo.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://web.meetcleo.com/terms
created: '2025-03-01'
description: Cleo is an AI-powered personal finance assistant delivered through a chat interface in iOS and Android apps. The platform helps consumers budget, track spending across linked bank accounts, set savings goals, and access features such as Cleo Wallet (savings), Cleo Cover (cash advance), and Cleo Builder (credit-building). Cleo connects to user bank accounts using Plaid for read-only transaction access and does not currently publish a public, third-party developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleo.png
layout: provider
modified: '2026-04-26'
name: Cleo
nav: Providers
network: true
overview: 'Cleo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Banking, Budgeting, Cash Advance, and Consumer Finance.


  Cleo''s developer surface includes engineering blog, GitHub presence, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 3.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cleo/refs/heads/main/screenshots/cleo-2026-08-07T180001.png
security:
- kind: domain-security
  name: Cleo Domain Security
  slug: cleo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleo
tags:
- Artificial Intelligence
- Banking
- Budgeting
- Cash Advance
- Consumer Finance
- Financial Assistant
- Personal Finance
website: https://web.meetcleo.com/
---
