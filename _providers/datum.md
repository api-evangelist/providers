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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Kubernetes-style declarative control-plane API for managing Datum Cloud resources — projects, domains, DNS zones and record sets, gateways, HTTPProxies, HTTPRoutes, traffic protection policies (WAF), '
  name: Datum Cloud API
  slug: datum-cloud-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.datum.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.datum.net/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.datum.net/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.datum.net/docs/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.datum.net/docs/datumctl/quickstart.md
- group: company
  title: ''
  type: Blog
  url: https://www.datum.net/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.datum.net/roadmap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datum-cloud
- group: operate
  title: ''
  type: Support
  url: https://www.datum.net/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datum.net/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.datum.net/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.datumstatus.net
- group: auth
  title: ''
  type: Authentication
  url: authentication/datum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/datum-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.datum.net/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/datum-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.datum.net/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datum-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/datum-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/datum-packages.yml
- group: design
  title: ''
  type: Components
  url: components/datum-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datum-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datum-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datum-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datum-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datum-domain-security.yml
created: '2026-07-17'
description: 'Datum is an open source network cloud built for AI, founded in 2024 and backed by $13.6M from Amplify Partners, CRV, Encoded Ventures, Cervin Ventures, Ex/Ante, Step Function, and Vine Ventures, and founded by Zac Smith and Jacob Smith (ex-Equinix, Packet). Datum gives AI-native developers and alternative cloud providers critical, neutral network infrastructure to compete at scale: an Envoy-based AI Edge with a Coraza OWASP WAF, Layer 7 HTTPProxy/HTTPRoute traffic management, authoritative DNS and programmatic domain management, QUIC-based secure tunnels (Connectors) powered by Iroh, and a Galactic VPC global backbone, all deployed across 17+ global network locations. The platform is exposed through a Kubernetes-style declarative control-plane API at api.datum.net, the datumctl CLI, an official MCP server, and packaged agent Skills, with OAuth 2.0 / OIDC authentication and a forever-free Builder tier. Core platform is licensed AGPLv3.'
image: https://www.datum.net/brand/social/
layout: provider
mcp_servers:
- description: ''
  name: datum-mcp.yml
  slug: datum-mcpyml
modified: '2026-07-18'
name: Datum
nav: Providers
network: true
overview: 'Datum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Cloud, Networking, and Edge.


  Datum''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 65
scopes:
- name: Datum Scopes
  scope_count: 6
  slug: datum-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 33.1
  delta: 0.9
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 32.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/screenshots/datum-2026-07-25T211422.png
security:
- kind: authentication
  name: Datum Authentication
  slug: datum-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Datum Domain Security
  slug: datum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datum
tags:
- Company
- Data
- Cloud
- Networking
- Edge
- AI
- DNS
- Infrastructure
- CDN
- Developer Tools
website: https://www.datum.net/
---
