---
access_model:
  confidence: high
  label: Paid · Sales-led onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://magicmoment.jp/playbook/faq
  - https://magicmoment.jp/company/contact
  - https://magicmoment.jp/announcements/xip33i39nknwve03om0ym3vw
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Magic Moment Agentic Access
  operation_count: 111
  slug: magic-moment-agentic-access
  summary_line: 111 operations · 51 acting
api_count: 5
apis:
- description: 'Swagger 2.0 contract for the Playbook Salesforce integration service: OAuth 2.0 connection to Salesforce, sync settings, field and ID mappings, engagement sync settings, Salesforce lead statuses / opp'
  name: Magic Moment Playbook Salesforce Integration API
  slug: magic-moment-playbook-salesforce-integration-api
- description: 'Swagger 2.0 contract for the Playbook HubSpot integration service: OAuth 2.0 connection to HubSpot, sync settings and field mappings, Playbook <-> HubSpot ID mappings, engagement sync settings, HubSpo'
  name: Magic Moment Playbook HubSpot Integration API
  slug: magic-moment-playbook-hubspot-integration-api
- description: 'Swagger 2.0 contract for the Playbook office-suite integration service: calendar event create/list/update/delete across connected Google Workspace and Microsoft 365 accounts, mail sync (OAuth results '
  name: Magic Moment Playbook Office Suite Integration API
  slug: magic-moment-playbook-office-suite-integration-api
- description: 'Swagger 2.0 contract for the Playbook call integration service: call-log capture (including MiiTel), call-provider settings, capability tokens for the softphone client, and conference control (create,'
  name: Magic Moment Playbook Call Integration API
  slug: magic-moment-playbook-call-integration-api
- description: 'Swagger 2.0 contract for the Playbook aggregation/reporting service: performance summary and detail by team, rep, and playbook phase, achievement by unit and user, performance targets, playbook phase '
  name: Magic Moment Playbook Reporting API
  slug: magic-moment-playbook-reporting-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magic-moment-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magic-moment-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.magicmoment.jp/
- group: company
  title: ''
  type: Blog
  url: https://www.magicmoment.jp/blog
- group: operate
  title: ''
  type: Support
  url: https://www.magicmoment.jp/company/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.magicmoment.jp/company/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.magicmoment.jp/company/security-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/magic-moment-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/magic-moment-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magic-moment-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magic-moment-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.magicmoment.co.jp
- group: commercial
  title: ''
  type: Pricing
  url: https://magicmoment.jp/playbook/faq
- group: start
  title: ''
  type: Login
  url: https://magicmoment.co.jp/login
- group: commercial
  title: ''
  type: Plans
  url: plans/magic-moment-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magic-moment-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/magic-moment-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/magic-moment-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/magic-moment-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/magic-moment-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Magic Moment is a Tokyo-based AI sales-automation company whose Magic Moment Playbook platform captures real business facts from deals, calls, email, and meetings and writes them back into Salesforce, HubSpot, and other CRMs as structured sales data. Products include Magic Moment Playbook (AI auto-recording SFA/CRM), Playbook Capture, MM Claw, the Revenue Platform performance-based demand service, and the Magic Moment X managed AI department. The company publishes a Playbook API for developers and partners (announced 2024-04-03, documented at developer.magicmoment.co.jp behind the product login) and serves five anonymous Swagger 2.0 contracts for its Playbook integration services on its production hosts — Salesforce, HubSpot, Office suite (Google Workspace / Microsoft 365), call integration (MiiTel, Zoom Phone), and the reporting/aggregation service. The company is ISO/IEC 27001:2022 certified and publishes an llms.txt.
image: https://www.magicmoment.jp/favicon.ico
layout: provider
modified: '2026-08-13'
name: Magic Moment
nav: Providers
network: true
overview: 'Magic Moment publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Playbook Salesforce Integration API, Playbook HubSpot Integration API, Playbook Office Suite Integration API, and 2 more. Tagged areas include Company, Enterprise, Sales, Artificial Intelligence, and CRM.


  Magic Moment''s developer surface includes authentication, engineering blog, support, pricing, and 17 more developer resources.'
plans:
- name: Magic Moment Plans Pricing
  plan_count: 2
  slug: magic-moment-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Magic Moment Rate Limits
  slug: magic-moment-rate-limits
score:
  band: developing
  composite: 41.4
  delta: -0.4
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 30.3
    contract_quality: 46.4
    developer_ergonomics: 25.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magic-moment/refs/heads/main/screenshots/magic-moment-2026-07-25T225847.png
security:
- kind: authentication
  name: Magic Moment Authentication
  slug: magic-moment-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Magic Moment Domain Security
  slug: magic-moment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Magic Moment Trust Center
  slug: magic-moment-trust-center
  summary_line: ISO/IEC 27001:2022
slug: magic-moment
tags:
- Company
- Enterprise
- Sales
- Artificial Intelligence
- CRM
- Sales Automation
- SaaS
- Japan
- Salesforce
- HubSpot
- Sales Enablement
- API
website: https://www.magicmoment.jp/
---
