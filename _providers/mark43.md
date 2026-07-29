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
  band: agent-aware
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
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-07-28'
api_count: 15
apis:
- description: The Associated Records API from Mark43 — 2 operation(s) for associated records.
  name: Mark43 Associated Records API
  slug: mark43-associated-records-api
- description: The Attachments API from Mark43 — 5 operation(s) for attachments.
  name: Mark43 Attachments API
  slug: mark43-attachments-api
- description: The CAD Configuration API from Mark43 — 4 operation(s) for cad configuration.
  name: Mark43 CAD Configuration API
  slug: mark43-cad-configuration-api
- description: The CAD Events API from Mark43 — 10 operation(s) for cad events.
  name: Mark43 CAD Events API
  slug: mark43-cad-events-api
- description: The CAD Tickets API from Mark43 — 1 operation(s) for cad tickets.
  name: Mark43 CAD Tickets API
  slug: mark43-cad-tickets-api
- description: The Cases API from Mark43 — 3 operation(s) for cases.
  name: Mark43 Cases API
  slug: mark43-cases-api
- description: The E911 API from Mark43 — 2 operation(s) for e911.
  name: Mark43 E911 API
  slug: mark43-e911-api
- description: The Evidence API from Mark43 — 5 operation(s) for evidence.
  name: Mark43 Evidence API
  slug: mark43-evidence-api
- description: The GPS API from Mark43 — 1 operation(s) for gps.
  name: Mark43 GPS API
  slug: mark43-gps-api
- description: The Persons API from Mark43 — 8 operation(s) for persons.
  name: Mark43 Persons API
  slug: mark43-persons-api
- description: The Reports API from Mark43 — 38 operation(s) for reports.
  name: Mark43 Reports API
  slug: mark43-reports-api
- description: The Tasks API from Mark43 — 1 operation(s) for tasks.
  name: Mark43 Tasks API
  slug: mark43-tasks-api
- description: The Users API from Mark43 — 7 operation(s) for users.
  name: Mark43 Users API
  slug: mark43-users-api
- description: The Vehicles API from Mark43 — 1 operation(s) for vehicles.
  name: Mark43 Vehicles API
  slug: mark43-vehicles-api
- description: The Warrants API from Mark43 — 5 operation(s) for warrants.
  name: Mark43 Warrants API
  slug: mark43-warrants-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/mark43-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mark43.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mark43.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.mark43.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mark43-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.mark43.com/#developer-terms-of-use-agreement
- group: company
  title: ''
  type: Website
  url: https://mark43.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mark43
- group: design
  title: ''
  type: Conventions
  url: conventions/mark43-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mark43-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mark43-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mark43-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mark43-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mark43-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mark43.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mark43-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mark43 is a cloud-native public safety software company whose platform unifies computer-aided dispatch (CAD), records management (RMS), first-responder mobile applications, evidence and property management, and analytics for law enforcement and public safety agencies. Serving more than 300 federal, state, and local agencies, Mark43 exposes a Partnerships (External) API that lets approved location providers, community-engagement software, and other law-enforcement technologies integrate directly with an agency's Mark43 tenant. The REST API provides endpoints for reports, persons, evidence and chain-of-custody, attachments, CAD events and configuration, warrants, tasks, users, vehicles, and E911 data, secured with HTTP Basic authentication using agency-issued API tokens and returning a consistent JSON response envelope.
image: https://mark43.com/wp-content/uploads/2021/04/cropped-Mark43_logo_horizontal_black-1-1-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: mark43-mcp.yml
  slug: mark43-mcpyml
modified: '2026-07-20'
name: Mark43
nav: Providers
network: true
overview: 'Mark43 publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Associated Records API, Attachments API, CAD Configuration API, and 12 more. Tagged areas include Company, Public Safety, Law Enforcement, Records Management, and Computer-Aided Dispatch.


  Mark43''s developer surface includes documentation, API reference, authentication, and 14 more developer resources.'
random_paper: 68
score:
  band: thin
  composite: 36.4
  delta: -4.8
  facets:
    commercial_clarity: 26.3
    contract_quality: 39.7
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 41.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mark43/refs/heads/main/screenshots/mark43-2026-07-25T230313.png
security:
- kind: authentication
  name: Mark43 Authentication
  slug: mark43-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mark43 Domain Security
  slug: mark43-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mark43 Trust Center
  slug: mark43-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR, CSA STAR, FIPS 140
slug: mark43
tags:
- Company
- Public Safety
- Law Enforcement
- Records Management
- Computer-Aided Dispatch
- CAD
- RMS
- GovTech
- Evidence Management
- Government
website: https://mark43.com/
---
