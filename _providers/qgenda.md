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
api_count: 27
apis:
- description: The Company API from QGenda — 1 operation(s) for company.
  name: QGenda Company API
  slug: qgenda-company-api
- description: The Contacts API from QGenda — 3 operation(s) for contacts.
  name: QGenda Contacts API
  slug: qgenda-contacts-api
- description: The Corporate Entities API from QGenda — 2 operation(s) for corporate entities.
  name: QGenda Corporate Entities API
  slug: qgenda-corporate-entities-api
- description: The Credit Allocation API from QGenda — 2 operation(s) for credit allocation.
  name: QGenda Credit Allocation API
  slug: qgenda-credit-allocation-api
- description: The Daily API from QGenda — 6 operation(s) for daily.
  name: QGenda Daily API
  slug: qgenda-daily-api
- description: The Daily Case API from QGenda — 2 operation(s) for daily case.
  name: QGenda Daily Case API
  slug: qgenda-daily-case-api
- description: The Integration API from QGenda — 1 operation(s) for integration.
  name: QGenda Integration API
  slug: qgenda-integration-api
- description: The Location API from QGenda — 18 operation(s) for location.
  name: QGenda Location API
  slug: qgenda-location-api
- description: The Locations API from QGenda — 2 operation(s) for locations.
  name: QGenda Locations API
  slug: qgenda-locations-api
- description: The Login API from QGenda — 1 operation(s) for login.
  name: QGenda Login API
  slug: qgenda-login-api
- description: The Notification List API from QGenda — 4 operation(s) for notification list.
  name: QGenda Notification List API
  slug: qgenda-notification-list-api
- description: The Organization API from QGenda — 1 operation(s) for organization.
  name: QGenda Organization API
  slug: qgenda-organization-api
- description: The Pay Code API from QGenda — 1 operation(s) for pay code.
  name: QGenda Pay Code API
  slug: qgenda-pay-code-api
- description: The Pay Pool Template API from QGenda — 1 operation(s) for pay pool template.
  name: QGenda Pay Pool Template API
  slug: qgenda-pay-pool-template-api
- description: The Pay Rate API from QGenda — 2 operation(s) for pay rate.
  name: QGenda Pay Rate API
  slug: qgenda-pay-rate-api
- description: The Profile API from QGenda — 1 operation(s) for profile.
  name: QGenda Profile API
  slug: qgenda-profile-api
- description: The Request API from QGenda — 2 operation(s) for request.
  name: QGenda Request API
  slug: qgenda-request-api
- description: The Request Limit API from QGenda — 6 operation(s) for request limit.
  name: QGenda Request Limit API
  slug: qgenda-request-limit-api
- description: The Schedule API from QGenda — 4 operation(s) for schedule.
  name: QGenda Schedule API
  slug: qgenda-schedule-api
- description: The Staff Member API from QGenda — 27 operation(s) for staff member.
  name: QGenda Staff Member API
  slug: qgenda-staff-member-api
- description: The Staff Target API from QGenda — 8 operation(s) for staff target.
  name: QGenda Staff Target API
  slug: qgenda-staff-target-api
- description: The Support API from QGenda — 1 operation(s) for support.
  name: QGenda Support API
  slug: qgenda-support-api
- description: The Tags API from QGenda — 1 operation(s) for tags.
  name: QGenda Tags API
  slug: qgenda-tags-api
- description: The Task API from QGenda — 5 operation(s) for task.
  name: QGenda Task API
  slug: qgenda-task-api
- description: The Time Event API from QGenda — 2 operation(s) for time event.
  name: QGenda Time Event API
  slug: qgenda-time-event-api
- description: The User API from QGenda — 4 operation(s) for user.
  name: QGenda User API
  slug: qgenda-user-api
- description: The Workflows API from QGenda — 5 operation(s) for workflows.
  name: QGenda Workflows API
  slug: qgenda-workflows-api
artifact_total: 31
common:
- group: company
  title: ''
  type: Website
  url: https://www.qgenda.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://restapi.qgenda.com/
- group: docs
  title: ''
  type: Documentation
  url: https://restapi.qgenda.com/
- group: docs
  title: ''
  type: APIReference
  url: https://restapi.qgenda.com/
- group: build
  title: ''
  type: Postman
  url: postman/qgenda-collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/qgenda-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qgenda-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qgenda-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qgenda-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qgenda-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qgenda-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qgenda-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qgenda.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qgenda-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qgenda-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.qgenda.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qgenda-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qgenda-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qgenda-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://www.qgenda.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.qgenda.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qgenda
- group: start
  title: ''
  type: Login
  url: https://login.qgenda.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.qgenda.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qgenda.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qgenda.com/privacy-policy/
created: '2026-07-17'
description: QGenda is a healthcare workforce management platform used by hospitals, health systems, medical groups, and academic medical centers for physician and staff scheduling, on-call management, provider credentialing, time tracking, and clinical operations. Its public REST API (version 2) exposes 146 operations across scheduling, open shifts, rotations, staff members, tasks, time-off requests and limits, pay codes and rates, locations, credentialing, notifications, and workflows. The API uses token-based authentication via a login endpoint, serves JSON over HTTPS (TLS 1.2/1.3 only), supports BR/GZip compression, and offers OData query parameters on select resources. Backed by ICONIQ Capital.
image: https://www.qgenda.com/wp-content/uploads/2025/05/hero-homepage-new.png
layout: provider
mcp_servers:
- description: ''
  name: qgenda-mcp.yml
  slug: qgenda-mcpyml
modified: '2026-07-20'
name: QGenda
nav: Providers
network: true
overview: 'QGenda publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Company API, Contacts API, Corporate Entities API, and 24 more. Tagged areas include Company, Healthcare, Scheduling, Workforce Management, and Physician Scheduling.


  QGenda''s developer surface includes documentation, API reference, authentication, support, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 48.9
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 53.1
  provenance:
    conformance: unknown
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Qgenda Authentication
  slug: qgenda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qgenda Domain Security
  slug: qgenda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qgenda Trust Center
  slug: qgenda-trust-center
  summary_line: SOC 2
slug: qgenda
tags:
- Company
- Healthcare
- Scheduling
- Workforce Management
- Physician Scheduling
- On-Call
- Credentialing
- Clinical Operations
website: https://www.qgenda.com/
---
