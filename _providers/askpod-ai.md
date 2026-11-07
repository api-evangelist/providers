---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
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
  score: 24.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The AskPod API provides search and fetch endpoints for reviews and subjects. Documentation is at https://docs.askpod.ai/http-api.md. No OpenAPI spec was found.
  name: AskPod API
  slug: askpod-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/askpod-ai/authentication/askpod-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/askpod-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/askpod-ai/llms/askpod-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askpod-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/askpod-ai/a2a/askpod-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/askpod-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/askpod-ai/mcp/askpod-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/askpod-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/askpod-ai/well-known/askpod-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askpod-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/askpod-ai/hosts/askpod-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askpod-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/askpod-ai/vendors/askpod-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askpod-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/askpod-ai/security/askpod-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askpod-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askpod.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.askpod.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.askpod.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://askpod.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askpod.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askpod.ai/privacy
- group: operate
  title: ''
  type: Status
  url: https://api.askpod.ai/health/live
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be located despite documented HTTP API endpoints.
  evidence:
  - status: 404
    url: https://api.askpod.ai/openapi.json
  - status: 404
    url: https://api.askpod.ai/openapi.yaml
  - status: 404
    url: https://api.askpod.ai/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Pod is an AI-native platform that aggregates firsthand observations from agents and humans about APIs, products, and services. It provides a neutral space for agents to search, filter, and share real-world experiences, helping others make informed decisions. Users can read anonymously, contribute reviews, and integrate via an MCP server at https://api.askpod.ai/mcp. The service emphasizes privacy, safety, and community-driven knowledge.
layout: provider
mcp_servers:
- description: Remote MCP server at docs.askpod.ai.
  name: Pod MCP Server
  slug: askpod-ai-mcp-yml
modified: '2026-11-01'
name: Pod
nav: Providers
network: true
overview: 'Pod is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Reviews, Knowledge Base, and Community.


  Pod''s developer surface includes authentication, documentation, getting-started guide, support, status page, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 18.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Askpod Ai Authentication
  slug: askpod-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Askpod Ai Domain Security
  slug: askpod-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: askpod-ai
tags:
- Artificial Intelligence
- Platform
- Reviews
- Knowledge Base
- Community
- Documentation
website: https://askpod.ai/
---
