---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Public, unauthenticated GET endpoint returning aggregate social sharing metrics for any URL — clicks and shares broken out per network (facebook, twitter, linkedin, pinterest, whatsapp and dozens more
  name: ShareThis Social Share Count API
  slug: sharethis-social-share-count-api
- description: 'First-party remote Model Context Protocol server letting AI assistants create and manage ShareThis properties, validate domain ownership, configure apps and inspect live app output. JSON-RPC 2.0 over '
  name: ShareThis MCP Server
  slug: sharethis-mcp-server
- baseURL: https://platform-api.sharethis.com/v2.0
  baseurl_source: declared
  description: Generates the "Key Observations" summary for the Sharing Intelligence Overview page from a compact, pre-aggregated metrics payload. The OpenAI key stays server-side.
  name: ShareThis AI Summary API
  slug: sharethis-ai-summary-api
- baseURL: https://platform-api.sharethis.com/v2.0
  baseurl_source: declared
  description: ShareThis apps attached to a property
  name: ShareThis Apps API
  slug: sharethis-apps-api
- baseURL: https://platform-api.sharethis.com/v2.0
  baseurl_source: declared
  description: Audience analytics for the Sharing Intelligence page.
  name: ShareThis Audience API
  slug: sharethis-audience-api
- baseURL: https://platform-api.sharethis.com/v2.0
  baseurl_source: declared
  description: Managing user authentication
  name: ShareThis Authentication API
  slug: sharethis-authentication-api
- baseURL: https://platform-api.sharethis.com/v2.0
  baseurl_source: declared
  description: Manage machine-to-machine (client_credentials) OAuth credentials for the authenticated account. Create a client to receive a client_id and a client_secret (shown once), then exchange them at /v2.0/mcp
  name: ShareThis OAuth Clients API
  slug: sharethis-oauth-clients-api
- baseURL: https://platform-api.sharethis.com/v2.0
  baseurl_source: declared
  description: Managing properties. A Property represents a single website or domain and is used to configure and manage multiple apps under that domain.
  name: ShareThis Properties API
  slug: sharethis-properties-api
artifact_total: 14
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/capabilities/sharethis-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sharethis-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/overlays/sharethis-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sharethis-platform-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/security/sharethis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sharethis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sharethis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sharethis.com/platform-api/
- group: docs
  title: ''
  type: Documentation
  url: https://sharethis.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sharethis.com/platform-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://sharethis.com/mcp/
- group: operate
  title: ''
  type: Support
  url: https://sharethis.com/support/
- group: company
  title: ''
  type: Blog
  url: https://sharethis.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://sharethis.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sharethis-github
- group: start
  title: ''
  type: SignUp
  url: https://platform.sharethis.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sharethis.com/publisher-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sharethis.com/privacy/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/packages/sharethis-packages.yml
  title: ''
  type: Packages
  url: packages/sharethis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/packages/sharethis-packages.yml
  title: ''
  type: SDKs
  url: packages/sharethis-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/well-known/sharethis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sharethis-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/llms/sharethis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sharethis-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/conformance/sharethis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sharethis-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/lifecycle/sharethis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sharethis-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/scopes/sharethis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sharethis-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/authentication/sharethis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sharethis-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/conventions/sharethis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sharethis-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/components/sharethis-components.yml
  title: ''
  type: Components
  url: components/sharethis-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/data-model/sharethis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sharethis-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/errors/sharethis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sharethis-problem-types.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/plans/sharethis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sharethis-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/rate-limits/sharethis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sharethis-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/mcp/sharethis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sharethis-mcp.yml
created: '2026-08-27'
description: ShareThis is a Palo Alto, California website-tools and audience-data company, founded in 2007 and now operating as a brand of Predactiv following the 2024 corporate rebrand. Its share, follow, reaction, image and video buttons are embedded across millions of publisher sites via a single sharethis.js loader, and the resulting real-time sharing behavior feeds the company's audience, analytics and targeting data products. For developers ShareThis publishes an OpenAPI 3.0.3-described Platform API for managing properties, app configurations, OAuth clients and AI summaries, an unauthenticated Social Share Count API, and a remote Model Context Protocol server at mcp.sharethis.com that exposes property and app management to AI agents over OAuth.
image: https://sharethis-com.imgix.net/uploads/2016/08/favicon.png
layout: provider
mcp_servers:
- description: First-party remote Model Context Protocol server that exposes ShareThis property and app management to AI assistants. Documented on ShareThis's own site at https://sharethis.com/mcp/ and served from m
  name: ShareThis MCP
  slug: sharethis-mcp
modified: '2026-08-27'
name: ShareThis
nav: Providers
network: true
overview: 'ShareThis publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AI Summary API, Apps API, Audience API, and 5 more. Tagged areas include Company, Social Sharing, Website Tools, Audience Data, and AdTech.


  ShareThis'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Sharethis Plans Pricing
  plan_count: 1
  slug: sharethis-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Sharethis Rate Limits
  slug: sharethis-rate-limits
scopes:
- name: Sharethis Scopes
  scope_count: 0
  slug: sharethis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 47.1
    developer_ergonomics: 66.1
    discoverability: 68.3
    operational_transparency: 2.6
  previous_composite: 45.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/sharethis/refs/heads/main/screenshots/sharethis-2026-09-02T155116.png
security:
- kind: authentication
  name: Sharethis Authentication
  slug: sharethis-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sharethis Domain Security
  slug: sharethis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sharethis
tags:
- Company
- Social Sharing
- Website Tools
- Audience Data
- AdTech
- Analytics
- Consent Management
- Publishing
- MCP
website: https://sharethis.com/
---
