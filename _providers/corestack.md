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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Hosted, unified Model Context Protocol server exposing 100 documented tools across five domains — Common/Auth (10), FinOps (24), Graphion (45), Assessment (15) and Workload (6) — at a single /mcp endp
  name: CoreStack MCP Server
  slug: corestack-mcp-server
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Access Pillar
  name: CoreStack Access API
  slug: corestack-access-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Cloud Accounts
  name: CoreStack Account Governance API
  slug: corestack-account-governance-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: AI Agent Framework API
  name: CoreStack AI Agent API
  slug: corestack-ai-agent-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Application Health
  name: CoreStack Application Health API
  slug: corestack-application-health-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Application Security
  name: CoreStack App Sec Ops API
  slug: corestack-appsecops-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Assessment
  name: CoreStack Assessment API
  slug: corestack-assessment-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Attachments
  name: CoreStack Attachments API
  slug: corestack-attachments-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Tokens
  name: CoreStack Authorization API
  slug: corestack-authorization-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Templates, Scripts & Blueprints
  name: CoreStack Automation API
  slug: corestack-automation-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Automation WorkFlows
  name: CoreStack Automation WorkFlows API
  slug: corestack-automation-workflows-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: AWS Security Hub
  name: CoreStack AWS Security Hub API
  slug: corestack-aws-security-hub-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage AWS SSM
  name: CoreStack Aws Ssm API
  slug: corestack-awsssm-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage AWS SSM Automation
  name: CoreStack AwsSsm Automation API
  slug: corestack-awsssm-automation-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage AWS SSM Command
  name: CoreStack AwsSsm Command API
  slug: corestack-awsssm-command-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Azure DevOps Pipeline DashBoard
  name: CoreStack Azure DevOps Pipeline DashBoard API
  slug: corestack-azure-devops-pipeline-dashboard-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Background Jobs
  name: CoreStack Background Jobs API
  slug: corestack-background-jobs-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Cost Management
  name: CoreStack Billing API
  slug: corestack-billing-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Billing commitment
  name: CoreStack Billing Commitment API
  slug: corestack-billing-commitment-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Billing Metrics
  name: CoreStack Billing Metric API
  slug: corestack-billing-metric-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage BillOps Plans
  name: CoreStack Billing Plan Definitions API
  slug: corestack-billingplandefinitions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage BillOps Plan Versions
  name: CoreStack Billing Plan Definition Versions API
  slug: corestack-billingplandefinitionversions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Budget V2 Management
  name: CoreStack Budget V2 Management API
  slug: corestack-budget-v2-management-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Corestack compliance Rest API
  name: CoreStack Compliance API
  slug: corestack-compliance-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Copilot Governance Metrics
  name: CoreStack Copilot Governance API
  slug: corestack-copilot-governance-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Cost Anomaly Detection
  name: CoreStack Cost Anomaly API
  slug: corestack-cost-anomaly-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Cost Pillar
  name: CoreStack Cost API
  slug: corestack-cost-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Currency Exchange Configuration
  name: CoreStack Currency Exchange Configuration API
  slug: corestack-currencyexchangeconfiguration-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Custom Metric Configuration
  name: CoreStack Custom Metric Configuration API
  slug: corestack-custom-metric-configuration-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Custom Tags
  name: CoreStack Custom Tags API
  slug: corestack-custom-tags-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Executive Dashboard Versions
  name: CoreStack Dashboard Definition Versions API
  slug: corestack-dashboard-definition-versions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Executive Dashboards
  name: CoreStack Dashboard Definitions API
  slug: corestack-dashboard-definitions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage saved views for executive dashboards (deep-linkable)
  name: CoreStack Dashboard Saved Views API
  slug: corestack-dashboard-saved-views-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Dimensions
  name: CoreStack Dimension API
  slug: corestack-dimension-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Dimension Versions
  name: CoreStack Dimension Version API
  slug: corestack-dimensionversion-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Freshservice Ticket Integration
  name: CoreStack Freshservice Tickets API
  slug: corestack-freshservice-tickets-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Policy
  name: CoreStack Guardrails API
  slug: corestack-guardrails-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: User, Tenants & Roles Management
  name: CoreStack Identity API
  slug: corestack-identity-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Jira Service Management
  name: CoreStack Jira Service Management API
  slug: corestack-jira-service-management-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Kubernetes Agent
  name: CoreStack Kubernetes Agent API
  slug: corestack-kubernetes-agent-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Master Data apis
  name: CoreStack Master Data API
  slug: corestack-master-data-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Master Account Billing
  name: CoreStack MasterAccount Billing API
  slug: corestack-masteraccount-billing-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage NextGen Reports
  name: CoreStack NextGen Reports API
  slug: corestack-nextgen-reports-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage On premises Metrics
  name: CoreStack On premises API
  slug: corestack-on-premises-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Operations Pillar
  name: CoreStack Operations API
  slug: corestack-operations-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Dashboard For Utilization
  name: CoreStack Operations Utilization API
  slug: corestack-operations-utilization-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Dashboard For Utilization Metrics
  name: CoreStack Operations Utilization Metric Dashboard API
  slug: corestack-operations-utilization-metric-dashboard-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Assign Platform related background tasks to service accounts
  name: CoreStack Platform Task API
  slug: corestack-platformtask-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Cloud SKU Pricing API
  name: CoreStack Pricing API
  slug: corestack-pricing-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Pro Active Scanner Configurations
  name: CoreStack Pro Active Scanner Configurations API
  slug: corestack-pro-active-scanner-configurations-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Product bundles, Product & Role templates
  name: CoreStack Product API
  slug: corestack-product-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Recommendation summary
  name: CoreStack Recommendation API
  slug: corestack-recommendation-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Recommendations
  name: CoreStack Recommendation V2 Dashboard API
  slug: corestack-recommendation-v2-dashboard-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Reports Pillar
  name: CoreStack Reports API
  slug: corestack-reports-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Analyze Request Audit
  name: CoreStack Request Audit API
  slug: corestack-request-audit-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Resource Pillar
  name: CoreStack Resource API
  slug: corestack-resource-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Savings plans purchased and utilization
  name: CoreStack Savings Plans API
  slug: corestack-savings-plans-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Schedule Recommendation
  name: CoreStack Schedule Recommendations API
  slug: corestack-schedule-recommendations-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Schedules
  name: CoreStack Schedules API
  slug: corestack-schedules-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Security Pillar
  name: CoreStack Security API
  slug: corestack-security-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Self Service Pillar
  name: CoreStack Self Service API
  slug: corestack-self-service-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Service Accounts
  name: CoreStack Service Account Governance API
  slug: corestack-service-account-governance-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Service Account Resources
  name: CoreStack Service Account Resources API
  slug: corestack-service-account-resources-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: ServiceNow Integrations
  name: CoreStack ServiceNow Integrations API
  slug: corestack-servicenow-integrations-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Stacks Marketplace Products
  name: CoreStack Stacks Marketplace Product API
  slug: corestack-stacksmarketplaceproduct-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Stacks Marketplace Stack Definitions
  name: CoreStack Stacks Marketplace Stack Definition API
  slug: corestack-stacksmarketplacestackdefinition-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Stacks Marketplace Stack Definition Versions
  name: CoreStack Stacks Marketplace Stack Definition Version API
  slug: corestack-stacksmarketplacestackdefinitionversion-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Stacks Marketplace Stack Deployments
  name: CoreStack Stacks Marketplace Stack Deployment API
  slug: corestack-stacksmarketplacestackdeployment-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Summary Dashboard APIs
  name: CoreStack Summary Dashboard API
  slug: corestack-summarydashboard-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Tagging Governance
  name: CoreStack Tagging Governance Definitions API
  slug: corestack-tagginggovernancedefinitions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Tagging Governance Versions
  name: CoreStack Tagging Governance Definition Versions API
  slug: corestack-tagginggovernancedefinitionversions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Tagging Governance Postures
  name: CoreStack Tagging Governance Postures API
  slug: corestack-tagginggovernancepostures-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Corestack UserPreferences Rest API
  name: CoreStack User Preference API
  slug: corestack-userpreference-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Assessments
  name: CoreStack Waf Assessment Definitions API
  slug: corestack-wafassessmentdefinitions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Assessment Versions
  name: CoreStack Waf Assessment Definition Versions API
  slug: corestack-wafassessmentdefinitionversions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Assessment Runs
  name: CoreStack Waf Assessment Runs API
  slug: corestack-wafassessmentruns-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Corestack Well Architecture Framework Rest API
  name: CoreStack Well Architected Framework API
  slug: corestack-wellarchitectedframework-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Workloads
  name: CoreStack Workload Definitions API
  slug: corestack-workloaddefinitions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Manage Workload Versions
  name: CoreStack Workload Definition Versions API
  slug: corestack-workloaddefinitionversions-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Query Resources for Workloads
  name: CoreStack Workload Query API
  slug: corestack-workloadquery-api
