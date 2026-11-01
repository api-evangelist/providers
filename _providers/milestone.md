---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://events.mstone.ai
  baseurl_source: declared
  description: 'Milestone API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Milestone API
  slug: milestone-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/milestone/rules/milestone-rules.yml
  title: ''
  type: Spectral
  url: rules/milestone-rules.yml
- group: design
  href: https://artifacts.apis.io/milestone/json-ld/milestone-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/milestone-context.jsonld
- group: design
  href: https://artifacts.apis.io/milestone/vocabulary/milestone-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/milestone-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/milestone/data-model/milestone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/milestone-data-model.yml
- group: auth
  href: https://artifacts.apis.io/milestone/authentication/milestone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/milestone-authentication.yml
- group: design
  href: https://artifacts.apis.io/milestone/conformance/milestone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/milestone-conformance.yml
- group: agent
  href: https://artifacts.apis.io/milestone/llms/milestone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/milestone-llms.txt
- group: agent
  href: https://artifacts.apis.io/milestone/well-known/milestone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/milestone-well-known.yml
- group: other
  href: https://artifacts.apis.io/milestone/hosts/milestone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/milestone-hosts.yml
- group: other
  href: https://artifacts.apis.io/milestone/vendors/milestone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/milestone-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://mstone.ai/docs/integration-instructions/gen-ai-coding-tools/Lite-LLM/litellm-direct-setup
- group: auth
  href: https://artifacts.apis.io/milestone/security/milestone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/milestone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mstone.ai
- group: docs
  title: ''
  type: Documentation
  url: https://mstone.ai/docs/
- group: company
  title: ''
  type: Blog
  url: https://mstone.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mstone.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mstone.ai/privacy-policy/
created: '2026-10-29'
description: Milestone AI provides a platform to measure AI spend, track engineering ROI, and manage AI agents across organizations. Their solution offers analytics, cost tracking, and performance insights to help businesses optimize AI investments and operational efficiency.
image: https://mstone.ai/wp-content/uploads/2026/07/social-home.jpg?t=1792829161
json_schemas:
- name: GetReadyResponse
  property_count: 1
  slug: milestone-get-ready-response
- name: GetStatusResponse
  property_count: 1
  slug: milestone-get-status-response
- name: PostDeploymentsRequest
  property_count: 1
  slug: milestone-post-deployments-request
- name: PostIdentityResourcesAuthV1ApiTokenRequest
  property_count: 2
  slug: milestone-post-identity-resources-auth-v1-api-token-request
jsonld:
- class_count: 4
  name: Milestone Context
  property_count: 4
  slug: milestone-context
layout: provider
modified: '2026-10-29'
name: Milestone
nav: Providers
network: true
overview: 'Milestone is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Spend, Agent Governance, AI Productivity, AI Governance, and KPI Dashboards.


  The Milestone catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Milestone''s developer surface includes authentication, getting-started guide, documentation, engineering blog, and 13 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Milestone API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: milestone-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
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
  name: Milestone Authentication
  slug: milestone-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Milestone Domain Security
  slug: milestone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: milestone
tags:
- AI Spend
- Agent Governance
- AI Productivity
- AI Governance
- KPI Dashboards
website: https://mstone.ai
---
