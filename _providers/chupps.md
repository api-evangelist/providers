---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: No public developer API discovered.
  name: Chupps API
  slug: chupps-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/chupps/llms/chupps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chupps-llms.txt
- group: agent
  href: https://artifacts.apis.io/chupps/well-known/chupps-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chupps-well-known.yml
- group: other
  href: https://artifacts.apis.io/chupps/hosts/chupps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chupps-hosts.yml
- group: other
  href: https://artifacts.apis.io/chupps/vendors/chupps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chupps-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chupps.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chupps.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://chupps.com/pages/media
- group: start
  title: ''
  type: Login
  url: https://chupps.com/account/login
- group: auth
  href: https://artifacts.apis.io/chupps/security/chupps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chupps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chupps.com
coverage:
  checked: '2026-10-08'
  detail: The site is a Shopify storefront with no developer API.
  evidence:
  - status: 200
    url: https://chupps.com/
  reason: not-a-software-company
  state: none
created: '2026-10-08'
description: Chupps is a footwear brand offering sliders, clogs, sandals and flip‑flops. Their e‑commerce site showcases a wide range of styles for men and women, emphasizing biodegradable materials and free shipping. The company operates primarily online through its website, providing product listings, an About Us page, and customer support.
image: http://chupps.com/cdn/shop/files/website_url_icon_6d33874d-4368-4e3d-9453-c39a2742f1d5.jpg?v=1733384567
layout: provider
modified: '2026-10-08'
name: Chupps
nav: Providers
network: true
overview: Chupps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Footwear, Sliders, Sandals, Clogs, and Flip‑Flops.
random_paper: 11
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 13.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chupps/chupps-2026-11-03T124132.png
security:
- kind: domain-security
  name: Chupps Domain Security
  slug: chupps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chupps
tags:
- Footwear
- Sliders
- Sandals
- Clogs
- Flip‑Flops
- Biodegradable
- Men
- Women
website: https://chupps.com
---
