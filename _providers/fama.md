---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fama Agentic Access
  operation_count: 26
  slug: fama-agentic-access
  summary_line: 26 operations · 2 acting
api_count: 3
apis:
- description: v2 REST API for submitting candidate screening checks and retrieving report findings (person, profiles, posts, web content, summary, and signed PDF). Bearer-token auth; report completion via HTTP call
  name: Fama REST API
  slug: fama-rest-api
- baseURL: https://public-api.fama.io
  baseurl_source: declared
  description: The Public Endpoints API from Fama — 11 operation(s) for public endpoints.
  name: Fama Public Endpoints API
  slug: fama-public-endpoints-api
- baseURL: https://public-api.fama.io
  baseurl_source: declared
  description: endpoints intended for direct use
  name: Fama Public API
  slug: fama-publicapi-api
- baseURL: https://public-api.fama.io
  baseurl_source: declared
  description: The Report API from Fama — 1 operation(s) for report.
  name: Fama Report API
  slug: fama-report-api
artifact_total: 16
asyncapis:
- description: ''
  name: Fama Webhooks
  slug: fama-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/agentic-access/fama-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fama-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/rules/fama-rules.yml
  title: ''
  type: Spectral
  url: rules/fama-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/json-ld/fama-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fama-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/vocabulary/fama-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fama-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/errors/fama-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fama-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/well-known/fama-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fama-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/hosts/fama-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fama-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/vendors/fama-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fama-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fama.io/terms-and-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://fama.io/press
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/plans/fama-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fama-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fama.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fama.io
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fama.io/reference/fama-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fama.io/reference/api-token
- group: operate
  title: ''
  type: Support
  url: https://fama.io/contact
- group: company
  title: ''
  type: Blog
  url: https://fama.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fama.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fama.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fama.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fama.io
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/llms/fama-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fama-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/authentication/fama-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fama-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/rate-limits/fama-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fama-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/errors/fama-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/fama-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/conventions/fama-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fama-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/lifecycle/fama-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fama-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/lifecycle/fama-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/fama-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/asyncapi/fama-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fama-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/sandbox/fama-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fama-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/mcp/fama-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fama-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/data-model/fama-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fama-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/conformance/fama-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fama-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fama.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/security/fama-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fama-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/security/fama-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fama.io
created: '2026-07-17'
description: Fama is an AI-powered social media and online screening platform for employment decisions. Its REST API lets HR platforms and background-screening providers submit candidate checks and retrieve behavioral findings — flagged posts, web content, and social profiles — mapped to workplace-misconduct categories across 30+ languages while filtering out protected-class information for EEOC/FCRA-aligned adjudication. Reports are delivered via completion callbacks or polling as JSON or a signed PDF, powering pre-employment screening (Fama Plus), comprehensive candidate assessment (Fama 360), and ongoing employee monitoring (Fama Pulse).
image: https://cdn.prod.website-files.com/63ea1ecaf41aeda5d5045103/6622b457a4c9d4fde1e2a424_Fama%20Open%20Graph%20Image%202%201200%20x%20630.svg
json_schemas:
- name: CheckRequest
  property_count: 6
  slug: fama-check-request
- name: CheckResponse
  property_count: 2
  slug: fama-check-response
- name: CheckStatus
  property_count: 10
  slug: fama-check-status
jsonld:
- class_count: 22
  name: Fama Context
  property_count: 63
  slug: fama-context
layout: provider
modified: '2026-07-19'
name: Fama
nav: Providers
network: true
overview: 'Fama publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public Endpoints API, Public API, Report API, and 1 more. Tagged areas include Company, Employment Screening, Background Checks, Human Resources, and Social Media.


  The Fama catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Fama''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Fama Plans Pricing
  plan_count: 2
  slug: fama-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Fama Rate Limits
  slug: fama-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Fama API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: fama-rules
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.3
  facets:
    access_clarity: 81.6
    contract_governance: 35.6
    contract_quality: 72.2
    developer_ergonomics: 47.0
    discoverability: 80.4
    operational_transparency: 44.7
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/screenshots/fama-2026-07-25T214205.png
security:
- kind: authentication
  name: Fama Authentication
  slug: fama-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fama Domain Security
  slug: fama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fama Trust Center
  slug: fama-trust-center
  summary_line: SOC 2 Type 1
slug: fama
tags:
- Company
- Employment Screening
- Background Checks
- Human Resources
- Social Media
- Risk Management
- Compliance
- Artificial Intelligence
website: https://fama.io
---
