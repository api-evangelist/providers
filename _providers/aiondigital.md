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
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiondigital/refs/heads/main/security/aiondigital-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiondigital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiondigital.com/
- group: company
  title: ''
  type: About
  url: https://aiondigital.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://aiondigital.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://aiondigital.com/resources/?tab=blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://aiondigital.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiondigital.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiondigital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aiondigital
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiondigital/refs/heads/main/packages/aiondigital-packages.yml
  title: ''
  type: Packages
  url: packages/aiondigital-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiondigital/refs/heads/main/llms/aiondigital-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiondigital-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiondigital/refs/heads/main/plans/aiondigital-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiondigital-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiondigital/refs/heads/main/rate-limits/aiondigital-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiondigital-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiondigital/refs/heads/main/conformance/aiondigital-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiondigital-conformance.yml
coverage:
  checked: '2026-09-14'
  detail: 'Aion Digital markets an API gateway, "API management with API analytics" and — via a 2019 Open Bank Project partnership — a 200+ API catalogue with a sandbox, but publishes no developer route to any of it: every call to action on aiondigital.com and ekyc.aiondigital.com is "Request a demo", and api., apis., developer., developers., docs., portal., sandbox., openbanking., rubix. and app. under aiondigital.com are all NXDOMAIN.'
  evidence:
  - status: 200
    url: https://aiondigital.com/aion-rubix/
  - status: 404
    url: https://aiondigital.com/openapi.json
  - status: 404
    url: https://aiondigital.com/.well-known/api-catalog
  - status: 404
    url: https://aiondigital.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-09-14'
description: 'Aion Digital is a Bahrain-headquartered digital banking platform vendor, operated by Waqfe W.L.L and founded in 2017, that sells bank-in-a-box software to financial institutions across the GCC and Pakistan. Its product lines are eKYC and digital onboarding, retail digital banking, corporate digital banking, an AI layer (Aion Hikmah) and the Aion Rubix platform, whose marketed components include an API gateway, an API management and analytics platform, and modular middleware with pre-integrations. Aion Digital markets an API platform and, through a 2019 Open Bank Project partnership, an API catalogue and sandbox delivered to its bank customers, but it publishes no public developer portal, API reference, or machine-readable contract of its own: every developer-facing call to action on aiondigital.com and ekyc.aiondigital.com is "Request a demo". The one public first-party code it does ship is a small set of internal platform libraries on npm and an iOS analytics framework on
  GitHub.'
image: https://aiondigital.com/wp-content/uploads/2022/07/cropped-Artboard-1-192x192.png
layout: provider
modified: '2026-09-14'
name: Aion Digital
nav: Providers
network: true
overview: 'Aion Digital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, Digital Banking, and Fintech.


  Aion Digital''s developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Aiondigital Plans Pricing
  plan_count: 0
  slug: aiondigital-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Aiondigital Rate Limits
  slug: aiondigital-rate-limits
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 8.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.0
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiondigital Domain Security
  slug: aiondigital-domain-security
  summary_line: TLSv1.2 · DMARC
slug: aiondigital
tags:
- Company
- Banking
- Financial-Services
- Digital Banking
- Fintech
- Open Banking
- eKYC
- Identity Verification
- Onboarding
- Artificial Intelligence
- Bahrain
- Middle East
website: https://aiondigital.com/
---
