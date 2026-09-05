---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 28.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: HTTP API and flow-execution surface for DigitalGenius AI agents, including generic DG API calls, flow execution, JSON handling, and the hosted MCP server. Region-scoped EU/US hosts, HTTP Basic (encode
  name: DigitalGenius API
  slug: digitalgenius-api
artifact_total: 6
asyncapis:
- description: ''
  name: Digitalgenius Webhooks
  slug: digitalgenius-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.digitalgenius.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.digitalgenius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalgenius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.digitalgenius.com/docs/generic-digitalgenius-api-call
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.digitalgenius.com/docs/create-basic-token
- group: operate
  title: ''
  type: Support
  url: https://docs.digitalgenius.com/docs/create-a-ticket-on-support-portal.md
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digitalgenius.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitalgenius.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalgenius.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.digitalgenius.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DigitalGenius
- group: agent
  title: ''
  type: MCPServer
  url: mcp/digitalgenius-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digitalgenius-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/digitalgenius-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/digitalgenius-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digitalgenius-packages.yml
- group: design
  title: ''
  type: Components
  url: components/digitalgenius-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digitalgenius-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digitalgenius-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digitalgenius-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digitalgenius-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/digitalgenius-trust-center.yml
created: '2026-07-17'
description: DigitalGenius is an AI agent platform purpose-built for ecommerce and retail customer service. It automates pre- and post-purchase support, fully resolving customer issues such as order tracking, returns and exchanges, subscription management, and warranty claims by orchestrating "flows" that deeply integrate with a brand's existing systems (helpdesks like Zendesk, Freshchat, Freshdesk, Kustomer, Gorgias and Salesforce Service Cloud, plus dozens of carriers, WMS/OMS and logistics providers). Developers connect via a documented HTTP API, an embeddable Genius Chat headless SDK (web, iOS, Android, Expo), and an official hosted Model Context Protocol (MCP) server, with region-scoped EU and US hosts and Auth0-backed platform authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digitalgenius.png
layout: provider
mcp_servers:
- description: ''
  name: DigitalGenius MCP Server
  slug: digitalgenius-mcp-server
modified: '2026-07-18'
name: DigitalGenius
nav: Providers
network: true
overview: 'DigitalGenius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, E-Commerce, Artificial Intelligence, and AI Agents.


  The DigitalGenius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DigitalGenius'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.9
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digitalgenius/refs/heads/main/screenshots/digitalgenius-2026-07-25T212022.png
security:
- kind: authentication
  name: Digitalgenius Authentication
  slug: digitalgenius-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Digitalgenius Domain Security
  slug: digitalgenius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Digitalgenius Trust Center
  slug: digitalgenius-trust-center
  summary_line: trust center published
slug: digitalgenius
tags:
- Company
- Customer Service
- E-Commerce
- Artificial Intelligence
- AI Agents
- Conversational AI
- Customer Support Automation
- Retail
- MCP
website: http://www.digitalgenius.com/
---
