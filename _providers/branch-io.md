---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Branch API reference—create deep links and QR codes, track events, and export attribution data.
  name: Branch API
  slug: branch-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.branch.io/
- group: agent
  href: https://artifacts.apis.io/branch-io/llms/branch-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branch-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/branch-io/well-known/branch-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/branch-io-status-security.txt
- group: agent
  href: https://artifacts.apis.io/branch-io/well-known/branch-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branch-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/branch-io/hosts/branch-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branch-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/branch-io/vendors/branch-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branch-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/branch-io/packages/branch-io-packages.yml
  title: ''
  type: SDKs
  url: packages/branch-io-packages.yml
- group: build
  href: https://artifacts.apis.io/branch-io/packages/branch-io-packages.yml
  title: ''
  type: Packages
  url: packages/branch-io-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.branch.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.branch.io/
- group: auth
  title: ''
  type: Security
  url: https://www.branch.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.branch.io/saas/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.branch.io/pricing/
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
  type: GettingStarted
  url: https://help.branch.io/account-hub/category/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.branch.io/resources/category/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://help.branch.io/apidocs/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.branch.io/
- group: auth
  href: https://artifacts.apis.io/branch-io/security/branch-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/branch-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/branch-io/security/branch-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branch-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.branch.io/
coverage:
  checked: '2026-10-26'
  detail: OpenAPI spec endpoint https://help.branch.io/apidocs/openapi.json returns 403, no machine-readable spec available.
  evidence:
  - status: 403
    url: https://help.branch.io/apidocs/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Branch provides a mobile measurement and deep linking platform that helps brands attribute marketing campaigns, manage links, and analyze user journeys across web, app, and other channels. Leveraging AI-driven tools like Ivy, Branch offers analytics, fraud detection, and customizable linking solutions for enterprises, supporting over 3.5 billion users worldwide.
json_schemas:
- name: GetV2LogsJobidResponse
  property_count: 4
  slug: branch-io-get-v2-logs-jobid-response
- name: PostScheduledExportsLogsSubscribeRequest
  property_count: 2
  slug: branch-io-post-scheduled-exports-logs-subscribe-request
- name: PostScheduledExportsLogsSubscribeResponse
  property_count: 4
  slug: branch-io-post-scheduled-exports-logs-subscribe-response
- name: PostV2DataReadyRequest
  property_count: 4
  slug: branch-io-post-v2-data-ready-request
- name: PostV2DataReadyResponse
  property_count: 2
  slug: branch-io-post-v2-data-ready-response
jsonld:
- class_count: 5
  name: Branch Io Context
  property_count: 14
  slug: branch-io-context
layout: provider
modified: '2026-10-26'
name: Branch
nav: Providers
network: true
overview: 'Branch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Branch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Branch''s developer surface includes support, pricing, getting-started guide, engineering blog, API reference, documentation, and 16 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Branch API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: branch-io-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 16.3
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/branch-io/branch-io-2026-11-03T122451.png
security:
- kind: domain-security
  name: Branch Io Domain Security
  slug: branch-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Branch Io Trust Center
  slug: branch-io-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: branch-io
tags:
- Company
website: https://www.branch.io/
---
