---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Dfns Agentic Access
  operation_count: 49
  slug: dfns-agentic-access
  summary_line: 49 operations · 26 acting
api_count: 12
apis:
- description: Approval workflow driven by the policy engine.
  name: Dfns Approvals API
  slug: dfns-approvals-api
- description: Login, User Action Signing, users, and credentials.
  name: Dfns Auth API
  slug: dfns-auth-api
- description: Standalone MPC keys and delegated signing.
  name: Dfns Keys API
  slug: dfns-keys-api
- description: Network fee estimates and read-only blockchain calls.
  name: Dfns Networks API
  slug: dfns-networks-api
- description: Permissions and their assignments to identities.
  name: Dfns Permissions API
  slug: dfns-permissions-api
- description: Policy engine rules and approval decisions.
  name: Dfns Policies API
  slug: dfns-policies-api
- description: Machine identities and their access tokens.
  name: Dfns ServiceAccounts API
  slug: dfns-serviceaccounts-api
- description: Raw signature generation from keys.
  name: Dfns Signatures API
  slug: dfns-signatures-api
- description: Sign-and-broadcast of caller-supplied transactions from a wallet.
  name: Dfns Transactions API
  slug: dfns-transactions-api
- description: Asset transfers built, signed, and broadcast from a wallet.
  name: Dfns Transfers API
  slug: dfns-transfers-api
- description: Programmable non-custodial wallets, balances, NFTs, and history.
  name: Dfns Wallets API
  slug: dfns-wallets-api
- description: Event webhooks and delivery logs.
  name: Dfns Webhooks API
  slug: dfns-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: Dfns API
  slug: open-dfns
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dfns-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dfns-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dfns-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dfns
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dfns
- group: company
  title: ''
  type: Website
  url: https://www.dfns.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dfns.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/dfns-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dfns-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dfns-finops.yml
created: '2026-07-01'
description: Dfns is a wallet-as-a-service and MPC key-management infrastructure provider. Its API lets businesses create programmable, non-custodial wallets backed by multi-party-computation key shares, sign and broadcast transactions across many blockchains, and govern every action through a programmable policy engine with delegated signing, approvals, and User Action Signing.
finops:
- name: Dfns Finops
  service_category: Blockchain and Digital Asset Infrastructure
  slug: dfns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dfns.png
layout: provider
modified: '2026-07-01'
name: Dfns
nav: Providers
network: true
overview: 'Dfns publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Approvals API, Auth API, Keys API, and 9 more. Tagged areas include Wallets, MPC, Key Management, Digital Assets, and Web3.


  Dfns'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Dfns Plans Pricing
  plan_count: 3
  slug: dfns-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 4
  name: Dfns Rate Limits
  slug: dfns-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dfns/refs/heads/main/screenshots/dfns-2026-07-25T212051.png
security:
- kind: authentication
  name: Dfns Authentication
  slug: dfns-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Dfns Domain Security
  slug: dfns-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dfns
tags:
- Wallets
- MPC
- Key Management
- Digital Assets
- Web3
- Non-Custodial
website: https://www.dfns.co/
---
