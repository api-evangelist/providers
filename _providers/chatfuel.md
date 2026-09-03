---
access_model:
  confidence: high
  label: Self-serve signup with a 7-day free trial
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans/chatfuel-plans-pricing.yml
  - authentication/chatfuel-authentication.yml
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: The only documented Chatfuel API operation as of 2026-08-13. POST https://panel.chatfuel.com/api/contacts/{automation_id}/whatsapp/ imports a batch of up to 1,000 WhatsApp phone numbers into an automa
  name: Chatfuel Contacts API
  slug: chatfuel-contacts-api
- description: HTTP API for sending any block or flow from a bot to a user via a POST request, including targeting users by attribute. Historically rate limited to 25 requests per second per bot and authenticated wi
  name: Chatfuel Broadcasting API
  slug: chatfuel-broadcasting-api
- description: HTTP API to programmatically create and modify bots and pages — create bots, clone bot content, generate role-based invite links, and bind/unbind bots to Facebook pages. Authenticated with a Bearer Da
  name: Chatfuel Dashboard API
  slug: chatfuel-dashboard-api
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.chatfuel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.chatfuel.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.chatfuel.com/create-contacts-in-chatfuel-via-api-23134b06ecf8800683b6efacab24b68d
- group: start
  title: ''
  type: GettingStarted
  url: https://help.chatfuel.com/how-to-set-up-ai:-the-definitive-guide-1b934b06ecf88097b2a3dd91314c1a6b
- group: operate
  title: ''
  type: Support
  url: https://help.chatfuel.com/
- group: company
  title: ''
  type: Blog
  url: https://chatfuel.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatfuel-lab
- group: commercial
  title: ''
  type: Pricing
  url: https://chatfuel.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/chatfuel-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.chatfuel.com/
- group: start
  title: ''
  type: Login
  url: https://app.chatfuel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatfuel.com/files/TermsOfUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatfuel.com/privacy-policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chatfuel.com/
- group: auth
  title: ''
  type: Compliance
  url: https://chatfuel.com/gdpr
- group: company
  title: ''
  type: Website
  url: https://chatfuel.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatfuel-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatfuel-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chatfuel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chatfuel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chatfuel-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatfuel-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/chatfuel-packages.yml
- group: design
  title: ''
  type: Components
  url: components/chatfuel-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chatfuel-llms.txt
created: '2026-07-17'
description: 'Chatfuel is a no-code AI-powered chatbot and business-automation platform for conversational commerce across Meta-owned messaging channels — WhatsApp, Instagram, Facebook Messenger, TikTok, and an embeddable website chat widget. An official Meta Business Partner, Chatfuel lets teams build automated flows and Fuely AI agents that qualify leads, answer customer questions, take bookings, run re-engagement campaigns, and hand off to live agents. Its developer surface is deliberately small and has been shrinking: the single documented HTTP operation is a Contacts API on panel.chatfuel.com that imports up to 1,000 WhatsApp numbers into an automation with a Bearer account token. The older Broadcasting API (api.chatfuel.com) and Dashboard API (dashboard.chatfuel.com/api) still respond, but Chatfuel retired their documentation along with the whole docs.chatfuel.com help center during 2026, leaving no reference, no deprecation notice and no redirect. A live GraphQL gateway runs at panel.chatfuel.com/graphql
  with introspection disabled, and a Swagger route on the API host is walled behind Google SSO. Chatfuel publishes no OpenAPI, no AsyncAPI, no first-party SDK and no MCP server.'
image: https://chatfuel.com/favicons/apple-touch-icon.png
layout: provider
modified: '2026-08-13'
name: Chatfuel
nav: Providers
network: true
overview: 'Chatfuel publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chatbots, Conversational AI, Messaging, and Marketing Automation.


  Chatfuel''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Chatfuel Plans Pricing
  plan_count: 17
  slug: chatfuel-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Chatfuel Rate Limits
  slug: chatfuel-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 40.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatfuel/refs/heads/main/screenshots/chatfuel-2026-07-25T205116.png
security:
- kind: authentication
  name: Chatfuel Authentication
  slug: chatfuel-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Chatfuel Domain Security
  slug: chatfuel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chatfuel
tags:
- Company
- Chatbots
- Conversational AI
- Messaging
- Marketing Automation
- Customer-Support
- WhatsApp
- Instagram
- Facebook Messenger
- TikTok
- No-Code
- AI Agents
website: https://chatfuel.com
---
