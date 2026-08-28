---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.6
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: RESTful API covering the full Leadpages platform across eight documented endpoint categories — Pages, Sites, Assets, Blogs, Analytics, Forms, Domains and Brand Kits — with JSON responses and bearer-to
  name: Leadpages REST API
  slug: leadpages-rest-api
- description: 'Hosted Model Context Protocol server exposing 47 tools across Pages, Sites, Assets, Blogs, Brand Kit and Utility categories, letting AI assistants build, publish, edit and manage landing pages, sites '
  name: Leadpages MCP Server
  slug: leadpages-mcp-server
- description: Agent2Agent endpoint for a nine-agent marketing team — Otto, Piper, Cash, Iris, Ray, Milo, Penn, Vera and Cam — that watches campaigns, proposes optimizations and, with explicit approval, executes cha
  name: Leadpages A2A Agent
  slug: leadpages-a2a-agent
artifact_total: 12
asyncapis:
- description: ''
  name: Leadpages Webhooks
  slug: leadpages-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://leadpages.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://leadpages.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://leadpages.com/developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://leadpages.com/developers/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://leadpages.com/developers/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://leadpages.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://leadpages.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leadpages.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leadpages.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://leadpages.com/contact
- group: company
  title: ''
  type: Blog
  url: https://leadpages.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LeadPages
- group: auth
  title: ''
  type: Security
  url: https://leadpages.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://leadpages.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/leadpages-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadpages-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadpages-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leadpages-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/leadpages-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leadpages-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadpages-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leadpages-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leadpages-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/leadpages-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leadpages-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leadpages-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leadpages-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leadpages-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leadpages-webhooks.yml
created: '2026-08-12'
description: Leadpages is an AI web platform with built-in conversion optimization, part of the Redbrick family of brands. It builds and hosts landing pages, multi-page sites and blogs that improve themselves through A/B testing, Smart Traffic variant routing, click and scroll heatmaps, dynamic text replacement and auto-personalization, with no traffic caps on any plan. For developers and agents it publishes a REST API covering pages, sites, assets, blogs, analytics, forms, custom domains and brand kits; a hosted Model Context Protocol server exposing 47 tools over OAuth 2.0 with PKCE; webhooks for page-publish, lead-capture and form-submission events; and an A2A agent card describing a nine-agent campaign team. Founded 2012 and rebuilt from scratch in 2026.
image: https://leadpages.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Leadpages MCP Server
  slug: leadpages-mcp-server
modified: '2026-08-12'
name: Leadpages
nav: Providers
network: true
overview: 'Leadpages publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Landing Pages, Marketing, Conversion Optimization, and A/B Testing.


  The Leadpages catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leadpages'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 22 more developer resources.'
plans:
- name: Leadpages Plans Pricing
  plan_count: 6
  slug: leadpages-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Leadpages Rate Limits
  slug: leadpages-rate-limits
scopes:
- name: Leadpages Scopes
  scope_count: 11
  slug: leadpages-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 54.7
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 54.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leadpages/refs/heads/main/screenshots/leadpages-2026-08-17T081052.png
security:
- kind: authentication
  name: Leadpages Authentication
  slug: leadpages-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Leadpages Domain Security
  slug: leadpages-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leadpages Vulnerability Disclosure
  slug: leadpages-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Leadpages Trust Center
  slug: leadpages-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: leadpages
tags:
- Company
- Landing Pages
- Marketing
- Conversion Optimization
- A/B Testing
- Website Builder
- Lead Generation
- Content Management
- Agents
- Analytics
website: https://leadpages.com/
---
