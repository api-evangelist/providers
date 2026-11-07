---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Answercheckup Com Agentic Access
  operation_count: 7
  slug: answercheckup-com-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://answercheckup.com
  baseurl_source: declared
  description: The Pricing API from Answer Checkup — 1 operation(s) for pricing.
  name: Answer Checkup Pricing API
  slug: answercheckup-com-pricing-api
- baseURL: https://answercheckup.com
  baseurl_source: declared
  description: The Report API from Answer Checkup — 1 operation(s) for report.
  name: Answer Checkup Report API
  slug: answercheckup-com-report-api
- baseURL: https://answercheckup.com
  baseurl_source: declared
  description: The Reports API from Answer Checkup — 1 operation(s) for reports.
  name: Answer Checkup Reports API
  slug: answercheckup-com-reports-api
- baseURL: https://answercheckup.com
  baseurl_source: declared
  description: The Scan API from Answer Checkup — 2 operation(s) for scan.
  name: Answer Checkup Scan API
  slug: answercheckup-com-scan-api
- baseURL: https://answercheckup.com
  baseurl_source: declared
  description: The Scan Details API from Answer Checkup — 1 operation(s) for scan details.
  name: Answer Checkup Scan Details API
  slug: answercheckup-com-scan-details-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/answercheckup-com/agentic-access/answercheckup-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/answercheckup-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/answercheckup-com/rate-limits/answercheckup-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/answercheckup-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/answercheckup-com/plans/answercheckup-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/answercheckup-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/answercheckup-com/rules/answercheckup-com-rules.yml
  title: ''
  type: Spectral
  url: rules/answercheckup-com-rules.yml
- group: design
  href: https://artifacts.apis.io/answercheckup-com/json-ld/answercheckup-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/answercheckup-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/answercheckup-com/vocabulary/answercheckup-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/answercheckup-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/answercheckup-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/answercheckup-com/data-model/answercheckup-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/answercheckup-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/answercheckup-com/security/answercheckup-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/answercheckup-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/answercheckup-com/errors/answercheckup-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/answercheckup-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/answercheckup-com/conformance/answercheckup-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/answercheckup-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/answercheckup-com/llms/answercheckup-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/answercheckup-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/answercheckup-com/mcp/answercheckup-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/answercheckup-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/answercheckup-com/well-known/answercheckup-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/answercheckup-com-security.txt
- group: agent
  href: https://artifacts.apis.io/answercheckup-com/well-known/answercheckup-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/answercheckup-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/answercheckup-com/hosts/answercheckup-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/answercheckup-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/answercheckup-com/vendors/answercheckup-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/answercheckup-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/answercheckup-com/security/answercheckup-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/answercheckup-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/answercheckup-com/security/answercheckup-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/answercheckup-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://answercheckup.com/
- group: docs
  title: ''
  type: APIReference
  url: https://answercheckup.com/openapi.json
- group: docs
  title: ''
  type: Documentation
  url: https://answercheckup.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://answercheckup.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://answercheckup.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://answercheckup.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://answercheckup.com/privacy
created: '2026-11-01'
description: Answer Checkup provides a deep SEO and GEO test that determines whether AI models such as ChatGPT and Perplexity mention your business when users ask them. The service offers a free scan and paid reports (Lite $29, Full $49) that query multiple AI engines, aggregate results, and return a JSON report. It also exposes an OpenAPI 3.1 specification at /openapi.json and an MCP server for agents. The platform helps businesses understand AI visibility and improve their online presence.
image: https://answercheckup.com/brand/og-c.png?v=d585a67f38
json_schemas:
- name: LockedScanView
  property_count: 7
  slug: answercheckup-com-locked-scan-view
- name: ReportResponse
  property_count: 2
  slug: answercheckup-com-report-response
- name: ScanResult
  property_count: 6
  slug: answercheckup-com-scan-result
jsonld:
- class_count: 4
  name: Answercheckup Com Context
  property_count: 16
  slug: answercheckup-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at answercheckup.com.
  name: Answer Checkup MCP Server
  slug: answercheckup-com-mcp-yml
modified: '2026-11-01'
name: Answer Checkup
nav: Providers
network: true
overview: 'Answer Checkup publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Pricing API, Report API, Reports API, and 2 more. Tagged areas include Artificial Intelligence, SEO, Marketing, Analytics, and Business.


  The Answer Checkup catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Answer Checkup''s developer surface includes API reference, documentation, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Answercheckup Com Plans Pricing
  plan_count: 4
  slug: answercheckup-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Answercheckup Com Rate Limits
  slug: answercheckup-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Answer Checkup API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: answercheckup-com-rules
scopes:
- name: Answercheckup Com Scopes
  scope_count: 0
  slug: answercheckup-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 79.8
    catalog_earned_first_party: 20.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 57.3
    developer_ergonomics: 16.0
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
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
  name: Answercheckup Com Authentication
  slug: answercheckup-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Answercheckup Com Domain Security
  slug: answercheckup-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Answercheckup Com Vulnerability Disclosure
  slug: answercheckup-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: scan-site
  slug: answercheckup-com-scan-site
slug: answercheckup-com
tags:
- Artificial Intelligence
- SEO
- Marketing
- Analytics
- Business
website: https://answercheckup.com/
---
