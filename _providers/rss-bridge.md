---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: RSS-Bridge provides a web interface that generates RSS/Atom feeds for websites; it does not expose a public machine‑readable API.
  name: RSS-Bridge API
  slug: rss-bridge-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/rss-bridge/cli/rss-bridge-cli.yml
  title: ''
  type: CLI
  url: cli/rss-bridge-cli.yml
- group: auth
  href: https://artifacts.apis.io/rss-bridge/authentication/rss-bridge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rss-bridge-authentication.yml
- group: other
  href: https://artifacts.apis.io/rss-bridge/hosts/rss-bridge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rss-bridge-hosts.yml
- group: other
  href: https://artifacts.apis.io/rss-bridge/vendors/rss-bridge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rss-bridge-vendors.yml
- group: build
  href: https://artifacts.apis.io/rss-bridge/packages/rss-bridge-packages.yml
  title: ''
  type: SDKs
  url: packages/rss-bridge-packages.yml
- group: build
  href: https://artifacts.apis.io/rss-bridge/packages/rss-bridge-packages.yml
  title: ''
  type: Packages
  url: packages/rss-bridge-packages.yml
- group: auth
  href: https://artifacts.apis.io/rss-bridge/security/rss-bridge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rss-bridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rss-bridge.org/
- group: docs
  title: ''
  type: Documentation
  url: https://rss-bridge.github.io/rss-bridge/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rss-bridge.github.io/rss-bridge/
- group: start
  title: ''
  type: GettingStarted
  url: https://rss-bridge.github.io/rss-bridge/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RSS-Bridge
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation site https://rss-bridge.github.io/rss-bridge/ contains only HTML pages and no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://rss-bridge.github.io/rss-bridge/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: RSS-Bridge is an open-source PHP project that provides RSS/Atom feeds for websites that do not natively offer them. By running the bridge on a server, users can generate feeds for a wide variety of sites, including social media, video platforms, news sites, and many niche services. The project ships with hundreds of individual “bridges” that scrape content and expose it as standard RSS, enabling easy aggregation in any feed reader. RSS-Bridge can be self-hosted, customized, and extended, making it a flexible tool for developers and hobbyists who need universal access to web content through RSS.
image: https://rss-bridge.org/logo_600px.png
layout: provider
modified: '2026-10-28'
name: RSS-Bridge
nav: Providers
network: true
overview: 'RSS-Bridge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OpenSource, PHP, RSS, Aggregator, and SelfHosted.


  RSS-Bridge''s developer surface includes CLI, authentication, documentation, getting-started guide, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
- kind: authentication
  name: Rss Bridge Authentication
  slug: rss-bridge-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Rss Bridge Domain Security
  slug: rss-bridge-domain-security
  summary_line: TLSv1.3
slug: rss-bridge
tags:
- OpenSource
- PHP
- RSS
- Aggregator
- SelfHosted
website: https://rss-bridge.org/
---
