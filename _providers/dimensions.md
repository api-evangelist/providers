---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dimensions Agentic Access
  operation_count: 2
  slug: dimensions-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: 'The Dimensions Analytics API provides programmatic access to the Dimensions research data platform via the Dimensions Search Language (DSL). It supports queries against publications, grants, patents, '
  name: Dimensions Analytics API
  slug: dimensions-analytics-api
- baseURL: https://app.dimensions.ai/api
  baseurl_source: declared
  description: The Authentication API from Dimensions — 1 operation(s) for authentication.
  name: Dimensions Authentication API
  slug: dimensions-authentication-api
- baseURL: https://app.dimensions.ai/api
  baseurl_source: declared
  description: The Query API from Dimensions — 1 operation(s) for query.
  name: Dimensions Query API
  slug: dimensions-query-api
artifact_total: 18
collections:
- collection_type: open
  name: Dimensions Analytics Authentication API
  slug: open-dimensions-authentication-api
- collection_type: open
  name: Dimensions Analytics Authentication Query API
  slug: open-dimensions-query-api
- collection_type: open
  name: Dimensions Analytics API
  slug: open-dimensions
common:
- group: other
  href: https://artifacts.apis.io/dimensions/capabilities/dimensions-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dimensions-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/digital-science/dimcli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/digital-science/dimcli/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/digital-science/dimcli/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/dimensions/agentic-access/dimensions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dimensions-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dimensions/security/dimensions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimensions-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dimensions/authentication/dimensions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dimensions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dimensions.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dimensions.ai/dsl/
- group: operate
  title: ''
  type: Support
  url: https://help.dimensions.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.dimensions.ai/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dimensions.ai/dsl/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dimensions.ai/dsl/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digital-science
- group: start
  title: ''
  type: Login
  url: https://app.dimensions.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dimensions.ai/website-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dimensions.ai/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dimensions.ai/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dimensions.ai/dsl/releasenotes.html
- group: operate
  href: https://artifacts.apis.io/dimensions/changelog/dimensions-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dimensions-changelog.yml
- group: design
  href: https://artifacts.apis.io/dimensions/lifecycle/dimensions-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dimensions-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/dimensions/packages/dimensions-packages.yml
  title: ''
  type: Packages
  url: packages/dimensions-packages.yml
- group: build
  href: https://artifacts.apis.io/dimensions/packages/dimensions-packages.yml
  title: ''
  type: SDKs
  url: packages/dimensions-packages.yml
- group: build
  href: https://artifacts.apis.io/dimensions/cli/dimensions-cli.yml
  title: ''
  type: CLI
  url: cli/dimensions-cli.yml
- group: design
  href: https://artifacts.apis.io/dimensions/components/dimensions-components.yml
  title: ''
  type: Components
  url: components/dimensions-components.yml
- group: agent
  href: https://artifacts.apis.io/dimensions/mcp/dimensions-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dimensions-mcp.yml
- group: build
  href: https://artifacts.apis.io/dimensions/mcp/dimensions-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dimensions-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dimensions/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dimensions/llms/dimensions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dimensions-llms.txt
- group: agent
  href: https://artifacts.apis.io/dimensions/well-known/dimensions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dimensions-well-known.yml
- group: auth
  href: https://artifacts.apis.io/dimensions/scopes/dimensions-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dimensions-scopes.yml
- group: design
  href: https://artifacts.apis.io/dimensions/conventions/dimensions-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dimensions-conventions.yml
- group: design
  href: https://artifacts.apis.io/dimensions/errors/dimensions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dimensions-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dimensions/conformance/dimensions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dimensions-conformance.yml
- group: design
  href: https://artifacts.apis.io/dimensions/data-model/dimensions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dimensions-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/dimensions/plans/dimensions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dimensions-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dimensions/rate-limits/dimensions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dimensions-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dimensions/finops/dimensions-finops.yml
  title: ''
  type: FinOps
  url: finops/dimensions-finops.yml
created: '2025-02-06'
description: Dimensions is a research data platform from Digital Science providing access to publications, grants, patents, clinical trials, datasets, and policy documents. The Dimensions Analytics API offers programmatic access to this research data via the Dimensions Search Language (DSL), enabling citation analysis, researcher discovery, organization benchmarking, and topic identification. The API is subscription-only and is not intended for bulk data extraction or to power dashboards or other derivative products.
finops:
- has_sources: true
  method: derived
  name: Dimensions Finops
  primary_unit: ''
  service_category: ''
  slug: dimensions-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dimensions.png
layout: provider
mcp_servers:
- description: 'Digital Science publishes first-party MCP servers for Dimensions. The flagship is the Dimensions Analytics MCP — an open-source (MIT) local stdio server on npm that exposes 27 tools plus 10 resources '
  name: Dimensions MCP Server
  slug: dimensions-mcp-yml
modified: '2026-09-06'
name: Dimensions
nav: Providers
network: true
overview: 'Dimensions publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Query API, and 1 more. Tagged areas include Analytics, Research, Publications, Grants, and Patents.


  The Dimensions catalog on APIs.io includes 1 Spectral governance ruleset.


  Dimensions'' developer surface includes authentication, documentation, support, engineering blog, API reference, getting-started guide, changelog, and 31 more developer resources.'
plans:
- name: Dimensions Plans Pricing
  plan_count: 0
  slug: dimensions-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Dimensions Rate Limits
  slug: dimensions-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Dimensions API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: dimensions-rules
scopes:
- name: Dimensions Scopes
  scope_count: 1
  slug: dimensions-scopes
  summary_line: 1 scope · authorization_code/refresh_token
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 31.8
    contract_quality: 42.9
    developer_ergonomics: 63.7
    discoverability: 68.3
    operational_transparency: 63.2
  open_source:
    applies: true
    score: 25.0
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dimensions/dimensions-2026-06-20T180036.png
security:
- kind: authentication
  name: Dimensions Authentication
  slug: dimensions-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Dimensions Domain Security
  slug: dimensions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: dimensions-authenticate-and-query
  slug: dimensions-authenticate-and-query
- name: dimensions-funding-and-impact-analytics
  slug: dimensions-funding-and-impact-analytics
- name: dimensions-literature-search
  slug: dimensions-literature-search
slug: dimensions
tags:
- Analytics
- Research
- Publications
- Grants
- Patents
- Clinical Trials
- Jupyter Notebooks
- Scientometrics
- Bibliometrics
- Research Intelligence
- Datasets
- Policy Documents
- MCP
- Research Data
website: https://www.dimensions.ai/
---