- baseURL: https://api.corestack.io/
  baseurl_source: declared
  description: Zoho Incident
  name: CoreStack Zoho Incident API
  slug: corestack-zoho-incident-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: AI Agents observability APIs (AgentCore agent discovery and span/trace collection)
  name: CoreStack AI Agents Observability API
  slug: corestack-ai-agents-observability-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Manage Locks
  name: CoreStack Lock Configuration API
  slug: corestack-lock-configuration-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Manage policies and policy job details
  name: CoreStack Policy V2 API
  slug: corestack-policy-v2-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Roles Management
  name: CoreStack Roles API
  slug: corestack-roles-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Manage templates
  name: CoreStack Templates API
  slug: corestack-templates-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Tenant Management
  name: CoreStack Tenants API
  slug: corestack-tenants-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: User Delegation Rules and Reports
  name: CoreStack User Delegation API
  slug: corestack-userdelegation-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: User Management - CRUD, listing and search
  name: CoreStack Users API
  slug: corestack-users-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: User Authentication - passwords, keys, verification and activation
  name: CoreStack Users Auth API
  slug: corestack-usersauth-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: User Profile and Notifications
  name: CoreStack Users Profile API
  slug: corestack-usersprofile-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Manage AI Governance Metrics
  name: CoreStack AI Governance API
  slug: corestack-ai-governance-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Manage Audit Log
  name: CoreStack Audit Log API
  slug: corestack-audit-log-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: Manage Master Account
  name: CoreStack Master Account API
  slug: corestack-master-account-api
