---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public v2 REST API for brand systems, token exports, and related resources.
  name: BrandPilot REST API
  slug: brandpilot-rest-api
- description: 'BrandPilot API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BrandPilot API
  slug: brandpilot-dev-api
artifact_total: 9
asyncapis:
- description: ''
  name: Brandpilot Dev Webhooks
  slug: brandpilot-dev-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/brandpilot-dev/plans/brandpilot-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brandpilot-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/rules/brandpilot-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/brandpilot-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/json-ld/brandpilot-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brandpilot-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/vocabulary/brandpilot-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brandpilot-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/asyncapi/brandpilot-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/brandpilot-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/data-model/brandpilot-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brandpilot-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/brandpilot-dev/changelog/brandpilot-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brandpilot-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/brandpilot-dev/authentication/brandpilot-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brandpilot-dev-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://brandpilot.dev/docs/developers/migration-v2
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/lifecycle/brandpilot-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brandpilot-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/brandpilot-dev/conformance/brandpilot-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandpilot-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/brandpilot-dev/hosts/brandpilot-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandpilot-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandpilot-dev/vendors/brandpilot-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandpilot-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandpilot.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandpilot.dev/privacy
- group: start
  title: ''
  type: Login
  url: https://brandpilot.dev/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://brandpilot.dev/docs/developers/changelog
- group: auth
  href: https://artifacts.apis.io/brandpilot-dev/security/brandpilot-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandpilot-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandpilot.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://brandpilot.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://brandpilot.dev/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://brandpilot.dev/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://brandpilot.dev/contact
coverage:
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://brandpilot.dev/docs/developers/rest-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BrandPilot provides a comprehensive brand system platform that delivers your logo, color palettes, fonts, and ready-to-use brand assets across multiple channels. Users can generate brand guidelines, download files, and integrate the system via APIs to ensure consistent branding in marketing, product design, and digital experiences. The service includes customizable deliverables, kits, and showcases to help businesses maintain a cohesive visual identity.
image: https://brandpilot.dev/opengraph-image
json_schemas:
- name: PostApiV2SystemsNameWebhooksRequest
  property_count: 2
  slug: brandpilot-dev-post-api-v2-systems-name-webhooks-request
jsonld:
- class_count: 1
  name: Brandpilot Dev Context
  property_count: 2
  slug: brandpilot-dev-context
layout: provider
modified: '2026-11-02'
name: BrandPilot
nav: Providers
network: true
overview: 'BrandPilot is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Branding, Design, Software-as-a-Service, and Marketing.


  The BrandPilot catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BrandPilot''s developer surface includes changelog, authentication, documentation, pricing, getting-started guide, support, and 17 more developer resources.'
plans:
- name: Brandpilot Dev Plans Pricing
  plan_count: 3
  slug: brandpilot-dev-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: BrandPilot API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: brandpilot-dev-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 25.0
    discoverability: 48.2
    operational_transparency: 19.7
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Brandpilot Dev Authentication
  slug: brandpilot-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Brandpilot Dev Domain Security
  slug: brandpilot-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brandpilot-dev
tags:
- Branding
- Design
- Software-as-a-Service
- Marketing
website: https://brandpilot.dev/
---
