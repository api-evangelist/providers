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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chairish/refs/heads/main/hosts/chairish-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chairish-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chairish/refs/heads/main/vendors/chairish-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chairish-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.chairish.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chairish.com/pages/privacy-request
- group: company
  title: ''
  type: Blog
  url: https://www.chairish.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chairish/refs/heads/main/security/chairish-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chairish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chairish.com
coverage:
  checked: '2026-10-08'
  detail: No public developer documentation or API specification was found; attempts to fetch OpenAPI at https://api.chairish.com/openapi.json returned HTTP 410.
  evidence:
  - status: 410
    url: https://api.chairish.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Chairish is an online marketplace for buying and selling vintage and used furniture, decor, and art. It connects collectors and designers with curated, high-quality pieces, offering a curated shopping experience and a platform for sellers to consign items. The site features a wide range of categories including furniture, lighting, rugs, and accessories, emphasizing style and sustainability.
image: https://chairish-prod-static-images.freetls.fastly.net/logos/logo-1200-630.jpg
layout: provider
modified: '2026-10-07'
name: Chairish
nav: Providers
network: true
overview: 'Chairish is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Vintage, Furniture, E-Commerce, and Art.


  Chairish''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chairish Domain Security
  slug: chairish-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: chairish
tags:
- Marketplace
- Vintage
- Furniture
- E-Commerce
- Art
website: https://www.chairish.com
---
