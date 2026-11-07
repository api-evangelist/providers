---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Read-only JSON API for Braiins Pool, the oldest active Bitcoin mining pool (first block 2010, 1.29M+ BTC mined). Six documented endpoints: pool stats and recent blocks, user profile and rewards, daily'
  name: Braiins Pool API
  slug: braiins-pool-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: Read caller-owned balances and accounting transactions.
  name: Braiins Accounts API
  slug: braiins-academy-accounts-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Actions API from Braiins — 8 operation(s) for actions.
  name: Braiins Actions API
  slug: braiins-academy-actions-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Advanced Settings API from Braiins — 2 operation(s) for advanced settings.
  name: Braiins Advanced Settings API
  slug: braiins-academy-advanced-settings-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Authentication API from Braiins — 2 operation(s) for authentication.
  name: Braiins Authentication API
  slug: braiins-academy-authentication-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: Create, update, cancel, and inspect caller-owned spot-market bids.
  name: Braiins Bid orders API
  slug: braiins-academy-bid-orders-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Configuration API from Braiins — 2 operation(s) for configuration.
  name: Braiins Configuration API
  slug: braiins-academy-configuration-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: Quote, schedule, manage, and inspect caller-owned fixed-duration contracts.
  name: Braiins Contracts API
  slug: braiins-academy-contracts-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Cooling API from Braiins — 2 operation(s) for cooling.
  name: Braiins Cooling API
  slug: braiins-academy-cooling-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Documentation API from Braiins — 1 operation(s) for documentation.
  name: Braiins Documentation API
  slug: braiins-academy-documentation-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The License API from Braiins — 2 operation(s) for license.
  name: Braiins License API
  slug: braiins-academy-license-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: Spot-market rules, units, and fees needed to construct valid orders.
  name: Braiins Market configuration API
  slug: braiins-academy-market-configuration-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: Public statistics, order-book snapshots, trades, and OHLCV bars.
  name: Braiins Market data API
  slug: braiins-academy-market-data-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Miner API from Braiins — 8 operation(s) for miner.
  name: Braiins Miner API
  slug: braiins-academy-miner-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Network API from Braiins — 2 operation(s) for network.
  name: Braiins Network API
  slug: braiins-academy-network-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Performance API from Braiins — 18 operation(s) for performance.
  name: Braiins Performance API
  slug: braiins-academy-performance-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Pools API from Braiins — 3 operation(s) for pools.
  name: Braiins Pools API
  slug: braiins-academy-pools-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Upgrade API from Braiins — 3 operation(s) for upgrade.
  name: Braiins Upgrade API
  slug: braiins-academy-upgrade-api
- baseURL: http://miner/api/v1
  baseurl_source: declared
  description: The Version API from Braiins — 1 operation(s) for version.
  name: Braiins Version API
  slug: braiins-academy-version-api
artifact_total: 31
common:
- group: other
  href: https://artifacts.apis.io/braiins-academy/capabilities/braiins-academy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/braiins-academy-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/braiins-academy/overlays/braiins-academy-braiins-os-public-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/braiins-academy-braiins-os-public-rest-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/braiins-academy/overlays/braiins-academy-braiins-hashpower-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/braiins-academy-braiins-hashpower-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://braiins.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://academy.braiins.com
- group: docs
  title: ''
  type: Documentation
  url: https://academy.braiins.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.braiins-os.com/latest/openapi.html
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.braiins.com/braiins-hashpower/quick-start.md
- group: company
  title: ''
  type: Blog
  url: https://braiins.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braiins
- group: operate
  title: ''
  type: Support
  url: https://help.braiins.com/en/support/tickets/new
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.braiins.com
- group: start
  title: ''
  type: SignUp
  url: https://manager.braiins.com/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://braiins.com/manager/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://braiins.com/legal/braiins-general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://braiins.com/legal/privacy-policy
- group: learn
  title: ''
  type: X-Academy
  url: https://academy.braiins.com
- group: other
  title: ''
  type: X-Product-Pool
  url: https://braiins.com/pool
- group: other
  title: ''
  type: X-Product-Firmware
  url: https://braiins.com/os/plus
- group: other
  title: ''
  type: X-StratumV2
  url: https://braiins.com/stratum-v2
- group: auth
  href: https://artifacts.apis.io/braiins-academy/authentication/braiins-academy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/braiins-academy-authentication.yml
- group: design
  href: https://artifacts.apis.io/braiins-academy/conventions/braiins-academy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/braiins-academy-conventions.yml
- group: design
  href: https://artifacts.apis.io/braiins-academy/errors/braiins-academy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/braiins-academy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/braiins-academy/lifecycle/braiins-academy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/braiins-academy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/braiins-academy/lifecycle/braiins-academy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/braiins-academy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/braiins-academy/changelog/braiins-academy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/braiins-academy-changelog.yml
- group: design
  href: https://artifacts.apis.io/braiins-academy/conformance/braiins-academy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/braiins-academy-conformance.yml
