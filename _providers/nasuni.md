---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-02'
api_count: 14
apis:
- baseURL: https://hostname/mobileapi/1
  baseurl_source: declared
  description: HTTP API providing programmatic access to the filesystem of a Nasuni Edge Appliance — create, read, update and delete files and folders, list shares, and read previous versions. Requires Mobile Access
  name: Nasuni Data API
  slug: nasuni-data-api
- description: Hosted, OAuth 2.0-authenticated Model Context Protocol server that exposes the Nasuni Portal to AI clients (Claude, ChatGPT, Microsoft Copilot Studio) as roughly 40 tools spanning appliance and volume
  name: Nasuni Portal MCP Server
  slug: nasuni-portal-mcp-server
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Account API from Nasuni — 4 operation(s) for account.
  name: Nasuni Account API
  slug: nasuni-account-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Account Management API from Nasuni — 3 operation(s) for account management.
  name: Nasuni Account Management API
  slug: nasuni-account-management-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Activity Logs API from Nasuni — 2 operation(s) for activity logs.
  name: Nasuni Activity Logs API
  slug: nasuni-activity-logs-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The AI Activate API from Nasuni — 5 operation(s) for ai activate.
  name: Nasuni AI Activate API
  slug: nasuni-ai-activate-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Auth API from Nasuni — 5 operation(s) for auth.
  name: Nasuni Auth API
  slug: nasuni-auth-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Cloud Credentials API from Nasuni — 5 operation(s) for cloud credentials.
  name: Nasuni Cloud Credentials API
  slug: nasuni-cloud-credentials-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Configuration API from Nasuni — 5 operation(s) for configuration.
  name: Nasuni Configuration API
  slug: nasuni-configuration-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Data API from Nasuni — 1 operation(s) for data.
  name: Nasuni Data API
  slug: nasuni-data-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Edge Appliances (Edge) API from Nasuni — 4 operation(s) for edge appliances (edge).
  name: Nasuni Edge Appliances (Edge) API
  slug: nasuni-edge-appliances-edge-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The File IQ Appliances (File IQ) API from Nasuni — 2 operation(s) for file iq appliances (file iq).
  name: Nasuni File IQ Appliances (File IQ) API
  slug: nasuni-file-iq-appliances-file-iq-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Filers API from Nasuni — 30 operation(s) for filers.
  name: Nasuni Filers API
  slug: nasuni-filers-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Global File Accelerator (GFA) API from Nasuni — 2 operation(s) for global file accelerator (gfa).
  name: Nasuni Global File Accelerator (GFA) API
  slug: nasuni-global-file-accelerator-gfa-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Health API from Nasuni — 1 operation(s) for health.
  name: Nasuni Health API
  slug: nasuni-health-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The IAM API from Nasuni — 13 operation(s) for iam.
  name: Nasuni IAM API
  slug: nasuni-iam-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Index API from Nasuni — 1 operation(s) for index.
  name: Nasuni Index API
  slug: nasuni-index-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Jobs API from Nasuni — 3 operation(s) for jobs.
  name: Nasuni Jobs API
  slug: nasuni-jobs-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The ?list Type=2 API from Nasuni — 1 operation(s) for ?list type=2.
  name: Nasuni ?list Type=2 API
  slug: nasuni-list-type-2-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Messages API from Nasuni — 2 operation(s) for messages.
  name: Nasuni Messages API
  slug: nasuni-messages-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Nasuni Data Service (NDS) API API from Nasuni — 3 operation(s) for nasuni data service (nds) api.
  name: Nasuni Nasuni Data Service (NDS) API
  slug: nasuni-nasuni-data-service-nds-api-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Nasuni Data Service (NDS) AWS API API from Nasuni — 2 operation(s) for nasuni data service (nds) aws api.
  name: Nasuni Nasuni Data Service (NDS) AWS API
  slug: nasuni-nasuni-data-service-nds-aws-api-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Notifications API from Nasuni — 3 operation(s) for notifications.
  name: Nasuni Notifications API
  slug: nasuni-notifications-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: '**Requires Premium Ops IQ license** (`ops-iq-premium`). The Ops IQ Telemetry API is available only to accounts with the Premium Ops IQ license bit enabled. Reach out to your Nasuni account team or Sup'
  name: Nasuni Ops IQ API
  slug: nasuni-ops-iq-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Portal API API from Nasuni — 1 operation(s) for portal api.
  name: Nasuni Portal API
  slug: nasuni-portal-api-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Serials API from Nasuni — 3 operation(s) for serials.
  name: Nasuni Serials API
  slug: nasuni-serials-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Software API from Nasuni — 2 operation(s) for software.
  name: Nasuni Software API
  slug: nasuni-software-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The UniFS As A Service (UaaS) API from Nasuni — 10 operation(s) for unifs as a service (uaas).
  name: Nasuni UniFS As A Service (UaaS) API
  slug: nasuni-unifs-as-a-service-uaas-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Volume Connections API from Nasuni — 1 operation(s) for volume connections.
  name: Nasuni Volume Connections API
  slug: nasuni-volume-connections-api
