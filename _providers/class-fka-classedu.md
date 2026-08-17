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
    agentic_access: derived
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
  score: 34.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Class Fka Classedu Agentic Access
  operation_count: 21
  slug: class-fka-classedu-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 7
apis:
- description: Create, read, update and remove classes.
  name: Class (fka ClassEDU) Classes API
  slug: class-fka-classedu-classes-api
- description: Enroll learners into classes and manage their enrollment records.
  name: Class (fka ClassEDU) Enrollments API
  slug: class-fka-classedu-enrollments-api
- description: Generate a one-time access link for a learner to join a class.
  name: Class (fka ClassEDU) Launch API
  slug: class-fka-classedu-launch-api
- description: Attendance and engagement metrics reporting.
  name: Class (fka ClassEDU) Reporting API
  slug: class-fka-classedu-reporting-api
- description: Manage the scheduled dates (sessions) for a class.
  name: Class (fka ClassEDU) Schedules API
  slug: class-fka-classedu-schedules-api
- description: Manage reusable class templates.
  name: Class (fka ClassEDU) Templates API
  slug: class-fka-classedu-templates-api
- description: Manage non-learner users (instructors, admins).
  name: Class (fka ClassEDU) Users API
  slug: class-fka-classedu-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Class Developer Classes API
  slug: open-class-fka-classedu-classes-api
- collection_type: open
  name: Class Developer Classes Enrollments API
  slug: open-class-fka-classedu-enrollments-api
- collection_type: open
  name: Class Developer Classes Launch API
  slug: open-class-fka-classedu-launch-api
- collection_type: open
  name: Class Developer Classes Reporting API
  slug: open-class-fka-classedu-reporting-api
- collection_type: open
  name: Class Developer Classes Schedules API
  slug: open-class-fka-classedu-schedules-api
- collection_type: open
  name: Class Developer Classes Templates API
  slug: open-class-fka-classedu-templates-api
- collection_type: open
  name: Class Developer Classes Users API
  slug: open-class-fka-classedu-users-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/class-fka-classedu-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/class-fka-classedu-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/class-fka-classedu-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/class-fka-classedu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.class.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.class.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.class.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.class.com/
- group: operate
  title: ''
  type: Support
  url: https://support.class.com/
- group: company
  title: ''
  type: Blog
  url: https://www.class.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.class.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.class.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.class.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.class.com/privacy-policy/
- group: start
  title: ''
  type: Demo
  url: https://www.class.com/demo/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/class-fka-classedu-openapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/class-fka-classedu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/class-fka-classedu-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/class-fka-classedu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/class-fka-classedu-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.class.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/class-fka-classedu-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/class-fka-classedu-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/class-fka-classedu-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/class-fka-classedu-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Class (fka ClassEDU) is a virtual classroom platform, founded in 2020 by education-technology leader Michael Chasen, that adds a full teaching and learning layer on top of Zoom and Microsoft Teams for K-12, higher education, government, and corporate training. The platform provides interactive course setup and templates, real-time engagement analytics and attendance tracking, enhanced breakout rooms, polls, whiteboards, auto transcription, an AI assistant, proctoring, and LMS integrations. Class also publishes a REST developer API (developer.class.com) that lets administrators and integrators provision classes, manage enrollments, generate learner launch links, schedule class dates, manage class templates, manage non-learner users, and pull attendance and engagement reporting, authenticated with a per-organization API key presented as a Bearer token and gated by permission scopes.
image: https://www.class.com/wp-content/uploads/2022/12/class_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: class-fka-classedu-mcp.yml
  slug: class-fka-classedu-mcpyml
modified: '2026-07-18'
name: Class (fka ClassEDU)
nav: Providers
network: true
overview: 'Class (fka ClassEDU) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Classes API, Enrollments API, Launch API, and 4 more. Tagged areas include Company, Education, EdTech, Virtual Classroom, and Learning Management.


  Class (fka ClassEDU)''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 21 more developer resources.'
random_paper: 143
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 58.8
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/class-fka-classedu/refs/heads/main/screenshots/class-fka-classedu-2026-07-25T205514.png
security:
- kind: authentication
  name: Class Fka Classedu Authentication
  slug: class-fka-classedu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Class Fka Classedu Domain Security
  slug: class-fka-classedu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Class Fka Classedu Trust Center
  slug: class-fka-classedu-trust-center
  summary_line: SOC 2, ISO 27001
slug: class-fka-classedu
tags:
- Company
- Education
- EdTech
- Virtual Classroom
- Learning Management
- Online Learning
- Training
- Zoom
- Microsoft Teams
- Attendance
website: https://www.class.com/
---
