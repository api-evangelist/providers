---
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-12'
api_count: 14
apis:
- description: The individual services Order.co reports health for.
  name: Order.co Components API
  slug: orderco-components-api
- description: Posts, pages and media.
  name: Order.co Content API
  slug: orderco-content-api
- description: Published Order.co customer case studies.
  name: Order.co Customer Stories API
  slug: orderco-customer-stories-api
- description: Self-describing route, type and taxonomy introspection.
  name: Order.co Discovery API
  slug: orderco-discovery-api
- description: Question-and-answer entries used across the site.
  name: Order.co FA Qs API
  slug: orderco-faqs-api
- description: Open and historical incidents with their dated updates.
  name: Order.co Incidents API
  slug: orderco-incidents-api
- description: Scheduled maintenance windows.
  name: Order.co Maintenance API
  slug: orderco-maintenance-api
- description: First-party cn/v1 theme namespace.
  name: Order.co Newsroom API
  slug: orderco-newsroom-api
- description: Ebooks, webinars, tools and spend insights.
  name: Order.co Resources API
  slug: orderco-resources-api
- description: Cross-type search.
  name: Order.co Search API
  slug: orderco-search-api
- description: The rollup status indicator for the whole page.
  name: Order.co Status API
  slug: orderco-status-api
- description: Categories, tags, industries and use cases.
  name: Order.co Taxonomies API
  slug: orderco-taxonomies-api
- description: Customer quotes.
  name: Order.co Testimonials API
  slug: orderco-testimonials-api
- description: Published Order.co vendor/supplier case studies.
  name: Order.co Vendor Stories API
  slug: orderco-vendor-stories-api
artifact_total: 27
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/orderco-content-overlay.yaml
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
overview: 'Order.co publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Components API, Content API, Customer Stories API, and 11 more. Tagged areas include Company, Procurement, Spend Management, Accounts Payable, and Purchasing.


  Order.co''s developer surface includes authentication, code examples, engineering blog, and 21 more developer resources.'
random_paper: 30
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 13.5
    developer_ergonomics: 14.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 27.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orderco/refs/heads/main/screenshots/orderco-2026-08-07T190910.png
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
