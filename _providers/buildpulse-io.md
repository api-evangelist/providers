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
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Buildpulse Io Agentic Access
  operation_count: 13
  slug: buildpulse-io-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 1
apis:
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: 'Token validation and caller identity. Send an API token as `Authorization: Bearer bp_<64-hex>` (or `Authorization: token …`). Tokens are created under Organization Settings → API Tokens and shown once'
  name: BuildPulse Auth API
  slug: buildpulse-io-auth-api
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: SVG status badges (flakiness, coverage).
  name: BuildPulse Badges API
  slug: buildpulse-io-badges-api
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: Cross-repo flaky test inventory with optional field expansion.
  name: BuildPulse Flaky API
  slug: buildpulse-io-flaky-api
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: Service health checks (unauthenticated).
  name: BuildPulse Health API
  slug: buildpulse-io-health-api
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: Test result sets (a.k.a. submissions) — one per CI run.
  name: BuildPulse Submissions API
  slug: buildpulse-io-submissions-api
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: Disruptive / flaky tests per repository.
  name: BuildPulse Tests API
  slug: buildpulse-io-tests-api
- baseURL: https://platform.buildpulse.io
  baseurl_source: declared
  description: GitHub App webhook ingress (HMAC-verified; not a customer-callable endpoint).
  name: BuildPulse Webhooks API
  slug: buildpulse-io-webhooks-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/buildpulse-io/agentic-access/buildpulse-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buildpulse-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/buildpulse-io/plans/buildpulse-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildpulse-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildpulse-io/rules/buildpulse-io-rules.yml
  title: ''
  type: Spectral
  url: rules/buildpulse-io-rules.yml
- group: design
  href: https://artifacts.apis.io/buildpulse-io/json-ld/buildpulse-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildpulse-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildpulse-io/vocabulary/buildpulse-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildpulse-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buildpulse-io/data-model/buildpulse-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildpulse-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/buildpulse-io/changelog/buildpulse-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/buildpulse-io-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://buildpulse.io/security
- group: design
  href: https://artifacts.apis.io/buildpulse-io/errors/buildpulse-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildpulse-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buildpulse-io/conformance/buildpulse-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildpulse-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buildpulse-io/llms/buildpulse-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildpulse-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildpulse-io/mcp/buildpulse-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buildpulse-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/buildpulse-io/well-known/buildpulse-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buildpulse-io-security.txt
- group: auth
  href: https://artifacts.apis.io/buildpulse-io/well-known/buildpulse-io-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buildpulse-io-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/buildpulse-io/well-known/buildpulse-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildpulse-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildpulse-io/hosts/buildpulse-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildpulse-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildpulse-io/vendors/buildpulse-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildpulse-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/buildpulse-io/packages/buildpulse-io-packages.yml
  title: ''
  type: SDKs
  url: packages/buildpulse-io-packages.yml
- group: build
  href: https://artifacts.apis.io/buildpulse-io/packages/buildpulse-io-packages.yml
  title: ''
  type: Packages
  url: packages/buildpulse-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildpulse.io/terms
- group: auth
  title: ''
  type: Security
  url: https://buildpulse.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildpulse.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://buildpulse.io/pricing
- group: start
  title: ''
  type: Login
  url: https://buildpulse.io/auth/login
- group: company
  title: ''
  type: Blog
  url: https://buildpulse.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.buildpulse.io/docs/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://dev.buildpulse.io/
- group: docs
  title: ''
  type: APIReference
  url: https://platform.buildpulse.io/docs/
- group: auth
  href: https://artifacts.apis.io/buildpulse-io/authentication/buildpulse-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildpulse-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/buildpulse-io/security/buildpulse-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/buildpulse-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/buildpulse-io/security/buildpulse-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildpulse-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buildpulse-io/security/buildpulse-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildpulse-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildpulse.io/
created: '2026-11-03'
description: BuildPulse helps engineering teams ship faster on GitHub Actions by providing test analytics, faster runners, and AI code review. It detects flaky tests, quarantines them, and offers performance insights, serving customers like Replit and Auditboard.
image: https://buildpulse.io/opengraph-image?4b78022c15b08514
json_schemas:
- name: FlakyTestsResponse
  property_count: 3
  slug: buildpulse-io-flaky-tests-response
- name: HealthResponse
  property_count: 1
  slug: buildpulse-io-health-response
- name: SubmissionTestsResponse
  property_count: 3
  slug: buildpulse-io-submission-tests-response
- name: SubmissionsResponse
  property_count: 3
  slug: buildpulse-io-submissions-response
- name: TestResultsResponse
  property_count: 1
  slug: buildpulse-io-test-results-response
- name: TestsResponse
  property_count: 3
  slug: buildpulse-io-tests-response
jsonld:
- class_count: 16
  name: Buildpulse Io Context
  property_count: 47
  slug: buildpulse-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.buildpulse.io requiring OAuth.
  name: BuildPulse MCP Server
  slug: buildpulse-io-mcp-yml
modified: '2026-11-03'
name: BuildPulse
nav: Providers
network: true
overview: 'BuildPulse publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Badges API, Flaky API, and 4 more. Tagged areas include CI, DevOps, Testing, Artificial Intelligence, and Analytics.


  The BuildPulse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuildPulse''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, API reference, authentication, and 26 more developer resources.'
plans:
- name: Buildpulse Io Plans Pricing
  plan_count: 4
  slug: buildpulse-io-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: BuildPulse API Rules
  rule_count: 71
  severity_counts:
    error: 66
    hint: 0
    info: 2
    warn: 3
  slug: buildpulse-io-rules
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 67.5
    developer_ergonomics: 34.5
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buildpulse Io Authentication
  slug: buildpulse-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Buildpulse Io Domain Security
  slug: buildpulse-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Buildpulse Io Vulnerability Disclosure
  slug: buildpulse-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Buildpulse Io Trust Center
  slug: buildpulse-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: buildpulse-io
tags:
- CI
- DevOps
- Testing
- Artificial Intelligence
- Analytics
- Company
website: https://buildpulse.io/
---
