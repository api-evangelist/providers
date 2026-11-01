---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Stratalize Com Agentic Access
  operation_count: 202
  slug: stratalize-com-agentic-access
  summary_line: 202 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.stratalize.com
  baseurl_source: declared
  description: The X402 API from stratalize-com — 202 operation(s) for x402.
  name: stratalize-com X402 API
  slug: stratalize-com-x402-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/stratalize-com/agentic-access/stratalize-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stratalize-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/stratalize-com/rate-limits/stratalize-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stratalize-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/stratalize-com/rules/stratalize-com-rules.yml
  title: ''
  type: Spectral
  url: rules/stratalize-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/stratalize-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/stratalize-com/security/stratalize-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/stratalize-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stratalize-com/authentication/stratalize-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stratalize-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/stratalize-com/errors/stratalize-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stratalize-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stratalize-com/conformance/stratalize-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stratalize-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stratalize-com/llms/stratalize-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stratalize-com-llms.txt
- group: other
  href: https://artifacts.apis.io/stratalize-com/a2a/stratalize-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/stratalize-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/stratalize-com/well-known/stratalize-com-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stratalize-com-trust-security.txt
- group: auth
  href: https://artifacts.apis.io/stratalize-com/well-known/stratalize-com-stratalize-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stratalize-com-stratalize-security.txt
- group: auth
  href: https://artifacts.apis.io/stratalize-com/well-known/stratalize-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stratalize-com-status-security.txt
- group: auth
  href: https://artifacts.apis.io/stratalize-com/well-known/stratalize-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stratalize-com-security.txt
- group: auth
  href: https://artifacts.apis.io/stratalize-com/well-known/stratalize-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stratalize-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/stratalize-com/well-known/stratalize-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stratalize-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stratalize-com/hosts/stratalize-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stratalize-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stratalize-com/vendors/stratalize-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stratalize-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.stratalize.com/
- group: auth
  href: https://artifacts.apis.io/stratalize-com/security/stratalize-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stratalize-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stratalize-com/security/stratalize-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stratalize-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stratalize.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.stratalize.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stratalize.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.stratalize.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://www.stratalize.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stratalize.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stratalize.com/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://stratalize.com/openapi.json
  - status: null
    url: https://app.stratalize.com/openapi.json
  - status: null
    url: https://trust.stratalize.com/openapi.json
  - status: 401
    url: https://app.stratalize.com/api/mcp
  - status: 401
    url: https://status.stratalize.com/api/mcp
  - status: 401
    url: https://trust.stratalize.com/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Stratalize provides project controls intelligence for construction schedule compliance. Its platform reads schedule files, validates them against specifications, and generates deliverables required by contracts. Human approval is required for each deliverable, and all approvals are cryptographically signed, ensuring auditability and governance. The service integrates with tools like Primavera P6 and supports AI-driven analysis while maintaining strict compliance and security.
image: https://www.stratalize.com/api/og/home
layout: provider
modified: '2026-10-29'
name: stratalize-com
nav: Providers
network: true
overview: 'stratalize-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: X402 API. Tagged areas include Company, Construction, Project Controls, Schedule Management, and AI.


  The stratalize-com catalog on APIs.io includes 1 Spectral governance ruleset.


  stratalize-com''s developer surface includes authentication, documentation, API reference, signup flow, and 24 more developer resources.'
plans:
- name: Stratalize Com Plans Pricing
  plan_count: 0
  slug: stratalize-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Stratalize Com Rate Limits
  slug: stratalize-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: stratalize-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: stratalize-com-rules
scopes:
- name: Stratalize Com Scopes
  scope_count: 0
  slug: stratalize-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 44.7
    developer_ergonomics: 44.5
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Stratalize Com Authentication
  slug: stratalize-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stratalize Com Domain Security
  slug: stratalize-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stratalize Com Vulnerability Disclosure
  slug: stratalize-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: fx-rate-benchmark
  slug: stratalize-com-fx-rate-benchmark
slug: stratalize-com
tags:
- Company
- Construction
- Project Controls
- Schedule Management
- AI
- Compliance
website: https://stratalize.com/
---
