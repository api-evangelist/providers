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
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST API for the Class virtual classroom platform. Manage classes, enrollments, schedules, templates, and non-learner users; generate per-user launch URLs; and pull attendance and activity reporting. '
  name: Class API
  slug: class-api
artifact_total: 6
common:
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
- group: company
  title: ''
  type: Website
  url: https://www.class.com/
- group: operate
  title: ''
  type: Support
  url: https://support.class.com/
- group: company
  title: ''
  type: Blog
  url: https://www.class.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.class.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.class.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.class.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.class.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.class.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.class.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/class-technologies-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/class-technologies-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/class-technologies-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/class-technologies-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/class-technologies-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/class-technologies-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/class-technologies-domain-security.yml
created: '2026-07-17'
description: Class Technologies Inc. builds Class, a virtual instructor-led learning platform that layers a full classroom experience on top of Zoom and Microsoft Teams, plus the web-based Class Collaborate. It gives instructors breakout rooms, whiteboards, polling, chat, attendance, transcription, a gradebook, engagement scoring, and deep LMS integration for K-12, higher education, corporate training, government (FedRAMP), healthcare (HIPAA), and financial services. Class exposes a REST API (developer.class.com) for managing classes, enrollments, schedules, templates, users, launch URLs, and attendance/activity reporting, secured with scoped API-key bearer tokens.
image: https://www.class.com/wp-content/uploads/2024/03/class-virtual-classroom-featured.png
layout: provider
mcp_servers:
- description: ''
  name: class-technologies-mcp.yml
  slug: class-technologies-mcpyml
modified: '2026-07-18'
name: Class Technologies
nav: Providers
network: true
overview: 'Class Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edtech, Education, Virtual Classroom, and E-Learning.


  Class Technologies'' developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 13 more developer resources.'
random_paper: 59
scopes:
- name: Class Technologies Scopes
  scope_count: 12
  slug: class-technologies-scopes
  summary_line: 12 scopes
score:
  band: emerging
  composite: 27.6
  delta: -3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 31.3
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/class-technologies/refs/heads/main/screenshots/class-technologies-2026-07-25T205514.png
security:
- kind: authentication
  name: Class Technologies Authentication
  slug: class-technologies-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Class Technologies Domain Security
  slug: class-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Class Technologies Trust Center
  slug: class-technologies-trust-center
  summary_line: FedRAMP, HIPAA
slug: class-technologies
tags:
- Company
- Edtech
- Education
- Virtual Classroom
- E-Learning
- LMS
- Online Learning
- Corporate Training
- Video Conferencing
website: https://www.class.com/
---
