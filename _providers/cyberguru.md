---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cyberguru provides cybersecurity awareness and training platform APIs as documented on their developer site.
  name: Cyberguru API
  slug: cyberguru-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cyberguru/hosts/cyberguru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyberguru-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyberguru/vendors/cyberguru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyberguru-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cyberguru/security/cyberguru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyberguru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cyberguru.it/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cyberguru.it/en/
- group: docs
  title: ''
  type: APIReference
  url: https://www.cyberguru.it/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cyberguru.it/en/how-to-buy/
- group: operate
  title: ''
  type: Support
  url: https://support.cyberguru.eu/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cyberguru.it/en/cyber-blog-cyber-guru-solutions-for-security-awareness/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyberguru.it/en/privacy-cookie-policy/
- group: company
  title: ''
  type: Website
  url: https://www.cyberguru.it
- group: docs
  title: ''
  type: Documentation
  url: https://www.cyberguru.it/chi-siamo-cyber-guru-company/
- group: company
  title: ''
  type: Blog
  url: https://www.cyberguru.it/cyber-blog/
coverage:
  checked: '2026-10-22'
  detail: Main website renders content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.cyberguru.it/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Cyberguru, now operating under the LibraCyber brand, provides comprehensive cybersecurity awareness and training solutions across Europe. Their platform offers phishing simulations, real‑time awareness, compliance training, and a cyber‑advisor service, targeting enterprises seeking to improve security behaviors. The company emphasizes a human‑centric approach and integrates multilingual support, resources, and consulting to help organizations build a safer digital environment.
image: https://www.cyberguru.it/wp-content/uploads/2025/11/pillar-Awareness-1.png
layout: provider
modified: '2026-10-21'
name: Cyberguru
nav: Providers
network: true
overview: 'Cyberguru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Training, Awareness, Europe, and Enterprise.


  Cyberguru''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 14.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cyberguru/cyberguru-2026-11-03T125946.png
security:
- kind: domain-security
  name: Cyberguru Domain Security
  slug: cyberguru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyberguru
tags:
- Cybersecurity
- Training
- Awareness
- Europe
- Enterprise
website: https://www.cyberguru.it/en/
---
