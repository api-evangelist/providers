---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.purplle.com/
- group: company
  title: ''
  type: About
  url: https://www.purplle.com/pr/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.purplle.com/magazine
- group: operate
  title: ''
  type: Support
  url: https://www.purplle.com/contactus
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.purplle.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purplle.com/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/purplle-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purplle-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Purplle is a direct-to-consumer beauty marketplace whose only machine-readable publication is a consumer-catalogue llms.txt; api.purplle.com answers HTTP 502 on every path, developer.purplle.com and docs.purplle.com do not resolve, and no OpenAPI, GraphQL, MCP or agent-card probe returned a contract on any host.
  evidence:
  - status: 200
    url: https://www.purplle.com/llms.txt
  - status: 502
    url: https://api.purplle.com/openapi.json
  - status: 247
    url: https://www.purplle.com/openapi.json
  - status: 247
    url: https://www.purplle.com/.well-known/agent-card.json
  - status: 0
    url: https://developer.purplle.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Purplle is an Indian beauty and personal care e-commerce marketplace headquartered in Mumbai, founded in 2012 by Manish Taneja, Rahul Dash, Suyash Katyayani and Anurag Neema. The platform sells skincare, makeup, haircare, fragrance, bath and body, grooming, mom and baby and wellness products across India, carrying a catalogue of 60,000+ products from 1,000+ brands alongside its own homegrown labels — Good Vibes, DERMDOC, Alps Goodness, NY Bae, FACES CANADA, Carmesi, Salm Skin and Juicy Chemistry. Purplle became an Indian unicorn in 2022 and is backed by ADIA, Kedaara, Premji Invest, Peak XV Partners, Goldman Sachs, Verlinvest, JSW Ventures and Blume Ventures. It operates a consumer website and mobile app plus 100+ offline stores, and publishes editorial guidance through Purplle Magazine. Purplle is a direct-to-consumer retailer: as of this profile it publishes no public developer program, API documentation, or machine-readable API contract. It does publish an llms.txt at its
  web root describing its catalogue for AI agents.'
image: https://media6.ppl-media.com/mediafiles/ecomm/promo/1728010486_purplle-logo.svg
layout: provider
modified: '2026-08-26'
name: Purplle
nav: Providers
network: true
overview: 'Purplle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Cosmetics, E-Commerce, and Retail.


  Purplle''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Purplle Plans Pricing
  plan_count: 0
  slug: purplle-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Purplle Rate Limits
  slug: purplle-rate-limits
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/purplle/refs/heads/main/screenshots/purplle-2026-09-02T152345.png
security:
- kind: domain-security
  name: Purplle Domain Security
  slug: purplle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: purplle
tags:
- Company
- Beauty
- Cosmetics
- E-Commerce
- Retail
- Marketplace
- Personal Care
- Consumer
- India
website: https://www.purplle.com/
---
