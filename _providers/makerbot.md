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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Bearer-token / OAuth 2.0 authenticated JSON REST API for browsing and managing Thingiverse things (3D models), their files and images, users, collections, categories, tags, and search. Operated by Mak
  name: Thingiverse REST API
  slug: thingiverse-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://makerbot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.thingiverse.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.thingiverse.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.thingiverse.com/developers
- group: auth
  title: ''
  type: Authentication
  url: authentication/makerbot-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/makerbot-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/makerbot-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/makerbot-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/makerbot-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/makerbot-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makerbot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/makerbot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/makerbot-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/makerbot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ultimaker.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makerbot
- group: start
  title: ''
  type: SignUp
  url: https://www.thingiverse.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thingiverse.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thingiverse.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.makerbot.com
created: '2026-07-17'
description: MakerBot is a desktop 3D printer manufacturer, now part of UltiMaker, and the operator of Thingiverse, the largest online community for discovering, sharing, and downloading 3D-printable designs. MakerBot's public developer surface is the Thingiverse REST API (https://api.thingiverse.com), a Bearer-token / OAuth 2.0 authenticated JSON API that exposes things (models), their files and images, users, collections, categories, tags, and full-text search. Developers register an application on the Thingiverse developers site to receive an App Token or run the OAuth 2.0 authorization flow to act on behalf of a Thingiverse user. This profile was surfaced as a venture-backed company and enriched from its live API.
image: https://www.makerbot.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: makerbot-mcp.yml
  slug: makerbot-mcpyml
modified: '2026-07-20'
name: Makerbot
nav: Providers
network: true
overview: 'Makerbot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Manufacturing, Thingiverse, and Maker.


  Makerbot''s developer surface includes documentation, API reference, authentication, signup flow, support, and 15 more developer resources.'
random_paper: 93
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 29.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/makerbot/refs/heads/main/screenshots/makerbot-2026-07-25T225942.png
security:
- kind: authentication
  name: Makerbot Authentication
  slug: makerbot-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Makerbot Domain Security
  slug: makerbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makerbot
tags:
- Company
- 3D Printing
- Manufacturing
- Thingiverse
- Maker
- Hardware
- Designs
- Community
website: https://makerbot.com
---
