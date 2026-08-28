---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The Reprise MCP server is a remote Model Context Protocol endpoint that lets any MCP-compatible AI assistant — Claude, ChatGPT, Codex, Microsoft Copilot, Gemini, Cursor — drive the whole Reprise platf
  name: Reprise MCP Server
  slug: mcp
- description: The Clone Environment Data API returns viewer session analytics for published Reprise Clone Environment demos as a single JSON pipe (api_replicate_analytics). The response carries a meta block of colu
  name: Reprise Clone Environment Data API
  slug: data-api
- description: 'The HTML Environment Data API returns click-level viewer activity for published Reprise HTML Environment (Product Tour) demos through a single endpoint, replay_session_activity. Each record describes '
  name: Reprise HTML Environment Data API
  slug: html-environment-data-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.reprise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://reprise.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://reprise.zendesk.com/hc/en-us/articles/18940321925659-HTML-Environment-Data-API
- group: start
  title: ''
  type: GettingStarted
  url: https://reprise.zendesk.com/hc/en-us/articles/12519794531099-New-to-Reprise-Get-Started-Here
- group: operate
  title: ''
  type: Support
  url: https://reprise.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetReprise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getreprise
- group: other
  title: ''
  type: X
  url: https://x.com/getreprise
- group: company
  title: ''
  type: Blog
  url: https://www.reprise.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reprise.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.reprise.com/get-started-reprise
- group: start
  title: ''
  type: Login
  url: https://app.getreprise.com/auth/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reprise.com/tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reprise.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reprise.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/reprise-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.reprise.com/platform/enterprise-scale-and-security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reprise-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/reprise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reprise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reprise-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reprise-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reprise-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reprise-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reprise-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reprise-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reprise-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reprise-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reprise-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reprise-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reprise-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/reprise-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/reprise-packages.yml
created: 2026-06-13
description: Reprise is the enterprise demo creation platform sales, presales and marketing teams use to build no-code interactive product demos — guided Product Tours captured from a live front end, Data Injection that overlays prospect-specific data on a real application, and full Clone Environments that reproduce an application down to the code. Reprise ships a remote Model Context Protocol server at app.getreprise.com that exposes more than 100 atomic demo-authoring tools to any MCP client (Claude, ChatGPT, Copilot, Gemini, Codex) over OAuth 2.0 authorization code with PKCE, plus two token-authenticated analytics Data APIs (HTML Environment replay_session_activity and Clone Environment api_replicate_analytics) for pulling click-level demo engagement data into a warehouse. Reprise is SOC 2 Type 2 and ISO/IEC 27001:2022 certified, with SSO and RBAC in every package, and has served over 20 million demos for customers including Databricks, ServiceNow, Cloudera, 1Password, Commvault and iCIMS.
finops:
- name: Reprise Finops
  service_category: ''
  slug: reprise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reprise.png
jsonld:
- class_count: 0
  name: Reprise Context
  property_count: 0
  slug: reprise-context
layout: provider
mcp_servers:
- description: ''
  name: Reprise MCP Server
  slug: reprise-mcp-server
modified: 2026-08-13
name: Reprise
nav: Providers
network: true
overview: 'Reprise publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Demo Automation, Product Tours, Sales Demos, Interactive Demos, and Sandbox Environments.


  The Reprise catalog on APIs.io includes 1 JSON-LD context.


  Reprise''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Reprise Plans Pricing
  plan_count: 0
  slug: reprise-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Reprise Rate Limits
  slug: reprise-rate-limits
scopes:
- name: Reprise Scopes
  scope_count: 1
  slug: reprise-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.5
  delta: 1.6
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 13.3
    developer_ergonomics: 54.8
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 42.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reprise/refs/heads/main/screenshots/reprise-2026-06-20T192911.png
security:
- kind: authentication
  name: Reprise Authentication
  slug: reprise-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Reprise Domain Security
  slug: reprise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Reprise Trust Center
  slug: reprise-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022
slug: reprise
tags:
- Demo Automation
- Product Tours
- Sales Demos
- Interactive Demos
- Sandbox Environments
- Enterprise Sales
- Marketing Technology
- Sales Enablement
- MCP
- Agent Tooling
- Demo Analytics
website: https://www.reprise.com/
---
