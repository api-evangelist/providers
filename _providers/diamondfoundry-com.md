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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/diamondfoundry-com/hosts/diamondfoundry-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diamondfoundry-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/diamondfoundry-com/vendors/diamondfoundry-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diamondfoundry-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.df.com/insights-categories/media
- group: auth
  href: https://artifacts.apis.io/diamondfoundry-com/security/diamondfoundry-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diamondfoundry-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diamondfoundry.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.df.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.df.com/insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.df.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.df.com/contact
coverage:
  checked: '2026-10-23'
  detail: The provider's website and docs are HTML pages without any published OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.df.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Diamond Foundry creates lab-grown diamonds using proprietary technology that produces high-quality single-crystal diamond wafers for industrial and consumer applications. The company focuses on sustainable manufacturing, reducing the environmental impact compared to traditional mining, and offers products for electronics, optics, and jewelry markets. Founded with backing from obvious-ventures, Diamond Foundry aims to shape the future of materials science through innovative diamond production.
image: https://cdn.prod.website-files.com/6a96e5c74cce21a226992e29/6ac00c59fff6a4c32add55dd_OpenGraph.jpg
layout: provider
modified: '2026-10-22'
name: Diamond Foundry
nav: Providers
network: true
overview: 'Diamond Foundry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diamond, Manufacturing, Materials, and Technology.


  Diamond Foundry''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diamondfoundry Com Domain Security
  slug: diamondfoundry-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diamondfoundry-com
tags:
- Company
- Diamond
- Manufacturing
- Materials
- Technology
- Sustainable
website: https://diamondfoundry.com
---
