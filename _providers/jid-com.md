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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Jid Com Agentic Access
  operation_count: 15
  slug: jid-com-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
apis:
- baseURL: https://jid.com
  baseurl_source: declared
  description: Change monitoring with signed webhooks
  name: jid-com Monitors API
  slug: jid-com-monitors-api
- baseURL: https://jid.com
  baseurl_source: declared
  description: B2B lead and counterparty qualification
  name: jid-com Qualify API
  slug: jid-com-qualify-api
- baseURL: https://jid.com
  baseurl_source: declared
  description: 'Engage or not: a fast, deterministic answer for a lead, sender, vendor or website'
  name: jid-com Screen API
  slug: jid-com-screen-api
- baseURL: https://jid.com
  baseurl_source: declared
  description: The search API from jid-com — 1 operation(s) for search.
  name: jid-com Search API
  slug: jid-com-search-api
- baseURL: https://jid.com
  baseurl_source: declared
  description: The Signal API from jid-com — 1 operation(s) for signal.
  name: jid-com Signal API
  slug: jid-com-signal-api
- baseURL: https://jid.com
  baseurl_source: declared
  description: Decisions, files and receipts
  name: jid-com Verify API
  slug: jid-com-verify-api
artifact_total: 22
asyncapis:
- description: ''
  name: Jid Com Webhooks
  slug: jid-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/jid-com/agentic-access/jid-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jid-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/jid-com/rate-limits/jid-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jid-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jid-com/plans/jid-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jid-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jid-com/rules/jid-com-rules.yml
  title: ''
  type: Spectral
  url: rules/jid-com-rules.yml
- group: design
  href: https://artifacts.apis.io/jid-com/json-ld/jid-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jid-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/jid-com/vocabulary/jid-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jid-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/jid-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/jid-com/asyncapi/jid-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jid-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/jid-com/data-model/jid-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jid-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/jid-com/changelog/jid-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jid-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://jid.com/security
- group: auth
  href: https://artifacts.apis.io/jid-com/authentication/jid-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jid-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/jid-com/errors/jid-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jid-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jid-com/conformance/jid-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jid-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jid-com/llms/jid-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jid-com-llms.txt
- group: other
  href: https://artifacts.apis.io/jid-com/hosts/jid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jid-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/jid-com/vendors/jid-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jid-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jid.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://jid.com/status
- group: auth
  title: ''
  type: Security
  url: https://jid.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://jid.com/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://jid.com/changelog
- group: auth
  href: https://artifacts.apis.io/jid-com/security/jid-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jid-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/jid-com/security/jid-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jid-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jid-com/security/jid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jid.com/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://jid.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://jid.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://jid.com/solutions/procurement-agents
- group: commercial
  title: ''
  type: Pricing
  url: https://jid.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://jid.com/account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jid.com/privacy
created: '2026-10-30'
description: Jid provides a public trust API for AI agents, allowing them to verify whether a business is authorized, active, licensed, and not sanctioned before performing transactions. The service aggregates cited public registry data to produce a decision with reasons and a signed receipt, supporting compliance, risk management, and automated decision-making. It offers free access with generous limits, detailed privacy policies, and transparent terms, and is operated by QEIP LLC, a Silicon Valley Ventures company.
image: https://jid.com/opengraph-image?2fd2615791c4a3b9
json_schemas:
- name: Qualification
  property_count: 25
  slug: jid-com-qualification
- name: Receipt
  property_count: 5
  slug: jid-com-receipt
- name: ScreenResult
  property_count: 21
  slug: jid-com-screen-result
- name: SearchResponse
  property_count: 3
  slug: jid-com-search-response
- name: VerifyResponse
  property_count: 12
  slug: jid-com-verify-response
jsonld:
- class_count: 15
  name: Jid Com Context
  property_count: 113
  slug: jid-com-context
layout: provider
modified: '2026-10-30'
name: jid-com
nav: Providers
network: true
overview: 'jid-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Monitors API, Qualify API, Screen API, and 3 more. Tagged areas include Trust, Artificial Intelligence, Compliance, Data, and Verification.


  The jid-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  jid-com''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, pricing, and 26 more developer resources.'
plans:
- name: Jid Com Plans Pricing
  plan_count: 1
  slug: jid-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Jid Com Rate Limits
  slug: jid-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: jid-com API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: jid-com-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.4
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 71.5
    developer_ergonomics: 41.0
    discoverability: 66.1
    operational_transparency: 60.5
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jid-com/jid-com-2026-11-03T134142.png
security:
- kind: authentication
  name: Jid Com Authentication
  slug: jid-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jid Com Domain Security
  slug: jid-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jid Com Vulnerability Disclosure
  slug: jid-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Jid Com Trust Center
  slug: jid-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: search-businesses
  slug: jid-com-search-businesses
slug: jid-com
tags:
- Trust
- Artificial Intelligence
- Compliance
- Data
- Verification
website: https://jid.com/
---
