---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 21
  human_in_the_loop: 3
  name: Busup Agentic Access
  operation_count: 74
  slug: busup-agentic-access
  summary_line: 74 operations · 21 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Billing information API from BusUp — 1 operation(s) for billing information.
  name: BusUp Billing information API
  slug: busup-billing-information-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The CheckIn API from BusUp — 1 operation(s) for checkin.
  name: BusUp Check In API
  slug: busup-checkin-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Commuting Companies API from BusUp — 3 operation(s) for commuting companies.
  name: BusUp Commuting Companies API
  slug: busup-commuting-companies-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Commuting Employees API from BusUp — 3 operation(s) for commuting employees.
  name: BusUp Commuting Employees API
  slug: busup-commuting-employees-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Commuting Sites API from BusUp — 7 operation(s) for commuting sites.
  name: BusUp Commuting Sites API
  slug: busup-commuting-sites-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Consumptions API from BusUp — 1 operation(s) for consumptions.
  name: BusUp Consumptions API
  slug: busup-consumptions-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Countries API from BusUp — 1 operation(s) for countries.
  name: BusUp Countries API
  slug: busup-countries-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Credit Memos API from BusUp — 2 operation(s) for credit memos.
  name: BusUp Credit Memos API
  slug: busup-credit-memos-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Datalog API from BusUp — 2 operation(s) for datalog.
  name: BusUp Datalog API
  slug: busup-datalog-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Invoices API from BusUp — 2 operation(s) for invoices.
  name: BusUp Invoices API
  slug: busup-invoices-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Leisure Companies API from BusUp — 2 operation(s) for leisure companies.
  name: BusUp Leisure Companies API
  slug: busup-leisure-companies-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Orders API from BusUp — 2 operation(s) for orders.
  name: BusUp Orders API
  slug: busup-orders-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Permissions API from BusUp — 2 operation(s) for permissions.
  name: BusUp Permissions API
  slug: busup-permissions-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Promoters API from BusUp — 2 operation(s) for promoters.
  name: BusUp Promoters API
  slug: busup-promoters-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Role API from BusUp — 2 operation(s) for role.
  name: BusUp Role API
  slug: busup-role-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Roles API from BusUp — 2 operation(s) for roles.
  name: BusUp Roles API
  slug: busup-roles-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Route Rate API from BusUp — 1 operation(s) for route rate.
  name: BusUp Route Rate API
  slug: busup-route-rate-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Route Stops API from BusUp — 1 operation(s) for route stops.
  name: BusUp Route Stops API
  slug: busup-route-stops-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Routes API from BusUp — 5 operation(s) for routes.
  name: BusUp Routes API
  slug: busup-routes-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The RoutesRatesUserPlans API from BusUp — 2 operation(s) for routesratesuserplans.
  name: BusUp Routes Rates User Plans API
  slug: busup-routesratesuserplans-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Sites API from BusUp — 2 operation(s) for sites.
  name: BusUp Sites API
  slug: busup-sites-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Student API from BusUp — 3 operation(s) for student.
  name: BusUp Student API
  slug: busup-student-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The Tickets API from BusUp — 2 operation(s) for tickets.
  name: BusUp Tickets API
  slug: busup-tickets-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The User API from BusUp — 12 operation(s) for user.
  name: BusUp User API
  slug: busup-user-api
- baseURL: https://api.busup.com/v2
  baseurl_source: declared
  description: The User Plans API from BusUp — 4 operation(s) for user plans.
  name: BusUp User Plans API
  slug: busup-user-plans-api
artifact_total: 28
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/agentic-access/busup-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/busup-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/rules/busup-rules.yml
  title: ''
  type: Spectral
  url: rules/busup-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/errors/busup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/busup-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/conformance/busup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/busup-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/llms/busup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/busup-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/hosts/busup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/busup-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/vendors/busup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/busup-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.busup.com/ca/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.busup.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/busup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/busup/refs/heads/main/security/busup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/busup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.busup.com/
created: '2026-10-06'
description: BusUp Technologies provides a cloud‑based platform that enables businesses to digitize and automate their procurement, invoicing, and expense management processes. The solution offers real‑time analytics, integration with ERP and accounting systems, and a mobile app for on‑the‑go approvals. Targeted at mid‑size enterprises, BusUp aims to streamline spend management, improve compliance, and reduce manual effort across the purchase‑to‑pay lifecycle.
layout: provider
modified: '2026-10-06'
name: BusUp
nav: Providers
network: true
overview: 'BusUp publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing information API, Check In API, Commuting Companies API, and 22 more. Tagged areas include Company, Procurement, Spend-Management, Software-as-a-Service, and Automation.


  The BusUp catalog on APIs.io includes 1 Spectral governance ruleset.


  BusUp''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: BusUp API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: busup-rules
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 2.4
    discoverability: 69.6
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Busup Domain Security
  slug: busup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: busup
tags:
- Company
- Procurement
- Spend-Management
- Software-as-a-Service
- Automation
website: https://www.busup.com/
---
