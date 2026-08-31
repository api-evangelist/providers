---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Admakeai Agentic Access
  operation_count: 65
  slug: admakeai-agentic-access
  summary_line: 65 operations
api_count: 3
apis:
- description: RPC-style JSON REST API with dot-named tRPC procedure paths (e.g. adGeneration.create) covering ad image and UGC video generation, batch ad sets, ad copy, competitor ad research, Meta analytics, and M
  name: AdMakeAI REST API
  slug: admakeai-rest-api
- description: Hosted, stateless streamable-HTTP MCP server exposing 65 tools across account, projects, uploads, ad image generation, ad copy, ad sets, UGC video, competitor research, Meta publishing and Meta analyt
  name: AdMakeAI MCP Server
  slug: admakeai-mcp-server
- description: 'Published SKILL.md that teaches an agent tool selection from natural-language intent, credit mechanics, pagination, destructive-action confirmation, and prompt patterns for ad creative. Installed via '
  name: AdMakeAI Agent Skill
  slug: admakeai-agent-skill
artifact_total: 11
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/admakeai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admakeai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/admakeai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/admakeai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/admakeai-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/admakeai-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/admakeai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/admakeai-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/admakeai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/admakeai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/admakeai-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/admakeai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/admakeai-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admakeai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://admakeai.com/agents
- group: docs
  title: ''
  type: Documentation
  url: https://admakeai.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://admakeai.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://admakeai.com/connect
- group: operate
  title: ''
  type: Support
  url: https://admakeai.com/resources/faq
- group: company
  title: ''
  type: Blog
  url: https://admakeai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://admakeai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admakeai.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://admakeai.com/resources/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://admakeai.com/resources/privacy-policy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mesmerlord/admakeai-mcp
created: '2026-08-11'
description: 'AI ad-creative platform for Meta, Instagram, and TikTok that turns product photos or prompts into finished ad images and UGC-style video ads, batch-generates ad-set variations, generates ad copy, researches competitor ads from the Meta Ad Library, reads Meta campaign analytics, and drafts and publishes campaigns through the official Meta Marketing API. Its machine-readable contract is not an OpenAPI: AdMakeAI is a tRPC application projected two ways, as a hosted streamable-HTTP MCP server at /api/mcp and as 1:1 REST procedure paths at /api/v1, both bound to one account and one credit pool. It implements the full MCP authorization stack (RFC 8414, RFC 9728, RFC 7591, PKCE S256) with three scopes filtered at tools/list, publishes an llms.txt, an MCP server card and an agent-skills index under /.well-known/, and ships a first-party Agent Skill for coding agents.'
image: https://admakeai.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: AdMakeAI MCP Server
  slug: admakeai-mcp-server
- description: ''
  name: AdMakeAI MCP Server
  slug: admakeai-mcp-server-2
modified: '2026-08-11'
name: AdMakeAI
nav: Providers
network: true
overview: 'AdMakeAI publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, AdTech, Generative AI, and Image-Generation.


  AdMakeAI''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Admakeai Plans Pricing
  plan_count: 4
  slug: admakeai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Admakeai Rate Limits
  slug: admakeai-rate-limits
scopes:
- name: Admakeai Scopes
  scope_count: 4
  slug: admakeai-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Admakeai Authentication
  slug: admakeai-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Admakeai Domain Security
  slug: admakeai-domain-security
  summary_line: TLSv1.3
slug: admakeai
tags:
- Advertising
- Marketing
- AdTech
- Generative AI
- Image-Generation
- Video Generation
- Meta Ads
- Competitive Intelligence
- MCP
- Agents
- Agent Skills
website: https://admakeai.com/agents
---
