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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getsafe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hellogetsafe.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hellogetsafe.com/en-de/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getsafe
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellogetsafe.com/en-de/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellogetsafe.com/en-de/data-protection
- group: start
  title: ''
  type: Login
  url: https://link.hellogetsafe.com/home
created: '2026-07-17'
description: Getsafe (Getsafe Digital GmbH) is a Heidelberg, Germany-based digital insurance company (insurtech) that lets consumers buy, manage, and file claims for insurance entirely through a mobile app. Getsafe operates as a licensed insurance carrier and offers 15+ products across liability and legal protection, health (public, private, dental, and travel), living (contents and drone), pet (pet health and dog liability), and protection and finance (income protection, term life, private pension, and children's savings). It serves 500k+ customers in Germany and Austria with English-language, app-based support. In 2018 Getsafe launched an early-access P&C and health insurance API and embeddable widget for partner distribution; that partner API is no longer offered as a public self-service developer program, so this profile is maintained as a company record. Backed by earlybird and partech.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getsafe.png
layout: provider
modified: '2026-07-19'
name: Getsafe
nav: Providers
network: true
overview: 'Getsafe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Insurance, Digital Insurance, and Financial-Services.


  Getsafe''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.4
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getsafe/refs/heads/main/screenshots/getsafe-2026-07-25T215742.png
security:
- kind: domain-security
  name: Getsafe Domain Security
  slug: getsafe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getsafe
tags:
- Company
- Insurtech
- Insurance
- Digital Insurance
- Financial-Services
- Germany
- Mobile App
- Embedded Insurance
website: https://www.hellogetsafe.com/
---
