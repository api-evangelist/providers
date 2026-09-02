---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Melon's first-party remote Model Context Protocol server, published by Kakao Entertainment's AI Application Technology team. Streamable HTTP transport at https://mcp.melon.com/mcp, OAuth 2.0 authentic
  name: Melon MCP Server
  slug: kakao-entertainment-melon-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kakao-entertainment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kakaoent.com/
- group: company
  title: ''
  type: Blog
  url: https://tech.kakaoent.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://tech.kakaoent.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kakaoent
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kakaoent.com/privacy/policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kakao-entertainment-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kakao-entertainment-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kakao-entertainment-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kakao-entertainment-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kakao-entertainment-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kakao-entertainment-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kakao-entertainment-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kakao-entertainment-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kakao-entertainment-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kakao-entertainment-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kakao-entertainment-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: 'Kakao Entertainment Corp. is the South Korean entertainment subsidiary of Kakao Corp., formed from the 2021 merger of Kakao Page and Kakao M. It operates three business lines — Story (Kakao Page and Kakao Webtoon serialized webtoon and web-novel platforms, plus the overseas Tapas and Radish properties), Music (the Melon streaming service and the StarShip, IST, EDAM and Antenna labels), and Media (film, drama and artist management). Its public machine-readable API surface is agent-native rather than REST: Melon publishes a first-party remote Model Context Protocol (MCP) server at https://mcp.melon.com/mcp, in beta, exposing 18 anonymously-introspectable tools for music search, official Melon charts, artist and album detail, genre browsing, personalized DJ Mallang recommendations, listening history and playlist/playback URL generation. Access is authenticated with OAuth 2.0 against the Melon Alliance Auth v3 platform, which publishes RFC 8414 authorization server metadata and
  an RFC 7591 dynamic client registration endpoint. Kakao Entertainment publishes no OpenAPI, no REST developer portal, and no SDKs; the corporate site and the Melon consumer properties carry no developer program. Kakao Corp''s general developer platform at developers.kakao.com belongs to the parent company and is profiled separately as `kakao`.'
image: https://www.kakaoent.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Kakao Entertainment MCP Server
  slug: kakao-entertainment-mcp-server
modified: '2026-08-23'
name: Kakao Entertainment
nav: Providers
network: true
overview: 'Kakao Entertainment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Entertainment, Music, Streaming, Webtoons, and Publishing.


  Kakao Entertainment''s developer surface includes engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Kakao Entertainment Plans Pricing
  plan_count: 0
  slug: kakao-entertainment-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Kakao Entertainment Rate Limits
  slug: kakao-entertainment-rate-limits
scopes:
- name: Kakao Entertainment Scopes
  scope_count: 10
  slug: kakao-entertainment-scopes
  summary_line: 10 scopes
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 16.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Kakao Entertainment Authentication
  slug: kakao-entertainment-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kakao Entertainment Domain Security
  slug: kakao-entertainment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kakao-entertainment
tags:
- Entertainment
- Music
- Streaming
- Webtoons
- Publishing
- Media
- MCP
- Agents
- South Korea
- Company
website: https://www.kakaoent.com/
---
