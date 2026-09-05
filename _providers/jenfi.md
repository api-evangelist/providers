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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jenfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jenfi.com/
- group: company
  title: ''
  type: About
  url: https://jenfi.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://jenfi.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://jenfi.com/feed/
- group: company
  title: ''
  type: Partners
  url: https://jenfi.com/partner-with-jenfi/
- group: start
  title: ''
  type: SignUp
  url: https://partners.jenfi.com/accounts/signup/
- group: start
  title: ''
  type: Login
  url: https://partners.jenfi.com/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jenfi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jenfi.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jenfi-eng
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jenfi/
- group: other
  title: ''
  type: X
  url: https://x.com/jenficapital
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/jenficapital/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/jenfi
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jenfi-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/jenfi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jenfi-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: 'Jenfi markets "Embedded Financing — integrating our financing solutions" on https://jenfi.com/partner-with-jenfi/ but publishes no developer portal, reference or spec behind it: the page ends at "Speak with us to find out more" and a contact form, and the only integration surface, the b2b BNPL partner console, 302s to partners.jenfi.com/accounts/login/ and returns a real 404 on every spec, /.well-known/ and GraphQL/MCP path probed.'
  evidence:
  - status: 202
    url: https://jenfi.com/partner-with-jenfi/
  - status: 200
    url: https://partners.jenfi.com/
  - status: 404
    url: https://partners.jenfi.com/openapi.json
  - status: 404
    url: https://partners.jenfi.com/graphql
  - status: 404
    url: https://partners.jenfi.com/.well-known/agent-card.json
  - status: 404
    url: https://api.paidfi.com/openapi.json
  - status: 0
    url: https://app.jenfi.com/accounts/sign_in
  reason: sales-gate
  state: gated
created: '2026-08-23'
description: 'Jenfi is a Singapore-headquartered SME credit platform for digitally-enabled businesses in Southeast Asia, operating principally in Singapore and Vietnam. Founded in 2019 by Jeffrey Liu and Justin Louie and backed by Y Combinator, Monk''s Hill Ventures and Headline, it started with revenue-based financing — non-dilutive growth capital repaid as a percentage of monthly revenue rather than on a fixed schedule — and has since broadened into growth financing, working capital and supply-chain financing, alongside a B2B buy-now-pay-later product marketed as PaidFi ("b2b BNPL by Jenfi"). In May 2026 the company reported passing US$100 million in cumulative originations across more than 2,400 financings, from over 30,000 evaluated enquiries. Jenfi publishes no public developer portal, API reference, or machine-readable contract: its only integration surface is a login-gated partner console at partners.jenfi.com and a contact-sales "Embedded Financing" offer on its partner page.'
image: https://avatars.githubusercontent.com/u/50892604?s=200&v=4
layout: provider
modified: '2026-08-23'
name: Jenfi
nav: Providers
network: true
overview: 'Jenfi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Lending, and SME Finance.


  Jenfi''s developer surface includes engineering blog, signup flow, and 16 more developer resources.'
plans:
- name: Jenfi Plans Pricing
  plan_count: 0
  slug: jenfi-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Jenfi Rate Limits
  slug: jenfi-rate-limits
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jenfi/refs/heads/main/screenshots/jenfi-2026-09-02T145938.png
security:
- kind: domain-security
  name: Jenfi Domain Security
  slug: jenfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jenfi
tags:
- Company
- Financial-Services
- Fintech
- Lending
- SME Finance
- Revenue-Based Financing
- Working Capital
- Supply Chain Finance
- Buy Now Pay Later
- Embedded Finance
- Southeast Asia
- Singapore
- Vietnam
website: https://jenfi.com/
---
