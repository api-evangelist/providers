---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Inboxpolicy Com Agentic Access
  operation_count: 3
  slug: inboxpolicy-com-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.inboxpolicy.com
  baseurl_source: declared
  description: The Verification API from inboxpolicy-com — 3 operation(s) for verification.
  name: inboxpolicy-com Verification API
  slug: inboxpolicy-com-verification-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/inboxpolicy-com/agentic-access/inboxpolicy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inboxpolicy-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/inboxpolicy-com/plans/inboxpolicy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inboxpolicy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/inboxpolicy-com/rules/inboxpolicy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/inboxpolicy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/inboxpolicy-com/vocabulary/inboxpolicy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inboxpolicy-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/inboxpolicy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/inboxpolicy-com/errors/inboxpolicy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inboxpolicy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/inboxpolicy-com/conformance/inboxpolicy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inboxpolicy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/inboxpolicy-com/llms/inboxpolicy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inboxpolicy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/inboxpolicy-com/hosts/inboxpolicy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inboxpolicy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/inboxpolicy-com/vendors/inboxpolicy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inboxpolicy-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inboxpolicy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inboxpolicy.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://inboxpolicy.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://inboxpolicy.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.inboxpolicy.com</code
- group: auth
  href: https://artifacts.apis.io/inboxpolicy-com/authentication/inboxpolicy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inboxpolicy-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/inboxpolicy-com/security/inboxpolicy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inboxpolicy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inboxpolicy.com/
created: '2026-10-30'
description: InboxPolicy provides a Send-Decision Email Verification API that helps applications determine whether to send an email to a given address. By calling a single endpoint, developers receive a decision (send, review, or avoid), confidence score, and reasoning, enabling cost‑effective email outreach and reducing bounce rates. The service is built for AI agents and integrates via REST and MCP, offering pay‑per‑call pricing and no free tier, with support for USDC payments.
image: https://inboxpolicy.com/og.png
json_schemas:
- name: CaptureSession
  property_count: 6
  slug: inboxpolicy-com-capture-session
- name: Connector
  property_count: 9
  slug: inboxpolicy-com-connector
- name: CreateRunRequest
  property_count: 7
  slug: inboxpolicy-com-create-run-request
- name: CreateSecretRequest
  property_count: 6
  slug: inboxpolicy-com-create-secret-request
- name: File
  property_count: 8
  slug: inboxpolicy-com-file
- name: Run
  property_count: 13
  slug: inboxpolicy-com-run
jsonld:
- class_count: 40
  name: Inboxpolicy Com Context
  property_count: 72
  slug: inboxpolicy-com-context
layout: provider
modified: '2026-10-30'
name: inboxpolicy-com
nav: Providers
network: true
overview: 'inboxpolicy-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Verification API. Tagged areas include Company, Email Verification, Artificial Intelligence, Payments, and Pricing.


  The inboxpolicy-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  inboxpolicy-com''s developer surface includes pricing, documentation, authentication, and 15 more developer resources.'
plans:
- name: Inboxpolicy Com Plans Pricing
  plan_count: 4
  slug: inboxpolicy-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Inboxpolicy Com Rate Limits
  slug: inboxpolicy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: inboxpolicy-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: inboxpolicy-com-rules
scopes:
- name: Inboxpolicy Com Scopes
  scope_count: 0
  slug: inboxpolicy-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 27.9
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/inboxpolicy-com/inboxpolicy-com-2026-11-03T133725.png
security:
- kind: authentication
  name: Inboxpolicy Com Authentication
  slug: inboxpolicy-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Inboxpolicy Com Domain Security
  slug: inboxpolicy-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: inboxpolicy-com-agent
  slug: inboxpolicy-com-agent
- name: batch-verify
  slug: inboxpolicy-com-batch-verify
- name: decide
  slug: inboxpolicy-com-decide
- name: verify
  slug: inboxpolicy-com-verify
slug: inboxpolicy-com
tags:
- Company
- Email Verification
- Artificial Intelligence
- Payments
- Pricing
website: https://inboxpolicy.com/
---
