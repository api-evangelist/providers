---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Citation Co Agentic Access
  operation_count: 47
  slug: citation-co-agentic-access
  summary_line: 47 operations · 26 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Balance API from Citation — 1 operation(s) for balance.
  name: Citation Balance API
  slug: citation-co-balance-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Checks API from Citation — 1 operation(s) for checks.
  name: Citation Checks API
  slug: citation-co-checks-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Documents API from Citation — 17 operation(s) for documents.
  name: Citation Documents API
  slug: citation-co-documents-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Events API from Citation — 1 operation(s) for events.
  name: Citation Events API
  slug: citation-co-events-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Exports API from Citation — 1 operation(s) for exports.
  name: Citation Exports API
  slug: citation-co-exports-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Files API from Citation — 3 operation(s) for files.
  name: Citation Files API
  slug: citation-co-files-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Imports API from Citation — 1 operation(s) for imports.
  name: Citation Imports API
  slug: citation-co-imports-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Jobs API from Citation — 5 operation(s) for jobs.
  name: Citation Jobs API
  slug: citation-co-jobs-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Ledger API from Citation — 1 operation(s) for ledger.
  name: Citation Ledger API
  slug: citation-co-ledger-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Me API from Citation — 1 operation(s) for me.
  name: Citation Me API
  slug: citation-co-me-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Pricing API from Citation — 1 operation(s) for pricing.
  name: Citation Pricing API
  slug: citation-co-pricing-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Sources API from Citation — 1 operation(s) for sources.
  name: Citation Sources API
  slug: citation-co-sources-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Webhooks API from Citation — 3 operation(s) for webhooks.
  name: Citation Webhooks API
  slug: citation-co-webhooks-api
- baseURL: https://citation.co/api/v1
  baseurl_source: declared
  description: The Write API from Citation — 1 operation(s) for write.
  name: Citation Write API
  slug: citation-co-write-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/citation-co/agentic-access/citation-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/citation-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/citation-co/rules/citation-co-rules.yml
  title: ''
  type: Spectral
  url: rules/citation-co-rules.yml
- group: design
  href: https://artifacts.apis.io/citation-co/json-ld/citation-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citation-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/citation-co/vocabulary/citation-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citation-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/citation-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/citation-co/data-model/citation-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citation-co-data-model.yml
- group: build
  href: https://artifacts.apis.io/citation-co/cli/citation-co-cli.yml
  title: ''
  type: CLI
  url: cli/citation-co-cli.yml
- group: design
  href: https://artifacts.apis.io/citation-co/conventions/citation-co-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/citation-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/citation-co/conventions/citation-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/citation-co-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://citation.co/security
- group: auth
  href: https://artifacts.apis.io/citation-co/authentication/citation-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/citation-co-authentication.yml
- group: auth
  href: https://artifacts.apis.io/citation-co/scopes/citation-co-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/citation-co-scopes.yml
- group: design
  href: https://artifacts.apis.io/citation-co/errors/citation-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/citation-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/citation-co/conformance/citation-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citation-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citation-co/llms/citation-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citation-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/citation-co/mcp/citation-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/citation-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/citation-co/well-known/citation-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citation-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/citation-co/hosts/citation-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citation-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/citation-co/vendors/citation-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citation-co-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://citation.co/security
- group: auth
  href: https://artifacts.apis.io/citation-co/security/citation-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/citation-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/citation-co/security/citation-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citation-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citation-co/security/citation-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citation-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citation.co/
- group: docs
  title: ''
  type: Documentation
  url: https://citation.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://citation.co/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://citation.co/docs/start-guide
- group: operate
  title: ''
  type: Support
  url: https://citation.co/contact
- group: company
  title: ''
  type: Blog
  url: https://citation.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citationco
- group: commercial
  title: ''
  type: Pricing
  url: https://citation.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://citation.co/signup
- group: start
  title: ''
  type: Login
  url: https://citation.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citation.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citation.co/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://citation.co/openapi.json
  - status: 401
    url: https://citation.co/mcp
  - status: 200
    url: https://citation.co/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Citation provides a web-based citation generator and writing workspace that supports APA, MLA, Chicago and other citation styles. Users can create citations by entering URLs, DOIs, ISBNs or titles, manage sources, organize research files, and export bibliographies. The platform offers a free tier with usage limits and paid plans for higher allowances, and includes AI‑assisted suggestions and source verification.
image: https://citation.co/opengraph-image.jpg
json_schemas:
- name: CheckReview
  property_count: 3
  slug: citation-co-check-review
- name: Connection
  property_count: 6
  slug: citation-co-connection
- name: context
  property_count: 2
  slug: citation-co-context
- name: Job
  property_count: 11
  slug: citation-co-job
- name: write
  property_count: 15
  slug: citation-co-write
- name: WritingContext
  property_count: 2
  slug: citation-co-writing-context
jsonld:
- class_count: 56
  name: Citation Co Context
  property_count: 109
  slug: citation-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at citation.co.
  name: Citation MCP Server
  slug: citation-co-mcp-yml
modified: '2026-10-30'
name: Citation
nav: Providers
network: true
overview: 'Citation publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Checks API, Documents API, and 11 more. Tagged areas include Citation, Bibliography, WritingTool, Academic, and Productivity.


  The Citation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citation''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Citation Co Rate Limits
  slug: citation-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Citation API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: citation-co-rules
scopes:
- name: Citation Co Scopes
  scope_count: 13
  slug: citation-co-scopes
  summary_line: 13 scopes
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 19.7
    contract_quality: 63.0
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Citation Co Authentication
  slug: citation-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Citation Co Domain Security
  slug: citation-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Citation Co Vulnerability Disclosure
  slug: citation-co-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Citation Co Trust Center
  slug: citation-co-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: citation-co
tags:
- Citation
- Bibliography
- WritingTool
- Academic
- Productivity
website: https://citation.co/
---
