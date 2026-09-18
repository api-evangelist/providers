---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 4.7
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/security/afficiency-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afficiency-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afficiency.com/
- group: build
  title: ''
  type: Integration
  url: https://www.afficiency.com/how-afficiency-can-work-for-you/
- group: operate
  title: ''
  type: Support
  url: https://www.afficiency.com/customer-support/
- group: operate
  title: ''
  type: FAQ
  url: https://www.afficiency.com/frequently-asked-questions/
- group: company
  title: ''
  type: News
  url: https://www.afficiency.com/press-room/
- group: company
  title: ''
  type: About
  url: https://www.afficiency.com/meet-the-team/
- group: company
  title: ''
  type: Careers
  url: https://www.afficiency.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.afficiency.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.afficiency.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afficiency.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/afficiency
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/conformance/afficiency-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afficiency-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/conformance/afficiency-conformance.yml
  title: ''
  type: Compliance
  url: conformance/afficiency-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/well-known/afficiency-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/afficiency-robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/llms/afficiency-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afficiency-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/plans/afficiency-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/afficiency-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/rate-limits/afficiency-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/afficiency-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/afficiency/refs/heads/main/packages/afficiency-packages.yml
  title: ''
  type: Packages
  url: packages/afficiency-packages.yml
coverage:
  checked: '2026-09-12'
  detail: Afficiency markets a "robust RESTful API suite" for quote-to-policy-issue but points every documentation request at support.afficiency.com, a HubSpot customer portal that returns HTTP 404 to anonymous clients on its own root, while api.afficiency.com sits behind Cloudflare with an origin that never answers (HTTP 522) — so the contract exists only for signed customers and the only public route to it is the Book a Demo form.
  evidence:
  - status: 404
    url: https://support.afficiency.com/
  - status: 522
    url: https://api.afficiency.com/openapi.json
  - status: 200
    url: https://www.afficiency.com/embedded-insurance/
  - status: 404
    url: https://www.afficiency.com/.well-known/api-catalog
  - status: 404
    url: https://www.afficiency.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-12'
description: Afficiency is a New York-based insurtech that designs, digitally underwrites and issues life insurance products on behalf of carrier and reinsurance partners, and distributes them through a 100% digital, API-first platform. Its product suite spans level term, final expense whole life, participating whole life, indexed universal life and annual renewable term, all issued without a medical exam and with instant underwriting decisions in a single session. Partners integrate through one of three models — a hosted white-label storefront, a direct REST API integration covering the full quote-to-policy-issue journey, or a hybrid of the two — which lets agencies, P&C agents, financial advisors, worksite and affinity channels and embedded fintech partners offer life insurance inside their own customer journeys. Afficiency states it is SOC 2 Type II certified. Its REST API suite is marketed publicly, but the reference and any machine-readable contract are reachable only through the customer
  support portal or a sales conversation.
image: https://www.afficiency.com/images/logos/globalLogo.svg
layout: provider
modified: '2026-09-12'
name: Afficiency
nav: Providers
network: true
overview: 'Afficiency is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Life Insurance, Insurtech, and Embedded Insurance.


  Afficiency''s developer surface includes support, FAQ, product news, and 16 more developer resources.'
plans:
- name: Afficiency Plans Pricing
  plan_count: 0
  slug: afficiency-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Afficiency Rate Limits
  slug: afficiency-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afficiency Domain Security
  slug: afficiency-domain-security
  summary_line: TLSv1.3 · DMARC
slug: afficiency
tags:
- Company
- Insurance
- Life Insurance
- Insurtech
- Embedded Insurance
- Underwriting
- Financial-Services
- Policy Administration
website: https://www.afficiency.com/
---
