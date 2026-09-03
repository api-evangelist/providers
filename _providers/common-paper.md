---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'REST API for managing Common Paper agreements and templates — list, create, send, void, reassign, download, and share agreements; manage templates, attachments, users, organizations, invitations, and '
  name: Common Paper API
  slug: common-paper-api
artifact_total: 5
asyncapis:
- description: ''
  name: Common Paper Webhooks
  slug: common-paper-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/common-paper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commonpaper.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.commonpaper.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.commonpaper.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.commonpaper.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://api.commonpaper.com/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/common-paper-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/common-paper-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/common-paper-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/common-paper-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/common-paper-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/common-paper-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/common-paper-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commonpaper.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/common-paper-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/common-paper-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.commonpaper.com/
- group: operate
  title: ''
  type: Support
  url: https://help.commonpaper.com/en/
- group: company
  title: ''
  type: Blog
  url: https://commonpaper.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commonpaper
- group: commercial
  title: ''
  type: Pricing
  url: https://commonpaper.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.commonpaper.com/auth/auth0?screen_hint=signup
- group: start
  title: ''
  type: Login
  url: https://app.commonpaper.com/auth/auth0?screen_hint=signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commonpaper.com/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commonpaper.com/privacy-policy
created: '2026-07-17'
description: Common Paper is a contract management platform that helps revenue, legal, and operations teams build, negotiate, sign, and manage commercial agreements in minutes using a library of committee-drafted standard agreements (Cloud Service Agreement, Mutual NDA, DPA, BAA, Professional Services, Partnership, Software License, Pilot, Design Partner, and Letter of Intent) paired with AI-assisted contract review. The company exposes a public REST API at api.commonpaper.com/v1 with Bearer-token authentication, JSON:API read responses, Ransack filtering, offset pagination, a documented webhook catalog, an agentic account-provisioning flow, and an official hosted MCP server plus a published Claude agent skill, so agents and integrations can list, create, send, void, reassign, and download agreements and templates programmatically.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/common-paper.png
layout: provider
mcp_servers:
- description: ''
  name: Common Paper MCP Server
  slug: common-paper-mcp-server
modified: '2026-07-18'
name: Common Paper
nav: Providers
network: true
overview: 'Common Paper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contracts, Contract Management, Legal Tech, and Agreements.


  The Common Paper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Common Paper''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 19 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 43.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/common-paper/refs/heads/main/screenshots/common-paper-2026-07-25T210135.png
security:
- kind: authentication
  name: Common Paper Authentication
  slug: common-paper-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Common Paper Domain Security
  slug: common-paper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: common-paper
tags:
- Company
- Contracts
- Contract Management
- Legal Tech
- Agreements
- SaaS Contracts
- E-Signature
- Webhook
- MCP
website: https://commonpaper.com
---
