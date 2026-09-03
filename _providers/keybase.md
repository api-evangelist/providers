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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Keybase public HTTP JSON API (v1.0). Read-oriented endpoints for user lookup and discovery by social proof, PGP public-key fetch, Merkle-tree root and block retrieval for verification, and the salt/lo
  name: Keybase API
  slug: keybase-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/zoom/
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
modified: '2026-07-20'
name: Keybase
nav: Providers
network: true
overview: 'Keybase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Encryption, Cryptography, and Identity.


  Keybase''s developer surface includes documentation, API reference, engineering blog, support, CLI, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 22.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
