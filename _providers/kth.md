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
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Template API project for Node.js
  name: Node API
  slug: node-api
- baseURL: https://kth.se/api/node
  baseurl_source: declared
  description: The data API from KTH Royal Institute of Technology — 1 operation(s) for data.
  name: KTH Royal Institute of Technology Data API
  slug: kth-data-api
- baseURL: https://kth.se/api/node
  baseurl_source: declared
  description: The system API from KTH Royal Institute of Technology — 1 operation(s) for system.
  name: KTH Royal Institute of Technology System API
  slug: kth-system-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/kth/rules/kth-rules.yml
  title: ''
  type: Spectral
  url: rules/kth-rules.yml
- group: design
  href: https://artifacts.apis.io/kth/data-model/kth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kth-data-model.yml
- group: design
  href: https://artifacts.apis.io/kth/errors/kth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kth-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/kth/well-known/kth-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kth-www-security.txt
- group: auth
  href: https://artifacts.apis.io/kth/security/kth-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kth-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/kth/conformance/kth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kth-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kth/well-known/kth-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kth-security.txt
- group: auth
  href: https://artifacts.apis.io/kth/well-known/kth-intra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kth-intra-security.txt
- group: agent
  href: https://artifacts.apis.io/kth/well-known/kth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kth-well-known.yml
- group: other
  href: https://artifacts.apis.io/kth/hosts/kth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kth-hosts.yml
- group: build
  href: https://artifacts.apis.io/kth/packages/kth-packages.yml
  title: ''
  type: SDKs
  url: packages/kth-packages.yml
- group: build
  href: https://artifacts.apis.io/kth/packages/kth-packages.yml
  title: ''
  type: Packages
  url: packages/kth-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.kth.se/om/kontakt/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KTH
- group: auth
  href: https://artifacts.apis.io/kth/security/kth-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kth-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kth/security/kth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kth.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://webmail.kth.se/api/mcp
  - status: 200
    url: https://kth.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: KTH Royal Institute of Technology (KTH) is Sweden's largest technical university, located in Stockholm. It offers a broad range of engineering and technology education, conducts cutting‑edge research, and collaborates with industry and international partners. KTH provides various digital services and APIs for students, researchers, and partners, supporting open data, learning platforms, and research infrastructure. The university is committed to sustainability, innovation, and societal impact through its extensive academic and research programs.
image: https://intra.kth.se/polopoly_fs/1.858858!/image/KTH_Logotyp_RGB_2013.png
layout: provider
modified: '2026-10-15'
name: KTH Royal Institute of Technology
nav: Providers
network: true
overview: 'KTH Royal Institute of Technology publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, System API, and 1 more. Tagged areas include Company, Education, Research, Sweden, and Technology.


  The KTH Royal Institute of Technology catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: KTH Royal Institute of Technology API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: kth-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 44.1
    developer_ergonomics: 7.1
    discoverability: 67.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 23.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kth/kth-2026-11-03T134540.png
security:
- kind: domain-security
  name: Kth Domain Security
  slug: kth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kth Vulnerability Disclosure
  slug: kth-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kth
tags:
- Company
- Education
- Research
- Sweden
- Technology
website: https://kth.se/
---
