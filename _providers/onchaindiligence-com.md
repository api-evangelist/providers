---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pay-per-call compliance checks and free discovery routes as described in the OpenAPI spec.
  name: OnchainDiligence API
  slug: onchaindiligence-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/onchaindiligence-com/vocabulary/onchaindiligence-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/onchaindiligence-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/onchaindiligence-com/security/onchaindiligence-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/onchaindiligence-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/onchaindiligence-com/conformance/onchaindiligence-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onchaindiligence-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/onchaindiligence-com/llms/onchaindiligence-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onchaindiligence-com-llms.txt
- group: other
  href: https://artifacts.apis.io/onchaindiligence-com/a2a/onchaindiligence-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/onchaindiligence-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/onchaindiligence-com/well-known/onchaindiligence-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/onchaindiligence-com-security.txt
- group: agent
  href: https://artifacts.apis.io/onchaindiligence-com/well-known/onchaindiligence-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onchaindiligence-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/onchaindiligence-com/hosts/onchaindiligence-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onchaindiligence-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/onchaindiligence-com/vendors/onchaindiligence-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onchaindiligence-com-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@onchaindiligence/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qazza1
- group: start
  title: ''
  type: GettingStarted
  url: https://onchaindiligence.com/pilot
- group: auth
  href: https://artifacts.apis.io/onchaindiligence-com/security/onchaindiligence-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/onchaindiligence-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/onchaindiligence-com/security/onchaindiligence-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onchaindiligence-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onchaindiligence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://onchaindiligence.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://onchaindiligence.com/developers
- group: operate
  title: ''
  type: Support
  url: https://onchaindiligence.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onchaindiligence.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onchaindiligence.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://onchaindiligence.com/status
created: '2026-10-30'
description: OnChainDiligence provides independent reconciliation for AI agent payments, offering free preflight evaluations, SDKs, and integration guides. It enables agents to declare payments, wallets to execute, and the platform to observe and reconcile evidence across supported settlement networks, including USDC on Base, Solana, and more. The service includes documentation, developer portals, pricing details, and support resources, aiming to simplify compliance and verification for AI-driven financial interactions.
image: https://onchaindiligence.com/og.png
layout: provider
modified: '2026-10-30'
name: onchaindiligence-com
nav: Providers
network: true
overview: 'onchaindiligence-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Artificial Intelligence, Payments, and Reconciliation.


  onchaindiligence-com''s developer surface includes getting-started guide, documentation, support, and 18 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 10.5
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 73.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/onchaindiligence-com/onchaindiligence-com-2026-11-03T140545.png
security:
- kind: domain-security
  name: Onchaindiligence Com Domain Security
  slug: onchaindiligence-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Onchaindiligence Com Vulnerability Disclosure
  slug: onchaindiligence-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: onchaindiligence-com
tags:
- Company
- Finance
- Artificial Intelligence
- Payments
- Reconciliation
- SDK
website: https://onchaindiligence.com/
---
