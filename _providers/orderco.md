---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://status.order.co/api/v2
  baseurl_source: declared
  description: The individual services Order.co reports health for.
  name: Order.co Components API
  slug: orderco-components-api
- baseURL: https://status.order.co/api/v2
  baseurl_source: declared
  description: Open and historical incidents with their dated updates.
  name: Order.co Incidents API
  slug: orderco-incidents-api
- baseURL: https://status.order.co/api/v2
  baseurl_source: declared
  description: Scheduled maintenance windows.
  name: Order.co Maintenance API
  slug: orderco-maintenance-api
- baseURL: https://status.order.co/api/v2
  baseurl_source: declared
  description: The rollup status indicator for the whole page.
  name: Order.co Status API
  slug: orderco-status-api
- description: 'The public WordPress REST API (wp-json) of the Order.co website at www.order.co: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Order.co Website (WordPress REST)
  slug: order-co-website-wordpress-rest
artifact_total: 36
collections:
- collection_type: open
  name: Order.co Status Components API
  slug: open-orderco-components-api
- collection_type: open
  name: Order.co Content API
  slug: open-orderco-content-api
- collection_type: open
  name: Order.co Content Customer Stories API
  slug: open-orderco-customer-stories-api
- collection_type: open
  name: Order.co Content Discovery API
  slug: open-orderco-discovery-api
- collection_type: open
  name: Order.co Content FA Qs API
  slug: open-orderco-faqs-api
- collection_type: open
  name: Order.co Status Incidents API
  slug: open-orderco-incidents-api
- collection_type: open
  name: Order.co Status Maintenance API
  slug: open-orderco-maintenance-api
- collection_type: open
  name: Order.co Content Newsroom API
  slug: open-orderco-newsroom-api
- collection_type: open
  name: Order.co Content Resources API
  slug: open-orderco-resources-api
- collection_type: open
  name: Order.co Content Search API
  slug: open-orderco-search-api
- collection_type: open
  name: Order.co Status API
  slug: open-orderco-status-api
- collection_type: open
  name: Order.co Content Taxonomies API
  slug: open-orderco-taxonomies-api
- collection_type: open
  name: Order.co Content Testimonials API
  slug: open-orderco-testimonials-api
- collection_type: open
  name: Order.co Content Vendor Stories API
  slug: open-orderco-vendor-stories-api
common:
- group: other
  href: https://artifacts.apis.io/orderco/overlays/orderco-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/orderco-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/orderco/authentication/orderco-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orderco-authentication.yml
- group: design
  href: https://artifacts.apis.io/orderco/conventions/orderco-conventions.yml
  title: ''
  type: Conventions
  url: conventions/orderco-conventions.yml
- group: design
  href: https://artifacts.apis.io/orderco/errors/orderco-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/orderco-problem-types.yml
- group: design
  href: https://artifacts.apis.io/orderco/lifecycle/orderco-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/orderco-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.order.co/
- group: design
  href: https://artifacts.apis.io/orderco/conformance/orderco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orderco-conformance.yml
- group: design
  href: https://artifacts.apis.io/orderco/data-model/orderco-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orderco-data-model.yml
- group: auth
  href: https://artifacts.apis.io/orderco/security/orderco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orderco-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/orderco/well-known/orderco-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orderco-well-known.yml
- group: agent
  href: https://artifacts.apis.io/orderco/llms/orderco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orderco-llms.txt
- group: agent
  href: https://artifacts.apis.io/orderco/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/orderco/examples/orderco-content-discovery.json
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
overview: 'Order.co publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Components API, Incidents API, Maintenance API, and 2 more. Tagged areas include Company, Procurement, Spend Management, Accounts Payable, and Purchasing.


  The Order.co catalog on APIs.io includes 1 Spectral governance ruleset.


  Order.co''s developer surface includes authentication, code examples, engineering blog, and 21 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Order.co API Rules
  rule_count: 61
  severity_counts:
    error: 53
    hint: 0
    info: 2
    warn: 6
  slug: orderco-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 15.8
    developer_ergonomics: 28.0
    discoverability: 65.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.4
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
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/orderco/orderco-2026-08-07T190910.png
security:
- kind: authentication
  name: Orderco Authentication
  slug: orderco-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Orderco Domain Security
  slug: orderco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Research Order.co customer and vendor stories by industry
  slug: orderco-customer-story-research
- name: Monitor Order.co platform status
  slug: orderco-platform-status-monitoring
- name: Retrieve Order.co procurement knowledge
  slug: orderco-procurement-knowledge-retrieval
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
