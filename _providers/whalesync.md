---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.whalesync.com/v1
  baseurl_source: declared
  description: 'Whalesync API as documented publicly: 45 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Whalesync API
  slug: whalesync-api
artifact_total: 13
asyncapis:
- description: ''
  name: Whalesync Webhooks
  slug: whalesync-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/whalesync/rate-limits/whalesync-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/whalesync-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/whalesync/plans/whalesync-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whalesync-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/whalesync/rules/whalesync-rules.yml
  title: ''
  type: Spectral
  url: rules/whalesync-rules.yml
- group: design
  href: https://artifacts.apis.io/whalesync/json-ld/whalesync-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whalesync-context.jsonld
- group: design
  href: https://artifacts.apis.io/whalesync/vocabulary/whalesync-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whalesync-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/whalesync/asyncapi/whalesync-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/whalesync-webhooks.yml
- group: design
  href: https://artifacts.apis.io/whalesync/data-model/whalesync-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whalesync-data-model.yml
- group: design
  href: https://artifacts.apis.io/whalesync/conformance/whalesync-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whalesync-conformance.yml
- group: other
  href: https://artifacts.apis.io/whalesync/overlays/whalesync-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/whalesync-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/whalesync/llms/whalesync-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whalesync-llms.txt
- group: agent
  href: https://artifacts.apis.io/whalesync/well-known/whalesync-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whalesync-well-known.yml
- group: other
  href: https://artifacts.apis.io/whalesync/hosts/whalesync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whalesync-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.whalesync.com/company/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.whalesync.com/company/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.whalesync.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.whalesync.com/sign-in
- group: other
  title: ''
  type: Leadership
  url: https://www.whalesync.com/team/ryder-ziola
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.whalesync.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.whalesync.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.whalesync.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.whalesync.com/start-here/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whalesync.com/
- group: auth
  href: https://artifacts.apis.io/whalesync/security/whalesync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whalesync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whalesync.com/
coverage:
  checked: '2026-10-26'
  detail: The developer portal provides documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL files were found.
  evidence:
  - status: 200
    url: https://www.whalesync.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Whalesync provides a two-way data synchronization platform that connects popular SaaS applications such as Google Sheets, Notion, Airtable, Webflow, HubSpot, and many more. Users can automate bidirectional data flows without code, enabling seamless integration, real-time updates, and unified data management across tools. The service offers a visual interface, pre-built connectors, and a developer-friendly API for custom workflows, supporting both no‑code and programmatic use cases.
image: https://www-static.whalesync.com/theme/generic-og.png
json_schemas:
- name: GetLiveExportLiveExportsIdScheduleResponse
  property_count: 7
  slug: whalesync-get-live-export-live-exports-id-schedule-response
- name: GetLiveExportLiveExportsIdStatusResponse
  property_count: 7
  slug: whalesync-get-live-export-live-exports-id-status-response
- name: GetLiveExportRunsIdResponse
  property_count: 8
  slug: whalesync-get-live-export-runs-id-response
- name: GetSyncRecordsRecordidResponse
  property_count: 7
  slug: whalesync-get-sync-records-recordid-response
- name: GetSyncSyncsSyncidTablesTableidFieldsResponse
  property_count: 9
  slug: whalesync-get-sync-syncs-syncid-tables-tableid-fields-response
- name: PostLiveExportLiveExportsIdSaveResponse
  property_count: 5
  slug: whalesync-post-live-export-live-exports-id-save-response
jsonld:
- class_count: 41
  name: Whalesync Context
  property_count: 57
  slug: whalesync-context
layout: provider
modified: '2026-10-25'
name: Whalesync
nav: Providers
network: true
overview: 'Whalesync is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Data Sync, No-Code, and Software-as-a-Service.


  The Whalesync catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Whalesync''s developer surface includes pricing, changelog, engineering blog, API reference, getting-started guide, documentation, and 18 more developer resources.'
plans:
- name: Whalesync Plans Pricing
  plan_count: 3
  slug: whalesync-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Whalesync Rate Limits
  slug: whalesync-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Whalesync API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 2
  slug: whalesync-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 40.4
    developer_ergonomics: 15.5
    discoverability: 74.1
    operational_transparency: 36.8
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/whalesync/whalesync-2026-11-03T150140.png
security:
- kind: domain-security
  name: Whalesync Domain Security
  slug: whalesync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whalesync
tags:
- Company
- Integration
- Data Sync
- No-Code
- Software-as-a-Service
website: https://whalesync.com/
---
