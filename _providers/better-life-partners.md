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
- group: company
  title: ''
  type: Website
  url: https://betterlifepartners.com/
- group: company
  title: ''
  type: Blog
  url: https://betterlifepartners.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://betterlifepartners.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://betterlifepartners.com/get-in-touch/
- group: operate
  title: ''
  type: Contact
  url: https://betterlifepartners.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://betterlifepartners.com/faqs/
- group: commercial
  title: ''
  type: Pricing
  url: https://betterlifepartners.com/how-much/
- group: start
  title: ''
  type: SignUp
  url: https://betterlifepartners.com/get-started/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterlifepartners.com/privacy-policy/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://betterlifepartners.com/resources/
- group: company
  title: ''
  type: Partners
  url: https://betterlifepartners.com/partners/
- group: company
  title: ''
  type: Careers
  url: https://betterlifepartners.com/careers/
- group: other
  title: ''
  type: Team
  url: https://betterlifepartners.com/leadership-team/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/better-life-partners/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/better-life-partners_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/better-life-partners-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/better-life-partners-llms.txt
coverage:
  checked: '2026-08-07'
  detail: Better Life Partners is a clinical addiction-treatment provider running virtual and in-person MAT clinics in five states; its entire public surface is a WordPress marketing site whose only machine-readable route is the WordPress /wp-json/ CMS API, and no api./developer./docs. host exists in DNS at all.
  evidence:
  - status: 200
    url: https://betterlifepartners.com/
  - status: 0
    url: https://api.betterlifepartners.com/
  - status: 0
    url: https://docs.betterlifepartners.com/
  - status: 404
    url: https://betterlifepartners.com/openapi.json
  - status: 404
    url: https://betterlifepartners.com/llms.txt
  - status: 404
    url: https://betterlifepartners.com/.well-known/security.txt
  - status: 404
    url: https://betterlifepartners.com/.well-known/agent-card.json
  - status: 404
    url: https://betterlifepartners.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: 'Better Life Partners is a Hanover, New Hampshire healthcare provider founded in 2018 that delivers same-day, whole-person treatment for opioid and alcohol use disorder across New Hampshire, Maine, Massachusetts, Vermont and North Carolina. It combines FDA-approved medication for addiction treatment (buprenorphine/Suboxone, naltrexone) with group counseling, peer recovery coaching and mental health care, delivered both virtually and in person, on a non-punitive harm-reduction model. The company contracts directly with Medicaid, Medicare and commercial health plans — MaineCare, NH Healthy Families, Anthem, Cigna, Harvard Pilgrim, Tufts, Humana and UnitedHealthcare — and markets value-based arrangements "from bundles to full risk" to payers and community partners. It is a clinical services organization rather than a software vendor: it references "purpose-built technology" internally but publishes no developer program, API, specification, SDK or integration documentation of any
  kind.'
image: https://betterlifepartners.com/wp-content/uploads/2026/07/logo-menu.svg
layout: provider
modified: '2026-08-07'
name: Better Life Partners
nav: Providers
network: true
overview: 'Better Life Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Behavioral Health, Addiction Treatment, and Substance Use Disorder.


  Better Life Partners'' developer surface includes engineering blog, support, FAQ, pricing, signup flow, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/better-life-partners/refs/heads/main/screenshots/better-life-partners-2026-08-07T162335.png
security:
- kind: domain-security
  name: Better Life Partners Domain Security
  slug: better-life-partners-domain-security
  summary_line: TLSv1.3 · DMARC
slug: better-life-partners
tags:
- Company
- Healthcare
- Behavioral Health
- Addiction Treatment
- Substance Use Disorder
- Telehealth
- Mental Health
- Value-Based Care
- Health Plans
website: https://betterlifepartners.com/
---
