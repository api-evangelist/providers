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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 148
  human_in_the_loop: 12
  name: Hydracept Com Agentic Access
  operation_count: 270
  slug: hydracept-com-agentic-access
  summary_line: 270 operations · 148 acting · 12 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.hydracept.com
  baseurl_source: declared
  description: The public_api API from hydracept-com — 115 operation(s) for public_api.
  name: hydracept-com Public API
  slug: hydracept-com-public-api-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/hydracept-com/agentic-access/hydracept-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hydracept-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/hydracept-com/plans/hydracept-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hydracept-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/rules/hydracept-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hydracept-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/json-ld/hydracept-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hydracept-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/hydracept-com/vocabulary/hydracept-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hydracept-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hydracept-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/data-model/hydracept-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hydracept-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/hydracept-com/cli/hydracept-com-cli.yml
  title: ''
  type: CLI
  url: cli/hydracept-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/hydracept-com/changelog/hydracept-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hydracept-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/conventions/hydracept-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hydracept-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/conventions/hydracept-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hydracept-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hydracept.com/trust
- group: auth
  href: https://artifacts.apis.io/hydracept-com/security/hydracept-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/hydracept-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hydracept-com/authentication/hydracept-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hydracept-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/lifecycle/hydracept-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hydracept-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/errors/hydracept-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hydracept-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hydracept-com/conformance/hydracept-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hydracept-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hydracept-com/llms/hydracept-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hydracept-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/hydracept-com/mcp/hydracept-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hydracept-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/hydracept-com/well-known/hydracept-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hydracept-com-security.txt
- group: agent
  href: https://artifacts.apis.io/hydracept-com/well-known/hydracept-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hydracept-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hydracept-com/hosts/hydracept-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hydracept-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hydracept-com/vendors/hydracept-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hydracept-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/hydracept-com/packages/hydracept-com-packages.yml
  title: ''
  type: SDKs
  url: packages/hydracept-com-packages.yml
- group: build
  href: https://artifacts.apis.io/hydracept-com/packages/hydracept-com-packages.yml
  title: ''
  type: Packages
  url: packages/hydracept-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://hydracept.com/changelog/
- group: auth
  href: https://artifacts.apis.io/hydracept-com/security/hydracept-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hydracept-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hydracept-com/security/hydracept-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hydracept-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hydracept-com/security/hydracept-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hydracept-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hydracept.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hydracept.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hydracept.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hydracept.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydracept.com/privacy.html
- group: start
  title: ''
  type: SignUp
  url: https://hydracept.com/start
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hydracept.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hydracept.com/terms.html
- group: docs
  title: ''
  type: APIReference
  url: https://hydracept.com/openapi/hydracept-v1.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zencodeinc
created: '2026-10-30'
description: Run external AI capabilities from one API—for software teams and coding agents. Durable jobs, artifacts, execution receipts, BYOK, and managed billing. Eligible durable text jobs run at 50% of standard token rates.
image: https://hydracept.com/og-card.png
json_schemas:
- name: CapabilityInvokeRequest
  property_count: 19
  slug: hydracept-com-capability-invoke-request
- name: CapabilityJobRequest
  property_count: 18
  slug: hydracept-com-capability-job-request
- name: HydraceptInvocationResult
  property_count: 22
  slug: hydracept-com-hydracept-invocation-result
- name: HydraceptJob
  property_count: 28
  slug: hydracept-com-hydracept-job
- name: HydraceptReceipt
  property_count: 27
  slug: hydracept-com-hydracept-receipt
- name: PublicCapabilityDescriptor
  property_count: 27
  slug: hydracept-com-public-capability-descriptor
jsonld:
- class_count: 120
  name: Hydracept Com Context
  property_count: 373
  slug: hydracept-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.hydracept.com.
  name: hydracept-com MCP Server
  slug: hydracept-com-mcp-yml
modified: '2026-10-30'
name: hydracept-com
nav: Providers
network: true
overview: 'hydracept-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Artificial Intelligence, ExternalCapabilities, DurableJobs, and Billing.


  The hydracept-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  hydracept-com''s developer surface includes CLI, changelog, authentication, documentation, getting-started guide, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Hydracept Com Plans Pricing
  plan_count: 4
  slug: hydracept-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Hydracept Com Rate Limits
  slug: hydracept-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: hydracept-com API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: hydracept-com-rules
scopes:
- name: Hydracept Com Scopes
  scope_count: 0
  slug: hydracept-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 60.7
    developer_ergonomics: 42.3
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hydracept-com/hydracept-com-2026-11-03T133545.png
security:
- kind: authentication
  name: Hydracept Com Authentication
  slug: hydracept-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hydracept Com Domain Security
  slug: hydracept-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hydracept Com Vulnerability Disclosure
  slug: hydracept-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Hydracept Com Trust Center
  slug: hydracept-com-trust-center
  summary_line: SOC 2
skill_count: 1
skills:
- name: list-aliases
  slug: hydracept-com-list-aliases
slug: hydracept-com
tags:
- Company
- Artificial Intelligence
- ExternalCapabilities
- DurableJobs
- Billing
website: https://hydracept.com/
---
