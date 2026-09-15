---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-09-14'
api_count: 3
apis:
- description: 'The Unifonic Conversations API sends WhatsApp template and session messages and manages the WhatsApp service: template management and Meta catalog retrieval endpoints, incoming-message and delivery-st'
  name: Unifonic Conversations (WhatsApp) API
  slug: unifonic-conversations-whatsapp-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Call Management and Status API from Unifonic — 2 operation(s) for call management and status.
  name: Unifonic Call Management and Status API
  slug: unifonic-call-management-and-status-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Call Queue Management API from Unifonic — 2 operation(s) for call queue management.
  name: Unifonic Call Queue Management API
  slug: unifonic-call-queue-management-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Number Masking API from Unifonic — 3 operation(s) for number masking.
  name: Unifonic Number Masking API
  slug: unifonic-number-masking-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Rest API from Unifonic — 3 operation(s) for rest.
  name: Unifonic Rest API
  slug: unifonic-rest-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Verifications API from Unifonic — 2 operation(s) for verifications.
  name: Unifonic Verifications API
  slug: unifonic-verifications-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Webhooks API from Unifonic — 1 operation(s) for webhooks.
  name: Unifonic Webhooks API
  slug: unifonic-webhooks-api
- baseURL: https://el.cloud.unifonic.com
  baseurl_source: declared
  description: The Wrapper API from Unifonic — 2 operation(s) for wrapper.
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
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/capabilities/unifonic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/unifonic-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/overlays/unifonic-authenticate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unifonic-authenticate-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unifonic/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/security/unifonic-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/changelog/unifonic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/unifonic-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/lifecycle/unifonic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unifonic-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/errors/unifonic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unifonic-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/authentication/unifonic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unifonic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/conventions/unifonic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unifonic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/conformance/unifonic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unifonic-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/packages/unifonic-packages.yml
  title: ''
  type: Packages
  url: packages/unifonic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/packages/unifonic-packages.yml
  title: ''
  type: SDKs
  url: packages/unifonic-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/components/unifonic-components.yml
  title: ''
  type: Components
  url: components/unifonic-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/data-model/unifonic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unifonic-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/sandbox/unifonic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/unifonic-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/asyncapi/unifonic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/unifonic-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/mcp/unifonic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unifonic-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/llms/unifonic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unifonic-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/well-known/unifonic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unifonic-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unifonic/refs/heads/main/security/unifonic-trust-center.yml
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
  composite: 56.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 63.7
    developer_ergonomics: 74.4
    discoverability: 74.1
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 56.6
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
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
