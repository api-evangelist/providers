---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Alkami's RESTful digital-banking APIs (D2C, B2B, and Open Banking) plus the Alkami SDK, built on OpenID Connect and documented in the gated Alkami DevPortal.
  name: Alkami Digital Banking API
  slug: alkami-digital-banking-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.alkami.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.alkami.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.alkami.com/build-with-us/developers/
- group: company
  title: ''
  type: Blog
  url: https://www.alkami.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.alkami.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alkami.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alkami
- group: auth
  title: ''
  type: Authentication
  url: authentication/alkami-authentication.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/alkami-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alkami-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alkami-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.alkami.com/tools/Vulnerability-Disclosure.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alkami-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alkami-llms.txt
created: '2026-07-17'
description: 'Alkami Technology (NASDAQ: ALKT) is a Plano, Texas based cloud digital banking platform for U.S. banks and credit unions. Through its "Alkami Foundry" developer program it exposes RESTful APIs and an extensible SDK — spanning authentication, money movement, data access, and real-time and batch workflows — that financial institutions and fintech partners use to embed and extend digital-banking experiences. The APIs are grouped into D2C (embed fintech experiences), B2B (automate backend workflows), and Open Banking (third-party connections such as Plaid) surfaces, are built on OpenID Connect, and are delivered through a gated DevPortal rather than an open public API. Alkami was surfaced as a portfolio company of D1 Capital and enriched by the API Evangelist pipeline from its public developer, security, and legal surfaces.'
image: https://www.alkami.com/wp-content/uploads/2023/01/alkami-logo.svg
layout: provider
modified: '2026-07-17'
name: Alkami
nav: Providers
network: true
overview: 'Alkami publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Digital Banking, Banking, and Credit Unions.


  Alkami''s developer surface includes documentation, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alkami/refs/heads/main/screenshots/alkami-2026-07-25T195627.png
security:
- kind: authentication
  name: Alkami Authentication
  slug: alkami-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Alkami Domain Security
  slug: alkami-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Alkami Vulnerability Disclosure
  slug: alkami-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: alkami
tags:
- Company
- Fintech
- Digital Banking
- Banking
- Credit Unions
- Financial-Services
- Open Banking
- SDK
website: https://www.alkami.com
---
