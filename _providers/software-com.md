---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 15
common:
- group: auth
  href: https://artifacts.apis.io/software-com/security/software-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/software-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://software.com
created: '2026-10-21'
description: Software is a technology company focusing on delivering software solutions across various industries. The company provides a suite of APIs for integration, data access, and automation, targeting developers and enterprise customers. Detailed information about its offerings, platform capabilities, and developer resources can be found through its official channels.
json_schemas:
- name: GetApiV2AlphaAnalyticsConsumptionResponse
  property_count: 1
  slug: software-com-get-api-v2-alpha-analytics-consumption-response
- name: GetV1AnalyticsCodexWorkspacesWorkspaceidUsageResponse
  property_count: 5
  slug: software-com-get-v1-analytics-codex-workspaces-workspaceid-usage-response
- name: GetV1AnalyticsWorkspacesWorkspaceidUsageResponse
  property_count: 5
  slug: software-com-get-v1-analytics-workspaces-workspaceid-usage-response
- name: GetV1ManageWorkspacesWorkspaceidUsersResponse
  property_count: 5
  slug: software-com-get-v1-manage-workspaces-workspaceid-users-response
- name: GetV3EnterpriseConsumptionDailyResponse
  property_count: 1
  slug: software-com-get-v3-enterprise-consumption-daily-response
- name: GetV3EnterpriseConsumptionDailyUsersUseridResponse
  property_count: 1
  slug: software-com-get-v3-enterprise-consumption-daily-users-userid-response
jsonld:
- class_count: 7
  name: Software Com Context
  property_count: 18
  slug: software-com-context
layout: provider
modified: '2026-10-21'
name: Software
nav: Providers
network: true
overview: 'Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, API, Integration, and Enterprise.


  The Software catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Software Com Plans Pricing
  plan_count: 4
  slug: software-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Software Com Rate Limits
  slug: software-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Software API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: software-com-rules
scopes:
- name: Software Com Scopes
  scope_count: 0
  slug: software-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.5
    catalog_earned_first_party: 12.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Software Com Authentication
  slug: software-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Software Com Domain Security
  slug: software-com-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Software Com Vulnerability Disclosure
  slug: software-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Software Com Trust Center
  slug: software-com-trust-center
  summary_line: SOC 2
slug: software-com
tags:
- Company
- Software
- API
- Integration
- Enterprise
website: http://software.com
---
