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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'flurry API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: flurry API
  slug: dvt-dev-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/dvt-dev/plans/dvt-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dvt-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dvt-dev/rules/dvt-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/dvt-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/dvt-dev/vocabulary/dvt-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dvt-dev-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/dvt-dev/security/dvt-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dvt-dev-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/dvt-dev/conformance/dvt-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dvt-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dvt-dev/llms/dvt-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dvt-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/dvt-dev/well-known/dvt-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dvt-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/dvt-dev/well-known/dvt-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dvt-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/dvt-dev/hosts/dvt-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dvt-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/dvt-dev/vendors/dvt-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dvt-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/dvt-dev/packages/dvt-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/dvt-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/dvt-dev/packages/dvt-dev-packages.yml
  title: ''
  type: Packages
  url: packages/dvt-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dvt.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dvt.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dvt.dev/pricing/
- group: company
  title: ''
  type: Blog
  url: https://dvt.dev/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dvt.dev/
- group: auth
  href: https://artifacts.apis.io/dvt-dev/security/dvt-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dvt-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dvt-dev/security/dvt-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dvt-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dvt.dev/
coverage:
  checked: '2026-11-06'
  detail: Documentation is provided as markdown pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://dvt.dev/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: flurry provides AI‑generated data applications built on Snowflake. Users describe an app in a single sentence and the platform creates a React‑based data app, versioned and governed, with unlimited users for a flat $100 per month. It offers a developer portal, API reference, pricing, and documentation for building and managing these data apps.
image: https://dvt.dev/og-image.png
layout: provider
modified: '2026-11-06'
name: flurry
nav: Providers
network: true
overview: 'flurry is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Apps, Snowflake, and Platform.


  The flurry catalog on APIs.io includes 1 Spectral governance ruleset.


  flurry''s developer surface includes pricing, engineering blog, documentation, and 17 more developer resources.'
plans:
- name: Dvt Dev Plans Pricing
  plan_count: 2
  slug: dvt-dev-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: flurry API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: dvt-dev-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dvt Dev Domain Security
  slug: dvt-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dvt Dev Vulnerability Disclosure
  slug: dvt-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dvt-dev
tags:
- Company
- Artificial Intelligence
- Data Apps
- Snowflake
- Platform
website: https://dvt.dev/
---
