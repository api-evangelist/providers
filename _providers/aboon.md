---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aboon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aboon.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.aboon.com/
- group: start
  title: ''
  type: Login
  url: https://app.aboon.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aboon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aboon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aboon.com/privacy
created: '2026-07-17'
description: Aboon is a digital 401(k) retirement-plan platform and third-party administrator (TPA) that helps financial advisors and employers design, launch, and manage workplace retirement plans. It pairs AI-powered workflows with dedicated human plan consultants to generate customized 401(k) proposals in minutes, streamline recordkeeper onboarding, handle digital plan contracting and census intake, and run ongoing compliance testing and Form 3(16) administration. Aboon markets partnerships with major recordkeepers (American Funds, Empower, John Hancock, and others) and serves a network of advisors nationwide. It is a fintech company backed by Bain Capital Ventures. No public developer/API surface has been identified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aboon.png
layout: provider
modified: '2026-07-17'
name: Aboon
nav: Providers
network: true
overview: 'Aboon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Retirement, 401k, and Wealth Management.


  Aboon''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aboon/refs/heads/main/screenshots/aboon-2026-07-25T181405.png
security:
- kind: domain-security
  name: Aboon Domain Security
  slug: aboon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aboon
tags:
- Company
- Fintech
- Retirement
- 401k
- Wealth Management
- Financial-Services
- TPA
- Recordkeeping
website: https://www.aboon.com/
---
