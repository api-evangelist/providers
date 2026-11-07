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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Audit Domains Agentic Access
  operation_count: 10
  slug: audit-domains-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 2
apis:
- baseURL: https://audit.domains
  baseurl_source: declared
  description: Key usage and allowance
  name: audit.domains Account API
  slug: audit-domains-account-api
- baseURL: https://audit.domains
  baseurl_source: declared
  description: Deterministic valuations and comparable sales for one domain
  name: audit.domains Appraisals API
  slug: audit-domains-appraisals-api
- baseURL: https://audit.domains
  baseurl_source: declared
  description: Multi-domain appraisal with reserve-then-settle metering
  name: audit.domains Bulk API
  slug: audit-domains-bulk-api
- baseURL: https://audit.domains
  baseurl_source: declared
  description: The machine API from audit.domains — 1 operation(s) for machine.
  name: audit.domains Machine API
  slug: audit-domains-machine-api
- baseURL: https://audit.domains
  baseurl_source: declared
  description: Recorded domain sales search
  name: audit.domains Sales API
  slug: audit-domains-sales-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/audit-domains/agentic-access/audit-domains-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audit-domains-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/audit-domains/rules/audit-domains-rules.yml
  title: ''
  type: Spectral
  url: rules/audit-domains-rules.yml
- group: design
  href: https://artifacts.apis.io/audit-domains/json-ld/audit-domains-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audit-domains-context.jsonld
- group: design
  href: https://artifacts.apis.io/audit-domains/vocabulary/audit-domains-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audit-domains-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/audit-domains/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/audit-domains/data-model/audit-domains-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audit-domains-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://audit.domains/terms
- group: auth
  href: https://artifacts.apis.io/audit-domains/authentication/audit-domains-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audit-domains-authentication.yml
- group: design
  href: https://artifacts.apis.io/audit-domains/errors/audit-domains-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audit-domains-problem-types.yml
- group: design
  href: https://artifacts.apis.io/audit-domains/conformance/audit-domains-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audit-domains-conformance.yml
- group: agent
  href: https://artifacts.apis.io/audit-domains/llms/audit-domains-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audit-domains-llms.txt
- group: other
  href: https://artifacts.apis.io/audit-domains/a2a/audit-domains-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/audit-domains-a2a.yml
- group: build
  href: https://artifacts.apis.io/audit-domains/mcp/audit-domains-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/audit-domains-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/audit-domains/mcp/audit-domains-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audit-domains-mcp.yml
- group: auth
  href: https://artifacts.apis.io/audit-domains/well-known/audit-domains-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audit-domains-security.txt
- group: agent
  href: https://artifacts.apis.io/audit-domains/well-known/audit-domains-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audit-domains-well-known.yml
- group: other
  href: https://artifacts.apis.io/audit-domains/hosts/audit-domains-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audit-domains-hosts.yml
- group: other
  href: https://artifacts.apis.io/audit-domains/vendors/audit-domains-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audit-domains-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://audit.domains/status
- group: company
  title: ''
  type: Blog
  url: https://audit.domains/blog/how-to-value-a-domain-name/
- group: auth
  href: https://artifacts.apis.io/audit-domains/security/audit-domains-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/audit-domains-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/audit-domains/security/audit-domains-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audit-domains-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audit.domains/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://audit.domains/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://audit.domains/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://audit.domains/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://audit.domains/developers/
- group: operate
  title: ''
  type: Support
  url: https://audit.domains/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://audit.domains/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://audit.domains/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audit.domains/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audit.domains/privacy/
created: '2026-11-02'
description: audit.domains provides professional domain valuation and portfolio intelligence services. It offers sales‑calibrated appraisals, bulk appraisal, portfolio audit, domain analytics, and a certified accuracy model backed by a public methodology. Users can obtain single‑report certificates, explore market intelligence, and integrate the service via a documented API with OpenAPI specifications.
image: https://audit.domains/og-image.png
json_schemas:
- name: Appraisal
  property_count: 14
  slug: audit-domains-appraisal
- name: Comp
  property_count: 6
  slug: audit-domains-comp
- name: SaleRecord
  property_count: 7
  slug: audit-domains-sale-record
jsonld:
- class_count: 17
  name: Audit Domains Context
  property_count: 74
  slug: audit-domains-context
layout: provider
mcp_servers:
- description: Remote MCP server at audit.domains.
  name: audit.domains MCP Server
  slug: audit-domains-mcp-yml
modified: '2026-11-02'
name: audit.domains
nav: Providers
network: true
overview: 'audit.domains publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Appraisals API, Bulk API, and 2 more. Tagged areas include Domain, Valuation, Analytics, and Portfolio.


  The audit.domains catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  audit.domains'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 25 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: audit.domains API Rules
  rule_count: 48
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 1
  slug: audit-domains-rules
scopes:
- name: Audit Domains Scopes
  scope_count: 0
  slug: audit-domains-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 63.1
    developer_ergonomics: 41.0
    discoverability: 56.7
    operational_transparency: 13.2
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Audit Domains Authentication
  slug: audit-domains-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Audit Domains Domain Security
  slug: audit-domains-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Audit Domains Vulnerability Disclosure
  slug: audit-domains-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: appraise-domain
  slug: audit-domains-appraise
slug: audit-domains
tags:
- Domain
- Valuation
- Analytics
- Portfolio
website: https://audit.domains/
---
