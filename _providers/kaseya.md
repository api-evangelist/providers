---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-12'
api_count: 7
apis:
- description: The Kaseya BMS (Business Management Solution) V2 REST API exposes the professional services automation surface of BMS — tickets, accounts, contacts, contracts, opportunities, projects, timesheets, exp
  name: Kaseya BMS API 2.0
  slug: bms
- description: The Datto|Autotask PSA REST API is Kaseya's largest published contract — a Swagger 2.0 document with 2,077 paths and 3,009 operations covering companies, contacts, tickets, projects, tasks, contracts,
  name: Datto Autotask PSA REST API
  slug: autotask-psa
- description: The Datto RMM REST API v2 gives programmatic access to the remote monitoring and management platform — devices, sites, site variables, alerts, jobs, audit data, filters, users, activity logs and accou
  name: Datto RMM API v2
  slug: datto-rmm
- description: The IT Glue API is a JSON:API-conformant REST interface over the IT Glue IT-documentation platform — organizations, configurations, contacts, locations, passwords, documents, flexible assets and flexi
  name: IT Glue API
  slug: it-glue
- description: The Kaseya VSA 9 REST API lets third-party applications integrate with a VSA server and perform many of the tasks a VSA user performs in the product — agents, machine groups, organizations, assets, au
  name: Kaseya VSA 9 REST API
  slug: vsa9
- description: VSA 10 (formerly VSA X) exposes a REST API browsable from each tenant's own server at /api, with access controlled through VSA access tokens that carry explicit REST API (Read, Write) scopes, and thro
  name: Kaseya VSA 10 API
  slug: vsa10
- description: 'myITprocess is Kaseya''s strategic IT planning and QBR (quarterly business review) product for MSPs. It ships a REST API documented with Swagger UI at reporting.live.myitprocess.com, covering clients, '
  name: myITprocess API
  slug: myitprocess
artifact_total: 14
asyncapis:
- description: ''
  name: Kaseya Webhooks
  slug: kaseya-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kaseya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://helpdesk.kaseya.com/hc/en-gb
- group: docs
  title: ''
  type: APIReference
  url: https://api.bms.kaseya.com/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.itglue.kaseya.com/help/Content/1-admin/it-glue-api/getting-started-with-the-it-glue-api.html
- group: operate
  title: ''
  type: Support
  url: https://www.kaseya.com/customer-success/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.kaseya.com/hc/en-gb
- group: operate
  title: ''
  type: Community
  url: https://community.kaseya.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kaseya.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kaseya
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kaseya.com/request/pricing/
- group: start
  title: ''
  type: Login
  url: https://one.kaseya.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kaseya.com/legal/kaseya-master-agreement/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.kaseya.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kaseya.com/legal/kaseya-privacy-statement/
- group: commercial
  title: ''
  type: Legal
  url: https://www.kaseya.com/legal/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kaseya.com/
- group: auth
  title: ''
  type: Security
  url: https://www.kaseya.com/trust-center/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.kaseya.com/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.kaseya.com/trust-center/soc-report/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kaseya-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaseya-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kaseya-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/kaseya-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kaseya-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kaseya-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kaseya-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kaseya-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kaseya-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kaseya-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kaseya-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kaseya-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kaseya-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kaseya-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kaseya-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kaseya-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kaseya-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'Kaseya is a Miami-based provider of IT and security management software for managed service providers (MSPs) and internal IT teams, delivering its portfolio through the Kaseya 365 and IT Complete platforms. The company owns a large family of separately-branded products, several of which ship public REST APIs: Kaseya BMS (business management / PSA), Datto Autotask PSA, Datto RMM (remote monitoring and management), Kaseya VSA 9 and VSA 10 (endpoint management), IT Glue (IT documentation), myITprocess, Datto BCDR, SaaS Alerts, RocketCyber, Graphus, Spanning and Vonahi vPenTest. Kaseya publishes machine-readable contracts for three of these surfaces — the BMS API 2.0 (OpenAPI 3.0.1), the Datto|Autotask PSA REST API (Swagger 2.0, 3,000+ operations) and the Datto RMM API v2 (OpenAPI 3.1.0) — with the remainder documented in HTML help systems or behind tenant authentication.'
image: https://www.kaseya.com/wp-content/uploads/2023/04/kaseya-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: kaseya-mcp.yml
  slug: kaseya-mcpyml
modified: '2026-08-01'
name: Kaseya
nav: Providers
network: true
overview: 'Kaseya publishes 3 APIs on the [APIs.io](https://apis.io/) network: BMS API 2.0, Datto Autotask PSA REST API, and Datto RMM API v2. Tagged areas include Company, IT Management, Managed Service Providers, Remote Monitoring and Management, and Professional Services Automation.


  The Kaseya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kaseya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, legal docs, and 30 more developer resources.'
random_paper: 38
rate_limits:
- limit_count: 4
  name: Kaseya Rate Limits
  slug: kaseya-rate-limits
score:
  band: strong
  composite: 57.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.7
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 86.8
  previous_composite: 57.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaseya/refs/heads/main/screenshots/kaseya-2026-08-07T171103.png
security:
- kind: authentication
  name: Kaseya Authentication
  slug: kaseya-authentication
  summary_line: http/apiKey/oauth2 · 6 schemes
- kind: domain-security
  name: Kaseya Domain Security
  slug: kaseya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kaseya Vulnerability Disclosure
  slug: kaseya-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kaseya Trust Center
  slug: kaseya-trust-center
  summary_line: SOC 2 Type II, CMMC (Cybersecurity Maturity Model Certification)
slug: kaseya
tags:
- Company
- IT Management
- Managed Service Providers
- Remote Monitoring and Management
- Professional Services Automation
- Cybersecurity
- Backup and Disaster Recovery
- IT Documentation
- Endpoint Management
- Service Desk
- Ticketing
- Compliance
website: https://www.kaseya.com/
---
