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
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: The Course API from Uplimit — 3 operation(s) for course.
  name: Uplimit Course API
  slug: uplimit-course-api
- description: The Enrollment API from Uplimit — 4 operation(s) for enrollment.
  name: Uplimit Enrollment API
  slug: uplimit-enrollment-api
- description: The Export API from Uplimit — 2 operation(s) for export.
  name: Uplimit Export API
  slug: uplimit-export-api
- description: The Platform API from Uplimit — 1 operation(s) for platform.
  name: Uplimit Platform API
  slug: uplimit-platform-api
- description: The Session API from Uplimit — 4 operation(s) for session.
  name: Uplimit Session API
  slug: uplimit-session-api
- description: The User API from Uplimit — 10 operation(s) for user.
  name: Uplimit User API
  slug: uplimit-user-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uplimit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uplimit.com
- group: company
  title: ''
  type: Blog
  url: https://uplimit.com/blog
- group: company
  title: ''
  type: About
  url: https://uplimit.com/about
- group: operate
  title: ''
  type: Contact
  url: https://uplimit.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uplimit.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uplimit.com/about/privacy
- group: company
  title: ''
  type: Careers
  url: https://uplimit.com/go/work-at-uplimit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uplimit
- group: build
  title: ''
  type: Packages
  url: packages/uplimit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uplimit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uplimit-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uplimit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uplimit-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/uplimit-organization-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/uplimit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uplimit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uplimit-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uplimit.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/uplimit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uplimit-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uplimit-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Uplimit (formerly CoRise, operated by Veda Education, Inc.) is an AI-native corporate learning platform backed by Greylock and Cowboy Ventures. It generates personalized, adaptive training programs with AI instructors, voice and visual practice simulations, real-time feedback, and per-learner mastery measurement for use cases like leadership training, onboarding, customer education, and sales readiness. Its Organization API lets enterprise customers manage users, course and session enrollments, SSO identity bindings, and learner-activity exports, with first-party generated Go, Python, and TypeScript clients published on GitHub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uplimit.png
layout: provider
mcp_servers:
- description: ''
  name: uplimit-mcp.yml
  slug: uplimit-mcpyml
modified: '2026-07-21'
name: Uplimit
nav: Providers
network: true
overview: 'Uplimit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Course API, Enrollment API, Export API, and 3 more. Tagged areas include Company, Future Of Work, Learning, Education, and Training.


  Uplimit''s developer surface includes engineering blog, authentication, and 21 more developer resources.'
random_paper: 61
score:
  band: thin
  composite: 35.6
  delta: -2.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 53.4
    developer_ergonomics: 23.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 37.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Uplimit Authentication
  slug: uplimit-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Uplimit Domain Security
  slug: uplimit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uplimit
tags:
- Company
- Future Of Work
- Learning
- Education
- Training
- Artificial Intelligence
- Corporate Training
website: https://uplimit.com
---
