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
- description: API for Aquaria water generator services
  name: Aquaria API
  slug: aquaria-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aquaria/refs/heads/main/plans/aquaria-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aquaria-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aquaria/refs/heads/main/llms/aquaria-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aquaria-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aquaria/refs/heads/main/well-known/aquaria-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aquaria-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquaria/refs/heads/main/hosts/aquaria-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquaria-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquaria/refs/heads/main/vendors/aquaria-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquaria-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aquaria.world/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquaria.world/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aquaria.world/legal/price-match-guarantee
- group: company
  title: ''
  type: Blog
  url: https://www.aquaria.world/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquaria/refs/heads/main/security/aquaria-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquaria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aquaria.world
coverage:
  checked: 2026-09-26
  detail: No owned OpenAPI or GraphQL spec could be verified for Aquaria; the GraphQL endpoint appears to be a generic Shopify API not specific to Aquaria.
  evidence:
  - status: 200
    url: https://shop.aquaria.world/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aquaria makes water from thin air—delivering abundant, safe water for your entire home with no pipes, no wells, no PFAS. The company provides atmospheric water generators for residential, commercial, and community use, aiming to solve water scarcity with sustainable technology.
layout: provider
modified: '2026-09-25'
name: Aquaria
nav: Providers
network: true
overview: 'Aquaria publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WaterTech, Sustainability, AtmosphericWater, and Cleantech.


  Aquaria''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Aquaria Plans Pricing
  plan_count: 2
  slug: aquaria-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquaria Domain Security
  slug: aquaria-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aquaria
tags:
- Company
- WaterTech
- Sustainability
- AtmosphericWater
- Cleantech
- HomeTech
website: https://www.aquaria.world
---
