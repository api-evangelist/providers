---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cbre Agentic Access
  operation_count: 1
  slug: cbre-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Real Estate operations
  name: CBRE Real Estate API
  slug: cbre-real-estate-api
artifact_total: 27
collections:
- collection_type: open
  name: CBRE API
  slug: open-cbre-cbre-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cbre-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cbre-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cbre-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CBRE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cbre
- group: company
  title: ''
  type: Website
  url: https://www.cbre.com
- group: company
  title: ''
  type: About
  url: https://www.cbre.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.cbre.com/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cbre.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.cbre.com/about-us/newsroom
- group: operate
  title: ''
  type: PressReleases
  url: https://www.cbre.com/about-us/newsroom
- group: other
  title: ''
  type: Research
  url: https://www.cbre.com/insights
- group: other
  title: ''
  type: Sustainability
  url: https://www.cbre.com/services/energy-and-sustainability-solutions
- group: operate
  title: ''
  type: Contact
  url: https://www.cbre.com/about-us/culture-and-history/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cbre.com/about-us/disclaimer-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbre.com/about-us/global-privacy-and-cookie-notice
- group: start
  title: ''
  type: Portal
  url: https://developer.cbre.com/
created: '2026-03-21'
description: 'CBRE Group, Inc. (NYSE: CBRE) is the world''s largest commercial real estate services and investment firm, with 155,000 professionals across 500+ offices in 100+ countries. CBRE provides advisory and transaction, project management, property management, valuation, investment management, and consulting services. Its technology arm publishes developer APIs through developer.cbre.com that expose property, analytics, and facilities data to partners.'
features:
- name: Property Search
- name: Listing Management
- name: Lease Administration
- name: Market Analytics
- name: Valuation
- name: Facilities Management
- name: Work Order Management
- name: Space Utilization
- name: Investment Management
- name: Transaction Services
- name: Portfolio Reporting
- name: Sustainability Metrics
finops:
- name: Cbre Finops
  service_category: Commercial Real Estate Services
  slug: cbre-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cbre.png
layout: provider
modified: '2026-05-19'
name: CBRE
nav: Providers
network: true
overview: 'CBRE publishes 1 API on the [APIs.io](https://apis.io/) network: Real Estate API. Tagged areas include Analytics, Commercial Real Estate, Facilities Management, Fortune 500, and Investment Management.


  CBRE''s developer surface includes authentication, developer portal, and 15 more developer resources.'
plans:
- name: Cbre Plans Pricing
  plan_count: 1
  slug: cbre-plans-pricing
press:
- date: '2026-05-25'
  title: CBRE chooses AI veteran to fill new C-suite role
  url: https://www.costar.com/article/401170000/cbre-creates-c-level-role-adds-leader-with-ai-history
- date: '2026-05-25'
  title: Investment in artificial intelligence is fueling office demand ...
  url: https://www.facebook.com/foxsanantonio/posts/investment-in-artificial-intelligence-is-fueling-office-demand-in-a-handful-of-t/1383861323789368/
- date: '2026-05-25'
  title: CBRE Investment Management's AI-Enhanced Data ...
  url: https://www.cbreim.com/press-releases/cbreim-ai-enhanced-data-collection-global-real-estate-secondaries-excess-us23-billion-annually
- date: '2026-05-25'
  title: CBRE Deepens AI And Data Center Push As Valuation ...
  url: https://finance.yahoo.com/news/cbre-deepens-ai-data-center-210925799.html
- date: '2026-05-25'
  title: Companies Add Artificial Intelligence Expertise with ...
  url: https://www.cbre.com/press-releases/companies-add-artificial-intelligence-expertise-with-specialized-jobs-skills-amid-slower-tech-talent
random_paper: 4
rate_limits:
- limit_count: 1
  name: Cbre Rate Limits
  slug: cbre-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cbre/refs/heads/main/screenshots/cbre-2026-06-20T174059.png
security:
- kind: authentication
  name: Cbre Authentication
  slug: cbre-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cbre Domain Security
  slug: cbre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cbre
tags:
- Analytics
- Commercial Real Estate
- Facilities Management
- Fortune 500
- Investment Management
- Property Management
- Real Estate
- Valuation
use_cases:
- name: Corporate Real Estate Portfolio Management
- name: Commercial Property Marketing
- name: Facilities Operations
- name: Lease Accounting (ASC 842 / IFRS 16)
- name: Investment Fund Reporting
- name: Workplace Occupancy Analytics
- name: Market Research and Forecasting
website: https://www.cbre.com
---
