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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API endpoint for Umami Cart services (no public specification discovered).
  name: Umami Cart API
  slug: umami-cart-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/umami-cart/refs/heads/main/llms/umami-cart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/umami-cart-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/umami-cart/refs/heads/main/well-known/umami-cart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/umami-cart-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/umami-cart/refs/heads/main/hosts/umami-cart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/umami-cart-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/umami-cart/refs/heads/main/vendors/umami-cart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/umami-cart-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/umamicart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/umami-cart/refs/heads/main/security/umami-cart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/umami-cart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.umamicart.com
- group: company
  title: ''
  type: Blog
  url: https://www.umamicart.com/blogs/
- group: company
  title: ''
  type: About
  url: https://www.umamicart.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.umamicart.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.umamicart.com/privacy-policy/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host despite probing common endpoints.
  evidence:
  - status: 0
    url: https://api.umamicart.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Umami Cart is an online platform offering authentic Asian recipes, ingredient guides, and cooking techniques. It covers Chinese, Japanese, Korean, Thai, Vietnamese, Indian, Filipino, Malaysian and more cuisines, providing detailed guides, step‑by‑step recipes, and culinary tips tested in a real home kitchen. The site also features a blog, cooking methods, and a marketplace for Asian food products, aiming to explore and celebrate the flavors of Asia for home cooks worldwide.
image: https://www.umamicart.com/wp-content/uploads/2026/02/Gemini_Generated_Image_gsn9hrgsn9hrgsn9__1_-removebg-preview-removebg-preview.png
layout: provider
modified: '2026-10-12'
name: Umami Cart
nav: Providers
network: true
overview: 'Umami Cart is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Recipes, AsianCuisine, and Cooking.


  Umami Cart''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.7
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
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Umami Cart Domain Security
  slug: umami-cart-domain-security
  summary_line: TLSv1.3
slug: umami-cart
tags:
- Company
- Food
- Recipes
- AsianCuisine
- Cooking
website: https://www.umamicart.com
---
