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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Notfair Co Agentic Access
  operation_count: 4
  slug: notfair-co-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://notfair.co
  baseurl_source: declared
  description: The Health API from notfair-co — 1 operation(s) for health.
  name: notfair-co Health API
  slug: notfair-co-health-api
- baseURL: https://notfair.co
  baseurl_source: declared
  description: The Mcp API from notfair-co — 1 operation(s) for mcp.
  name: notfair-co MCP API
  slug: notfair-co-mcp-api
- baseURL: https://notfair.co
  baseurl_source: declared
  description: The .well Known API from notfair-co — 2 operation(s) for .well known.
  name: notfair-co .well Known API
  slug: notfair-co-well-known-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/notfair-co/agentic-access/notfair-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/notfair-co-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/notfair-co/plans/notfair-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/notfair-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/notfair-co/rules/notfair-co-rules.yml
  title: ''
  type: Spectral
  url: rules/notfair-co-rules.yml
- group: design
  href: https://artifacts.apis.io/notfair-co/json-ld/notfair-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/notfair-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/notfair-co/vocabulary/notfair-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/notfair-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/notfair-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/notfair-co/data-model/notfair-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/notfair-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/notfair-co/errors/notfair-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/notfair-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/notfair-co/conformance/notfair-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/notfair-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/notfair-co/llms/notfair-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/notfair-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/notfair-co/mcp/notfair-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/notfair-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/notfair-co/well-known/notfair-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/notfair-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/notfair-co/hosts/notfair-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/notfair-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/notfair-co/vendors/notfair-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/notfair-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://notfair.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://notfair.co/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://notfair.co/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/notfair-co/authentication/notfair-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/notfair-co-authentication.yml
- group: auth
  href: https://artifacts.apis.io/notfair-co/security/notfair-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/notfair-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://notfair.co/
- group: docs
  title: ''
  type: Documentation
  url: https://notfair.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://notfair.co/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://notfair.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://notfair.co/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://notfair.co/openapi.json
  - status: 401
    url: https://notfair.co/api/mcp
  - status: 401
    url: https://dev.notfair.co/mcp
  - status: 200
    url: https://notfair.co/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: NotFair provides AI‑powered advertising management across major platforms such as Google, Meta, X (Twitter), LinkedIn, Reddit, TikTok and more. It offers a suite of MCP (Multi‑Channel Platform) servers that integrate ad, analytics, CRM and search‑console data, enabling automated campaign creation, reporting and optimization through AI assistants like Claude and ChatGPT. The platform includes a developer portal, comprehensive documentation, pricing plans, and a blog with guides and best‑practice articles.
image: https://notfair.co/opengraph-image
json_schemas:
- name: McpRequest
  property_count: 0
  slug: notfair-co-mcp-request
- name: McpResponse
  property_count: 0
  slug: notfair-co-mcp-response
- name: ServerCard
  property_count: 5
  slug: notfair-co-server-card
jsonld:
- class_count: 7
  name: Notfair Co Context
  property_count: 23
  slug: notfair-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at notfair.co requiring OAuth.
  name: notfair-co MCP Server
  slug: notfair-co-mcp-yml
modified: '2026-10-30'
name: notfair-co
nav: Providers
network: true
overview: 'notfair-co publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API, MCP API, and .well Known API. Tagged areas include Company, Advertising, Artificial Intelligence, Marketing, and Automation.


  The notfair-co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  notfair-co''s developer surface includes getting-started guide, authentication, documentation, API reference, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Notfair Co Plans Pricing
  plan_count: 2
  slug: notfair-co-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: notfair-co API Rules
  rule_count: 63
  severity_counts:
    error: 59
    hint: 0
    info: 3
    warn: 1
  slug: notfair-co-rules
scopes:
- name: Notfair Co Scopes
  scope_count: 0
  slug: notfair-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 29.2
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/notfair-co/notfair-co-2026-11-03T140336.png
security:
- kind: authentication
  name: Notfair Co Authentication
  slug: notfair-co-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Notfair Co Domain Security
  slug: notfair-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: notfair-co-send-mcp-message
  slug: notfair-co-send-mcp-message
slug: notfair-co
tags:
- Company
- Advertising
- Artificial Intelligence
- Marketing
- Automation
website: https://notfair.co/
---
