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
  url: security/lending-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.happen.com/
- group: company
  title: ''
  type: About
  url: https://www.happen.com/company/about-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.happen.com/help
- group: operate
  title: ''
  type: Support
  url: https://www.happen.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.happen.com/resource-center
- group: start
  title: ''
  type: Login
  url: https://www.happen.com/loans/landing/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.happen.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.happen.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LendingClub
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.happen.com/company/contact/investor-relations
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lending-club-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lending-club-llms.txt
created: '2026-07-17'
description: LendingClub is a US consumer-finance company and digital bank, originally founded in 2006 as a peer-to-peer marketplace lender and later a national bank holding company after its 2021 acquisition of Radius Bancorp. In 2026 the company rebranded as Happen Bank, N.A. (a wholly-owned subsidiary of Happen, Inc.) and moved its public web presence from lendingclub.com to happen.com, where it offers personal loans, auto refinancing, business loans, LevelUp checking and savings accounts, the DebtIQ credit dashboard, and an institutional investing program for marketplace-lending loan buyers. LendingClub historically published a public Investor API for its retail notes marketplace; that marketplace was retired in December 2020 and the developer portal and API documentation are no longer published. As of this enrichment pass the company operates no public developer program, API reference, or SDK surface, and no OpenAPI or event specifications are available to harvest.
image: https://www.happen.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: LendingClub
nav: Providers
network: true
overview: 'LendingClub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Banking, Lending, and Consumer Finance.


  LendingClub''s developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lending-club/refs/heads/main/screenshots/lending-club-2026-07-25T224859.png
security:
- kind: domain-security
  name: Lending Club Domain Security
  slug: lending-club-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lending-club
tags:
- Company
- Financial-Services
- Banking
- Lending
- Consumer Finance
- Fintech
- Marketplace Lending
- Personal Loans
website: https://www.happen.com/
---
