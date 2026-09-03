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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Honeybook Agentic Access
  operation_count: 25
  slug: honeybook-agentic-access
  summary_line: 25 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Clients and inquiries/leads captured through HoneyBook lead forms.
  name: HoneyBook Clients API
  slug: honeybook-clients-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Contracts and e-signature agreements attached to a project.
  name: HoneyBook Contracts API
  slug: honeybook-contracts-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Invoices issued to clients within a project.
  name: HoneyBook Invoices API
  slug: honeybook-invoices-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Card and ACH payments made against invoices.
  name: HoneyBook Payments API
  slug: honeybook-payments-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: The visual project pipeline - bookings and pipeline stage.
  name: HoneyBook Projects API
  slug: honeybook-projects-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Combined quote + contract + invoice documents sent to clients.
  name: HoneyBook Proposals API
  slug: honeybook-proposals-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Self-service session-type booking (Essentials/Premium plans).
  name: HoneyBook Scheduler API
  slug: honeybook-scheduler-api
- baseURL: https://api.honeybook.com/v1
  baseurl_source: declared
  description: Modeled event subscription surface mirroring HoneyBook's Zapier triggers.
  name: HoneyBook Webhooks API
  slug: honeybook-webhooks-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HoneyBook API (Modeled) Clients API
  slug: open-honeybook-clients-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Contracts API
  slug: open-honeybook-contracts-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Invoices API
  slug: open-honeybook-invoices-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Payments API
  slug: open-honeybook-payments-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Projects API
  slug: open-honeybook-projects-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Proposals API
  slug: open-honeybook-proposals-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Scheduler API
  slug: open-honeybook-scheduler-api
- collection_type: open
  name: HoneyBook API (Modeled) Clients Webhooks API
  slug: open-honeybook-webhooks-api
- collection_type: open
  name: HoneyBook API (Modeled)
  slug: open-honeybook
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/honeybook-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honeybook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/honeybook-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/honeybook-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honeybook
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honeybook
- group: company
  title: ''
  type: Website
  url: https://www.honeybook.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.honeybook.com/en/collections/68941-integrations-and-partnerships
- group: commercial
  title: ''
  type: Plans
  url: plans/honeybook-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/honeybook-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/honeybook-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.honeybook.com/blog
created: '2026-07-04'
description: HoneyBook is an all-in-one clientflow management platform for independent, service-based businesses - photographers, event planners, designers, consultants, coaches, and similar creative entrepreneurs. It combines CRM/lead capture, proposals, contracts and e-signature, invoicing and payments, scheduling, automations, and client communication in one product. HoneyBook does not publish a self-serve public developer API or a developer portal; third-party connectivity is offered through a limited set of native integrations (QuickBooks Online, Zoom, Calendly, Flodesk, Canva, Meta Leads, Slack, Asana, monday.com) and, most broadly, through Zapier. An internal API host (api.honeybook.com) is live and clearly powers the Zapier integration and native connectors, but HoneyBook has never published a self-serve technical reference, OAuth client registration flow, or endpoint documentation for outside developers, and community requests for direct API access date back to at least January
  2024 with no roadmap commitment as of this review.
finops:
- name: Honeybook Finops
  service_category: Business Applications - Clientflow / CRM
  slug: honeybook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honeybook.png
layout: provider
modified: '2026-07-04'
name: HoneyBook
nav: Providers
network: true
overview: 'HoneyBook publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Contracts API, Invoices API, and 5 more. Tagged areas include CRM, Clientflow, Proposals, Contracts, and Invoicing.


  HoneyBook''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Honeybook Plans Pricing
  plan_count: 4
  slug: honeybook-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Honeybook Rate Limits
  slug: honeybook-rate-limits
scopes:
- name: Honeybook Scopes
  scope_count: 14
  slug: honeybook-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 37.5
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honeybook/refs/heads/main/screenshots/honeybook-2026-07-25T221358.png
security:
- kind: authentication
  name: Honeybook Authentication
  slug: honeybook-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Honeybook Domain Security
  slug: honeybook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: honeybook
tags:
- CRM
- Clientflow
- Proposals
- Contracts
- Invoicing
- Payments
- Scheduling
- Creative Entrepreneurs
- Small Business
website: https://www.honeybook.com
---
