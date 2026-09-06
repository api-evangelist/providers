---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Simplifi by Quicken provides a consumer personal finance platform that connects to financial institutions via OAuth APIs and biller networks via purpose-built APIs. Users can aggregate bank accounts, '
  name: Simplifi by Quicken API
  slug: simplifi-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplifi-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/simplifi/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/simplifi/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/simplifi/refs/heads/main/finops/finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://support.simplifi.quicken.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.quicken.com/blog/search/simplifi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quicken.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quicken.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/simplifi-by-quicken-status
- group: operate
  title: ''
  type: Community
  url: https://community.simplifimoney.com/
created: '2026-06-13'
description: Simplifi by Quicken is a personal finance management application that aggregates financial accounts from over 14,000 institutions, enabling users to track spending, manage budgets, monitor investments, set savings goals, and access projected cash flow analytics. The platform uses OAuth-based API connections to banks and purpose-built APIs to billers to pull data into a unified financial dashboard available on web and mobile.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplifi.png
layout: provider
modified: '2026-06-13'
name: Simplifi by Quicken
nav: Providers
network: true
overview: 'Simplifi by Quicken publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Finance, Budgeting, Financial Aggregation, Account Management, and Spending Tracking.


  Simplifi by Quicken''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simplifi/refs/heads/main/screenshots/simplifi-2026-06-20T193937.png
security:
- kind: domain-security
  name: Simplifi Domain Security
  slug: simplifi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simplifi
tags:
- Personal Finance
- Budgeting
- Financial Aggregation
- Account Management
- Spending Tracking
- Investment Tracking
- Savings Goals
- Cash Flow
---
