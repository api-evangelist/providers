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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://career.wingeat.com/
- group: company
  title: ''
  type: About
  url: https://career.wingeat.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wingeat-inc
- group: operate
  title: ''
  type: Support
  url: https://www.wingeat.com/cs-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.wingeat.com/cs-center/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wingeat.com/term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wingeat.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agreable/refs/heads/main/security/agreable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agreable-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agreable/refs/heads/main/conformance/agreable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agreable-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agreable/refs/heads/main/lifecycle/agreable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agreable-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agreable/refs/heads/main/packages/agreable-packages.yml
  title: ''
  type: Packages
  url: packages/agreable-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agreable/refs/heads/main/plans/agreable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agreable-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agreable/refs/heads/main/rate-limits/agreable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agreable-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: Agreable (now 주식회사 윙잇 / Wing Eat, Inc.) is a direct-to-consumer frozen-food retailer whose software is entirely internal — api.wingeat.com answers "Cannot GET" on every path, erp.wingeat.com is a private Vercel SPA, and the wingeat-inc GitHub organization has zero public repositories, so there is no developer portal, no specification and no agent surface to profile.
  evidence:
  - status: 404
    url: https://api.wingeat.com/openapi.json
  - status: 404
    url: https://www.wingeat.com/llms.txt
  - status: 404
    url: https://career.wingeat.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/wingeat-inc
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Agreable (아그레아블) is a South Korean direct-to-consumer brand-commerce company founded by Lim Seung-jin (임승진, "Jason Im") out of a reading-club community of the same name. It has run the frozen convenience-food platform Wingeat (윙잇, wingeat.com) since 2015, and in March 2022 renamed itself after that brand — the operating legal entity is now 주식회사 윙잇 (Wing Eat, Inc.) in Guro-gu, Seoul, and agreable.com and agreable.co.kr both redirect to career.wingeat.com. The company designs, contract-manufactures and fulfils its own private-label food brands — 윙잇Dining, 윙잇Made, 고른, 페이보잇, 랠리 and 방아당 — across more than 200 products. It is a consumer packaged-goods and retail operator, not a software vendor: it builds its storefront, ERP and fulfilment systems in house on private hosts and publishes no developer portal, no public API, no SDK, no machine-readable specification and no agent surface of any kind. Its GitHub organization, wingeat-inc, carries zero public repositories.'
image: https://image.wingeat.com/og/images/0d8f505b-654a-4b48-9a68-31866dee9148.png
layout: provider
modified: '2026-09-12'
name: Agreable
nav: Providers
network: true
overview: 'Agreable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Food and Beverage, and Convenience Food.


  Agreable''s developer surface includes support and 12 more developer resources.'
plans:
- name: Agreable Plans Pricing
  plan_count: 0
  slug: agreable-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Agreable Rate Limits
  slug: agreable-rate-limits
score:
  band: emerging
  composite: 12.7
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
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 12.7
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agreable Domain Security
  slug: agreable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agreable
tags:
- Company
- E-Commerce
- Retail
- Food and Beverage
- Convenience Food
- Consumer Packaged Goods
- Direct to Consumer
- Private Label
- South Korea
website: https://career.wingeat.com/
---
