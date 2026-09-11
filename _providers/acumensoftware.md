---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-10'
api_count: 3
apis:
- description: Authenticated REST surface behind the Forcelink mobile field-service ERP, served from the vendor-hosted za2.forcelink.net tenant alongside the Forcelink web login and the Forcelink Android/iOS apps. E
  name: Forcelink REST API
  slug: forcelink-rest-api
- description: Authenticated REST surface consumed by the My Smart City citizen web app at app.mysmart.city. The web client's own JavaScript bundle names the base path /api/msc/rest/smartcitymanager/, and the same o
  name: My Smart City REST API
  slug: my-smart-city-rest-api
- description: Anonymous, remote MCP endpoint served on each of the three Acumen Software marketing domains. It is the Wix platform's Site MCP, not a first-party Acumen or Forcelink product API — the nine tools it r
  name: Acumen Software Site MCP
  slug: acumen-software-site-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.acumensoft.net/
- group: operate
  title: ''
  type: Support
  url: https://www.acumensoft.net/contact
- group: company
  title: ''
  type: Blog
  url: https://www.forcelink.net/news-forcelink
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forcelink.net/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mysmart.city/termsandconditions
- group: start
  title: ''
  type: Login
  url: https://za2.forcelink.net/forcelink/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acumensoftware-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acumensoftware-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acumensoftware-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/acumensoftware-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acumensoftware-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/acumensoftware-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acumensoftware-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acumensoftware-rate-limits.yml
created: '2026-09-06'
description: Acumen Software is a Johannesburg, South Africa software company founded in 2006 that builds highly configurable mobile SaaS for work, workforce and asset management. Its flagship product Forcelink is a mobile field-service ERP covering work management, workforce scheduling, asset and materials management, fleet, project, facilities, CRM and outage management (Powerlink) for power and water utilities, telecoms, transport, healthcare, forestry, mining, roads, waste, local government and municipal councils. A second product line, My Smart City, is a citizen-engagement platform that lets residents log municipal service faults, book vetted service providers, submit self-meter readings and pay municipal accounts, running on the same Forcelink back end. Both products are delivered as hosted multi-tenant web and mobile apps; the underlying REST surfaces are authenticated tenant APIs with no public developer program or published contract.
image: https://static.wixstatic.com/media/f3eb90_393c3a2fe853418ba367c5553bf6f8cc~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: Acumen Software Site MCP
  slug: acumen-software-site-mcp
- description: ''
  name: Acumen Software MCP Server
  slug: acumen-software-mcp-server
modified: '2026-09-06'
name: Acumen Software
nav: Providers
network: true
overview: 'Acumen Software publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Field Service Management, Workforce Management, Asset Management, Enterprise Resource Planning, and Smart Cities.


  Acumen Software''s developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Acumensoftware Plans Pricing
  plan_count: 0
  slug: acumensoftware-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Acumensoftware Rate Limits
  slug: acumensoftware-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 20.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acumensoftware Domain Security
  slug: acumensoftware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acumensoftware
tags:
- Field Service Management
- Workforce Management
- Asset Management
- Enterprise Resource Planning
- Smart Cities
- Local Government
- Utilities
- Mobile
- South Africa
- MCP
website: https://www.acumensoft.net/
---
