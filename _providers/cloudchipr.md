---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted, fully remote Model Context Protocol server at https://mcp.cloudchipr.com/mcp exposing 25 read-only tools across five categories - cloud accounts and organizations, Billing Explorer, savings op
  name: CloudChipr MCP Server
  slug: cloudchipr-mcp-server
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about accounts
  name: CloudChipr Accounts API
  slug: cloudchipr-accounts-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about budgets
  name: CloudChipr Budgets API
  slug: cloudchipr-budgets-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about categories
  name: CloudChipr Categories API
  slug: cloudchipr-categories-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about custom data sources
  name: CloudChipr Custom Data API
  slug: cloudchipr-custom-data-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about dashboards
  name: CloudChipr Dashboards API
  slug: cloudchipr-dashboards-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about filters
  name: CloudChipr Filters API
  slug: cloudchipr-filters-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: The Regions API from CloudChipr — 1 operation(s) for regions.
  name: CloudChipr Regions API
  slug: cloudchipr-regions-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about Resource Explorer
  name: CloudChipr Resource Explorer API
  slug: cloudchipr-resource-explorer-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Endpoints for resources
  name: CloudChipr Resources API
  slug: cloudchipr-resources-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about savings opportunities
  name: CloudChipr Savings Opportunities API
  slug: cloudchipr-savings-opportunities-api
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: Everything about widgets
  name: CloudChipr Widgets API
  slug: cloudchipr-widgets-api
artifact_total: 27
asyncapis:
- description: ''
  name: Cloudchipr Webhooks
  slug: cloudchipr-webhooks
common:
- group: other
  href: https://artifacts.apis.io/cloudchipr/capabilities/cloudchipr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudchipr-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/cloudchipr/security/cloudchipr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudchipr-trust-center.yml
- group: docs
  href: https://artifacts.apis.io/cloudchipr/openapi/cloudchipr-enterprise-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/cloudchipr-enterprise-api-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://cloudchipr.github.io/api-service/
- group: agent
  href: https://artifacts.apis.io/cloudchipr/mcp/cloudchipr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloudchipr-mcp.yml
- group: build
  href: https://artifacts.apis.io/cloudchipr/mcp/cloudchipr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudchipr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cloudchipr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/cloudchipr/authentication/cloudchipr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudchipr-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cloudchipr/scopes/cloudchipr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloudchipr-scopes.yml
- group: design
  href: https://artifacts.apis.io/cloudchipr/conventions/cloudchipr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudchipr-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudchipr/conventions/cloudchipr-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloudchipr-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudchipr/errors/cloudchipr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudchipr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudchipr/data-model/cloudchipr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudchipr-data-model.yml
- group: other
  href: https://artifacts.apis.io/cloudchipr/overlays/cloudchipr-enterprise-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudchipr-enterprise-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cloudchipr/conformance/cloudchipr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudchipr-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cloudchipr/conformance/cloudchipr-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cloudchipr-conformance.yml
- group: design
  href: https://artifacts.apis.io/cloudchipr/lifecycle/cloudchipr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudchipr-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cloudchipr/changelog/cloudchipr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudchipr-changelog.yml
- group: design
  href: https://artifacts.apis.io/cloudchipr/asyncapi/cloudchipr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudchipr-webhooks.yml
- group: build
  href: https://artifacts.apis.io/cloudchipr/packages/cloudchipr-packages.yml
  title: ''
  type: Packages
  url: packages/cloudchipr-packages.yml
- group: build
  href: https://artifacts.apis.io/cloudchipr/packages/cloudchipr-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudchipr-packages.yml
- group: agent
  href: https://artifacts.apis.io/cloudchipr/well-known/cloudchipr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudchipr-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/cloudchipr/plans/cloudchipr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudchipr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudchipr/rate-limits/cloudchipr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudchipr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cloudchipr/finops/cloudchipr-finops.yml
  title: ''
  type: FinOps
  url: finops/cloudchipr-finops.yml
- group: agent
  href: https://artifacts.apis.io/cloudchipr/llms/cloudchipr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudchipr-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cloudchipr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudchipr.com/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://cloudchipr.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudchipr.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudchipr.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.cloudchipr.com/registration
- group: start
  title: ''
  type: Login
  url: https://app.cloudchipr.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudchipr
