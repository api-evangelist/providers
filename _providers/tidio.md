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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Tidio Agentic Access
  operation_count: 26
  slug: tidio-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 1
apis:
- description: Real-time event notifications delivered via HTTP POST to a configured endpoint. Webhooks are available exclusively on Plus and Premium plans and are configured via the Developer panel. Supports signat
  name: Tidio Webhooks
  slug: tidio-webhooks
- description: JavaScript SDK for embedding and customizing the Tidio chat widget on websites. Supports user tracking, custom bot triggers, and behavioral customization. Available to all plan tiers.
  name: Tidio Widget SDK
  slug: tidio-widget-sdk
- description: Manage contacts (website visitors identified by name, email, or phone)
  name: Tidio Contacts API
  slug: tidio-contacts-api
- description: Retrieve department information
  name: Tidio Departments API
  slug: tidio-departments-api
- description: Lyro AI data sources and ticket answering
  name: Tidio Lyro API
  slug: tidio-lyro-api
- description: Retrieve operator (chat agent) information
  name: Tidio Operators API
  slug: tidio-operators-api
- description: Product catalog for Lyro AI recommendations
  name: Tidio Products API
  slug: tidio-products-api
- description: Retrieve project information
  name: Tidio Project API
  slug: tidio-project-api
- description: Manage email tickets and replies
  name: Tidio Tickets API
  slug: tidio-tickets-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts API
  slug: open-tidio-contacts-api
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts Departments API
  slug: open-tidio-departments-api
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts Lyro API
  slug: open-tidio-lyro-api
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts Operators API
  slug: open-tidio-operators-api
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts Products API
  slug: open-tidio-products-api
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts Project API
  slug: open-tidio-project-api
- collection_type: open
  name: Tidio OpenAPI (REST) Contacts Tickets API
  slug: open-tidio-tickets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tidio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tidio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tidio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tidio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tidio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tidio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tidio.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tidio.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tidio.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tidio-ltd
- group: other
  title: ''
  type: X
  url: https://twitter.com/tidiochat
- group: commercial
  title: ''
  type: Plans
  url: plans/tidio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tidio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tidio-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tidio-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/tidio-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tidio.com/feed/
created: 2026-06-12
description: Tidio is a customer service platform used by over 300,000 businesses that combines live chat, AI-powered chatbots (Lyro AI), and email ticketing into a unified support workspace. The platform exposes a REST OpenAPI for managing contacts, conversations, and tickets, a Webhooks system for real-time event notifications, and a JavaScript Widget SDK for front-end customization. API access uses paired client-id and client-secret headers and is gated by plan tier, with full OpenAPI access available on Plus and Premium plans. Rate limits range from 10 requests per minute on entry plans to 120 requests per minute on Premium. Tidio also offers an AI automation product called Flows for proactive visitor engagement via a no-code builder.
examples:
- key_count: 2
  name: Tidio Get Contacts Example
  slug: tidio-get-contacts-example
- key_count: 2
  name: Tidio Get Tickets Example
  slug: tidio-get-tickets-example
finops:
- name: Tidio Finops
  service_category: ''
  slug: tidio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tidio.png
json_schemas:
- name: Tidio Contact
  property_count: 12
  slug: tidio-contact
- name: Tidio Ticket
  property_count: 11
  slug: tidio-ticket
jsonld:
- class_count: 50
  name: Tidio Context
  property_count: 3
  slug: tidio-context
layout: provider
modified: 2026-06-12
name: Tidio
nav: Providers
network: true
overview: 'Tidio publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Departments API, Lyro API, and 4 more. Tagged areas include Live Chat, Chatbots, Customer Service, Artificial Intelligence, and Help Desk.


  The Tidio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tidio''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Tidio Plans Pricing
  plan_count: 5
  slug: tidio-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Tidio Rate Limits
  slug: tidio-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tidio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tidio-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 63.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 47.4
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tidio/refs/heads/main/screenshots/tidio-2026-06-20T195338.png
security:
- kind: authentication
  name: Tidio Authentication
  slug: tidio-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tidio Domain Security
  slug: tidio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tidio Trust Center
  slug: tidio-trust-center
  summary_line: SOC 2, GDPR
slug: tidio
tags:
- Live Chat
- Chatbots
- Customer Service
- Artificial Intelligence
- Help Desk
- Ticketing
- Conversations
- Contacts
- Webhook
- Widget
website: https://www.tidio.com/
---
