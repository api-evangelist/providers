---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.7
  scored_at: '2026-11-06'
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
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/realpage/well-known/realpage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/realpage-well-known.yml
- group: other
  href: https://artifacts.apis.io/realpage/hosts/realpage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/realpage-hosts.yml
- group: other
  href: https://artifacts.apis.io/realpage/vendors/realpage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/realpage-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.realpage.com/support/security/responsible-disclosure/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RealPage
- group: commercial
  href: https://artifacts.apis.io/realpage/plans/realpage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/realpage-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/realpage/rate-limits/realpage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/realpage-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/realpage/finops/realpage-finops.yml
  title: ''
  type: FinOps
  url: finops/realpage-finops.yml
- group: auth
  href: https://artifacts.apis.io/realpage/security/realpage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/realpage-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/realpage/security/realpage-domain-security.yml
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
  type: DeveloperPortal
  url: https://developer.realpage.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.realpage.com/explore/api
- group: start
  title: ''
  type: SignUp
  url: https://developer.realpage.com/get-started
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realpage.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realpage.com/legal/terms-of-use/
- group: company
  title: ''
  type: Newsroom
  url: https://www.realpage.com/news/
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
coverage:
  checked: '2026-10-20'
  detail: developer.realpage.com publicly lists 16 AppPartner APIs (Accounts Payable v2, Knock API, Resident Management, Units...) as route names only, with route-level docs and credentials behind AppPartner vendor registration at /get-started, so no contract was published or generatable.
  evidence:
  - status: 200
    url: https://developer.realpage.com/explore/api
  - status: 200
    url: https://developer.realpage.com/get-started
  - status: 404
    url: https://api.realpage.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-05-23'
description: RealPage is a multifamily and rental-housing software company offering property management, marketing, leasing, resident experience, accounting, facilities, utility, spend, revenue management, and AI workforce tooling across a large portfolio of products including OneSite, Knock CRM, G5 Marketing, Online Leasing, LOFT Resident Portal, AI Revenue Management, Lumina AI Workforce, and the RealPage Exchange (RPX) integration platform. RealPage is enterprise sales-led; partner integrations are exposed through the RPX integration marketplace and provisioned under contract rather than via a public self-serve developer portal.
finops:
- has_sources: false
  method: generated
  name: Realpage Finops
  primary_unit: ''
  service_category: API
  slug: realpage-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realpage.png
layout: provider
modified: '2026-07-25'
name: RealPage
nav: Providers
network: true
overview: 'RealPage is listed with 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Multifamily, Rental Housing, Revenue Management, and Leasing.


  RealPage''s developer surface includes engineering blog, API reference, signup flow, training material, support, and 17 more developer resources.'
plans:
- name: Realpage Plans Pricing
  plan_count: 1
  slug: realpage-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Realpage Rate Limits
  slug: realpage-rate-limits
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 63.4
    operational_transparency: 13.2
  previous_composite: 25.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/realpage/realpage-2026-06-20T192646.png
security:
- kind: domain-security
  name: Realpage Domain Security
  slug: realpage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Realpage Vulnerability Disclosure
  slug: realpage-vulnerability-disclosure
  summary_line: no policy recorded
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
