---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The internal-but-anonymously-discoverable JSON API behind the Zerocater ordering application at app.zerocater.com. Built on Django REST Framework, it serves an RFC 6570 URI-template hypermedia index a
  name: Zerocater API v3
  slug: zerocater-api-v3
artifact_total: 3
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ZeroCater/PyZeroCater/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerocater-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zerocater.com/
- group: company
  title: ''
  type: Blog
  url: https://zerocater.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://zerocater.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://zerocater.com/about/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://zerocater.com/faq/
- group: start
  title: ''
  type: SignUp
  url: https://app.zerocater.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.zerocater.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zerocater.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zerocater.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZeroCater
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zerocater-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/zerocater-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zerocater-packages.yml
- group: other
  title: ''
  type: APIDiscovery
  url: discovery/zerocater-api-v3-discovery.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zerocater-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zerocater-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zerocater-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zerocater-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zerocater-lifecycle.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/zerocater_stock/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Zerocater
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zerocater
created: '2026-08-05'
description: Zerocater is a San Francisco-founded corporate catering and workplace food company that builds and manages office food programs for businesses. It acts as an intermediary between employers and a curated network of local restaurants, caterers and chefs, covering daily corporate catering (buffet and individually boxed), chef-led on-site corporate cafeterias with snack and barista programs, and full-service event catering with on-site staffing. Its CaterAi product uses AI to recommend and assemble menus from a team's stated preferences, dietary restrictions and order history, and to book on-site staff and event decor. Zerocater states it serves 500+ companies across 12+ major U.S. metros including the SF Bay Area, New York, Austin, Boston, Los Angeles, Chicago, Washington DC, Seattle, Denver, Dallas, Atlanta, Philadelphia and Phoenix. It runs a customer-facing ordering web application at app.zerocater.com backed by an undocumented Django REST Framework token-authenticated JSON
  API (v3), whose hypermedia root index is served anonymously, and it publishes a first-party Python client library on PyPI.
image: https://zerocater.com/wp-content/uploads/2026/05/make-catering-effortless-with-cater-ai-social.jpg
layout: provider
modified: '2026-08-05'
name: Zerocater
nav: Providers
network: true
overview: 'Zerocater publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Catering, Corporate Services, and Workplace.


  Zerocater''s developer surface includes engineering blog, support, FAQ, signup flow, authentication, and 19 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.2
  delta: 0.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Zerocater Authentication
  slug: zerocater-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zerocater Domain Security
  slug: zerocater-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zerocater
tags:
- Company
- Food and Beverage
- Catering
- Corporate Services
- Workplace
- Food Delivery
- Hospitality
- Artificial Intelligence
- Ordering
- Marketplace
website: https://zerocater.com/
---
