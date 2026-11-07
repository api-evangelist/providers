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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 4
  name: Past Dev Agentic Access
  operation_count: 68
  slug: past-dev-agentic-access
  summary_line: 68 operations · 36 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Create and manage the audiences that scope data points.
  name: past-dev Audiences API
  slug: past-dev-audiences-api
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Read what the platform did with what you sent, and what it costs.
  name: past-dev Debugging API
  slug: past-dev-debugging-api
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Manage customer-owned identities and traits.
  name: past-dev Identities API
  slug: past-dev-identities-api
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Accept, observe, and forget source data.
  name: past-dev Ingestion API
  slug: past-dev-ingestion-api
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Projects and project keys, with the management key.
  name: past-dev Management API
  slug: past-dev-management-api
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Retrieve ranked memory documents.
  name: past-dev Recall API
  slug: past-dev-recall-api
- baseURL: https://api.past.dev
  baseurl_source: declared
  description: Receive events from another system on a URL the console issues.
  name: past-dev Webhooks API
  slug: past-dev-webhooks-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/past-dev/agentic-access/past-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/past-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/past-dev/plans/past-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/past-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/past-dev/rules/past-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/past-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/past-dev/json-ld/past-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/past-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/past-dev/vocabulary/past-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/past-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/past-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/past-dev/data-model/past-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/past-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/past-dev/changelog/past-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/past-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/past-dev/conventions/past-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/past-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/past-dev/conventions/past-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/past-dev-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://past.dev/security
- group: auth
  href: https://artifacts.apis.io/past-dev/authentication/past-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/past-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/past-dev/errors/past-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/past-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/past-dev/conformance/past-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/past-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/past-dev/llms/past-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/past-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/past-dev/mcp/past-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/past-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/past-dev/well-known/past-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/past-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/past-dev/well-known/past-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/past-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/past-dev/hosts/past-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/past-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/past-dev/vendors/past-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/past-dev-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://past.dev/docs/memory-api/api-reference
- group: auth
  href: https://artifacts.apis.io/past-dev/security/past-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/past-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/past-dev/security/past-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/past-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/past-dev/security/past-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/past-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://past.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://past.dev/docs/memory-api/overview
- group: company
  title: ''
  type: Blog
  url: https://past.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://past.dev/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://past.dev/docs/mcp/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pastdotdev
- group: commercial
  title: ''
  type: Pricing
  url: https://past.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://past.dev/privacy
- group: auth
  title: ''
  type: Security
  url: https://past.dev/security
- group: start
  title: ''
  type: SignUp
  url: https://sso.past.dev/sign-up
- group: operate
  title: ''
  type: StatusPage
  url: https://status.past.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://past.dev/terms
created: '2026-10-30'
description: Past.dev provides a cutting‑edge memory API for AI agents, enabling them to store, retrieve, and manage both short‑term and long‑term contextual data. The platform offers robust endpoints for creating, updating, and querying memory objects, with built‑in versioning, access controls, and analytics. Designed for developers building intelligent applications, Past.dev integrates seamlessly with popular AI frameworks and supports scalable workloads. Documentation, SDKs, and example integrations are available to accelerate development and deployment.
image: https://past.dev/og.png?v=ca17a274cec2
json_schemas:
- name: IngestEstimate
  property_count: 12
  slug: past-dev-ingest-estimate
- name: IngestRequest
  property_count: 8
  slug: past-dev-ingest-request
- name: IngestionDiagnosis
  property_count: 12
  slug: past-dev-ingestion-diagnosis
- name: RecallRequest
  property_count: 9
  slug: past-dev-recall-request
- name: TraceNode
  property_count: 19
  slug: past-dev-trace-node
- name: WebhookReceipt
  property_count: 7
  slug: past-dev-webhook-receipt
jsonld:
- class_count: 69
  name: Past Dev Context
  property_count: 173
  slug: past-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at past.dev.
  name: past-dev MCP Server
  slug: past-dev-mcp-yml
modified: '2026-10-30'
name: past-dev
nav: Providers
network: true
overview: 'past-dev publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audiences API, Debugging API, Identities API, and 4 more. Tagged areas include Artificial Intelligence, Memory, Platform, and Developers.


  The past-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  past-dev''s developer surface includes changelog, authentication, API reference, documentation, engineering blog, getting-started guide, pricing, and 29 more developer resources.'
plans:
- name: Past Dev Plans Pricing
  plan_count: 3
  slug: past-dev-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: past-dev API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: past-dev-rules
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.1
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 29.2
    discoverability: 56.7
    operational_transparency: 23.7
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
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
screenshot: https://apis.io/screenshots/past-dev/past-dev-2026-11-03T141151.png
security:
- kind: authentication
  name: Past Dev Authentication
  slug: past-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Past Dev Domain Security
  slug: past-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Past Dev Vulnerability Disclosure
  slug: past-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Past Dev Trust Center
  slug: past-dev-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 3
skills:
- name: past-dev-ingest-single-data-point
  slug: past-dev-ingest-single-data-point
- name: past-dev-management-create-project-with-key
  slug: past-dev-management-create-project-with-key
- name: past-dev-upsert-and-get-identity
  slug: past-dev-upsert-and-get-identity
slug: past-dev
tags:
- Artificial Intelligence
- Memory
- Platform
- Developers
website: https://past.dev/
---
