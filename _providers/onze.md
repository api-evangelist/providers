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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.onze.com.br/
- group: company
  title: ''
  type: Blog
  url: https://www.onze.com.br/blog/
- group: start
  title: ''
  type: Login
  url: https://www.onze.com.br/painel/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onze.com.br/politica-de-privacidade
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onze.com.br/termos-de-uso-onze
created: '2026-07-17'
description: Onze is a Brazilian fintech (São Paulo) focused on corporate private pension (previdência privada) and financial health for companies and their employees. It offers digital management of employer-sponsored pension plans, access to more than 300 investment funds, one-on-one financial consultations with specialists, and financial-education seminars, all delivered as a B2B employee benefits platform. Onze positions itself as the first fintech centered on pension and financial wellness for a company's collaborators, and is backed by Ribbit Capital. This profile was added to the API Evangelist network as a portfolio-lead stub; as of this enrichment pass Onze publishes no public developer portal, API reference, or machine-readable API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onze.png
layout: provider
modified: '2026-07-20'
name: Onze
nav: Providers
network: true
overview: 'Onze is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Pension, Retirement, and Financial Health.


  Onze''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onze/refs/heads/main/screenshots/onze-2026-08-07T190434.png
security:
- kind: domain-security
  name: Onze Domain Security
  slug: onze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onze
tags:
- Company
- Fintech
- Pension
- Retirement
- Financial Health
- Employee Benefits
- Brazil
- Investments
website: https://www.onze.com.br/
---
