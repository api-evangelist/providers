---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Regal Ai Agentic Access
  operation_count: 9
  slug: regal-ai-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 10
apis:
- description: Regal publishes 40+ reporting webhook event types covering agent activity, call lifecycle (placed, completed, IVR triggered, wrapup), call recording and transcript availability, AI call analysis, task
  name: Regal Reporting Webhooks
  slug: regal-reporting-webhooks
- description: Carrier-level branded caller ID and spam remediation
  name: Regal Branded Phone Numbers API
  slug: regal-ai-branded-phone-numbers-api
- description: The Business Profiles API from Regal — 1 operation(s) for business profiles.
  name: Regal Business Profiles API
  slug: regal-ai-business-profiles-api
- description: The Campaigns API from Regal — 1 operation(s) for campaigns.
  name: Regal Campaigns API
  slug: regal-ai-campaigns-api
- description: The Dispositions API from Regal — 1 operation(s) for dispositions.
  name: Regal Dispositions API
  slug: regal-ai-dispositions-api
- description: Contact creation, update, and custom event tracking
  name: Regal Events API
  slug: regal-ai-events-api
- description: The Messages API from Regal — 1 operation(s) for messages.
  name: Regal Messages API
  slug: regal-ai-messages-api
- description: The Phone Numbers API from Regal — 1 operation(s) for phone numbers.
  name: Regal Phone Numbers API
  slug: regal-ai-phone-numbers-api
- description: List and retrieve Regal user accounts — both human agents and AI agents — with their skills, teams, custom attributes and eligible routing queues. List Users supports cursor pagination and filtering b
  name: Regal Users API
  slug: regal-ai-users-api
