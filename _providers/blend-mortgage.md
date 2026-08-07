---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Blend Mortgage Agentic Access
  operation_count: 52
  slug: blend-mortgage-agentic-access
  summary_line: 52 operations · 25 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Borrowers, coborrowers, realtors, employers, incomes, and positions.
  name: Blend Borrowers & Parties API
  slug: blend-mortgage-borrowers-parties-api
- description: Closings, packages, eNotes, and RON sessions.
  name: Blend Closings & eSignature API
  slug: blend-mortgage-closings-esignature-api
- description: Consumer lending, account opening, and deposit account applications.
  name: Blend Consumer Lending & Deposit API
  slug: blend-mortgage-consumer-lending-deposit-api
- description: Documents, disclosures, tax transcripts, and loan file export.
  name: Blend Documents & Disclosures API
  slug: blend-mortgage-documents-disclosures-api
- description: Event notifications and event status.
  name: Blend Events & Webhooks API
  slug: blend-mortgage-events-webhooks-api
- description: Borrower tasks and conditions.
  name: Blend Follow-ups API
  slug: blend-mortgage-follow-ups-api
- description: Create and manage mortgage (home lending) applications.
  name: Blend Home Lending Applications API
  slug: blend-mortgage-home-lending-applications-api
- description: Lender users and application assignments.
  name: Blend Lenders & Assignments API
  slug: blend-mortgage-lenders-assignments-api
- description: Apply a priced product to a loan.
  name: Blend Products & Pricing API
  slug: blend-mortgage-products-pricing-api
- description: Reporting and analytics datasets.
  name: Blend Reporting API
  slug: blend-mortgage-reporting-api
artifact_total: 17
collections:
- collection_type: open
  name: Blend Public API
  slug: open-blend-mortgage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blend-mortgage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blend-mortgage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blend-mortgage-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blendlabs-inc-
- group: company
  title: ''
  type: Website
  url: https://blend.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.blend.com/blend
- group: docs
  title: ''
  type: APIReference
  url: https://developers.blend.com/blend/reference
- group: start
  title: ''
  type: SignUp
  url: https://developers.blend.com/blend/docs/blend-api-quick-start-guide
- group: company
  title: ''
  type: Blog
  url: https://blend.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/blend-mortgage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blend-mortgage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blend-mortgage-finops.yml
created: '2026-07-04'
description: Blend (Blend Labs) is a cloud digital-lending and account-opening platform for banks, credit unions, and mortgage lenders. Its Builder platform powers consumer-facing origination for mortgage (home lending), consumer lending (home equity, personal loans, credit cards, auto), and deposit account opening. The Blend Public API is a documented REST surface (developers.blend.com) that lets lenders and their technology partners create and manage lending applications, borrowers/parties, documents and disclosures, pricing, closings and eSignature packages, follow-ups (tasks), assignments, and webhook event notifications, and to export industry-standard loan files (Fannie Mae 3.2, MISMO 3.3.1/3.4) into a loan origination system (LOS). API access is credential-gated - tokens are issued to Blend customers and certified integration partners rather than through open self-service signup.
finops:
- name: Blend Mortgage Finops
  service_category: Financial Services and Lending Platform
  slug: blend-mortgage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blend-mortgage.png
layout: provider
modified: '2026-07-04'
name: Blend
nav: Providers
network: true
overview: 'Blend publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Borrowers & Parties API, Closings & eSignature API, Consumer Lending & Deposit API, and 7 more. Tagged areas include Digital Lending, Mortgage, Consumer Lending, Account Opening, and FinTech.


  Blend''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Blend Mortgage Plans Pricing
  plan_count: 3
  slug: blend-mortgage-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Blend Mortgage Rate Limits
  slug: blend-mortgage-rate-limits
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 56.1
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blend-mortgage/refs/heads/main/screenshots/blend-mortgage-2026-07-25T203309.png
security:
- kind: authentication
  name: Blend Mortgage Authentication
  slug: blend-mortgage-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Blend Mortgage Domain Security
  slug: blend-mortgage-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: blend-mortgage
tags:
- Digital Lending
- Mortgage
- Consumer Lending
- Account Opening
- FinTech
- Loan Origination
- Banking
- Financial Services
website: https://blend.com
---
