---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.5
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Read-only JSON catalog API built on API Platform (Symfony) that backs the santeacademie.com websites and the play.santeacademie.com learner app. Ten GET operations cover training-topic and resource se
  name: Santé Académie Frontstage API
  slug: santé-académie-frontstage-api
- description: Read-only JSON "connector" API generated with swagger-php on the same frontstage host, used by the marketing site and funding simulator. Fourteen GET operations cover article and topic search, per-slu
  name: Santé Académie Connector API
  slug: santé-académie-connector-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.santeacademie.com/
- group: start
  title: ''
  type: Login
  url: https://play.santeacademie.com/
- group: operate
  title: ''
  type: Support
  url: https://support.santeacademie.com/fr/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.santeacademie.com/fr/
- group: company
  title: ''
  type: Blog
  url: https://www.santeacademie.com/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/santeacademie
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.notion.so/CGU-V-de-Sant-Acad-mie-b4730d8bf25b47bca95d0e3b2c40ba08
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.notion.so/santeacademie/Politique-de-confidentialit-af621df7e4be4f4182e0879851735568
- group: operate
  title: ''
  type: StatusPage
  url: https://status.santeacademie.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/santeacademie-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/santeacademie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/santeacademie-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/santeacademie-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/santeacademie-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/santeacademie-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/santeacademie-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santeacademie-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/santeacademie-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/santeacademie-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/santeacademie-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/santeacademie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/santeacademie-rate-limits.yml
created: '2026-08-17'
description: Santé Académie is a French continuing-professional-development (DPC) training provider for healthcare professionals — physicians, nurses, pharmacists, pharmacy technicians, nursing assistants and health-facility training managers — delivering e-learning, virtual classrooms and in-person courses funded through ANDPC, FIF-PL, FAF-PM, ANFH and OPCO schemes. The company is Qualiopi-certified, registered with France Compétences and approved by the Agence Nationale du DPC, and says more than 35,000 healthcare professionals have trained on its platform. Its public technical surface is a pair of unauthenticated read-only catalog APIs served from frontstage.santeacademie.com — the API Platform "Frontstage API" and a swagger-php "Connector API" — which expose the training catalog (topics, resources, courses, trainers, funding schemes, professions/métiers, FAQs, testimonials, pharmacy and health-facility lookup) that powers its own websites and learner app.
image: https://www.santeacademie.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Santé Académie MCP Server
  slug: santé-académie-mcp-server
modified: '2026-08-17'
name: Santé Académie
nav: Providers
network: true
overview: 'Santé Académie publishes 2 APIs on the [APIs.io](https://apis.io/) network: Frontstage API and Connector API. Tagged areas include Company, EdTech, Healthcare Training, Continuing Education, and DPC.


  Santé Académie''s developer surface includes support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Santeacademie Plans Pricing
  plan_count: 0
  slug: santeacademie-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Santeacademie Rate Limits
  slug: santeacademie-rate-limits
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 16.7
    contract_quality: 44.4
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 37.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Santeacademie Authentication
  slug: santeacademie-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Santeacademie Domain Security
  slug: santeacademie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: santeacademie
tags:
- Company
- EdTech
- Healthcare Training
- Continuing Education
- DPC
- E-Learning
- France
- Healthcare Professionals
- Course Catalog
- LMS
website: https://www.santeacademie.com/
---
