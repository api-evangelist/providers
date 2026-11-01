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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/webstarted/llms/webstarted-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webstarted-llms.txt
- group: other
  href: https://artifacts.apis.io/webstarted/hosts/webstarted-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webstarted-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webstarted.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://webstarted.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://webstarted.com/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webstarted
- group: auth
  href: https://artifacts.apis.io/webstarted/security/webstarted-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webstarted-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webstarted.com/
- group: company
  title: ''
  type: Blog
  url: https://webstarted.com/blog
coverage:
  checked: '2026-10-28'
  detail: No public API contract or developer documentation was found; standard spec endpoints returned 404.
  evidence:
  - status: 404
    url: https://webstarted.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Webstarted is a LATAM‑based staff augmentation and technology recruiting firm founded in 2019. It provides near‑shore engineering talent, sales and marketing professionals, MVP development, and startup advisory services to help startups quickly scale with vetted remote talent. Based in Coral Springs, Florida, the company connects US startups with Latin American engineers.
image: https://webstarted.com/webstarted-logo.svg
layout: provider
modified: '2026-10-28'
name: Webstarted
nav: Providers
network: true
overview: 'Webstarted is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Staff Augmentation, Nearshore, LATAM, Recruiting, and Startup Advisory.


  Webstarted''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Webstarted Plans Pricing
  plan_count: 0
  slug: webstarted-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Webstarted Rate Limits
  slug: webstarted-rate-limits
scopes:
- name: Webstarted Scopes
  scope_count: 0
  slug: webstarted-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Webstarted Authentication
  slug: webstarted-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Webstarted Domain Security
  slug: webstarted-domain-security
  summary_line: TLSv1.3 · DMARC
slug: webstarted
tags:
- Staff Augmentation
- Nearshore
- LATAM
- Recruiting
- Startup Advisory
website: https://webstarted.com/
---
