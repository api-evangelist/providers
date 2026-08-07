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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for planning and launching guaranteed and auction out-of-home (OOH) campaigns, placing insertion orders, submitting and scheduling creatives, and gathering in-flight delivery reporting. Authe
  name: AdQuick Partner API
  slug: adquick-partner-api
artifact_total: 5
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
created: '2026-07-17'
description: AdQuick is an intelligence and marketplace platform for out-of-home (OOH) advertising that lets advertisers plan, buy, execute, and measure billboard, transit, street-furniture, and programmatic digital-out-of-home (DOOH) campaigns across a network of 1,500+ media owners covering close to 100% of US OOH supply. AdQuick exposes a partner REST API (X-PARTNER-TOKEN authentication) at api.adquick.com for planning guaranteed and auction OOH campaigns, placing insertion orders, submitting and scheduling creatives, and pulling in-flight delivery reporting, plus a hosted Model Context Protocol (MCP) server (OAuth 2.0 + PKCE) at www.adquick.com/mcp that gives AI agents natural-language access to inventory discovery, campaign management, market analytics, exports, and programmatic DSP tooling. Backed by Initialized Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adquick.png
layout: provider
mcp_servers:
- description: ''
  name: AdQuick MCP Server
  slug: adquick-mcp-server
modified: '2026-07-17'
name: AdQuick
nav: Providers
network: true
overview: 'AdQuick publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Advertising, Out Of Home Advertising, and DOOH.


  AdQuick''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 60
scopes:
- name: Adquick Scopes
  scope_count: 6
  slug: adquick-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
  summary_line: TLSv1.3 · DNSSEC · DMARC
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
