---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'REST API for the Class virtual classroom platform. Manage classes, enrollments, schedules, templates, and non-learner users; generate per-user launch URLs; and pull attendance and activity reporting. '
  name: Class API
  slug: class-api
artifact_total: 5
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
  type: X-MCPServerCandidate
  url: mcp/class-technologies-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/class-technologies-domain-security.yml
created: '2026-07-17'
description: Class Technologies Inc. builds Class, a virtual instructor-led learning platform that layers a full classroom experience on top of Zoom and Microsoft Teams, plus the web-based Class Collaborate. It gives instructors breakout rooms, whiteboards, polling, chat, attendance, transcription, a gradebook, engagement scoring, and deep LMS integration for K-12, higher education, corporate training, government (FedRAMP), healthcare (HIPAA), and financial services. Class exposes a REST API (developer.class.com) for managing classes, enrollments, schedules, templates, users, launch URLs, and attendance/activity reporting, secured with scoped API-key bearer tokens.
image: https://www.class.com/wp-content/uploads/2024/03/class-virtual-classroom-featured.png
layout: provider
modified: '2026-07-18'
name: Class Technologies
nav: Providers
network: true
overview: 'Class Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EdTech, Education, Virtual Classroom, and E-Learning.


  Class Technologies'' developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 13 more developer resources.'
random_paper: 15
scopes:
- name: Class Technologies Scopes
  scope_count: 12
  slug: class-technologies-scopes
  summary_line: 12 scopes
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 33.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- EdTech
- Education
- Virtual Classroom
- E-Learning
- LMS
- Online Learning
- Corporate Training
- Video Conferencing
website: https://www.class.com/
---
