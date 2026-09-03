---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 15.5
  scored_at: '2026-09-02'
api_count: 11
apis:
- description: RealPage's integration marketplace and partner API surface offering standardised APIs across RealPage products for ATS-like data exchange, property data, residents, leases, and financials. Access is p
  name: RealPage Exchange (RPX)
  slug: realpage-exchange
- description: OneSite is RealPage's flagship multifamily property management system covering accounting, leasing, resident, and operational workflows.
  name: RealPage OneSite Property Management System
  slug: onesite
- description: AI-driven rent pricing and revenue management product for multifamily operators, using portfolio and market data to recommend unit-level pricing.
  name: RealPage AI Revenue Management (AIRM)
  slug: ai-revenue-management
- description: AI agent suite operating across operations, leasing, and resident support inside the RealPage product line.
  name: RealPage Lumina AI Workforce
  slug: lumina-ai-workforce
- description: Leasing CRM that captures prospects, manages tours, and tracks conversion across multifamily properties.
  name: RealPage Knock CRM
  slug: knock-crm
- description: Digital marketing platform covering websites, SEO, paid media, and reputation for multifamily and other rental-housing operators.
  name: RealPage G5 Marketing
  slug: g5-marketing
- description: Self-service online leasing workflow covering application, screening, lease execution, and move-in.
  name: RealPage Online Leasing
  slug: online-leasing
- description: Resident-facing portal and mobile app for payments, maintenance requests, communications, and resident services.
  name: RealPage LOFT Resident Portal
  slug: loft-resident-portal
- description: Accounting and financial management products covering general ledger, payables, receivables, and reporting for rental-housing operators.
  name: RealPage Financial Management & Accounting
  slug: financial-accounting
- description: Facilities and maintenance management product covering work orders, preventive maintenance, and vendor coordination.
  name: RealPage Facilities & Maintenance
  slug: facilities
- description: Analytics and benchmarking products covering operational, financial, market, and revenue metrics for the rental-housing portfolio.
  name: RealPage Analytics
  slug: analytics
artifact_total: 17
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/realpage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realpage-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.realpage.com/blog/feed/
- group: company
  title: ''
  type: Website
  url: https://www.realpage.com
- group: start
  title: ''
  type: CustomerPortal
  url: https://realpage.my.site.com/RealPage/s/login/
- group: learn
  title: ''
  type: Training
  url: https://www.realpage.com/training/
- group: operate
  title: ''
  type: Support
  url: https://www.realpage.com/support/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/realpage/
created: '2026-05-23'
description: RealPage is a multifamily and rental-housing software company offering property management, marketing, leasing, resident experience, accounting, facilities, utility, spend, revenue management, and AI workforce tooling across a large portfolio of products including OneSite, Knock CRM, G5 Marketing, Online Leasing, LOFT Resident Portal, AI Revenue Management, Lumina AI Workforce, and the RealPage Exchange (RPX) integration platform. RealPage is enterprise sales-led; partner integrations are exposed through the RPX integration marketplace and provisioned under contract rather than via a public self-serve developer portal.
finops:
- name: Realpage Finops
  service_category: API
  slug: realpage-finops
graphqls:
- description: RealPage is a multifamily real estate software platform. The API covers property management, leasing workflows, resident screening, online rent payment, maintenance requests, lease documents, and occu
  name: RealPage GraphQL API
  slug: realpage-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realpage.png
layout: provider
modified: '2026-07-25'
name: RealPage
nav: Providers
network: true
overview: 'RealPage publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Multifamily, Rental Housing, Revenue Management, and Leasing.


  RealPage''s developer surface includes engineering blog, training material, support, and 5 more developer resources.'
plans:
- name: Realpage Plans Pricing
  plan_count: 1
  slug: realpage-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Realpage Rate Limits
  slug: realpage-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/realpage/refs/heads/main/screenshots/realpage-2026-06-20T192646.png
security:
- kind: domain-security
  name: Realpage Domain Security
  slug: realpage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Realpage Vulnerability Disclosure
  slug: realpage-vulnerability-disclosure
  summary_line: disclosure policy published
slug: realpage
tags:
- Property Management
- Multifamily
- Rental Housing
- Revenue Management
- Leasing
- PropTech
- Resident Experience
website: https://www.realpage.com
---
