---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/3doptix-com/plans/3doptix-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3doptix-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/3doptix-com/hosts/3doptix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3doptix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/3doptix-com/vendors/3doptix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3doptix-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/3doptix-com/packages/3doptix-com-packages.yml
  title: ''
  type: SDKs
  url: packages/3doptix-com-packages.yml
- group: build
  href: https://artifacts.apis.io/3doptix-com/packages/3doptix-com-packages.yml
  title: ''
  type: Packages
  url: packages/3doptix-com-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.3doptix.com/
- group: auth
  href: https://artifacts.apis.io/3doptix-com/security/3doptix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3doptix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.3doptix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.3doptix.com/api-integration/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.3doptix.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.3doptix.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.3doptix.com/term-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3doptix.com/privacy-policy/
coverage:
  checked: '2026-10-31'
  detail: API documentation page exists but provides no machine‑readable OpenAPI/GraphQL/AsyncAPI contract.
  evidence:
  - status: 200
    url: https://www.3doptix.com/api-integration/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 3DOptix provides native‑cloud optical prototyping and optical bench simulation software. Their platform offers design‑studio tools, AI‑assisted optical design, OptiTwin and TrueScene beta programs, and a suite of simulation widgets, catalog, filter finder, and API integration for developers to embed optical design capabilities into applications. The company serves industries such as imaging, academia, and engineering with cloud‑based solutions and extensive documentation, tutorials, and support resources.
image: https://www.3doptix.com/wp-content/uploads/2025/04/Screenshot-2024-11-14-140649-1024x631.png
layout: provider
modified: '2026-10-31'
name: 3DOptix
nav: Providers
network: true
overview: '3DOptix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpticalDesign, Simulation, Cloud Software, and Engineering.


  3DOptix''s developer surface includes documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: 3Doptix Com Plans Pricing
  plan_count: 3
  slug: 3doptix-com-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Doptix Com Domain Security
  slug: 3doptix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3doptix-com
tags:
- Company
- OpticalDesign
- Simulation
- Cloud Software
- Engineering
website: https://www.3doptix.com/
---
