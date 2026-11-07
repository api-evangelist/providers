---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'SharpTools API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: SharpTools API
  slug: sharptools-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/sharptools/plans/sharptools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sharptools-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sharptools/rules/sharptools-rules.yml
  title: ''
  type: Spectral
  url: rules/sharptools-rules.yml
- group: design
  href: https://artifacts.apis.io/sharptools/json-ld/sharptools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sharptools-context.jsonld
- group: design
  href: https://artifacts.apis.io/sharptools/vocabulary/sharptools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sharptools-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sharptools/data-model/sharptools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sharptools-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sharptools/authentication/sharptools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sharptools-authentication.yml
- group: design
  href: https://artifacts.apis.io/sharptools/conformance/sharptools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sharptools-conformance.yml
- group: other
  href: https://artifacts.apis.io/sharptools/hosts/sharptools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sharptools-hosts.yml
- group: other
  href: https://artifacts.apis.io/sharptools/vendors/sharptools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sharptools-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.sharptools.io/policies/terms.html
- group: operate
  title: ''
  type: Support
  url: https://help.sharptools.io
- group: commercial
  title: ''
  type: Pricing
  url: https://sharptools.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.sharptools.io
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sharptools.io/article/42-how-do-i-setup-pushover
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sharptools.io/
- group: auth
  href: https://artifacts.apis.io/sharptools/security/sharptools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sharptools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sharptools.io/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.sharptools.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SharpTools provides an intuitive dashboard platform for building smart home automations, integrating with a wide range of IoT devices and services. Users can create custom dashboards, set up automation rules, and monitor device status in real time, all through a web interface and mobile apps. The platform emphasizes ease of use, flexibility, and extensive third‑party integrations, enabling both hobbyists and professionals to streamline their smart environments.
image: https://cdn.sharptools.io/images/landing/og/OG-Landing_Page.png
json_schemas:
- name: PostButtonRequest
  property_count: 2
  slug: sharptools-post-button-request
- name: PostMotionRequest
  property_count: 1
  slug: sharptools-post-motion-request
- name: PostSwitchRequest
  property_count: 1
  slug: sharptools-post-switch-request
- name: PostTemperatureRequest
  property_count: 1
  slug: sharptools-post-temperature-request
jsonld:
- class_count: 4
  name: Sharptools Context
  property_count: 3
  slug: sharptools-context
layout: provider
modified: '2026-10-28'
name: SharpTools
nav: Providers
network: true
overview: 'SharpTools is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Smart Home, Dashboards, Automation, Rule Engine, and Hub Integration.


  The SharpTools catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SharpTools'' developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Sharptools Plans Pricing
  plan_count: 3
  slug: sharptools-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: SharpTools API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: sharptools-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 32.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sharptools/sharptools-2026-11-03T143110.png
security:
- kind: authentication
  name: Sharptools Authentication
  slug: sharptools-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Sharptools Domain Security
  slug: sharptools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sharptools
tags:
- Smart Home
- Dashboards
- Automation
- Rule Engine
- Hub Integration
- Device Monitoring
- Custom Tiles
website: https://sharptools.io/
---
