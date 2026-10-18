---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: IMDb provides a GraphQL‑backed API via AWS Data Exchange for ratings, analytics, and metadata.
  name: IMDb Data API
  slug: imdb-data-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/changelog/imdb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/imdb-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/conventions/imdb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/imdb-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/authentication/imdb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/imdb-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/llms/imdb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/imdb-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/hosts/imdb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/imdb-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/vendors/imdb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/imdb-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/packages/imdb-packages.yml
  title: ''
  type: SDKs
  url: packages/imdb-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/packages/imdb-packages.yml
  title: ''
  type: Packages
  url: packages/imdb-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.imdb.com/contact/developer/?ref_=devsite_header
- group: operate
  title: ''
  type: ChangeLog
  url: https://data.imdb.com/documentation/release-notes/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/imdb/refs/heads/main/security/imdb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.imdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://data.imdb.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://data.imdb.com/documentation/api-documentation/
- group: operate
  title: ''
  type: Support
  url: https://help.imdb.com/contact/developer/
- group: company
  title: ''
  type: Blog
  url: https://pages.awscloud.com/adx-webinar-dex-ux-staytrendy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imdb.com/conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imdb.com/privacy
coverage:
  checked: '2026-10-13'
  detail: API documentation is rendered via a JavaScript single‑page app with no machine‑readable OpenAPI, GraphQL or other contract available.
  evidence:
  - status: 200
    url: https://data.imdb.com/documentation/api-documentation/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: IMDb provides a premier source of global entertainment metadata, including over 12 million titles, 16 million cast and crew entries, and extensive box office data. The new GraphQL‑backed API, available via AWS Data Exchange, offers on‑demand access to ratings, analytics, and detailed metadata for developers building entertainment‑focused applications.
layout: provider
modified: '2026-10-13'
name: IMDb
nav: Providers
network: true
overview: 'IMDb is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Data, Movies, and Metadata.


  IMDb''s developer surface includes changelog, authentication, documentation, API reference, support, engineering blog, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.8
    discoverability: 60.7
    operational_transparency: 15.8
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Imdb Authentication
  slug: imdb-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Imdb Domain Security
  slug: imdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: imdb
tags:
- Company
- Entertainment
- Data
- Movies
- Metadata
website: https://developer.imdb.com
---
