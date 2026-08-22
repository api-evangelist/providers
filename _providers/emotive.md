---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.emotive.io/pricing/sms
  - https://help.emotive.io/docs/integrations/open-api-integration-orders
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: The public Emotive Open API for eCommerce integrations — track orders for attribution, opt a phone number out of SMS, and push custom events that can trigger an Emotive Flow. Authenticated with an Emo
  name: Emotive Open API
  slug: emotive-open-api
- description: List Growth API for opting customers in to SMS and email from an external system. Returns the active signup flows (subscriber lists) a subscriber can be added to.
  name: Emotive Lists API (Subscriber Engine)
  slug: emotive-lists-api-subscriber-engine
- description: Inbound webhook receiver on the Emotive API gateway — create subscribers singly and in bulk, set profile properties, and receive Shopify, Twilio and Alloy callbacks. This is the API behind the documen
  name: Emotive Sensus Webhooks API
  slug: emotive-sensus-webhooks-api
- description: Connect a custom helpdesk to Emotive — register a ticket-system connection, mint a brand token, configure webhooks for ticket creation and updates, and post ticket events back to Emotive. Emotive's kn
  name: Emotive Helpdesk API
  slug: emotive-helpdesk-api
- description: Emotive's authentication and tenancy service — OAuth token issuance, Auth0, Google and Shopify login legs, JWT claims, brand and user management, roles, invitations, products and the Zapier app key ch
  name: Emotive Auth Server API
  slug: emotive-auth-server-api
- description: Create, retrieve, update and archive audience segments used to target SMS broadcasts and flows.
  name: Emotive Segments API
  slug: emotive-segments-api
- description: Read campaign and campaign-step analytics for an Emotive Experience (Flow).
  name: Emotive Experiences API
  slug: emotive-experiences-api
- description: 'Anonymous remote MCP server published by Emotive''s Mintlify knowledge base. Three tools — documentation search, a read-only virtual filesystem over the docs, and documentation feedback. Verified live '
  name: Emotive Knowledge Base MCP Server
  slug: emotive-knowledge-base-mcp-server
artifact_total: 14
asyncapis:
- description: ''
  name: Emotive Webhooks
  slug: emotive-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.emotive.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.emotive.io/pricing/sms
- group: company
  title: ''
  type: Blog
  url: https://www.emotive.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.emotive.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emotive.io/privacy
- group: start
  title: ''
  type: Login
  url: https://www.emotiveapp.co/
- group: operate
  title: ''
  type: Support
  url: https://www.emotive.io/customer-success
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.emotive.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.emotive.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://emotive.gitbook.io/emotive-lists
- group: docs
  title: ''
  type: APIReference
  url: https://emotive.gitbook.io/emotive-lists/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://emotive.gitbook.io/emotive-lists/integration-setup-instructions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emotive.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emotive-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emotive-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emotive-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/emotive-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/emotive-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emotive-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/emotive-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/emotive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emotive-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/emotive-components.yml
created: '2026-07-17'
description: 'Emotive is an SMS marketing platform for eCommerce brands, combining two-way conversational text messaging, behavioral triggers, and automation with a dedicated managed service (TextPros) of ex-agency SMS strategists and copywriters. Its products include SMS Marketing campaigns and flows, CartAI cart-recovery pixel technology, multi-touch Attribution analytics, RealLink branded short links, and integrations with eCommerce platforms, email service providers, and business tools. Emotive markets a "5X ROI guarantee" to Shopify and other direct-to-consumer merchants. The company was surfaced as a portfolio company of CRV and was acquired by Privy. Emotive runs a real, publicly documented developer surface: an Open API for order tracking, manual opt-outs and custom events on api.emotiveapp.co; a Lists / Subscriber API documented in GitBook; and an API gateway at api-gw.emotiveapp.co that serves five OpenAPI 3.0.2 documents (Helpdesk, Sensus Webhooks, Auth Server, Segments, Experiences).
  Its Mintlify knowledge base publishes an llms.txt, an A2A agent card, a packaged Agent Skill and an anonymous remote MCP server.'
image: https://www.emotive.io/assets/brand/emotive-symbol-blue-on-transparent.png
layout: provider
mcp_servers:
- description: ''
  name: emotive-mcp.yml
  slug: emotive-mcpyml
modified: '2026-08-13'
name: Emotive
nav: Providers
network: true
overview: 'Emotive publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Open API, Lists API (Subscriber Engine), Sensus Webhooks API, and 4 more. Tagged areas include Company, Marketing, SMS, Messaging, and eCommerce.


  The Emotive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Emotive''s developer surface includes pricing, engineering blog, support, documentation, API reference, getting-started guide, and 18 more developer resources.'
plans:
- name: Emotive Plans Pricing
  plan_count: 0
  slug: emotive-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Emotive Rate Limits
  slug: emotive-rate-limits
score:
  band: developing
  composite: 50.2
  delta: 5.3
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 30.3
    contract_quality: 58.4
    developer_ergonomics: 52.4
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 15.8
  previous_composite: 44.9
  provenance:
    conformance: first-party
    contracts:
      callable: 71.4
      derived: 0
      marker_coverage: 85.7
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/emotive/refs/heads/main/screenshots/emotive-2026-07-25T213253.png
security:
- kind: authentication
  name: Emotive Authentication
  slug: emotive-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Emotive Domain Security
  slug: emotive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: emotive
tags:
- Company
- Marketing
- SMS
- Messaging
- eCommerce
- Marketing Automation
- Text Message Marketing
- Conversational Commerce
- Webhooks
- Customer Data
- Segmentation
- Attribution
website: https://www.emotive.io/
---