- group: auth
  href: https://artifacts.apis.io/braiins-academy/security/braiins-academy-trust-center.yml
  title: ''
  type: Compliance
  url: security/braiins-academy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/braiins-academy/security/braiins-academy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/braiins-academy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/braiins-academy/security/braiins-academy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/braiins-academy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/braiins-academy/security/braiins-academy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/braiins-academy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/braiins-academy/well-known/braiins-academy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/braiins-academy-security.txt
- group: agent
  href: https://artifacts.apis.io/braiins-academy/well-known/braiins-academy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/braiins-academy-well-known.yml
- group: auth
  href: https://artifacts.apis.io/braiins-academy/security/braiins-academy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braiins-academy-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/braiins-academy/rate-limits/braiins-academy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/braiins-academy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/braiins-academy/plans/braiins-academy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/braiins-academy-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/braiins-academy/finops/braiins-academy-finops.yml
  title: ''
  type: FinOps
  url: finops/braiins-academy-finops.yml
- group: build
  href: https://artifacts.apis.io/braiins-academy/packages/braiins-academy-packages.yml
  title: ''
  type: Packages
  url: packages/braiins-academy-packages.yml
- group: build
  href: https://artifacts.apis.io/braiins-academy/cli/braiins-academy-cli.yml
  title: ''
  type: CLI
  url: cli/braiins-academy-cli.yml
- group: start
  href: https://artifacts.apis.io/braiins-academy/sandbox/braiins-academy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/braiins-academy-sandbox.yml
- group: design
  href: https://artifacts.apis.io/braiins-academy/data-model/braiins-academy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/braiins-academy-data-model.yml
- group: agent
  href: https://artifacts.apis.io/braiins-academy/llms/braiins-academy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/braiins-academy-llms.txt
- group: agent
  href: https://artifacts.apis.io/braiins-academy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/braiins-academy/mcp/braiins-academy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/braiins-academy-mcp.yml
created: '2025-03-01'
description: 'Braiins is a Prague-based Bitcoin mining technology company that operates the world''s longest-running Bitcoin mining pool (Slush Pool, now Braiins Pool, mining since 2010), builds Braiins OS autotuning ASIC firmware, and co-developed Stratum V2, the successor mining-pool protocol. Three of its products publish an API: Braiins OS ships a Public API over both gRPC and REST that runs on the miner itself (63 REST operations, 16 proto3 service files); Braiins Hashpower publishes an OpenAPI 3.1 contract for its spot hashrate marketplace and fixed-duration contracts (35 operations); and Braiins Pool exposes six read-only JSON endpoints for pool, worker and reward statistics. Braiins Manager gates its own public API behind a paid tier. Braiins completed a SOC 2 Type 2 audit in 2025 and publishes a vulnerability disclosure policy with a five-business-day response commitment.'
finops:
- has_sources: true
  method: derived
  name: Braiins Academy Finops
  primary_unit: settled amount during order execution
  service_category: ''
  slug: braiins-academy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/braiins-academy.png
layout: provider
modified: '2026-09-04'
name: Braiins
nav: Providers
network: true
overview: 'Braiins publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Actions API, Advanced Settings API, and 16 more. Tagged areas include Bitcoin Mining, Cryptocurrency, Mining Pool, Mining Firmware, and Blockchain.


  The Braiins catalog on APIs.io includes 1 Spectral governance ruleset.


  Braiins'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 37 more developer resources.'
plans:
- name: Braiins Academy Plans Pricing
  plan_count: 1
  slug: braiins-academy-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Braiins Academy Rate Limits
  slug: braiins-academy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Braiins API Rules
  rule_count: 56
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 14
  slug: braiins-academy-rules
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 49.4
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - czech-republic
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 62.6
  provenance:
    conformance: first-party
    contracts:
      callable: 27.8
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/braiins-academy/braiins-academy-2026-06-20T173627.png
security:
- kind: authentication
  name: Braiins Academy Authentication
  slug: braiins-academy-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Braiins Academy Domain Security
  slug: braiins-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Braiins Academy Vulnerability Disclosure
  slug: braiins-academy-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Braiins Academy Trust Center
  slug: braiins-academy-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
skill_count: 4
skills:
- name: buy-hashrate-on-the-spot-market
  slug: braiins-academy-buy-hashrate-on-the-spot-market
- name: curtail-a-miner-on-an-energy-signal
  slug: braiins-academy-curtail-a-miner-on-an-energy-signal
- name: roll-a-fleet-onto-braiins-os
  slug: braiins-academy-roll-a-fleet-onto-braiins-os
- name: schedule-and-unwind-a-hashrate-contract
  slug: braiins-academy-schedule-and-unwind-a-hashrate-contract
slug: braiins-academy
tags:
- Bitcoin Mining
- Cryptocurrency
- Mining Pool
- Mining Firmware
- Blockchain
- Stratum V2
- Hashrate Marketplace
- Mining Management
- ASIC
- Energy
website: https://braiins.com
---
