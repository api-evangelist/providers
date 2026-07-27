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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 35.6
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Phone.com v4 ("Phoenix") JSON REST API for managing accounts, extensions, devices, phone numbers, call routing, media, messaging (SMS/fax), and event webhooks. OAuth 2.0 secured.
  name: phone-com-api
  slug: phone-com-api
artifact_total: 7
asyncapis:
- description: ''
  name: Phone Com Events Webhooks
  slug: phone-com-events-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.phone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phone.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.phone.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phone.com/aboutdevenv/aboutdevenvhome.html
- group: operate
  title: ''
  type: Support
  url: https://support.phone.com/
- group: company
  title: ''
  type: Blog
  url: https://www.phone.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phonedotcom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.phone.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.phone.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://my.phone.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phone.com/general-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phone.com/privacy-statement/
- group: build
  title: ''
  type: Packages
  url: packages/phone-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/phone-com-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phone-com-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/phone-com-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/phone-com-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/phone-com-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/phone-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/phone-com-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phone-com-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/phone-com-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/phone-com-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/phone-com-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/phone-com-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/phone-com-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/phone-com-events-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/phone-com-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Phone.com is a cloud business phone and unified communications provider for small and mid-sized businesses, offering VoIP calling, SMS/MMS, video conferencing, fax, and virtual phone numbers. Its developer platform is the JSON REST v4 API (codenamed "Phoenix") at api.phone.com, which gives programmatic control over accounts, extensions, devices, phone numbers, call routing (routes, menus, queues, schedules), media, messaging, and an event callback/listener webhook system. Authentication is OAuth 2.0. First-party SDKs are published for Go, Python, PHP, Android, and JavaScript. Surfaced as a portfolio company of Lightspeed Venture Partners and enriched into the API Evangelist network.
image: https://github.com/phonedotcom.png
layout: provider
mcp_servers:
- description: ''
  name: phone-com-mcp.yml
  slug: phone-com-mcpyml
modified: '2026-07-20'
name: Phone Com
nav: Providers
network: true
overview: 'Phone Com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VoIP, Telephony, Business Phone, and SMS.


  The Phone Com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Phone Com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 18
scopes:
- name: Phone Com Scopes
  scope_count: 0
  slug: phone-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 45.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Phone Com Authentication
  slug: phone-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Phone Com Domain Security
  slug: phone-com-domain-security
  summary_line: no transport/DNS hardening detected
- kind: trust-center
  name: Phone Com Trust Center
  slug: phone-com-trust-center
  summary_line: SOC 2 Type 2, HIPAA, PCI DSS
slug: phone-com
tags:
- Company
- VoIP
- Telephony
- Business Phone
- SMS
- Video Conferencing
- Communications
- API
website: https://apidocs.phone.com/
---
