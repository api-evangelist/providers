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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saphlux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saphlux.com/
- group: company
  title: ''
  type: Blog
  url: https://www.saphlux.com/blog-3
- group: company
  title: ''
  type: BlogRSS
  url: https://www.saphlux.com/blog-3?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.saphlux.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saphlux.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saphlux.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/saphlux-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/saphlux-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/saphlux-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Saphlux is a semiconductor materials and display-module manufacturer — it sells semi-polar (20-21) GaN-on-sapphire epitaxial wafers and NPQD quantum-dot Micro-LED panels to display OEMs — and its entire public surface is a four-item Squarespace marketing site (Home / Products / Newsroom / Contact) whose 150-URL sitemap contains no developer, docs, or API reference page at all.
  evidence:
  - status: 200
    url: https://www.saphlux.com/sitemap.xml
  - status: 404
    url: https://www.saphlux.com/developers
  - status: 404
    url: https://www.saphlux.com/openapi.json
  - status: 404
    url: https://www.saphlux.com/llms.txt
  - status: 404
    url: https://www.saphlux.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Saphlux is a quantum dot Micro-LED (QD-MLED) display technology company founded in 2014 out of Yale University and headquartered in San Diego, California, with additional operations in China and Japan. It commercialized semi-polar (20-21) GaN-on-sapphire epitaxial wafers to address efficiency droop and the green gap in nitride emitters, and now mass-produces NPQD quantum-dot Micro-LED devices. Its product lineup spans QD-COB and QD-COB Pro Series panels for large-format commercial and home-theater displays and the T-Series monolithic full-color micro-displays for all-day wearable AR eyewear and AI smart glasses. Saphlux is a semiconductor materials and display-module manufacturer that sells hardware to OEMs and display integrators; it publishes no public developer program, API, or SDK.
image: https://static1.squarespace.com/static/60f70a871d58107fff2b086c/t/6511e9a071a8b360ae17c10e/1695672736192/logo.png?format=1500w
layout: provider
modified: '2026-08-26'
name: Saphlux
nav: Providers
network: true
overview: 'Saphlux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Displays, Micro-LED, and Quantum Dots.


  Saphlux''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Saphlux Plans Pricing
  plan_count: 0
  slug: saphlux-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Saphlux Rate Limits
  slug: saphlux-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saphlux/refs/heads/main/screenshots/saphlux-2026-09-02T154408.png
security:
- kind: domain-security
  name: Saphlux Domain Security
  slug: saphlux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saphlux
tags:
- Company
- Semiconductors
- Displays
- Micro-LED
- Quantum Dots
- Hardware
- Augmented Reality
- Optoelectronics
- Manufacturing
website: https://www.saphlux.com/
---
