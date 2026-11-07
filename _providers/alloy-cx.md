---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Private API for storage, workflow triggers, and Stargate routes as documented in the developer docs.
  name: Alloy API
  slug: alloy-api
- description: 'Alloy API as documented publicly: 77 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Alloy API
  slug: alloy-cx-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/alloy-cx/rules/alloy-cx-rules.yml
  title: ''
  type: Spectral
  url: rules/alloy-cx-rules.yml
- group: design
  href: https://artifacts.apis.io/alloy-cx/json-ld/alloy-cx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alloy-cx-context.jsonld
- group: design
  href: https://artifacts.apis.io/alloy-cx/vocabulary/alloy-cx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alloy-cx-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/alloy-cx/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/alloy-cx/data-model/alloy-cx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alloy-cx-data-model.yml
- group: auth
  href: https://artifacts.apis.io/alloy-cx/authentication/alloy-cx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alloy-cx-authentication.yml
- group: design
  href: https://artifacts.apis.io/alloy-cx/conformance/alloy-cx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alloy-cx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alloy-cx/llms/alloy-cx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alloy-cx-llms.txt
- group: other
  href: https://artifacts.apis.io/alloy-cx/hosts/alloy-cx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alloy-cx-hosts.yml
- group: other
  href: https://artifacts.apis.io/alloy-cx/vendors/alloy-cx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alloy-cx-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://alloy.cx/security
- group: start
  title: ''
  type: Login
  url: https://app.alloy.cx/login
- group: auth
  href: https://artifacts.apis.io/alloy-cx/security/alloy-cx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alloy-cx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alloy.cx/
- group: docs
  title: ''
  type: Documentation
  url: https://alloy.cx/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://alloy.cx/docs/getting-started/what-alloy-is
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alloy.cx/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alloy.cx/privacy-policy
coverage:
  checked: '2026-11-01'
  detail: Provider docs describe a private API but no OpenAPI or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://alloy.cx/docs/build-and-connect/api-access
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Alloy provides an AI‑powered Real Estate Investor OS that automates deal intake, screening, and analysis. It integrates with existing CRMs to code broker emails into structured data, offers an AI assistant named Ally for query handling, and supports multifamily capital markets workflows. The platform streamlines deal history management, reduces manual data entry, and enhances investment decision‑making with AI insights.
image: https://alloy.cx/opengraph-image?44ecfcd7f20b2455
json_schemas:
- name: GetApiOrganizationsOrgidMcpsResponse
  property_count: 1
  slug: alloy-cx-get-api-organizations-orgid-mcps-response
- name: PostApiOrganizationsOrgidMcpsEmployeeEmployeeidRequest
  property_count: 2
  slug: alloy-cx-post-api-organizations-orgid-mcps-employee-employeeid-request
- name: PostApiOrganizationsOrgidMcpsRequest
  property_count: 4
  slug: alloy-cx-post-api-organizations-orgid-mcps-request
- name: PostApiOrganizationsOrgidMcpsTestRequest
  property_count: 3
  slug: alloy-cx-post-api-organizations-orgid-mcps-test-request
- name: PostApiOrganizationsOrgidMcpsTestResponse
  property_count: 1
  slug: alloy-cx-post-api-organizations-orgid-mcps-test-response
- name: PutApiOrganizationsOrgidMcpsMcpMcpidRequest
  property_count: 4
  slug: alloy-cx-put-api-organizations-orgid-mcps-mcp-mcpid-request
jsonld:
- class_count: 11
  name: Alloy Cx Context
  property_count: 13
  slug: alloy-cx-context
layout: provider
modified: '2026-11-01'
name: Alloy
nav: Providers
network: true
overview: 'Alloy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Artificial Intelligence, Investment, Automation, and CRM.


  The Alloy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alloy''s developer surface includes authentication, documentation, getting-started guide, and 15 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Alloy API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: alloy-cx-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 17.1
    contract_governance: 19.7
    contract_quality: 25.2
    developer_ergonomics: 29.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alloy Cx Authentication
  slug: alloy-cx-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Alloy Cx Domain Security
  slug: alloy-cx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alloy-cx
tags:
- Real Estate
- Artificial Intelligence
- Investment
- Automation
- CRM
website: https://alloy.cx/
---
