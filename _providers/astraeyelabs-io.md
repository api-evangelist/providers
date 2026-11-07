---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Research API for AI Assistants – read your own research projects and report summaries.
  name: Research API
  slug: research-api
- description: 'AstraEye Labs API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AstraEye Labs API
  slug: astraeyelabs-io-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/astraeyelabs-io/plans/astraeyelabs-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astraeyelabs-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/astraeyelabs-io/rules/astraeyelabs-io-rules.yml
  title: ''
  type: Spectral
  url: rules/astraeyelabs-io-rules.yml
- group: design
  href: https://artifacts.apis.io/astraeyelabs-io/json-ld/astraeyelabs-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/astraeyelabs-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/astraeyelabs-io/vocabulary/astraeyelabs-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astraeyelabs-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/astraeyelabs-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/astraeyelabs-io/data-model/astraeyelabs-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astraeyelabs-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/astraeyelabs-io/conformance/astraeyelabs-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astraeyelabs-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astraeyelabs-io/llms/astraeyelabs-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astraeyelabs-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/astraeyelabs-io/well-known/astraeyelabs-io-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/astraeyelabs-io-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/astraeyelabs-io/well-known/astraeyelabs-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astraeyelabs-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/astraeyelabs-io/hosts/astraeyelabs-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astraeyelabs-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/astraeyelabs-io/vendors/astraeyelabs-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astraeyelabs-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astraeyelabs.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astraeyelabs.io/privacy
- group: other
  title: ''
  type: Leadership
  url: https://astraeyelabs.io/team
- group: auth
  href: https://artifacts.apis.io/astraeyelabs-io/security/astraeyelabs-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astraeyelabs-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astraeyelabs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://astraeyelabs.io/library
- group: start
  title: ''
  type: GettingStarted
  url: https://astraeyelabs.io/subscribe
- group: commercial
  title: ''
  type: Pricing
  url: https://astraeyelabs.io/subscribe
- group: start
  title: ''
  type: SignUp
  url: https://astraeyelabs.io/subscribe
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alexeykovalyov
coverage:
  checked: '2026-11-02'
  detail: Provider documentation describes the Research API but offers no public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://astraeyelabs.io/research-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AstraEye Labs computes standardized market analyses for crypto and U.S. equities from licensed data, then uses AI to interpret the results. Informational research only, and not investment, financial, legal, or tax advice.
image: https://astraeyelabs.io/icon.png
json_schemas:
- name: GetApiV1ResearchAnalysesResponse
  property_count: 19
  slug: astraeyelabs-io-get-api-v1-research-analyses-response
- name: GetApiV1ResearchMarketSlicesResponse
  property_count: 14
  slug: astraeyelabs-io-get-api-v1-research-market-slices-response
- name: GetApiV1ResearchProjectsResponse
  property_count: 10
  slug: astraeyelabs-io-get-api-v1-research-projects-response
- name: GetApiV1ResearchReportsIdResponse
  property_count: 19
  slug: astraeyelabs-io-get-api-v1-research-reports-id-response
- name: GetApiV1ResearchTemplatesIdResponse
  property_count: 15
  slug: astraeyelabs-io-get-api-v1-research-templates-id-response
- name: GetApiV1ResearchTemplatesResponse
  property_count: 11
  slug: astraeyelabs-io-get-api-v1-research-templates-response
jsonld:
- class_count: 30
  name: Astraeyelabs Io Context
  property_count: 106
  slug: astraeyelabs-io-context
layout: provider
modified: '2026-11-01'
name: AstraEye Labs
nav: Providers
network: true
overview: 'AstraEye Labs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Finance, Cryptocurrency, Stocks, and Research.


  The AstraEye Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AstraEye Labs'' developer surface includes documentation, getting-started guide, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Astraeyelabs Io Plans Pricing
  plan_count: 5
  slug: astraeyelabs-io-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Astraeyelabs Io Rate Limits
  slug: astraeyelabs-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: AstraEye Labs API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: astraeyelabs-io-rules
scopes:
- name: Astraeyelabs Io Scopes
  scope_count: 0
  slug: astraeyelabs-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 17.1
    discoverability: 58.0
    operational_transparency: 13.2
  previous_composite: 40.2
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astraeyelabs Io Authentication
  slug: astraeyelabs-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Astraeyelabs Io Domain Security
  slug: astraeyelabs-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astraeyelabs-io
tags:
- Artificial Intelligence
- Finance
- Cryptocurrency
- Stocks
- Research
website: https://astraeyelabs.io/
---
