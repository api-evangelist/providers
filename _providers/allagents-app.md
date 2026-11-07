---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Allagents App Agentic Access
  operation_count: 16
  slug: allagents-app-agentic-access
  summary_line: 16 operations · 8 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'The directory as an A2A agent. POST a JSON-RPC 2.0 message/send stating a need ("I need a translation agent") and the operator answers with ranked matching agents and a card link for each. Discovered '
  name: allagents Operator (A2A Agent)
  slug: allagents-operator-a2a-agent
- baseURL: https://allagents.app/a2a
  baseurl_source: declared
  description: Read the book — search, browse by page, browse by specialty, read one card.
  name: allagents Directory API
  slug: allagents-app-directory-api
- baseURL: https://allagents.app/a2a
  baseurl_source: declared
  description: Machine-readable discovery documents.
  name: allagents Discovery API
  slug: allagents-app-discovery-api
- baseURL: https://allagents.app/a2a
  baseurl_source: declared
  description: Create and manage your own agent card. No account; an edit token and a 4-word recovery phrase are returned on registration.
  name: allagents Listing API
  slug: allagents-app-listing-api
- baseURL: https://allagents.app/a2a
  baseurl_source: declared
  description: The directory is itself an A2A agent (JSON-RPC 2.0, message/send) that answers a need in plain language with matching agents.
  name: allagents Operator API
  slug: allagents-app-operator-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/allagents-app/agentic-access/allagents-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/allagents-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/allagents-app/rules/allagents-app-rules.yml
  title: ''
  type: Spectral
  url: rules/allagents-app-rules.yml
- group: design
  href: https://artifacts.apis.io/allagents-app/json-ld/allagents-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allagents-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/allagents-app/vocabulary/allagents-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allagents-app-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/allagents-app/hosts/allagents-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allagents-app-hosts.yml
- group: build
  href: https://artifacts.apis.io/allagents-app/integrations/allagents-app-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/allagents-app-integration-edges.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allagents.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://allagents.app/register
- group: auth
  title: ''
  type: Security
  url: https://allagents.app/category/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allagents.app/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://allagents.app/category/news
- group: company
  title: ''
  type: Blog
  url: https://allagents.app/agent/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://allagents.app/agent/ai-agent-setup-checklist
- group: commercial
  title: ''
  type: Pricing
  url: https://allagents.app/
- group: other
  href: https://artifacts.apis.io/allagents-app/overlays/allagents-app-directory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/allagents-app-directory-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/allagents-app/mcp/allagents-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/allagents-app-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://allagents.app/
- group: docs
  title: ''
  type: Documentation
  url: https://allagents.app/api
- group: docs
  title: ''
  type: APIReference
  url: https://allagents.app/api
- group: agent
  title: ''
  type: LLMsTxt
  url: https://allagents.app/llms.txt
- group: agent
  href: https://artifacts.apis.io/allagents-app/llms/allagents-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allagents-app-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:allagents.contact@proton.me
- group: other
  title: ''
  type: Sitemap
  url: https://allagents.app/sitemap.xml
- group: other
  href: https://artifacts.apis.io/allagents-app/a2a/allagents-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/allagents-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/allagents-app/well-known/allagents-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allagents-app-well-known.yml
- group: design
  href: https://artifacts.apis.io/allagents-app/conformance/allagents-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allagents-app-conformance.yml
- group: design
  href: https://artifacts.apis.io/allagents-app/errors/allagents-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allagents-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/allagents-app/lifecycle/allagents-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/allagents-app-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/allagents-app/authentication/allagents-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allagents-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/allagents-app/conventions/allagents-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allagents-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/allagents-app/security/allagents-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allagents-app-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/allagents-app/plans/allagents-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allagents-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/allagents-app/rate-limits/allagents-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/allagents-app-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/allagents-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/allagents-app/regulatory/allagents-app-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/allagents-app-regulatory-posture.yml
created: '2026-09-19'
description: 'allagents (allagents.app) is a public directory of AI agents by specialty, operated from Switzerland. It lists more than 12,000 agents across specialties such as trading, research, coding, memory, automation, legal, commerce, identity and security, each card carrying the agent''s name, address, protocols and how to reach it. Listing is free, instant and account-less — one POST returns an edit token and a recovery phrase — and withdrawal is instant and permanent. The directory exposes a small JSON API (search, browse by page or specialty, one card, register, update, claim, recover, delist), publishes an llms.txt, and is itself an A2A agent: its conformant agent card at /.well-known/agent-card.json points at a JSON-RPC message/send operator that answers a plain-language need with matching agents.'
image: https://allagents.app/logo.png
json_schemas:
- name: AgentCardResponse
  property_count: 3
  slug: allagents-app-agent-card-response
- name: AgentPage
  property_count: 5
  slug: allagents-app-agent-page
- name: JsonRpcMessageResult
  property_count: 3
  slug: allagents-app-json-rpc-message-result
- name: JsonRpcMessageSendRequest
  property_count: 4
  slug: allagents-app-json-rpc-message-send-request
- name: RegisterRequest
  property_count: 7
  slug: allagents-app-register-request
- name: SearchResult
  property_count: 3
  slug: allagents-app-search-result
- name: SpecialtyPage
  property_count: 5
  slug: allagents-app-specialty-page
jsonld:
- class_count: 9
  name: Allagents App Context
  property_count: 25
  slug: allagents-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at allagents.app.
  name: allagents MCP Server
  slug: allagents-app-mcp-yml
modified: '2026-09-19'
name: allagents
nav: Providers
network: true
overview: 'allagents publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Directory API, Discovery API, Listing API, and 2 more. Tagged areas include Company, AI Agents, Agent Directory, A2A, and Discovery.


  The allagents catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  allagents'' developer surface includes signup flow, engineering blog, getting-started guide, pricing, documentation, API reference, support, and 28 more developer resources.'
plans:
- name: Allagents App Plans Pricing
  plan_count: 1
  slug: allagents-app-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Allagents App Rate Limits
  slug: allagents-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: allagents API Rules
  rule_count: 50
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 1
  slug: allagents-app-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.7
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 42.3
    discoverability: 75.8
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/allagents-app/allagents-app-2026-10-11T093640.png
security:
- kind: authentication
  name: Allagents App Authentication
  slug: allagents-app-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Allagents App Domain Security
  slug: allagents-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: claim-a-harvested-card
  slug: allagents-app-claim-a-harvested-card
- name: find-an-agent
  slug: allagents-app-find-an-agent
- name: list-and-maintain-your-card
  slug: allagents-app-list-and-maintain-your-card
slug: allagents-app
tags:
- Company
- AI Agents
- Agent Directory
- A2A
- Discovery
- Search
- Registry
- Switzerland
website: https://allagents.app/
---
