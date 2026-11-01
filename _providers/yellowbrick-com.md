---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Yellowbrick provides a data platform with APIs documented at https://docs.yellowbrick.com (no public OpenAPI spec found).
  name: Yellowbrick API
  slug: yellowbrick-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/yellowbrick-com/vendors/yellowbrick-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yellowbrick-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/yellowbrick-com/plans/yellowbrick-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yellowbrick-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/yellowbrick-com/llms/yellowbrick-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yellowbrick-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/yellowbrick-com/well-known/yellowbrick-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yellowbrick-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/yellowbrick-com/hosts/yellowbrick-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yellowbrick-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://community.yellowbrick.com/auth/v3/register?brand_id=8417595743891&return_to=null&locale=en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://yellowbrick.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://yellowbrick.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://yellowbrick.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yellowbrick.com/
- group: auth
  href: https://artifacts.apis.io/yellowbrick-com/security/yellowbrick-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yellowbrick-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yellowbrick.com
coverage:
  checked: '2026-10-22'
  detail: Docs site returns HTML and blocks OpenAPI spec access (403 on /openapi.json).
  evidence:
  - status: 403
    url: https://docs.yellowbrick.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: 'Yellowbrick Data is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by ivp, menlo-ventures, threshold-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://yellowbrick.com/wp-content/uploads/2025/04/yellowbrick_og_image_default_1200x630.png
layout: provider
modified: '2026-10-22'
name: Yellowbrick Data
nav: Providers
network: true
overview: 'Yellowbrick Data is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Warehouse, Enterprise Analytics, SQL Platform, Streaming Analytics, and Data Residency.


  Yellowbrick Data''s developer surface includes signup flow, pricing, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Yellowbrick Com Plans Pricing
  plan_count: 3
  slug: yellowbrick-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yellowbrick Com Domain Security
  slug: yellowbrick-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yellowbrick-com
tags:
- Data Warehouse
- Enterprise Analytics
- SQL Platform
- Streaming Analytics
- Data Residency
- Cloud Data
website: https://yellowbrick.com
---
