---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Stable REST API over the Adsmom ad index. 78 operations across Explore (list, hydrate and detail Meta/TikTok/Google/LinkedIn ads, plus reach and impression timeseries and point-in-time snapshots), Ins
  name: Adsmom REST API
  slug: adsmom-rest-api
- description: 'First-party hosted Model Context Protocol server that exposes the same ad index to AI assistants (Claude, Codex, Cursor, Gemini). Streamable HTTP at https://api.adsmom.com/mcp, protected by OAuth 2.0 '
  name: Adsmom MCP Server
  slug: adsmom-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://adsmom.com
- group: docs
  title: ''
  type: Documentation
  url: https://adsmom.com/product/api
- group: docs
  title: ''
  type: APIReference
  url: https://adsmom.com/product/api
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/adsmom-inc-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adsmom-inc-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/adsmom-inc-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adsmom-inc-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adsmom-inc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adsmom-inc-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adsmom-inc-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adsmom-inc-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adsmom-inc-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adsmom-inc-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adsmom-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adsmom-inc-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/adsmom-inc-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adsmom-inc-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adsmom-inc-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://adsmom.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adsmom.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/adsmom-inc-plans.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.adsmom.com/
- group: start
  title: ''
  type: Login
  url: https://app.adsmom.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsmom.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsmom.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adsmom
created: '2026-07-17'
description: Adsmom (SIA Adsmom) is a Latvia-based AI-powered ad intelligence platform that indexes 200M+ ads from Meta, TikTok and Google, decodes them with AI, and gives brands, agencies and research teams a clear read on what competitors are running and what is actually working. The platform covers ad search across a competitor library, spend and creative-strategy insights, an AI chat analyst ("Sense"), real-time competitor alerts, and branded reporting. Adsmom exposes its ad index programmatically via both a hosted Model Context Protocol (MCP) server — for connecting AI assistants such as Claude, Codex, Cursor and Gemini — and a REST API for server-to-server pipelines, internal tools and scheduled jobs. API and MCP access are included on all paid tiers. The REST API publishes a public OpenAPI 3.0.0 description at api.adsmom.com covering 78 operations across four paid-ad platforms (Meta, TikTok, Google, LinkedIn) plus TikTok and Instagram organic accounts, grouped into Explore (ad search
  and hydration), Insights (tracked-advertiser management, AI summaries, weekly reports) and Analytics (reach, activity, share of voice, runtime, creative mix, targeting). Adsmom is a 500 Global portfolio company and raised ~$610K in early 2025.
image: https://adsmom.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: Adsmom Inc. MCP Server
  slug: adsmom-inc-mcp-server
modified: '2026-08-13'
name: Adsmom Inc.
nav: Providers
network: true
overview: 'Adsmom Inc. publishes 1 API on the [APIs.io](https://apis.io/) network: Adsmom REST API. Tagged areas include Company, Advertising, Ad Intelligence, Competitive Intelligence, and Marketing.


  Adsmom Inc.''s developer surface includes documentation, API reference, authentication, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Adsmom Inc Plans
  plan_count: 3
  slug: adsmom-inc-plans
random_paper: 13
rate_limits:
- limit_count: 1
  name: Adsmom Inc Rate Limits
  slug: adsmom-inc-rate-limits
scopes:
- name: Adsmom Inc Scopes
  scope_count: 0
  slug: adsmom-inc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.8
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 30.3
    contract_quality: 44.9
    developer_ergonomics: 32.7
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 7.9
  previous_composite: 43.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adsmom-inc/refs/heads/main/screenshots/adsmom-inc-2026-07-25T181702.png
security:
- kind: authentication
  name: Adsmom Inc Authentication
  slug: adsmom-inc-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Adsmom Inc Domain Security
  slug: adsmom-inc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adsmom-inc
tags:
- Company
- Advertising
- Ad Intelligence
- Competitive Intelligence
- Marketing
- Artificial Intelligence
- MCP
- Software-as-a-Service
- OpenAPI
- REST
- Analytics
- Social-Media
- agent-native
website: https://adsmom.com
---
