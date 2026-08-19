---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for planning and launching guaranteed and auction out-of-home (OOH) campaigns, placing insertion orders, submitting and scheduling creatives, and gathering in-flight delivery reporting. Authe
  name: AdQuick Partner API
  slug: adquick-partner-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.adquick.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.adquick.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adquick.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adquick.com/campaigns
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adquick.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.adquick.com/
- group: operate
  title: ''
  type: Support
  url: https://help.adquick.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adquick
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adquick.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adquick-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adquick-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adquick-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adquick-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adquick-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adquick-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adquick-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adquick-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adquick-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/adquick-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/adquick-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adquick-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adquick-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adquick-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adquick-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/adquick-trust-center.yml
created: '2026-07-17'
description: AdQuick is an intelligence and marketplace platform for out-of-home (OOH) advertising that lets advertisers plan, buy, execute, and measure billboard, transit, street-furniture, and programmatic digital-out-of-home (DOOH) campaigns across a network of 1,500+ media owners covering close to 100% of US OOH supply. AdQuick exposes a partner REST API (X-PARTNER-TOKEN authentication) at api.adquick.com for planning guaranteed and auction OOH campaigns, placing insertion orders, submitting and scheduling creatives, and pulling in-flight delivery reporting, plus a hosted Model Context Protocol (MCP) server (OAuth 2.0 + PKCE) at www.adquick.com/mcp that gives AI agents natural-language access to inventory discovery, campaign management, market analytics, exports, and programmatic DSP tooling. Backed by Initialized Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adquick.png
layout: provider
mcp_servers:
- description: ''
  name: AdQuick MCP Server
  slug: adquick-mcp-server
modified: '2026-08-13'
name: AdQuick
nav: Providers
network: true
overview: 'AdQuick publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Advertising, Out Of Home Advertising, and DOOH.


  AdQuick''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Adquick Plans Pricing
  plan_count: 0
  slug: adquick-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 0
  name: Adquick Rate Limits
  slug: adquick-rate-limits
scopes:
- name: Adquick Scopes
  scope_count: 6
  slug: adquick-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: emerging
  composite: 25.6
  delta: -1.3
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/screenshots/adquick-2026-07-25T181659.png
security:
- kind: authentication
  name: Adquick Authentication
  slug: adquick-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Adquick Domain Security
  slug: adquick-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Adquick Trust Center
  slug: adquick-trust-center
  summary_line: trust center published
slug: adquick
tags:
- Company
- Enterprise Saas
- Advertising
- Out Of Home Advertising
- DOOH
- Programmatic Advertising
- Media Buying
- Marketing
- MCP
website: https://www.adquick.com
---
