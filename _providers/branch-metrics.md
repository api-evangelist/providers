---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-04'
api_count: 7
apis:
- description: Branch Metrics API provides deep linking and attribution endpoints as documented in the API Reference.
  name: Branch Metrics API
  slug: branch-metrics-api-2
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Analytics API from Branch Metrics — 2 operation(s) for analytics.
  name: Branch Metrics Analytics API
  slug: branch-metrics-analytics-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The App API from Branch Metrics — 1 operation(s) for app.
  name: Branch Metrics App API
  slug: branch-metrics-app-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Branch Metrics API API from Branch Metrics — 1 operation(s) for branch metrics api.
  name: Branch Metrics Branch Metrics API
  slug: branch-metrics-branch-metrics-api-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Event API from Branch Metrics — 1 operation(s) for event.
  name: Branch Metrics Event API
  slug: branch-metrics-event-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Img1 API from Branch Metrics — 1 operation(s) for img1.
  name: Branch Metrics Img1 API
  slug: branch-metrics-img1-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Query API from Branch Metrics — 1 operation(s) for query.
  name: Branch Metrics Query API
  slug: branch-metrics-query-api
artifact_total: 14
asyncapis:
- description: ''
  name: Branch Metrics Webhooks
  slug: branch-metrics-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/well-known/branch-metrics-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/branch-metrics-status-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/rules/branch-metrics-rules.yml
  title: ''
  type: Spectral
  url: rules/branch-metrics-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/json-ld/branch-metrics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/branch-metrics-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/vocabulary/branch-metrics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/branch-metrics-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/asyncapi/branch-metrics-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/branch-metrics-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/data-model/branch-metrics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/branch-metrics-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/conformance/branch-metrics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/branch-metrics-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/llms/branch-metrics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branch-metrics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/well-known/branch-metrics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branch-metrics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/hosts/branch-metrics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branch-metrics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/vendors/branch-metrics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branch-metrics-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.branch.io
- group: auth
  title: ''
  type: Security
  url: https://branch.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.branch.io/resources/category/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.branch.io/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.branch.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branch-metrics/refs/heads/main/security/branch-metrics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branch-metrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.branch.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.branch.io/
- group: docs
  title: ''
  type: APIReference
  url: https://help.branch.io/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://help.branch.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.branch.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.branch.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.branch.io/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.branch.io/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/branchio/workspace/branch-api/overview
coverage:
  checked: '2026-10-03'
  detail: API documentation pages are HTML rendered without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://help.branch.io/apidocs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Branch Metrics provides a mobile measurement and deep linking platform that helps brands attribute marketing campaigns, improve user acquisition, and drive engagement across web, app, and email channels. Leveraging AI-powered tools like Ivy, Branch offers advanced analytics, fraud detection, and customizable link management for enterprises worldwide. The platform serves over 100,000 brands, handling billions of user interactions to deliver actionable insights and optimize ROI.
json_schemas:
- name: GetV2AnalyticsResponse
  property_count: 4
  slug: branch-metrics-get-v2-analytics-response
- name: PutV1AppBranchkeyRequest
  property_count: 15
  slug: branch-metrics-put-v1-app-branchkey-request
- name: PutV1AppBranchkeyResponse
  property_count: 19
  slug: branch-metrics-put-v1-app-branchkey-response
jsonld:
- class_count: 3
  name: Branch Metrics Context
  property_count: 23
  slug: branch-metrics-context
layout: provider
modified: '2026-10-03'
name: Branch Metrics
nav: Providers
network: true
overview: 'Branch Metrics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, App API, Branch Metrics API, and 4 more. Tagged areas include Mobile, Attribution, Deep Linking, Marketing, and Analytics.


  The Branch Metrics catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Branch Metrics'' developer surface includes documentation, API reference, getting-started guide, support, pricing, engineering blog, and 20 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Branch Metrics API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: branch-metrics-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 30.2
    developer_ergonomics: 50.0
    discoverability: 69.6
    operational_transparency: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Branch Metrics Domain Security
  slug: branch-metrics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: branch-metrics
tags:
- Mobile
- Attribution
- Deep Linking
- Marketing
- Analytics
- Artificial Intelligence
website: https://www.branch.io/
---
