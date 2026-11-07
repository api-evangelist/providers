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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for Netmon appliance providing monitoring, logs, alerts, and integrations.
  name: Netmon API
  slug: netmon-api
- description: 'netmon-com API as documented publicly: 39 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: netmon-com API
  slug: netmon-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/netmon-com/plans/netmon-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/netmon-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/netmon-com/rules/netmon-com-rules.yml
  title: ''
  type: Spectral
  url: rules/netmon-com-rules.yml
- group: design
  href: https://artifacts.apis.io/netmon-com/json-ld/netmon-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/netmon-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/netmon-com/vocabulary/netmon-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/netmon-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/netmon-com/data-model/netmon-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/netmon-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/netmon-com/conventions/netmon-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/netmon-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/netmon-com/authentication/netmon-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/netmon-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/netmon-com/errors/netmon-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/netmon-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/netmon-com/conformance/netmon-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/netmon-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/netmon-com/llms/netmon-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netmon-com-llms.txt
- group: other
  href: https://artifacts.apis.io/netmon-com/hosts/netmon-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netmon-com-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://netmon.com/api-reference/
- group: auth
  href: https://artifacts.apis.io/netmon-com/security/netmon-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netmon-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netmon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://netmon.com/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://netmon.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://netmon.com/support/
- group: start
  title: ''
  type: GettingStarted
  url: https://netmon.com/documentation/
- group: company
  title: ''
  type: Blog
  url: https://netmon.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://netmon.com/privacy-policy/
created: '2026-10-30'
description: Netmon provides a self-hosted network monitoring appliance that offers comprehensive visibility into network performance, traffic, logs, and security events. It includes built-in alerting via email, webhooks, Slack, Microsoft Teams, and Discord, as well as a built-in MCP server for AI assistants to query devices, logs, and traffic. The solution supports Linux and Windows agents, packet capture streaming to Wireshark, and offers extensive documentation, pricing, and support resources.
image: https://netmon.com/wp-content/uploads/2026/08/netmon-social-card.png
json_schemas:
- name: GetApiAgentDownloadResponse
  property_count: 4
  slug: netmon-com-get-api-agent-download-response
- name: GetApiDeviceDeviceidAlertHistoryResponse
  property_count: 2
  slug: netmon-com-get-api-device-deviceid-alert-history-response
- name: GetApiNetworkactivityResponse
  property_count: 10
  slug: netmon-com-get-api-networkactivity-response
- name: PostApiAlertsAlertidToggleResponse
  property_count: 7
  slug: netmon-com-post-api-alerts-alertid-toggle-response
- name: PostApiAlertsLegacyLegacyidMaintenanceWindowsSyncResponse
  property_count: 9
  slug: netmon-com-post-api-alerts-legacy-legacyid-maintenance-windows-sync-response
- name: PostApiDeviceSetRequest
  property_count: 6
  slug: netmon-com-post-api-device-set-request
jsonld:
- class_count: 54
  name: Netmon Com Context
  property_count: 97
  slug: netmon-com-context
layout: provider
modified: '2026-10-30'
name: netmon-com
nav: Providers
network: true
overview: 'netmon-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Network Monitoring, Self-Hosted, AI Integration, and Open Source.


  The netmon-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  netmon-com''s developer surface includes authentication, API reference, documentation, pricing, support, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Netmon Com Plans Pricing
  plan_count: 4
  slug: netmon-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: netmon-com API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: netmon-com-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.5
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
screenshot: https://apis.io/screenshots/netmon-com/netmon-com-2026-11-03T140130.png
security:
- kind: authentication
  name: Netmon Com Authentication
  slug: netmon-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Netmon Com Domain Security
  slug: netmon-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: netmon-com
tags:
- Company
- Network Monitoring
- Self-Hosted
- AI Integration
- Open Source
website: https://netmon.com/
---
