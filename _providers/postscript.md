---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Postscript Agentic Access
  operation_count: 20
  slug: postscript-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: Read, filter, page and update a shop's SMS subscribers. Filters use suffixed operators (__eq, __gt, __contains, __in) across created_at, updated_at, email, phone_number, shopify_customer_id and ps_id.
  name: Postscript Subscribers API
  slug: postscript-subscribers-api
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: Send custom events for use in Postscript Flows and triggers.
  name: Postscript Events API
  slug: postscript-events-api
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: Read the opt-in keywords a shop has configured for subscriber acquisition and attribution.
  name: Postscript Keywords API
  slug: postscript-keywords-api
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: Send promotional, transactional or conversational SMS and MMS to an existing subscriber, and read the resulting message request and sent message.
  name: Postscript Messages API
  slug: postscript-messages-api
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: Create, read, update and delete webhook subscriptions, fetch the Postscript-Signature signing token, retrieve example event payloads and trigger test deliveries.
  name: Postscript Webhooks API
  slug: postscript-webhooks-api
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: TCPA opt-out and data redaction for a subscriber, addressable by subscriber id, phone, email or Shopify customer id.
  name: Postscript Compliance API
  slug: postscript-compliance-api
- baseURL: https://api.postscript.io
  baseurl_source: declared
  description: Verify which partner or shop the calling API token resolves to.
  name: Postscript Identity API
  slug: postscript-identity-api
artifact_total: 16
asyncapis:
- description: ''
  name: Postscript Webhooks
  slug: postscript-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/postscript-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-08-13'
name: Postscript
nav: Providers
network: true
overview: 'Postscript publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Subscribers API, Events API, Keywords API, and 4 more. Tagged areas include SMS, Marketing, Messaging, E-Commerce, and Shopify.


  The Postscript catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Postscript''s developer surface includes authentication, changelog, documentation, getting-started guide, API reference, pricing, engineering blog, and 36 more developer resources.'
plans:
- name: Postscript Plans Pricing
  plan_count: 4
  slug: postscript-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Postscript Rate Limits
  slug: postscript-rate-limits
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
- E-Commerce
- Shopify
- RCS
- Subscribers
- Webhook
- Compliance
website: https://postscript.io
---