- baseURL: https://hostname/api/v1.2
  baseurl_source: declared
  description: The Volumes API from Nasuni — 52 operation(s) for volumes.
  name: Nasuni Volumes API
  slug: nasuni-volumes-api
artifact_total: 40
asyncapis:
- description: ''
  name: Nasuni File Iq Alerts Webhooks
  slug: nasuni-file-iq-alerts-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasuni-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nasuni-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasuni-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasuni.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.nasuni.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nasuni.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.nasuni.com/api/nmc/v120/reference/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nasuni.com/docs/nasuni-quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://www.nasuni.com/customers/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.nasuni.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.nasuni.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nasuni-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nasuni.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://portal.nasuni.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nasuni.com/legal/master-subscription-and-services-agreement-2026/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasuni.com/legal/privacy-notice-2026/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nasuni.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/nasuni-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nasuni-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nasuni-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nasuni-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/nasuni-nmc-v1-2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/nasuni-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nasuni-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nasuni-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nasuni-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nasuni-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nasuni-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nasuni-file-iq-alerts-webhooks.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nasuni-file-iq-alert-webhook-payload.schema.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nasuni-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasuni-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nasuni-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nasuni-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nasuni-tool-crosswalk.yml
created: '2026-08-26'
description: 'Nasuni is an enterprise hybrid-cloud file data platform that consolidates distributed NAS and file servers into UniFS, a cloud-native global file system backed by customer-owned object storage (Azure Blob, Amazon S3, Google Cloud Storage and S3-compatible on-prem targets). Edge appliances cache hot data at each site while every version is written immutably to the cloud, delivering multi-site collaboration with Global File Lock and Global File Acceleration, continuous versioning, rapid ransomware recovery, and file data services for analytics and AI. Nasuni exposes a substantial programmable surface: the REST Nasuni Management Console (NMC) API for fleet, volume, share, snapshot and appliance management; the multi-region Nasuni Portal API for account, IAM, Ops IQ telemetry, UaaS and job orchestration; the Global File Acceleration Telemetry API; Nasuni Data Service (NDS) endpoints that present Nasuni volumes through Azure Blob- and Amazon S3-compatible interfaces; the Nasuni
  Data API for appliance filesystem access; and a hosted, OAuth 2.0 Portal MCP Server plus open-source local MCP servers that make the platform callable by AI agents.'
image: https://www.nasuni.com/wp-content/uploads/2026/04/nasuni-featured-image-logo-540x283.png
json_schemas:
- name: Nasuni File IQ Alert Webhook Payload
  property_count: 6
  slug: nasuni-file-iq-alert-webhook-payload.schema
layout: provider
mcp_servers:
- description: ''
  name: Nasuni MCP servers
  slug: nasuni-mcp-servers
modified: '2026-08-26'
name: Nasuni
nav: Providers
network: true
overview: 'Nasuni publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Data API, Account API, Account Management API, and 26 more. Tagged areas include Company, File Storage, Hybrid Cloud, Object Storage, and Enterprise Storage.


  The Nasuni catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nasuni''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Nasuni Plans Pricing
  plan_count: 5
  slug: nasuni-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Nasuni Rate Limits
  slug: nasuni-rate-limits
scopes:
- name: Nasuni Scopes
  scope_count: 0
  slug: nasuni-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 61.0
    developer_ergonomics: 66.1
    discoverability: 63.0
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 60.9
  provenance:
    conformance: first-party
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasuni/refs/heads/main/screenshots/nasuni-2026-09-02T150723.png
security:
- kind: authentication
  name: Nasuni Authentication
  slug: nasuni-authentication
  summary_line: apiKey/http/oauth2 · 24 schemes
- kind: domain-security
  name: Nasuni Domain Security
  slug: nasuni-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nasuni Vulnerability Disclosure
  slug: nasuni-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Nasuni Trust Center
  slug: nasuni-trust-center
  summary_line: SOC 2 Type II, SOC 2 Type I, ISO 27001, HIPAA, CSA STAR
slug: nasuni
tags:
- Company
- File Storage
- Hybrid Cloud
- Object Storage
- Enterprise Storage
- Data Management
- Backup and Recovery
- Ransomware Protection
- Infrastructure
- Observability
- MCP
- agent-native
website: https://www.nasuni.com/
---
