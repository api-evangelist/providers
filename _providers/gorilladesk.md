---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gorilladesk Agentic Access
  operation_count: 9
  slug: gorilladesk-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 6
apis:
- description: The Company API from GorillaDesk — 1 operation(s) for company.
  name: GorillaDesk Company API
  slug: gorilladesk-company-api
- description: The Customer API from GorillaDesk — 2 operation(s) for customer.
  name: GorillaDesk Customer API
  slug: gorilladesk-customer-api
- description: The Note API from GorillaDesk — 1 operation(s) for note.
  name: GorillaDesk Note API
  slug: gorilladesk-note-api
- description: The Phone Type API from GorillaDesk — 1 operation(s) for phone type.
  name: GorillaDesk Phone Type API
  slug: gorilladesk-phone-type-api
- description: The User API from GorillaDesk — 2 operation(s) for user.
  name: GorillaDesk User API
  slug: gorilladesk-user-api
- description: The Users API from GorillaDesk — 1 operation(s) for users.
  name: GorillaDesk Users API
  slug: gorilladesk-users-api
artifact_total: 13
collections:
- collection_type: open
  name: GorillaDesk v1 API
  slug: open-gorilladesk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gorilladesk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gorilladesk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gorilladesk-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gorilladesk
- group: company
  title: ''
  type: Website
  url: https://gorilladesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.gorilladesk.com/
- group: start
  title: ''
  type: SignUp
  url: https://beta.gorilladesk.com/addons/api
- group: commercial
  title: ''
  type: Plans
  url: plans/gorilladesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gorilladesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gorilladesk-finops.yml
created: '2026-07-04'
description: GorillaDesk is field service management software for pest control, lawn care, pool service, and other home-service businesses, covering scheduling, routing, invoicing, payments, customer records, and technician management. GorillaDesk exposes a real, self-serve public REST API - the GorillaDesk v1 API at https://api.gorilladesk.com/v1 - documented with a public OpenAPI 3.0.3 specification (rendered via Redoc at https://api.gorilladesk.com/). Access uses per-company API keys (Bearer token authentication) generated on the in-app Addons page; there is no separate developer signup or API pricing tier - any paying account can mint a key. The documented public surface is intentionally narrow (Company, Users, Customers, Customer Notes, and Phone Types); broader automation (invoices, jobs, work orders, payments) is offered through Zapier connectors and out-of-the-box integrations (QuickBooks, Square, Stripe, Google) rather than through the public v1 REST spec. A newer, auth-gated v2
  API surface (apiv2.gdesk.io) exists but is not publicly documented.
finops:
- name: Gorilladesk Finops
  service_category: Field Service Management Software
  slug: gorilladesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gorilladesk.png
layout: provider
modified: '2026-07-04'
name: GorillaDesk
nav: Providers
network: true
overview: 'GorillaDesk publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Company API, Customer API, Note API, and 3 more. Tagged areas include Field Service Management, Pest Control, Lawn Care, Scheduling, and Invoicing.


  GorillaDesk''s developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Gorilladesk Plans Pricing
  plan_count: 4
  slug: gorilladesk-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 2
  name: Gorilladesk Rate Limits
  slug: gorilladesk-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 52.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gorilladesk/refs/heads/main/screenshots/gorilladesk-2026-07-25T220117.png
security:
- kind: authentication
  name: Gorilladesk Authentication
  slug: gorilladesk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gorilladesk Domain Security
  slug: gorilladesk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gorilladesk
tags:
- Field Service Management
- Pest Control
- Lawn Care
- Scheduling
- Invoicing
- Customers
- SaaS
website: https://gorilladesk.com/
---
