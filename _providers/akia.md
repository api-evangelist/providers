---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Akia's REST API (version 3, with version 4 resources for mini apps and reservations) for creating and searching customers and reservations, sending guest messages, reading properties, generating and r
  name: Akia API
  slug: akia-api
- description: Akia's remote Model Context Protocol server, advertised through RFC 9728 OAuth protected-resource metadata at api.akia.com and sys.akia.com. The endpoint requires a Bearer token issued by the Akia aut
  name: Akia MCP Server
  slug: akia-mcp
artifact_total: 9
asyncapis:
- description: ''
  name: Akia Webhooks
  slug: akia-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/akia-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/akia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.akia.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.akia.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.akia.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.akia.com/docs/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.akia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.akia.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.akia.com/demo
- group: start
  title: ''
  type: Login
  url: https://sys.akia.ai
- group: operate
  title: ''
  type: Support
  url: https://www.akia.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.akia.com/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.akia.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.akia.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.akia.com/security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/akia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/akia-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/akia-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/akia-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/akia-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/akia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/akia-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/akia-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/akia-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/akia-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/akia-webhooks.yml
created: '2026-08-06'
description: Akia (The Akia Syndicate) is a San Francisco based hospitality technology company whose AI agent platform automates the guest lifecycle for hotels and vacation rentals — guest messaging over SMS/WhatsApp/web chat, an AI voice agent, digital check-in and pre-registration through Mini Apps, guidebooks, upsells, tipping, tasks, team chat, keyless entry, surveys, reputation management and marketing campaigns. Akia synchronizes with more than fifty property management, smart-lock, payment and operations systems (Opera, Mews, Cloudbeds, Apaleo, StayNTouch, Track, Guesty, RemoteLock, Brivo, Salto KS, Veriff, Stripe) and exposes a partner-gated REST API at api.akia.com/v3 with OAuth 2.0 authorization, a published scope catalog, outbound webhook subscriptions, an embeddable web chat and partner embed SDK, and a remote MCP server at sys.akia.ai/mcp for agent access.
image: https://www.akia.com/icon.png
layout: provider
mcp_servers:
- description: ''
  name: akia-mcp.yml
  slug: akia-mcpyml
modified: '2026-08-06'
name: Akia
nav: Providers
network: true
overview: 'Akia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Hotels, Vacation Rentals, and Guest Experience.


  The Akia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Akia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 58
scopes:
- name: Akia Scopes
  scope_count: 16
  slug: akia-scopes
  summary_line: 16 scopes · authorizationCode
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 18.4
  previous_composite: 53.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akia/refs/heads/main/screenshots/akia-2026-08-07T161133.png
security:
- kind: authentication
  name: Akia Authentication
  slug: akia-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Akia Domain Security
  slug: akia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Akia Vulnerability Disclosure
  slug: akia-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Akia Trust Center
  slug: akia-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: akia
tags:
- Company
- Hospitality
- Hotels
- Vacation Rentals
- Guest Experience
- Messaging
- Artificial Intelligence
- Agents
- Property Management
- Check-In
website: https://www.akia.com/
---
