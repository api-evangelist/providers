---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Tablecheck Agentic Access
  operation_count: 59
  slug: tablecheck-agentic-access
  summary_line: 59 operations · 22 acting
api_count: 14
apis:
- description: The availability API from TableCheck — 1 operation(s) for availability.
  name: TableCheck availability API
  slug: tablecheck-availability-api
- description: The blockages API from TableCheck — 2 operation(s) for blockages.
  name: TableCheck blockages API
  slug: tablecheck-blockages-api
- description: The calendar API from TableCheck — 1 operation(s) for calendar.
  name: TableCheck calendar API
  slug: tablecheck-calendar-api
- description: The customers API from TableCheck — 3 operation(s) for customers.
  name: TableCheck customers API
  slug: tablecheck-customers-api
- description: The franchises API from TableCheck — 2 operation(s) for franchises.
  name: TableCheck franchises API
  slug: tablecheck-franchises-api
- description: The membership_programs API from TableCheck — 2 operation(s) for membership_programs.
  name: TableCheck membership_programs API
  slug: tablecheck-membership-programs-api
- description: The memberships API from TableCheck — 2 operation(s) for memberships.
  name: TableCheck memberships API
  slug: tablecheck-memberships-api
- description: The pos_journals API from TableCheck — 3 operation(s) for pos_journals.
  name: TableCheck pos_journals API
  slug: tablecheck-pos-journals-api
- description: The reservation_flags API from TableCheck — 2 operation(s) for reservation_flags.
  name: TableCheck reservation_flags API
  slug: tablecheck-reservation-flags-api
- description: The reservations API from TableCheck — 6 operation(s) for reservations.
  name: TableCheck reservations API
  slug: tablecheck-reservations-api
- description: The shops API from TableCheck — 3 operation(s) for shops.
  name: TableCheck shops API
  slug: tablecheck-shops-api
- description: The table_status API from TableCheck — 2 operation(s) for table_status.
  name: TableCheck table_status API
  slug: tablecheck-table-status-api
- description: The tables API from TableCheck — 1 operation(s) for tables.
  name: TableCheck tables API
  slug: tablecheck-tables-api
- description: The timetable API from TableCheck — 1 operation(s) for timetable.
  name: TableCheck timetable API
  slug: tablecheck-timetable-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TableCheck API - V1 availability API
  slug: open-tablecheck-availability-api
- collection_type: open
  name: TableCheck API - V1 availability blockages API
  slug: open-tablecheck-blockages-api
- collection_type: open
  name: TableCheck API - V1 availability calendar API
  slug: open-tablecheck-calendar-api
- collection_type: open
  name: TableCheck API - V1 availability customers API
  slug: open-tablecheck-customers-api
- collection_type: open
  name: TableCheck API - V1 availability franchises API
  slug: open-tablecheck-franchises-api
- collection_type: open
  name: TableCheck API - V1 availability membership_programs API
  slug: open-tablecheck-membership-programs-api
- collection_type: open
  name: TableCheck API - V1 availability memberships API
  slug: open-tablecheck-memberships-api
- collection_type: open
  name: TableCheck API - V1 availability pos_journals API
  slug: open-tablecheck-pos-journals-api
- collection_type: open
  name: TableCheck API - V1 availability reservation_flags API
  slug: open-tablecheck-reservation-flags-api
- collection_type: open
  name: TableCheck API - V1 availability reservations API
  slug: open-tablecheck-reservations-api
- collection_type: open
  name: TableCheck API - V1 availability shops API
  slug: open-tablecheck-shops-api
- collection_type: open
  name: TableCheck API - V1 availability table_status API
  slug: open-tablecheck-table-status-api
- collection_type: open
  name: TableCheck API - V1 availability tables API
  slug: open-tablecheck-tables-api
- collection_type: open
  name: TableCheck API - V1 availability timetable API
  slug: open-tablecheck-timetable-api
- collection_type: open
  name: TableCheck API
  slug: open-tablecheck
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tablecheck-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tablecheck-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tablecheck-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tablecheck
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tablecheck
- group: company
  title: ''
  type: Website
  url: https://www.tablecheck.com
- group: docs
  title: ''
  type: Documentation
  url: https://tablecheck.atlassian.net/wiki/spaces/API
- group: commercial
  title: ''
  type: Plans
  url: plans/tablecheck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tablecheck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tablecheck-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tablecheck.com/en/blog/
created: '2026-07-05'
description: TableCheck is a restaurant booking and guest-experience platform (founded 2011, headquartered in Tokyo, Japan) used by thousands of restaurants across 35+ countries to consolidate reservations, availability, guest CRM, memberships, and POS integration into one system. TableCheck exposes a production JSON/REST API, partitioned into components - Availability, Web Booking, Booking, CRM, POS, and Site Controller - under https://api.tablecheck.com/api. Access is partner-gated, and a per-environment secret_key is issued by the TableCheck API team on approval, while some components (notably the direct Booking API) are available only by special arrangement. Each component publishes an OpenAPI 3.0 description.
finops:
- name: Tablecheck Finops
  service_category: Restaurant Reservation and Guest Management
  slug: tablecheck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tablecheck.png
layout: provider
modified: '2026-07-05'
name: TableCheck
nav: Providers
network: true
overview: 'TableCheck publishes 14 APIs on the [APIs.io](https://apis.io/) network, including availability API, blockages API, calendar API, and 11 more. Tagged areas include Restaurant, Reservations, Booking, Hospitality, and Availability.


  TableCheck''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tablecheck Plans Pricing
  plan_count: 2
  slug: tablecheck-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Tablecheck Rate Limits
  slug: tablecheck-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 2.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.9
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Tablecheck Authentication
  slug: tablecheck-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tablecheck Domain Security
  slug: tablecheck-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: tablecheck
tags:
- Restaurant
- Reservations
- Booking
- Hospitality
- Availability
- Guest CRM
- Point-of-Sale
- Japan
website: https://www.tablecheck.com
---
