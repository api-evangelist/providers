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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Wunderkind Agentic Access
  operation_count: 23
  slug: wunderkind-agentic-access
  summary_line: 23 operations · 21 acting
api_count: 7
apis:
- description: 'RESTful endpoints for delivering text messages from platforms external to the Wunderkind ecosystem (ESP, CDP, etc.): single and bulk sends of up to 50,000 messages per request, message status lookup, '
  name: Wunderkind Text Message API
  slug: wunderkind-text-message-api
- description: Email sending operations
  name: Wunderkind Email API
  slug: wunderkind-email-api
- description: The Id Resolution API from Wunderkind — 3 operation(s) for id resolution.
  name: Wunderkind Id Resolution API
  slug: wunderkind-id-resolution-api
- description: The Identity API from Wunderkind — 2 operation(s) for identity.
  name: Wunderkind Identity API
  slug: wunderkind-identity-api
- description: The Send Event API from Wunderkind — 11 operation(s) for send event.
  name: Wunderkind Send Event API
  slug: wunderkind-send-event-api
- description: The Ucrm API from Wunderkind — 2 operation(s) for ucrm.
  name: Wunderkind Ucrm API
  slug: wunderkind-ucrm-api
- description: The Wunderhook API from Wunderkind — 1 operation(s) for wunderhook.
  name: Wunderkind Wunderhook API
  slug: wunderkind-wunderhook-api
artifact_total: 14
asyncapis:
- description: ''
  name: Wunderkind Signals Webhooks
  slug: wunderkind-signals-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wunderkind-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wunderkind-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wunderkind-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wunderkind.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wunderkind.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wunderkind.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wunderkind.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wunderkind.co/docs/msdk-getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.wunderkind.co/hc
- group: company
  title: ''
  type: Blog
  url: https://www.wunderkind.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wunderkind-oss
- group: start
  title: ''
  type: Login
  url: https://platform.wunderkind.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wunderkind.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wunderkind.co/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wunderkind.co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bewunderkind/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wunderkind-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wunderkind-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wunderkind-signals-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/wunderkind-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wunderkind-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wunderkind-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wunderkind-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wunderkind-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wunderkind-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wunderkind-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wunderkind-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wunderkind-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wunderkind-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wunderkind-trust-center.yml
created: '2026-07-17'
description: 'Wunderkind (formerly BounceX) is a performance marketing and identity resolution platform that turns anonymous website and mobile-app traffic into triggered, one-to-one email and text messages. Its Autonomous Marketing Platform pairs an identity graph with AI decisioning, and its Build with Wunderkind developer surface exposes that machinery as APIs: an Identity API for device-ID-to-email resolution, an Event Ingestion API for server-side behavioral events, Email and Text Message send APIs, a UCRM subscribe and unsubscribe API, Signals webhooks that deliver behavioral triggers into ESPs like Klaviyo, Salesforce Marketing Cloud, Braze, and Bloomreach, plus Web and Mobile SDKs for Android, iOS, Flutter, and React Native.'
image: https://avatars.githubusercontent.com/u/197307309?v=4
layout: provider
mcp_servers:
- description: ''
  name: wunderkind-mcp.yml
  slug: wunderkind-mcpyml
modified: '2026-07-21'
name: Wunderkind
nav: Providers
network: true
overview: 'Wunderkind publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Email API, Id Resolution API, Identity API, and 3 more. Tagged areas include Company, Marketing, Personalization, Identity Resolution, and Email.


  The Wunderkind catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wunderkind''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 24 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Wunderkind Rate Limits
  slug: wunderkind-rate-limits
score:
  band: developing
  composite: 50.9
  delta: -3.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wunderkind Authentication
  slug: wunderkind-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Wunderkind Domain Security
  slug: wunderkind-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Wunderkind Trust Center
  slug: wunderkind-trust-center
  summary_line: trust center published
slug: wunderkind
tags:
- Company
- Marketing
- Personalization
- Identity Resolution
- Email
- SMS
- Behavioral Data
- eCommerce
- Webhooks
website: https://www.wunderkind.co
---
