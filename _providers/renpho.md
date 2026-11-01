---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/renpho/llms/renpho-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/renpho-llms.txt
- group: agent
  href: https://artifacts.apis.io/renpho/well-known/renpho-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/renpho-well-known.yml
- group: other
  href: https://artifacts.apis.io/renpho/hosts/renpho-hosts.yml
  title: ''
  type: Hosts
  url: hosts/renpho-hosts.yml
- group: other
  href: https://artifacts.apis.io/renpho/vendors/renpho-vendors.yml
  title: ''
  type: Vendors
  url: vendors/renpho-vendors.yml
- group: build
  href: https://artifacts.apis.io/renpho/packages/renpho-packages.yml
  title: ''
  type: SDKs
  url: packages/renpho-packages.yml
- group: build
  href: https://artifacts.apis.io/renpho/packages/renpho-packages.yml
  title: ''
  type: Packages
  url: packages/renpho-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://renpho.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://renpho.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://renpho.com/blogs/newsroom
- group: start
  title: ''
  type: Login
  url: https://renpho.com/account/login
- group: auth
  href: https://artifacts.apis.io/renpho/security/renpho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/renpho-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://renpho.com/
coverage:
  checked: '2026-10-26'
  detail: Renpho website is a Shopify storefront with JavaScript‑rendered pages and no publicly available API documentation.
  evidence:
  - status: 200
    url: https://renpho.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Renpho, founded in 2016 in California, USA, creates state‑of‑the‑art lifestyle and wellness solutions, including smart scales, massage devices, and health‑tracking apps. Their mission is to make premium wellness technology accessible to all, empowering individuals to monitor and improve their health through connected devices and intuitive software.
image: http://renpho.com/cdn/shop/files/Watermark_Slogan_-_White_1200x628_32c46670-7078-4580-b32a-b21bfcc49dcd.png?v=1736224913
layout: provider
modified: '2026-10-26'
name: Renpho
nav: Providers
network: true
overview: Renpho is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, HealthTech, IoT, and Consumer Electronics.
random_paper: 4
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
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
  name: Renpho Domain Security
  slug: renpho-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: renpho
tags:
- Company
- Wellness
- HealthTech
- IoT
- Consumer Electronics
- Wellness
- HealthTech
- IoT
- Consumer Electronics
website: https://renpho.com/
---
