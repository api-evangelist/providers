---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trengo Agentic Access
  operation_count: 21
  slug: trengo-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 1
apis:
- description: List connected channels.
  name: Trengo Channels API
  slug: trengo-channels-api
- description: Manage contacts and contact profiles.
  name: Trengo Contacts API
  slug: trengo-contacts-api
- description: Manage labels and custom fields.
  name: Trengo Labels and Custom Fields API
  slug: trengo-labels-and-custom-fields-api
- description: List and send text and media messages on a ticket.
  name: Trengo Messages API
  slug: trengo-messages-api
- description: Manage teams and list agents.
  name: Trengo Teams and Users API
  slug: trengo-teams-and-users-api
- description: Create, list, assign, label, and close conversations.
  name: Trengo Tickets API
  slug: trengo-tickets-api
- description: Register and manage webhook subscriptions.
  name: Trengo Webhooks API
  slug: trengo-webhooks-api
- description: Send approved WhatsApp Business templates.
  name: Trengo WhatsApp API
  slug: trengo-whatsapp-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trengo Channels API
  slug: open-trengo-channels-api
- collection_type: open
  name: Trengo Channels Contacts API
  slug: open-trengo-contacts-api
- collection_type: open
  name: Trengo Channels Labels and Custom Fields API
  slug: open-trengo-labels-and-custom-fields-api
- collection_type: open
  name: Trengo Channels Messages API
  slug: open-trengo-messages-api
- collection_type: open
  name: Trengo Channels Teams and Users API
  slug: open-trengo-teams-and-users-api
- collection_type: open
  name: Trengo Channels Tickets API
  slug: open-trengo-tickets-api
- collection_type: open
  name: Trengo Channels Webhooks API
  slug: open-trengo-webhooks-api
- collection_type: open
  name: Trengo Channels WhatsApp API
  slug: open-trengo-whatsapp-api
- collection_type: open
  name: Trengo API
  slug: open-trengo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/trengo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trengo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trengo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trengo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trengo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trengo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trengo
- group: company
  title: ''
  type: Website
  url: https://trengo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trengo.com/docs/welcome
- group: commercial
  title: ''
  type: Plans
  url: plans/trengo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trengo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trengo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://trengo.com/blog
created: '2026-06-20'
description: Trengo is an omnichannel customer-engagement and shared-inbox platform that unifies email, WhatsApp, live chat, voice, SMS, and social channels into one team inbox with AI agents. The Trengo REST API (app.trengo.com/api/v2) lets you create and manage tickets, contacts, messages, channels, teams, users, labels, custom fields, webhooks, and WhatsApp templates programmatically with Bearer-token authentication.
finops:
- name: Trengo Finops
  service_category: Customer Engagement and Communications
  slug: trengo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trengo.png
layout: provider
modified: '2026-06-20'
name: Trengo
nav: Providers
network: true
overview: 'Trengo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Contacts API, Labels and Custom Fields API, and 5 more. Tagged areas include Customer Engagement, Omnichannel, Shared Inbox, Messaging, and WhatsApp.


  Trengo''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Trengo Plans Pricing
  plan_count: 4
  slug: trengo-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Trengo Rate Limits
  slug: trengo-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trengo/refs/heads/main/screenshots/trengo-2026-06-20T195707.png
security:
- kind: authentication
  name: Trengo Authentication
  slug: trengo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trengo Domain Security
  slug: trengo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trengo Vulnerability Disclosure
  slug: trengo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Trengo Trust Center
  slug: trengo-trust-center
  summary_line: PCI DSS, GDPR
slug: trengo
tags:
- Customer Engagement
- Omnichannel
- Shared Inbox
- Messaging
- WhatsApp
- Customer-Support
website: https://trengo.com/
---