- baseURL: https://cloud.corestack.io/mcp
  baseurl_source: declared
  description: User Group Management
  name: CoreStack User Groups API
  slug: corestack-user-groups-api
artifact_total: 109
asyncapis:
- description: ''
  name: Corestack Webhooks
  slug: corestack-webhooks
collections:
- collection_type: open
  name: CoreStack External API
  slug: open-corestack-external-api-openapi-original
common:
- group: company
  title: ''
  type: Blog
  url: https://www.corestack.io/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.corestack.io/feed/
- group: other
  href: https://artifacts.apis.io/corestack/capabilities/corestack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/corestack-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/corestack/security/corestack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corestack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corestack.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.corestack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corestack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.corestack.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.corestack.io/docs/corestack-api-modules
- group: operate
  title: ''
  type: Support
  url: https://support.corestack.io/portal/en/home
- group: company
  title: ''
  type: Blog
  url: https://www.corestack.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.corestack.io/solutions/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.corestack.io/contact-us/
- group: start
  title: ''
  type: Login
  url: https://cloud.corestack.io/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corestack.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corestack.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://corestack.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.corestack.io/changelog
- group: operate
  href: https://artifacts.apis.io/corestack/changelog/corestack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/corestack-changelog.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.corestack.io/docs/external-apis-62-2603
- group: auth
  title: ''
  type: Compliance
  url: https://www.corestack.io/blog/corestack-achieves-soc-2-type-ii-certification/
- group: agent
  href: https://artifacts.apis.io/corestack/llms/corestack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/corestack-llms.txt
- group: agent
  href: https://artifacts.apis.io/corestack/well-known/corestack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/corestack-well-known.yml
- group: agent
  href: https://artifacts.apis.io/corestack/mcp/corestack-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/corestack-mcp.yml
