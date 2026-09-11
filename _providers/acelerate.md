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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acelerate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acelerate.io/
- group: start
  title: ''
  type: SignUp
  url: https://app.acelerate.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.acelerate.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.acelerate.io/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acelerate
coverage:
  checked: '2026-09-06'
  detail: 'Acelerate ships an end-user restaurant purchasing and virtual-brand SaaS and nothing else: its entire public web presence is the authenticated app at app.acelerate.io, whose own production route manifest has no developer, docs or API-reference route, its retired marketing site never carried one, npm and PyPI hold no first-party package, and every /.well-known/ discovery path returns a true 404.'
  evidence:
  - status: 301
    url: https://acelerate.io/
  - status: 404
    url: https://app.acelerate.io/.well-known/api-catalog
  - status: 404
    url: https://app.acelerate.io/.well-known/agent-card.json
  - status: 404
    url: https://app.acelerate.io/llms.txt
  - status: 403
    url: https://app.acelerate.io/api/v1/openapi.json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=acelerate
  - status: 200
    url: https://api.github.com/users/acelerate
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: Acelerate (acelerate.io) is a Santa Monica, California restaurant technology company founded in 2019 by former DoorDash operator George Jacobs. It launched as a virtual-brand and host-kitchen platform that let existing restaurants run additional delivery-only brands out of their idle kitchen capacity, and raised a USD 14.44M Series A led by Sequoia Capital in July 2021. The product has since moved up the restaurant supply chain -- the production application at app.acelerate.io covers purchasing from distributors, invoices and rebates, supplier offers, a menu manager, an order manager, sales storefronts, payments and bank accounts. Acelerate publishes no public developer program - no developer portal, API reference, OpenAPI or other machine-readable contract, SDK, webhook catalog or MCP server - and the marketing site that once carried its brand and customer pages has been retired, with acelerate.io now redirecting straight into the authenticated application.
image: https://app.acelerate.io/pwa-icons/192.png
layout: provider
modified: '2026-09-06'
name: Acelerate
nav: Providers
network: true
overview: 'Acelerate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Restaurant Technology, Food Service, Hospitality, and Ghost Kitchens.


  Acelerate''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.7
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acelerate Domain Security
  slug: acelerate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acelerate
tags:
- Restaurants
- Restaurant Technology
- Food Service
- Hospitality
- Ghost Kitchens
- Supply Chain
- Procurement
- Foodservice Distribution
- SaaS
- United States
- Company
website: https://acelerate.io/
---
