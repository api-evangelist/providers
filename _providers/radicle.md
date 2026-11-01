---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: Repository issues (collaborative objects)
  name: Radicle Issues API
  slug: radicle-issues-api
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: Node identity, configuration and peers
  name: Radicle Node API
  slug: radicle-node-api
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: Repository patches (change proposals)
  name: Radicle Patches API
  slug: radicle-patches-api
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: Radicle repositories seeded by the node
  name: Radicle Repositories API
  slug: radicle-repositories-api
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: API root and service metadata
  name: Radicle Service API
  slug: radicle-service-api
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: Commits, trees, blobs and READMEs
  name: Radicle Source API
  slug: radicle-source-api
- baseURL: https://seed.radicle.xyz/api/v1
  baseurl_source: declared
  description: Aggregate node statistics
  name: Radicle Stats API
  slug: radicle-stats-api
artifact_total: 19
collections:
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues API
  slug: open-radicle-issues-api
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues Node API
  slug: open-radicle-node-api
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues Patches API
  slug: open-radicle-patches-api
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues Repositories API
  slug: open-radicle-repositories-api
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues Service API
  slug: open-radicle-service-api
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues Source API
  slug: open-radicle-source-api
- collection_type: open
  name: Radicle HTTP API (radicle-httpd) Issues Stats API
  slug: open-radicle-stats-api
common:
- group: other
  href: https://artifacts.apis.io/radicle/capabilities/radicle-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/radicle-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/radicle/overlays/radicle-httpd-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/radicle-httpd-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://radicle.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://radicle.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://radicle.dev/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://radicle.dev/guides/quick-start/
- group: docs
  href: https://artifacts.apis.io/radicle/openapi/_original/radicle-httpd-openapi.yml
  title: ''
  type: APIReference
  url: openapi/_original/radicle-httpd-openapi.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radicle-dev
- group: company
  title: ''
  type: Blog
  url: https://radicle.dev/#updates
- group: company
  title: ''
  type: BlogRSS
  url: https://radicle.dev/feed.xml
- group: other
  title: ''
  type: Download
  url: https://radicle.dev/download
- group: operate
  title: ''
  type: FAQ
  url: https://radicle.dev/faq
- group: operate
  title: ''
  type: Support
  url: https://radicle.zulipchat.com
- group: build
  href: https://artifacts.apis.io/radicle/packages/radicle-packages.yml
  title: ''
  type: SDKs
  url: packages/radicle-packages.yml
- group: build
  href: https://artifacts.apis.io/radicle/packages/radicle-packages.yml
  title: ''
  type: Packages
  url: packages/radicle-packages.yml
- group: build
  href: https://artifacts.apis.io/radicle/cli/radicle-cli.yml
  title: ''
  type: CLI
  url: cli/radicle-cli.yml
- group: operate
  href: https://artifacts.apis.io/radicle/changelog/radicle-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/radicle-changelog.yml
- group: design
  href: https://artifacts.apis.io/radicle/lifecycle/radicle-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/radicle-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/radicle/authentication/radicle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/radicle-authentication.yml
- group: agent
  href: https://artifacts.apis.io/radicle/well-known/radicle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/radicle-well-known.yml
- group: auth
  href: https://artifacts.apis.io/radicle/well-known/radicle-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/radicle-security.txt
- group: auth
  href: https://artifacts.apis.io/radicle/security/radicle-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/radicle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://radicle.dev/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/radicle/security/radicle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/radicle-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/radicle/llms/radicle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/radicle-llms.txt
- group: agent
  href: https://artifacts.apis.io/radicle/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/radicle/mcp/radicle-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/radicle-mcp.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://radicle.dev/legal
created: '2026-07-17'
description: 'Radicle is a sovereign, peer-to-peer code collaboration stack built on Git, developed by Radicle (radicle.dev) and backed by Electric Capital. Instead of relying on a central host, every user runs their own node, and repositories, issues and patches replicate across the network as cryptographically-signed Collaborative Objects (COBs). The stack ships the `rad` command-line tooling, the Heartwood protocol and node, a terminal UI, a desktop app, and a web explorer. Each node can run `radicle-httpd`, a lightweight HTTP daemon that exposes a read-oriented JSON API over the node''s storage — repositories, issues, patches, commits, source trees, node info and network statistics — which powers the Radicle web explorer and third-party tooling. Identity is key-based (DIDs / did:key), so there are no accounts, passwords or platform lock-in. This profile was enriched from Radicle''s public surface: the live seed node API, the security.txt, the Heartwood source, and the CLI manuals.'
image: https://radicle.dev/assets/images/radicle.svg
layout: provider
modified: '2026-07-20'
name: Radicle
nav: Providers
network: true
overview: 'Radicle publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Issues API, Node API, Patches API, and 4 more. Tagged areas include Company, Developer Tools, Code Collaboration, Version Control, and Peer-to-Peer.


  Radicle''s developer surface includes documentation, getting-started guide, API reference, engineering blog, FAQ, support, CLI, and 21 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 40.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/radicle/radicle-2026-08-17T081437.png
security:
- kind: authentication
  name: Radicle Authentication
  slug: radicle-authentication
  summary_line: none/session · 2 schemes
- kind: domain-security
  name: Radicle Domain Security
  slug: radicle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Radicle Vulnerability Disclosure
  slug: radicle-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: Browse a Radicle repository
  slug: radicle-browse-repository
- name: Read Radicle source code
  slug: radicle-read-source-tree
slug: radicle
tags:
- Company
- Developer Tools
- Code Collaboration
- Version Control
- Peer-to-Peer
- Open Source
- Decentralized
- Developer Tools API
website: https://radicle.dev/
---
