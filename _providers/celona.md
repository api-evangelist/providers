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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Celona Orchestrator REST API for network monitoring, event querying, device experience, system status, and audit logs. Authenticated with an X-API-Key generated in the Orchestrator.
  name: Celona API
  slug: celona-api
artifact_total: 7
asyncapis:
- description: ''
  name: Celona Events Webhooks
  slug: celona-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://celona.io
- group: start
  title: ''
  type: DeveloperPortal
  url: http://docs.celona.io/en/collections/3911889-developer-documentation
- group: docs
  title: ''
  type: Documentation
  url: http://docs.celona.io/en/
- group: docs
  title: ''
  type: APIReference
  url: http://docs.celona.io/en/articles/13613033-events-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: http://docs.celona.io/en/articles/5471140-introduction-to-celona-apis
- group: operate
  title: ''
  type: Support
  url: https://support.celona.io/
- group: company
  title: ''
  type: Blog
  url: https://www.celona.io/private-mobile-network-blog
- group: start
  title: ''
  type: Login
  url: https://cso.celona.io/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.celona.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.celona.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.celona.io
- group: operate
  title: ''
  type: Deprecation
  url: http://docs.celona.io/en/articles/7828531-api-endpoints-for-events
- group: auth
  title: ''
  type: Authentication
  url: authentication/celona-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/celona-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/celona-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/celona-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/celona-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.celona.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/celona-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.celona.io/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/celona-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celona-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/celona-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/celona-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celona-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Celona provides enterprise private 5G and LTE cellular networking that connects where Wi-Fi cannot reach. The platform combines Celona Edge appliances, indoor and outdoor 5G Access Points, and the cloud-delivered Celona Orchestrator (CSO) for zero-touch provisioning, policy, and lifecycle management over CBRS and shared spectrum. Celona exposes a REST API surface through the Orchestrator for network monitoring, event querying, device experience, system status (Edge and Access Point CPU, memory, and uptime), and account audit logs, authenticated with an X-API-Key generated in the Orchestrator. It serves manufacturing, logistics, healthcare, higher education, oil and gas, and other industries needing mission-critical wireless.
image: https://cdn.prod.website-files.com/5e3277d251fd9e4b90615367/6450b4ba92a91d1652d39d1a_Home.png
layout: provider
mcp_servers:
- description: ''
  name: celona-mcp.yml
  slug: celona-mcpyml
modified: '2026-07-18'
name: Celona
nav: Providers
network: true
overview: 'Celona publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Private Cellular, 5G, and LTE.


  The Celona catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Celona''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 59
score:
  band: developing
  composite: 49.8
  delta: 5.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 42.1
  previous_composite: 43.9
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/celona/refs/heads/main/screenshots/celona-2026-07-25T204906.png
security:
- kind: authentication
  name: Celona Authentication
  slug: celona-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Celona Domain Security
  slug: celona-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Celona Vulnerability Disclosure
  slug: celona-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Celona Trust Center
  slug: celona-trust-center
  summary_line: SOC 2, GDPR
slug: celona
tags:
- Company
- Networking
- Private Cellular
- 5G
- LTE
- CBRS
- Wireless
- Network Monitoring
- Telecommunications
- IoT
website: https://celona.io
---
