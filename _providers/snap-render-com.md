---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Snap Render Com Agentic Access
  operation_count: 23
  slug: snap-render-com-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 1
apis:
- baseURL: https://app.snap-render.com
  baseurl_source: declared
  description: The Extract API from snap-render-com — 1 operation(s) for extract.
  name: snap-render-com Extract API
  slug: snap-render-com-extract-api
- baseURL: https://app.snap-render.com
  baseurl_source: declared
  description: The Health API from snap-render-com — 1 operation(s) for health.
  name: snap-render-com Health API
  slug: snap-render-com-health-api
- baseURL: https://app.snap-render.com
  baseurl_source: declared
  description: The Schedules API from snap-render-com — 4 operation(s) for schedules.
  name: snap-render-com Schedules API
  slug: snap-render-com-schedules-api
- baseURL: https://app.snap-render.com
  baseurl_source: declared
  description: The Screenshot API from snap-render-com — 6 operation(s) for screenshot.
  name: snap-render-com Screenshot API
  slug: snap-render-com-screenshot-api
- baseURL: https://app.snap-render.com
  baseurl_source: declared
  description: The Usage API from snap-render-com — 2 operation(s) for usage.
  name: snap-render-com Usage API
  slug: snap-render-com-usage-api
- baseURL: https://app.snap-render.com
  baseurl_source: declared
  description: The Webhooks API from snap-render-com — 3 operation(s) for webhooks.
  name: snap-render-com Webhooks API
  slug: snap-render-com-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Snap Render Com Webhooks
  slug: snap-render-com-webhooks
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://snap-render.com/pricing
- group: agent
  href: https://artifacts.apis.io/snap-render-com/agentic-access/snap-render-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snap-render-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/snap-render-com/plans/snap-render-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snap-render-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/snap-render-com/rules/snap-render-com-rules.yml
  title: ''
  type: Spectral
  url: rules/snap-render-com-rules.yml
- group: design
  href: https://artifacts.apis.io/snap-render-com/json-ld/snap-render-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snap-render-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/snap-render-com/vocabulary/snap-render-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snap-render-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/snap-render-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/snap-render-com/asyncapi/snap-render-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/snap-render-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/snap-render-com/data-model/snap-render-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snap-render-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/snap-render-com/authentication/snap-render-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snap-render-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/snap-render-com/errors/snap-render-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snap-render-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snap-render-com/conformance/snap-render-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snap-render-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/snap-render-com/llms/snap-render-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snap-render-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/snap-render-com/well-known/snap-render-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snap-render-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/snap-render-com/hosts/snap-render-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snap-render-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/snap-render-com/vendors/snap-render-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snap-render-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/snap-render-com/packages/snap-render-com-packages.yml
  title: ''
  type: Packages
  url: packages/snap-render-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snap-render.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://snap-render.com/status
- group: build
  title: ''
  type: SDKs
  url: https://snap-render.com/sdks
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snap-render.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.snap-render.com/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://snap-render.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://snap-render.com/blog
- group: auth
  href: https://artifacts.apis.io/snap-render-com/security/snap-render-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snap-render-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snap-render.com/
- group: docs
  title: ''
  type: Documentation
  url: https://snap-render.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://snap-render.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://snap-render.com/docs/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://snap-render.com/openapi.json
  - status: null
    url: https://app.snap-render.com/openapi.json
  - status: 401
    url: https://app.snap-render.com/mcp
  - status: 200
    url: https://snap-render.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: SnapRender provides a Screenshot API that allows developers and AI agents to capture any website as PNG, JPEG, WebP, or PDF using real Chrome. The service handles cookie walls, device emulation, and page change monitoring, offering 200 free captures per month. It aims to simplify website rendering for integration into applications, analytics, and automated workflows.
image: https://snap-render.com/og-image.png
json_schemas:
- name: BatchJobResponse
  property_count: 9
  slug: snap-render-com-batch-job-response
- name: ExtractResult
  property_count: 5
  slug: snap-render-com-extract-result
- name: ScheduleCapture
  property_count: 13
  slug: snap-render-com-schedule-capture
- name: Schedule
  property_count: 15
  slug: snap-render-com-schedule
- name: Usage
  property_count: 3
  slug: snap-render-com-usage
- name: WebhookResponse
  property_count: 6
  slug: snap-render-com-webhook-response
jsonld:
- class_count: 7
  name: Snap Render Com Context
  property_count: 43
  slug: snap-render-com-context
layout: provider
modified: '2026-10-31'
name: snap-render-com
nav: Providers
network: true
overview: 'snap-render-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Extract API, Health API, Schedules API, and 3 more. Tagged areas include Company, API, Screenshot, Rendering, and Automation.


  The snap-render-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  snap-render-com''s developer surface includes pricing, authentication, changelog, engineering blog, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Snap Render Com Plans Pricing
  plan_count: 5
  slug: snap-render-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: snap-render-com API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: snap-render-com-rules
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 68.3
    developer_ergonomics: 56.4
    discoverability: 66.1
    operational_transparency: 39.5
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
- kind: authentication
  name: Snap Render Com Authentication
  slug: snap-render-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Snap Render Com Domain Security
  slug: snap-render-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: snap-render-com-capture-screenshot
  slug: snap-render-com-capture-screenshot
slug: snap-render-com
tags:
- Company
- API
- Screenshot
- Rendering
- Automation
- Cloud
website: https://snap-render.com/
---
