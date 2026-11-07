---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/masabi/llms/masabi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/masabi-llms.txt
- group: other
  href: https://artifacts.apis.io/masabi/hosts/masabi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/masabi-hosts.yml
- group: other
  href: https://artifacts.apis.io/masabi/vendors/masabi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/masabi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.masabi.com/policies/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.masabi.com/
- group: auth
  title: ''
  type: Security
  url: https://www.masabi.com/policies/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.masabi.com/policies/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.masabi.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.masabi.com/company/blog/
- group: auth
  href: https://artifacts.apis.io/masabi/security/masabi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/masabi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.masabi.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.masabi.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Masabi provides a SaaS platform for transit agencies to enable mobile ticketing, account‑based ticketing, open payments and fare management. Their Justride platform powers fare collection for 400+ agencies worldwide, handling billions in fare revenue and offering APIs for integration with third‑party apps, validators and reporting tools. The company focuses on rider engagement, revenue protection and multi‑operator scalability, delivering cloud‑native solutions across many regions.
image: https://www.masabi.com/wp-content/uploads/2022/02/Passenger-Social-Intro-Graphic.jpg
layout: provider
modified: '2026-10-13'
name: Masabi
nav: Providers
network: true
overview: 'Masabi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transit, Software-as-a-Service, MobileTicketing, and OpenPayments.


  Masabi''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.3
    operational_transparency: 13.2
  previous_composite: 13.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/masabi/masabi-2026-11-03T135346.png
security:
- kind: domain-security
  name: Masabi Domain Security
  slug: masabi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: masabi
tags:
- Company
- Transit
- Software-as-a-Service
- MobileTicketing
- OpenPayments
website: https://www.masabi.com
---
