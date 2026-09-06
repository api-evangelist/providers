---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.unified.com
  baseurl_source: declared
  description: 'The Unified MCP Service is the company''s agent-facing surface. Its remote Model Context Protocol endpoint at https://mcp.unified.com/mcp answers JSON-RPC over HTTP and is gated by OAuth bearer tokens '
  name: Unified MCP Service
  slug: unified-mcp-service
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unified-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unified.com/
- group: company
  title: ''
  type: Blog
  url: https://www.unified.com/blog/
- group: start
  title: ''
  type: Login
  url: https://get.unified.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unified.com/docs/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unified.com/docs/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unified
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unified-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/unified-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unified-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unified-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unified-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unified-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unified-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unified-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unified-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unified-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unified-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unified-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unified-plans-pricing.yml
created: '2026-09-02'
description: Unified (Unified Enterprise Corp.) is a New York based omnichannel digital advertising company that pairs a purpose-built social advertising insights and investment-intelligence platform with managed campaign services across paid social, programmatic, OTT and digital audio. Client access to the platform runs through the get.unified.com application and a GitBook-hosted documentation space at docs.unified.com that is behind single sign-on. The company also operates a production remote Model Context Protocol server at https://mcp.unified.com/mcp, fronted by its own OAuth authorization server (RFC 8414 metadata, RFC 7591 dynamic client registration, PKCE S256) and an RFC 9728 protected-resource descriptor, plus a FastAPI operations service at api.unified.com that publishes an OpenAPI 3.1 description of its root and health endpoints. iHeartMedia, a long-standing partner and investor, is reported to have acquired the company; Unified continues to operate under its own brand at unified.com.
image: https://cdn.sanity.io/images/o4clnjpa/production/8c1083b248157d01e13c79409ef263fa1397c846-3051x1775.png?w=1200
layout: provider
mcp_servers:
- description: Unified runs a production remote Model Context Protocol server at https://mcp.unified.com/mcp. The service identifies itself on its own root endpoint as "unified-mcp-service" version 0.0.59, build 66,
  name: Unified MCP Service
  slug: unified-mcp-service
modified: '2026-09-02'
name: Unified
nav: Providers
network: true
overview: 'Unified publishes 1 API on the [APIs.io](https://apis.io/) network: MCP Service. Tagged areas include Company, Advertising, Social Media, Digital Advertising, and Marketing.


  Unified''s developer surface includes engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Unified Plans Pricing
  plan_count: 0
  slug: unified-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Unified Rate Limits
  slug: unified-rate-limits
scopes:
- name: Unified Scopes
  scope_count: 0
  slug: unified-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Unified Authentication
  slug: unified-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Unified Domain Security
  slug: unified-domain-security
  summary_line: TLSv1.3 · HSTS
slug: unified
tags:
- Company
- Advertising
- Social Media
- Digital Advertising
- Marketing
- Analytics
- Media
- Agents
- MCP
website: https://www.unified.com/
---
