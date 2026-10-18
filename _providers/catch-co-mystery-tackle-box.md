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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: GraphQL API providing access to product, subscription, and account data.
  name: Mystery Tackle Box GraphQL API
  slug: mystery-tackle-box-graphql-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/catch-co-mystery-tackle-box/refs/heads/main/plans/catch-co-mystery-tackle-box-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/catch-co-mystery-tackle-box-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catch-co-mystery-tackle-box/refs/heads/main/llms/catch-co-mystery-tackle-box-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catch-co-mystery-tackle-box-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catch-co-mystery-tackle-box/refs/heads/main/well-known/catch-co-mystery-tackle-box-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catch-co-mystery-tackle-box-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catch-co-mystery-tackle-box/refs/heads/main/hosts/catch-co-mystery-tackle-box-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catch-co-mystery-tackle-box-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catch-co-mystery-tackle-box/refs/heads/main/vendors/catch-co-mystery-tackle-box-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catch-co-mystery-tackle-box-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.mysterytacklebox.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mysterytacklebox.com/plans
- group: start
  title: ''
  type: Login
  url: https://mysterytacklebox.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catch-co-mystery-tackle-box/refs/heads/main/security/catch-co-mystery-tackle-box-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catch-co-mystery-tackle-box-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mysterytacklebox.com
- group: company
  title: ''
  type: Blog
  url: https://mysterytacklebox.com/blogs/news
- group: company
  title: ''
  type: Blog
  url: https://mysterytacklebox.com/blogs/fish-tales
- group: company
  title: ''
  type: Blog
  url: https://mysterytacklebox.com/blogs/mtb-u
- group: company
  title: ''
  type: Blog
  url: https://mysterytacklebox.com/blogs/dibble
coverage:
  checked: '2026-10-12'
  detail: GraphQL introspection returns Shopify generic schema not specific to Mystery Tackle Box, indicating the API is not owned by the company.
  evidence:
  - status: 200
    url: https://mysterytacklebox.com/api/graphql
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Mystery Tackle Box, a division of Catch Co, offers a monthly fishing tackle subscription service delivering curated selections of lures, baits, and accessories to anglers across the United States. Founded to simplify the hobby, the company provides flexible plans ranging from beginner to elite tiers, each featuring species-specific assortments, exclusive gear, and educational content. The platform operates an e‑commerce storefront, supports gift subscriptions, and engages customers through a blog and community resources, aiming to enhance the fishing experience for enthusiasts of all skill levels.
image: http://mysterytacklebox.com/cdn/shop/files/mtb-social-share-img.jpg?v=1776981825
layout: provider
modified: '2026-10-12'
name: Catch Co / Mystery Tackle Box
nav: Providers
network: true
overview: 'Catch Co / Mystery Tackle Box is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fishing, Subscription, E-Commerce, and Outdoors.


  Catch Co / Mystery Tackle Box''s developer surface includes support, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Catch Co Mystery Tackle Box Plans Pricing
  plan_count: 3
  slug: catch-co-mystery-tackle-box-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catch Co Mystery Tackle Box Domain Security
  slug: catch-co-mystery-tackle-box-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catch-co-mystery-tackle-box
tags:
- Company
- Fishing
- Subscription
- E-Commerce
- Outdoors
website: https://mysterytacklebox.com
---
