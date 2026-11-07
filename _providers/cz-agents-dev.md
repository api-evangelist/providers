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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://ares.cz-agents.dev
  baseurl_source: declared
  description: 'cz-agents-dev API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: cz-agents-dev API
  slug: cz-agents-dev-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/cz-agents-dev/rate-limits/cz-agents-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cz-agents-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cz-agents-dev/plans/cz-agents-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cz-agents-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cz-agents-dev/rules/cz-agents-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/cz-agents-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/cz-agents-dev/json-ld/cz-agents-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cz-agents-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/cz-agents-dev/vocabulary/cz-agents-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cz-agents-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cz-agents-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cz-agents-dev/data-model/cz-agents-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cz-agents-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/cz-agents-dev/conformance/cz-agents-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cz-agents-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cz-agents-dev/llms/cz-agents-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cz-agents-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/cz-agents-dev/well-known/cz-agents-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cz-agents-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/cz-agents-dev/hosts/cz-agents-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cz-agents-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/cz-agents-dev/vendors/cz-agents-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cz-agents-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cz-agents.dev
- group: auth
  href: https://artifacts.apis.io/cz-agents-dev/security/cz-agents-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cz-agents-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cz-agents.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://cz-agents.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cz-agents.dev/docs/api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://cz-agents.dev/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cz-agents.dev/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cz-agents.dev/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://cz-agents.dev/
coverage:
  checked: '2026-10-29'
  detail: Provider documentation lists example endpoints but does not publish an OpenAPI/Swagger file.
  evidence:
  - status: 404
    url: https://cz-agents.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: cz-agents provides open-source Model Context Protocol (MCP) servers delivering Czech and EU business, financial, and compliance data for AI agents and scripts. It offers native AI‑friendly endpoints for the Czech ARES business register, ČNB foreign‑exchange rates, EU and OFAC sanctions, ISIR insolvency records, ADIS unreliable VAT payer detection, and a comprehensive due‑diligence aggregator. Free tier includes limited calls, with paid plans for higher depth and credit packs. The service is MIT‑licensed and hosted with no token required for basic usage.
json_schemas:
- name: GetV1CompaniesCompanieidBankAccountsResponse
  property_count: 2
  slug: cz-agents-dev-get-v1-companies-companieid-bank-accounts-response
- name: GetV1CompaniesCompanieidResponse
  property_count: 2
  slug: cz-agents-dev-get-v1-companies-companieid-response
- name: GetV1CompaniesCompanieidStatutariesResponse
  property_count: 2
  slug: cz-agents-dev-get-v1-companies-companieid-statutaries-response
- name: GetV1CompaniesResponse
  property_count: 2
  slug: cz-agents-dev-get-v1-companies-response
- name: GetV1DdDdidResponse
  property_count: 2
  slug: cz-agents-dev-get-v1-dd-ddid-response
- name: GetV1DdDdidRiskResponse
  property_count: 2
  slug: cz-agents-dev-get-v1-dd-ddid-risk-response
jsonld:
- class_count: 8
  name: Cz Agents Dev Context
  property_count: 2
  slug: cz-agents-dev-context
layout: provider
modified: '2026-10-29'
name: cz-agents-dev
nav: Providers
network: true
overview: 'cz-agents-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Czech, Compliance, and Open Source.


  The cz-agents-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cz-agents-dev''s developer surface includes documentation, API reference, pricing, and 18 more developer resources.'
plans:
- name: Cz Agents Dev Plans Pricing
  plan_count: 7
  slug: cz-agents-dev-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 8
  name: Cz Agents Dev Rate Limits
  slug: cz-agents-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: cz-agents-dev API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: cz-agents-dev-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 81.0
    catalog_earned_first_party: 24.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 24.7
    developer_ergonomics: 14.8
    discoverability: 69.6
    operational_transparency: 42.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cz-agents-dev/cz-agents-dev-2026-11-03T130001.png
security:
- kind: domain-security
  name: Cz Agents Dev Domain Security
  slug: cz-agents-dev-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: ares-skill
  slug: cz-agents-dev-ares-skill
- name: dd-skill
  slug: cz-agents-dev-dd-skill
- name: insolvency-skill
  slug: cz-agents-dev-insolvency-skill
slug: cz-agents-dev
tags:
- Company
- MCP
- Czech
- Compliance
- Open Source
- Artificial Intelligence
website: https://cz-agents.dev/
---
