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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: koppla advertises an "Offene Schnittstelle / API" (open interface / API) as an included capability of its Enterprise plan, alongside a Power BI integration that pushes koppla schedule data into custom
  name: Koppla API
  slug: koppla-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.koppla.de/
- group: start
  title: ''
  type: SignUp
  url: https://my.koppla.de/sign_in
- group: start
  title: ''
  type: Login
  url: https://my.koppla.de/sign_in
- group: operate
  title: ''
  type: Support
  url: https://support.koppla.de/de
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.koppla.de/de
- group: company
  title: ''
  type: Blog
  url: https://www.koppla.de/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.koppla.de/preise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://koppla.notion.site/AGBs-Datenschutz-f321f10b4c35405e8f0ab2d5b74f2f23
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://koppla.notion.site/AGBs-Datenschutz-f321f10b4c35405e8f0ab2d5b74f2f23
- group: other
  title: ''
  type: Imprint
  url: https://www.koppla.de/impressum
- group: operate
  title: ''
  type: Contact
  url: https://www.koppla.de/kontakt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kopplasoftware
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@koppla
- group: operate
  title: ''
  type: StatusPage
  url: https://status.koppla.de/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.koppla.de/
- group: auth
  title: ''
  type: Compliance
  url: https://security.koppla.de/
- group: auth
  title: ''
  type: Security
  url: https://security.koppla.de/
- group: auth
  title: ''
  type: TrustCenter
  url: security/koppla-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/koppla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koppla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/koppla-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koppla-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koppla-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/koppla-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/koppla-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koppla-llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/koppla-graphql.graphql
- group: design
  title: ''
  type: DataModel
  url: data-model/koppla-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koppla-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koppla-error-codes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/koppla-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/koppla-browse-project-schedule.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/koppla-report-site-progress.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/koppla-manage-tickets.md
created: '2026-07-17'
description: koppla GmbH is a Potsdam, Germany based construction technology company building Bauterminplan (construction scheduling) software for general contractors, general planners, project developers and architects. The cloud platform combines lean-construction scheduling, day-to-day project control and collaboration, standardized company-wide templates, reporting and analytics, a jobsite mobile app, AI-assisted import of existing schedules from MS Project, Asta Powerproject and Primavera, and a BIM integration that adds the time dimension (4D) to the model. koppla states that more than 100 construction companies and 600+ live projects run on the platform, covering over EUR 15 billion of managed construction volume. An open interface (API) plus a Power BI integration are offered as part of the Enterprise plan; koppla does not publish a public developer portal, API reference or machine-readable specification, so the API is available under contract rather than via self-service onboarding.
image: https://framerusercontent.com/images/8nYdPiJ2n9S523P0LvOTKwYtTI.png
layout: provider
mcp_servers:
- description: ''
  name: koppla-mcp.yml
  slug: koppla-mcpyml
modified: '2026-07-19'
name: Koppla
nav: Providers
network: true
overview: 'Koppla publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Construction Technology, Project Management, and Scheduling.


  Koppla''s developer surface includes signup flow, support, engineering blog, pricing, YouTube channel, authentication, and 29 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 41.8
  delta: 9.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 43.2
    developer_ergonomics: 21.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 34.2
  previous_composite: 32.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/koppla/refs/heads/main/screenshots/koppla-2026-07-25T224214.png
security:
- kind: authentication
  name: Koppla Authentication
  slug: koppla-authentication
  summary_line: bearer · 1 scheme
- kind: domain-security
  name: Koppla Domain Security
  slug: koppla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Koppla Vulnerability Disclosure
  slug: koppla-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Koppla Trust Center
  slug: koppla-trust-center
  summary_line: ISO/IEC 27001, TISAX, GDPR
slug: koppla
tags:
- Company
- Construction
- Construction Technology
- Project Management
- Scheduling
- Lean Construction
- BIM
- Germany
- SaaS
website: https://www.koppla.de/
---
