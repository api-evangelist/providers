---
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
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: REST API to monitor and configure the Nasuni resources managed by a Nasuni Management Console, emulating the NMC web interface. Covers account, authentication, Edge Appliance (filer) inventory and con
  name: Nasuni Management Console (NMC) API
  slug: nasuni-management-console-nmc-api
- description: 'Multi-region REST API for the Nasuni Portal control plane — account management, IAM, roles and permissions, serials and software, Edge and File IQ appliance inventory, volumes and volume connections, '
  name: Nasuni Portal API
  slug: nasuni-portal-api
- description: Telemetry API that returns Global File Acceleration performance metrics from the Nasuni NOC service, for use in dashboards and time-series monitoring of accelerated file movement across a Nasuni estat
  name: Global File Acceleration (GFA) Telemetry API
  slug: global-file-acceleration-gfa-telemetry-api
- description: Azure Blob Storage-compatible endpoint that exposes data stored in a Nasuni volume to Azure-native tooling and analytics/AI services without copying the data. Supports container and blob listing, blob
  name: Nasuni Data Service (NDS) for Azure API
  slug: nasuni-data-service-nds-for-azure-api
- description: S3-compatible, read-only endpoints exposed through AWS S3 Object Lambda for accessing data stored in a Nasuni volume from AWS-native analytics and AI services. Supports ListObjectsV2, GetObject and He
  name: Nasuni Data Service (NDS) for AWS API
  slug: nasuni-data-service-nds-for-aws-api
- description: HTTP API providing programmatic access to the filesystem of a Nasuni Edge Appliance — create, read, update and delete files and folders, list shares, and read previous versions. Requires Mobile Access
  name: Nasuni Data API
  slug: nasuni-data-api
- description: Hosted, OAuth 2.0-authenticated Model Context Protocol server that exposes the Nasuni Portal to AI clients (Claude, ChatGPT, Microsoft Copilot Studio) as roughly 40 tools spanning appliance and volume
  name: Nasuni Portal MCP Server
  slug: nasuni-portal-mcp-server
artifact_total: 17
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
overview: 'Nasuni publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Management Console (NMC) API, Portal API, Global File Acceleration (GFA) Telemetry API, and 2 more. Tagged areas include Company, File Storage, Hybrid Cloud, Object Storage, and Enterprise Storage.


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
  composite: 63.3
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 59.6
    developer_ergonomics: 66.1
    discoverability: 72.2
    governance: 30.3
    operational_transparency: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 28.6
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
