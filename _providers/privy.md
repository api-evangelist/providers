---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Privy Agentic Access
  operation_count: 3
  slug: privy-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
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
- baseURL: https://api.privy.io/v1
  baseurl_source: declared
  description: Manage users and their linked accounts.
  name: Privy Users API
  slug: privy-users-api
- baseURL: https://api.privy.io/v1
  baseurl_source: declared
  description: Create and operate Privy-managed wallets.
  name: Privy Wallets API
  slug: privy-wallets-api
artifact_total: 17
collections:
- collection_type: open
  name: Privy REST Users API
  slug: open-privy-users-api
- collection_type: open
  name: Privy REST Users Wallets API
  slug: open-privy-wallets-api
- collection_type: open
  name: Privy REST API
  slug: open-privy
common:
- group: agent
  href: https://artifacts.apis.io/privy/agentic-access/privy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/privy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/privy/security/privy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/privy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/privy/security/privy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/privy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/privy/authentication/privy-authentication.yml
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
  href: https://artifacts.apis.io/privy/plans/privy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/privy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/privy/rate-limits/privy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/privy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/privy/finops/privy-finops.yml
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
- has_sources: true
  method: generated
  name: Privy Finops
  primary_unit: ''
  service_category: Web3
  slug: privy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/privy.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.privy.io over HTTP; 3 tools listed.
  name: Privy MCP Server
  slug: privy
modified: '2026-05-08'
name: Privy
nav: Providers
network: true
overview: 'Privy publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Users API, Wallets API, and 3 more. Tagged areas include Web3, Wallets, Authentication, Embedded Wallets, and MPC.


  The Privy catalog on APIs.io includes 1 Spectral governance ruleset.


  Privy''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Privy Plans Pricing
  plan_count: 3
  slug: privy-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Privy Rate Limits
  slug: privy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Privy API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: privy-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 16.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/privy/privy-2026-06-20T192122.png
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
  summary_line: no policy recorded
slug: privy
tags:
- Web3
- Wallets
- Authentication
- Embedded Wallets
- MPC
website: https://www.privy.io/
---
