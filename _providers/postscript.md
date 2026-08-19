---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · API access gated to Professional/Enterprise
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Postscript Agentic Access
  operation_count: 20
  slug: postscript-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 8
apis:
- description: The Postscript Partner API v2 enables partners and Shopify shops to manage SMS subscribers, read opt-in keywords, send custom events into Flow Builder, send SMS and MMS messages, configure webhook sub
  name: Postscript Partner API
  slug: postscript-api
- description: Read, filter, page and update a shop's SMS subscribers. Filters use suffixed operators (__eq, __gt, __contains, __in) across created_at, updated_at, email, phone_number, shopify_customer_id and ps_id.
  name: Postscript Subscribers API
  slug: postscript-subscribers-api
- description: Send custom events for use in Postscript Flows and triggers.
  name: Postscript Events API
  slug: postscript-events-api
- description: Read the opt-in keywords a shop has configured for subscriber acquisition and attribution.
  name: Postscript Keywords API
  slug: postscript-keywords-api
- description: Send promotional, transactional or conversational SMS and MMS to an existing subscriber, and read the resulting message request and sent message.
  name: Postscript Messages API
  slug: postscript-messages-api
- description: Create, read, update and delete webhook subscriptions, fetch the Postscript-Signature signing token, retrieve example event payloads and trigger test deliveries.
  name: Postscript Webhooks API
  slug: postscript-webhooks-api
- description: TCPA opt-out and data redaction for a subscriber, addressable by subscriber id, phone, email or Shopify customer id.
  name: Postscript Compliance API
  slug: postscript-compliance-api
- description: Verify which partner or shop the calling API token resolves to.
  name: Postscript Identity API
  slug: postscript-identity-api
artifact_total: 18
asyncapis:
- description: ''
  name: Postscript Webhooks
  slug: postscript-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/postscript-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/postscript-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/postscript-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://postscript.io/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postscript-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postscript-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/postscript-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/postscript-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/postscript-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/postscript-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postscript.io
- group: design
  title: ''
  type: DataModel
  url: data-model/postscript-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/postscript-packages.yml
- group: design
  title: ''
  type: Components
  url: components/postscript-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/postscript-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/postscript-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/postscript-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postscript-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/postscript-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postscript-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/postscript-changelog.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postscriptio
- group: company
  title: ''
  type: Website
  url: https://postscript.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.postscript.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.postscript.io
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.postscript.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.postscript.io/docs/api-authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.postscript.io/docs/rate-limits
- group: auth
  title: ''
  type: Compliance
  url: https://developers.postscript.io/docs/compliance
- group: docs
  title: ''
  type: APIReference
  url: https://developers.postscript.io/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.postscript.io/changelog
- group: build
  title: ''
  type: SDKs
  url: https://developers.postscript.io/docs/javascript-sdk-api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://postscript.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://postscript.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.postscript.io
- group: start
  title: ''
  type: SignUp
  url: https://postscript.io/partners-signup
- group: start
  title: ''
  type: Login
  url: https://app.postscript.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postscript.io/terms-of-service
- group: commercial
  title: ''
  type: APITermsOfService
  url: https://postscript.io/api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postscript.io/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.postscript.io/llms.txt
created: '2025-01-01'
description: Postscript is an SMS and RCS marketing platform built for Shopify brands, covering list growth, campaign and automation delivery, conversational messaging, AI shopping assistants and TCPA compliance. Its developer surface is the Partner API v2 at api.postscript.io, a twenty-operation REST API authenticated with private API keys, through which partners and enterprise shops read and update SMS subscribers, read opt-in keywords, push custom events into Flow Builder, send promotional, transactional and conversational messages, manage webhook subscriptions for shop and subscriber lifecycle events, and run compliance unsubscribe and redaction operations. A browser JavaScript SDK carries the onsite opt-in popups, the checkout consent checkbox and browse-behaviour event tracking.
finops:
- name: Postscript Finops
  service_category: API
  slug: postscript-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postscript.png
layout: provider
mcp_servers:
- description: ''
  name: postscript-mcp.yml
  slug: postscript-mcpyml
modified: '2026-08-13'
name: Postscript
nav: Providers
network: true
overview: 'Postscript publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Partner API, Subscribers API, Events API, and 5 more. Tagged areas include SMS, Marketing, Messaging, E-commerce, and Shopify.


  The Postscript catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Postscript''s developer surface includes authentication, changelog, documentation, getting-started guide, API reference, pricing, engineering blog, and 35 more developer resources.'
plans:
- name: Postscript Plans Pricing
  plan_count: 4
  slug: postscript-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 1
  name: Postscript Rate Limits
  slug: postscript-rate-limits
score:
  band: strong
  composite: 65.5
  delta: 1.9
  facets:
    access_clarity: 96.1
    commercial_clarity: 96.1
    contract_governance: 16.7
    contract_quality: 70.8
    developer_ergonomics: 41.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 59.2
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 46.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postscript/refs/heads/main/screenshots/postscript-2026-06-20T192017.png
security:
- kind: authentication
  name: Postscript Authentication
  slug: postscript-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Postscript Domain Security
  slug: postscript-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Postscript Vulnerability Disclosure
  slug: postscript-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Postscript Trust Center
  slug: postscript-trust-center
  summary_line: SOC 2, GDPR
slug: postscript
tags:
- SMS
- Marketing
- Messaging
- E-commerce
- Shopify
- RCS
- Subscribers
- Webhooks
- Compliance
website: https://postscript.io
---
