---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - '{''url'': ''https://www.lendingclub.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.happen.com/?b=7f79f2de-7eb3-4ffe-b2e9-613ff6c70b41 — a different registrable domain (lendingclub.com -> happen.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-06'
api_count: 1
apis:
- description: 'No public contract or reference is published for this API. api.lendingclub.com is live and gated - /api/investor/v1/accounts/1/summary answers HTTP 401 and /api/investor/v1/loans/listing answers HTTP '
  name: LendingClub API
  slug: lendingclub-api
artifact_total: 5
common:
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
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.happen.com/company/contact/investor-relations
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lendingclub-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lendingclub-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendingclub-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LendingClub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/happenbank
- group: build
  title: ''
  type: Packages
  url: packages/lendingclub-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.happen.com
coverage:
  checked: '2026-09-06'
  detail: The LCX Primary and Secondary Market REST API technical documentation, live as recently as 2026-06-08, now returns HTTP 404 on both lendingclub.com and happen.com after the Happen Bank rebrand, leaving the "API-driven purchasing" that Marketplace Connect still advertises reachable only through the institutions-and-banks contact-sales form.
  evidence:
  - status: 404
    url: https://www.happen.com/institutional-investing/lcxpm-api
  - status: 404
    url: https://www.happen.com/developers/api-overview
  - status: 200
    url: https://www.happen.com/institutional-investing/overview
  - status: 200
    url: https://www.happen.com/company/contact/institutions-and-banks
  - status: 401
    url: https://api.lendingclub.com/api/investor/v1/accounts/1/summary
  reason: sales-gate
  state: gated
created: '2026-04-19'
description: 'LendingClub is a US consumer-finance company and national bank, founded in 2006 as a peer-to-peer marketplace lender and now a Fortune 1000 digital bank following its 2021 acquisition of Radius Bancorp. In 2026 it rebranded as Happen Bank, N.A. and moved its web presence from lendingclub.com to happen.com. It no longer operates a public developer program: the /developers tree and the LCX Primary and Secondary Market API technical documentation were withdrawn during the rebrand and now return HTTP 404, while the legacy investor host api.lendingclub.com remains live but gated and undocumented. The API the company still markets - "API-driven purchasing" inside Marketplace Connect for institutional loan buyers - is reachable only through an institutional contact-sales form, with no published reference or machine-readable contract.'
finops:
- name: Lendingclub Finops
  service_category: Financial Services / API
  slug: lendingclub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lendingclub.png
layout: provider
modified: '2026-09-06'
name: LendingClub
nav: Providers
network: true
overview: 'LendingClub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Personal Loans, Banking, Financial Services, and Marketplace Lending.


  LendingClub''s developer surface includes support, engineering blog, and 13 more developer resources.'
plans:
- name: Lendingclub Plans Pricing
  plan_count: 0
  slug: lendingclub-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Lendingclub Rate Limits
  slug: lendingclub-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/lendingclub/refs/heads/main/screenshots/lendingclub-2026-06-20T184419.png
security:
- kind: domain-security
  name: Lendingclub Domain Security
  slug: lendingclub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lendingclub
tags:
- Fintech
- Personal Loans
- Banking
- Financial Services
- Marketplace Lending
- Consumer Lending
website: https://www.happen.com
---
