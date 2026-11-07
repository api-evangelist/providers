---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/wearepatchworks/plans/wearepatchworks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wearepatchworks-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wearepatchworks/conventions/wearepatchworks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wearepatchworks-conventions.yml
- group: design
  href: https://artifacts.apis.io/wearepatchworks/conformance/wearepatchworks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wearepatchworks-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wearepatchworks/llms/wearepatchworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wearepatchworks-llms.txt
- group: agent
  href: https://artifacts.apis.io/wearepatchworks/well-known/wearepatchworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wearepatchworks-well-known.yml
- group: other
  href: https://artifacts.apis.io/wearepatchworks/hosts/wearepatchworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wearepatchworks-hosts.yml
- group: other
  href: https://artifacts.apis.io/wearepatchworks/vendors/wearepatchworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wearepatchworks-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://patchworks.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://patchworks.io/security-and-compliance/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://patchworks.io/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://patchworks.io/resources/news/ecommerce-peak-resilience-checklist-bfcm/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://patchworks.io/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.wearepatchworks.com/product-documentation/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.wearepatchworks.com/product-documentation/getting-started/subscription-tier-limits
- group: docs
  title: ''
  type: Documentation
  url: https://doc.wearepatchworks.com/
- group: auth
  href: https://artifacts.apis.io/wearepatchworks/security/wearepatchworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wearepatchworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wearepatchworks.com/
coverage:
  checked: '2026-10-21'
  detail: The provider offers a webmcp manifest but no OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://patchworks.io/.well-known/api-catalog
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Patchworks connects ERP, ecommerce, WMS and more into one reliable integration layer, assisted with AI. Used by over 1,700 retail and DTC brands, it provides a unified commerce platform that automates data flow, reduces manual work, and scales efficiently for retailers and brands.
image: https://patchworks.io/wp-content/uploads/2026/05/Patchworks-Social-Banner-1.png
layout: provider
modified: '2026-10-21'
name: Patchworks
nav: Providers
network: true
overview: 'Patchworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, E-Commerce, ERP, Automation, and Artificial Intelligence.


  Patchworks'' developer surface includes pricing, API reference, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Wearepatchworks Plans Pricing
  plan_count: 3
  slug: wearepatchworks-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wearepatchworks/wearepatchworks-2026-11-03T150039.png
security:
- kind: domain-security
  name: Wearepatchworks Domain Security
  slug: wearepatchworks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: wearepatchworks
tags:
- Integration
- E-Commerce
- ERP
- Automation
- Artificial Intelligence
website: https://wearepatchworks.com/
---
