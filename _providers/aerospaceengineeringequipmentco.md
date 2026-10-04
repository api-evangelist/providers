---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Aerospace Engineering Equipment website at a-fsw.com: the route index of the site''s content management system, catalogued as one site surface rather than'
  name: Aerospace Engineering Equipment Website (WordPress REST)
  slug: a-fsw-com-website-wordpress-rest
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/security/aerospaceengineeringequipmentco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerospaceengineeringequipmentco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a-fsw.com/
- group: operate
  title: ''
  type: Support
  url: https://a-fsw.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://a-fsw.com/category/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a-fsw.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/authentication/aerospaceengineeringequipmentco-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aerospaceengineeringequipmentco-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/conventions/aerospaceengineeringequipmentco-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aerospaceengineeringequipmentco-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/errors/aerospaceengineeringequipmentco-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aerospaceengineeringequipmentco-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/lifecycle/aerospaceengineeringequipmentco-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aerospaceengineeringequipmentco-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/conformance/aerospaceengineeringequipmentco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aerospaceengineeringequipmentco-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/data-model/aerospaceengineeringequipmentco-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aerospaceengineeringequipmentco-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/llms/aerospaceengineeringequipmentco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerospaceengineeringequipmentco-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/packages/aerospaceengineeringequipmentco-packages.yml
  title: ''
  type: Packages
  url: packages/aerospaceengineeringequipmentco-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/plans/aerospaceengineeringequipmentco-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aerospaceengineeringequipmentco-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/rate-limits/aerospaceengineeringequipmentco-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aerospaceengineeringequipmentco-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerospaceengineeringequipmentco/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-10'
description: Aerospace Engineering Equipment (Suzhou) Co., Ltd. — trading as AEE — is a Chinese industrial equipment manufacturer founded in December 2011 that designs, builds and integrates friction stir welding (FSW) machines, automatic FSW production lines and FSW tooling. It is a wholly owned subsidiary of Shanghai Aerospace Equipment Manufacturing Factory (149 Factory) under the Eighth Academy of the China Aerospace Science and Technology Corporation (CASC), operating an R&D headquarters in Wuzhong District, Suzhou and a volume production base in Liyang across roughly 55,000 square metres. AEE supplies one-, two- and three-dimensional FSW equipment plus process services into aerospace and aviation, rail transit, marine and shipbuilding, new-energy automotive, nuclear, power electronics and marine engineering. AEE publishes no developer program, no API documentation and no machine-readable specification; the surfaces profiled here are the anonymously readable WordPress REST content APIs
  served from its English-language marketing site at a-fsw.com, documented by API Evangelist from the server's own route index and OPTIONS schema documents.
image: https://a-fsw.com/wp-content/uploads/2026/05/cropped-ioc.png
layout: provider
modified: '2026-09-10'
name: Aerospace Engineering Equipment
nav: Providers
network: true
overview: 'Aerospace Engineering Equipment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Industrial Equipment, Welding, and Friction Stir Welding.


  Aerospace Engineering Equipment''s developer surface includes support, engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Aerospaceengineeringequipmentco Plans Pricing
  plan_count: 0
  slug: aerospaceengineeringequipmentco-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aerospaceengineeringequipmentco Rate Limits
  slug: aerospaceengineeringequipmentco-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 16.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Aerospaceengineeringequipmentco Authentication
  slug: aerospaceengineeringequipmentco-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aerospaceengineeringequipmentco Domain Security
  slug: aerospaceengineeringequipmentco-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aerospaceengineeringequipmentco
tags:
- Company
- Manufacturing
- Industrial Equipment
- Welding
- Friction Stir Welding
- Aerospace
- Rail Transit
- Automotive
- Shipbuilding
- Content
- China
website: https://a-fsw.com/
---
