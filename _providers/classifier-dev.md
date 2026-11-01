---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Classifier Dev Agentic Access
  operation_count: 30
  slug: classifier-dev-agentic-access
  summary_line: 30 operations · 15 acting
api_count: 1
apis:
- baseURL: https://classifier.dev
  baseurl_source: declared
  description: Workspace balance and usage; requires a workspace API key and enabled account access.
  name: classifier-dev Account API
  slug: classifier-dev-account-api
- baseURL: https://classifier.dev
  baseurl_source: declared
  description: The Classifier.dev API from classifier-dev — 2 operation(s) for classifier.dev.
  name: classifier-dev Classifier.dev API
  slug: classifier-dev-classifier-dev-api
- baseURL: https://classifier.dev
  baseurl_source: declared
  description: Sort texts into labels, with a calibrated confidence.
  name: classifier-dev Classify API
  slug: classifier-dev-classify-api
- baseURL: https://classifier.dev
  baseurl_source: declared
  description: Documentation served over HTTP.
  name: classifier-dev Docs API
  slug: classifier-dev-docs-api
- baseURL: https://classifier.dev
  baseurl_source: declared
  description: 'Structured feedback from agents (feedback.now protocol): submit, then poll a receipt.'
  name: classifier-dev Feedback API
  slug: classifier-dev-feedback-api
- baseURL: https://classifier.dev
  baseurl_source: declared
  description: The Subscribe API from classifier-dev — 2 operation(s) for subscribe.
  name: classifier-dev Subscribe API
  slug: classifier-dev-subscribe-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/classifier-dev/agentic-access/classifier-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/classifier-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/classifier-dev/rate-limits/classifier-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/classifier-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/classifier-dev/plans/classifier-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/classifier-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/classifier-dev/rules/classifier-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/classifier-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/classifier-dev/json-ld/classifier-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/classifier-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/classifier-dev/vocabulary/classifier-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/classifier-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/classifier-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/classifier-dev/data-model/classifier-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/classifier-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/classifier-dev/cli/classifier-dev-cli.yml
  title: ''
  type: CLI
  url: cli/classifier-dev-cli.yml
- group: auth
  href: https://artifacts.apis.io/classifier-dev/security/classifier-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/classifier-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/classifier-dev/authentication/classifier-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/classifier-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/classifier-dev/errors/classifier-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/classifier-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/classifier-dev/conformance/classifier-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/classifier-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/classifier-dev/llms/classifier-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/classifier-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/classifier-dev/a2a/classifier-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/classifier-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/classifier-dev/mcp/classifier-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/classifier-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/classifier-dev/mcp/classifier-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/classifier-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/classifier-dev/well-known/classifier-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/classifier-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/classifier-dev/well-known/classifier-dev-cal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/classifier-dev-cal-security.txt
- group: agent
  href: https://artifacts.apis.io/classifier-dev/well-known/classifier-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/classifier-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/classifier-dev/hosts/classifier-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/classifier-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/classifier-dev/vendors/classifier-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/classifier-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/classifier-dev/packages/classifier-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/classifier-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/classifier-dev/packages/classifier-dev-packages.yml
  title: ''
  type: Packages
  url: packages/classifier-dev-packages.yml
- group: start
  title: ''
  type: Login
  url: https://classifier.dev/login
- group: start
  title: ''
  type: GettingStarted
  url: https://classifier.dev/mcp-setup
- group: auth
  href: https://artifacts.apis.io/classifier-dev/security/classifier-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/classifier-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/classifier-dev/security/classifier-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/classifier-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://classifier.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://classifier.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://classifier.dev/developers
- group: docs
  title: ''
  type: APIReference
  url: https://classifier.dev/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://classifier.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://classifier.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://classifier.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mrmps
created: '2026-10-29'
description: classifier.dev provides a zero‑shot text classification API over plain HTTP. Users can submit raw text, URLs, or structured questions and receive classification labels without any API key, account, or authentication. The service offers a free tier with per‑IP limits and paid plans for higher usage, workspace keys, and billing. An OpenAPI 3.1 description is available at /openapi.json and a short index at /llms.txt. Documentation and developer resources are at /developers, pricing at /pricing, terms at /terms, and privacy at /privacy. The platform supports data‑sharing opt‑out via request parameters or headers. Hosted at classifier.dev with source linked to a GitHub organization.
image: https://classifier.dev/favicon.ico
json_schemas:
- name: ClassifyRequest
  property_count: 14
  slug: classifier-dev-classify-request
- name: ClassifyResponse
  property_count: 7
  slug: classifier-dev-classify-response
- name: FeedbackReport
  property_count: 5
  slug: classifier-dev-feedback-report
- name: SingleResult
  property_count: 12
  slug: classifier-dev-single-result
- name: TypeSafeSystemOneRequest
  property_count: 6
  slug: classifier-dev-type-safe-system-one-request
- name: TypeSafeSystemOneResponse
  property_count: 3
  slug: classifier-dev-type-safe-system-one-response
jsonld:
- class_count: 22
  name: Classifier Dev Context
  property_count: 122
  slug: classifier-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at classifier.dev.
  name: classifier-dev MCP Server
  slug: classifier-dev-mcp-yml
modified: '2026-10-29'
name: classifier-dev
nav: Providers
network: true
overview: 'classifier-dev publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Classifier.dev API, Classify API, and 3 more. Tagged areas include Company, Machine Learning, NLP, Classification, and API.


  The classifier-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  classifier-dev''s developer surface includes CLI, authentication, getting-started guide, documentation, API reference, pricing, and 30 more developer resources.'
plans:
- name: Classifier Dev Plans Pricing
  plan_count: 5
  slug: classifier-dev-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Classifier Dev Rate Limits
  slug: classifier-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: classifier-dev API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 3
  slug: classifier-dev-rules
scopes:
- name: Classifier Dev Scopes
  scope_count: 0
  slug: classifier-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 66.4
    developer_ergonomics: 70.7
    discoverability: 65.0
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Classifier Dev Authentication
  slug: classifier-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Classifier Dev Domain Security
  slug: classifier-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Classifier Dev Vulnerability Disclosure
  slug: classifier-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: classifier-dev-classify
  slug: classifier-dev-classify
slug: classifier-dev
tags:
- Company
- Machine Learning
- NLP
- Classification
- API
- OpenAPI
website: https://classifier.dev/
---
