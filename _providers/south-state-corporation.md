---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - llms.txt
  - dns
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: 'Machine-readable filing data for SouthState Bank Corporation is available from the U.S. Securities and Exchange Commission, not from the company. The SEC EDGAR submissions API returns the full filing '
  name: SEC EDGAR Filings (SouthState Bank Corp, CIK 764038)
  slug: sec-edgar-filings
artifact_total: 5
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.southstatebank.com/global/help/terms-of-use
- group: company
  title: ''
  type: Website
  url: https://www.southstatebank.com
- group: company
  title: ''
  type: About
  url: https://www.southstatebank.com/global/about
- group: operate
  title: ''
  type: Support
  url: https://www.southstatebank.com/global/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.southstatebank.com/global/privacy-notice
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/south-state-corporation/refs/heads/main/llms/south-state-corporation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/south-state-corporation-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/south-state-corporation/refs/heads/main/security/south-state-corporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/south-state-corporation-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/south-state-corporation/refs/heads/main/plans/south-state-corporation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/south-state-corporation-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/south-state-corporation/refs/heads/main/rate-limits/south-state-corporation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/south-state-corporation-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/south-state-bank
coverage:
  checked: '2026-09-17'
  detail: SouthState ships end-user and treasury banking software only — the developer.southstatebank.com and api.southstatebank.com hosts do not resolve in DNS, and the bank's own llms.txt (200, curated from its sitemap on 2026-08-24) lists no API, developer, or integration page anywhere on www.southstatebank.com.
  evidence:
  - status: 0
    url: https://developer.southstatebank.com/
  - status: 0
    url: https://api.southstatebank.com/
  - status: 200
    url: https://www.southstatebank.com/llms.txt
  - status: 404
    url: https://www.southstatebank.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'South State Corporation — now SouthState Bank Corporation (NYSE: SSB), the Winter Haven, Florida holding company for SouthState Bank, N.A. — is a Fortune 1000 regional bank serving consumer, mortgage, small business, commercial and wealth customers across the Southeast, Texas and Colorado. It publishes no developer program: the developer.southstatebank.com and api.southstatebank.com hosts that earlier versions of this record pointed at do not resolve in DNS, the bank''s own curated llms.txt (served from www.southstatebank.com, last modified 2026-08-24) lists no API, developer or integration page, and commercial connectivity (Treasury Navigator, Integrated Payables) is file-based treasury tooling sold through a banker, not a public API. Consumer data access reaches SouthState through third-party aggregators. The only real programmatic access to the company is the SEC''s own EDGAR API, listed here as a clearly labelled third-party government API.'
finops:
- name: South State Corporation Finops
  service_category: Regional Banking
  slug: south-state-corporation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/south-state-corporation.png
layout: provider
modified: '2026-09-17'
name: South State Corporation
nav: Providers
network: true
overview: 'South State Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial-Services, Regional Bank, Treasury Management, and Fortune 1000.


  South State Corporation''s developer surface includes support and 9 more developer resources.'
plans:
- name: South State Corporation Plans Pricing
  plan_count: 1
  slug: south-state-corporation-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: South State Corporation Rate Limits
  slug: south-state-corporation-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.8
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    operational_transparency: 5.3
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/south-state-corporation/refs/heads/main/screenshots/south-state-corporation-2026-06-20T194228.png
security:
- kind: domain-security
  name: South State Corporation Domain Security
  slug: south-state-corporation-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: south-state-corporation
tags:
- Banking
- Financial-Services
- Regional Bank
- Treasury Management
- Fortune 1000
- SEC EDGAR
website: https://www.southstatebank.com
---
