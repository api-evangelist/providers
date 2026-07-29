---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 3
  name: Lightning Social Ventures Agentic Access
  operation_count: 9
  slug: lightning-social-ventures-agentic-access
  summary_line: 9 operations · 3 acting · 3 human-in-the-loop
api_count: 3
apis:
- description: The Applications API from Lightning Social Ventures — 5 operation(s) for applications.
  name: Lightning Social Ventures Applications API
  slug: lightning-social-ventures-applications-api
- description: The Support Schemes API from Lightning Social Ventures — 1 operation(s) for support schemes.
  name: Lightning Social Ventures Support Schemes API
  slug: lightning-social-ventures-support-schemes-api
- description: The Webhooks API from Lightning Social Ventures — 2 operation(s) for webhooks.
  name: Lightning Social Ventures Webhooks API
  slug: lightning-social-ventures-webhooks-api
artifact_total: 8
asyncapis:
- description: ''
  name: Lightning Social Ventures Webhooks
  slug: lightning-social-ventures-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://lightningreach.org/
- group: docs
  title: ''
  type: APIReference
  url: https://api.lightningreach.org/docs
- group: operate
  title: ''
  type: Support
  url: https://www.lightningreach.org/support
- group: start
  title: ''
  type: SignUp
  url: https://apply.lightningreach.org/signup
- group: start
  title: ''
  type: Login
  url: https://apply.lightningreach.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lightningreach.org/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lightningreach.org/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightning-social-ventures-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightning-social-ventures-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lightning-social-ventures-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightning-social-ventures-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightning-social-ventures-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightning-social-ventures-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightning-social-ventures-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightning-social-ventures-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightning-social-ventures-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightning-social-ventures-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightning-social-ventures-submit-application.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightning-social-ventures-review-and-decide.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightning-social-ventures-refer-and-track.md
created: '2026-07-17'
description: Lightning Social Ventures is the UK social-impact company behind Lightning Reach, a financial support platform that connects people facing hardship to grants, benefits, vouchers and assistance schemes through a single profile and eligibility match. Councils, housing associations, charities, utilities and banks use the platform to run and administer their own support programmes, from application intake through evidence review to award and payment. Lightning Reach operates a partner-facing REST API that exposes support schemes, application submission and referral, applicant evidence assets, decision and award recording, and webhook subscriptions with public-key signature verification.
image: https://static.wixstatic.com/media/b5277c_f5fd0014edb2463184acc145d446cc23~mv2.png/v1/fill/w_2400,h_1260,al_c/b5277c_f5fd0014edb2463184acc145d446cc23~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: lightning-social-ventures-mcp.yml
  slug: lightning-social-ventures-mcpyml
modified: '2026-07-19'
name: Lightning Social Ventures
nav: Providers
network: true
overview: 'Lightning Social Ventures publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Support Schemes API, and Webhooks API. Tagged areas include Company, Financial Inclusion, Grants, Social Impact, and Nonprofit.


  The Lightning Social Ventures catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lightning Social Ventures'' developer surface includes API reference, support, signup flow, and 18 more developer resources.'
random_paper: 40
score:
  band: thin
  composite: 34.7
  delta: -1.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 47.5
    developer_ergonomics: 21.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightning-social-ventures/refs/heads/main/screenshots/lightning-social-ventures-2026-07-25T225125.png
security:
- kind: authentication
  name: Lightning Social Ventures Authentication
  slug: lightning-social-ventures-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lightning Social Ventures Domain Security
  slug: lightning-social-ventures-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lightning-social-ventures
tags:
- Company
- Financial Inclusion
- Grants
- Social Impact
- Nonprofit
- Housing
- Government
- Welfare Benefits
- United Kingdom
website: https://lightningreach.org/
---
