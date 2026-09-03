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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Fiddler Everywhere is a cross-platform web debugging proxy for macOS, Windows, and Linux. It captures HTTP and HTTPS traffic, provides API composition capabilities, and includes collaboration features
  name: Fiddler Everywhere
  slug: fiddler-everywhere
- description: The Fiddler Everywhere MCP server is the only programmatic interface Progress Telerik publishes for Fiddler. It is hosted by the desktop application on the loopback interface at http://localhost:8868/
  name: Fiddler Everywhere MCP Server
  slug: fiddler-everywhere-mcp
- description: Fiddler Classic is the original free Windows-based HTTP debugging proxy for logging all HTTP and HTTPS traffic between a computer and the Internet. It supports traffic inspection, breakpoints, and ext
  name: Fiddler Classic
  slug: fiddler-classic
- description: FiddlerCore is the embeddable Fiddler proxy engine for .NET and .NET Standard applications, licensed and delivered as a download rather than through a public package registry. Two first-party helper l
  name: FiddlerCore
  slug: fiddlercore
- description: RETIRED. Fiddler Jam was a browser-based troubleshooting solution that let non-technical users capture HTTP traffic logs and share them with development teams. Progress Software discontinued it on 202
  name: Fiddler Jam
  slug: fiddler-jam
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.telerik.com/fiddler
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telerik.com/fiddler-everywhere/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://www.telerik.com/fiddler/fiddler-everywhere/documentation/agent-tools/fiddler-mcp-server
- group: start
  title: ''
  type: GettingStarted
  url: https://www.telerik.com/fiddler/fiddler-everywhere/documentation/installation-and-setup/quickstart-windows
- group: operate
  title: ''
  type: Support
  url: https://www.telerik.com/support/fiddler-everywhere
- group: company
  title: ''
  type: Blog
  url: https://www.telerik.com/blogs/fiddler
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.telerik.com/fiddler-everywhere
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telerik
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telerik.com/purchase/fiddler
- group: commercial
  title: ''
  type: Plans
  url: plans/fiddler-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fiddler-rate-limits.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.telerik.com/login#register
- group: start
  title: ''
  type: Login
  url: https://www.telerik.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.progress.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.progress.com/legal/privacy-policy
- group: other
  title: ''
  type: Download
  url: https://www.telerik.com/download/fiddler-everywhere
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fiddler-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fiddler-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/fiddler-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fiddler-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fiddler-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fiddler-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fiddler-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/fiddler-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fiddler-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fiddler-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telerik.com
- group: operate
  title: ''
  type: Deprecation
  url: https://www.telerik.com/purchase/license-agreement/fiddler
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fiddler-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fiddler-security.txt
- group: auth
  title: ''
  type: Security
  url: security/fiddler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fiddler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fiddler-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiddler-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telerik
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/telerik
- group: learn
  title: ''
  type: Videos
  url: https://www.youtube.com/c/progresssw
created: '2026-03-26'
description: Fiddler by Telerik (Progress Software) is a family of HTTP debugging proxy tools for capturing, inspecting, modifying, and replaying HTTP and HTTPS traffic between a machine and the internet. The line comprises Fiddler Everywhere (the cross-platform flagship), Fiddler Classic (the original Windows proxy, licensed for non-commercial use only as of 2026-08-03), Fiddler Everywhere Reporter (a free capture-and-report companion) and FiddlerCore (an embeddable proxy engine for .NET). Fiddler publishes no hosted REST API; its programmatic surface is a first-party Model Context Protocol server hosted by the Fiddler Everywhere desktop app on the loopback interface, exposing 20 documented tools that let a coding agent start captures, read sessions and request/response details, apply filters, create traffic-rewriting rules, run a reverse proxy and cache LLM agent calls. Progress also publishes three official Agent Skills for it. Fiddler Jam was retired by Progress on 2024-07-01.
finops:
- name: Fiddler Finops
  service_category: API
  slug: fiddler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiddler.png
layout: provider
mcp_servers:
- description: 'Fiddler Everywhere ships a first-party Model Context Protocol server that lets a coding agent drive the locally installed proxy: start browser/terminal/ network captures, read captured sessions and fu'
  name: Fiddler Everywhere MCP Server
  slug: fiddler-everywhere-mcp-server
modified: '2026-08-29'
name: Fiddler
nav: Providers
network: true
overview: 'Fiddler publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Debugging, HTTP Debugging, HTTP Proxy, Performance Testing, and Traffic Inspection.


  Fiddler''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Fiddler Plans Pricing
  plan_count: 3
  slug: fiddler-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Fiddler Rate Limits
  slug: fiddler-rate-limits
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 47.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiddler/refs/heads/main/screenshots/fiddler-2026-06-20T181148.png
security:
- kind: authentication
  name: Fiddler Authentication
  slug: fiddler-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Fiddler Domain Security
  slug: fiddler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fiddler Vulnerability Disclosure
  slug: fiddler-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Fiddler Trust Center
  slug: fiddler-trust-center
  summary_line: ISO/IEC 27001, SOC 2, HIPAA
slug: fiddler
tags:
- API Debugging
- HTTP Debugging
- HTTP Proxy
- Performance Testing
- Traffic Inspection
- Web Development
- Developer Tools
- MCP
- Agent Tooling
website: https://www.telerik.com/fiddler
---
