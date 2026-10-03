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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for Andie Swim e-commerce platform
  name: Andie Swim API
  slug: andie-swim-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/andie-swim/refs/heads/main/llms/andie-swim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/andie-swim-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/andie-swim/refs/heads/main/well-known/andie-swim-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/andie-swim-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andie-swim/refs/heads/main/hosts/andie-swim-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andie-swim-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andie-swim/refs/heads/main/vendors/andie-swim-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andie-swim-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andie-swim/refs/heads/main/security/andie-swim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andie-swim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andieswim.com/
created: '2026-09-24'
description: Andie Swim (operating as Andie Co.) is a modern swimwear and essentials brand offering a wide range of swimwear, activewear, and lifestyle apparel. The company emphasizes inclusive sizing, high-quality materials, and a seamless online shopping experience with global shipping. Their website showcases collections, detailed product information, and a focus on comfort and confidence for all body types.
image: https://cdn.shopify.com/s/files/1/0024/2289/8758/files/ANDIE-logo-full-rgb-black.png?height=628&pad_color=fff&v=1619642340&width=1200
layout: provider
modified: '2026-09-24'
name: Andie Swim
nav: Providers
network: true
overview: Andie Swim publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Swimwear, Fashion, E-Commerce, InclusiveSizing, and Lifestyle.
random_paper: 16
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Andie Swim Domain Security
  slug: andie-swim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andie-swim
tags:
- Swimwear
- Fashion
- E-Commerce
- InclusiveSizing
- Lifestyle
website: https://andieswim.com/
---
