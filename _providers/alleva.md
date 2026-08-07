---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Alleva REST API ("Alleva Rest Api", OpenAPI 3.0.1) exposes 424 operations across 37 resource groups covering clients, prospects and intake, appointments and sessions, beds/rooms/occupancy and rese
  name: Alleva REST API
  slug: alleva-rest-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://helloalleva.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.helloalleva.com/swagger/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.helloalleva.com/swagger/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.helloalleva.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helloalleva.com/help-center/
- group: company
  title: ''
  type: Blog
  url: https://helloalleva.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://helloalleva.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://helloalleva.com/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://helloalleva.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.helloalleva.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/alleva-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.helloalleva.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alleva-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alleva-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alleva-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alleva-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alleva-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alleva-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alleva-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alleva-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alleva-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alleva-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/alleva-rest-api-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/alleva-tool-crosswalk.yml
created: '2026-08-06'
description: Alleva is a behavioral health operations platform — an EMR/EHR, CRM, admissions, scheduling, clinical documentation, and revenue-cycle system purpose-built for substance use disorder and mental health treatment providers across the residential, PHP, IOP, and outpatient continuum. The platform covers client intake and prospect management, bed and facility census, treatment plans and reviews, discharge planning, medications and e-prescribe, group and individual sessions, shift rounds, incident reports, homework and surveys, and configurable advanced forms, with AI-assisted documentation (Echo ambient scribe, Alleva Intelligence) and a built-in GRC module (InCheck). A public ASP.NET REST API at api.helloalleva.com exposes 424 operations across 37 resource groups under JWT bearer authentication, with a publicly reachable Swagger UI and machine-readable OpenAPI 3.0.1 description. Alleva holds ONC Certification and SOC 2 Type II attestation and publishes a Vanta trust center and an
  Atlassian status page that tracks the REST API as a first-class component.
image: https://helloalleva.com/wp-content/uploads/2026/02/int_4.png
layout: provider
mcp_servers:
- description: ''
  name: alleva-mcp.yml
  slug: alleva-mcpyml
modified: '2026-08-06'
name: Alleva
nav: Providers
network: true
overview: 'Alleva publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include behavioral-health, electronic-health-records, emr, ehr, and substance-use-disorder.


  Alleva''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 64
scopes:
- name: Alleva Scopes
  scope_count: 1
  slug: alleva-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 38.8
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Alleva Authentication
  slug: alleva-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Alleva Domain Security
  slug: alleva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Alleva Trust Center
  slug: alleva-trust-center
  summary_line: SOC 2 Type II, HIPAA, ONC Certification (ONC Health IT Certification Program)
slug: alleva
tags:
- behavioral-health
- electronic-health-records
- emr
- ehr
- substance-use-disorder
- mental-health
- healthcare
- treatment-centers
- clinical-documentation
- revenue-cycle-management
- patient-intake
- healthcare-compliance
website: https://helloalleva.com/
---
