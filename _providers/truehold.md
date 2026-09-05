---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truehold-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truehold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truehold.com/
- group: company
  title: ''
  type: About
  url: https://www.truehold.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.truehold.com/post
- group: company
  title: ''
  type: News
  url: https://www.truehold.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.truehold.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truehold.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truehold.com/privacy
- group: other
  title: ''
  type: Licensing
  url: https://www.truehold.com/licensing
- group: start
  title: ''
  type: CustomerPortal
  url: https://my.truehold.com/
- group: company
  title: ''
  type: Careers
  url: https://www.truehold.com/work-with-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truehold
- group: other
  title: ''
  type: Email
  url: mailto:hello@truehold.com
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/truehold-stock
coverage:
  checked: '2026-08-30'
  detail: Truehold buys and rents back houses and originates investor loans; its entire public surface is a Next.js marketing site plus two authenticated customer applications, and /openapi.json, /swagger.json, /api-docs, /docs, /llms.txt, /apis.json and all seven /.well-known paths return 404 on every one of www., my. and app.truehold.com while api., developer. and docs.truehold.com do not resolve at all.
  evidence:
  - status: 404
    url: https://www.truehold.com/openapi.json
  - status: 404
    url: https://www.truehold.com/.well-known/agent-card.json
  - status: 404
    url: https://app.truehold.com/openapi.json
  - status: 0
    url: https://api.truehold.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/Truehold/repos
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: Truehold is a St. Louis, Missouri-founded residential real estate company that buys homes from owners and rents them back to those same owners through a residential sale-leaseback, letting a homeowner convert home equity into cash without moving. Launched in 2021, the company expanded across the Midwest and into the South and Southwest, and in 2025 added Truehold Financial, a Jacksonville, Florida-based lending arm offering DSCR loans, fix-and-flip financing and other investor lending products. Truehold also transacts portfolio sales and multifamily sales with real estate investors. Its public surface is a marketing and lead-generation website plus two authenticated web applications for customers and borrowers; it publishes no developer program, no API documentation and no machine-readable API contract.
image: https://www.truehold.com/assets/og/truehold-og.png
layout: provider
modified: '2026-08-30'
name: Truehold
nav: Providers
network: true
overview: 'Truehold is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Residential Real Estate, Sale-Leaseback, and Home Equity.


  Truehold''s developer surface includes engineering blog, product news, support, and 12 more developer resources.'
plans:
- name: Truehold Plans Pricing
  plan_count: 0
  slug: truehold-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Truehold Rate Limits
  slug: truehold-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truehold/refs/heads/main/screenshots/truehold-2026-09-02T164349.png
security:
- kind: domain-security
  name: Truehold Domain Security
  slug: truehold-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truehold
tags:
- Company
- Real-Estate
- Residential Real Estate
- Sale-Leaseback
- Home Equity
- Property Investment
- Lending
- Financial-Services
website: https://www.truehold.com/
---
