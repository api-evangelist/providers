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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'REST API for embedded mobile connectivity: manage projects, plans, users, subscriptions, SIMs (eSIM/pSIM), devices, number portings, add-ons, usage and vouchers. Bearer API-key auth, cursor pagination'
  name: Gigs Core API
  slug: gigs-core-api
artifact_total: 6
asyncapis:
- description: ''
  name: Gigs Events Webhooks
  slug: gigs-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://gigs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gigs.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gigs.com/docs/create-a-subscription
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gigs.com/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gigs.com/docs/create-a-subscription
- group: operate
  title: ''
  type: Support
  url: mailto:support@gigs.com
- group: company
  title: ''
  type: Blog
  url: https://gigs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gigs
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.gigs.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.gigs.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gigs.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gigs.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gigs.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gigs.com
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gigs-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gigs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gigs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gigs-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/gigs-decline-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gigs-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gigs-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gigs-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gigs-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gigs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gigs-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gigs-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/gigs-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gigs-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gigs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://gigs.com/security/vulnerability-disclosure
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gigs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Gigs is the operating system for embedded telecom, giving any technology brand the ability to launch and operate mobile phone and data plans without becoming a mobile network operator. The Gigs Core API (base https://api.gigs.com) exposes REST resources for projects, plans, users, addresses, subscriptions, SIMs (eSIM and physical), devices, number portings and port-outs, add-ons, subscription changes, usage and usage balances, and vouchers, secured with per-project Bearer API keys. Gigs also ships Connect (a prebuilt embeddable checkout), integrated Payments, an Operator automation layer, a Dashboard, and a Svix-backed webhook/event stream. Backed by Ribbit Capital and Speedinvest.
image: https://i.gigscdn.net/docs/v1/embedded-connectivity.png
layout: provider
mcp_servers:
- description: ''
  name: gigs-mcp.yml
  slug: gigs-mcpyml
modified: '2026-07-19'
name: Gigs
nav: Providers
network: true
overview: 'Gigs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecom, Connectivity, eSIM, and MVNO.


  The Gigs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gigs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 128
score:
  band: developing
  composite: 49.0
  delta: -0.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 49.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gigs/refs/heads/main/screenshots/gigs-2026-07-25T215810.png
security:
- kind: authentication
  name: Gigs Authentication
  slug: gigs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gigs Domain Security
  slug: gigs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gigs Vulnerability Disclosure
  slug: gigs-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gigs
tags:
- Company
- Telecom
- Connectivity
- eSIM
- MVNO
- Mobile
- Subscriptions
- Payments
- Webhooks
- Embedded Finance
website: https://gigs.com
---
