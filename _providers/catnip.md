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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: Bulk-create WhatsApp contacts inside a Chatfuel automation. POST a list of up to 1,000 E.164 phone numbers plus a contact_data.properties map of custom attributes applied to every contact in the reque
  name: Chatfuel Contacts API
  slug: chatfuel-contacts-api
- description: Programmatically send messages and trigger flows/blocks to a specific bot user on Messenger, Instagram, or WhatsApp. POST to the send endpoint with the bot's unique chatfuel_token and a flow name, blo
  name: Chatfuel Broadcasting API
  slug: chatfuel-broadcasting-api
- description: Manage Chatfuel bots and their Facebook page bindings. Create empty bots, clone content between bots, generate role-scoped invite links (ADMIN, EDITOR, MARKETER, OPERATOR, VIEWER), and bind/unbind bot
  name: Chatfuel Dashboard API
  slug: chatfuel-dashboard-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://chatfuel.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://academy.chatfuel.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.chatfuel.com
- group: docs
  title: ''
  type: APIReference
  url: https://help.chatfuel.com/create-contacts-in-chatfuel-via-api-23134b06ecf8800683b6efacab24b68d
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.chatfuel.com/docs
- group: operate
  title: ''
  type: Support
  url: https://help.chatfuel.com
- group: company
  title: ''
  type: Blog
  url: https://chatfuel.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chatfuel.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://academy.chatfuel.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/catnip-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://chatfuel.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://panel.chatfuel.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatfuel.com/files/TermsOfUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatfuel.com/privacy-policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://chatfuel.com/gdpr
- group: auth
  title: ''
  type: Authentication
  url: authentication/catnip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/catnip-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catnip-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/catnip-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catnip-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/catnip-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/catnip-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/catnip-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/catnip-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/catnip-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/catnip-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/catnip-llms.txt
created: '2026-07-17'
description: 'Catnip Inc is the company behind Chatfuel, an AI-powered business messaging and chatbot automation platform for WhatsApp, Instagram, Facebook Messenger, TikTok and an embeddable website chat widget. Chatfuel lets businesses and agencies build conversational flows, run Meta click-to-WhatsApp ad funnels, qualify leads, book appointments and automate customer support with AI agents. Its developer surface is small and shrinking: the only currently documented API is a Contacts API that bulk-imports up to 1,000 phone numbers into an automation using a Bearer token from Settings, while the older Broadcasting API on api.chatfuel.com and Dashboard API on dashboard.chatfuel.com remain live on the wire but lost their documentation when the docs.chatfuel.com developer help centre was retired. Chatfuel publishes no OpenAPI, but it does serve an llms.txt and a real remote MCP documentation server on its academy docs host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catnip.png
layout: provider
mcp_servers:
- description: 'Chatfuel serves a remote MCP server on its own documentation host. It is a DOCUMENTATION-SEARCH server generated by the Fern docs platform, not a product API server: the single exposed tool performs r'
  name: academy.chatfuel.com docs
  slug: academychatfuelcom-docs
modified: '2026-08-13'
name: Catnip
nav: Providers
network: true
overview: 'Catnip publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chatbots, Messaging, Conversational AI, and Marketing Automation.


  Catnip''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 20 more developer resources.'
plans:
- name: Catnip Plans Pricing
  plan_count: 2
  slug: catnip-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Catnip Rate Limits
  slug: catnip-rate-limits
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 40.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/catnip/refs/heads/main/screenshots/catnip-2026-07-25T204810.png
security:
- kind: authentication
  name: Catnip Authentication
  slug: catnip-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Catnip Domain Security
  slug: catnip-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: catnip
tags:
- Company
- Chatbots
- Messaging
- Conversational AI
- Marketing Automation
- Facebook Messenger
- Instagram
- WhatsApp
- TikTok
- Customer Engagement
- Lead Qualification
website: https://chatfuel.com
---
