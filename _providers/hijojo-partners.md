---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hijojo-partners-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hijojo-partners-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hijojo-partners-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.hijojo-partners.com/
- group: company
  title: ''
  type: About
  url: https://www.hijojo-partners.com/en/about/company
- group: company
  title: ''
  type: News
  url: https://www.hijojo-partners.com/en/news
- group: operate
  title: ''
  type: Support
  url: https://www.hijojo.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://www.hijojo.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://members.hijojo.com/register/memberinfo
- group: start
  title: ''
  type: Login
  url: https://members.hijojo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hijojo.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hijojo.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.hijojo-partners.com/en/inquiry
- group: commercial
  title: ''
  type: Plans
  url: plans/hijojo-partners-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hijojo-partners-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: HiJoJo Partners ships an end-user investment platform only - the member application at members.hijojo.com is a login wall with no API behind it that the company documents, and DNS enumeration returns no api., dev., developer., docs., portal. or mcp. host on either hijojo-partners.com or hijojo.com.
  evidence:
  - status: 404
    url: https://members.hijojo.com/openapi.json
  - status: 404
    url: https://members.hijojo.com/graphql
  - status: 404
    url: https://www.hijojo-partners.com/openapi.json
  - status: 404
    url: https://www.hijojo-partners.com/llms.txt
  - status: 403
    url: https://www.hijojo.com/.well-known/agent-card.json
  - status: 200
    url: https://www.hijojo-partners.com/en/about/company
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'HiJoJo Partners Inc. (HiJoJo Partners株式会社) is a Tokyo-based independent asset management and fintech group, established in November 2017 and registered with the Director of the Kanto Local Finance Bureau (No. 3065) for Type II Financial Instruments Business, Investment Management Business, and Investment Advisory and Agency Business. The firm forms, sells and manages funds that give Japanese institutional and individual investors access to late-stage private and pre-IPO companies, and works to develop Japan''s secondary market for unlisted shares. It operates three lines: HiJoJo Prime (in-person advisory for investors with 100M JPY or more in investable assets), HiJoJo.com (an online fund platform for individual investors with 30M JPY or more), and HiJoJo Private Market Solution for institutional investors and startups. HiJoJo joined the Nasdaq Private Market investor consortium in 2024 to expand secondary-market access in Japan. Its investor-facing platform is delivered as
  an authenticated member web application; the company publishes no public API, developer portal, SDK or machine-readable specification of any kind.'
image: https://www.hijojo-partners.com/ogp.jpg
layout: provider
modified: '2026-08-22'
name: HiJoJo Partners
nav: Providers
network: true
overview: 'HiJoJo Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Investment Management, Private Markets, and Secondary Markets.


  HiJoJo Partners'' developer surface includes product news, support, FAQ, signup flow, and 11 more developer resources.'
plans:
- name: Hijojo Partners Plans Pricing
  plan_count: 0
  slug: hijojo-partners-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Hijojo Partners Rate Limits
  slug: hijojo-partners-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.5
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Hijojo Partners Domain Security
  slug: hijojo-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hijojo-partners
tags:
- Company
- Financial-Services
- Investment Management
- Private Markets
- Secondary Markets
- Pre-IPO
- Venture Capital
- Fintech
- Japan
- Asset Management
website: https://www.hijojo-partners.com/
---
