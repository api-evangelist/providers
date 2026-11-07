---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Anthra Com Agentic Access
  operation_count: 1
  slug: anthra-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Programmatic access to Anthra API as documented.
  name: Anthra API
  slug: anthra-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/anthra-com/agentic-access/anthra-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anthra-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/anthra-com/rules/anthra-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anthra-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anthra-com/json-ld/anthra-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anthra-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anthra-com/vocabulary/anthra-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anthra-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anthra-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anthra-com/data-model/anthra-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anthra-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/anthra-com/authentication/anthra-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anthra-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/anthra-com/scopes/anthra-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/anthra-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/anthra-com/errors/anthra-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anthra-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anthra-com/conformance/anthra-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anthra-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anthra-com/llms/anthra-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anthra-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anthra-com/mcp/anthra-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anthra-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anthra-com/well-known/anthra-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anthra-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anthra-com/hosts/anthra-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anthra-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anthra-com/vendors/anthra-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anthra-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://anthra.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://anthra.com/changelog
- group: auth
  href: https://artifacts.apis.io/anthra-com/security/anthra-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anthra-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anthra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anthra.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anthra.com/docs/api/books
- group: start
  title: ''
  type: GettingStarted
  url: https://anthra.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://anthra.com/contact
- group: company
  title: ''
  type: Blog
  url: https://anthra.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anthra.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anthra.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://anthra.com/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://anthra.com/api/mcp
  - status: 200
    url: https://anthra.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Anthra is an agentic AI book creator that helps users plan, write, illustrate, and narrate their books. The platform provides AI-driven tools for drafting chapters, generating artwork, creating lifelike narration, and publishing both ebook and print formats. Users can collaborate with the AI co-author, customize story elements, and export finished books as illustrated e‑books, audiobooks, or print‑ready PDFs. Anthra offers a free starter tier and paid plans for advanced features, targeting authors, educators, and creators seeking AI‑enhanced storytelling.
image: https://anthra.com/og.png
jsonld:
- class_count: 3
  name: Anthra Com Context
  property_count: 31
  slug: anthra-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at anthra.com.
  name: Anthra MCP Server
  slug: anthra-com-mcp-yml
modified: '2026-11-01'
name: Anthra
nav: Providers
network: true
overview: 'Anthra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, BookCreation, Writing, Illustration, and Audiobook.


  The Anthra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anthra''s developer surface includes authentication, pricing, changelog, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Anthra Com Plans Pricing
  plan_count: 0
  slug: anthra-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Anthra Com Rate Limits
  slug: anthra-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Anthra API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: anthra-com-rules
scopes:
- name: Anthra Com Scopes
  scope_count: 6
  slug: anthra-com-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    conformance: derived
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
  name: Anthra Com Authentication
  slug: anthra-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Anthra Com Domain Security
  slug: anthra-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anthra-com
tags:
- Artificial Intelligence
- BookCreation
- Writing
- Illustration
- Audiobook
website: https://anthra.com/
---
