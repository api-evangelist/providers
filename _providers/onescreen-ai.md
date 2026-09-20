---
access_model:
  confidence: high
  label: Free public beta, access by request
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.onescreen.ai/mcp/
  - https://mcp.onescreen.ai/.well-known/oauth-protected-resource/mcp
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.6
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: 'OneScreen''s only API surface: a remote Model Context Protocol server over Streamable HTTP that exposes OOH audience personas, market and inventory rankings, geospatial points of interest, media-owner '
  name: OneScreen MCP Server
  slug: onescreen-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://onescreen.ai/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/mcp/onescreen-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/onescreen-ai-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.onescreen.ai/mcp/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/authentication/onescreen-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onescreen-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/scopes/onescreen-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/onescreen-ai-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/well-known/onescreen-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onescreen-ai-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://www.onescreen.ai/robots.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/conformance/onescreen-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onescreen-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/conventions/onescreen-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onescreen-ai-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/plans/onescreen-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onescreen-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/rate-limits/onescreen-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onescreen-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/lifecycle/onescreen-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/onescreen-ai-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/packages/onescreen-ai-packages.yml
  title: ''
  type: Packages
  url: packages/onescreen-ai-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/security/onescreen-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onescreen-ai-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/llms/onescreen-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onescreen-ai-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.onescreen.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.onescreen.ai/contact/
- group: start
  title: ''
  type: Login
  url: https://auth.onescreen.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onescreen.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onescreen.ai/privacy-policy/
created: '2026-07-17'
description: OneScreen AI is a data-driven out-of-home (OOH) advertising company that makes real-world media — billboards, transit, and place-based advertising — as queryable and buyable as any digital channel. It combines more than 1,500 OOH audience personas, close to one million live inventory listings, and audience-based market and inventory recommendation models. OneScreen exposes this OOH intelligence to AI agents through a public Model Context Protocol (MCP) server at https://mcp.onescreen.ai/mcp, protected by OAuth 2.1 with audience-restricted tokens, open dynamic client registration and a published 22-scope permission model — and no REST or GraphQL contract at all. Products include OneScreen Research (free public beta) and OneScreen Planner (closed beta). The company was originally surfaced as a Techstars portfolio lead and is headquartered in Boston, Massachusetts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onescreen-ai.png
layout: provider
mcp_servers:
- description: ''
  name: OneScreen MCP Server
  slug: onescreen-mcp-server
modified: '2026-08-13'
name: OneScreen AI
nav: Providers
network: true
overview: 'OneScreen AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Out-of-Home, Digital Out Of Home, and Advertising Technology.


  OneScreen AI''s developer surface includes documentation, authentication, engineering blog, support, and 16 more developer resources.'
plans:
- name: Onescreen Ai Plans Pricing
  plan_count: 2
  slug: onescreen-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Onescreen Ai Rate Limits
  slug: onescreen-ai-rate-limits
scopes:
- name: Onescreen Ai Scopes
  scope_count: 22
  slug: onescreen-ai-scopes
  summary_line: 22 scopes
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/onescreen-ai/refs/heads/main/screenshots/onescreen-ai-2026-08-07T190340.png
security:
- kind: authentication
  name: Onescreen Ai Authentication
  slug: onescreen-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Onescreen Ai Domain Security
  slug: onescreen-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: onescreen-ai
tags:
- Company
- Advertising
- Out-of-Home
- Digital Out Of Home
- Advertising Technology
- Marketing
- Media
- AI Agents
- MCP
- Authentication
- Agent Readiness
website: https://onescreen.ai/
---
