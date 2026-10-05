---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Beautyhaul e‑commerce platform
  name: Beautyhaul API
  slug: beautyhaul-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beautyhaul/refs/heads/main/hosts/beautyhaul-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beautyhaul-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.beautyhaul.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beautyhaul/refs/heads/main/security/beautyhaul-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beautyhaul-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beautyhaul.com
- group: company
  title: ''
  type: Blog
  url: https://www.beautyhaul.com/blog
coverage:
  checked: '2026-09-27'
  detail: OpenAPI spec endpoints returned empty responses, no machine‑readable contract found
  evidence:
  - status: 200
    url: https://api.beautyhaul.com/openapi.json
  - status: 200
    url: https://api.beautyhaul.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Beautyhaul is an Indonesian e‑commerce platform specializing in beauty products, offering a wide range of makeup, skincare, fragrance and personal care items. The site emphasizes original, BPOM‑approved products with discounts up to 50% off, catering to both local and multinational brands. It provides online shopping, store pick‑up, and detailed product information, aiming to solve skin concerns and deliver affordable beauty solutions.
image: https://cdn.beautyhaul.com/assets/uploads/thumbs/Main_Banner_GACOR_Sep_PIi.__2880.png
layout: provider
modified: '2026-09-27'
name: Beautyhaul
nav: Providers
network: true
overview: 'Beautyhaul publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Beauty, Indonesia, Cosmetics, and Online Shopping.


  Beautyhaul''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beautyhaul Domain Security
  slug: beautyhaul-domain-security
  summary_line: TLSv1.3
slug: beautyhaul
tags:
- E-Commerce
- Beauty
- Indonesia
- Cosmetics
- Online Shopping
website: https://www.beautyhaul.com
---
