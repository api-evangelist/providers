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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dameproducts/llms/dameproducts-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dameproducts-llms.txt
- group: agent
  href: https://artifacts.apis.io/dameproducts/well-known/dameproducts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dameproducts-well-known.yml
- group: other
  href: https://artifacts.apis.io/dameproducts/hosts/dameproducts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dameproducts-hosts.yml
- group: other
  href: https://artifacts.apis.io/dameproducts/vendors/dameproducts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dameproducts-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dame.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dame.com/pages/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://dame.com/pages/press
- group: start
  title: ''
  type: Login
  url: https://dame.com/account/login
- group: auth
  href: https://artifacts.apis.io/dameproducts/security/dameproducts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dameproducts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dame.com
coverage:
  checked: '2026-10-22'
  detail: Dameproducts provides an e‑commerce storefront but no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://dame.com/api/graphql
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Dame Products is a consumer‑focused sex‑tech company founded in 2014, offering clinically‑studied vibrators and wellness products. The brand emphasizes ergonomic design, inclusive pleasure, and evidence‑based performance, with a public blog, lab research, and a commitment to sustainability. It operates an e‑commerce storefront at dame.com and provides product manuals, FAQs, and a community quiz to help customers find the right experience.
image: http://dame.com/cdn/shop/files/img20220929_15480079_horizontal_10020a00-18ae-4dc0-af09-9ffe64e979d5.jpg?v=1666089920
layout: provider
modified: '2026-10-22'
name: Dameproducts
nav: Providers
network: true
overview: Dameproducts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SexTech, Consumer Goods, E-Commerce, and Wellness.
random_paper: 19
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Dameproducts Domain Security
  slug: dameproducts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dameproducts
tags:
- Company
- SexTech
- Consumer Goods
- E-Commerce
- Wellness
website: https://dame.com
---
