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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
api_count: 14
apis:
- description: The Activity API from Velaris — 4 operation(s) for activity.
  name: Velaris Activity API
  slug: velaris-activity-api
- description: The Attribute Change Log API from Velaris — 1 operation(s) for attribute change log.
  name: Velaris Attribute Change Log API
  slug: velaris-attribute-change-log-api
- description: The Currencies API from Velaris — 3 operation(s) for currencies.
  name: Velaris Currencies API
  slug: velaris-currencies-api
- description: The Custom Objects API from Velaris — 15 operation(s) for custom objects.
  name: Velaris Custom Objects API
  slug: velaris-custom-objects-api
- description: The Entity Management V1 API from Velaris — 24 operation(s) for entity management v1.
  name: Velaris Entity Management V1 API
  slug: velaris-entity-management-v1-api
- description: The Entity Management V2 API from Velaris — 11 operation(s) for entity management v2.
  name: Velaris Entity Management V2 API
  slug: velaris-entity-management-v2-api
- description: The Field Definitions API from Velaris — 2 operation(s) for field definitions.
  name: Velaris Field Definitions API
  slug: velaris-field-definitions-api
- description: The Integrations API from Velaris — 1 operation(s) for integrations.
  name: Velaris Integrations API
  slug: velaris-integrations-api
- description: The Lifecycles API from Velaris — 1 operation(s) for lifecycles.
  name: Velaris Lifecycles API
  slug: velaris-lifecycles-api
- description: The Notes API from Velaris — 2 operation(s) for notes.
  name: Velaris Notes API
  slug: velaris-notes-api
- description: The Surveys API from Velaris — 1 operation(s) for surveys.
  name: Velaris Surveys API
  slug: velaris-surveys-api
- description: The Tasks API from Velaris — 3 operation(s) for tasks.
  name: Velaris Tasks API
  slug: velaris-tasks-api
- description: The Ticketing API from Velaris — 6 operation(s) for ticketing.
  name: Velaris Ticketing API
  slug: velaris-ticketing-api
- description: The Users API from Velaris — 2 operation(s) for users.
  name: Velaris Users API
  slug: velaris-users-api
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://www.velaris.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.velaris.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.velaris.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.velaris.io/
- group: operate
  title: ''
  type: Support
  url: https://www.velaris.io/resources/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.velaris.io/resources/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.velaris.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.euw1.velaris.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.velaris.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.velaris.io/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.velaris.io/resources/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/velaris-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/velaris-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/velaris-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/velaris-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/velaris-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/velaris-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/velaris-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.velaris.io/velaris-security-portal
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/velaris-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/velaris-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/velaris-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/velaris-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/velaris-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/velaris-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.velaris.io/velaris-security-portal
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Velaris is an AI-native Customer Success platform for mid-market and enterprise B2B SaaS teams, centralizing customer data, health scoring, churn and expansion signals, and lifecycle automation with AI agents and a Copilot workspace assistant. Its Public API (developers.velaris.io) exposes organizations, accounts, contacts, opportunities, risks, custom objects, activities, notes, tickets, tasks, users, surveys, currencies, and lifecycle stages over REST with user-scoped bearer tokens. Velaris is a Battery Ventures portfolio company.
image: https://cdn.prod.website-files.com/6082c882cae3781954fcc067/68907364a5c043be5750b3ea_velaris-favicon.png
layout: provider
mcp_servers:
- description: ''
  name: velaris-mcp.yml
  slug: velaris-mcpyml
modified: '2026-07-21'
name: Velaris
nav: Providers
network: true
overview: 'Velaris publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Attribute Change Log API, Currencies API, and 11 more. Tagged areas include Customer Success, AI, SaaS, Customer Data, and CRM.


  Velaris'' developer surface includes documentation, API reference, support, engineering blog, pricing, changelog, authentication, and 20 more developer resources.'
random_paper: 29
score:
  band: developing
  composite: 50.5
  delta: -0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 56.8
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 50.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Velaris Authentication
  slug: velaris-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Velaris Domain Security
  slug: velaris-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Velaris Vulnerability Disclosure
  slug: velaris-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Velaris Trust Center
  slug: velaris-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II, GDPR
slug: velaris
tags:
- Customer Success
- AI
- SaaS
- Customer Data
- CRM
- Analytics
- Automation
- Company
website: https://www.velaris.io/
---
