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
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Castle's REST API for real-time fraud and abuse detection. The Risk API scores authenticated user events (login, transaction, profile update), the Filter API scores anonymous/pre-authentication events
  name: Castle API
  slug: castle-api
artifact_total: 6
asyncapis:
- description: ''
  name: Castle Webhooks
  slug: castle-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/castle-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/castle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://castle.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.castle.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.castle.io/
- group: docs
  title: ''
  type: APIReference
  url: https://reference.castle.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.castle.io/docs/integration-guide
- group: operate
  title: ''
  type: Support
  url: https://castle.io/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.castle.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/castle
- group: commercial
  title: ''
  type: Pricing
  url: https://castle.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.castle.io/signup/new
- group: start
  title: ''
  type: Login
  url: https://dashboard.castle.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blog.castle.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blog.castle.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.castle.io
- group: auth
  title: ''
  type: Compliance
  url: security/castle-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/castle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/castle-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/castle-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/castle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/castle-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/castle-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/castle-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/castle-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/castle-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/castle-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/castle-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/castle-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/castle-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/castle-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Castle is a fraud and account-abuse prevention platform that stops bots, credential stuffing, account takeover, and multi-accounting through behavioral analysis and device fingerprinting — without CAPTCHAs or puzzles for legitimate users. Developers integrate a client-side SDK (browser and mobile) that generates a short-lived request token, then call Castle's backend Risk API and Filter API to score authentication and transaction events in real time. Castle returns machine-learning risk scores and signals (bot, proxy/VPN, residential proxy, impossible travel, device reputation) that drive a policy rules engine, Lists, and webhooks. It serves security and trust-and-safety teams across gaming, fintech, marketplaces, and SaaS.
image: https://castle.io/og.png
layout: provider
mcp_servers:
- description: ''
  name: castle-mcp.yml
  slug: castle-mcpyml
modified: '2026-07-18'
name: Castle
nav: Providers
network: true
overview: 'Castle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Fraud Prevention, Bot Detection, and Device Fingerprinting.


  The Castle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Castle''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 56
score:
  band: developing
  composite: 54.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 54.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/castle/refs/heads/main/screenshots/castle-2026-07-25T204740.png
security:
- kind: authentication
  name: Castle Authentication
  slug: castle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Castle Domain Security
  slug: castle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Castle Trust Center
  slug: castle-trust-center
  summary_line: SOC 2, GDPR
slug: castle
tags:
- Company
- Security
- Fraud Prevention
- Bot Detection
- Device Fingerprinting
- Account Takeover
- Risk Scoring
- Identity
website: https://castle.io
---
