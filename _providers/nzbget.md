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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/nzbget/hosts/nzbget-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nzbget-hosts.yml
- group: other
  href: https://artifacts.apis.io/nzbget/vendors/nzbget-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nzbget-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nzbget/security/nzbget-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nzbget-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nzbget.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nzbget.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://nzbget.com/documentation/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://nzbget.com/documentation/how-to-set-up-nzbget-quickstart-guide-for-beginners/
- group: operate
  title: ''
  type: Support
  url: https://nzbget.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nzbgetcom
coverage:
  checked: '2026-10-28'
  detail: The NZBGet API reference page lists RPC methods but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://nzbget.com/documentation/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: NZBGet is a fast, reliable, feature‑packed NZB downloader for Usenet that runs on Windows, macOS, Linux, NAS devices and Docker. It offers XML‑RPC, JSON‑RPC and JSON‑P‑RPC interfaces for programmatic control, enabling integration with third‑party tools and scripts.
image: https://nzbget.com/img/logo.svg
layout: provider
modified: '2026-10-28'
name: NZBGet
nav: Providers
network: true
overview: 'NZBGet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Usenet, Downloader, Cross‑platform, RPC, and Open‑source.


  NZBGet''s developer surface includes documentation, API reference, getting-started guide, support, and 5 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nzbget Domain Security
  slug: nzbget-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nzbget
tags:
- Usenet
- Downloader
- Cross‑platform
- RPC
- Open‑source
website: https://nzbget.com/
---
