---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.cloudchipr.com
  baseurl_source: declared
  description: 'The CloudChipr Enterprise API - 26 operations over 26 paths, described by a public OpenAPI 3.0.3 document CloudChipr serves from its own GitHub Pages site and links from its homepage and docs. Covers '
  name: CloudChipr API
  slug: cloudchipr-api
- description: Hosted, fully remote Model Context Protocol server at https://mcp.cloudchipr.com/mcp exposing 25 read-only tools across five categories - cloud accounts and organizations, Billing Explorer, savings op
  name: CloudChipr MCP Server
  slug: cloudchipr-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Cloudchipr Webhooks
  slug: cloudchipr-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudchipr-trust-center.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cloudchipr-enterprise-api-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://cloudchipr.github.io/api-service/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudchipr-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudchipr-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudchipr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloudchipr-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudchipr-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cloudchipr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudchipr-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudchipr-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cloudchipr-enterprise-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudchipr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cloudchipr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudchipr-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudchipr-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudchipr-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloudchipr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudchipr-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudchipr-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudchipr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudchipr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudchipr-finops.yml
- group: agent
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
  title: ''
  type: DomainSecurity
  url: security/cloudchipr-domain-security.yml
- group: auth
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
- name: Cloudchipr Finops
  service_category: API
  slug: cloudchipr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudchipr.png
layout: provider
mcp_servers:
- description: ''
  name: CloudChipr MCP Server
  slug: cloudchipr-mcp-server
- description: ''
  name: CloudChipr MCP Server
  slug: cloudchipr-mcp-server-2
modified: '2026-09-05'
name: CloudChipr
nav: Providers
network: true
overview: 'CloudChipr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Azure, Cloud Cost Management, Cost Optimization, FinOps, and GCP.


  The CloudChipr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudChipr''s developer surface includes API reference, authentication, changelog, getting-started guide, support, signup flow, YouTube channel, and 38 more developer resources.'
plans:
- name: Cloudchipr Plans Pricing
  plan_count: 4
  slug: cloudchipr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Cloudchipr Rate Limits
  slug: cloudchipr-rate-limits
scopes:
- name: Cloudchipr Scopes
  scope_count: 0
  slug: cloudchipr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 37.6
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 65.6
    developer_ergonomics: 50.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 20.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudchipr/refs/heads/main/screenshots/cloudchipr-2026-06-20T174545.png
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
slug: cloudchipr
tags:
- Azure
- Cloud Cost Management
- Cost Optimization
- FinOps
- GCP
- Multi-Cloud
- Resource Cleanup
- Rightsizing
website: https://cloudchipr.com/
---
