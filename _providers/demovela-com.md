---
access_model:
  confidence: high
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
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    idempotency: documented
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
  score: 27.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'OAuth-protected Demovela REST API at https://demovela.com/v1, documented on the n8n integration page: six operations (GET /v1/account, GET /v1/templates, GET /v1/videos, GET /v1/videos/:videoId, GET /'
  name: Demovela REST API
  slug: demovela-rest-api
- description: 'Hosted remote MCP server at https://mcp.demovela.com/mcp (OAuth 2.0, scopes profile:read videos:read drafts:write, authorization server demovela.com) exposing six documented tools: get_profile, list_t'
  name: Demovela MCP Server
  slug: demovela-mcp-server
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/demovela-com/plans/demovela-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demovela-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/demovela-com/conventions/demovela-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/demovela-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/demovela-com/conventions/demovela-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/demovela-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/demovela-com/authentication/demovela-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demovela-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/demovela-com/scopes/demovela-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/demovela-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/demovela-com/lifecycle/demovela-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demovela-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/demovela-com/conformance/demovela-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/demovela-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/demovela-com/llms/demovela-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demovela-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/demovela-com/mcp/demovela-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/demovela-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/demovela-com/well-known/demovela-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/demovela-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/demovela-com/hosts/demovela-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demovela-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/demovela-com/vendors/demovela-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/demovela-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/demovela-com/packages/demovela-com-packages.yml
  title: ''
  type: SDKs
  url: packages/demovela-com-packages.yml
- group: build
  href: https://artifacts.apis.io/demovela-com/packages/demovela-com-packages.yml
  title: ''
  type: Packages
  url: packages/demovela-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/demovela-com/security/demovela-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demovela-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demovela.com/
- group: docs
  title: ''
  type: Documentation
  url: https://demovela.com/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://demovela.com/#pricing
- group: start
  title: ''
  type: Login
  url: https://demovela.com/app/
- group: company
  title: ''
  type: Blog
  url: https://demovela.com/articles/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demovela
- group: agent
  title: ''
  type: LLMsTxt
  url: https://demovela.com/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demovela.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demovela.com/privacy/
created: '2026-11-05'
description: 'Demovela is an AI product demo and marketing video maker: from a public HTTPS website URL it generates a launch film, product overview and vertical ad, with optional product recordings or uploads and edits refined through chat. Pricing is credit-based (one credit per finished second; Starter $19, Studio $49, Agency $99 one-time packs, first watermarked film free). It offers an n8n integration node using OAuth sign-in and an OAuth-gated MCP endpoint at demovela.com/mcp for connected MCP apps.'
image: https://demovela.com/media/social-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.demovela.com over streamable HTTP requiring OAuth; 6 tools listed.
  name: Demovela MCP Server
  slug: demovela-mcp-server
modified: '2026-11-05'
name: Demovela
nav: Providers
network: true
overview: 'Demovela is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Video, Product Demos, Marketing Video, and Video Generation.


  Demovela''s developer surface includes authentication, documentation, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Demovela Com Plans Pricing
  plan_count: 4
  slug: demovela-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Demovela Com Rate Limits
  slug: demovela-com-rate-limits
scopes:
- name: Demovela Com Scopes
  scope_count: 3
  slug: demovela-com-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 71.7
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Demovela Com Authentication
  slug: demovela-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Demovela Com Domain Security
  slug: demovela-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: demovela-com
tags:
- Company
- AI Video
- Product Demos
- Marketing Video
- Video Generation
- MCP
- n8n
- Software-as-a-Service
website: https://demovela.com/
---
