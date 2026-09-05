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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Consumer-facing checking-account capability of Varo Bank, N.A., covering fee-free checking, early direct deposit (up to two days early), debit card management, access to 55,000+ Allpoint ATMs, cash de
  name: Varo Bank Account API
  slug: varo-bank-account
- description: The real, documented seam through which third-party applications reach Varo Bank account data. Varo runs a native Plaid integration that lets customers link their Varo accounts to external financial a
  name: Varo Aggregator Data Access (Plaid)
  slug: varo-aggregator-access
artifact_total: 8
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
- group: other
  title: ''
  type: ProductPage
  url: https://www.varomoney.com/savings-account/
- group: other
  title: ''
  type: ProductPage
  url: https://www.varomoney.com/cash-advance/
- group: other
  title: ''
  type: ProductPage
  url: https://www.varomoney.com/line-of-credit/
- group: other
  title: ''
  type: ProductPage
  url: https://www.varomoney.com/credit-builder/
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
modified: '2026-07-25'
name: Varo Bank
nav: Providers
network: true
overview: 'Varo Bank publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Fintech, Consumer Finance, Savings, and Cash Advance.


  Varo Bank''s developer surface includes documentation, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Varo Plans Pricing
  plan_count: 5
  slug: varo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Varo Rate Limits
  slug: varo-rate-limits
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 41.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
