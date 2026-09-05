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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eisen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.witheisen.com
- group: company
  title: ''
  type: About
  url: https://www.witheisen.com/about
- group: auth
  title: ''
  type: Compliance
  url: https://www.witheisen.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.witheisen.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.witheisen.com/terms
created: '2026-07-17'
description: Eisen is an AI-enabled compliance operations platform for financial institutions and digital asset companies, managing escheatment (unclaimed property), disbursement, customer outreach, and 1099 tax reporting across all account types. Its product suite includes an Escheatment Manager that tracks state compliance deadlines and dormancy rules, a Disbursement Manager that automates personalized customer payments, an Outreach Manager that re-engages dormant account holders, and a 1099 Reporting Manager for tax reporting. Eisen handles dormant accounts, stale checks, account wind-downs, and forced closures, and is backed by Cowboy Ventures, Homebrew, and Index Ventures. As of this profile Eisen exposes no public developer API, portal, or documentation; this record captures its identity and public web surface.
image: https://cdn.prod.website-files.com/66e479115928652a34d9e8ac/670586219c4bb8d1fe9ae3b3_OG%20image%20(default).jpg
layout: provider
modified: '2026-07-19'
name: Eisen
nav: Providers
network: true
overview: Eisen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Escheatment, Unclaimed Property, and Financial-Services.
random_paper: 7
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eisen/refs/heads/main/screenshots/eisen-2026-07-25T213026.png
security:
- kind: domain-security
  name: Eisen Domain Security
  slug: eisen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eisen
tags:
- Company
- Compliance
- Escheatment
- Unclaimed Property
- Financial-Services
- RegTech
- Disbursements
- Tax Reporting
- Fintech
website: https://www.witheisen.com
---
