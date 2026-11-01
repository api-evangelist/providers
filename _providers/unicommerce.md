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
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/unicommerce/conformance/unicommerce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unicommerce-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unicommerce/llms/unicommerce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unicommerce-llms.txt
- group: agent
  href: https://artifacts.apis.io/unicommerce/well-known/unicommerce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unicommerce-well-known.yml
- group: other
  href: https://artifacts.apis.io/unicommerce/hosts/unicommerce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unicommerce-hosts.yml
- group: other
  href: https://artifacts.apis.io/unicommerce/vendors/unicommerce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unicommerce-vendors.yml
- group: build
  href: https://artifacts.apis.io/unicommerce/packages/unicommerce-packages.yml
  title: ''
  type: SDKs
  url: packages/unicommerce-packages.yml
- group: build
  href: https://artifacts.apis.io/unicommerce/packages/unicommerce-packages.yml
  title: ''
  type: Packages
  url: packages/unicommerce-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unicommerce.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://support.unicommerce.com/
- group: start
  title: ''
  type: SignUp
  url: https://unicommerce.com/sign-up/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unicommerce.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://unicommerce.com/blog/
- group: auth
  href: https://artifacts.apis.io/unicommerce/security/unicommerce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unicommerce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unicommerce.com/
coverage:
  checked: '2026-10-27'
  detail: Access to the developer page returned HTTP 403 Forbidden, indicating a partner login gate.
  evidence:
  - status: 403
    url: https://unicommerce.com/developer
  reason: partner-login
  state: gated
created: '2026-10-27'
description: 'Unicommerce is India’s #1 e‑commerce enablement SaaS platform for order management, warehouse management, and multi‑channel inventory operations. It offers a cloud‑based solution to streamline order processing, inventory syncing across marketplaces, and fulfillment, helping merchants scale their online businesses. Book a free demo today.'
image: https://infowordpress.s3.ap-south-1.amazonaws.com/wp-content/uploads/2025/01/08065145/cloud-based-ecommerce-saas-platform-in-india.webp
layout: provider
modified: '2026-10-27'
name: Unicommerce
nav: Providers
network: true
overview: 'Unicommerce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, e-commerce, SaaS, Order Management, and Warehouse Management.


  Unicommerce''s developer surface includes support, signup flow, engineering blog, and 11 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Unicommerce Domain Security
  slug: unicommerce-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unicommerce
tags:
- Company
- e-commerce
- SaaS
- Order Management
- Warehouse Management
website: https://unicommerce.com/
---
