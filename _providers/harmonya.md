---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.harmonya.com/
- group: company
  title: ''
  type: Blog
  url: https://www.harmonya.com/perspectives
- group: operate
  title: ''
  type: Support
  url: mailto:support@harmonya.com
- group: start
  title: ''
  type: SignUp
  url: https://app.harmonya.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harmonya.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harmonya.com/legal/privacy-policy
- group: other
  title: ''
  type: OpenIDConnect
  url: authentication/harmonya-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmonya-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmonya-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/harmonya-plans-pricing.yml
coverage:
  checked: '2026-08-22'
  detail: 'Harmonya has a real programmatic surface — the app.harmonya.com tenant backend, protected by its own Auth0 tenant with a client_credentials grant enabled — but publishes no developer portal, reference or spec anywhere: api., docs., developer. and developers.harmonya.com are all NXDOMAIN, the 150-URL sitemap has no developer page, and every commercial path on the site ends at the /get-a-demo form.'
  evidence:
  - status: 200
    url: https://www.harmonya.com/sitemap.xml
  - status: 404
    url: https://www.harmonya.com/openapi.json
  - status: 404
    url: https://app.harmonya.com/openapi.json
  - status: 404
    url: https://www.harmonya.com/llms.txt
  - status: 404
    url: https://www.harmonya.com/.well-known/agent-card.json
  - status: 200
    url: https://harmonya.us.auth0.com/.well-known/openid-configuration
  - status: 200
    url: https://www.harmonya.com/get-a-demo
  reason: sales-gate
  state: gated
created: '2026-08-22'
description: Harmonya is a New York- and Tel Aviv-based product intelligence company for consumer packaged goods manufacturers and retailers. Founded in 2021, it reads live product listings, pack and label copy, manufacturer specs, syndicated feeds and consumer reviews, and turns them into normalized product attributes at the UPC level — claims, ingredients, flavors, pack, dietary positioning and measured nutrition values — plus demand themes and consumer-voice signals layered on top. The platform ships as four modules (Demand Intelligence, Consumer Intelligence, Attribute Intelligence and Product Catalog) delivered through a tenant web application at app.harmonya.com and as an enriched product feed into a customer's PIM, data lake and analytics stack. Harmonya publishes no public developer portal, API reference or machine-readable contract; access runs through a sales conversation and an Auth0-protected tenant.
image: https://cdn.prod.website-files.com/62399ef94090aecdfc702bde/62399ef94090ae5993702bfb_Harmonya_primaryLogo_256.png
layout: provider
modified: '2026-08-22'
name: Harmonya
nav: Providers
network: true
overview: 'Harmonya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Product Intelligence, Product Data, Data Enrichment, and Consumer Packaged Goods.


  Harmonya''s developer surface includes engineering blog, support, signup flow, and 7 more developer resources.'
plans:
- name: Harmonya Plans Pricing
  plan_count: 0
  slug: harmonya-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Harmonya Rate Limits
  slug: harmonya-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 8
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 13.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harmonya/refs/heads/main/screenshots/harmonya-2026-09-02T145705.png
security:
- kind: authentication
  name: Harmonya Authentication
  slug: harmonya-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Harmonya Domain Security
  slug: harmonya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harmonya
tags:
- Company
- Product Intelligence
- Product Data
- Data Enrichment
- Consumer Packaged Goods
- Retail
- Consumer Insights
- Retail Media
- Artificial Intelligence
website: https://www.harmonya.com/
---
