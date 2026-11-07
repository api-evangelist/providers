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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/confotherapeutics/llms/confotherapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/confotherapeutics-llms.txt
- group: agent
  href: https://artifacts.apis.io/confotherapeutics/well-known/confotherapeutics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/confotherapeutics-well-known.yml
- group: other
  href: https://artifacts.apis.io/confotherapeutics/hosts/confotherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/confotherapeutics-hosts.yml
- group: other
  href: https://artifacts.apis.io/confotherapeutics/vendors/confotherapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/confotherapeutics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.confotherapeutics.com/news/
- group: auth
  href: https://artifacts.apis.io/confotherapeutics/security/confotherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/confotherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.confotherapeutics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.confotherapeutics.com/about/
- group: docs
  title: ''
  type: Documentation
  url: https://www.confotherapeutics.com/pipeline
- group: docs
  title: ''
  type: Documentation
  url: https://www.confotherapeutics.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://www.confotherapeutics.com/investors
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confotherapeutics.com/privacy-statement/
- group: operate
  title: ''
  type: Support
  url: https://www.confotherapeutics.com/contact/
coverage:
  checked: '2026-10-10'
  detail: Main website pages return JavaScript challenges preventing access to documentation.
  evidence:
  - status: 429
    url: https://www.confotherapeutics.com/about/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Confotherapeutics (also styled as Confo Therapeutics) is a clinical‑stage biotechnology company focused on developing novel GPCR‑directed therapeutics for metabolic and endocrine diseases. The company leverages a unique platform to create medicines targeting G‑protein‑coupled receptors, aiming to address unmet medical needs in areas such as obesity, diabetes, and related disorders. It operates from its headquarters in the Netherlands and collaborates with academic and industry partners to advance its pipeline through pre‑clinical and clinical development.
image: https://www.confotherapeutics.com/wp-content/uploads/2025/02/social-share-image-2000x1600-1.jpg
layout: provider
modified: '2026-10-10'
name: Confotherapeutics
nav: Providers
network: true
overview: 'Confotherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, GPCR, Therapeutics, Metabolic Diseases, and Netherlands.


  Confotherapeutics'' developer surface includes documentation, support, and 11 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 56.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 10.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/confotherapeutics/confotherapeutics-2026-11-03T125056.png
security:
- kind: domain-security
  name: Confotherapeutics Domain Security
  slug: confotherapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: confotherapeutics
tags:
- Biotechnology
- GPCR
- Therapeutics
- Metabolic Diseases
- Netherlands
- Company
website: https://www.confotherapeutics.com
---
