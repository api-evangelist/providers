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
api_count: 1
apis:
- description: autumo provides intelligent IT security products and services; API details are not publicly documented.
  name: autumo API
  slug: autumo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/autumo/hosts/autumo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autumo-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://autumo.ch/en/security/supply-chain-threats-demand-proactive-scanning
- group: auth
  href: https://artifacts.apis.io/autumo/security/autumo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autumo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autumo.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://autumo.ch/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://autumo.ch/en/home/about-autumo
- group: operate
  title: ''
  type: Support
  url: https://autumo.ch/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autumo.ch/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autumo.ch/en/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autumoswitzerland
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are publicly available on autumo's domains.
  evidence:
  - status: 200
    url: https://autumo.ch/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: autumo Ltd. is a Swiss technology company focused on sophisticated software, secure IT systems, and intelligent digital solutions. With over 20 years of experience, autumo develops software and technologies for businesses, especially in the financial sector, emphasizing security, privacy, independence, and sustainable technology.
image: https://autumo.ch/images/ogimage.jpg
layout: provider
modified: '2026-10-19'
name: autumo
nav: Providers
network: true
overview: 'autumo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Security, Software, and Finance.


  autumo''s developer surface includes documentation, getting-started guide, support, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autumo Domain Security
  slug: autumo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autumo
tags:
- Company
- Technology
- Security
- Software
- Finance
website: https://autumo.ch/
---
