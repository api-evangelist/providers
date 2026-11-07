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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Scale3 Agentic Access
  operation_count: 2
  slug: scale3-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://web-backend.scale3production.com
  baseurl_source: declared
  description: Node software updates and network intelligence feeds
  name: Scale3 Blockchain Intelligence API
  slug: scale3-blockchain-intelligence-api
artifact_total: 13
asyncapis:
- description: ''
  name: Scale3 Webhooks
  slug: scale3-webhooks
collections:
- collection_type: open
  name: Scale3 Blockchain Intelligence API
  slug: open-scale3-blockchain-intelligence-api
common:
- group: other
  href: https://artifacts.apis.io/scale3/capabilities/scale3-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scale3-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/scale3/plans/scale3-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scale3-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/scale3/mcp/scale3-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/scale3-mcp.yml
- group: other
  href: https://artifacts.apis.io/scale3/overlays/scale3-blockchain-intelligence-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scale3-blockchain-intelligence-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.scale3labs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scale3labs.com/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scale3labs.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scale3labs.com/intel/blockchain-intelligence/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scale3labs.com/intel/blockchain-intelligence/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scale3labs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.scale3labs.com/signin
- group: company
  title: ''
  type: Blog
  url: https://medium.com/scale3-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Scale3-Labs
- group: operate
  title: ''
  type: Support
  url: mailto:support@scale3labs.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scale3labs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scale3labs.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://scale3labs.statuspage.io
- group: auth
  title: ''
  type: Compliance
  url: https://www.scale3labs.com/security
- group: agent
  href: https://artifacts.apis.io/scale3/llms/scale3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scale3-llms.txt
- group: build
  href: https://artifacts.apis.io/scale3/packages/scale3-packages.yml
  title: ''
  type: Packages
  url: packages/scale3-packages.yml
- group: build
  href: https://artifacts.apis.io/scale3/packages/scale3-packages.yml
  title: ''
  type: SDKs
  url: packages/scale3-packages.yml
- group: build
  href: https://artifacts.apis.io/scale3/cli/scale3-cli.yml
  title: ''
  type: CLI
  url: cli/scale3-cli.yml
- group: design
  href: https://artifacts.apis.io/scale3/asyncapi/scale3-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/scale3-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/scale3/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/scale3/well-known/scale3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scale3-well-known.yml
- group: design
  href: https://artifacts.apis.io/scale3/conformance/scale3-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scale3-conformance.yml
- group: design
  href: https://artifacts.apis.io/scale3/lifecycle/scale3-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scale3-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/scale3/security/scale3-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scale3-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/scale3/security/scale3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scale3-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/scale3/agentic-access/scale3-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scale3-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/scale3/authentication/scale3-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scale3-authentication.yml
created: '2026-07-17'
description: Scale3 Labs is a modern observability and infrastructure platform for Web3 and generative AI. Its Web3 products (Autopilot, Nodepilot and Blockchain Intelligence) let node operators and validators deploy, monitor, log and alert on blockchain nodes across 40+ chains including Ethereum, Sui, Solana, Cosmos and Polkadot, with a Blockchain Intelligence REST API that surfaces node software updates and network announcements. Scale3 also builds Langtrace, an open-source OpenTelemetry-based observability SDK for LLM applications. The company is SOC 2 Type 1 certified and is backed by Redpoint Ventures.
finops:
- has_sources: true
  method: derived
  name: Scale3 Finops
  primary_unit: node
  service_category: ''
  slug: scale3-finops
  template: false
image: https://www.scale3labs.com/assets/scale3-opengraph.png
layout: provider
modified: '2026-07-21'
name: Scale3
nav: Providers
network: true
overview: 'Scale3 publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Blockchain Intelligence API. Tagged areas include Company, Blockchain, Web3, Node Monitoring, and Observability.


  The Scale3 catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Scale3''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 24 more developer resources.'
plans:
- name: Scale3 Plans Pricing
  plan_count: 3
  slug: scale3-plans-pricing
- name: Scale3 Price Estimates
  plan_count: 0
  slug: scale3-price-estimates
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Scale3 API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: scale3-rules
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 60.6
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/scale3/scale3-2026-08-17T081729.png
security:
- kind: authentication
  name: Scale3 Authentication
  slug: scale3-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scale3 Domain Security
  slug: scale3-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Scale3 Trust Center
  slug: scale3-trust-center
  summary_line: SOC 2
skill_count: 2
skills:
- name: Check blockchain node software updates
  slug: scale3-check-node-updates
- name: Query the blockchain network intelligence feed
  slug: scale3-query-network-feed
slug: scale3
tags:
- Company
- Blockchain
- Web3
- Node Monitoring
- Observability
- Infrastructure
- Validator
- DevOps
- Alerting
- LLM Observability
website: https://www.scale3labs.com/
---
