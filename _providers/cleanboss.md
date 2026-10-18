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
- description: API for CleanBoss platform (no machine-readable spec discovered)
  name: CleanBoss API
  slug: cleanboss-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleanboss/refs/heads/main/llms/cleanboss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleanboss-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleanboss/refs/heads/main/well-known/cleanboss-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleanboss-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleanboss/refs/heads/main/hosts/cleanboss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleanboss-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleanboss/refs/heads/main/vendors/cleanboss-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleanboss-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cleanboss.co/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cleanboss.co/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cleanboss.co/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.cleanboss.co/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleanboss/refs/heads/main/security/cleanboss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanboss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleanboss.co
coverage:
  checked: '2026-10-09'
  detail: Home page loads JavaScript and provides no machine-readable API spec.
  evidence:
  - status: 200
    url: https://www.cleanboss.co
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: CleanBoss is a consumer products brand offering non‑toxic, botanically‑derived cleaning solutions. Founded by Joy Mangano and Armando Christian Pérez, the company sells multi‑surface cleaners, laundry sheets, fruit‑and‑veggie washes, and other eco‑friendly products through its Shopify storefront. The brand emphasizes safety, effectiveness, and a “cleaning revolution” with a 100 % money‑back guarantee and free shipping on orders over $45.
image: https://www.cleanboss.co/cdn/shop/files/favicon-32x32_f475c7c3-8c4f-4a08-b2e2-f6883cab297c_180x180.png?v=1614339365
layout: provider
modified: '2026-10-08'
name: CleanBoss
nav: Providers
network: true
overview: CleanBoss is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Products, Cleaning, Eco-friendly, and E-Commerce.
random_paper: 8
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 5
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
  name: Cleanboss Domain Security
  slug: cleanboss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleanboss
tags:
- Company
- Consumer Products
- Cleaning
- Eco-friendly
- E-Commerce
website: https://www.cleanboss.co
---
