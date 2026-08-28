---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 233
  human_in_the_loop: 2
  name: Dotdigital Agentic Access
  operation_count: 522
  slug: dotdigital-agentic-access
  summary_line: 522 operations · 233 acting · 2 human-in-the-loop
api_count: 4
apis:
- description: The legacy v2 REST framework, still the only home for many capabilities — email and SMS campaigns, programs and enrolments, pages and forms, documents and images, segments, data fields, preferences an
  name: Dotdigital v2 API
  slug: dotdigital-v2-api
- description: The current v3 REST framework, designed around unified contacts. Per-service paths (/contacts/v3, /insightData/v3, /events/v3, /data-firehose/v3, /configuration, /marketing-email) with seek pagination
  name: Dotdigital v3 API
  slug: dotdigital-v3-api
- description: The Communications Platform as a Service estate under /cpaas — omnichannel outbound and inbound messaging across SMS, MMS, WhatsApp, push, Facebook Messenger and app messaging, plus chat, conversation
  name: Dotdigital CPaaS API
  slug: dotdigital-cpaas-api
- description: A remote MCP server that exposes the Dotdigital OpenAPI corpus and the developer-hub documentation to AI coding tools. Seven read-only tools (list-specs, list-endpoints, get-endpoint, search-endpoints
  name: Dotdigital Marketing Developer Hub MCP Server
  slug: dotdigital-marketing-developer-hub-mcp-server
artifact_total: 58
asyncapis:
- description: ''
  name: Dotdigital Webhooks
  slug: dotdigital-webhooks
collections:
- collection_type: open
  name: Accounts and Utilities
  slug: open-dotdigital-accounts-and-utilities
- collection_type: open
  name: Analytics API
  slug: open-dotdigital-analytics
- collection_type: open
  name: Campaign Templates
  slug: open-dotdigital-campaign-templates
- collection_type: open
  name: Chat Config API
  slug: open-dotdigital-chat-config
- collection_type: open
  name: Chat Message API
  slug: open-dotdigital-chat-message
- collection_type: open
  name: Chat Presence API
  slug: open-dotdigital-chat-presence
- collection_type: open
  name: Chat API
  slug: open-dotdigital-chat
- collection_type: open
  name: Dotdigital Configuration Service
  slug: open-dotdigital-configuration-service
- collection_type: open
  name: Contact data fields
  slug: open-dotdigital-contact-data-fields
- collection_type: open
  name: Contacts
  slug: open-dotdigital-contacts
- collection_type: open
  name: Content API
  slug: open-dotdigital-content
- collection_type: open
  name: Conversation Message API
  slug: open-dotdigital-conversation-message
- collection_type: open
  name: Conversation API
  slug: open-dotdigital-conversation
- collection_type: open
  name: CPaaS API
  slug: open-dotdigital-cpaas
- collection_type: open
  name: Data Firehose
  slug: open-dotdigital-data-firehose
- collection_type: open
  name: Documents
  slug: open-dotdigital-documents
- collection_type: open
  name: Ecommerce
  slug: open-dotdigital-ecommerce
- collection_type: open
  name: Email campaigns
  slug: open-dotdigital-email-campaigns
- collection_type: open
  name: Email contacts
  slug: open-dotdigital-email-contacts
- collection_type: open
  name: Events
  slug: open-dotdigital-events
- collection_type: open
  name: Images
  slug: open-dotdigital-images
- collection_type: open
  name: Insight and transactional data
  slug: open-dotdigital-insight-and-transactional-data
- collection_type: open
  name: Insight data service
  slug: open-dotdigital-insight-data-service
- collection_type: open
  name: Lists / Address books
  slug: open-dotdigital-lists-address-books
- collection_type: open
  name: Marketing Email API
  slug: open-dotdigital-marketing-email
- collection_type: open
  name: Message History API
  slug: open-dotdigital-message-history
- collection_type: open
  name: Message Rules API
  slug: open-dotdigital-message-rules
- collection_type: open
  name: Omnichannel API
  slug: open-dotdigital-omnichannel
- collection_type: open
  name: Pages and forms
  slug: open-dotdigital-pages-and-forms
- collection_type: open
  name: Phone Number Validation API
  slug: open-dotdigital-phone-number-validation
- collection_type: open
  name: Preferences and subscriptions
  slug: open-dotdigital-preferences-and-subscriptions
- collection_type: open
  name: Product recommendations
  slug: open-dotdigital-product-recommendations
- collection_type: open
  name: Profile API
  slug: open-dotdigital-profile
- collection_type: open
  name: Programs
  slug: open-dotdigital-programs
- collection_type: open
  name: Scoring
  slug: open-dotdigital-scoring
- collection_type: open
  name: Segments
  slug: open-dotdigital-segments
- collection_type: open
  name: Session API
  slug: open-dotdigital-session
- collection_type: open
  name: SMS campaigns
  slug: open-dotdigital-sms-campaigns
- collection_type: open
  name: Templates API
  slug: open-dotdigital-templates
- collection_type: open
  name: Transactional email
  slug: open-dotdigital-transactional-email
- collection_type: open
  name: apiconnector.com
  slug: open-dotdigital-v2-api-full
- collection_type: open
  name: Webhook API
  slug: open-dotdigital-webhook
- collection_type: open
  name: WhatsApp Channel API
  slug: open-dotdigital-whatsapp-channel
common:
- group: company
  title: ''
  type: Website
  url: https://dotdigital.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dotdigital.com/
- group: docs
  title: ''
  type: Documentation
  url: https://marketing.developer.dotdigital.com/docs/getting-started-with-the-api
- group: docs
  title: ''
  type: APIReference
  url: https://marketing.developer.dotdigital.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://marketing.developer.dotdigital.com/docs/getting-started-with-the-api
- group: operate
  title: ''
  type: Support
  url: https://support.dotdigital.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.dotdigital.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotmailer
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dotmailer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotdigital
- group: other
  title: ''
  type: X
  url: https://x.com/dotdigital
- group: company
  title: ''
  type: Blog
  url: https://dotdigital.com/blog/
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: start
  title: ''
  type: Login
  url: https://login.dotdigital.com/login.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dotdigital.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dotdigital.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://dotdigitalstatus.com
- group: commercial
  title: ''
  type: Plans
  url: plans/dotdigital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dotdigital-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dotdigital-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/dotdigital-context.jsonld
- group: docs
  title: ''
  type: OpenAPICatalog
  url: https://developer.dotdigital.com/openapi
- group: auth
  title: ''
  type: Authentication
  url: authentication/dotdigital-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dotdigital-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dotdigital-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/dotdigital-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dotdigital-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dotdigital-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dotdigital-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dotdigital-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dotdigital.com/trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dotdigital-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://dotdigital.com/trust-center/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dotdigital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dotdigital-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotdigital-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dotdigital-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/dotdigital-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/dotdigital-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dotdigital-packages.yml
- group: design
  title: ''
  type: Components
  url: components/dotdigital-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dotdigital-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dotdigital-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dotdigital-llms.txt
created: '2026-06-13'
description: 'Dotdigital is a UK-headquartered customer engagement platform (LSE: DOTD) whose Marketing product combines email, SMS, MMS, WhatsApp, push, app messaging, chat and web personalization behind one contact database. Its API estate is unusually large and unusually well published: 42 OpenAPI descriptions are served from a public catalog at developer.dotdigital.com/openapi and enumerated in an RFC 9727 api-catalog linkset, spanning contacts, lists, segments, preferences and consent, email and SMS campaigns, transactional email, programs, pages and forms, insight data, ecommerce, product recommendations, scoring, and the whole CPaaS omnichannel messaging stack. Two frameworks run side by side — legacy v2 at /v2/* and the current v3 services at /<service>/v3/* built around unified contacts — and most integrations need both. Everything authenticates with HTTP Basic API-user credentials against a mandatory regional host (r1 Europe, r2 North America, r3 Asia Pacific). Dotdigital also
  runs a remote MCP server over its developer hub and publishes webhooks, a durable Events in/out API and a Data Firehose for streaming engagement data to cloud storage.'
finops:
- name: Dotdigital Finops
  service_category: ''
  slug: dotdigital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotdigital.png
jsonld:
- class_count: 0
  name: Dotdigital Context
  property_count: 10
  slug: dotdigital-context
layout: provider
mcp_servers:
- description: 'Dotdigital hosts a remote MCP server for the Marketing Developer Hub. It is a documentation-and-specification discovery server, not a data-plane server: the seven tools read the published OpenAPI desc'
  name: Dotdigital MCP Server
  slug: dotdigital-mcp-server
modified: '2026-08-13'
name: Dotdigital
nav: Providers
network: true
overview: 'Dotdigital publishes 3 APIs on the [APIs.io](https://apis.io/) network: v2 API, v3 API, and CPaaS API. Tagged areas include Marketing Automation, Email Marketing, SMS, MMS, and WhatsApp.


  The Dotdigital catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Dotdigital''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 38 more developer resources.'
plans:
- name: Dotdigital Plans Pricing
  plan_count: 1
  slug: dotdigital-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Dotdigital Rate Limits
  slug: dotdigital-rate-limits
score:
  band: strong
  composite: 63.4
  delta: 0.0
  facets:
    access_clarity: 72.4
    commercial_clarity: 72.4
    contract_governance: 16.7
    contract_quality: 69.2
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 52.6
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dotdigital/refs/heads/main/screenshots/dotdigital-2026-06-20T180203.png
security:
- kind: authentication
  name: Dotdigital Authentication
  slug: dotdigital-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dotdigital Domain Security
  slug: dotdigital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dotdigital Vulnerability Disclosure
  slug: dotdigital-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dotdigital Trust Center
  slug: dotdigital-trust-center
  summary_line: ISO 27001, ISO 27701, Cyber Essentials Plus, CSA STAR
slug: dotdigital
tags:
- Marketing Automation
- Email Marketing
- SMS
- MMS
- WhatsApp
- Contacts
- Campaigns
- Push Notifications
- Transactional Email
- Engagement
- Automation
- CPaaS
- Omnichannel
- Customer Data
- Consent Management
- Personalization
- Loyalty
- E-Commerce
- Event
- Webhook
website: https://dotdigital.com
---
