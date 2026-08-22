---
access_model:
  confidence: medium
  label: Customer-only API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://cast.app/pricing.html
  - https://school.cast.app/cast-api/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Read-only REST API for exporting Cast.app campaign performance data — per-campaign engagement summaries, paged engagement events (delivered / view / play / action / feedback) with contact and device d
  name: Cast Analytics API
  slug: cast-analytics-api
- description: Server-side endpoint for minting a personalized Cast presentation permalink for one contact in one project, in play (automated presentation), ama (Ask Me Anything), information (customer center), or p
  name: Cast In-app Delivery API
  slug: cast-in-app-delivery-api
artifact_total: 8
asyncapis:
- description: ''
  name: Cast Corporation Webhooks
  slug: cast-corporation-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cast.app/
- group: docs
  title: ''
  type: Documentation
  url: https://school.cast.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://school.cast.app/
- group: docs
  title: ''
  type: APIReference
  url: https://school.cast.app/cast-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://school.cast.app/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cast-corp
- group: operate
  title: ''
  type: Support
  url: mailto:support@cast.app
- group: operate
  title: ''
  type: Community
  url: https://castcommunity.slack.com/join/shared_invite/zt-xd5ge8yq-sNtPTAXPaSKb0RXMUIAOvA
- group: commercial
  title: ''
  type: Pricing
  url: https://cast.app/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cast.app/terms-and-conditions.html
- group: start
  title: ''
  type: SignUp
  url: https://cast.app/designer/login
- group: company
  title: ''
  type: Blog
  url: https://cast.app/articles.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cast-corporation-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://school.cast.app/security-documents/
- group: auth
  title: ''
  type: Compliance
  url: https://school.cast.app/security-documents/
- group: design
  title: ''
  type: Conformance
  url: conformance/cast-corporation-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cast-corporation-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cast-corporation-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cast-corporation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cast-corporation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cast-corporation-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cast-corporation-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cast-corporation-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/cast-corporation-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/cast-corporation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cast-corporation-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cast-corporation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cast-corporation-rate-limits.yml
- group: operate
  title: ''
  type: SLA
  url: https://school.cast.app/security-docs/service-level-agreement/
created: '2026-07-17'
description: 'Cast Corporation (Cast.app) is an AI-agent platform that automates customer success and post-sales revenue operations for B2B SaaS and technology companies. Its autonomous "digital CSM" agents deliver personalized business reviews, grounded answers, onboarding, usage adoption, churn reduction, renewal influence, and referral workflows across email, in-app, and chat in 17 languages. Cast positions itself as an autopilot layer over an existing stack, connecting natively to 60+ systems including Salesforce, HubSpot, Gainsight, Totango, and data warehouses, with customers such as Pure Storage, HPE, and Aruba Networks. Backed by Techstars, Array Ventures, Soma Capital, New York Venture Partners, Leonis Capital, and Comcast NBCUniversal LiftLabs. Cast publishes two documented REST surfaces: a Cast Analytics API for exporting campaign engagement events and summaries, and an In-app Delivery API plus embeddable loader for minting personalized presentation permalinks inside a customer''s
  own web app. Both are documented in prose only — Cast publishes no OpenAPI, AsyncAPI, GraphQL SDL, or Postman collection.'
image: https://uploads-ssl.webflow.com/5f3f7b0970b95a4ebfda0084/66bd8a8750ec202866f9fbeb_cast-media.gif
layout: provider
modified: '2026-08-13'
name: Cast Corporation
nav: Providers
network: true
overview: 'Cast Corporation publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Success, Artificial Intelligence, AI Agents, and Revenue Operations.


  The Cast Corporation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cast Corporation''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 22 more developer resources.'
plans:
- name: Cast Corporation Plans Pricing
  plan_count: 2
  slug: cast-corporation-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Cast Corporation Rate Limits
  slug: cast-corporation-rate-limits
score:
  band: developing
  composite: 49.0
  delta: -0.7
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 49.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cast-corporation/refs/heads/main/screenshots/cast-corporation-2026-07-25T204732.png
security:
- kind: authentication
  name: Cast Corporation Authentication
  slug: cast-corporation-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cast Corporation Domain Security
  slug: cast-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cast Corporation Trust Center
  slug: cast-corporation-trust-center
  summary_line: SOC 2, SOC 3, GDPR, WCAG 2.2 AA
slug: cast-corporation
tags:
- Company
- Customer Success
- Artificial Intelligence
- AI Agents
- Revenue Operations
- SaaS
- Automation
- Post-Sales
- Analytics
- Webhooks
- Embeddable
website: https://cast.app/
---
