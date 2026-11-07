---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Asterpay Io Agentic Access
  operation_count: 68
  slug: asterpay-io-agentic-access
  summary_line: 68 operations · 11 acting
api_count: 1
apis:
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The ai API from AsterPay — 8 operation(s) for ai.
  name: AsterPay AI API
  slug: asterpay-io-ai-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The crypto API from AsterPay — 3 operation(s) for crypto.
  name: AsterPay Crypto API
  slug: asterpay-io-crypto-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The data API from AsterPay — 39 operation(s) for data.
  name: AsterPay Data API
  slug: asterpay-io-data-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The discovery API from AsterPay — 1 operation(s) for discovery.
  name: AsterPay Discovery API
  slug: asterpay-io-discovery-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The market API from AsterPay — 5 operation(s) for market.
  name: AsterPay Market API
  slug: asterpay-io-market-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The sessions API from AsterPay — 1 operation(s) for sessions.
  name: AsterPay Sessions API
  slug: asterpay-io-sessions-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The settlement API from AsterPay — 3 operation(s) for settlement.
  name: AsterPay Settlement API
  slug: asterpay-io-settlement-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The trust API from AsterPay — 6 operation(s) for trust.
  name: AsterPay Trust API
  slug: asterpay-io-trust-api
- baseURL: https://x402.asterpay.io
  baseurl_source: declared
  description: The utility API from AsterPay — 1 operation(s) for utility.
  name: AsterPay Utility API
  slug: asterpay-io-utility-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/asterpay-io/agentic-access/asterpay-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asterpay-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/asterpay-io/rate-limits/asterpay-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asterpay-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/asterpay-io/plans/asterpay-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asterpay-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asterpay-io/rules/asterpay-io-rules.yml
  title: ''
  type: Spectral
  url: rules/asterpay-io-rules.yml
- group: design
  href: https://artifacts.apis.io/asterpay-io/vocabulary/asterpay-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asterpay-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/asterpay-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/asterpay-io/cli/asterpay-io-cli.yml
  title: ''
  type: CLI
  url: cli/asterpay-io-cli.yml
- group: design
  href: https://artifacts.apis.io/asterpay-io/conventions/asterpay-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/asterpay-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/asterpay-io/conventions/asterpay-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/asterpay-io-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://asterpay.io/trust/
- group: auth
  href: https://artifacts.apis.io/asterpay-io/authentication/asterpay-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asterpay-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/asterpay-io/errors/asterpay-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asterpay-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asterpay-io/conformance/asterpay-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asterpay-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asterpay-io/llms/asterpay-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asterpay-io-llms.txt
- group: other
  href: https://artifacts.apis.io/asterpay-io/a2a/asterpay-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/asterpay-io-a2a.yml
- group: build
  href: https://artifacts.apis.io/asterpay-io/mcp/asterpay-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/asterpay-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/asterpay-io/mcp/asterpay-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asterpay-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/asterpay-io/well-known/asterpay-io-x402-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asterpay-io-x402-security.txt
- group: auth
  href: https://artifacts.apis.io/asterpay-io/well-known/asterpay-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asterpay-io-security.txt
- group: auth
  href: https://artifacts.apis.io/asterpay-io/well-known/asterpay-io-mta-sts-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asterpay-io-mta-sts-security.txt
- group: auth
  href: https://artifacts.apis.io/asterpay-io/well-known/asterpay-io-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asterpay-io-api-security.txt
- group: agent
  href: https://artifacts.apis.io/asterpay-io/well-known/asterpay-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asterpay-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/asterpay-io/hosts/asterpay-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asterpay-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/asterpay-io/vendors/asterpay-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asterpay-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/asterpay-io/packages/asterpay-io-packages.yml
  title: ''
  type: SDKs
  url: packages/asterpay-io-packages.yml
- group: build
  href: https://artifacts.apis.io/asterpay-io/packages/asterpay-io-packages.yml
  title: ''
  type: Packages
  url: packages/asterpay-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://asterpay.io/status/
- group: auth
  title: ''
  type: Security
  url: https://asterpay.io/security/
- group: auth
  href: https://artifacts.apis.io/asterpay-io/security/asterpay-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/asterpay-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/asterpay-io/security/asterpay-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/asterpay-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/asterpay-io/security/asterpay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asterpay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asterpay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://asterpay.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://asterpay.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://asterpay.io/#top
- group: company
  title: ''
  type: Blog
  url: https://asterpay.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AsterPay
- group: commercial
  title: ''
  type: Pricing
  url: https://asterpay.io/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.asterpay.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asterpay.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asterpay.io/privacy
created: '2026-11-01'
description: AsterPay, operated by AELIRA LTD in Cyprus, provides an EUR‑native facilitator for AI agent payments. It supports x402 (Coinbase) and MPP (Stripe/Tempo) protocols, converting USDC to EUR via SEPA Instant, with KYA trust scoring and MiCA alignment. Agents can pay merchants directly to their bank accounts in under 10 seconds, with transparent fees and compliance features.
image: https://asterpay.io/assets/asterpay-icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.asterpay.io.
  name: AsterPay MCP Server
  slug: asterpay-io-mcp-yml
modified: '2026-11-01'
name: AsterPay
nav: Providers
network: true
overview: 'AsterPay publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Crypto API, Data API, and 6 more. Tagged areas include Payments, Fintech, Artificial Intelligence, EUR, and Settlement.


  The AsterPay catalog on APIs.io includes 1 Spectral governance ruleset.


  AsterPay''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 34 more developer resources.'
plans:
- name: Asterpay Io Plans Pricing
  plan_count: 3
  slug: asterpay-io-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Asterpay Io Rate Limits
  slug: asterpay-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: AsterPay API Rules
  rule_count: 55
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 6
  slug: asterpay-io-rules
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 51.5
    developer_ergonomics: 48.1
    discoverability: 65.0
    operational_transparency: 36.8
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asterpay Io Authentication
  slug: asterpay-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Asterpay Io Domain Security
  slug: asterpay-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Asterpay Io Vulnerability Disclosure
  slug: asterpay-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Asterpay Io Trust Center
  slug: asterpay-io-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: agent-trust-score
  slug: asterpay-io-agent-trust-score
slug: asterpay-io
tags:
- Payments
- Fintech
- Artificial Intelligence
- EUR
- Settlement
website: https://asterpay.io/
---
