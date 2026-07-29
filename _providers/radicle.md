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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Repository issues (collaborative objects)
  name: Radicle Issues API
  slug: radicle-issues-api
- description: Node identity, configuration and peers
  name: Radicle Node API
  slug: radicle-node-api
- description: Repository patches (change proposals)
  name: Radicle Patches API
  slug: radicle-patches-api
- description: Radicle repositories seeded by the node
  name: Radicle Repositories API
  slug: radicle-repositories-api
- description: API root and service metadata
  name: Radicle Service API
  slug: radicle-service-api
- description: Commits, trees, blobs and READMEs
  name: Radicle Source API
  slug: radicle-source-api
- description: Aggregate node statistics
  name: Radicle Stats API
  slug: radicle-stats-api
artifact_total: 11
common:
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
  title: ''
  type: APIReference
  url: openapi/radicle-httpd-openapi.yml
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
  title: ''
  type: SDKs
  url: packages/radicle-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/radicle-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/radicle-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/radicle-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/radicle-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/radicle-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/radicle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/radicle-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/radicle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://radicle.dev/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radicle-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/radicle-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/radicle-mcp.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://radicle.dev/legal
created: '2026-07-17'
description: 'Radicle is a sovereign, peer-to-peer code collaboration stack built on Git, developed by Radicle (radicle.dev) and backed by Electric Capital. Instead of relying on a central host, every user runs their own node, and repositories, issues and patches replicate across the network as cryptographically-signed Collaborative Objects (COBs). The stack ships the `rad` command-line tooling, the Heartwood protocol and node, a terminal UI, a desktop app, and a web explorer. Each node can run `radicle-httpd`, a lightweight HTTP daemon that exposes a read-oriented JSON API over the node''s storage — repositories, issues, patches, commits, source trees, node info and network statistics — which powers the Radicle web explorer and third-party tooling. Identity is key-based (DIDs / did:key), so there are no accounts, passwords or platform lock-in. This profile was enriched from Radicle''s public surface: the live seed node API, the security.txt, the Heartwood source, and the CLI manuals.'
image: https://radicle.dev/assets/images/radicle.svg
layout: provider
mcp_servers:
- description: ''
  name: radicle-mcp.yml
  slug: radicle-mcpyml
modified: '2026-07-20'
name: Radicle
nav: Providers
network: true
overview: 'Radicle publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Issues API, Node API, Patches API, and 4 more. Tagged areas include Company, Developer Tools, Code Collaboration, Git, and Peer-to-Peer.


  Radicle''s developer surface includes documentation, getting-started guide, API reference, engineering blog, FAQ, support, CLI, and 19 more developer resources.'
random_paper: 76
score:
  band: developing
  composite: 43.2
  delta: -1.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.1
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 44.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
slug: radicle
tags:
- Company
- Developer Tools
- Code Collaboration
- Git
- Peer-to-Peer
- Version Control
- Open Source
- Decentralized
- Developer Tools API
website: https://radicle.dev/
---
