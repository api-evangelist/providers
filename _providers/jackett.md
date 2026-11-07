---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Jackett API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Jackett API
  slug: jackett-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/jackett/overlays/jackett-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jackett-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/jackett/well-known/jackett-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jackett-security.txt
- group: design
  href: https://artifacts.apis.io/jackett/rules/jackett-rules.yml
  title: ''
  type: Spectral
  url: rules/jackett-rules.yml
- group: design
  href: https://artifacts.apis.io/jackett/vocabulary/jackett-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jackett-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/jackett/authentication/jackett-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jackett-authentication.yml
- group: design
  href: https://artifacts.apis.io/jackett/conformance/jackett-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jackett-conformance.yml
- group: auth
  href: https://artifacts.apis.io/jackett/well-known/jackett-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jackett-www-security.txt
- group: auth
  href: https://artifacts.apis.io/jackett/well-known/jackett-linuxserver-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jackett-linuxserver-security.txt
- group: agent
  href: https://artifacts.apis.io/jackett/well-known/jackett-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jackett-well-known.yml
- group: other
  href: https://artifacts.apis.io/jackett/hosts/jackett-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jackett-hosts.yml
- group: other
  href: https://artifacts.apis.io/jackett/vendors/jackett-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jackett-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.linuxserver.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linuxserver
- group: company
  title: ''
  type: Blog
  url: https://www.linuxserver.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linuxserver.io/selkies/user-guide/quickstart/
- group: auth
  href: https://artifacts.apis.io/jackett/security/jackett-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jackett-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.linuxserver.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Jackett/Jackett/wiki
- group: operate
  title: ''
  type: Support
  url: https://github.com/Jackett/Jackett/issues
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Jackett/Jackett
created: '2026-10-28'
description: Jackett provides a proxy server that translates queries from various torrent clients into a unified API, allowing users to search and retrieve torrent tracker results across many sources. It supports a wide range of trackers, offers configuration options, and can be self‑hosted via Docker or native installations on Windows, Linux, and macOS. The project is open‑source and maintained on GitHub, with active community contributions and documentation covering installation, usage, and API endpoints.
layout: provider
modified: '2026-10-28'
name: Jackett
nav: Providers
network: true
overview: 'Jackett is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, Torrent, and Proxy.


  The Jackett catalog on APIs.io includes 1 Spectral governance ruleset.


  Jackett''s developer surface includes authentication, engineering blog, getting-started guide, documentation, support, and 15 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Jackett API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: jackett-rules
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 84.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 21.1
  previous_composite: 22.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jackett/jackett-2026-11-03T134112.png
security:
- kind: authentication
  name: Jackett Authentication
  slug: jackett-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jackett Domain Security
  slug: jackett-domain-security
  summary_line: TLSv1.3
slug: jackett
tags:
- Company
- Open Source
- Torrent
- Proxy
website: https://www.linuxserver.io/
---
