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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Curai Agentic Access
  operation_count: 2
  slug: curai-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: The Partner API from Curai — 2 operation(s) for partner.
  name: Curai Partner API
  slug: curai-partner-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.curaihealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gateway.curaihealth.com/partner/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.curaihealth.com/sdk-quickstart-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.curaihealth.com/sdk-quickstart-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/curai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curaihealth.com/terms-of-use
- group: build
  title: ''
  type: Packages
  url: packages/curai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/curai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/curai-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/curai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/curai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curai-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/curai-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/curai-agentic-access.yml
created: '2026-07-17'
description: Curai Health is a virtual-first primary care company offering 24/7 text-based telemedicine to patients across all 50 U.S. states, connecting them with board-certified clinicians for urgent care, chronic disease management, wellness, and preventive screenings, with orders for labs and prescriptions and referrals to specialists. For organizations, health systems, TPAs, and benefits administrators, Curai exposes a Partner API and an embeddable Web SDK (curai-js) that let partners register patients and drop the Curai patient experience into their own web and mobile apps, plus integration via standards-based APIs, Health Information Exchanges (HIE), and webhooks. The Partner API is a small, key-authenticated surface used to onboard patients and obtain session access tokens for the embedded experience.
image: https://cdn.prod.website-files.com/619acca858666ac6759d6e31/61d79c66ae46600b755a13be_logo_webclip.png
layout: provider
mcp_servers:
- description: ''
  name: curai-mcp.yml
  slug: curai-mcpyml
modified: '2026-07-18'
name: Curai
nav: Providers
network: true
overview: 'Curai publishes 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Company, Health, Healthcare, Telemedicine, and Telehealth.


  Curai''s developer surface includes documentation, getting-started guide, authentication, sandbox, and 18 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 40.2
  delta: 1.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.9
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 39.2
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 45.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Curai Authentication
  slug: curai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Curai Domain Security
  slug: curai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curai
tags:
- Company
- Health
- Healthcare
- Telemedicine
- Telehealth
- Primary Care
- Digital Health
- Patient Engagement
- Partner API
- SDK
website: https://www.curaihealth.com/
---