- group: build
  href: https://artifacts.apis.io/corestack/mcp/corestack-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/corestack-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/corestack/authentication/corestack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/corestack-authentication.yml
- group: auth
  href: https://artifacts.apis.io/corestack/scopes/corestack-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/corestack-scopes.yml
- group: design
  href: https://artifacts.apis.io/corestack/conventions/corestack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/corestack-conventions.yml
- group: design
  href: https://artifacts.apis.io/corestack/errors/corestack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/corestack-problem-types.yml
- group: design
  href: https://artifacts.apis.io/corestack/lifecycle/corestack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/corestack-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/corestack/conformance/corestack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/corestack-conformance.yml
- group: design
  href: https://artifacts.apis.io/corestack/data-model/corestack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/corestack-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/corestack/plans/corestack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/corestack-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/corestack/rate-limits/corestack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/corestack-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/corestack/asyncapi/corestack-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/corestack-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/corestack/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/corestack/overlays/corestack-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/corestack-external-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/corestack/packages/corestack-packages.yml
  title: ''
  type: Packages
  url: packages/corestack-packages.yml
created: '2026-08-11'
description: CoreStack is a multi-cloud governance and security platform that unifies FinOps (cost visibility, budgets, anomaly detection, rightsizing and commitment optimization), CloudOps (workload lifecycle, tagging, automation and self-service), SecOps/compliance (policy guardrails, posture management and continuous assessment against ISO, NIST, HIPAA, PCI DSS, CIS and the AWS Well-Architected Framework), and Graphion, its AI-native CNAPP layer covering SBOM, container findings and vulnerability intelligence, across AWS, Microsoft Azure, Google Cloud and Oracle Cloud Infrastructure. Every one of those capabilities is exposed through the CoreStack External API — a Swagger 2.0 contract of 838 operations across 767 paths, published live at the API host — and, since 2026, through a hosted unified MCP server that surfaces 100 documented tools to AI clients over OAuth or API key headers.
finops:
- has_sources: true
  method: derived
  name: Corestack Finops
  primary_unit: ''
  service_category: ''
  slug: corestack-finops
  template: true
image: https://www.corestack.io/wp-content/uploads/Agentic-Governance-OS-Unified-Governance-Across-Cloud-SaaS-and-AI.png
layout: provider
mcp_servers:
- description: Remote MCP server at cloud.corestack.io over HTTP; 100 tools listed.
  name: CoreStack MCP Server
  slug: corestack
modified: '2026-10-06'
name: CoreStack
nav: Providers
network: true
overview: 'CoreStack publishes 95 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Account Governance API, AI Agent API, and 92 more. Tagged areas include Cloud Governance, FinOps, Cloud Cost Management, Cloud Security Posture Management, and Compliance.


  The CoreStack catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CoreStack''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Corestack Plans Pricing
  plan_count: 6
  slug: corestack-plans-pricing
- name: Corestack Price Estimates
  plan_count: 0
  slug: corestack-price-estimates
random_paper: 23
rate_limits:
- limit_count: 0
  name: Corestack Rate Limits
  slug: corestack-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: CoreStack API Rules
  rule_count: 59
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 17
  slug: corestack-rules
scopes:
- name: Corestack Scopes
  scope_count: 3
  slug: corestack-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.3
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 49.4
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 54.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 178
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
screenshot: https://apis.io/screenshots/corestack/corestack-2026-08-17T080832.png
security:
- kind: authentication
  name: Corestack Authentication
  slug: corestack-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Corestack Domain Security
  slug: corestack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: corestack-authenticate-and-scope
  slug: corestack-authenticate-and-scope
- name: corestack-investigate-cost-anomaly
  slug: corestack-investigate-cost-anomaly
- name: corestack-triage-graphion-findings
  slug: corestack-triage-graphion-findings
slug: corestack
tags:
- Cloud Governance
- FinOps
- Cloud Cost Management
- Cloud Security Posture Management
- Compliance
- Multi-Cloud
- CNAPP
- Policy as Code
- cloudops
- MCP
- Agent-Native
- Kubernetes
website: https://www.corestack.io/
---
