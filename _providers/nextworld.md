---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'Inbound REST endpoints into the Nextworld Platform. Every table and logic block created in the platform automatically exposes a set of endpoints for fetching, inserting, updating and deleting records '
  name: Nextworld Platform REST API
  slug: nextworld-platform-rest-api
- description: 'Remote Model Context Protocol server operated by Nextworld at apps.nextworld.net/ai/mcp. An MCP client connects to a single application, project or metadata bundle via a per-user URL generated inside '
  name: Nextworld MCP Server
  slug: nextworld-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Nextworld Events Webhooks
  slug: nextworld-events-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/nextworld-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextworld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextw.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nextw.com/platform/developer-studio
- group: docs
  title: ''
  type: Documentation
  url: https://www.nextw.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.nextw.com/docs/developerstudiointeroperability
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nextw.com/docs/developerstudioquickstart
- group: operate
  title: ''
  type: Support
  url: https://community.nextw.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nextw.com/tech-blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nextw.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.nextworld.net/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextw.com/utility/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextw.com/utility/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextw.com/utility/compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nextworld-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nextworld-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nextworld-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nextworld-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nextworld-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nextworld-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nextworld-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nextworld-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nextworld-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nextworld-events-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nextworld-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nextworld-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nextworld-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/nextworld-packages.yml
created: '2026-08-26'
description: Nextworld is a Denver, Colorado enterprise application platform company founded by members of the original JD Edwards team. Its AI-native, no-code platform lets enterprises build, extend and govern mission-critical applications on top of existing ERP investments — the company markets this as eliminating "Shadow ERP", the layer of spreadsheets and side systems that accumulates when an ERP cannot keep up. The platform surfaces to developers and agents through Developer Studio, Logic Builder, workflow automation, REST-based inbound and outbound endpoints, event emissions to AWS EventBridge, inbound webhooks, and a remote Model Context Protocol (MCP) server at apps.nextworld.net that exposes per-application record and workflow operations to MCP clients such as Claude and ChatGPT. Nextworld reports 600+ enterprise customers across distribution, manufacturing, engineering and construction, telecommunications, utilities, and food and beverage.
image: https://cdn.prod.website-files.com/68fbb4299bc0c9e658c018cc/6978e9a290aa1dc1c6a606c3_Nextworld_OpenGraph.jpg
layout: provider
mcp_servers:
- description: ''
  name: Nextworld MCP Server
  slug: nextworld-mcp-server
modified: '2026-08-26'
name: Nextworld
nav: Providers
network: true
overview: 'Nextworld publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Resource Planning, No-Code, Enterprise Application Platform, and Workflow-Automation.


  The Nextworld catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nextworld''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Nextworld Plans Pricing
  plan_count: 2
  slug: nextworld-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Nextworld Rate Limits
  slug: nextworld-rate-limits
scopes:
- name: Nextworld Scopes
  scope_count: 0
  slug: nextworld-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 49.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Nextworld Authentication
  slug: nextworld-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nextworld Domain Security
  slug: nextworld-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nextworld Vulnerability Disclosure
  slug: nextworld-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Nextworld Trust Center
  slug: nextworld-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISAE 3000, ISAE 3402, CSA STAR Level 1
slug: nextworld
tags:
- Company
- Enterprise Resource Planning
- No-Code
- Enterprise Application Platform
- Workflow-Automation
- Artificial Intelligence
- MCP
- Integration
- Manufacturing
- Distribution
website: https://www.nextw.com/
---
