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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Knit Agentic Access
  operation_count: 9
  slug: knit-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for managing department data across connected platforms.
  name: Knit Departments API
  slug: knit-departments-api
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for managing employee data across connected HRIS platforms.
  name: Knit Employees API
  slug: knit-employees-api
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for managing connected integrations.
  name: Knit Integrations API
  slug: knit-integrations-api
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for managing job postings and applications via ATS integrations.
  name: Knit Jobs API
  slug: knit-jobs-api
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for managing location/office data.
  name: Knit Locations API
  slug: knit-locations-api
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for monitoring sync status and triggering syncs.
  name: Knit Syncs API
  slug: knit-syncs-api
- baseURL: https://api.getknit.dev/v1
  baseurl_source: declared
  description: Operations for managing time off and leave data.
  name: Knit Time Off API
  slug: knit-time-off-api
artifact_total: 58
asyncapis:
- description: ''
  name: Knit Webhooks
  slug: knit-webhooks
collections:
- collection_type: open
  name: Knit Unified Departments API
  slug: open-knit-departments-api
- collection_type: open
  name: Knit Unified Departments Employees API
  slug: open-knit-employees-api
- collection_type: open
  name: Knit Unified Departments Integrations API
  slug: open-knit-integrations-api
- collection_type: open
  name: Knit Unified Departments Jobs API
  slug: open-knit-jobs-api
- collection_type: open
  name: Knit Unified Departments Locations API
  slug: open-knit-locations-api
- collection_type: open
  name: Knit Unified Departments Syncs API
  slug: open-knit-syncs-api
- collection_type: open
  name: Knit Unified Departments Time Off API
  slug: open-knit-time-off-api
- collection_type: open
  name: Knit Unified API
  slug: open-knit-unified-api
common:
- group: design
  href: https://artifacts.apis.io/knit/rules/knit-rules.yml
  title: ''
  type: Spectral
  url: rules/knit-rules.yml
- group: design
  href: https://artifacts.apis.io/knit/rules/knit-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/knit-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/knit/vocabulary/knit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/knit-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/knit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/knit/asyncapi/knit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/knit-webhooks.yml
- group: design
  href: https://artifacts.apis.io/knit/data-model/knit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/knit-data-model.yml
- group: design
  href: https://artifacts.apis.io/knit/conventions/knit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/knit-conventions.yml
- group: design
  href: https://artifacts.apis.io/knit/conventions/knit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/knit-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://getknit.dev/security/
- group: design
  href: https://artifacts.apis.io/knit/errors/knit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/knit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/knit/conformance/knit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/knit-conformance.yml
- group: agent
  href: https://artifacts.apis.io/knit/llms/knit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/knit-llms.txt
- group: agent
  href: https://artifacts.apis.io/knit/mcp/knit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/knit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/knit/well-known/knit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/knit-well-known.yml
- group: other
  href: https://artifacts.apis.io/knit/hosts/knit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/knit-hosts.yml
- group: other
  href: https://artifacts.apis.io/knit/vendors/knit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/knit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getknit.dev/terms
- group: auth
  title: ''
  type: Security
  url: https://getknit.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getknit.dev/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://getknit.dev/pricing/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getknit.dev/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getknit.dev/docs/getting-started-with-knit/llms.txt
- group: auth
  href: https://artifacts.apis.io/knit/security/knit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/knit-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/knit/plans/knit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/knit/rate-limits/knit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/knit/finops/knit-finops.yml
  title: ''
  type: FinOps
  url: finops/knit-finops.yml
- group: other
  href: https://artifacts.apis.io/knit/capabilities/knit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/knit-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.getknit.dev/
- group: agent
  href: https://artifacts.apis.io/knit/agentic-access/knit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/knit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/knit/security/knit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/knit/authentication/knit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knit-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knitapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getknit
- group: start
  title: ''
  type: Portal
  url: https://developers.getknit.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getknit.dev/
- group: docs
  href: https://artifacts.apis.io/knit/json-schema/knit-unified-api-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/knit-unified-api-schema.json
- group: design
  href: https://artifacts.apis.io/knit/json-ld/knit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/knit-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.getknit.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.getknit.dev/blog/rss.xml
created: '2026-03-16'
description: Knit is a unified API platform for B2B products, AI agents, and MCP clients, providing integrations infrastructure for HR, recruitment, and collaboration tools. Knit manages cron jobs, rate limits, and retries out of the box for predictable data syncing at scale.
features:
- Unified API for multiple HRIS and ATS platforms
- Automatic cron job management for data syncing
- Built-in rate limiting and retry logic
- Standardized data models across providers
- MCP client and AI agent support
- Real-time webhook notifications
- Incremental sync with updated_after filtering
finops:
- has_sources: false
  method: generated
  name: Knit Finops
  primary_unit: request
  service_category: API
  slug: knit-finops
  template: true
image: /assets/icons/knit.png
integrations:
- BambooHR
- Gusto
- Workday
- ADP
- Rippling
- Greenhouse
- Lever
- Slack
- Microsoft Teams
json_schemas:
- name: Department
  property_count: 4
  slug: knit-department
- name: Employee
  property_count: 12
  slug: knit-employee
- name: Integration
  property_count: 5
  slug: knit-integration
- name: Job
  property_count: 7
  slug: knit-job
- name: Location
  property_count: 7
  slug: knit-location
- name: Pagination
  property_count: 4
  slug: knit-pagination
- name: Sync
  property_count: 5
  slug: knit-sync
- name: TimeOff
  property_count: 7
  slug: knit-time-off
- name: Knit Unified API Resources
  property_count: 0
  slug: knit-unified-api
jsonld:
- class_count: 0
  name: Knit Context
  property_count: 5
  slug: knit-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.getknit.dev over HTTP; 6 tools listed.
  name: Knit MCP Server
  slug: knit
modified: '2026-05-19'
name: Knit
nav: Providers
network: true
overview: 'Knit publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Departments API, Employees API, Integrations API, and 4 more. Tagged areas include B2B, HR Integrations, HRIS, Unified API, and Integration Platform.


  The Knit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Knit''s developer surface includes pricing, API reference, getting-started guide, authentication, developer portal, documentation, engineering blog, and 32 more developer resources.'
plans:
- name: Knit Plans Pricing
  plan_count: 3
  slug: knit-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Knit Rate Limits
  slug: knit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Knit — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: knit-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Knit API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: knit-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 35.5
    contract_governance: 22.0
    contract_quality: 68.2
    developer_ergonomics: 50.6
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 51.6
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
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/knit/knit-2026-06-20T184110.png
security:
- kind: authentication
  name: Knit Authentication
  slug: knit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Knit Domain Security
  slug: knit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Knit Trust Center
  slug: knit-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: knit-syncs-list-and-trigger
  slug: knit-syncs-list-and-trigger
slug: knit
tags:
- B2B
- HR Integrations
- HRIS
- Unified API
- Integration Platform
- API Management
- iPaaS
- Automation
- SaaS Integration
- AI Agents
use_cases:
- Synchronizing employee data across HR platforms
- Building B2B integrations without managing individual provider APIs
- Powering AI agents with unified HR and recruitment data
- Automating onboarding workflows across HRIS systems
- Aggregating time-off and attendance data from multiple providers
website: https://www.getknit.dev/
---
