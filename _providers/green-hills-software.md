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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/green-hills-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ghs.com/
- group: other
  title: ''
  type: Products
  url: https://www.ghs.com/products.html
- group: operate
  title: ''
  type: Support
  url: https://support.ghs.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ghs.com/news/index.html
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ghs.com/news/news_feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ghs.com/policies/privacy_policy.html
- group: operate
  title: ''
  type: Contact
  url: https://www.ghs.com/contact/index.html
- group: learn
  title: ''
  type: Training
  url: https://www.ghs.com/training.html
- group: company
  title: ''
  type: Partners
  url: https://www.ghs.com/partners/index.html
- group: company
  title: ''
  type: About
  url: https://www.ghs.com/corporate/index.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/green-hills-software/
- group: commercial
  title: ''
  type: Plans
  url: plans/green-hills-software-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/green-hills-software-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/green-hills-software-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/green-hills-software-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/green-hills-software-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Green Hills Software ships an embedded RTOS and compiler toolchain as licensed end-user products and runs no developer program at all - no API host, no developer portal, no SDK in any public registry, and its only technical documentation surface (support.ghs.com) 302s every FAQ, application-note and download path to an email-link login.
  evidence:
  - status: 404
    url: https://www.ghs.com/openapi.json
  - status: 404
    url: https://www.ghs.com/.well-known/api-catalog
  - status: 302
    url: https://support.ghs.com/faq/
  - status: 404
    url: https://www.ghs.com/pricing.html
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'Green Hills Software is a privately held embedded software company founded in 1982 by Dan O''Dowd and Carl Rosenberg and headquartered in Santa Barbara, California. It builds safety- and security-certified real-time operating systems (INTEGRITY, INTEGRITY-178 tuMP, u-velOSity), embedded hypervisors (INTEGRITY Multivisor, u-visor), optimizing C/C++/Ada/Fortran compilers, the MULTI and AdaMULTI integrated development environments, the TimeMachine back-in-time debug suite, the DoubleCheck static analyzer, the Green Hills Probe hardware debugger, and networking, file-system and USB middleware. Its customers ship these components inside aerospace, defense, automotive, medical, industrial, rail, telecommunications and consumer devices. Green Hills is a toolchain and operating-system vendor rather than an API provider: the programmable interfaces it ships are in-product C/C++, POSIX and MULTI-Python scripting APIs delivered with a licensed installation and documented in manuals distributed
  with the product, and its technical support portal at support.ghs.com requires an account. No public web API, developer portal, or machine-readable API description was found on any Green Hills host during enrichment.'
image: https://www.ghs.com/images/logos/ghs_logo_hires2.png
layout: provider
modified: '2026-08-22'
name: Green Hills Software
nav: Providers
network: true
overview: 'Green Hills Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Embedded Systems, Real-Time Operating Systems, RTOS, and Compilers.


  Green Hills Software''s developer surface includes support, engineering blog, training material, and 14 more developer resources.'
plans:
- name: Green Hills Software Plans Pricing
  plan_count: 0
  slug: green-hills-software-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Green Hills Software Rate Limits
  slug: green-hills-software-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.0
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/green-hills-software/refs/heads/main/screenshots/green-hills-software-2026-09-02T145630.png
security:
- kind: domain-security
  name: Green Hills Software Domain Security
  slug: green-hills-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: green-hills-software
tags:
- Company
- Embedded Systems
- Real-Time Operating Systems
- RTOS
- Compilers
- Developer Tools
- Debugging
- Virtualization
- Safety Critical
- Automotive
- Aerospace and Defense
- Cybersecurity
website: https://www.ghs.com/
---
