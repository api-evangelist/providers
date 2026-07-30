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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST-first JSON API to Contently's vetted creative network and project workflow. Search creators, open NDA-scoped projects, brief and message contributors, submit draft reviews, approve and pay out wo
  name: Contently Talent API
  slug: contently-talent-api
artifact_total: 7
asyncapis:
- description: ''
  name: Contently Webhooks
  slug: contently-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://contently.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.contently.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.contently.com
- group: start
  title: ''
  type: GettingStarted
  url: https://contently.com/platform/talent-api/
- group: company
  title: ''
  type: Blog
  url: https://contently.com/strategist
- group: operate
  title: ''
  type: Support
  url: https://support.contently.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contently
- group: commercial
  title: ''
  type: Pricing
  url: https://contently.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.contently.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contently.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contently.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contently.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contently-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://contently.com/trust/security/
- group: auth
  title: ''
  type: Compliance
  url: https://contently.com/trust/security/
- group: auth
  title: ''
  type: Security
  url: https://contently.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contently-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contently-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contently-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/contently-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/contently-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contently-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contently-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contently-llms.txt
created: '2026-07-17'
description: Contently is an end-to-end content marketing platform pairing enterprise content operations software with a vetted global network of freelance writers, editors, designers, and strategists. Brands use Contently to plan editorial calendars, source and manage creative talent, run review-and-approval workflows, publish across channels, and measure content performance. For developers Contently exposes the Talent API, a REST-first JSON API secured with scoped OAuth2 that lets teams search vetted creators, open NDA-scoped projects, brief and message contributors, submit draft reviews, approve and pay out work, and check funded balances. State-change webhooks (project assigned, draft submitted, review responded, payout released) fan out over Slack, Teams, or raw HTTP, and an official MCP server exposes the same surface to Claude, ChatGPT, and in-house agents. Contently maintains SOC 2 Type II, GDPR, CCPA, and HIPAA (BAA) posture with encrypted PII and NDA-scoped workspaces.
image: https://contently.com/wp-content/themes/contently-redesign-theme/assets/images/brand/og-default-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: contently-mcp.yml
  slug: contently-mcpyml
modified: '2026-07-18'
name: Contently
nav: Providers
network: true
overview: 'Contently publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Marketing, Talent Marketplace, Freelance, and Content Creation.


  The Contently catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Contently''s developer surface includes documentation, getting-started guide, engineering blog, support, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 50.1
  delta: 7.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 43.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/contently/refs/heads/main/screenshots/contently-2026-07-25T210335.png
security:
- kind: authentication
  name: Contently Authentication
  slug: contently-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Contently Domain Security
  slug: contently-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contently Vulnerability Disclosure
  slug: contently-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Contently Trust Center
  slug: contently-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA, HIPAA, FINRA
slug: contently
tags:
- Company
- Content Marketing
- Talent Marketplace
- Freelance
- Content Creation
- Publishing
- Editorial Workflow
- API
website: https://contently.com
---
