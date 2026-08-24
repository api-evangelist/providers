---
access_model:
  confidence: high
  label: Quote-only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://spotwise.ai/faq
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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: 'The product Model Context Protocol server for Spotwise aOS — the surface an agent connects to in order to reach Spotwise ad detections, leads, contacts and workflows. Streamable HTTP transport. Every '
  name: Spotwise Remote MCP
  slug: spotwise-remote-mcp
- description: A second remote Model Context Protocol server, over the Spotwise marketing site's Payload CMS content. OAuth 2.0 bearer required. It is the only Spotwise surface that declares product-shaped OAuth sco
  name: Spotwise CMS MCP
  slug: spotwise-cms-mcp
- description: 'Payload CMS 3 REST API behind spotwise.ai. Published-content collections answer anonymously — posts, news, pages, media, categories, forms, search, redirects and insights — with page/limit pagination '
  name: Spotwise Content API
  slug: spotwise-content-api
- description: Live GraphQL endpoint served by the same Payload instance. POST only; GET returns 405. Anonymous queries against published content succeed. Introspection is disabled and no SDL is published, so the sc
  name: Spotwise Content GraphQL
  slug: spotwise-content-graphql
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://spotwise.ai
- group: company
  title: ''
  type: Blog
  url: https://spotwise.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://spotwise.ai/faq
- group: start
  title: ''
  type: Login
  url: https://app.spotwise.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spotwise.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spotwise.ai/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpotwiseAI
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spotwise.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/spotwise-inc-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotwise-inc-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spotwise-inc-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spotwise-inc-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spotwise-inc-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spotwise-inc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spotwise-inc-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spotwise-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spotwise-inc-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spotwise-inc-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spotwise-inc-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spotwise-inc-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/spotwise-inc-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/spotwise-inc-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spotwise-inc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spotwise-inc-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spotwise-inc-llms.txt
created: '2026-07-17'
description: Spotwise is an agentic operating system for broadcast media that detects advertising across radio, TV, podcasts, and streaming audio in real time, converts that ad-play data into qualified sales leads with decision-maker enrichment, and automates the outreach and CRM workflows that sell against it. Built by broadcasters and backed by 500 Global, the platform packages products including Spotwise aOS, the Spotty conversational copilot, Spotwise Intelligence, Lead-list, Contact Finder, Monitors & Signals, and Skills for ad-sales and commercial-leadership teams across 14 countries. Spotwise ships two OAuth-protected remote Model Context Protocol servers — a product server at app.spotwise.ai/api/mcp and a content server at spotwise.ai/api/mcp — each advertised by RFC 8414 and RFC 9728 metadata documents, plus a publicly readable Payload CMS REST and GraphQL content API on spotwise.ai. It publishes no OpenAPI, no developer portal, no API reference and no SDK, so the product surface
  its own launch announcement calls "an open API and a Model Context Protocol server" cannot be planned against without an account.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spotwise-inc.png
layout: provider
mcp_servers:
- description: ''
  name: Spotwise Model Context Protocol servers
  slug: spotwise-model-context-protocol-servers
modified: '2026-08-12'
name: Spotwise, Inc.
nav: Providers
network: true
overview: 'Spotwise, Inc. publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Broadcast Media, Advertising, Media Monitoring, and Sales Intelligence.


  Spotwise, Inc.''s developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
plans:
- name: Spotwise Inc Plans Pricing
  plan_count: 0
  slug: spotwise-inc-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Spotwise Inc Rate Limits
  slug: spotwise-inc-rate-limits
scopes:
- name: Spotwise Inc Scopes
  scope_count: 0
  slug: spotwise-inc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Spotwise Inc Authentication
  slug: spotwise-inc-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Spotwise Inc Domain Security
  slug: spotwise-inc-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Spotwise Inc Vulnerability Disclosure
  slug: spotwise-inc-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Spotwise Inc Trust Center
  slug: spotwise-inc-trust-center
  summary_line: trust center published
slug: spotwise-inc
tags:
- Company
- Broadcast Media
- Advertising
- Media Monitoring
- Sales Intelligence
- Lead Generation
- Artificial Intelligence
- Radio
- MCP
- Agents
- Attribution
website: https://spotwise.ai
---
