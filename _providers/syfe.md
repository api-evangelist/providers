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
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syfe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.syfe.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.syfe.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.syfe.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.syfe.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.syfe.com/magazine/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syfe.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syfe.com/hk/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syfe-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/syfe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.syfe.com/bug-bounty
- group: design
  title: ''
  type: Conformance
  url: conformance/syfe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.syfe.com/security
coverage:
  checked: '2026-08-29'
  detail: Syfe ships consumer and business wealth-management apps only — its sitemap index carries zero URLs matching api/developer/docs/integration, developer.syfe.com and docs.syfe.com do not resolve, and the sole API host api.syfe.com is the private application backend that answers a Cloudflare challenge on every path including robots.txt.
  evidence:
  - status: 200
    url: https://www.syfe.com/sitemap_index.xml
  - status: 0
    url: https://developer.syfe.com/
  - status: 403
    url: https://api.syfe.com/openapi.json
  - status: 200
    url: https://www.syfe.com/openapi.json
  - status: 200
    url: https://www.syfe.com/syfe-for-business
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: 'Syfe is a Singapore-headquartered digital wealth management platform, licensed by the Monetary Authority of Singapore under Capital Markets Services licence CMS100837 and operating in Singapore, Hong Kong and Australia (where it trades as Selfwealth by Syfe). Founded in 2019 by Dhruv Arora and backed by Valar Ventures and Unbound, Syfe combines robo-advised managed portfolios (Core, REIT+, Income+, Select Themes), a self-directed brokerage for US, Singapore and Hong Kong listed stocks and ETFs, and Cash+ cash-management products, alongside a private wealth and a business treasury offering. Syfe is a consumer and business end-user product company: as of this profile it publishes no public developer portal, API reference, machine-readable specification, SDK or webhook surface. Its application backend at api.syfe.com is a private, WAF-protected first-party host and is not a documented developer API.'
image: https://cdn.prod.website-files.com/64d3542964db4e6ae6de7d1d/66e14507296bdb1ed3c04bc8_Syfe%20Homepage%20Open%20Graph.png
layout: provider
modified: '2026-08-29'
name: Syfe
nav: Providers
network: true
overview: 'Syfe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Wealth Management, Investing, and Brokerage.


  Syfe''s developer surface includes pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Syfe Plans Pricing
  plan_count: 0
  slug: syfe-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Syfe Rate Limits
  slug: syfe-rate-limits
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 24.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syfe/refs/heads/main/screenshots/syfe-2026-09-02T161434.png
security:
- kind: domain-security
  name: Syfe Domain Security
  slug: syfe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Syfe Vulnerability Disclosure
  slug: syfe-vulnerability-disclosure
  summary_line: Hackerone
slug: syfe
tags:
- Company
- Financial-Services
- Wealth Management
- Investing
- Brokerage
- Robo-Advisor
- Cash Management
- Fintech
- Singapore
- Asia Pacific
website: https://www.syfe.com/
---
