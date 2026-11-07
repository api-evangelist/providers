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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://<your-tenant>.app.blinkops.com
  baseurl_source: declared
  description: 'Blink API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Blink API
  slug: blinkops-com-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/blinkops-com/well-known/blinkops-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blinkops-com-well-known.yml
- group: design
  href: https://artifacts.apis.io/blinkops-com/rules/blinkops-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blinkops-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blinkops-com/json-ld/blinkops-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blinkops-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blinkops-com/vocabulary/blinkops-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blinkops-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blinkops-com/data-model/blinkops-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blinkops-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.blinkops.com/
- group: design
  href: https://artifacts.apis.io/blinkops-com/conformance/blinkops-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blinkops-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blinkops-com/llms/blinkops-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blinkops-com-llms.txt
- group: other
  href: https://artifacts.apis.io/blinkops-com/a2a/blinkops-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blinkops-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/blinkops-com/hosts/blinkops-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blinkops-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blinkops-com/vendors/blinkops-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blinkops-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blinkops.com/docs/getting-started/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blinkops.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blinkops.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blinkops
- group: auth
  href: https://artifacts.apis.io/blinkops-com/security/blinkops-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blinkops-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/blinkops-com/security/blinkops-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blinkops-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkops.com
created: '2026-10-24'
description: 'Blink is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by lightspeed-venture-partners) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostWorkspaceWsidCaseManagementTableAlertsRequest
  property_count: 7
  slug: blinkops-com-post-workspace-wsid-case-management-table-alerts-request
- name: PostWorkspaceWsidConnectionsResponse
  property_count: 19
  slug: blinkops-com-post-workspace-wsid-connections-response
- name: PostWorkspaceWsidPlaybooksIdExecuteRequest
  property_count: 6
  slug: blinkops-com-post-workspace-wsid-playbooks-id-execute-request
- name: PutWorkspaceWsidCaseManagementTableAlertsAlertidRequest
  property_count: 7
  slug: blinkops-com-put-workspace-wsid-case-management-table-alerts-alertid-request
- name: PutWorkspaceWsidPlaybooksIdEditRequest
  property_count: 14
  slug: blinkops-com-put-workspace-wsid-playbooks-id-edit-request
- name: PutWorkspaceWsidPlaybooksIdEditResponse
  property_count: 14
  slug: blinkops-com-put-workspace-wsid-playbooks-id-edit-response
jsonld:
- class_count: 41
  name: Blinkops Com Context
  property_count: 56
  slug: blinkops-com-context
layout: provider
modified: '2026-10-24'
name: Blink
nav: Providers
network: true
overview: 'Blink is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Blink catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Blink''s developer surface includes getting-started guide, documentation, API reference, and 15 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Blink API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: blinkops-com-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 14.3
    discoverability: 51.8
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/blinkops-com/blinkops-com-2026-11-03T121947.png
security:
- kind: domain-security
  name: Blinkops Com Domain Security
  slug: blinkops-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Blinkops Com Trust Center
  slug: blinkops-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: blinkops-com
tags:
- Company
website: https://blinkops.com
---
