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
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Factline Dev Agentic Access
  operation_count: 95
  slug: factline-dev-agentic-access
  summary_line: 95 operations
api_count: 1
apis:
- baseURL: https://factline.dev
  baseurl_source: declared
  description: The Free API from factline-dev — 52 operation(s) for free.
  name: factline-dev Free API
  slug: factline-dev-free-api
- baseURL: https://factline.dev
  baseurl_source: declared
  description: The Paid (x402) API from factline-dev — 43 operation(s) for paid (x402).
  name: factline-dev Paid (x402) API
  slug: factline-dev-paid-x402-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/factline-dev/agentic-access/factline-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/factline-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/factline-dev/rules/factline-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/factline-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/factline-dev/json-ld/factline-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/factline-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/factline-dev/vocabulary/factline-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/factline-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/factline-dev/data-model/factline-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/factline-dev-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://factline.dev/trust
- group: design
  href: https://artifacts.apis.io/factline-dev/errors/factline-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/factline-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/factline-dev/conformance/factline-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/factline-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/factline-dev/llms/factline-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/factline-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/factline-dev/a2a/factline-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/factline-dev-a2a.yml
- group: auth
  href: https://artifacts.apis.io/factline-dev/well-known/factline-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/factline-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/factline-dev/well-known/factline-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/factline-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/factline-dev/hosts/factline-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/factline-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/factline-dev/vendors/factline-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/factline-dev-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://factline.dev/trust
- group: start
  title: ''
  type: SignUp
  url: https://factline.dev/registerplicht-makelaars
- group: auth
  href: https://artifacts.apis.io/factline-dev/authentication/factline-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/factline-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/factline-dev/security/factline-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/factline-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/factline-dev/security/factline-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/factline-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://factline.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://factline.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://factline.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://factline.dev/business#trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://factline.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://factline.dev/privacy
- group: operate
  title: ''
  type: Changelog
  url: https://factline.dev/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://factline.dev/status
- group: commercial
  title: ''
  type: Pricing
  url: https://factline.dev/#prices
created: '2026-10-29'
description: Factline provides a unified API for financial teams and AI agents to verify suppliers and payees against official records. It offers KYB, invoice validation, IBAN, VAT, sanctions, and PEP checks in a single call, enabling compliance and risk management. Pricing starts from $0.001 per check, with a free trial available. The service aims to streamline due diligence and reduce fraud in payments.
image: https://factline.dev/og.png
jsonld:
- class_count: 1
  name: Factline Dev Context
  property_count: 3
  slug: factline-dev-context
layout: provider
modified: '2026-10-29'
name: factline-dev
nav: Providers
network: true
overview: 'factline-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Free API and Paid (x402) API. Tagged areas include Company, Finance, Compliance, and KYB.


  The factline-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  factline-dev''s developer surface includes signup flow, authentication, documentation, API reference, getting-started guide, changelog, pricing, and 21 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: factline-dev API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: factline-dev-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 56.2
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/factline-dev/factline-dev-2026-11-03T131809.png
security:
- kind: authentication
  name: Factline Dev Authentication
  slug: factline-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Factline Dev Domain Security
  slug: factline-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Factline Dev Vulnerability Disclosure
  slug: factline-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: factline-dev
tags:
- Company
- Finance
- Compliance
- KYB
website: https://factline.dev/
---
