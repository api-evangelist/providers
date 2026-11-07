---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jobopportunitiesapi Org Agentic Access
  operation_count: 20
  slug: jobopportunitiesapi-org-agentic-access
  summary_line: 20 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.jobopportunitiesapi.org
  baseurl_source: declared
  description: The companies API from jobopportunitiesapi-org — 2 operation(s) for companies.
  name: jobopportunitiesapi-org Companies API
  slug: jobopportunitiesapi-org-companies-api
- baseURL: https://api.jobopportunitiesapi.org
  baseurl_source: declared
  description: The Jobs API from jobopportunitiesapi-org — 8 operation(s) for jobs.
  name: jobopportunitiesapi-org Jobs API
  slug: jobopportunitiesapi-org-jobs-api
- baseURL: https://api.jobopportunitiesapi.org
  baseurl_source: declared
  description: The meta API from jobopportunitiesapi-org — 6 operation(s) for meta.
  name: jobopportunitiesapi-org Meta API
  slug: jobopportunitiesapi-org-meta-api
- baseURL: https://api.jobopportunitiesapi.org
  baseurl_source: declared
  description: Keyless, aggregate-only routes under /public/ (no rows, statistics only). Most of /public/* mirrors a keyed /v1 endpoint and is documented there; the two BETA history routes below have no keyed twin a
  name: jobopportunitiesapi-org Public API
  slug: jobopportunitiesapi-org-public-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/jobopportunitiesapi-org/agentic-access/jobopportunitiesapi-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jobopportunitiesapi-org-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/jobopportunitiesapi-org/rate-limits/jobopportunitiesapi-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jobopportunitiesapi-org-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jobopportunitiesapi-org/plans/jobopportunitiesapi-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jobopportunitiesapi-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/rules/jobopportunitiesapi-org-rules.yml
  title: ''
  type: Spectral
  url: rules/jobopportunitiesapi-org-rules.yml
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/json-ld/jobopportunitiesapi-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jobopportunitiesapi-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/vocabulary/jobopportunitiesapi-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jobopportunitiesapi-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/data-model/jobopportunitiesapi-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jobopportunitiesapi-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/conventions/jobopportunitiesapi-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jobopportunitiesapi-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/jobopportunitiesapi-org/authentication/jobopportunitiesapi-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jobopportunitiesapi-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/errors/jobopportunitiesapi-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jobopportunitiesapi-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jobopportunitiesapi-org/conformance/jobopportunitiesapi-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jobopportunitiesapi-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jobopportunitiesapi-org/llms/jobopportunitiesapi-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobopportunitiesapi-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/jobopportunitiesapi-org/mcp/jobopportunitiesapi-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jobopportunitiesapi-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/jobopportunitiesapi-org/well-known/jobopportunitiesapi-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jobopportunitiesapi-org-security.txt
- group: auth
  href: https://artifacts.apis.io/jobopportunitiesapi-org/well-known/jobopportunitiesapi-org-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jobopportunitiesapi-org-api-security.txt
- group: agent
  href: https://artifacts.apis.io/jobopportunitiesapi-org/well-known/jobopportunitiesapi-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobopportunitiesapi-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/jobopportunitiesapi-org/hosts/jobopportunitiesapi-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobopportunitiesapi-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/jobopportunitiesapi-org/vendors/jobopportunitiesapi-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jobopportunitiesapi-org-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://jobopportunitiesapi.org/status
- group: auth
  title: ''
  type: Security
  url: https://jobopportunitiesapi.org/security
- group: start
  title: ''
  type: Sandbox
  url: https://jobopportunitiesapi.org/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://jobopportunitiesapi.org/changelog
- group: auth
  href: https://artifacts.apis.io/jobopportunitiesapi-org/security/jobopportunitiesapi-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jobopportunitiesapi-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jobopportunitiesapi-org/security/jobopportunitiesapi-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jobopportunitiesapi-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jobopportunitiesapi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://jobopportunitiesapi.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://jobopportunitiesapi.org/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://jobopportunitiesapi.org/docs/quickstart
- group: operate
  title: ''
  type: Roadmap
  url: https://jobopportunitiesapi.org/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://jobopportunitiesapi.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://jobopportunitiesapi.org/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jobopportunitiesapi.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jobopportunitiesapi.org/privacy
created: '2026-10-20'
description: 'jobopportunitiesapi-org is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://jobopportunitiesapi.org/og-default.png
json_schemas:
- name: CompanyPage
  property_count: 5
  slug: jobopportunitiesapi-org-company-page
- name: Company
  property_count: 14
  slug: jobopportunitiesapi-org-company
- name: JobPage
  property_count: 4
  slug: jobopportunitiesapi-org-job-page
- name: Job
  property_count: 56
  slug: jobopportunitiesapi-org-job
jsonld:
- class_count: 6
  name: Jobopportunitiesapi Org Context
  property_count: 78
  slug: jobopportunitiesapi-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.jobopportunitiesapi.org.
  name: jobopportunitiesapi-org MCP Server
  slug: jobopportunitiesapi-org-mcp-yml
modified: '2026-10-20'
name: jobopportunitiesapi-org
nav: Providers
network: true
overview: 'jobopportunitiesapi-org publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Jobs API, Meta API, and 1 more. Tagged areas include Job, Employment Data, Data Provenance, Job Board, and AI Agents.


  The jobopportunitiesapi-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  jobopportunitiesapi-org''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 26 more developer resources.'
plans:
- name: Jobopportunitiesapi Org Plans Pricing
  plan_count: 9
  slug: jobopportunitiesapi-org-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Jobopportunitiesapi Org Rate Limits
  slug: jobopportunitiesapi-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: jobopportunitiesapi-org API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 2
  slug: jobopportunitiesapi-org-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 29.8
    discoverability: 66.7
    operational_transparency: 44.7
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jobopportunitiesapi-org/jobopportunitiesapi-org-2026-11-03T134157.png
security:
- kind: authentication
  name: Jobopportunitiesapi Org Authentication
  slug: jobopportunitiesapi-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jobopportunitiesapi Org Domain Security
  slug: jobopportunitiesapi-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jobopportunitiesapi Org Vulnerability Disclosure
  slug: jobopportunitiesapi-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jobopportunitiesapi-org
tags:
- Job
- Employment Data
- Data Provenance
- Job Board
- AI Agents
website: https://jobopportunitiesapi.org/
---
