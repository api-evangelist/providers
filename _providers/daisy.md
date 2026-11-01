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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/daisy/well-known/daisy-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daisy-www-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.linehub.com/coordinated-vulnerability-disclosure/
- group: agent
  href: https://artifacts.apis.io/daisy/llms/daisy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daisy-llms.txt
- group: auth
  href: https://artifacts.apis.io/daisy/well-known/daisy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daisy-security.txt
- group: agent
  href: https://artifacts.apis.io/daisy/well-known/daisy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daisy-well-known.yml
- group: other
  href: https://artifacts.apis.io/daisy/hosts/daisy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daisy-hosts.yml
- group: other
  href: https://artifacts.apis.io/daisy/vendors/daisy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daisy-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://login.daisycon.com/en/register/
- group: company
  title: ''
  type: Newsroom
  url: https://daisycon.com/en/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://daisycon.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://daisycon.com/en/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.daisycon.com/
- group: auth
  href: https://artifacts.apis.io/daisy/security/daisy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/daisy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/daisy/security/daisy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daisy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daisycon.com/
coverage:
  checked: '2026-10-22'
  detail: The API documentation is served as HTML pages rendered by JavaScript with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://daisycon.com/en/developers/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Daisycon is a performance‑based marketing platform offering affiliate, lead‑generation and product‑feed solutions across Europe. It connects advertisers with publishers through a robust API suite that provides access to campaigns, tracking, reporting and data feeds. The company emphasizes transparent revenue sharing and real‑time analytics for partners.
image: https://daisycon.com/wp-content/uploads/2025/12/20251204_1120_Transparent-Rocket-Design_remix_01kbmdyfmtfvsvcwhg63nv2m6d-1.png
layout: provider
modified: '2026-10-22'
name: Daisy
nav: Providers
network: true
overview: 'Daisy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliates, Marketing, Performance, and Europe.


  Daisy''s developer surface includes signup flow, engineering blog, documentation, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 41.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Daisy Domain Security
  slug: daisy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Daisy Vulnerability Disclosure
  slug: daisy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: daisy
tags:
- Affiliates
- Marketing
- Performance
- Europe
website: https://daisycon.com/
---
