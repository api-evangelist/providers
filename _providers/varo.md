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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: Consumer-facing checking-account capability of Varo Bank, N.A., covering fee-free checking, early direct deposit (up to two days early), debit card management, access to 55,000+ Allpoint ATMs, cash de
  name: Varo Bank Account API
  slug: varo-bank-account
- description: High-yield savings capability delivering up to 5.00% APY on balances up to $5,000 (2.50% APY above that threshold), with automated savings tools, round-ups, named savings goals, and no monthly fees. A
  name: Varo Savings Account API
  slug: varo-savings-account
- description: 'Short-term cash advance capability enabling eligible Varo customers to access $20–$500 with a flat fee and no interest, repaid automatically on the next qualifying direct deposit, providing overdraft '
  name: Varo Advance (Cash Advance) API
  slug: varo-advance
- description: Personal-credit capability offering up to $2,000 with a single flat fee, no interest, no late fees or prepayment penalties, and repayment terms up to 12 months, designed to provide flexible, consumer-
  name: Varo Personal Line of Credit API
  slug: varo-line-of-credit
- description: Secured Visa credit-builder capability supporting on-time payment tracking, reporting to all major credit bureaus, and credit score monitoring, with no annual fee and no interest — customers see an av
  name: Varo Believe Credit-Builder API
  slug: varo-believe
- description: The real, documented seam through which third-party applications reach Varo Bank account data. Varo runs a native Plaid integration that lets customers link their Varo accounts to external financial a
  name: Varo Aggregator Data Access (Plaid)
  slug: varo-aggregator-access
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/varo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.varomoney.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/varo-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/varo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/varo-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/varo-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.varomoney.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.varomoney.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.varomoney.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/varobank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/varobank
- group: company
  title: ''
  type: Blog
  url: https://www.varomoney.com/blog/
- group: company
  title: ''
  type: EngineeringBlog
  url: https://medium.com/engineering-varo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.varomoney.com/bank-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.varomoney.com/privacy-legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.varomoney.com/privacy-legal/
- group: operate
  title: ''
  type: StatusPage
  url: https://statusgator.com/services/varo
- group: other
  title: ''
  type: X
  url: https://x.com/varobank
- group: other
  title: ''
  type: OpenBankingTracker
  url: https://www.openbankingtracker.com/provider/varomoney
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/varo/refs/heads/main/plans/varo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/varo/refs/heads/main/rate-limits/varo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/varo/refs/heads/main/finops/varo-finops.yml
created: '2026-06-13'
description: Varo Bank is a mobile-first, FDIC-chartered digital bank offering fee-free checking and high-yield savings accounts, early direct deposit, instant cash advances, a credit-builder card, and a personal line of credit. Varo does not operate a public, first-party developer API or developer portal; its consumer banking data is reachable by third-party applications only through US open-finance aggregators such as Plaid (a documented, native integration), and potentially MX, Finicity, or Akoya. The surface catalogued here maps Varo's real consumer product family and the aggregator seam through which that data is accessed.
finops:
- name: Varo Finops
  service_category: ''
  slug: varo-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for Varo Money (Varo Bank), a mobile-first, FDIC-chartered digital bank. Varo offers fee-free checking and high-yield savings accounts, early direct
  name: Varo Money GraphQL Schema
  slug: varo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/varo.png
layout: provider
modified: '2026-07-23'
name: Varo Bank
nav: Providers
network: true
overview: 'Varo Bank publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Fintech, Consumer Finance, Savings, and Cash Advance.


  Varo Bank''s developer surface includes documentation, support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Varo Plans Pricing
  plan_count: 5
  slug: varo-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 6
  name: Varo Rate Limits
  slug: varo-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 7.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 29.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/varo/refs/heads/main/screenshots/varo-2026-06-20T200822.png
security:
- kind: domain-security
  name: Varo Domain Security
  slug: varo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Varo Vulnerability Disclosure
  slug: varo-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: varo
tags:
- Banking
- Fintech
- Consumer Finance
- Savings
- Cash Advance
- Credit Builder
- Open Banking
- Mobile Banking
- Digital Bank
- United States
website: https://www.varomoney.com/
---
