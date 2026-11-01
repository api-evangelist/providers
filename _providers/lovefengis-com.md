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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 64.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lovefengis Com Agentic Access
  operation_count: 8
  slug: lovefengis-com-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- baseURL: https://lovefengis.com
  baseurl_source: declared
  description: Several reads in one request
  name: lovefengis-com Batch API
  slug: lovefengis-com-batch-api
- baseURL: https://lovefengis.com
  baseurl_source: declared
  description: Services and prices
  name: lovefengis-com Catalog API
  slug: lovefengis-com-catalog-api
- baseURL: https://lovefengis.com
  baseurl_source: declared
  description: Asynchronous exports (202 Accepted, then poll)
  name: lovefengis-com Jobs API
  slug: lovefengis-com-jobs-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/lovefengis-com/agentic-access/lovefengis-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lovefengis-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lovefengis-com/rate-limits/lovefengis-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lovefengis-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/rules/lovefengis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/lovefengis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/json-ld/lovefengis-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lovefengis-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/lovefengis-com/vocabulary/lovefengis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lovefengis-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lovefengis-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/data-model/lovefengis-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lovefengis-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/lovefengis-com/cli/lovefengis-com-cli.yml
  title: ''
  type: CLI
  url: cli/lovefengis-com-cli.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/conventions/lovefengis-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lovefengis-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/conventions/lovefengis-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lovefengis-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/lovefengis-com/security/lovefengis-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lovefengis-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/lifecycle/lovefengis-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lovefengis-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/errors/lovefengis-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lovefengis-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lovefengis-com/conformance/lovefengis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lovefengis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lovefengis-com/llms/lovefengis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lovefengis-com-llms.txt
- group: other
  href: https://artifacts.apis.io/lovefengis-com/a2a/lovefengis-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lovefengis-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/lovefengis-com/mcp/lovefengis-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lovefengis-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lovefengis-com/mcp/lovefengis-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lovefengis-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/lovefengis-com/well-known/lovefengis-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lovefengis-com-security.txt
- group: auth
  href: https://artifacts.apis.io/lovefengis-com/well-known/lovefengis-com-sandbox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lovefengis-com-sandbox-security.txt
- group: auth
  href: https://artifacts.apis.io/lovefengis-com/well-known/lovefengis-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lovefengis-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/lovefengis-com/well-known/lovefengis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lovefengis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/lovefengis-com/hosts/lovefengis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lovefengis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lovefengis-com/vendors/lovefengis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lovefengis-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/lovefengis-com/packages/lovefengis-com-packages.yml
  title: ''
  type: SDKs
  url: packages/lovefengis-com-packages.yml
- group: build
  href: https://artifacts.apis.io/lovefengis-com/packages/lovefengis-com-packages.yml
  title: ''
  type: Packages
  url: packages/lovefengis-com-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://lovefengis.com/gelistirici/sandbox
- group: auth
  href: https://artifacts.apis.io/lovefengis-com/security/lovefengis-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lovefengis-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lovefengis-com/security/lovefengis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lovefengis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lovefengis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lovefengis.com/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://lovefengis.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://lovefengis.com/hizmetler
- group: company
  title: ''
  type: Blog
  url: https://lovefengis.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/systemonster
- group: commercial
  title: ''
  type: Pricing
  url: https://lovefengis.com/hizmetler
created: '2026-10-30'
description: lovefengis provides digital advertising management and SEO services for businesses across Turkey. The company offers campaign creation and management on Google, Meta, and emerging ChatGPT Ads platforms, as well as technical SEO audits, on‑page optimization, and AI‑assisted content creation. Services are delivered remotely with free 15‑minute consultations, transparent pricing, and ongoing performance reporting. The platform also exposes a public OpenAPI specification at /openapi.json for programmatic access to its service catalog.
image: https://lovefengis.com/logo-1024.png
json_schemas:
- name: BatchResponse
  property_count: 1
  slug: lovefengis-com-batch-response
- name: JobRequest
  property_count: 3
  slug: lovefengis-com-job-request
- name: Meta
  property_count: 8
  slug: lovefengis-com-meta
- name: PriceWithService
  property_count: 0
  slug: lovefengis-com-price-with-service
- name: Service
  property_count: 0
  slug: lovefengis-com-service
- name: ServiceSummary
  property_count: 5
  slug: lovefengis-com-service-summary
jsonld:
- class_count: 8
  name: Lovefengis Com Context
  property_count: 25
  slug: lovefengis-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at lovefengis.com.
  name: lovefengis-com MCP Server
  slug: lovefengis-com-mcp-yml
modified: '2026-10-30'
name: lovefengis-com
nav: Providers
network: true
overview: 'lovefengis-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Batch API, Catalog API, and Jobs API. Tagged areas include Company, Digital Marketing, SEO, Advertising, and Web Services.


  The lovefengis-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lovefengis-com''s developer surface includes CLI, sandbox, documentation, API reference, getting-started guide, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Lovefengis Com Plans Pricing
  plan_count: 0
  slug: lovefengis-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Lovefengis Com Rate Limits
  slug: lovefengis-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: lovefengis-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: lovefengis-com-rules
scopes:
- name: Lovefengis Com Scopes
  scope_count: 0
  slug: lovefengis-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 63.4
    developer_ergonomics: 58.8
    discoverability: 65.0
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lovefengis Com Authentication
  slug: lovefengis-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lovefengis Com Domain Security
  slug: lovefengis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lovefengis Com Vulnerability Disclosure
  slug: lovefengis-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: lovefengis-com-list-services
  slug: lovefengis-com-list-services
slug: lovefengis-com
tags:
- Company
- Digital Marketing
- SEO
- Advertising
- Web Services
- Turkey
website: https://lovefengis.com/
---
