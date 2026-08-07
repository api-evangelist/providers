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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Travelperk Agentic Access
  operation_count: 20
  slug: travelperk-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 5
apis:
- description: Cost center management and user assignment.
  name: TravelPerk Cost Centers API
  slug: travelperk-cost-centers-api
- description: Invoices, invoice lines, invoice profiles, and PDFs.
  name: TravelPerk Invoices API
  slug: travelperk-invoices-api
- description: Traveler and member provisioning via SCIM 2.0.
  name: TravelPerk Members API
  slug: travelperk-members-api
- description: Trips, bookings, and trip custom fields.
  name: TravelPerk Trips API
  slug: travelperk-trips-api
- description: Event subscriptions.
  name: TravelPerk Webhooks API
  slug: travelperk-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: TravelPerk API
  slug: open-travelperk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/travelperk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/travelperk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travelperk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/travelperk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/travelperk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/travelperk
- group: company
  title: ''
  type: Website
  url: https://www.travelperk.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.travelperk.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/travelperk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/travelperk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/travelperk-finops.yml
created: '2026-06-25'
description: TravelPerk is a business-travel management platform that lets companies book and manage flights, hotels, trains, and cars in one place. Its Open API gives partners and customers programmatic access to bookings and trips, invoices and expenses, travelers and members, cost centers, scheduled reports, and webhooks for real-time travel and finance data exchange with HR systems, ERPs, and expense tools.
finops:
- name: Travelperk Finops
  service_category: Business Travel Management
  slug: travelperk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travelperk.png
layout: provider
modified: '2026-06-25'
name: TravelPerk
nav: Providers
network: true
overview: 'TravelPerk publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cost Centers API, Invoices API, Members API, and 2 more. Tagged areas include Business Travel, Travel Management, Expenses, Invoices, and Bookings.


  TravelPerk''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Travelperk Plans Pricing
  plan_count: 4
  slug: travelperk-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 3
  name: Travelperk Rate Limits
  slug: travelperk-rate-limits
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Travelperk Authentication
  slug: travelperk-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Travelperk Domain Security
  slug: travelperk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Travelperk Vulnerability Disclosure
  slug: travelperk-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: travelperk
tags:
- Business Travel
- Travel Management
- Expenses
- Invoices
- Bookings
website: https://www.travelperk.com
---
