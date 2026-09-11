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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-10'
api_count: 3
apis:
- baseURL: https://a-fsw.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the AEE friction stir welding product catalogue — 18 published machines, production lines and tools across 6 product categories — via the WordPress core REST API
  name: AEE Products API
  slug: aee-products-api
- baseURL: https://a-fsw.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the AEE news and technical blog archive (50 posts) and the 14 static marketing, process, industry and policy pages behind a-fsw.com, via the WordPress core REST '
  name: AEE Content API
  slug: aee-content-api
- baseURL: https://a-fsw.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the site-wide index surfaces behind a-fsw.com — cross-content search, the 232-item media library of equipment photography and diagrams, and the content-type and '
  name: AEE Site Index API
  slug: aee-site-api
artifact_total: 7
common:
- group: auth
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
  title: ''
  type: Authentication
  url: authentication/aerospaceengineeringequipmentco-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aerospaceengineeringequipmentco-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aerospaceengineeringequipmentco-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aerospaceengineeringequipmentco-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aerospaceengineeringequipmentco-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aerospaceengineeringequipmentco-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aerospaceengineeringequipmentco-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/aerospaceengineeringequipmentco-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aerospaceengineeringequipmentco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aerospaceengineeringequipmentco-rate-limits.yml
- group: agent
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
overview: 'Aerospace Engineering Equipment publishes 3 APIs on the [APIs.io](https://apis.io/) network: AEE Products API, AEE Content API, and AEE Site Index API. Tagged areas include Company, Manufacturing, Industrial Equipment, Welding, and Friction Stir Welding.


  Aerospace Engineering Equipment''s developer surface includes support, engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Aerospaceengineeringequipmentco Plans Pricing
  plan_count: 0
  slug: aerospaceengineeringequipmentco-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aerospaceengineeringequipmentco Rate Limits
  slug: aerospaceengineeringequipmentco-rate-limits
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 13.3
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
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
