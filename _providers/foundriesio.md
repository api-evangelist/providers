---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: FoundriesFactory is a SaaS platform for Linux IoT and Edge device management, providing tools for building, testing, deploying, and maintaining secure devices.
  name: FoundriesFactory
  slug: foundriesfactory
- description: 'Foundries.io API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Foundries.io API
  slug: foundriesio-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/foundriesio/rules/foundriesio-rules.yml
  title: ''
  type: Spectral
  url: rules/foundriesio-rules.yml
- group: design
  href: https://artifacts.apis.io/foundriesio/json-ld/foundriesio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/foundriesio-context.jsonld
- group: design
  href: https://artifacts.apis.io/foundriesio/vocabulary/foundriesio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/foundriesio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/foundriesio/data-model/foundriesio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/foundriesio-data-model.yml
- group: build
  href: https://artifacts.apis.io/foundriesio/cli/foundriesio-cli.yml
  title: ''
  type: CLI
  url: cli/foundriesio-cli.yml
- group: design
  href: https://artifacts.apis.io/foundriesio/conformance/foundriesio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foundriesio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/foundriesio/llms/foundriesio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foundriesio-llms.txt
- group: auth
  href: https://artifacts.apis.io/foundriesio/well-known/foundriesio-foundriesio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/foundriesio-foundriesio-security.txt
- group: auth
  href: https://artifacts.apis.io/foundriesio/well-known/foundriesio-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/foundriesio-api-security.txt
- group: agent
  href: https://artifacts.apis.io/foundriesio/well-known/foundriesio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/foundriesio-well-known.yml
- group: other
  href: https://artifacts.apis.io/foundriesio/hosts/foundriesio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foundriesio-hosts.yml
- group: other
  href: https://artifacts.apis.io/foundriesio/vendors/foundriesio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/foundriesio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.foundries.io/company/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.foundries.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.foundries.io/company/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.foundries.io/insights/news/
- group: start
  title: ''
  type: Login
  url: https://app.foundries.io/login/?next=/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.foundries.io/products/releases/
- group: auth
  href: https://artifacts.apis.io/foundriesio/security/foundriesio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foundriesio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.foundries.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.foundries.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.foundries.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.foundries.io/get-in-touch/
- group: operate
  title: ''
  type: Support
  url: https://support.foundries.io/
- group: company
  title: ''
  type: Blog
  url: https://www.foundries.io/insights/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foundriesio
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://docs.foundries.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Foundries.io provides a secure IoT and Edge device development and management platform called FoundriesFactory. It enables developers to build, update, and manage Linux‑based embedded devices with end‑to‑end security, OTA updates, and device lifecycle tools. The platform supports a wide range of hardware, offers integrated CI/CD pipelines, and focuses on reducing time‑to‑market while keeping code ownership with the customer.
image: https://www.foundries.io/media/foundriesio-logo.svg
json_schemas:
- name: PostTestsRequest
  property_count: 2
  slug: foundriesio-post-tests-request
- name: PostTestsResponse
  property_count: 1
  slug: foundriesio-post-tests-response
- name: PutTestsTestIdRequest
  property_count: 2
  slug: foundriesio-put-tests-test-id-request
jsonld:
- class_count: 3
  name: Foundriesio Context
  property_count: 5
  slug: foundriesio-context
layout: provider
modified: '2026-10-29'
name: Foundries.io
nav: Providers
network: true
overview: 'Foundries.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Embedded Linux, Edge Computing, Device Management, and Secure-Updates.


  The Foundries.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Foundries.io''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Foundriesio Plans Pricing
  plan_count: 0
  slug: foundriesio-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Foundriesio Rate Limits
  slug: foundriesio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Foundries.io API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: foundriesio-rules
scopes:
- name: Foundriesio Scopes
  scope_count: 0
  slug: foundriesio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 25.0
    discoverability: 65.2
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.8
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/foundriesio/foundriesio-2026-11-03T132313.png
security:
- kind: authentication
  name: Foundriesio Authentication
  slug: foundriesio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Foundriesio Domain Security
  slug: foundriesio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: foundriesio
tags:
- IoT
- Embedded Linux
- Edge Computing
- Device Management
- Secure-Updates
website: https://www.foundries.io/
---
