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
  url: security/onlia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.onlia.ca/
- group: company
  title: ''
  type: About
  url: https://www.onlia.ca/about
- group: company
  title: ''
  type: Blog
  url: https://www.onlia.ca/magazine/blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://www.onlia.ca/magazine/blogs?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.onlia.ca/support
- group: other
  title: ''
  type: Claims
  url: https://www.onlia.ca/claims
- group: start
  title: ''
  type: Portal
  url: https://app.onlia.ca/
- group: company
  title: ''
  type: Partners
  url: https://www.onlia.ca/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onlia.ca/about/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onlia.ca/about/conditions-of-use
- group: auth
  title: ''
  type: Disclosure
  url: https://www.onlia.ca/broker-disclosure
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.onlia.ca/faqs
- group: other
  title: ''
  type: Accessibility
  url: https://www.onlia.ca/about/accessibility
- group: commercial
  title: ''
  type: PaymentAgreement
  url: https://www.onlia.ca/payment-agreement
- group: other
  title: ''
  type: FraudReporting
  url: https://www.onlia.ca/help/report-fraud
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/onlia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onlia-llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'Onlia is a Canadian digital insurance brokerage, operating as the registered business name of Onlia Agency Inc. and backed by Southampton Financial Inc. (the Southampton group of companies). It sells personal lines direct to consumers online and by phone — auto (car, motorcycle, ATV, snowmobile, trailer, motorhome), property (home, condo, tenant, landlord, second home, mobile home) and lifestyle lines (boat, pet, life, travel, seasonal) — plus group and bundle programs. Onlia does not underwrite; it places business with a panel of Canadian carriers disclosed publicly on its broker-disclosure page, including Aviva, Gore Mutual, Economical/Definity, Pembridge, Pafco, Echelon, Wawanesa, Unica, Forward, Premier, Facility Association (Intact) and APOLLO. Its home market is Canada, concentrated in Ontario, where market conduct sits with FSRA while OSFI supervises the federally-regulated carriers behind the policies. API posture, recorded honestly: Onlia publishes NO public developer
  portal and NO self-serve API. developer., developers., docs. and api. under onlia.ca do not resolve, and /developers, /api, /developer and /integrations on the marketing site all return 404. The only quote/bind/issue/FNOL surface is app.onlia.ca, a consumer-facing Angular single-page app running on a white-labelled Ignite Insurance policy administration platform whose backend is private to the app. The one "partner" page is a B2B marketing page inviting affinity discount partnerships by email, with no technical onboarding. No ACORD, AL3, ACORD XML or NGDS reference appears anywhere on the public site. The app''s own bundle shows the private backend runs on MuleSoft Anypoint CloudHub ESB services (auto and home policy, authentication, documents, VIN/MVR, claims) plus an Ignite Insurance authentication service — real REST plumbing behind the SPA, but undocumented, uncredentialed and not offered to third parties, so no API entry is claimed here.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Onlia
nav: Providers
network: true
overview: 'Onlia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Insurtech, and Brokers.


  Onlia''s developer surface includes engineering blog, support, developer portal, and 16 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onlia/refs/heads/main/screenshots/onlia-2026-08-07T190358.png
security:
- kind: domain-security
  name: Onlia Domain Security
  slug: onlia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onlia
tags:
- Insurance
- Canada
- Property and Casualty
- Insurtech
- Brokers
- Personal Lines
- Auto Insurance
- Home Insurance
- Direct to Consumer
- Ontario
website: https://www.onlia.ca/
---