- description: Retrieve routing instructions and call metadata after a Regal AI voice agent leaves a live call. The response carries the routing decision (route.type of skill, external, agent or hangup, plus route.v
  name: Regal Call Handoffs API
  slug: regal-ai-call-handoffs-api
artifact_total: 71
asyncapis:
- description: Regal Reporting Webhooks deliver 40+ event types covering agent activity, call lifecycle, recordings and transcripts, AI analysis, tasks, SMS, MMS, email, voicemail, contact lifecycle, scheduling, and
  name: Regal Reporting Webhooks
  slug: regal-reporting-webhooks-asyncapi
collections:
- collection_type: postman
  name: Regal Branded Phone Numbers API
  slug: postman-regal-ai-branded-phone-numbers-api
- collection_type: postman
  name: Regal Branded Phone Numbers Business Profiles API
  slug: postman-regal-ai-business-profiles-api
- collection_type: postman
  name: Regal Branded Phone Numbers Campaigns API
  slug: postman-regal-ai-campaigns-api
- collection_type: postman
  name: Regal Branded Phone Numbers Dispositions API
  slug: postman-regal-ai-dispositions-api
- collection_type: postman
  name: Regal Branded Phone Numbers Events API
  slug: postman-regal-ai-events-api
- collection_type: postman
  name: Regal Branded Phone Numbers Messages API
  slug: postman-regal-ai-messages-api
- collection_type: postman
  name: Regal Branded Phone Numbers API
  slug: postman-regal-ai-phone-numbers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Regal Branded Phone Numbers API
  slug: open-regal-ai-branded-phone-numbers-api
- collection_type: open
  name: Regal Branded Phone Numbers Business Profiles API
  slug: open-regal-ai-business-profiles-api
- collection_type: open
  name: Regal Branded Phone Numbers Campaigns API
  slug: open-regal-ai-campaigns-api
- collection_type: open
  name: Regal Branded Phone Numbers Dispositions API
  slug: open-regal-ai-dispositions-api
- collection_type: open
  name: Regal Branded Phone Numbers Events API
  slug: open-regal-ai-events-api
- collection_type: open
  name: Regal Branded Phone Numbers Messages API
  slug: open-regal-ai-messages-api
- collection_type: open
  name: Regal Branded Phone Numbers API
  slug: open-regal-ai-phone-numbers-api
- collection_type: open
  name: Regal Branded Phone Numbers API
  slug: open-regal-branded-phone-numbers-api
- collection_type: open
  name: Regal Events API
  slug: open-regal-events-api
- collection_type: open
  name: Regal Management API
  slug: open-regal-management-api
- collection_type: open
  name: Regal Messages API
  slug: open-regal-messages-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/regal/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/regal-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/regal-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regal-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/regal-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.regal.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.regal.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.regal.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.regal.ai/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.regal.ai/docs/plan-your-implementation
- group: docs
  title: ''
  type: Documentation
  url: https://developer.regal.ai/llms.txt
- group: operate
  title: ''
  type: FAQ
  url: https://developer.regal.ai/reference/faq
- group: start
  title: ''
  type: SupportPortal
  url: https://support.regal.ai/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://support.regal.ai/hc/en-us/articles/5725458229531-Integration-Guides-API-Docs
- group: start
  title: ''
  type: Login
  url: https://app.regal.io
- group: start
  title: ''
  type: Signup
  url: https://www.regal.ai/get-a-demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.regal.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/regal-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/regal-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/regal-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.regal.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.regal.ai/blog/january-2025-releases
- group: other
  title: ''
  type: Customers
  url: https://www.regal.ai/customers
- group: other
  title: ''
  type: Product
  url: https://www.regal.ai/ai-agents
- group: other
  title: ''
  type: Product
  url: https://www.regal.ai/sales-dialer
- group: other
  title: ''
  type: Product
  url: https://www.regal.ai/journey-builder
- group: other
  title: ''
  type: Product
  url: https://www.regal.ai/conversation-intelligence
- group: company
  title: ''
  type: Careers
  url: https://www.regal.ai/careers
- group: other
  title: ''
  type: Company
  url: https://www.regal.ai/about
- group: operate
  title: ''
  type: Contact
  url: https://www.regal.ai/contact
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.regal.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.regal.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.regal.ai/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regal-ai-official
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/regalio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@regalio
- group: other
  title: ''
  type: Embed
  url: https://developer.regal.ai/docs/salesforce-embed
- group: other
  title: ''
  type: Embed
  url: https://developer.regal.ai/docs/kustomer-embed
- group: other
  title: ''
  type: Embed
  url: https://developer.regal.ai/docs/retool
- group: other
  title: ''
  type: Embed
  url: https://developer.regal.ai/docs/chrome-extension
- group: other
  title: ''
  type: SingleSignOn
  url: https://developer.regal.ai/docs/google-sso
- group: other
  title: ''
  type: SingleSignOn
  url: https://developer.regal.ai/docs/okta-sso
- group: other
  title: ''
  type: SingleSignOn
  url: https://developer.regal.ai/docs/azure-sso
- group: other
  title: ''
  type: SCIM
  url: https://developer.regal.ai/docs/okta-scim
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/regal-ai-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/regal-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/regal-ai-tool-crosswalk.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.regal.ai/docs/regal-mcp
- group: agent
  title: ''
  type: WellKnown
  url: well-known/regal-ai-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/regal-ai-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/regal-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/regal-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/regal-ai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/regal-ai-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/regal-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/regal-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/regal-ai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/regal-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.regal.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/regal-ai-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.regal.io/category/whats-new
- group: start
  title: ''
  type: Sandbox
  url: sandbox/regal-ai-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/regal-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.regal.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/regal-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.regal.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.regal.ai
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/regal-ai-ingest-contact-and-event.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/regal-ai-register-branded-phone-number.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/regal-ai-send-sms.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/regal-ai-resolve-call-handoff.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.regal.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developer.regal.ai/reference/api
- group: operate
  title: ''
  type: Support
  url: https://support.regal.ai/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://www.regal.ai/get-a-demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/regal-ai
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/17258986-81c59f40-7e22-480e-bb40-aa29250b0e35
- group: build
  title: ''
  type: Examples
  url: examples/regal-post-custom-event-example.json
- group: build
  title: ''
  type: Examples
  url: examples/regal-send-message-example.json
- group: build
  title: ''
  type: Examples
  url: examples/regal-post-branded-phone-number-example.json
- group: build
  title: ''
  type: Examples
  url: examples/regal-list-campaigns-example.json
- group: build
  title: ''
  type: Examples
  url: examples/regal-call-completed-webhook-example.json
created: '2026-05-24'
description: Regal is a New York City-based AI Agent Platform purpose-built for contact center operations. The Regal platform lets enterprises design, test, deploy, monitor, and continuously improve AI Phone Agents, SMS Agents, Chat Agents, and WebRTC Voice Agents for inbound and outbound use cases including sales, customer support, scheduling, collections, and lead qualification. The product surface includes an Agent Builder (no-code prompts, actions, knowledge base, variants, languages, LLM models), a Sales Dialer, Journey Builder for orchestrating multi-channel customer experiences, Conversation Intelligence for QA and analytics, and a Copilot that automates agent design. Regal exposes a public REST API spanning a Custom Events ingest endpoint (events.regalvoice.com/events) for contact and event ingestion plus a v1 management API (api.regal.ai/v1) covering Branded Phone Numbers, Business Profiles, Active Phone Numbers, Campaigns, Dispositions, and outbound SMS message sending. The platform
  also publishes 40+ reporting webhook event types covering calls, SMS, MMS, email, voicemail, agent activity, contacts, and journey state, plus a Custom Actions framework that lets voice agents call out to customer-owned HTTP endpoints during conversations. Regal integrates natively with Segment, mParticle, HubSpot, Salesforce, Zendesk, Kustomer, Klaviyo, Braze, Marketo, Customer.io, Iterable, Microsoft Dynamics 365, Zoho, Hightouch, Cal.com, Calendly, Snowflake, S3, Slack, Microsoft Teams, Five9, Talkdesk, and 8x8.
examples:
- key_count: 7
  name: Regal Call Completed Webhook Example
  slug: regal-call-completed-webhook-example
- key_count: 2
  name: Regal List Campaigns Example
  slug: regal-list-campaigns-example
- key_count: 2
  name: Regal Post Branded Phone Number Example
  slug: regal-post-branded-phone-number-example
- key_count: 2
  name: Regal Post Custom Event Example
  slug: regal-post-custom-event-example
- key_count: 2
  name: Regal Send Message Example
  slug: regal-send-message-example
features:
- AI Phone Agents for 24/7 inbound and outbound voice with sub-second latency and 30+ languages
- SMS, Chat, and WebRTC AI Agents sharing the same prompt, knowledge base, and action library
- No-code Agent Builder with prompts, dynamic variables, actions, action sequences, branching, and agent variants
- Custom Actions framework that lets voice agents POST structured payloads to customer HTTP endpoints and branch on the response
- Journey Builder for multi-channel customer journeys including triggered outbound calls gated by TCPA opt-in flags
- Conversation Intelligence with AI call analysis, custom AI analysis and reporting, coverage gap dashboard, and cross-transcript search
- Sales Dialer with batch dialing, outbound routing, branded caller ID, spam remediation, and iOS call screening handling
- Copilot for AI-assisted agent design and tuning
- Single Custom Events ingestion endpoint (events.regalvoice.com/events) with userId/phone/email identity resolution at 300 RPS
- v1 Management API for Business Profiles, Active Phone Numbers, Campaigns, Dispositions, Branded Phone Numbers, and SMS sending
- 40+ reporting webhook event types covering calls, SMS, MMS, email, voicemail, contact lifecycle, scheduling, and custom tasks
- Native data integrations with Segment, mParticle, HubSpot, Salesforce, Zendesk, Kustomer, Klaviyo, Braze, Marketo, Customer.io, Iterable, Microsoft Dynamics 365, Zoho, Hightouch, Cal.com, Calendly, Snowflake Data Share, Amazon S3, Slack, Microsoft Teams, SendGrid, Zapier
- CCaaS integrations with 8x8, Five9, and Talkdesk
- Embeddable iframe for Salesforce, Kustomer, Retool, and Chrome Extension
- SSO via Google, Okta, and Azure; SCIM via Okta
- SOC 2, HIPAA, GDPR, CCPA, and DPA compliance with no customer data used for LLM training
finops:
- name: Regal Ai Finops
  service_category: ''
  slug: regal-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regal-ai.png
json_schemas:
- name: RegalBrandedPhoneNumber
  property_count: 7
  slug: regal-branded-phone-number
- name: RegalContact
  property_count: 6
  slug: regal-contact
- name: RegalEvent
  property_count: 6
  slug: regal-event
- name: RegalMessage
  property_count: 5
  slug: regal-message
json_structures:
- name: Regal Contact Structure
  property_count: 0
  slug: regal-contact-structure
- name: Regal Event Structure
  property_count: 0
  slug: regal-event-structure
jsonld:
- class_count: 41
  name: Regal Ai Context
  property_count: 0
  slug: regal-ai-context
layout: provider
mcp_servers:
- description: ''
  name: Regal MCP
  slug: regal-mcp
modified: '2026-08-14'
name: Regal
nav: Providers
network: true
overview: 'Regal publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Reporting Webhooks, Branded Phone Numbers API, Business Profiles API, and 7 more. Tagged areas include AI, AI Agents, Voice AI, Contact Center, and Outbound Calling.


  The Regal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Regal''s developer surface includes authentication, developer portal, documentation, getting-started guide, FAQ, signup flow, pricing, and 76 more developer resources.'
plans:
- name: Regal Ai Plans Pricing
  plan_count: 1
  slug: regal-ai-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 8
  name: Regal Ai Rate Limits
  slug: regal-ai-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Regal API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: regal-ai-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Regal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: regal-ai-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Regal API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: regal-rules
scopes:
- name: Regal Ai Scopes
  scope_count: 4
  slug: regal-ai-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken
score:
  band: exemplar
  composite: 79.4
  delta: -2.4
  facets:
    access_clarity: 72.4
    commercial_clarity: 72.4
    contract_governance: 59.1
    contract_quality: 80.2
    developer_ergonomics: 63.7
    discoverability: 83.3
    governance: 59.1
    operational_transparency: 76.3
  previous_composite: 81.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regal-ai/refs/heads/main/screenshots/regal-ai-2026-06-20T192753.png
security:
- kind: authentication
  name: Regal Ai Authentication
  slug: regal-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Regal Ai Domain Security
  slug: regal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Regal Ai Vulnerability Disclosure
  slug: regal-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Regal Ai Trust Center
  slug: regal-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR, CCPA
slug: regal-ai
tags:
- AI
- AI Agents
- Voice AI
- Contact Center
- Outbound Calling
- Inbound Calling
- Phone Agents
- SMS
- Chat
- WebRTC
- Conversation Intelligence
- Journey Orchestration
- Branded Caller ID
- CCaaS
- CPaaS
- Sales Dialer
- Customer Engagement
website: https://www.regal.ai/about
---
