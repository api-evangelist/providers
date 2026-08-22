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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Ticketspice Agentic Access
  operation_count: 32
  slug: ticketspice-agentic-access
  summary_line: 32 operations · 9 acting
api_count: 10
apis:
- description: The Coupons API from TicketSpice — 4 operation(s) for coupons.
  name: TicketSpice Coupons API
  slug: ticketspice-coupons-api
- description: The Customers API from TicketSpice — 2 operation(s) for customers.
  name: TicketSpice Customers API
  slug: ticketspice-customers-api
- description: The Forms API from TicketSpice — 3 operation(s) for forms.
  name: TicketSpice Forms API
  slug: ticketspice-forms-api
- description: The Health API from TicketSpice — 1 operation(s) for health.
  name: TicketSpice Health API
  slug: ticketspice-health-api
- description: The Orders API from TicketSpice — 2 operation(s) for orders.
  name: TicketSpice Orders API
  slug: ticketspice-orders-api
- description: The Registrants API from TicketSpice — 4 operation(s) for registrants.
  name: TicketSpice Registrants API
  slug: ticketspice-registrants-api
- description: The Subscriptions API from TicketSpice — 2 operation(s) for subscriptions.
  name: TicketSpice Subscriptions API
  slug: ticketspice-subscriptions-api
- description: The Tickets API from TicketSpice — 2 operation(s) for tickets.
  name: TicketSpice Tickets API
  slug: ticketspice-tickets-api
- description: The Transactions API from TicketSpice — 2 operation(s) for transactions.
  name: TicketSpice Transactions API
  slug: ticketspice-transactions-api
- description: The Webhooks API from TicketSpice — 5 operation(s) for webhooks.
  name: TicketSpice Webhooks API
  slug: ticketspice-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons API
  slug: open-ticketspice-coupons-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Customers API
  slug: open-ticketspice-customers-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Forms API
  slug: open-ticketspice-forms-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Health API
  slug: open-ticketspice-health-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Orders API
  slug: open-ticketspice-orders-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Registrants API
  slug: open-ticketspice-registrants-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Subscriptions API
  slug: open-ticketspice-subscriptions-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Tickets API
  slug: open-ticketspice-tickets-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Transactions API
  slug: open-ticketspice-transactions-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public) Coupons Webhooks API
  slug: open-ticketspice-webhooks-api
- collection_type: open
  name: TicketSpice API (Webconnex v2 Public)
  slug: open-ticketspice
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ticketspice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ticketspice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ticketspice-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webconnex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/webconnex
- group: company
  title: ''
  type: Website
  url: https://www.ticketspice.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webconnex.io/api/v2/
- group: commercial
  title: ''
  type: Plans
  url: plans/ticketspice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ticketspice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ticketspice-finops.yml
created: '2026-07-05'
description: TicketSpice is an online event ticketing platform built by Webconnex that lets organizers design fully customizable ticketing pages and sell tickets for events, festivals, tours, and immersive experiences at a flat 99-cent per-ticket fee. TicketSpice is powered by the shared Webconnex REST API (base https://api.webconnex.com/v2/public), the same read-and-manage API surface behind Webconnex products RegFox, RedPodium, and GivingFuel. Callers pass a product parameter of ticketspice and authenticate with an apiKey header to search and view orders, registrants, tickets, transactions, customers, forms, and inventory, manage coupons and webhooks, and check registrants in and out. API access is provisioned per account with an API key and is gated to higher-tier plans.
finops:
- name: Ticketspice Finops
  service_category: Event Ticketing and Registration
  slug: ticketspice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ticketspice.png
layout: provider
modified: '2026-07-05'
name: TicketSpice
nav: Providers
network: true
overview: 'TicketSpice publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Coupons API, Customers API, Forms API, and 7 more. Tagged areas include Event Ticketing, Ticketing, Events, Registration, and Payments.


  TicketSpice''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Ticketspice Plans Pricing
  plan_count: 3
  slug: ticketspice-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Ticketspice Rate Limits
  slug: ticketspice-rate-limits
score:
  band: thin
  composite: 35.4
  delta: 0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Ticketspice Authentication
  slug: ticketspice-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ticketspice Domain Security
  slug: ticketspice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ticketspice
tags:
- Event Ticketing
- Ticketing
- Events
- Registration
- Payments
- Webconnex
website: https://www.ticketspice.com
---
