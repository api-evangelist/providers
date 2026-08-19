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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sofi Agentic Access
  operation_count: 2
  slug: sofi-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 4
apis:
- description: SoFi's partner-offer-api (documented as Partner Offer Pre Qual V2) is a real, first-party external REST API that exposes SoFi's underwriting model to approved partners, returning real-time Personal Lo
  name: SoFi Partner Offer Pre-Qualification API
  slug: sofi-partner-offer-api
- description: SoFi's Home Loan Affiliate Lead API is a real, first-party REST endpoint that lets approved affiliate partners submit home-loan leads to SoFi via POST /afpq/api/v1/affiliate/lead/home-loan. The docume
  name: SoFi Home Loan Affiliate Lead API
  slug: sofi-home-loan-affiliate-lead-api
- description: SoFi Business Banking (marketed as Big Business Banking) is SoFi Bank, N.A.'s API-driven commercial platform combining a nationally chartered bank with direct Federal Reserve access to move money in r
  name: SoFi Business Banking API
  slug: sofi-business-banking-api
- description: SoFi Tech Solutions (formerly Galileo Financial Technologies, a SoFi company) is SoFi's B2B fintech platform arm, exposing cloud-native RESTful APIs - Program API (accounts, cards), Config API, Disput
  name: SoFi Tech Solutions Platform API
  slug: sofi-tech-solutions-platform-api
artifact_total: 28
collections:
- collection_type: open
  name: SoFi Home Loan Affiliate Lead API
  slug: open-sofi-home-loan-affiliate-lead-api
- collection_type: open
  name: SoFi Partner Offer Pre-Qualification API
  slug: open-sofi-partner-offer-api
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: sofi-mcp.yml
  slug: sofi-mcpyml
modified: '2026-07-23'
name: SoFi
nav: Providers
network: true
overview: 'SoFi publishes 2 APIs on the [APIs.io](https://apis.io/) network: Partner Offer Pre-Qualification API and Home Loan Affiliate Lead API. Tagged areas include Personal Finance, Banking, Lending, Student Loans, and Mortgages.


  SoFi''s developer surface includes authentication, documentation, engineering blog, pricing, support, sandbox, and 22 more developer resources.'
plans:
- name: Sofi Plans Pricing
  plan_count: 2
  slug: sofi-plans-pricing
random_paper: 135
rate_limits:
- limit_count: 2
  name: Sofi Rate Limits
  slug: sofi-rate-limits
score:
  band: developing
  composite: 49.0
  delta: 1.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 42.3
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 47.8
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- Banking-as-a-Service
- Partner API
- Business Banking
- United States
website: https://www.sofi.com/
---
