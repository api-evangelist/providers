---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.aivyro.io
  baseurl_source: declared
  description: 'Aivyro API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Aivyro API
  slug: aivyro-io-api
artifact_total: 18
common:
- group: auth
  href: https://artifacts.apis.io/aivyro-io/well-known/aivyro-io-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aivyro-io-www-security.txt
- group: operate
  href: https://artifacts.apis.io/aivyro-io/rate-limits/aivyro-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aivyro-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aivyro-io/plans/aivyro-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aivyro-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/rules/aivyro-io-rules.yml
  title: ''
  type: Spectral
  url: rules/aivyro-io-rules.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/json-ld/aivyro-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aivyro-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/aivyro-io/vocabulary/aivyro-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aivyro-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aivyro-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/data-model/aivyro-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aivyro-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/conventions/aivyro-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aivyro-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/conventions/aivyro-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aivyro-io-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://aivyro.io
- group: auth
  href: https://artifacts.apis.io/aivyro-io/authentication/aivyro-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aivyro-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aivyro-io/scopes/aivyro-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aivyro-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/errors/aivyro-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aivyro-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aivyro-io/conformance/aivyro-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aivyro-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aivyro-io/llms/aivyro-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aivyro-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/aivyro-io/mcp/aivyro-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aivyro-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aivyro-io/well-known/aivyro-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aivyro-io-security.txt
- group: auth
  href: https://artifacts.apis.io/aivyro-io/well-known/aivyro-io-aivyro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aivyro-io-aivyro-security.txt
- group: agent
  href: https://artifacts.apis.io/aivyro-io/well-known/aivyro-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aivyro-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aivyro-io/hosts/aivyro-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aivyro-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aivyro-io/vendors/aivyro-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aivyro-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aivyro.io
- group: start
  title: ''
  type: Login
  url: https://app.aivyro.io/login
- group: auth
  href: https://artifacts.apis.io/aivyro-io/security/aivyro-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aivyro-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aivyro-io/security/aivyro-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aivyro-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aivyro.io/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://knowledge.aivyro.io/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.aivyro.io/en
- group: docs
  title: ''
  type: APIReference
  url: https://www.aivyro.io/en
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aivyro.io/en/demo
- group: operate
  title: ''
  type: Support
  url: https://knowledge.aivyro.io/en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aivyro.io/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.aivyro.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.aivyro.io/en/privacy
created: '2026-11-01'
description: Aivyro is an AI‑powered revenue engineering platform that connects sales channels, CRM systems, and communication tools into a unified workflow. It uses specialized agents to identify opportunities, coordinate decisions, and execute actions, providing forecasting, analytics, and automation to accelerate revenue growth. Founded by Giovanni Colognesi and Armando Rodrigues, Aivyro offers modules for CRM, conversations, outbound prospecting, intelligence, and analytics, all governed by evidence‑backed AI.
image: https://www.aivyro.io/en/opengraph-image
json_schemas:
- name: GetResponse
  property_count: 3
  slug: aivyro-io-get-response
- name: PostAivyroHooksRequest
  property_count: 2
  slug: aivyro-io-post-aivyro-hooks-request
jsonld:
- class_count: 2
  name: Aivyro Io Context
  property_count: 5
  slug: aivyro-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.aivyro.io.
  name: Aivyro MCP Server
  slug: aivyro-io-mcp-yml
modified: '2026-11-01'
name: Aivyro
nav: Providers
network: true
overview: 'Aivyro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Revenue Engineering, Platform, CRM, and Analytics.


  The Aivyro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aivyro''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 29 more developer resources.'
plans:
- name: Aivyro Io Plans Pricing
  plan_count: 5
  slug: aivyro-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Aivyro Io Rate Limits
  slug: aivyro-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Aivyro API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aivyro-io-rules
scopes:
- name: Aivyro Io Scopes
  scope_count: 19
  slug: aivyro-io-scopes
  summary_line: 19 scopes
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 76.8
    catalog_earned_first_party: 20.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 21.7
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 53.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aivyro Io Authentication
  slug: aivyro-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aivyro Io Domain Security
  slug: aivyro-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aivyro Io Vulnerability Disclosure
  slug: aivyro-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: first-session
  slug: aivyro-io-first-session
- name: log-followup
  slug: aivyro-io-log-followup
- name: overview
  slug: aivyro-io-overview
- name: prep-meeting
  slug: aivyro-io-prep-meeting
- name: triage-inbox
  slug: aivyro-io-triage-inbox
- name: update-deal
  slug: aivyro-io-update-deal
slug: aivyro-io
tags:
- Artificial Intelligence
- Revenue Engineering
- Platform
- CRM
- Analytics
website: https://www.aivyro.io/en
---
