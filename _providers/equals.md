---
access_model:
  confidence: high
  label: Paid · Sales-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://equals.com/pricing
  - plans/equals-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Equals Agentic Access
  operation_count: 5
  slug: equals-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: Hosted, remote Model Context Protocol server that gives AI assistants direct access to an Equals workspace — search and list workbooks including team-trusted analyses, list connected datasources and e
  name: Equals MCP Server
  slug: equals-mcp-server
- baseURL: https://go.equals.com/api/v1
  baseurl_source: declared
  description: Facts the Equals AI analyst remembers about a workspace.
  name: Equals Memories API
  slug: equals-memories-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/equals/agentic-access/equals-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/equals-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://equals.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.equals.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.equals.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.equals.com/docs/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://docs.equals.com/docs/resources.md
- group: commercial
  title: ''
  type: Pricing
  url: https://equals.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://go.equals.com/
- group: start
  title: ''
  type: Login
  url: https://go.equals.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://equals.com/policies/equals-online-terms-and-conditions-GP-april-11-22.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://equals.com/policies/privacy-policy.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EqualsHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://status.equals.com
- group: agent
  href: https://artifacts.apis.io/equals/mcp/equals-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/equals-mcp.yml
- group: agent
  href: https://artifacts.apis.io/equals/llms/equals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/equals-llms.txt
- group: design
  href: https://artifacts.apis.io/equals/lifecycle/equals-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/equals-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/equals/security/equals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/equals-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.equals.com/docs/memories-api
- group: docs
  href: https://artifacts.apis.io/equals/openapi/_original/equals-memories-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/equals-memories-openapi.yml
- group: auth
  href: https://artifacts.apis.io/equals/authentication/equals-authentication.yml
  title: ''
  type: Authentication
  url: authentication/equals-authentication.yml
- group: design
  href: https://artifacts.apis.io/equals/conventions/equals-conventions.yml
  title: ''
  type: Conventions
  url: conventions/equals-conventions.yml
- group: design
  href: https://artifacts.apis.io/equals/errors/equals-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/equals-problem-types.yml
- group: design
  href: https://artifacts.apis.io/equals/data-model/equals-data-model.yml
  title: ''
  type: DataModel
  url: data-model/equals-data-model.yml
- group: operate
  href: https://artifacts.apis.io/equals/rate-limits/equals-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/equals-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/equals/plans/equals-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/equals-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/equals/mcp/equals-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/equals-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/equals/well-known/equals-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/equals-well-known.yml
- group: other
  href: https://artifacts.apis.io/equals/a2a/equals-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/equals-a2a.yml
- group: agent
  href: https://artifacts.apis.io/equals/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/equals/packages/equals-packages.yml
  title: ''
  type: Packages
  url: packages/equals-packages.yml
- group: design
  href: https://artifacts.apis.io/equals/components/equals-components.yml
  title: ''
  type: Components
  url: components/equals-components.yml
- group: design
  href: https://artifacts.apis.io/equals/conformance/equals-conformance.yml
  title: ''
  type: Conformance
  url: conformance/equals-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.equals.com/docs/faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://equals.com/launches/
- group: operate
  href: https://artifacts.apis.io/equals/changelog/equals-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/equals-changelog.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:help@equals.com
created: '2026-07-17'
description: Equals is an AI analytics platform that builds trusted spreadsheets and dashboards for revenue operations and go-to-market teams. It connects directly to databases and SaaS tools — PostgreSQL, MySQL, BigQuery, Snowflake, Redshift, Azure SQL, Supabase, Stripe, Salesforce, HubSpot, Intercom, and more — syncs data into a managed Equals Warehouse powered by Snowflake, and layers a familiar spreadsheet calculation, pivot, and charting surface with AI-powered querying on top. Teams use it to establish a single source of truth for metrics like ARR, pipeline, and retention, then auto-distribute live dashboards to Slack and email. Equals exposes a hosted Model Context Protocol (MCP) server so agents can discover workbooks, query connected datasources, and ask natural-language questions of company data.
finops:
- has_sources: true
  method: derived
  name: Equals Finops
  primary_unit: subscription
  service_category: ''
  slug: equals-finops
  template: false
image: https://avatars.githubusercontent.com/u/16228084?v=4
layout: provider
mcp_servers:
- description: Remote MCP server at go.equals.com over HTTP; 3 tools listed.
  name: Equals MCP Server
  slug: equals
modified: '2026-09-16'
name: Equals
nav: Providers
network: true
overview: 'Equals publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Memories API, and 1 more. Tagged areas include Company, Analytics, Spreadsheets, Business Intelligence, and Dashboards.


  The Equals catalog on APIs.io includes 1 Spectral governance ruleset.


  Equals'' developer surface includes documentation, getting-started guide, support, pricing, signup flow, API reference, authentication, and 29 more developer resources.'
plans:
- name: Equals Plans Pricing
  plan_count: 3
  slug: equals-plans-pricing
- name: Equals Price Estimates
  plan_count: 0
  slug: equals-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: Equals Rate Limits
  slug: equals-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Equals API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: equals-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 18.1
    developer_ergonomics: 61.9
    discoverability: 75.0
    operational_transparency: 34.2
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/equals/equals-2026-07-25T213540.png
security:
- kind: authentication
  name: Equals Authentication
  slug: equals-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Equals Domain Security
  slug: equals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Equals
  slug: equals-equals
- name: Manage Equals analyst memories
  slug: equals-manage-analyst-memories
slug: equals
tags:
- Company
- Analytics
- Spreadsheets
- Business Intelligence
- Dashboards
- Data
- Revenue Operations
- Reporting
- MCP
- A2A
website: https://equals.com
---
