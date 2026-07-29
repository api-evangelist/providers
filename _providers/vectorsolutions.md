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
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 2
  name: Vectorsolutions Agentic Access
  operation_count: 70
  slug: vectorsolutions-agentic-access
  summary_line: 70 operations · 19 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: The Courses API from Vector Solutions — 4 operation(s) for courses.
  name: Vector Solutions Courses API
  slug: vectorsolutions-courses-api
- description: The Credential Assignment API from Vector Solutions — 3 operation(s) for credential assignment.
  name: Vector Solutions Credential Assignment API
  slug: vectorsolutions-credential-assignment-api
- description: The Credential Categories API from Vector Solutions — 4 operation(s) for credential categories.
  name: Vector Solutions Credential Categories API
  slug: vectorsolutions-credential-categories-api
- description: The Credentials API from Vector Solutions — 4 operation(s) for credentials.
  name: Vector Solutions Credentials API
  slug: vectorsolutions-credentials-api
- description: The Feature Access API from Vector Solutions — 5 operation(s) for feature access.
  name: Vector Solutions Feature Access API
  slug: vectorsolutions-feature-access-api
- description: The Profile Categories API from Vector Solutions — 4 operation(s) for profile categories.
  name: Vector Solutions Profile Categories API
  slug: vectorsolutions-profile-categories-api
- description: The Profile Group Assignment API from Vector Solutions — 4 operation(s) for profile group assignment.
  name: Vector Solutions Profile Group Assignment API
  slug: vectorsolutions-profile-group-assignment-api
- description: The Profile Groups API from Vector Solutions — 4 operation(s) for profile groups.
  name: Vector Solutions Profile Groups API
  slug: vectorsolutions-profile-groups-api
- description: The Sites API from Vector Solutions — 2 operation(s) for sites.
  name: Vector Solutions Sites API
  slug: vectorsolutions-sites-api
- description: The Supervisor Access API from Vector Solutions — 5 operation(s) for supervisor access.
  name: Vector Solutions Supervisor Access API
  slug: vectorsolutions-supervisor-access-api
- description: The Training Assignments API from Vector Solutions — 5 operation(s) for training assignments.
  name: Vector Solutions Training Assignments API
  slug: vectorsolutions-training-assignments-api
- description: The User Emails API from Vector Solutions — 2 operation(s) for user emails.
  name: Vector Solutions User Emails API
  slug: vectorsolutions-user-emails-api
- description: The User History API from Vector Solutions — 3 operation(s) for user history.
  name: Vector Solutions User History API
  slug: vectorsolutions-user-history-api
- description: The Users API from Vector Solutions — 4 operation(s) for users.
  name: Vector Solutions Users API
  slug: vectorsolutions-users-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vectorsolutions-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vectorsolutions-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vectorsolutions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vectorsolutions.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.targetsolutions.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.targetsolutions.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.targetsolutions.com/documentation/routes
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.targetsolutions.com/worldoftargetsolutions
- group: operate
  title: ''
  type: Support
  url: https://www.vectorsolutions.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.vectorsolutions.com/resources/blogs/
- group: start
  title: ''
  type: Login
  url: https://www.vectorsolutions.com/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vectorsolutions.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vectorsolutions.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://www.vectorsolutions.com/request-a-demo/
- group: auth
  title: ''
  type: Compliance
  url: https://www.vectorsolutions.com/resources/press-releases/vector-solutions-successfully-completes-annual-soc-2-type-1-examination/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vectorsolutions-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vectorsolutions-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vectorsolutions-targetsolutions-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vectorsolutions-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vectorsolutions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vectorsolutions-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vectorsolutions-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vectorsolutions-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vectorsolutions-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vector Solutions is a training and workforce management software company serving education, public safety, government, manufacturing, construction, and gaming industries with products including Vector LMS, Vector EHS, Vector Scheduling, Vector Check It, Acadis, Guardian Tracking, and TargetSolutions. Its TargetSolutions platform for online training and records management exposes a REST API (v1) for managing sites, users, profile groups, supervisor and feature access, credentials, courses, and training assignments, documented at developers.targetsolutions.com.
image: https://www.vectorsolutions.com/wp-content/uploads/2021/03/VectorSolutions_Logo_Icon_Color-copy-e1610391064416-1024x907.png
layout: provider
mcp_servers:
- description: ''
  name: vectorsolutions-mcp.yml
  slug: vectorsolutions-mcpyml
modified: '2026-07-21'
name: Vector Solutions
nav: Providers
network: true
overview: 'Vector Solutions publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Courses API, Credential Assignment API, Credential Categories API, and 11 more. Tagged areas include Training, Learning Management, Compliance, Public Safety, and Workforce Management.


  Vector Solutions'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 44.6
  delta: -3.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 47.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vectorsolutions Authentication
  slug: vectorsolutions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vectorsolutions Domain Security
  slug: vectorsolutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vectorsolutions
tags:
- Training
- Learning Management
- Compliance
- Public Safety
- Workforce Management
- EHS
- Education
website: https://vectorsolutions.com
---
