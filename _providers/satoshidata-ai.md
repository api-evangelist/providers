---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Satoshidata Ai Agentic Access
  operation_count: 96
  slug: satoshidata-ai-agentic-access
  summary_line: 96 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The batch API from satoshidata-ai — 1 operation(s) for batch.
  name: satoshidata-ai Batch API
  slug: satoshidata-ai-batch-api
- description: Paid API-key bridge checkout, plan, and payment status surfaces.
  name: satoshidata-ai Billing API
  slug: satoshidata-ai-billing-api
- description: The chain API from satoshidata-ai — 2 operation(s) for chain.
  name: satoshidata-ai Chain API
  slug: satoshidata-ai-chain-api
- description: Community-submitted wallet reports, payment-backed publishing, and voting.
  name: satoshidata-ai Community API
  slug: satoshidata-ai-community-api
- description: OpenAPI and public discovery metadata for the current bridge state.
  name: satoshidata-ai Discovery API
  slug: satoshidata-ai-discovery-api
- description: The entities API from satoshidata-ai — 1 operation(s) for entities.
  name: satoshidata-ai Entities API
  slug: satoshidata-ai-entities-api
- description: The feedback API from satoshidata-ai — 1 operation(s) for feedback.
  name: satoshidata-ai Feedback API
  slug: satoshidata-ai-feedback-api
- description: Operational status, freshness, and service discovery.
  name: satoshidata-ai Health API
  slug: satoshidata-ai-health-api
- description: The labels API from satoshidata-ai — 1 operation(s) for labels.
  name: satoshidata-ai Labels API
  slug: satoshidata-ai-labels-api
- description: Price, mempool, derivatives, and transaction lookup endpoints.
  name: satoshidata-ai Market API
  slug: satoshidata-ai-market-api
- description: On-chain and lane-specific metric payloads.
  name: satoshidata-ai Metrics API
  slug: satoshidata-ai-metrics-api
- description: The risk API from satoshidata-ai — 4 operation(s) for risk.
  name: satoshidata-ai Risk API
  slug: satoshidata-ai-risk-api
- description: The sanctions API from satoshidata-ai — 3 operation(s) for sanctions.
  name: satoshidata-ai Sanctions API
  slug: satoshidata-ai-sanctions-api
- description: Bitcoin proof-of-existence endpoints for hash intake, status, proof download, and verification.
  name: satoshidata-ai Timestamping API
  slug: satoshidata-ai-timestamping-api
- description: Chain intelligence endpoints for trust, summary, detail, and source depth.
  name: satoshidata-ai Wallets API
  slug: satoshidata-ai-wallets-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/satoshidata-ai/agentic-access/satoshidata-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/satoshidata-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/satoshidata-ai/rules/satoshidata-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/satoshidata-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/satoshidata-ai/json-ld/satoshidata-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/satoshidata-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/satoshidata-ai/vocabulary/satoshidata-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/satoshidata-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/satoshidata-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/satoshidata-ai/data-model/satoshidata-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/satoshidata-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/satoshidata-ai/changelog/satoshidata-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/satoshidata-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/satoshidata-ai/security/satoshidata-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/satoshidata-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/satoshidata-ai/authentication/satoshidata-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/satoshidata-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/satoshidata-ai/errors/satoshidata-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/satoshidata-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/satoshidata-ai/conformance/satoshidata-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/satoshidata-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/satoshidata-ai/llms/satoshidata-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/satoshidata-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/satoshidata-ai/a2a/satoshidata-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/satoshidata-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/satoshidata-ai/well-known/satoshidata-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/satoshidata-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/satoshidata-ai/well-known/satoshidata-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/satoshidata-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/satoshidata-ai/hosts/satoshidata-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/satoshidata-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/satoshidata-ai/vendors/satoshidata-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/satoshidata-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/satoshidata-ai/packages/satoshidata-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/satoshidata-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/satoshidata-ai/packages/satoshidata-ai-packages.yml
  title: ''
  type: Packages
  url: packages/satoshidata-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/satoshidata-ai/security/satoshidata-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/satoshidata-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/satoshidata-ai/security/satoshidata-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/satoshidata-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://satoshidata.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://satoshidata.ai/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://satoshidata.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://satoshidata.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://satoshidata.ai/docs/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://satoshidata.ai/support
- group: company
  title: ''
  type: Blog
  url: https://satoshidata.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wrbtc
- group: operate
  title: ''
  type: Roadmap
  url: https://satoshidata.ai/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://satoshidata.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://satoshidata.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://satoshidata.ai/privacy
- group: build
  title: ''
  type: Postman
  url: https://satoshidata.ai/postman
created: '2026-10-30'
description: SatoshiData.ai provides a Bitcoin chain intelligence API designed for AI agents and developers. It offers wallet trust-safety analysis, on-chain signals, transaction verification, Bitcoin timestamping, and a discovery layer for machine-readable data. The service runs in a public beta, offering free access with optional paid tiers for higher limits. Documentation includes a quick-start guide, API reference, and examples. The platform emphasizes privacy, security, and transparent pricing.
image: https://satoshidata.ai/logo.png
json_schemas:
- name: ApiHealthFullResponse
  property_count: 39
  slug: satoshidata-ai-api-health-full-response
- name: ApiHealthResponse
  property_count: 39
  slug: satoshidata-ai-api-health-response
- name: NetworkIntelligenceResponse
  property_count: 37
  slug: satoshidata-ai-network-intelligence-response
- name: WalletOverviewResponse
  property_count: 34
  slug: satoshidata-ai-wallet-overview-response
- name: WalletSummaryResponse
  property_count: 39
  slug: satoshidata-ai-wallet-summary-response
- name: WalletTrustSafetyResponse
  property_count: 35
  slug: satoshidata-ai-wallet-trust-safety-response
jsonld:
- class_count: 120
  name: Satoshidata Ai Context
  property_count: 179
  slug: satoshidata-ai-context
layout: provider
modified: '2026-10-30'
name: satoshidata-ai
nav: Providers
network: true
overview: 'satoshidata-ai publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Billing API, Chain API, and 12 more. Tagged areas include Bitcoin, Artificial Intelligence, Finance, Chain-Intelligence, and Company.


  The satoshidata-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  satoshidata-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Satoshidata Ai Plans Pricing
  plan_count: 0
  slug: satoshidata-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Satoshidata Ai Rate Limits
  slug: satoshidata-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: satoshidata-ai API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: satoshidata-ai-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 50.5
    discoverability: 64.3
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/satoshidata-ai/satoshidata-ai-2026-11-03T142734.png
security:
- kind: authentication
  name: Satoshidata Ai Authentication
  slug: satoshidata-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Satoshidata Ai Domain Security
  slug: satoshidata-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Satoshidata Ai Vulnerability Disclosure
  slug: satoshidata-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: health-skill
  slug: satoshidata-ai-health-skill
slug: satoshidata-ai
tags:
- Bitcoin
- Artificial Intelligence
- Finance
- Chain-Intelligence
- Company
website: https://satoshidata.ai/
---
