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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Erebor's developer API for programmatic access to banking, money-movement, and stablecoin operations. The gateway at api.erebor.bank authenticates requests with an API key and returns a structured JSO
  name: Erebor API
  slug: erebor-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erebor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://erebor.bank
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.erebor.bank
- group: docs
  title: ''
  type: Documentation
  url: https://docs.erebor.bank
- group: docs
  title: ''
  type: APIReference
  url: https://docs.erebor.bank
- group: start
  title: ''
  type: SignUp
  url: https://erebor.bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://erebor.bank/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://erebor.bank/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/erebor-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/erebor-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/erebor-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/erebor-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/erebor-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/erebor-llms.txt
created: '2026-07-17'
description: Erebor is a digital-first, FDIC-insured national bank built for the innovation economy — technology startups, cryptocurrency and stablecoin businesses, and AI and defense companies that traditional banks have historically underserved. Co-founded by Palmer Luckey (Anduril) and Joe Lonsdale (8VC) and backed by Founders Fund, Lux Capital, Haun Ventures, and 8VC, Erebor received OCC preliminary conditional approval in October 2025, FDIC deposit-insurance approval in December 2025, and launched in February 2026. It offers deposit accounts, wires and money movement, and stablecoin operations. Erebor exposes a developer API at api.erebor.bank secured with API keys, an Auth0-authenticated developer dashboard at developer.erebor.bank, and Fern-based developer documentation at docs.erebor.bank. The public developer docs are login-gated, so the machine-readable surface captured here is limited to what is observable without credentials.
image: https://erebor.bank/apple-touch-icon.png
layout: provider
modified: '2026-07-19'
name: Erebor
nav: Providers
network: true
overview: 'Erebor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Digital Bank, and Stablecoins.


  Erebor''s developer surface includes documentation, API reference, signup flow, authentication, sandbox, and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erebor/refs/heads/main/screenshots/erebor-2026-07-25T213607.png
security:
- kind: authentication
  name: Erebor Authentication
  slug: erebor-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Erebor Domain Security
  slug: erebor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: erebor
tags:
- Company
- Fintech
- Banking
- Digital Bank
- Stablecoins
- Cryptocurrency
- Payments
- Financial-Services
website: https://erebor.bank
---
