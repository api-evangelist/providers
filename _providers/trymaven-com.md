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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Trymaven Com Agentic Access
  operation_count: 11
  slug: trymaven-com-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- baseURL: https://docs.trymaven.com
  baseurl_source: declared
  description: The Health API from Maven — 1 operation(s) for health.
  name: Maven Health API
  slug: trymaven-com-health-api
- baseURL: https://docs.trymaven.com
  baseurl_source: declared
  description: The Public API (v1) API from Maven — 6 operation(s) for public api (v1).
  name: Maven Public API (v1) API
  slug: trymaven-com-public-api-v1-api
- baseURL: https://docs.trymaven.com
  baseurl_source: declared
  description: The Retell API from Maven — 1 operation(s) for retell.
  name: Maven Retell API
  slug: trymaven-com-retell-api
- baseURL: https://docs.trymaven.com
  baseurl_source: declared
  description: The VAPI API from Maven — 1 operation(s) for vapi.
  name: Maven VAPI API
  slug: trymaven-com-vapi-api
- baseURL: https://docs.trymaven.com
  baseurl_source: declared
  description: The Widget Sessions API from Maven — 1 operation(s) for widget sessions.
  name: Maven Widget Sessions API
  slug: trymaven-com-widget-sessions-api
artifact_total: 18
asyncapis:
- description: ''
  name: Trymaven Com Webhooks
  slug: trymaven-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/trymaven-com/agentic-access/trymaven-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trymaven-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/trymaven-com/rules/trymaven-com-rules.yml
  title: ''
  type: Spectral
  url: rules/trymaven-com-rules.yml
- group: design
  href: https://artifacts.apis.io/trymaven-com/json-ld/trymaven-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trymaven-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/trymaven-com/vocabulary/trymaven-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trymaven-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trymaven-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trymaven-com/asyncapi/trymaven-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trymaven-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/trymaven-com/data-model/trymaven-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trymaven-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/trymaven-com/authentication/trymaven-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trymaven-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/trymaven-com/errors/trymaven-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trymaven-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trymaven-com/conformance/trymaven-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trymaven-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trymaven-com/llms/trymaven-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trymaven-com-llms.txt
- group: other
  href: https://artifacts.apis.io/trymaven-com/a2a/trymaven-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/trymaven-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/trymaven-com/mcp/trymaven-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trymaven-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trymaven-com/well-known/trymaven-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trymaven-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/trymaven-com/hosts/trymaven-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trymaven-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trymaven-com/vendors/trymaven-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trymaven-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MavenPayments
- group: auth
  href: https://artifacts.apis.io/trymaven-com/security/trymaven-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trymaven-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trymaven.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.trymaven.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trymaven.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trymaven.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trymaven.com/quickstart.md
- group: operate
  title: ''
  type: Support
  url: https://trust.trymaven.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trymaven.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trymaven.com/privacy
created: '2026-10-24'
description: Maven provides a payments API enabling voice AI agents and chatbots to securely collect credit card payments inline, handling PCI compliance and supporting over 25 payment gateways. Backed by Y Combinator, Maven’s platform lets developers integrate voice or chat payment flows with minimal code, offering SDKs, webhooks, and customizable widgets for seamless checkout experiences.
image: https://trymaven.com/opengraph-image?2af9e901f0448d02
json_schemas:
- name: AuthCheckResponse
  property_count: 4
  slug: trymaven-com-auth-check-response
- name: CreateWidgetSession
  property_count: 6
  slug: trymaven-com-create-widget-session
- name: SessionCreateResponse
  property_count: 5
  slug: trymaven-com-session-create-response
- name: SessionCreate
  property_count: 10
  slug: trymaven-com-session-create
- name: SessionGetResponse
  property_count: 19
  slug: trymaven-com-session-get-response
jsonld:
- class_count: 12
  name: Trymaven Com Context
  property_count: 80
  slug: trymaven-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.trymaven.com.
  name: Maven MCP Server
  slug: trymaven-com-mcp-yml
modified: '2026-10-24'
name: Maven
nav: Providers
network: true
overview: 'Maven publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Public API (v1) API, Retell API, and 2 more. Tagged areas include Payments, Voice AI, Chatbots, Fintech, and Y Combinator.


  The Maven catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Maven''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 21 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Maven API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: trymaven-com-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 62.8
    developer_ergonomics: 35.1
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trymaven-com/trymaven-com-2026-11-03T145149.png
security:
- kind: authentication
  name: Trymaven Com Authentication
  slug: trymaven-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trymaven Com Domain Security
  slug: trymaven-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: trymaven-com-create-and-manage-session
  slug: trymaven-com-create-and-manage-session
slug: trymaven-com
tags:
- Payments
- Voice AI
- Chatbots
- Fintech
- Y Combinator
website: https://trymaven.com
---
