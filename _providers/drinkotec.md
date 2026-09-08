---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://drinkotec.ch/drinkotec-api/
  - plans/drinkotec-plans-pricing.yml
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-07'
api_count: 1
apis:
- description: The DRINKOTEC API is the integration surface for DRINKOTEC's connected beverage dispensing systems and its LOOP360 beverage productivity platform, used to expand DRINKOTEC functionality with third-par
  name: DRINKOTEC API
  slug: drinkotec
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drinkotec-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drinkotec-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://info.drinkotec.ch/en/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://info.drinkotec.ch/en/blog/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drinkotec
coverage:
  checked: '2026-09-06'
  detail: DRINKOTEC's own API page states that "a complete reference documentation is available and includes every endpoint, attribute and supported method", but publishes no link to it and no base URL — the page's only call to action is a "MEET OUR SOFTWARE ENGINEERS" button pointing at a form to book a visit or callback at the Nyon office, so the contract sits behind a sales conversation rather than a URL.
  evidence:
  - status: 503
    url: https://drinkotec.ch/drinkotec-api/
  - status: 200
    url: http://web.archive.org/web/20260419112516id_/https://drinkotec.ch/drinkotec-api/
  - status: 404
    url: https://api.drinkotec.ch/openapi.json
  - status: 404
    url: https://api.drinkotec.ch/.well-known/agent-card.json
  - status: 200
    url: https://info.drinkotec.ch/en/blog
  reason: sales-gate
  state: gated
created: '2025-03-01'
description: DRINKOTEC is a Swiss beverage technology company headquartered in Nyon, Vaud, that designs, builds and services connected beverage dispensing systems and the software that runs them. Its hardware line covers all-in-one and modern postmix dispensers (NEO, VISION PX), compact premix dispensing (DRAFTER), cocktails and blends (MANHATTAN), self-service walls, contactless payment (BEVPAY), beer and wine counting and control (LEVELUP, BEERMAX), automatic keg switching, cellar cooling monitoring and water fountains. LOOP360, its cloud beverage productivity and analytics platform, connects dispensed beverages to a central system and is marketed as integrating with ERP and CRM platforms. DRINKOTEC sells into breweries, bars, pubs, nightclubs, restaurants, hotels, festivals, sports arenas, cruise ships, offices, schools and healthcare, and markets a RESTful DRINKOTEC API for third-party integration whose reference documentation is not published publicly.
finops:
- name: Drinkotec Finops
  service_category: API
  slug: drinkotec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drinkotec.png
layout: provider
modified: '2026-09-06'
name: DRINKOTEC
nav: Providers
network: true
overview: 'DRINKOTEC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, Beverage Dispensing, Hospitality, Point of Sale, and IoT.


  DRINKOTEC''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Drinkotec Plans Pricing
  plan_count: 0
  slug: drinkotec-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Drinkotec Rate Limits
  slug: drinkotec-rate-limits
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/drinkotec/refs/heads/main/screenshots/drinkotec-2026-06-20T180234.png
security:
- kind: authentication
  name: Drinkotec Authentication
  slug: drinkotec-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Drinkotec Domain Security
  slug: drinkotec-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: drinkotec
tags:
- Beverages
- Beverage Dispensing
- Hospitality
- Point of Sale
- IoT
- Analytics
- Payments
---
