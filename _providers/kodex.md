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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Real-time verification of law enforcement requesters. Pass a requester email address to the lookup endpoint and receive the agent's standing, their agency's status, and the domain's risk level, checke
  name: Kodex Verification API
  slug: verification-api
- description: 'The Request Portal (Targets / Data Production) API creates and manages data requests and automates producing data on verified requests — targets, attachments, and messages. Published endpoint: GET /v1'
  name: Kodex Request Portal API
  slug: request-portal-api
artifact_total: 7
asyncapis:
- description: ''
  name: Kodex Webhooks
  slug: kodex-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kodexglobal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kodexapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kodexapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kodexapi.com/request-portal/reference/request-api
- group: other
  title: ''
  type: ProductOverview
  url: https://www.kodexglobal.com/api
- group: company
  title: ''
  type: Blog
  url: https://www.kodexglobal.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.kodexglobal.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/albatross-technologies
- group: start
  title: ''
  type: SignUp
  url: https://www.kodexglobal.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.kodexglobal.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kodexglobal.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kodexglobal.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kodexglobal.com/
- group: auth
  title: ''
  type: Security
  url: https://www.kodexglobal.com/.well-known/security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.kodexglobal.com/security-compliance
- group: auth
  title: ''
  type: Authentication
  url: authentication/kodex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kodex-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kodex-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kodex-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kodex-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kodex-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kodex-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kodex-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kodex-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kodex-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kodex-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/kodex-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kodex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kodex-llms.txt
created: '2026-07-17'
description: 'Kodex (Albatross Technologies) operates the Kodex Global Network, a platform for managing law enforcement and government data requests — subpoenas, warrants, and emergency disclosure requests — for crypto exchanges, fintechs, banks, and telecommunications companies. The platform covers request intake and automation, requester verification against a network of 15K+ government agencies, threat intelligence, encrypted data production and delivery, cost recovery, and transparency reporting. Kodex exposes the same network programmatically through the Kodex API: a Verification API for real-time requester lookups, a Targets (Data Production) API for automating production on verified requests, and status webhooks for agent credential changes. Developer documentation is published on ReadMe at docs.kodexapi.com as two projects — Request Portal and Verifications API — both authenticated with scoped organization API keys sent in an X-API-Key header.'
image: https://files.readme.io/e8089f1952ef71694a5e2b27b67dd3f885d17bd265d6c6232d9a47fac9308d93-Kodex_PrimaryLogo_COLOR.png
layout: provider
mcp_servers:
- description: ''
  name: kodex-mcp.yml
  slug: kodex-mcpyml
modified: '2026-07-19'
name: Kodex
nav: Providers
network: true
overview: 'Kodex publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Law Enforcement, Compliance, Legal, and Identity Verification.


  The Kodex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kodex''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, changelog, and 22 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 51.4
  delta: 4.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 47.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kodex/refs/heads/main/screenshots/kodex-2026-07-25T224044.png
security:
- kind: authentication
  name: Kodex Authentication
  slug: kodex-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Kodex Domain Security
  slug: kodex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kodex Vulnerability Disclosure
  slug: kodex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kodex
tags:
- Company
- Law Enforcement
- Compliance
- Legal
- Identity Verification
- Government
- Security
- Threat Intelligence
- Data Requests
- Trust and Safety
website: https://www.kodexglobal.com/
---
