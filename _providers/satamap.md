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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/satamap/hosts/satamap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/satamap-hosts.yml
- group: other
  href: https://artifacts.apis.io/satamap/vendors/satamap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/satamap-vendors.yml
- group: auth
  href: https://artifacts.apis.io/satamap/security/satamap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/satamap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.satamap.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.satamap.com.au/satamap
- group: start
  title: ''
  type: GettingStarted
  url: https://www.satamap.com.au/satamap
- group: operate
  title: ''
  type: Support
  url: https://www.satamap.com.au/contact
- group: company
  title: ''
  type: Blog
  url: https://www.satamap.com.au/case-studies
- group: commercial
  title: ''
  type: Pricing
  url: https://www.satamap.com.au/cart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.satamap.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.satamap.com.au/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://global.satamap.com.au/login/_
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at common spec locations on the provider's hosts.
  evidence:
  - status: 200
    url: https://global.satamap.com.au/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Satamap provides high-quality, consistent satellite imagery to enhance agricultural operations, offering frequent updates, world-leading biomass imagery, and vegetative index tools for crop growth measurement, yield prediction, and field scouting. Subscriptions are area‑based, sourcing data from Landsat 8, Sentinel‑2, MODIS and archived missions, updated every five days under cloud‑free conditions.
image: https://images.squarespace-cdn.com/content/v1/67ad6b2849484d0a42d4afc5/fdd57a45-c64d-46f3-a420-2919a04cf9b3/Untitled+design+%281%29.png
layout: provider
modified: '2026-10-28'
name: Satamap
nav: Providers
network: true
overview: 'Satamap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite, Imagery, Agriculture, Remote Sensing, and SaaS.


  Satamap''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 6 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Satamap Domain Security
  slug: satamap-domain-security
  summary_line: TLSv1.3 · HSTS
slug: satamap
tags:
- Satellite
- Imagery
- Agriculture
- Remote Sensing
- SaaS
website: https://www.satamap.com.au/
---
