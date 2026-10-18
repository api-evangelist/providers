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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Public API for SVT content (not publicly documented)
  name: SVT API
  slug: svt-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/security/svt-se-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/svt-se-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/well-known/svt-se-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/svt-se-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/well-known/svt-se-omoss-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/svt-se-omoss-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/well-known/svt-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/svt-se-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/hosts/svt-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/svt-se-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/packages/svt-se-packages.yml
  title: ''
  type: SDKs
  url: packages/svt-se-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/packages/svt-se-packages.yml
  title: ''
  type: Packages
  url: packages/svt-se-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/svt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/security/svt-se-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/svt-se-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svt-se/refs/heads/main/security/svt-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/svt-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://svt.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://svt.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Sveriges Television (SVT) is Sweden's public service television company, providing news, sports, culture, and entertainment across multiple channels and digital platforms. The organization operates a comprehensive online presence at svt.se, offering up-to-date news articles, video streaming, regional coverage, and specialized sections such as SVT Play and SVT Barn. As a major media outlet, SVT delivers content in Swedish and serves a broad audience with a commitment to public service broadcasting.
image: https://www.svtstatic.se/image-news/1200/1.91:1/0.5/0.5/2f93ba843f7e400a13c86112e65490896499522866cbeab7a04aa887efed39b6
layout: provider
modified: '2026-10-15'
name: SVT
nav: Providers
network: true
overview: SVT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Public Service, Television, Sweden, and News.
random_paper: 16
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Svt Se Domain Security
  slug: svt-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Svt Se Vulnerability Disclosure
  slug: svt-se-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: svt-se
tags:
- Media
- Public Service
- Television
- Sweden
- News
website: https://svt.se/
---
