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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Apisign Io Agentic Access
  operation_count: 35
  slug: apisign-io-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 1
apis:
- baseURL: https://apisign.io/api
  baseurl_source: declared
  description: Manage API keys
  name: APISign API Keys API
  slug: apisign-io-api-keys-api
- baseURL: https://apisign.io/api
  baseurl_source: declared
  description: Create, manage, and track contracts
  name: APISign Contracts API
  slug: apisign-io-contracts-api
- baseURL: https://apisign.io/api
  baseurl_source: declared
  description: Unauthenticated service checks
  name: APISign Health API
  slug: apisign-io-health-api
- baseURL: https://apisign.io/api
  baseurl_source: declared
  description: Organization details and audit trail
  name: APISign Organization API
  slug: apisign-io-organization-api
- baseURL: https://apisign.io/api
  baseurl_source: declared
  description: Manage reusable contract templates
  name: APISign Templates API
  slug: apisign-io-templates-api
- baseURL: https://apisign.io/api
  baseurl_source: declared
  description: Configure webhook endpoints for events
  name: APISign Webhooks API
  slug: apisign-io-webhooks-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/apisign-io/agentic-access/apisign-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apisign-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/apisign-io/plans/apisign-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apisign-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apisign-io/rules/apisign-io-rules.yml
  title: ''
  type: Spectral
  url: rules/apisign-io-rules.yml
- group: design
  href: https://artifacts.apis.io/apisign-io/json-ld/apisign-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apisign-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/apisign-io/vocabulary/apisign-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apisign-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apisign-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apisign-io/data-model/apisign-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apisign-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/apisign-io/cli/apisign-io-cli.yml
  title: ''
  type: CLI
  url: cli/apisign-io-cli.yml
- group: auth
  href: https://artifacts.apis.io/apisign-io/authentication/apisign-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apisign-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/apisign-io/errors/apisign-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apisign-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apisign-io/conformance/apisign-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apisign-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apisign-io/llms/apisign-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apisign-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/apisign-io/well-known/apisign-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apisign-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/apisign-io/hosts/apisign-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apisign-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/apisign-io/packages/apisign-io-packages.yml
  title: ''
  type: SDKs
  url: packages/apisign-io-packages.yml
- group: build
  href: https://artifacts.apis.io/apisign-io/packages/apisign-io-packages.yml
  title: ''
  type: Packages
  url: packages/apisign-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apisign.io/terms
- group: operate
  title: ''
  type: Support
  url: https://apisign.io/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apisign.io/privacy
- group: auth
  href: https://artifacts.apis.io/apisign-io/security/apisign-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apisign-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apisign.io/
- group: docs
  title: ''
  type: Documentation
  url: https://apisign.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apisign.io/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apisign.io/docs
- group: company
  title: ''
  type: Blog
  url: https://apisign.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://apisign.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apisign.io/register
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://apisign.io/mcp
  - status: 200
    url: https://apisign.io/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: APISign provides a pay‑per‑contract e‑signature service tailored for AI agents and developers. It offers an MCP server, a REST API and a CLI that let agents draft contracts, send them for legally binding signatures, and track the signing process. Pricing is $0.25 per contract with 20 free contracts to start and no monthly fees. The platform supports Markdown and Word documents, returns sealed PDFs, and includes audit logs for compliance.
image: https://apisign.io/android-chrome-512x512.png
json_schemas:
- name: ContractAuditLog
  property_count: 14
  slug: apisign-io-contract-audit-log
- name: Contract
  property_count: 18
  slug: apisign-io-contract
- name: CreateContractRequest
  property_count: 9
  slug: apisign-io-create-contract-request
- name: Organization
  property_count: 13
  slug: apisign-io-organization
- name: UpdateContractRequest
  property_count: 8
  slug: apisign-io-update-contract-request
- name: VerificationResult
  property_count: 6
  slug: apisign-io-verification-result
jsonld:
- class_count: 30
  name: Apisign Io Context
  property_count: 92
  slug: apisign-io-context
layout: provider
modified: '2026-11-01'
name: APISign
nav: Providers
network: true
overview: 'APISign publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Contracts API, Health API, and 3 more. Tagged areas include E-Signature, Artificial Intelligence, MCP, Contracts, and Developer Platform.


  The APISign catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APISign''s developer surface includes CLI, authentication, support, documentation, API reference, getting-started guide, engineering blog, and 20 more developer resources.'
plans:
- name: Apisign Io Plans Pricing
  plan_count: 1
  slug: apisign-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Apisign Io Rate Limits
  slug: apisign-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: APISign API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: apisign-io-rules
scopes:
- name: Apisign Io Scopes
  scope_count: 0
  slug: apisign-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 63.7
    developer_ergonomics: 50.5
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 54.5
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apisign Io Authentication
  slug: apisign-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apisign Io Domain Security
  slug: apisign-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: create-contract
  slug: apisign-io-create-contract
- name: list-templates
  slug: apisign-io-list-templates
slug: apisign-io
tags:
- E-Signature
- Artificial Intelligence
- MCP
- Contracts
- Developer Platform
website: https://apisign.io/
---
