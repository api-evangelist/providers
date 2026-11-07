---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Verifly Email Agentic Access
  operation_count: 30
  slug: verifly-email-agentic-access
  summary_line: 30 operations · 15 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Account profile, credits, usage, and API key management.
  name: verifly-email Account API
  slug: verifly-email-account-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Credit packages and Stripe / crypto checkout. Agent-native crypto pay.
  name: verifly-email Billing API
  slug: verifly-email-billing-api
- baseURL: https://verifly.email/api/v1
  baseurl_source: declared
  description: The Clean API from verifly-email — 1 operation(s) for clean.
  name: verifly-email Clean API
  slug: verifly-email-clean-api
- baseURL: https://verifly.email/api/v1
  baseurl_source: declared
  description: The Extract API from verifly-email — 1 operation(s) for extract.
  name: verifly-email Extract API
  slug: verifly-email-extract-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Saved file storage for cleaned/verified lists, with raw download.
  name: verifly-email Files API
  slug: verifly-email-files-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Asynchronous bulk verification job lifecycle (status, results, download, process).
  name: verifly-email Jobs API
  slug: verifly-email-jobs-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Email list cleaning and extraction utilities (no mailbox verification).
  name: verifly-email List Cleaning API
  slug: verifly-email-list-cleaning-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Self-service agent registration. Get a first API key + free credits with no human.
  name: verifly-email Onboarding API
  slug: verifly-email-onboarding-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Public utility endpoints such as domain DNS health.
  name: verifly-email Tools API
  slug: verifly-email-tools-api
- baseURL: https://verifly.email
  baseurl_source: declared
  description: Single, batch, and asynchronous bulk email verification.
  name: verifly-email Verification API
  slug: verifly-email-verification-api
- baseURL: https://verifly.email/api/v1
  baseurl_source: declared
  description: The Verify API from verifly-email — 2 operation(s) for verify.
  name: verifly-email Verify API
  slug: verifly-email-verify-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/verifly-email/agentic-access/verifly-email-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/verifly-email-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/verifly-email/plans/verifly-email-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/verifly-email-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/verifly-email/rules/verifly-email-rules.yml
  title: ''
  type: Spectral
  url: rules/verifly-email-rules.yml
- group: design
  href: https://artifacts.apis.io/verifly-email/json-ld/verifly-email-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/verifly-email-context.jsonld
- group: design
  href: https://artifacts.apis.io/verifly-email/vocabulary/verifly-email-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/verifly-email-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/verifly-email/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/verifly-email/data-model/verifly-email-data-model.yml
  title: ''
  type: DataModel
  url: data-model/verifly-email-data-model.yml
- group: operate
  href: https://artifacts.apis.io/verifly-email/changelog/verifly-email-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/verifly-email-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://verifly.email/security
- group: design
  href: https://artifacts.apis.io/verifly-email/errors/verifly-email-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/verifly-email-problem-types.yml
- group: design
  href: https://artifacts.apis.io/verifly-email/conformance/verifly-email-conformance.yml
  title: ''
  type: Conformance
  url: conformance/verifly-email-conformance.yml
- group: agent
  href: https://artifacts.apis.io/verifly-email/llms/verifly-email-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verifly-email-llms.txt
- group: build
  href: https://artifacts.apis.io/verifly-email/mcp/verifly-email-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/verifly-email-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/verifly-email/mcp/verifly-email-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/verifly-email-mcp.yml
- group: agent
  href: https://artifacts.apis.io/verifly-email/well-known/verifly-email-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/verifly-email-well-known.yml
- group: other
  href: https://artifacts.apis.io/verifly-email/hosts/verifly-email-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verifly-email-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://verifly.email/status
- group: auth
  title: ''
  type: Security
  url: https://verifly.email/security
- group: commercial
  title: ''
  type: Pricing
  url: https://verifly.email/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://verifly.email/changelog
- group: auth
  href: https://artifacts.apis.io/verifly-email/security/verifly-email-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/verifly-email-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/verifly-email/security/verifly-email-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verifly-email-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verifly.email/
- group: docs
  title: ''
  type: Documentation
  url: https://verifly.email/docs
- group: docs
  title: ''
  type: APIReference
  url: https://verifly.email/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://verifly.email/docs
- group: company
  title: ''
  type: Blog
  url: https://verifly.email/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verifly.email/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verifly.email/privacy
- group: start
  title: ''
  type: SignUp
  url: https://verifly.email/register
created: '2026-10-31'
description: Fast, accurate email verification API, single, batch, and async bulk verification (up to 1M) with disposable detection, role filtering, catch-all and SMTP checks, plus a native MCP server for AI agents. Pay-as-you-go, credits never expire.
image: https://verifly.email/favicon.svg
json_schemas:
- name: DomainHealthResult
  property_count: 8
  slug: verifly-email-domain-health-result
- name: EmailBatch
  property_count: 1
  slug: verifly-email-email-batch
- name: ExtractRequest
  property_count: 2
  slug: verifly-email-extract-request
- name: FileProcessRequest
  property_count: 3
  slug: verifly-email-file-process-request
- name: FileProcessResult
  property_count: 6
  slug: verifly-email-file-process-result
- name: Job
  property_count: 14
  slug: verifly-email-job
- name: UsageResult
  property_count: 7
  slug: verifly-email-usage-result
- name: VerificationResult
  property_count: 10
  slug: verifly-email-verification-result
jsonld:
- class_count: 48
  name: Verifly Email Context
  property_count: 128
  slug: verifly-email-context
layout: provider
mcp_servers:
- description: Remote MCP server at verifly.email.
  name: verifly-email MCP Server
  slug: verifly-email-mcp-yml
modified: '2026-10-31'
name: verifly-email
nav: Providers
network: true
overview: 'verifly-email publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Clean API, and 8 more. Tagged areas include Email Verification, MCP, Developer Tools, Verification, and Company.


  The verifly-email catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  verifly-email''s developer surface includes changelog, pricing, documentation, API reference, getting-started guide, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Verifly Email Plans Pricing
  plan_count: 1
  slug: verifly-email-plans-pricing
- name: Verifly Email Plans
  plan_count: 1
  slug: verifly-email-plans
random_paper: 14
rate_limits:
- limit_count: 0
  name: Verifly Email Rate Limits
  slug: verifly-email-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: verifly-email API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: verifly-email-rules
scopes:
- name: Verifly Email Scopes
  scope_count: 0
  slug: verifly-email-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 66.5
    developer_ergonomics: 21.9
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Verifly Email Authentication
  slug: verifly-email-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Verifly Email Domain Security
  slug: verifly-email-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Verifly Email Trust Center
  slug: verifly-email-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: email-verification
  slug: verifly-email-email-verification
slug: verifly-email
tags:
- Email Verification
- MCP
- Developer Tools
- Verification
- Company
website: https://verifly.email/
---