- group: other
  title: ''
  type: X
  url: https://x.com/cloudchipr
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@cloudchipr
- group: other
  title: ''
  type: X-AWSMarketplace
  url: https://aws.amazon.com/marketplace/pp/prodview-enwub346vrmva
- group: auth
  href: https://artifacts.apis.io/cloudchipr/security/cloudchipr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudchipr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudchipr/security/cloudchipr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudchipr-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudchipr
- group: company
  title: ''
  type: Website
  url: https://cloudchipr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudchipr.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudchipr.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://cloudchipr.com/blog
- group: commercial
  title: ''
  type: FinOpsMember
  url: https://www.finops.org/members/cloudchipr/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.cloudchipr.com/llms.txt
created: '2026-03-27'
description: 'CloudChipr is a cloud cost-management and FinOps platform that consolidates AWS, Azure, GCP, Kubernetes and AI-vendor spend (OpenAI, Anthropic, Datadog, Snowflake, MongoDB, Confluent) in a single console and automates resource cleanup, rightsizing, and cost governance. The product surface centres on Billing Explorer, dashboards, live resource management, savings opportunities, commitments, budgets and anomaly alerts, no-code automation workflows, and integrations with email, Slack, Jira and webhooks. Two machine surfaces are published: a 26-operation OpenAPI 3.0.3 Enterprise API at api.cloudchipr.com, authenticated with an x-api-key header and served as a spec at cloudchipr.github.io/api-service, and a hosted remote MCP server at mcp.cloudchipr.com/mcp exposing 25 read-only tools over OAuth 2.0 or a bearer API key. CloudChipr is a FinOps Foundation member, states SOC 2 Type II certification, and lists on AWS Marketplace.'
finops:
- has_sources: true
  method: derived
  name: Cloudchipr Finops
  primary_unit: up to $5k monthly cloud spend
  service_category: ''
  slug: cloudchipr-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudchipr.png
layout: provider
mcp_servers:
- description: 'CloudChipr ships a first-party, fully hosted remote MCP server. Nothing is self-hosted and no package is installed: an MCP client points at one HTTPS endpoint and authenticates. The server is read-onl'
  name: CloudChipr MCP Server
  slug: cloudchipr
modified: '2026-09-05'
name: CloudChipr
nav: Providers
network: true
overview: 'CloudChipr publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Budgets API, Categories API, and 9 more. Tagged areas include Amazon Web Services, Microsoft Azure, Cloud Cost Management, Cost Optimization, and FinOps.


  The CloudChipr catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CloudChipr''s developer surface includes API reference, authentication, changelog, getting-started guide, support, signup flow, YouTube channel, and 39 more developer resources.'
plans:
- name: Cloudchipr Plans Pricing
  plan_count: 8
  slug: cloudchipr-plans-pricing
- name: Cloudchipr Price Estimates
  plan_count: 0
  slug: cloudchipr-price-estimates
random_paper: 13
rate_limits:
- limit_count: 0
  name: Cloudchipr Rate Limits
  slug: cloudchipr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: CloudChipr API Rules
  rule_count: 60
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 4
  slug: cloudchipr-rules
scopes:
- name: Cloudchipr Scopes
  scope_count: 4
  slug: cloudchipr-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.1
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 57.7
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 60.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cloudchipr/cloudchipr-2026-06-20T174545.png
security:
- kind: authentication
  name: Cloudchipr Authentication
  slug: cloudchipr-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Cloudchipr Domain Security
  slug: cloudchipr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudchipr Trust Center
  slug: cloudchipr-trust-center
  summary_line: SOC 2
skill_count: 4
skills:
- name: cloudchipr-budget-monitoring
  slug: cloudchipr-budget-monitoring
- name: cloudchipr-cost-breakdown
  slug: cloudchipr-cost-breakdown
- name: cloudchipr-custom-cost-ingestion
  slug: cloudchipr-custom-cost-ingestion
- name: cloudchipr-savings-opportunities
  slug: cloudchipr-savings-opportunities
slug: cloudchipr
tags:
- Amazon Web Services
- Microsoft Azure
- Cloud Cost Management
- Cost Optimization
- FinOps
- GCP
- Multi-Cloud
- Resource Cleanup
- Rightsizing
website: https://cloudchipr.com/
---
