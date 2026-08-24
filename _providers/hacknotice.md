---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.7
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: 'REST API over the HackNotice threat-intelligence platform: authentication, leak and leak-file search, first-party domain watchlists and alerts, third-party vendor watchlists, hacks and alerts, end-use'
  name: HackNotice API
  slug: hacknotice-api
- description: 'Remote Model Context Protocol server operated by HackNotice, speaking JSON-RPC 2.0 over Streamable HTTP at https://mcp.hacknotice.com:13330/mcp. It publishes 80 tools across third-party, first-party, '
  name: HackNotice MCP Server
  slug: hacknotice-mcp
artifact_total: 8
asyncapis:
- description: ''
  name: Hacknotice Webhooks
  slug: hacknotice-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hacknotice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hacknotice.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.hacknotice.com
- group: docs
  title: ''
  type: Documentation
  url: https://hacknotice.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.hacknotice.com
- group: start
  title: ''
  type: GettingStarted
  url: https://hacknotice.zendesk.com/hc/en-us/articles/13771563959828-Overview-Getting-Started-for-Sec-Teams
- group: operate
  title: ''
  type: Support
  url: https://hacknotice.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://hacknotice.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://hacknotice.com/category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hacknotice.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HackNotice
- group: commercial
  title: ''
  type: Pricing
  url: https://hacknotice.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://hacknotice.com/free-account/
- group: start
  title: ''
  type: Login
  url: https://app.hacknotice.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hacknotice.com/businesstandc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hacknotice.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://api-docs.hacknotice.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hacknotice-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hacknotice-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hacknotice-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/hacknotice-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hacknotice-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hacknotice-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hacknotice-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hacknotice-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hacknotice-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hacknotice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hacknotice-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hacknotice-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hacknotice-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hacknotice-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hacknotice-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hacknotice-llms.txt
created: '2026-08-22'
description: HackNotice is an external threat-intelligence and cyber-risk platform founded in 2018 and headquartered in Austin, Texas. It continuously collects intelligence from ransomware groups, infostealer malware logs, data breaches, dark-web marketplaces, hacker forums and public disclosures, then matches that intelligence against the domains, employees, customers and vendors an organization asks it to watch. The product is organized around four monitoring services — first-party domain monitoring, third-party vendor risk monitoring, end-user credential monitoring, and threat research and investigations — plus AI-assisted vendor security assessments. HackNotice exposes this surface programmatically through a REST API documented as a public Postman collection at api-docs.hacknotice.com, a remote Model Context Protocol server at mcp.hacknotice.com whose tool catalogue answers anonymously, first-party n8n automation nodes on npm, and webhook, Splunk HEC and SIEM/SOAR alert delivery.
image: https://hacknotice.com/wp-content/uploads/2022/12/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: HackNotice MCP Server
  slug: hacknotice-mcp-server
modified: '2026-08-22'
name: HackNotice
nav: Providers
network: true
overview: 'HackNotice publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Threat Intelligence, Cybersecurity, and Dark Web Monitoring.


  The HackNotice catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HackNotice''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Hacknotice Plans Pricing
  plan_count: 4
  slug: hacknotice-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Hacknotice Rate Limits
  slug: hacknotice-rate-limits
score:
  band: strong
  composite: 57.7
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 30.3
    contract_quality: 64.5
    developer_ergonomics: 54.8
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 31.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Hacknotice Authentication
  slug: hacknotice-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Hacknotice Domain Security
  slug: hacknotice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hacknotice
tags:
- Company
- Security
- Threat Intelligence
- Cybersecurity
- Dark Web Monitoring
- Data Breaches
- Credential Monitoring
- Third Party Risk
- Vendor Risk Management
- Vulnerability Management
- Ransomware
- Security Assessments
- Alerts
- Monitoring
website: https://hacknotice.com/
---
