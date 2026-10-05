---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: GraphQL API for Barnana offering product and order data.
  name: Barnana GraphQL API
  slug: barnana-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barnana/refs/heads/main/llms/barnana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barnana-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barnana/refs/heads/main/well-known/barnana-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barnana-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barnana/refs/heads/main/hosts/barnana-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barnana-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barnana/refs/heads/main/vendors/barnana-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barnana-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barnana.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://barnana.com/blogs/press
- group: company
  title: ''
  type: Blog
  url: https://barnana.com/blogs/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barnana/refs/heads/main/security/barnana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barnana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barnana.com
created: '2026-09-27'
description: Barnana is a snack food company that creates plant‑based, organic banana, plantain, and cassava chips and bites. Founded with a mission to reduce food waste, the brand sources imperfect bananas and turns them into tasty, sustainably‑packaged snacks. Their product line includes organic plantain chips, cassava chips, banana bites, and seasonal flavors, sold online and in retail stores across the United States.
image: http://barnana.com/cdn/shop/files/WEB-barnana---regenerative-pink-salt-Upscaled_eb511714-ef7a-4cda-9f41-94bc5da5dddb.jpg?v=1769208583
layout: provider
modified: '2026-09-27'
name: Barnana
nav: Providers
network: true
overview: 'Barnana publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SnackFood, Sustainable, Organic, Plant-Based, and Retail.


  Barnana''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barnana Domain Security
  slug: barnana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barnana
tags:
- SnackFood
- Sustainable
- Organic
- Plant-Based
- Retail
website: https://barnana.com
---
