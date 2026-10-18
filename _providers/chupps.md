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
- description: No public developer API discovered.
  name: Chupps API
  slug: chupps-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chupps/refs/heads/main/llms/chupps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chupps-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chupps/refs/heads/main/well-known/chupps-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chupps-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chupps/refs/heads/main/hosts/chupps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chupps-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chupps/refs/heads/main/vendors/chupps-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/chupps/refs/heads/main/security/chupps-domain-security.yml
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
random_paper: 21
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
