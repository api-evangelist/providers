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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'The Unifonic Conversations API sends WhatsApp template and session messages and manages the WhatsApp service: template management and Meta catalog retrieval endpoints, incoming-message and delivery-st'
  name: Unifonic Conversations (WhatsApp) API
  slug: unifonic-conversations-whatsapp-api
- description: The Call Management and Status API from Unifonic — 2 operation(s) for call management and status.
  name: Unifonic Call Management and Status API
  slug: unifonic-call-management-and-status-api
- description: The Call Queue Management API from Unifonic — 2 operation(s) for call queue management.
  name: Unifonic Call Queue Management API
  slug: unifonic-call-queue-management-api
- description: The Number Masking API from Unifonic — 3 operation(s) for number masking.
  name: Unifonic Number Masking API
  slug: unifonic-number-masking-api
- description: The Rest API from Unifonic — 3 operation(s) for rest.
  name: Unifonic Rest API
  slug: unifonic-rest-api
- description: The Verifications API from Unifonic — 2 operation(s) for verifications.
  name: Unifonic Verifications API
  slug: unifonic-verifications-api
- description: The Webhooks API from Unifonic — 1 operation(s) for webhooks.
  name: Unifonic Webhooks API
  slug: unifonic-webhooks-api
- description: The Wrapper API from Unifonic — 2 operation(s) for wrapper.
  name: Unifonic Wrapper API
  slug: unifonic-wrapper-api
artifact_total: 28
asyncapis:
- description: ''
  name: Unifonic Webhooks
  slug: unifonic-webhooks
collections:
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status API
  slug: postman-unifonic-call-management-and-status-api
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status Call Queue Management API
  slug: postman-unifonic-call-queue-management-api
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status Number Masking API
  slug: postman-unifonic-number-masking-api
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status Rest API
  slug: postman-unifonic-rest-api
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status Verifications API
  slug: postman-unifonic-verifications-api
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status Webhooks API
  slug: postman-unifonic-webhooks-api
- collection_type: postman
  name: Unifonic Authenticate Call Management and Status Wrapper API
  slug: postman-unifonic-wrapper-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unifonic Authenticate Call Management and Status API
  slug: open-unifonic-call-management-and-status-api
- collection_type: open
  name: Unifonic Authenticate Call Management and Status Call Queue Management API
  slug: open-unifonic-call-queue-management-api
- collection_type: open
  name: Unifonic Authenticate Call Management and Status Number Masking API
  slug: open-unifonic-number-masking-api
- collection_type: open
  name: Unifonic Authenticate Call Management and Status Rest API
  slug: open-unifonic-rest-api
- collection_type: open
  name: Unifonic Authenticate Call Management and Status Verifications API
  slug: open-unifonic-verifications-api
- collection_type: open
  name: Unifonic Authenticate Call Management and Status Webhooks API
  slug: open-unifonic-webhooks-api
- collection_type: open
  name: Unifonic Authenticate Call Management and Status Wrapper API
  slug: open-unifonic-wrapper-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unifonic-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/unifonic-authenticate-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unifonic/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unifonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unifonic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.unifonic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unifonic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unifonic.com/articles/api-documentation/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unifonic.com/articles/api-documentation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.unifonic.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.unifonic.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unifonic.com/en/pricing
- group: start
  title: ''
  type: Login
  url: https://cloud.unifonic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unifonic.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unifonic.com/en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unifonic.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.unifonic.com/articles/release-notes-publication/2026-release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unifonic-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unifonic-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unifonic-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unifonic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unifonic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unifonic-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/unifonic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unifonic-packages.yml
- group: design
  title: ''
  type: Components
  url: components/unifonic-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unifonic-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unifonic-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unifonic-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unifonic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unifonic-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unifonic-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unifonic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.unifonic.com/en/legal/trust-centre
created: '2026-07-17'
description: Unifonic is a Saudi Arabia-based customer engagement and CPaaS platform, backed by SoftBank Vision Fund, that powers SMS, WhatsApp, voice, push notification, and OTP-verification communication for enterprises across the Middle East and beyond. Its developer surface spans an SMS (NextGen) REST API, an Authenticate API for multi-channel OTP verification, Voice APIs for calls, IVR, and number masking, and a WhatsApp Conversations API with template, session, and management endpoints, alongside webhooks for delivery status and channel events, mobile push SDKs, a web event-tracking SDK, chatbot and Flow Studio automation products, and a WhatsApp sandbox for testing.
image: https://www.unifonic.com/hubfs/UNI_Logo_RGB-01.png
layout: provider
mcp_servers:
- description: Unifonic publishes no official MCP server (no MCP mention in the docs, no official GitHub organization, nothing in the MCP registry). A community-built MCP server exists on npm — @theyahia/unifonic-mc
  name: Unifonic MCP manifest (community server + candidate tools)
  slug: unifonic-mcp-manifest-community-server-candidate-tools
modified: '2026-07-21'
name: Unifonic
nav: Providers
network: true
overview: 'Unifonic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Call Management and Status API, Call Queue Management API, Number Masking API, and 4 more. Tagged areas include Company, Enterprise, CPaaS, Messaging, and SMS.


  The Unifonic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unifonic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, release notes, and 28 more developer resources.'
random_paper: 19
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 64.5
    developer_ergonomics: 78.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 58.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/screenshots/unifonic-2026-08-17T082602.png
security:
- kind: authentication
  name: Unifonic Authentication
  slug: unifonic-authentication
  summary_line: http-basic/apiKey · 4 schemes
- kind: domain-security
  name: Unifonic Domain Security
  slug: unifonic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Unifonic Trust Center
  slug: unifonic-trust-center
  summary_line: ISO 27001, ISO 42001, ISO 27017, ISO 27018, CSA STAR Level 2, SOC 2 Type I, SOC 2 Type II
slug: unifonic
tags:
- Company
- Enterprise
- CPaaS
- Messaging
- SMS
- WhatsApp
- Voice
- Push Notifications
- OTP
- Customer Engagement
- Saudi Arabia
website: https://www.unifonic.com/
---
