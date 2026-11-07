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
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Backworkhealth Com Agentic Access
  operation_count: 62
  slug: backworkhealth-com-agentic-access
  summary_line: 62 operations · 32 acting
api_count: 1
apis:
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Machine-readable tool manifest and controlled agent invocation
  name: Backwork Agent Tools API
  slug: backworkhealth-com-agent-tools-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Entitlement-gated, immutable commercial release snapshots with evidence-bound metadata
  name: Backwork Certified Releases API
  slug: backworkhealth-com-certified-releases-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Claim validation and denial-risk scoring
  name: Backwork Claims API
  slug: backworkhealth-com-claims-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Medical code lookup (CPT, HCPCS, ICD-10)
  name: Backwork Codes API
  slug: backworkhealth-com-codes-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Policy change review and acknowledgment workflow
  name: Backwork Compliance API
  slug: backworkhealth-com-compliance-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Coverage criteria search and evaluation
  name: Backwork Coverage API
  slug: backworkhealth-com-coverage-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Drug formulary and pharmacy benefit evidence
  name: Backwork Drugs API
  slug: backworkhealth-com-drugs-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: API health and status endpoints
  name: Backwork Health API
  slug: backworkhealth-com-health-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Coverage policy search, retrieval, and comparison
  name: Backwork Policies API
  slug: backworkhealth-com-policies-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Prior authorization requirements, research, and readiness
  name: Backwork Prior Auth API
  slug: backworkhealth-com-prior-auth-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Reference data (jurisdictions, payers)
  name: Backwork Reference API
  slug: backworkhealth-com-reference-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Medicare spending and utilization by billing code
  name: Backwork Spending API
  slug: backworkhealth-com-spending-api
- baseURL: https://backworkhealth.com/api/v1
  baseurl_source: declared
  description: Webhook endpoint management and delivery testing
  name: Backwork Webhooks API
  slug: backworkhealth-com-webhooks-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/backworkhealth-com/agentic-access/backworkhealth-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/backworkhealth-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/backworkhealth-com/rate-limits/backworkhealth-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/backworkhealth-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/backworkhealth-com/plans/backworkhealth-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/backworkhealth-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/backworkhealth-com/rules/backworkhealth-com-rules.yml
  title: ''
  type: Spectral
  url: rules/backworkhealth-com-rules.yml
- group: design
  href: https://artifacts.apis.io/backworkhealth-com/json-ld/backworkhealth-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/backworkhealth-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/backworkhealth-com/vocabulary/backworkhealth-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/backworkhealth-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/backworkhealth-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/backworkhealth-com/data-model/backworkhealth-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/backworkhealth-com-data-model.yml
- group: start
  href: https://artifacts.apis.io/backworkhealth-com/sandbox/backworkhealth-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/backworkhealth-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/backworkhealth-com/authentication/backworkhealth-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/backworkhealth-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/backworkhealth-com/errors/backworkhealth-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/backworkhealth-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/backworkhealth-com/conformance/backworkhealth-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backworkhealth-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/backworkhealth-com/llms/backworkhealth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backworkhealth-com-llms.txt
- group: build
  href: https://artifacts.apis.io/backworkhealth-com/mcp/backworkhealth-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/backworkhealth-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/backworkhealth-com/mcp/backworkhealth-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backworkhealth-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/backworkhealth-com/well-known/backworkhealth-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backworkhealth-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/backworkhealth-com/hosts/backworkhealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backworkhealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backworkhealth-com/vendors/backworkhealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backworkhealth-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backworkhealth.com/terms
- group: operate
  title: ''
  type: Support
  url: https://backworkhealth.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backworkhealth.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://backworkhealth.com/sign-up
- group: start
  title: ''
  type: GettingStarted
  url: https://backworkhealth.com/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.backworkhealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.backworkhealth.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/backworkhealth-com/security/backworkhealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backworkhealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backworkhealth.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://backworkhealth.com/openapi.json
  - status: 401
    url: https://backworkhealth.com/mcp
  - status: 200
    url: https://backworkhealth.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Backwork provides a research platform for Medicare and commercial payer coverage policies, prior authorization requirements, and policy changes. It helps billing, revenue cycle, and compliance teams locate documentation requirements, compare policy evidence, and verify coverage details without exposing patient information.
image: https://backworkhealth.com/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Fbackwork-policy-research.3mz42ok1pl178.png&w=3840&q=90
json_schemas:
- name: ClaimValidationResult
  property_count: 23
  slug: backworkhealth-com-claim-validation-result
- name: CoverageEvaluation
  property_count: 10
  slug: backworkhealth-com-coverage-evaluation
- name: CriteriaSearchResult
  property_count: 16
  slug: backworkhealth-com-criteria-search-result
- name: PolicyDetail
  property_count: 36
  slug: backworkhealth-com-policy-detail
- name: PolicyListItem
  property_count: 23
  slug: backworkhealth-com-policy-list-item
- name: PriorAuthCheck
  property_count: 19
  slug: backworkhealth-com-prior-auth-check
jsonld:
- class_count: 71
  name: Backworkhealth Com Context
  property_count: 302
  slug: backworkhealth-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at backworkhealth.com requiring an API key.
  name: Backwork MCP Server
  slug: backworkhealth-com-mcp-yml
modified: '2026-11-02'
name: Backwork
nav: Providers
network: true
overview: 'Backwork publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Tools API, Certified Releases API, Claims API, and 10 more. Tagged areas include Healthcare, Insurance, Policy, Medicare, and Compliance.


  The Backwork catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Backwork''s developer surface includes sandbox, authentication, support, signup flow, getting-started guide, documentation, API reference, and 20 more developer resources.'
plans:
- name: Backworkhealth Com Plans Pricing
  plan_count: 3
  slug: backworkhealth-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Backworkhealth Com Rate Limits
  slug: backworkhealth-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Backwork API Rules
  rule_count: 70
  severity_counts:
    error: 55
    hint: 0
    info: 4
    warn: 11
  slug: backworkhealth-com-rules
scopes:
- name: Backworkhealth Com Scopes
  scope_count: 0
  slug: backworkhealth-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 67.3
    developer_ergonomics: 42.1
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backworkhealth Com Authentication
  slug: backworkhealth-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Backworkhealth Com Domain Security
  slug: backworkhealth-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 5
skills:
- name: acknowledge-policy-change
  slug: backworkhealth-com-acknowledge-policy-change
- name: check-coverage
  slug: backworkhealth-com-check-coverage
- name: check-updates
  slug: backworkhealth-com-check-updates
- name: find-policies
  slug: backworkhealth-com-find-policies
- name: validate-claim
  slug: backworkhealth-com-validate-claim
slug: backworkhealth-com
tags:
- Healthcare
- Insurance
- Policy
- Medicare
- Compliance
website: https://backworkhealth.com/
---
