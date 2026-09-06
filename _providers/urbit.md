---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.4
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The HTTP interface of every Urbit ship, served by the Eyre kernel vane. Clients authenticate by POSTing the ship's web login code to /~/login for an urbauth session cookie, then interact through chann
  name: Urbit Ship HTTP API (Eyre)
  slug: urbit-ship-http-api-eyre
- description: The HTTP RPC-API of Azimuth's Layer 2 naive rollup roller, primarily intended for interacting with Bridge. Tlon operates the default public roller at roller.urbit.org, which batches Urbit ID transacti
  name: Azimuth Layer 2 Roller HTTP RPC-API
  slug: azimuth-layer-2-roller-http-rpc-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urbit.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.urbit.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urbit.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.urbit.org/urbit-os/kernel/eyre/external-api-ref
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.urbit.org/get-on-urbit
- group: operate
  title: ''
  type: Support
  url: https://urbit.org/overview/running-urbit/support
- group: company
  title: ''
  type: Blog
  url: https://urbit.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urbit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbit.org/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbit.org/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urbit-llms.txt
- group: other
  title: ''
  type: AgentsMd
  url: https://urbit.org/agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urbit-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/urbit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/urbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/urbit-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/urbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/urbit-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urbit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/urbit-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/urbit-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/urbit-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/urbit-cli.yml
created: '2026-07-17'
description: 'Urbit is an open-source personal server platform combining Urbit ID — a self-sovereign, Ethereum-anchored identity system (Azimuth) — with Urbit OS, a deterministic operating system built on the Nock virtual machine and the Hoon language. Every user runs their own ship, a self-hosted server whose Eyre HTTP vane exposes the platform''s API surface: cookie-authenticated channels (JSON actions in, Server-Sent Events out), read-only scries, and threads, with first-party JavaScript clients published under the @urbit npm scope. The project is notably agent-native: urbit.org publishes a canonical llms.txt, machine-oriented markdown mirrors, public Agent Skills, and a documented MCP path for driving ships from LLM clients. Originally bootstrapped by Tlon and backed by investors including Pantera Capital, the network''s identity layer trades as ERC-721 NFTs with a Layer 2 naive rollup (roller.urbit.org) that eliminates gas costs.'
image: https://s3.us-east-1.amazonaws.com/urbit.orgcontent/Social+Cards/Urbit+Home_Social+Card.png
layout: provider
mcp_servers:
- description: Urbit MCP (%mcp) is a general-purpose Model Context Protocol interface for Urbit, documented in urbit.org's first-party public agent-skill snapshot (/.agents/skills/using-urbit-apps/references/urbit-m
  name: Urbit MCP Server
  slug: urbit-mcp-server
modified: '2026-07-21'
name: Urbit
nav: Providers
network: true
overview: 'Urbit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Personal Servers, Decentralized Identity, and Peer-to-Peer.


  Urbit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 19 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 31.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urbit/refs/heads/main/screenshots/urbit-2026-09-02T165214.png
security:
- kind: authentication
  name: Urbit Authentication
  slug: urbit-authentication
  summary_line: cookie-session · 2 schemes
- kind: domain-security
  name: Urbit Domain Security
  slug: urbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urbit
tags:
- Company
- Crypto
- Personal Servers
- Decentralized Identity
- Peer-to-Peer
- Operating Systems
- Self-Hosting
- Agents
website: https://urbit.org/
---
