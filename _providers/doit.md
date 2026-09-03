---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 74.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 81
  human_in_the_loop: 0
  name: Doit Agentic Access
  operation_count: 166
  slug: doit-agentic-access
  summary_line: 166 operations · 81 acting
api_count: 1
apis:
- description: Official DoiT Model Context Protocol server. A remote Streamable HTTP endpoint at https://mcp.doit.com/mcp authenticated with OAuth 2.0 against console.doit.com, plus a local stdio server published to
  name: DoiT MCP Server
  slug: doit-mcp-server
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Find DoiT account managers assigned to your organization.
  name: DoiT Account Team API
  slug: doit-accountteam-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Notifications triggered when cloud costs exceed defined thresholds or meet specific conditions.
  name: DoiT Alerts API
  slug: doit-alerts-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Define how costs are distributed across your organization.
  name: DoiT Allocations API
  slug: doit-allocations-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Custom notes added to cost data to provide contextual information.
  name: DoiT Annotations API
  slug: doit-annotations-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Monitor cost spikes in your cloud environment.
  name: DoiT Anomalies API
  slug: doit-anomalies-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud resources or services in your cloud environment.
  name: DoiT Assets API
  slug: doit-assets-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: User authentication.
  name: DoiT Auth API
  slug: doit-auth-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Interact with Ava, DoiT's AI-powered cloud assistant.
  name: DoiT Ava API
  slug: doit-ava-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage AWS billing-transfer mappings between distributors and resellers and between resellers and end customers, and list program management accounts.
  name: DoiT Billing Transfer API
  slug: doit-billing-transfer-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: AI-generated budget recommendations you can accept (link to a budget you created) or dismiss.
  name: DoiT Budget Suggestions API
  slug: doit-budget-suggestions-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Track actual cloud spend against planned spend.
  name: DoiT Budgets API
  slug: doit-budgets-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud provider connections and check feature availability for connected accounts.
  name: DoiT Cloud Connect API
  slug: doit-cloud-connect-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Cloud Diagrams visualize your cloud infrastructure and resource relationships.
  name: DoiT Cloud Diagrams API
  slug: doit-cloud-diagrams-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Service disruptions and outages from cloud providers.
  name: DoiT Cloud Incidents API
  slug: doit-cloud-incidents-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage CloudFlow.
  name: DoiT Cloud Flow API
  slug: doit-cloudflow-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: View and manage commitment contracts with DoiT.
  name: DoiT Commitment Manager API
  slug: doit-commitment-manager-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud provider connections used in CloudFlow workflows (AWS and GCP).
  name: DoiT Connections API
  slug: doit-connections-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage contract templates for PartnerOps resellers (T1/T2).
  name: DoiT Contract Templates API
  slug: doit-contract-templates-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: List and manage tenant-scoped contracts as a T1/T2 PartnerOps caller.
  name: DoiT Contracts API
  slug: doit-contracts-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Ingest third-party cost, usage, and metric-based data for analysis.
  name: DoiT Data Hub API
  slug: doit-datahub-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: View available dimensions for analysis.
  name: DoiT Dimensions API
  slug: doit-dimensions-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Organize Cloud Analytics resources (reports, allocations) into folders.
  name: DoiT Folders API
  slug: doit-folders-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud insights representing recommendations and findings for cloud resources.
  name: DoiT Insights API
  slug: doit-insights-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Access your current and historical billing documents.
  name: DoiT Invoices API
  slug: doit-invoices-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Create and manage labels to organize and categorize your cloud resources.
  name: DoiT Labels API
  slug: doit-labels-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Organizations help you segment data by your company or team structure.
  name: DoiT Organizations API
  slug: doit-organizations-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: PerfectScale for Commitments (AWS) — commitment inventory, recommendations, and planned purchases.
  name: DoiT PerfectScale for Commitments AWS API
  slug: doit-perfectscale-for-commitments-aws-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Metadata about supported cloud providers.
  name: DoiT Platforms API
  slug: doit-platforms-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Metadata about cloud services and offerings.
  name: DoiT Products API
  slug: doit-products-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage Cloud Analytics reports and get reports data in JSON format.
  name: DoiT Reports API
  slug: doit-reports-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage user permissions and access levels in your organization.
  name: DoiT Roles API
  slug: doit-roles-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Monitor cloud service quota usage across connected accounts and projects.
  name: DoiT Service Quotas API
  slug: doit-service-quotas-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: The Settings API from DoiT — 3 operation(s) for settings.
  name: DoiT Settings API
  slug: doit-settings-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage permissions associated with specified Cloud Analytics resources.
  name: DoiT Sharing API
  slug: doit-sharing-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Create and manage support tickets with DoiT.
  name: DoiT Support Requests API
  slug: doit-support-requests-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Browse the catalogue of read-only CloudFlow templates (blueprints) used to create flows.
  name: DoiT Templates API
  slug: doit-templates-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage users who have access to the DoiT platform.
  name: DoiT Users API
  slug: doit-users-api
