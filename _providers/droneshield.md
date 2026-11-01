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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DroneSentry-C2 is DroneShield's command-and-control platform for counter-UAS sensors and effectors (on-premises or cloud). The product page states that a RESTful API allows easy deployment into existi
  name: DroneShield DroneSentry-C2 API
  slug: dronesentry-c2-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/droneshield/conformance/droneshield-conformance.yml
  title: ''
  type: Conformance
  url: conformance/droneshield-conformance.yml
- group: other
  href: https://artifacts.apis.io/droneshield/hosts/droneshield-hosts.yml
  title: ''
  type: Hosts
  url: hosts/droneshield-hosts.yml
- group: build
  href: https://artifacts.apis.io/droneshield/integrations/droneshield-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/droneshield-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/droneshield/vendors/droneshield-vendors.yml
  title: ''
  type: Vendors
  url: vendors/droneshield-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.droneshield.com/blog/tag/Security
- group: auth
  href: https://artifacts.apis.io/droneshield/security/droneshield-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/droneshield-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.droneshield.com/
- group: company
  title: ''
  type: About
  url: https://www.droneshield.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.droneshield.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.droneshield.com/media/news
- group: operate
  title: ''
  type: Support
  url: https://www.droneshield.com/product-support-form
- group: operate
  title: ''
  type: Contact
  url: https://www.droneshield.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.droneshield.com/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.droneshield.com/investor-relations
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/droneshield
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.droneshield.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.droneshield.com/terms-of-access
coverage:
  checked: '2026-10-21'
  detail: DroneShield's products-software page says DroneSentry-C2 has a RESTful API, but publishes no reference or contract; technical resources are delivered only to customers through the DroneShield Access Portal, and no OpenAPI/AsyncAPI/GraphQL/MCP was found on droneshield.com, www.droneshield.com or api.droneshield.com.
  evidence:
  - status: 200
    url: https://www.droneshield.com/products-software
  - status: 200
    url: https://www.droneshield.com/
  reason: customer-only-docs
  state: gated
created: '2026-10-21'
description: 'DroneShield (ASX:DRO) is a counter-drone technology company that describes itself as the global leader in AI-powered CUxS (counter-uncrewed systems), delivering counter-drone solutions for every mission with customer-first design and advanced threat detection. Its public website covers products, product support, investor relations, news and careers; no public developer API, API documentation or developer portal is published on droneshield.com. Originally surfaced via the API Evangelist harvest backlog (source: australia-apidays-2026).'
image: https://static1.squarespace.com/static/660a32624c94dd36e509baf3/t/6ab11e62685fd269d5e6a9d7/1789992546829/SocialSharing_1200x630.jpg?format=1500w
layout: provider
modified: '2026-10-21'
name: DroneShield
nav: Providers
network: true
overview: 'DroneShield is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Counter-Drone, Defense, Drones, and Artificial Intelligence.


  DroneShield''s developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Droneshield Plans Pricing
  plan_count: 0
  slug: droneshield-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Droneshield Rate Limits
  slug: droneshield-rate-limits
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 10.5
  previous_composite: 15.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Droneshield Domain Security
  slug: droneshield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: droneshield
tags:
- Company
- Counter-Drone
- Defense
- Drones
- Artificial Intelligence
- Security
- ASX Listed
website: https://www.droneshield.com/
---
