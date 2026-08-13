---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Keybase public HTTP JSON API (v1.0). Read-oriented endpoints for user lookup and discovery by social proof, PGP public-key fetch, Merkle-tree root and block retrieval for verification, and the salt/lo
  name: Keybase API
  slug: keybase-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://keybase.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://keybase.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://keybase.io/docs/api/1.0
- group: company
  title: ''
  type: Blog
  url: https://keybase.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keybase
- group: operate
  title: ''
  type: Support
  url: https://keybase.io/docs/bug_reporting
- group: auth
  title: ''
  type: Security
  url: https://keybase.io/docs/secadv
- group: build
  title: ''
  type: Packages
  url: packages/keybase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keybase-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/keybase-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keybase-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keybase-domain-security.yml
created: '2026-07-17'
description: Keybase is an end-to-end encrypted messaging, file-sharing, and key-directory platform built on public-key cryptography, founded by Chris Coyne and Max Krohn and acquired by Zoom in 2020. It maps human-readable usernames to public keys and cryptographically verifiable social-identity proofs (Twitter, GitHub, Reddit, Hacker News, personal domains, and cryptocurrency addresses), and provides encrypted chat, teams, KBFS encrypted filesystem, git, and a wallet. Keybase exposes a public read-oriented HTTP JSON API (version 1.0) at keybase.io/_/api/1.0 for user lookup, PGP key fetch, Merkle-tree verification, and session/signature auth, plus officially supported chat-bot SDKs for Node.js, Python, and Go that script the local keybase client and CLI.
image: https://keybase.io/images/icons/icon-keybase-logo-48.png
layout: provider
mcp_servers:
- description: ''
  name: keybase-mcp.yml
  slug: keybase-mcpyml
modified: '2026-07-20'
name: Keybase
nav: Providers
network: true
overview: 'Keybase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Encryption, Cryptography, and Identity.


  Keybase''s developer surface includes documentation, API reference, engineering blog, support, CLI, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 18.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keybase/refs/heads/main/screenshots/keybase-2026-07-25T223641.png
security:
- kind: authentication
  name: Keybase Authentication
  slug: keybase-authentication
  summary_line: session-token/signature-based · 2 schemes
- kind: domain-security
  name: Keybase Domain Security
  slug: keybase-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: keybase
tags:
- Company
- Security
- Encryption
- Cryptography
- Identity
- Messaging
- Key Management
- PGP
- Developer Tools
website: https://keybase.io/docs
---
