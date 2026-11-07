---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.dveracity.com
  baseurl_source: declared
  description: 'dVeracity API as documented publicly: 91 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: dVeracity API
  slug: dveracity-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/dveracity-com/plans/dveracity-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dveracity-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dveracity-com/rules/dveracity-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dveracity-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dveracity-com/json-ld/dveracity-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dveracity-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dveracity-com/vocabulary/dveracity-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dveracity-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dveracity-com/data-model/dveracity-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dveracity-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dveracity.com/trust
- group: auth
  title: ''
  type: Security
  url: https://dveracity.com/trust
- group: auth
  href: https://artifacts.apis.io/dveracity-com/authentication/dveracity-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dveracity-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dveracity-com/conformance/dveracity-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dveracity-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dveracity-com/llms/dveracity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dveracity-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dveracity-com/a2a/dveracity-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dveracity-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dveracity-com/mcp/dveracity-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dveracity-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dveracity-com/well-known/dveracity-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dveracity-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dveracity-com/well-known/dveracity-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dveracity-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dveracity-com/hosts/dveracity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dveracity-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dveracity.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dveracity.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dveracity.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://dveracity.com/docs/claude
- group: commercial
  title: ''
  type: Pricing
  url: https://dveracity.com/pricing
- group: auth
  href: https://artifacts.apis.io/dveracity-com/scopes/dveracity-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dveracity-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/dveracity-com/security/dveracity-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dveracity-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dveracity-com/security/dveracity-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dveracity-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dveracity-com/security/dveracity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dveracity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dveracity.com/
coverage:
  checked: '2026-11-06'
  detail: Provider docs are served as JavaScript-rendered pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dveracity.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: dVeracity provides an enterprise‑grade emissions verification platform built on Open Group standards. It offers Open Footprint, O‑DEF, and PACT‑compliant carbon accounting, enabling organizations to independently verify and report their greenhouse‑gas emissions with transparent, auditable data models and tools.
json_schemas:
- name: PostDdmsEnvironmentV1CalculationsRequest
  property_count: 3
  slug: dveracity-com-post-ddms-environment-v1-calculations-request
- name: PostDdmsEnvironmentV1EmissionsRequest
  property_count: 3
  slug: dveracity-com-post-ddms-environment-v1-emissions-request
- name: PostDdmsEnvironmentV1ReportsGenerateRequest
  property_count: 3
  slug: dveracity-com-post-ddms-environment-v1-reports-generate-request
jsonld:
- class_count: 3
  name: Dveracity Com Context
  property_count: 3
  slug: dveracity-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.dveracity.com.
  name: dVeracity MCP Server
  slug: dveracity-com-mcp-yml
modified: '2026-11-06'
name: dVeracity
nav: Providers
network: true
overview: 'dVeracity is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Emissions, Verification, Carbon Accounting, and Open Standard.


  The dVeracity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dVeracity''s developer surface includes authentication, support, documentation, pricing, and 21 more developer resources.'
plans:
- name: Dveracity Com Plans Pricing
  plan_count: 7
  slug: dveracity-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: dVeracity API Rules
  rule_count: 48
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 2
  slug: dveracity-com-rules
scopes:
- name: Dveracity Com Scopes
  scope_count: 7
  slug: dveracity-com-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 21.1
    developer_ergonomics: 26.2
    discoverability: 61.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dveracity Com Authentication
  slug: dveracity-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dveracity Com Domain Security
  slug: dveracity-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dveracity Com Vulnerability Disclosure
  slug: dveracity-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dveracity Com Trust Center
  slug: dveracity-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: dveracity-com
tags:
- Company
- Emissions
- Verification
- Carbon Accounting
- Open Standard
website: https://dveracity.com/
---
