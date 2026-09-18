---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.synovus.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synovus
- group: operate
  title: ''
  type: Support
  url: https://www.synovus.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.synovus.com/corporate/insights/
- group: company
  title: ''
  type: Newsroom
  url: https://www.synovus.com/about-us/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.pnfp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synovus.com/contact-us/privacy-policy/
- group: auth
  title: ''
  type: X-SecurityIncidentReporting
  url: https://www.synovus.com/contact-us/incident-reporting/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/synovus-financial/refs/heads/main/security/synovus-financial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synovus-financial-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synovus-financial/refs/heads/main/llms/synovus-financial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synovus-financial-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/synovus-financial/refs/heads/main/plans/synovus-financial-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synovus-financial-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/synovus-financial/refs/heads/main/rate-limits/synovus-financial-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/synovus-financial-rate-limits.yml
coverage:
  checked: '2026-09-17'
  detail: developer.synovus.com is a deliberately provisioned Akamai host (explicit edgekey CNAME, no wildcard DNS) that answers HTTP 403 "Access Denied" on every path — root, /docs, /openapi.json, robots.txt, llms.txt and every /.well-known/* document — from two separate egress networks, while the api.synovus.com base the prior scaffold named does not resolve in DNS; the only integration surfaces Synovus advertises (Gateway ERP via Koxa, Accelerate Pay) are reached through the bank relationship, not a public reference.
  evidence:
  - status: 403
    url: https://developer.synovus.com/
  - status: 403
    url: https://developer.synovus.com/docs
  - status: 403
    url: https://developer.synovus.com/openapi.json
  - status: 404
    url: https://www.synovus.com/.well-known/api-catalog
  - status: 404
    url: https://www.synovus.com/llms.txt
  - status: 0
    url: https://api.synovus.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-04-19'
description: 'Synovus Financial Corp. was a Columbus, Georgia based regional bank holding company whose bank subsidiary, Synovus Bank, provides commercial and consumer banking, treasury and payment solutions (Synovus Gateway and the Accelerate AR, FX, Pay and Trade suite), wealth services and capital markets across Georgia, Alabama, Florida, South Carolina and Tennessee. Synovus combined with Pinnacle Financial Partners in 2026 — synovus.com states "Synovus and Pinnacle Financial Partners are now one firm" and investors.synovus.com redirects to investors.pnfp.com — so the surviving company is Pinnacle. Synovus publishes no public API contract: developer.synovus.com is a provisioned Akamai host that answers HTTP 403 Access Denied on every path from two networks, api.synovus.com does not resolve, and www.synovus.com serves no discovery documents. Treasury integration runs through partners — Gateway ERP (October 2025) is powered by Koxa — and the Maast subsidiary has been wound down.'
finops:
- name: Synovus Financial Finops
  service_category: Banking
  slug: synovus-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synovus-financial.png
layout: provider
modified: '2026-09-17'
name: Synovus Financial
nav: Providers
network: true
overview: 'Synovus Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial-Services, Regional Bank, Treasury Management, and Payments.


  Synovus Financial''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Synovus Financial Plans Pricing
  plan_count: 1
  slug: synovus-financial-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Synovus Financial Rate Limits
  slug: synovus-financial-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 5.3
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/synovus-financial/refs/heads/main/screenshots/synovus-financial-2026-06-20T194832.png
security:
- kind: domain-security
  name: Synovus Financial Domain Security
  slug: synovus-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: synovus-financial
tags:
- Banking
- Financial-Services
- Regional Bank
- Treasury Management
- Payments
- United States
- Pinnacle-Financial-Partners
website: https://www.synovus.com
---
