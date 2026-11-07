---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Perplexity API (Sonar / Search API): Raw web search results API plus an Agent API that answers with live-web citations.'
  name: Perplexity Sonar API
  slug: perplexity-sonar-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/agentgid-com/rules/agentgid-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentgid-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentgid-com/json-ld/agentgid-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentgid-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentgid-com/vocabulary/agentgid-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentgid-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentgid-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentgid-com/data-model/agentgid-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentgid-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentgid-com/changelog/agentgid-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentgid-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentgid-com/conventions/agentgid-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentgid-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentgid-com/conventions/agentgid-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentgid-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentgid-com/errors/agentgid-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentgid-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentgid-com/conformance/agentgid-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentgid-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentgid-com/llms/agentgid-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentgid-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentgid-com/mcp/agentgid-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentgid-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentgid-com/well-known/agentgid-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentgid-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentgid-com/hosts/agentgid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentgid-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/carbon-intensity/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://agentgid.com/status/
- group: start
  title: ''
  type: Sandbox
  url: https://agentgid.com/apis/sandbox/
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentgid.com/releases/
- group: auth
  href: https://artifacts.apis.io/agentgid-com/security/agentgid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentgid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentgid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentgid.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://agentgid.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://agentgid.com/docs/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://agentgid.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://agentgid.com/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentgid.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://agentgid.com/account/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentgid.com/privacy/
coverage:
  checked: '2026-11-01'
  detail: AgentGid's documentation pages are public HTML but provide no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://agentgid.com/apis/perplexity-sonar/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AgentGid builds AI agent starter kits from tested recipes, providing live data on agents, libraries, APIs and assets such as usage, prices, licenses, limits and status. It offers a live scoreboard for AI agents, tracking package downloads, editor installs, GitHub stars, release activity, pricing and reliability, refreshed daily. The site also supplies documentation, quick-start guides, pricing pages, a contact page for support, and a blog with news and analysis.
image: https://agentgid.com/static/og-image.png
jsonld:
- class_count: 120
  name: Agentgid Com Context
  property_count: 183
  slug: agentgid-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentgid.com.
  name: AgentGid MCP Server
  slug: agentgid-com-mcp-yml
modified: '2026-10-31'
name: AgentGid
nav: Providers
network: true
overview: 'AgentGid publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Data, Marketplace, and Analytics.


  The AgentGid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentGid''s developer surface includes changelog, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AgentGid API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 4
  slug: agentgid-com-rules
scopes:
- name: Agentgid Com Scopes
  scope_count: 0
  slug: agentgid-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 27.9
    discoverability: 56.7
    operational_transparency: 15.8
  previous_composite: 36.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentgid Com Authentication
  slug: agentgid-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentgid Com Domain Security
  slug: agentgid-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: chat-completion
  slug: chat-completion-skill
slug: agentgid-com
tags:
- Artificial Intelligence
- Agents
- Data
- Marketplace
- Analytics
website: https://agentgid.com/
---
