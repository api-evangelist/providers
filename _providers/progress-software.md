---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-09-14'
api_count: 5
apis:
- baseURL: https://automate.chef.io
  baseurl_source: declared
  description: The Chef Automate API is the HTTP surface of Progress Chef Automate, the dashboard and control plane for Chef Infra, Chef InSpec and Chef Habitat. It covers configuration management node and run histo
  name: Chef Automate API
  slug: progress-software-chef-automate
- baseURL: https://{moveit-transfer-host}/api/v1
  baseurl_source: declared
  description: The MOVEit Transfer REST API is an optionally licensed interface that runs at a customer's own MOVEit Transfer server. It exposes authentication, files and folders, folder content, users and groups, a
  name: MOVEit Transfer REST API
  slug: progress-software-moveit-transfer
- baseURL: https://{whatsupgold-host}:9644/api/v1
  baseurl_source: declared
  description: The WhatsUp Gold REST API is the automation interface of Progress WhatsUp Gold network monitoring, served from the customer's own WhatsUp Gold host on port 9644. It covers device discovery and managem
  name: WhatsUp Gold REST API
  slug: progress-software-whatsup-gold
- description: The ShareFile API v3 is the OData-based REST interface of Progress ShareFile, covering Items, Folders, Accounts, Users, Groups, Shares, Access Controls, Capabilities, Connector Groups, Devices, Encryp
  name: ShareFile API v3
  slug: progress-software-sharefile
- description: Sitefinity CMS exposes its content as OData v4 web services under a configurable service route (by default /api/default) on the customer's own Sitefinity instance. The headless API serves content type
  name: Sitefinity CMS Headless OData Services
  slug: progress-software-sitefinity-odata
artifact_total: 14
asyncapis:
- description: ''
  name: Progress Software Sharefile Webhooks
  slug: progress-software-sharefile-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/security/progress-software-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/progress-software-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/security/progress-software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/progress-software-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/security/progress-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/progress-software-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/scopes/progress-software-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/progress-software-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/authentication/progress-software-authentication.yml
  title: ''
  type: Authentication
  url: authentication/progress-software-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.progress.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.progress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.progress.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chef.io/automate/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.sharefile.com/gettingstarted/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.progress.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.progress.com/s/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.progress.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/progress
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telerik.com/purchase.aspx
- group: start
  title: ''
  type: SignUp
  url: https://www.progress.com/trials
- group: start
  title: ''
  type: Login
  url: https://www.progress.com/support/customer-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.progress.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.progress.com/legal/privacy-center
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/openapi/progress-software-chef-automate-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/progress-software-chef-automate-openapi-original.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/openapi/progress-software-moveit-transfer-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/progress-software-moveit-transfer-openapi-original.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/openapi/progress-software-whatsup-gold-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/progress-software-whatsup-gold-openapi-original.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/packages/progress-software-packages.yml
  title: ''
  type: Packages
  url: packages/progress-software-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/packages/progress-software-packages.yml
  title: ''
  type: SDKs
  url: packages/progress-software-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/well-known/progress-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/progress-software-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/well-known/progress-software-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/progress-software-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/mcp/progress-software-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/progress-software-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/mcp/progress-software-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/progress-software-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/llms/progress-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/progress-software-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/overlays/progress-software-chef-automate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/progress-software-chef-automate-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/overlays/progress-software-moveit-transfer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/progress-software-moveit-transfer-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/overlays/progress-software-whatsup-gold-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/progress-software-whatsup-gold-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/conformance/progress-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/progress-software-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.progress.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/errors/progress-software-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/progress-software-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/lifecycle/progress-software-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/progress-software-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chef.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sharefile.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moveitcloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.progress.com/support/maintenance-and-support-policy
- group: auth
  title: ''
  type: Security
  url: https://www.progress.com/security/vulnerability-reporting-policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/conventions/progress-software-conventions.yml
  title: ''
  type: Conventions
  url: conventions/progress-software-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/changelog/progress-software-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/progress-software-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/cli/progress-software-cli.yml
  title: ''
  type: CLI
  url: cli/progress-software-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/components/progress-software-components.yml
  title: ''
  type: Components
  url: components/progress-software-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/data-model/progress-software-data-model.yml
  title: ''
  type: DataModel
  url: data-model/progress-software-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/asyncapi/progress-software-sharefile-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/progress-software-sharefile-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/plans/progress-software-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/progress-software-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/progress-software/refs/heads/main/rate-limits/progress-software-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/progress-software-rate-limits.yml
created: '2026-09-13'
description: 'Progress Software Corporation (NASDAQ: PRGS) is a Burlington, Massachusetts enterprise software company that builds and acquires infrastructure and digital-experience products. Its portfolio spans application development and data (OpenEdge, MarkLogic, Semaphore, DataDirect, Corticon, Nuclia agentic RAG), digital experience (Sitefinity CMS, Sitefinity Insight), developer tooling and UI components (Telerik, Kendo UI, Fiddler, Test Studio), secure file transfer and collaboration (MOVEit, ShareFile), infrastructure automation and monitoring (Chef, WhatsUp Gold, Flowmon, LoadMaster by Kemp). Most of its API surface is shipped inside self-hosted products — MOVEit Transfer, WhatsUp Gold and Chef Automate each publish a full Swagger 2.0 contract against the customer''s own installation — alongside SaaS surfaces such as the ShareFile OData API and Sitefinity''s headless OData services.'
image: https://www.progress.com/images/default-source/default-album/progress-album/images-album/social-image.png
layout: provider
mcp_servers:
- description: ''
  name: Progress Software MCP Server
  slug: progress-software-mcp-server
modified: '2026-09-13'
name: Progress Software
nav: Providers
network: true
overview: 'Progress Software publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chef Automate API, MOVEit Transfer REST API, and WhatsUp Gold REST API. Tagged areas include Company, Enterprise Software, Managed File Transfer, Infrastructure Automation, and Network Monitoring.


  The Progress Software catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Progress Software''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 43 more developer resources.'
plans:
- name: Progress Software Plans Pricing
  plan_count: 21
  slug: progress-software-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Progress Software Rate Limits
  slug: progress-software-rate-limits
scopes:
- name: Progress Software Scopes
  scope_count: 0
  slug: progress-software-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 49.5
    developer_ergonomics: 73.2
    discoverability: 81.5
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Progress Software Authentication
  slug: progress-software-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Progress Software Domain Security
  slug: progress-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Progress Software Vulnerability Disclosure
  slug: progress-software-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Progress Software Trust Center
  slug: progress-software-trust-center
  summary_line: SOC 1, SOC 2 Type I, SOC 2 Type II, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, CSA STAR, TISAX, GDPR
slug: progress-software
tags:
- Company
- Enterprise Software
- Managed File Transfer
- Infrastructure Automation
- Network Monitoring
- Content Management
- Developer Tools
- Data Platform
- Application Development
- DevOps
- Agentic RAG
- File Sharing
website: https://www.progress.com/
---
