---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://repo.jellyfin.org
  baseurl_source: declared
  description: 'Jellyfin API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Jellyfin API
  slug: jellyfin-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/jellyfin/rules/jellyfin-rules.yml
  title: ''
  type: Spectral
  url: rules/jellyfin-rules.yml
- group: design
  href: https://artifacts.apis.io/jellyfin/vocabulary/jellyfin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jellyfin-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jellyfin/conformance/jellyfin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jellyfin-conformance.yml
- group: other
  href: https://artifacts.apis.io/jellyfin/hosts/jellyfin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jellyfin-hosts.yml
- group: other
  href: https://artifacts.apis.io/jellyfin/vendors/jellyfin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jellyfin-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://jellyfin.org/posts/tags/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/jellyfin/jellyfin/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://jellyfin.org/docs/general/quick-start
- group: auth
  href: https://artifacts.apis.io/jellyfin/security/jellyfin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jellyfin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jellyfin.org/
- group: docs
  title: ''
  type: Documentation
  url: https://jellyfin.org/docs/
- group: company
  title: ''
  type: Blog
  url: https://jellyfin.org/posts/
- group: operate
  title: ''
  type: Forum
  url: https://forum.jellyfin.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jellyfin
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL spec.
  evidence:
  - status: 200
    url: https://jellyfin.org/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Jellyfin is a free, open-source media system that lets you collect, manage, and stream your media files. It is community‑built, runs on your own server, and offers no‑strings‑attached streaming to any device, with full control over your library and privacy.
image: https://jellyfin.org/images/social.png?v2
layout: provider
modified: '2026-10-28'
name: Jellyfin
nav: Providers
network: true
overview: 'Jellyfin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Open-Source, Free-Software, Community, and Streaming.


  The Jellyfin catalog on APIs.io includes 1 Spectral governance ruleset.


  Jellyfin''s developer surface includes changelog, getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Jellyfin API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: jellyfin-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jellyfin Domain Security
  slug: jellyfin-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: jellyfin
tags:
- Media
- Open-Source
- Free-Software
- Community
- Streaming
- Company
website: https://jellyfin.org/
---
