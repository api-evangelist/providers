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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Beliefstate Ai Agentic Access
  operation_count: 40
  slug: beliefstate-ai-agentic-access
  summary_line: 40 operations · 13 acting
api_count: 1
apis:
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Access API from BeliefState — 1 operation(s) for access.
  name: BeliefState Access API
  slug: beliefstate-ai-access-api
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Beliefs API from BeliefState — 1 operation(s) for beliefs.
  name: BeliefState Beliefs API
  slug: beliefstate-ai-beliefs-api
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Brief API from BeliefState — 2 operation(s) for brief.
  name: BeliefState Brief API
  slug: beliefstate-ai-brief-api
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Research API from BeliefState — 18 operation(s) for research.
  name: BeliefState Research API
  slug: beliefstate-ai-research-api
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Research payments API from BeliefState — 16 operation(s) for research payments.
  name: BeliefState Research payments API
  slug: beliefstate-ai-research-payments-api
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Sources API from BeliefState — 1 operation(s) for sources.
  name: BeliefState Sources API
  slug: beliefstate-ai-sources-api
- baseURL: https://beliefstate.ai
  baseurl_source: declared
  description: The Tickers API from BeliefState — 1 operation(s) for tickers.
  name: BeliefState Tickers API
  slug: beliefstate-ai-tickers-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/beliefstate-ai/agentic-access/beliefstate-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beliefstate-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/beliefstate-ai/plans/beliefstate-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beliefstate-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/rules/beliefstate-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/beliefstate-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/json-ld/beliefstate-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beliefstate-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/vocabulary/beliefstate-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beliefstate-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/beliefstate-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/data-model/beliefstate-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beliefstate-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/beliefstate-ai/changelog/beliefstate-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beliefstate-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/conventions/beliefstate-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beliefstate-ai-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://beliefstate.ai/privacy#security
- group: auth
  href: https://artifacts.apis.io/beliefstate-ai/authentication/beliefstate-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beliefstate-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/lifecycle/beliefstate-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beliefstate-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/errors/beliefstate-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beliefstate-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beliefstate-ai/conformance/beliefstate-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beliefstate-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beliefstate-ai/llms/beliefstate-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beliefstate-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/beliefstate-ai/a2a/beliefstate-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beliefstate-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/beliefstate-ai/mcp/beliefstate-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beliefstate-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/beliefstate-ai/well-known/beliefstate-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beliefstate-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/beliefstate-ai/well-known/beliefstate-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beliefstate-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/beliefstate-ai/hosts/beliefstate-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beliefstate-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/beliefstate-ai/vendors/beliefstate-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beliefstate-ai-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beliefstate.ai/api-reference/beliefs/find-investor-beliefs-or-inspect-a-full-record
- group: auth
  href: https://artifacts.apis.io/beliefstate-ai/security/beliefstate-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beliefstate-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beliefstate-ai/security/beliefstate-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beliefstate-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beliefstate.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://beliefstate.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://beliefstate.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beliefstate.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beliefstate.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://beliefstate.ai/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://beliefstate.ai/guides/ai-investing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://beliefstate.ai/openapi.json
  - status: null
    url: https://docs.beliefstate.ai/mcp
  - status: 401
    url: https://beliefstate.ai/mcp
  - status: 200
    url: https://beliefstate.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BeliefState provides an AI-powered platform delivering top analyst research, price targets, and risk assessments directly to AI agents. Users can access curated investment theses, real-time market data, and customizable research feeds, enabling AI-driven decision making and automated analysis across stocks and sectors.
image: https://beliefstate.ai/brand/beliefstate-x-pfp.png
json_schemas:
- name: X402BriefOverview
  property_count: 25
  slug: beliefstate-ai-x402-brief-overview
- name: X402_get_belief_Output
  property_count: 0
  slug: beliefstate-ai-x402-get-belief-output
- name: X402_get_beliefs_Output
  property_count: 0
  slug: beliefstate-ai-x402-get-beliefs-output
- name: X402_get_brief_Output
  property_count: 0
  slug: beliefstate-ai-x402-get-brief-output
- name: X402_get_context_assessment_Output
  property_count: 9
  slug: beliefstate-ai-x402-get-context-assessment-output
- name: X402_list_research_visuals_Output
  property_count: 0
  slug: beliefstate-ai-x402-list-research-visuals-output
jsonld:
- class_count: 23
  name: Beliefstate Ai Context
  property_count: 84
  slug: beliefstate-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.beliefstate.ai.
  name: BeliefState MCP Server
  slug: beliefstate-ai-mcp-yml
modified: '2026-11-02'
name: BeliefState
nav: Providers
network: true
overview: 'BeliefState publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Beliefs API, Brief API, and 4 more. Tagged areas include Artificial Intelligence, Finance, Research, Analytics, and Platform.


  The BeliefState catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BeliefState''s developer surface includes changelog, authentication, API reference, documentation, pricing, support, getting-started guide, and 24 more developer resources.'
plans:
- name: Beliefstate Ai Plans Pricing
  plan_count: 3
  slug: beliefstate-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Beliefstate Ai Rate Limits
  slug: beliefstate-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: BeliefState API Rules
  rule_count: 52
  severity_counts:
    error: 40
    hint: 0
    info: 6
    warn: 6
  slug: beliefstate-ai-rules
scopes:
- name: Beliefstate Ai Scopes
  scope_count: 0
  slug: beliefstate-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 35.0
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beliefstate Ai Authentication
  slug: beliefstate-ai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Beliefstate Ai Domain Security
  slug: beliefstate-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Beliefstate Ai Vulnerability Disclosure
  slug: beliefstate-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: beliefstate
  slug: beliefstate-ai-beliefstate
slug: beliefstate-ai
tags:
- Artificial Intelligence
- Finance
- Research
- Analytics
- Platform
website: https://beliefstate.ai/
---