artifact_total: 48
asyncapis:
- description: ''
  name: Doit Events
  slug: doit-events
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/doitintl/doit-mcp-server/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/doit-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.doit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.doit.com/docs/start
- group: docs
  title: ''
  type: APIReference
  url: https://developer.doit.com/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.doit.com/docs/start
- group: operate
  title: ''
  type: Support
  url: https://help.doit.com/
- group: company
  title: ''
  type: Blog
  url: https://www.doit.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.doit.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doitintl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.doit.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doit.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doit.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.doit.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.doit.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doit-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/doit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doit-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doit-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/doit-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/doit-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/doit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.doit.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/doit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.doit.com/docs/availability-matrix
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/doit-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doit-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://help.doit.com/docs/vendor-information/bug-bounty-program
- group: design
  title: ''
  type: Conventions
  url: conventions/doit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/doit-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/doit-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/doit-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/doit-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/doit-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/doit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doit-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-setup.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-reporting.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-anomaly-investigation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-api.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/doitintl
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/doit-openapi-original.yml
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://developer.doit.com/changelog.rss
created: '2026-08-12'
description: DoiT International is a cloud and FinOps technology company behind DoiT Cloud Intelligence, an intent-aware FinOps platform that unifies cost, usage and savings data across AWS, Google Cloud, Azure, Kubernetes and 40+ other clouds and SaaS providers. The DoiT Platform API at api.doit.com gives programmatic access to Cloud Analytics reports, allocations, budgets, alerts, anomalies, invoices, assets, DataHub ingestion, CloudFlow automation, cloud incidents, support requests, insights and its Ava AI assistant, published as a single OpenAPI 3.0.1 contract. DoiT also ships an official remote MCP server at mcp.doit.com, a generated dci CLI, a Terraform provider, a Grafana plugin, and an open-source Agent Skills plugin for agentic FinOps workflows.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: DoiT MCP Server
  slug: doit-mcp-server
modified: '2026-08-12'
name: DoiT
nav: Providers
network: true
overview: 'DoiT publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Account Team API, Alerts API, Allocations API, and 34 more. Tagged areas include Company, FinOps, Cloud Cost Management, Cloud Intelligence, and Cost Optimization.


  The DoiT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DoiT''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 46 more developer resources.'
plans:
- name: Doit Plans Pricing
  plan_count: 6
  slug: doit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Doit Rate Limits
  slug: doit-rate-limits
scopes:
- name: Doit Scopes
  scope_count: 4
  slug: doit-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 65.4
    developer_ergonomics: 64.3
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 69.7
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doit/refs/heads/main/screenshots/doit-2026-08-17T080051.png
security:
- kind: authentication
  name: Doit Authentication
  slug: doit-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Doit Domain Security
  slug: doit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doit Vulnerability Disclosure
  slug: doit-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Doit Trust Center
  slug: doit-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001, ISO 27001:2022, GDPR, CCPA, ICO registered, EU-US Data Privacy Framework
slug: doit
tags:
- Company
- FinOps
- Cloud Cost Management
- Cloud Intelligence
- Cost Optimization
- Multi-Cloud
- Kubernetes
- Analytics
- MCP
- Artificial Intelligence
website: https://www.doit.com/
---
