---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The public, anonymous Atlassian Statuspage v2 API for the Order.co platform, served on Order.co's own host status.order.co (page id ckzwmwkw4x3f) and documented by Order.co at https://status.order.co/
  name: Order.co Status API
  slug: orderco-status-api
- description: 'The public, anonymous WordPress REST API behind www.order.co. It is not the Order.co procurement API, but it is a real first-party machine-readable surface and it carries the corpus an agent actually '
  name: Order.co Content API
  slug: orderco-content-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/orderco-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orderco-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orderco-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orderco-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.order.co/
- group: design
  title: ''
  type: Conformance
  url: conformance/orderco-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orderco-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orderco-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orderco-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orderco-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/orderco-content-discovery.json
- group: company
  title: ''
  type: Website
  url: https://www.order.co/
- group: company
  title: ''
  type: Blog
  url: https://www.order.co/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.order.co/blog/feed/
- group: start
  title: ''
  type: Login
  url: https://app.order.co/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Negotiatus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/order-company
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.order.co/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.order.co/terms-and-conditions/
- group: company
  title: ''
  type: Careers
  url: https://www.order.co/careers/
- group: company
  title: ''
  type: Press
  url: https://www.order.co/newsroom/
- group: start
  title: ''
  type: Demo
  url: https://www.order.co/demo/
created: '2026-08-04'
description: 'Order.co (founded 2016 in New York as Negotiatus, rebranded to Order.co in 2021) is a procurement and finance-automation platform for mid-market and enterprise buyers: guided purchasing across a managed vendor catalog, purchase-order and approval workflow, accounts- payable automation, spend management and virtual cards, sold into multi-location operators in property management, hospitality, healthcare, retail, fitness, coworking, early childhood education, wellness, technology and nonprofit. The product connects to QuickBooks Online, NetSuite, Sage Intacct and Workday over API, and supports SSO through Okta and Ping Identity. Order.co publishes no developer portal, no API reference and no machine-readable specification for any of that - the procurement API is disclosed only to customers, and vendors receive API or EDI credentials during onboarding. What it does publish anonymously are two real, self-describing surfaces on its own hosts - the WordPress REST API behind www.order.co
  (blog, customer and vendor stories, ebooks, webinars, tools, 873 FAQ records, and the first-party industry and use-case taxonomies) and the Atlassian Statuspage v2 API on status.order.co - plus an llms.txt and a companion page written for language models.'
examples:
- key_count: 16
  name: Orderco Content Discovery
  slug: orderco-content-discovery
- key_count: 6
  name: Orderco Content Taxonomies
  slug: orderco-content-taxonomies
- key_count: 19
  name: Orderco Content Types
  slug: orderco-content-types
- key_count: 2
  name: Orderco Status Components
  slug: orderco-status-components
- key_count: 2
  name: Orderco Status Incidents Unresolved
  slug: orderco-status-incidents-unresolved
- key_count: 2
  name: Orderco Status Incidents
  slug: orderco-status-incidents
- key_count: 2
  name: Orderco Status Scheduled Maintenances Active
  slug: orderco-status-scheduled-maintenances-active
- key_count: 2
  name: Orderco Status Scheduled Maintenances Upcoming
  slug: orderco-status-scheduled-maintenances-upcoming
- key_count: 2
  name: Orderco Status Scheduled Maintenances
  slug: orderco-status-scheduled-maintenances
- key_count: 2
  name: Orderco Status Status
  slug: orderco-status-status
- key_count: 5
  name: Orderco Status Summary
  slug: orderco-status-summary
image: https://www.order.co/wp-content/themes/order/assets/img/logos/order.svg
layout: provider
modified: '2026-08-04'
name: Order.co
nav: Providers
network: true
overview: 'Order.co publishes 2 APIs on the [APIs.io](https://apis.io/) network: Status API and Content API. Tagged areas include Company, Procurement, Spend Management, Accounts Payable, and Purchasing.


  Order.co''s developer surface includes authentication, code examples, engineering blog, and 20 more developer resources.'
random_paper: 72
score:
  band: thin
  composite: 28.0
  delta: -9.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 13.8
    developer_ergonomics: 14.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 37.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: falling
security:
- kind: authentication
  name: Orderco Authentication
  slug: orderco-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Orderco Domain Security
  slug: orderco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orderco
tags:
- Company
- Procurement
- Spend Management
- Accounts Payable
- Purchasing
- Vendor Management
- Payments
- Virtual Cards
- Finance Automation
- United States
website: https://www.order.co/
---
