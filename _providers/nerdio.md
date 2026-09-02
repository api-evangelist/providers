---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 2
  name: Nerdio Agentic Access
  operation_count: 9
  slug: nerdio-agentic-access
  summary_line: 9 operations · 4 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: REST API for Nerdio Manager for Enterprise. The API is disabled by default and is enabled per install from System > Settings > Integrations, which provisions an Entra ID application under the nerdio-n
  name: Nerdio Manager for Enterprise REST API
  slug: nerdio-manager-for-enterprise-rest-api
- description: REST API for Nerdio Manager for MSP, used by MSPs to automate at the partner and account level what they would otherwise do in the NMM console — creating and managing host pools, session hosts and des
  name: Nerdio Manager for MSP Partner API
  slug: nerdio-manager-for-msp-partner-api
- description: The Health API from Nerdio — 1 operation(s) for health.
  name: Nerdio Health API
  slug: nerdio-health-api
- description: The Install API from Nerdio — 5 operation(s) for install.
  name: Nerdio Install API
  slug: nerdio-install-api
- description: The Invoices API from Nerdio — 2 operation(s) for invoices.
  name: Nerdio Invoices API
  slug: nerdio-invoices-api
- description: The Usage API from Nerdio — 1 operation(s) for usage.
  name: Nerdio Usage API
  slug: nerdio-usage-api
artifact_total: 14
asyncapis:
- description: ''
  name: Nerdio Notifications Webhooks
  slug: nerdio-notifications-webhooks
collections:
- collection_type: open
  name: NMM Distributor API
  slug: open-nerdio-distributor-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nerdio-distributor-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nerdio-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nerdio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nerdio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getnerdio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nmehelp.getnerdio.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://nmm-distributor-api.nerdio.net/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://nmehelp.getnerdio.com/hc/en-us/articles/26124297445901-Getting-Started-with-REST-API-Integration
- group: operate
  title: ''
  type: Support
  url: https://getnerdio.com/support/
- group: company
  title: ''
  type: Blog
  url: https://getnerdio.com/resources/?types%5B%5D=blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Get-Nerdio
- group: operate
  title: ''
  type: Roadmap
  url: https://nmeroadmap.getnerdio.com
- group: commercial
  title: ''
  type: Pricing
  url: https://getnerdio.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://getnerdio.com/nerdio-manager-free-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getnerdio.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getnerdio.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://getnerdio.com/nerdio-trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://getnerdio.com/nerdio-trust-center/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nerdio-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nerdio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://nmehelp.getnerdio.com/hc/en-us/articles/29088961923981-REST-API-Deprecated-Endpoints-and-Properties
- group: auth
  title: ''
  type: Authentication
  url: authentication/nerdio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nerdio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nerdio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nerdio-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/nerdio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nerdio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nerdio-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nerdio-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nerdio-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nerdio-llms.txt
created: '2026-08-01'
description: Nerdio (Nerdio, Inc., founded 2017, Chicago) builds automation and cost-optimization software for Microsoft cloud desktop environments — Azure Virtual Desktop, Windows 365, Intune and Microsoft 365. Its two products are Nerdio Manager for Enterprise (NME), an Azure-hosted management layer that IT departments deploy into their own Azure subscription to provision AVD host pools, manage desktop images, run scripted actions and drive auto-scale, and Nerdio Manager for MSP (NMM), a multi-tenant console managed service providers use to run hundreds of client environments. Both products expose a REST API that customers enable per install (OAuth2 client-credentials against Microsoft Entra ID, with Swagger and a downloadable Postman collection served from the install itself), and Nerdio additionally operates a public, internet-facing Distributor API used by NMM distributors to register, suspend, reactivate and cancel partner installs and to pull usage and invoice data. Nerdio publishes
  a first-party PowerShell module generated from the NME API specification with AutoRest.
image: https://getnerdio.com/wp-content/themes/nrd/assets/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Nerdio MCP Server
  slug: nerdio-mcp-server
modified: '2026-08-01'
name: Nerdio
nav: Providers
network: true
overview: 'Nerdio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Health API, Install API, Invoices API, and 1 more. Tagged areas include Company, Azure Virtual Desktop, Windows 365, Virtual Desktop Infrastructure, and Cloud Desktop Management.


  The Nerdio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nerdio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 47.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nerdio/refs/heads/main/screenshots/nerdio-2026-08-07T184907.png
security:
- kind: authentication
  name: Nerdio Authentication
  slug: nerdio-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Nerdio Domain Security
  slug: nerdio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nerdio Vulnerability Disclosure
  slug: nerdio-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Nerdio Trust Center
  slug: nerdio-trust-center
  summary_line: SOC 2, GDPR
slug: nerdio
tags:
- Company
- Azure Virtual Desktop
- Windows 365
- Virtual Desktop Infrastructure
- Cloud Desktop Management
- Microsoft Intune
- Managed Service Providers
- Cloud Cost Optimization
- Endpoint Management
- IT Automation
website: https://getnerdio.com/
---
