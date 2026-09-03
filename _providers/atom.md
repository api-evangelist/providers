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
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'REST service for managing the customer (cliente) records behind Atom''s WhatsApp conversations. The provider knowledge base documents three operations: create or update a customer, retrieve the list of'
  name: Atom Customers API
  slug: customers
- description: REST service for sending pre-approved WhatsApp template messages from an account's official WhatsApp number. The documented send endpoint is POST /api/Template/SendMessage, taking templateId, phoneNum
  name: Atom WhatsApp Templates API
  slug: templates
artifact_total: 7
asyncapis:
- description: ''
  name: Atom Webhooks
  slug: atom-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://atomchat.io/
- group: docs
  title: ''
  type: Documentation
  url: https://soporte.atomchat.io/knowledge/api-de-clientes
- group: operate
  title: ''
  type: Support
  url: https://soporte.atomchat.io/
- group: company
  title: ''
  type: Blog
  url: https://atomchat.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://soporte.atomchat.io/knowledge/aprende-a-probar-tu-api-en-postman-y-configurarlas-en-las-peticiones-http-de-atom
- group: commercial
  title: ''
  type: Pricing
  url: https://atomchat.io/espanol/precio
- group: start
  title: ''
  type: Login
  url: https://app.atomchat.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atomchat.io/legal/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atomchat.io/legal/politica-de-privacidad
- group: auth
  title: ''
  type: Authentication
  url: authentication/atom-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atom-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atom-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/atom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atom-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atom-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/atom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atom-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atom-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/atom-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/atom-packages.yml
created: '2026-07-17'
description: Atom (atomchat.io) is a Panama-based conversational-commerce platform whose multimodal AI Agents combine text, voice, image, and CRM data to run human-like WhatsApp conversations that qualify leads and close sales for businesses across Latin America. Founded in 2019 by Erick Holmann and Rene Mouynes and backed by Techstars and Mucker Capital, Atom connects WhatsApp click-to-chat ads to an AI agent that engages and qualifies prospects, then hands sales-ready leads to human reps. It exposes a Customers API and a WhatsApp template-message API, both authenticated with an account API key configured from the Atom admin panel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atom.png
layout: provider
modified: '2026-08-14'
name: ATOM
nav: Providers
network: true
overview: 'ATOM publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, WhatsApp, Artificial Intelligence, and Conversational Commerce.


  The ATOM catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ATOM''s developer surface includes documentation, support, engineering blog, getting-started guide, pricing, authentication, and 14 more developer resources.'
plans:
- name: Atom Plans Pricing
  plan_count: 4
  slug: atom-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Atom Rate Limits
  slug: atom-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 37.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atom/refs/heads/main/screenshots/atom-2026-07-25T201559.png
security:
- kind: authentication
  name: Atom Authentication
  slug: atom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Atom Domain Security
  slug: atom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atom
tags:
- Company
- Messaging
- WhatsApp
- Artificial Intelligence
- Conversational Commerce
- Chatbots
- Sales
- Lead Generation
- Customer Engagement
- Latin America
website: https://atomchat.io/
---
