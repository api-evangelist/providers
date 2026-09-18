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
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aidaly/refs/heads/main/security/aidaly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidaly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aidaly.com/
- group: company
  title: ''
  type: About
  url: https://aidaly.com/company
- group: company
  title: ''
  type: Blog
  url: https://aidaly.com/learning-studio
- group: operate
  title: ''
  type: HelpCenter
  url: https://aidaly.com/frequently-asked-questions
- group: start
  title: ''
  type: SignUp
  url: https://aidaly.com/check-my-eligibility
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidaly.com/service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidaly.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://aidaly.com/press
- group: company
  title: ''
  type: Careers
  url: https://aidaly.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aidaly
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aidaly/refs/heads/main/conformance/aidaly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidaly-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aidaly/refs/heads/main/conformance/aidaly-conformance.yml
  title: ''
  type: Compliance
  url: conformance/aidaly-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aidaly/refs/heads/main/plans/aidaly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidaly-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aidaly/refs/heads/main/rate-limits/aidaly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aidaly-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aidaly/refs/heads/main/llms/aidaly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidaly-llms.txt
coverage:
  checked: '2026-09-14'
  detail: 'Aidaly ships software only as an end-user product — a caregiver mobile app and the credentialed AidalyHQ web console at aidaly.com/hq, where access is requested by emailing operators@aidaly.com — and publishes no developer surface at all: www.aidaly.com has no /developers, /api or /docs path, api.aidaly.com, docs.aidaly.com and developer.aidaly.com do not resolve in DNS, app.aidaly.com 301s its root to the marketing site and 404s every spec path, there is no Aidaly GitHub organization, and no package exists on npm, PyPI, RubyGems, crates.io or Packagist.'
  evidence:
  - status: 404
    url: https://www.aidaly.com/developers
  - status: 404
    url: https://www.aidaly.com/openapi.json
  - status: 404
    url: https://app.aidaly.com/openapi.json
  - status: 404
    url: https://app.aidaly.com/graphql
  - status: 404
    url: https://www.aidaly.com/.well-known/api-catalog
  - status: 404
    url: https://www.aidaly.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/aidaly
  - status: 200
    url: https://www.aidaly.com/
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: Aidaly is a Miami, Florida home care company, founded in 2021 by CEO Margaret "Maggie" Norris, that trains, employs and pays family members as professional caregivers so households can draw on Medicaid, Medicare and private benefit dollars for care they were already giving unpaid. It runs a software-enabled care agency on its own aidalyOS platform - Aidaly Care, a caregiver mobile app with insurance-required electronic visit verification, care plans, visit notes and pay tracking; AidalyHQ, a credentialed console for supervising nurses; a Learning Studio training library; and a care-team nurse network. It operates in South Florida, Arizona and Michigan with Colorado and Massachusetts announced, is contracted into payer networks including Molina Healthcare and Meridian, displays Vanta-attested SOC 2 and HIPAA badges, and raised $8.5M led by Seven Seven Six. Aidaly publishes no public developer program, API documentation, SDK or machine-readable contract.
image: https://cdn.prod.website-files.com/618bf584fe2970faf482ca6f/618e89f9306762893fa79fd7_OG-Image.png
layout: provider
modified: '2026-09-14'
name: Aidaly
nav: Providers
network: true
overview: 'Aidaly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Home Care, Caregiving, Medicaid, and Health Tech.


  Aidaly''s developer surface includes engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Aidaly Plans Pricing
  plan_count: 0
  slug: aidaly-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Aidaly Rate Limits
  slug: aidaly-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aidaly Domain Security
  slug: aidaly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aidaly
tags:
- Healthcare
- Home Care
- Caregiving
- Medicaid
- Health Tech
- Digital Health
- Benefits
- Workforce
- United States
- Company
website: https://www.aidaly.com/
---
