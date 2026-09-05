---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'An undocumented Model Context Protocol server operated by Apollo Global Management on its own API host. Its existence is established by two first-party discovery documents fetched on 2026-09-04: RFC 8'
  name: Apollo MCP Server
  slug: apollo-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-global-management-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apollo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.com/insights-news
- group: operate
  title: ''
  type: Support
  url: https://www.apollo.com/aboutus/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apollo.com/governance/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apollo.com/governance/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apollo-global-management-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apollo-global-management-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-global-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apollo-global-management-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apollo-global-management-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apollo-global-management-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apollo-global-management-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apollo-global-management-llms.txt
created: '2026-03-21'
description: 'Apollo Global Management (NYSE: APO) is a global alternative asset manager and retirement services provider, running private equity, credit and real assets strategies for institutional investors, family offices and global wealth channels, with over $840 billion in assets under management. Apollo runs no public developer program: it publishes no OpenAPI, GraphQL schema, AsyncAPI, SDK, developer portal or API documentation of any kind, and a full enumeration of its 4,784-URL sitemap contains no /api or /developer path. It does operate one machine-readable surface that was found by probe rather than by documentation — an OAuth 2.0 authorization server on api.apollo.com whose authorization, token and dynamic client registration endpoints sit under /mcp/, fronting a Model Context Protocol resource declared at https://api.apollo.com/.well-known/oauth-protected-resource/mcp. That endpoint is undocumented and not anonymously routable, so its tool surface is unknown.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-global-management.png
layout: provider
mcp_servers:
- description: Apollo Global Management operates a Model Context Protocol server on its own API host. Nothing on any public Apollo page mentions it; it was found by probing api.apollo.com, which serves RFC 8414 auth
  name: Apollo MCP server (api.apollo.com)
  slug: apollo-mcp-server-apiapollocom
modified: '2026-09-04'
name: Apollo Global Management
nav: Providers
network: true
overview: 'Apollo Global Management publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Alternative Investments, Asset Management, Credit, Finance, and Investment Management.


  Apollo Global Management''s developer surface includes engineering blog, support, authentication, and 11 more developer resources.'
plans:
- name: Apollo Global Management Plans Pricing
  plan_count: 0
  slug: apollo-global-management-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Apollo Global Management Rate Limits
  slug: apollo-global-management-rate-limits
scopes:
- name: Apollo Global Management Scopes
  scope_count: 0
  slug: apollo-global-management-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 6.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-global-management/refs/heads/main/screenshots/apollo-global-management-2026-06-20T172312.png
security:
- kind: authentication
  name: Apollo Global Management Authentication
  slug: apollo-global-management-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apollo Global Management Domain Security
  slug: apollo-global-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apollo-global-management
tags:
- Alternative Investments
- Asset Management
- Credit
- Finance
- Investment Management
- Private Equity
- Real Assets
website: https://www.apollo.com/
---
