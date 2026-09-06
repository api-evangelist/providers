---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sofi Agentic Access
  operation_count: 2
  slug: sofi-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: SoFi Business Banking (marketed as Big Business Banking) is SoFi Bank, N.A.'s API-driven commercial platform combining a nationally chartered bank with direct Federal Reserve access to move money in r
  name: SoFi Business Banking API
  slug: sofi-business-banking-api
- description: SoFi Tech Solutions (formerly Galileo Financial Technologies, a SoFi company) is SoFi's B2B fintech platform arm, exposing cloud-native RESTful APIs - Program API (accounts, cards), Config API, Disput
  name: SoFi Tech Solutions Platform API
  slug: sofi-tech-solutions-platform-api
- baseURL: https://www.sofi.com
  baseurl_source: declared
  description: The Affiliate Leads API from SoFi — 1 operation(s) for affiliate leads.
  name: SoFi Affiliate Leads API
  slug: sofi-affiliate-leads-api
- baseURL: https://www.sofi.com
  baseurl_source: declared
  description: The Partner Offers API from SoFi — 1 operation(s) for partner offers.
  name: SoFi Partner Offers API
  slug: sofi-partner-offers-api
artifact_total: 27
collections:
- collection_type: open
  name: SoFi Home Loan Affiliate Lead API
  slug: open-sofi-home-loan-affiliate-lead-api
- collection_type: open
  name: SoFi Partner Offer Pre-Qualification API
  slug: open-sofi-partner-offer-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sofi-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sofi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sofi-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sofi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sofi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sofi.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sofi.com/business-banking/docs
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/sofi-api/team-sofi-s-public-workspace/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sofi
- group: company
  title: ''
  type: Blog
  url: https://www.sofi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sofi.com/sofi-plus/
- group: operate
  title: ''
  type: StatusPage
  url: https://sofi.statuspage.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/SoFi
- group: commercial
  title: ''
  type: Plans
  url: plans/sofi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sofi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sofi-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sofi.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sofi.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.sofi.com/hc/en-us
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sofi-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sofi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sofi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sofi-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sofi-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sofi-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sofi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sofi-partner-offer-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sofi-home-loan-affiliate-lead-api-overlay.yaml
created: '2026-06-13'
description: 'SoFi (Social Finance) is a digital personal finance company and federally chartered bank offering an integrated suite of financial products including banking (checking and savings), personal loans, student loan refinancing, private student loans, mortgages, home equity products, active and automated investing, cryptocurrency trading, and credit cards. The platform is unified through the SoFi app and complemented by a SoFi Plus premium membership ($10/month) that unlocks enhanced APY, investment matching, loan rate discounts, and unlimited financial planner access. Third-party integration with SoFi accounts is facilitated through open banking aggregators Plaid and Finicity (Mastercard Open Banking) for consumer-permissioned data access. SoFi''s subsidiary Galileo Financial Technologies provides the underlying fintech infrastructure and white-label banking APIs used by major fintech brands globally. SoFi does not publish a first-party consumer-facing open-banking API; consumer
  account access is aggregator-only (Plaid, Finicity, MX, Akoya). Its real first-party public API surface is B2B/partner-oriented: two documented REST APIs in SoFi''s public Postman workspace (a Partner Offer Pre-Qualification API exposing SoFi''s PL/SLR underwriting model, and a Home Loan Affiliate Lead API), a Business Banking developer-docs project at docs.sofi.com, and the SoFi Tech Solutions (formerly Galileo) platform at docs.tech.sofi.com.'
features:
- Digital personal finance platform covering banking, lending, investing, and insurance
- SoFi Money combined checking and savings with high-yield APY (4.50% for Plus members)
- Personal loans from $5,000 at fixed rates starting at 6.99% APR
- Student loan refinancing with fixed rates from 3.99% APR with autopay
- Private student loans with no origination, late, or NSF fees
- Mortgage, home equity loan, and HELOC products
- SoFi Invest for stocks, ETFs, fractional shares, crypto, IPOs, and automated investing
- SoFi Credit Card with cash back rewards and Smart Card with 5% grocery cash back
- SoFi Plus premium membership at $10/month with enhanced rates and rewards
- Open banking connectivity via Plaid and Finicity (Mastercard) aggregators
- SoFi Relay credit score monitoring and financial tracking dashboard
- Galileo Financial Technologies subsidiary powering white-label fintech infrastructure APIs
- 100% uptime across Bot, Site, Payment, and Backend services (90-day tracked)
- SoFi Coach AI-powered financial planning tool
- Unlimited financial planner appointments for SoFi Plus members
finops:
- name: Sofi Finops
  service_category: ''
  slug: sofi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sofi.png
layout: provider
modified: '2026-07-23'
name: SoFi
nav: Providers
network: true
overview: 'SoFi publishes 2 APIs on the [APIs.io](https://apis.io/) network: Affiliate Leads API and Partner Offers API. Tagged areas include Personal Finance, Banking, Lending, Student Loans, and Mortgages.


  SoFi''s developer surface includes authentication, documentation, engineering blog, pricing, support, sandbox, and 23 more developer resources.'
plans:
- name: Sofi Plans Pricing
  plan_count: 2
  slug: sofi-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Sofi Rate Limits
  slug: sofi-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 44.6
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sofi/refs/heads/main/screenshots/sofi-2026-06-20T194126.png
security:
- kind: authentication
  name: Sofi Authentication
  slug: sofi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sofi Domain Security
  slug: sofi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sofi
tags:
- Personal Finance
- Banking
- Lending
- Student Loans
- Mortgages
- Investing
- Credit Cards
- Fintech
- Open Banking
- Digital Banking
- Banking as a Service
- Partner API
- Business Banking
- United States
website: https://www.sofi.com/
---
