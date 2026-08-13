---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Default namespace
  name: Nomad Health Default API
  slug: nomad-health-default-api
artifact_total: 4
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nomad-health-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://nomadhealth.com
- group: docs
  title: ''
  type: APIReference
  url: https://nomadhealth.com/api
- group: company
  title: ''
  type: Blog
  url: https://nomadhealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://nomadhealth.com/faqs
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.nomadhealth.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://nomadhealth.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://nomadhealth.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nomadhealth.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nomadhealth.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NomadHealth
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nomad-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nomad-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nomad-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nomad-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nomad-health-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nomad-health-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nomad-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nomad-health-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nomad-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nomad-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nomad-health-domain-security.yml
created: '2026-08-04'
description: Nomad Health operates a digital marketplace for healthcare travel staffing, connecting travel nurses, allied health professionals and other clinicians directly with healthcare facilities across all fifty U.S. states. The two-sided platform lets clinicians search and apply for travel assignments with transparency on pay rate, shift structure and requirements, while facilities post open positions and manage hiring through a cloud-based system; Nomad Navigators support clinicians through credentialing, onboarding and on-assignment needs. Nomad Health holds the Joint Commission Gold Seal of Approval for Travel Nursing Accreditation and reports more than 400,000 registered clinicians across 50-plus specialties spanning nursing, cath lab, laboratory, occupational therapy, physical therapy, radiology, respiratory therapy, sonography, speech language pathology and surgical technology. The company runs no public developer program, but serves a live Swagger 2.0 contract and a Swagger
  UI from its production application host covering job search, applications, credentialing, placements, facilities and messaging.
image: https://marketing.nomadhealth.com/favicon/apple-icon-114x114.png
layout: provider
mcp_servers:
- description: ''
  name: nomad-health-mcp.yml
  slug: nomad-health-mcpyml
modified: '2026-08-04'
name: Nomad Health
nav: Providers
network: true
overview: 'Nomad Health publishes 1 API on the [APIs.io](https://apis.io/) network: Default API. Tagged areas include Company, Healthcare, Staffing, Jobs, and Marketplace.


  Nomad Health''s developer surface includes API reference, engineering blog, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 35.8
    developer_ergonomics: 27.7
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 31.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomad-health/refs/heads/main/screenshots/nomad-health-2026-08-07T185440.png
security:
- kind: authentication
  name: Nomad Health Authentication
  slug: nomad-health-authentication
  summary_line: session-cookie · 1 scheme
- kind: domain-security
  name: Nomad Health Domain Security
  slug: nomad-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nomad-health
tags:
- Company
- Healthcare
- Staffing
- Jobs
- Marketplace
- Travel Nursing
- Allied Health
- Credentialing
- Recruiting
- Human Resources
website: https://nomadhealth.com
---
