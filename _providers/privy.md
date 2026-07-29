---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Privy Agentic Access
  operation_count: 3
  slug: privy-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 5
apis:
- description: REST API for managing users, wallets, sessions, transactions, and policies. Endpoints include /v1/users, /v1/wallets, wallet RPC, signing, and transaction sending across EVM and Solana.
  name: Privy REST API
  slug: rest-api
- description: JSON-RPC method passthrough for signing transactions and arbitrary RPC calls against Privy-managed wallets.
  name: Privy Wallets RPC
  slug: wallets-rpc
- description: Webhook delivery of user, wallet, and transaction events. Subscriptions managed via the dashboard and REST API.
  name: Privy Webhooks
  slug: webhooks
- description: Manage users and their linked accounts.
  name: Privy Users API
  slug: privy-users-api
- description: Create and operate Privy-managed wallets.
  name: Privy Wallets API
  slug: privy-wallets-api
artifact_total: 13
collections:
- collection_type: open
  name: Privy REST API
  slug: open-privy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/privy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/privy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/privy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/privy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/privy-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/privyio
- group: company
  title: ''
  type: Website
  url: https://www.privy.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/privy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/privy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/privy-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.privy.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://privy.io/blog
created: '2026-05-08'
description: Privy is a wallet and authentication platform for Web3 apps offering embedded wallets, server wallets, and progressive authentication. Provides client SDKs (React, React Native, Swift, Android, Unity, Node, Go, Python) plus a public REST API for wallet, user, and transaction operations.
finops:
- name: Privy Finops
  service_category: Web3
  slug: privy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/privy.png
layout: provider
modified: '2026-05-08'
name: Privy
nav: Providers
network: true
overview: 'Privy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Users API and Wallets API. Tagged areas include Web3, Wallets, Authentication, Embedded Wallets, and MPC.


  Privy''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Privy Plans Pricing
  plan_count: 3
  slug: privy-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Privy Rate Limits
  slug: privy-rate-limits
score:
  band: thin
  composite: 36.8
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/privy/refs/heads/main/screenshots/privy-2026-06-20T192122.png
security:
- kind: authentication
  name: Privy Authentication
  slug: privy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Privy Domain Security
  slug: privy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Privy Vulnerability Disclosure
  slug: privy-vulnerability-disclosure
  summary_line: disclosure policy published
slug: privy
tags:
- Web3
- Wallets
- Authentication
- Embedded Wallets
- MPC
website: https://www.privy.io/
---
