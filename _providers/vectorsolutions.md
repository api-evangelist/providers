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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 19
  human_in_the_loop: 2
  name: Vectorsolutions Agentic Access
  operation_count: 70
  slug: vectorsolutions-agentic-access
  summary_line: 70 operations · 19 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Courses API from Vector Solutions — 4 operation(s) for courses.
  name: Vector Solutions Courses API
  slug: vectorsolutions-courses-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Credential Assignment API from Vector Solutions — 3 operation(s) for credential assignment.
  name: Vector Solutions Credential Assignment API
  slug: vectorsolutions-credential-assignment-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Credential Categories API from Vector Solutions — 4 operation(s) for credential categories.
  name: Vector Solutions Credential Categories API
  slug: vectorsolutions-credential-categories-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Credentials API from Vector Solutions — 4 operation(s) for credentials.
  name: Vector Solutions Credentials API
  slug: vectorsolutions-credentials-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Feature Access API from Vector Solutions — 5 operation(s) for feature access.
  name: Vector Solutions Feature Access API
  slug: vectorsolutions-feature-access-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Profile Categories API from Vector Solutions — 4 operation(s) for profile categories.
  name: Vector Solutions Profile Categories API
  slug: vectorsolutions-profile-categories-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Profile Group Assignment API from Vector Solutions — 4 operation(s) for profile group assignment.
  name: Vector Solutions Profile Group Assignment API
  slug: vectorsolutions-profile-group-assignment-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Profile Groups API from Vector Solutions — 4 operation(s) for profile groups.
  name: Vector Solutions Profile Groups API
  slug: vectorsolutions-profile-groups-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Sites API from Vector Solutions — 2 operation(s) for sites.
  name: Vector Solutions Sites API
  slug: vectorsolutions-sites-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Supervisor Access API from Vector Solutions — 5 operation(s) for supervisor access.
  name: Vector Solutions Supervisor Access API
  slug: vectorsolutions-supervisor-access-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Training Assignments API from Vector Solutions — 5 operation(s) for training assignments.
  name: Vector Solutions Training Assignments API
  slug: vectorsolutions-training-assignments-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The User Emails API from Vector Solutions — 2 operation(s) for user emails.
  name: Vector Solutions User Emails API
  slug: vectorsolutions-user-emails-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The User History API from Vector Solutions — 3 operation(s) for user history.
  name: Vector Solutions User History API
  slug: vectorsolutions-user-history-api
- baseURL: https://api.targetsolutions.com/v1
  baseurl_source: declared
  description: The Users API from Vector Solutions — 4 operation(s) for users.
  name: Vector Solutions Users API
  slug: vectorsolutions-users-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TargetSolutions Courses API
  slug: open-vectorsolutions-courses-api
- collection_type: open
  name: TargetSolutions Courses Credential Assignment API
  slug: open-vectorsolutions-credential-assignment-api
- collection_type: open
  name: TargetSolutions Courses Credential Categories API
  slug: open-vectorsolutions-credential-categories-api
- collection_type: open
  name: TargetSolutions Courses Credentials API
  slug: open-vectorsolutions-credentials-api
- collection_type: open
  name: TargetSolutions Courses Feature Access API
  slug: open-vectorsolutions-feature-access-api
- collection_type: open
  name: TargetSolutions Courses Profile Categories API
  slug: open-vectorsolutions-profile-categories-api
- collection_type: open
  name: TargetSolutions Courses Profile Group Assignment API
  slug: open-vectorsolutions-profile-group-assignment-api
- collection_type: open
  name: TargetSolutions Courses Profile Groups API
  slug: open-vectorsolutions-profile-groups-api
- collection_type: open
  name: TargetSolutions Courses Sites API
  slug: open-vectorsolutions-sites-api
- collection_type: open
  name: TargetSolutions Courses Supervisor Access API
  slug: open-vectorsolutions-supervisor-access-api
- collection_type: open
  name: TargetSolutions Courses Training Assignments API
  slug: open-vectorsolutions-training-assignments-api
- collection_type: open
  name: TargetSolutions Courses User Emails API
  slug: open-vectorsolutions-user-emails-api
- collection_type: open
  name: TargetSolutions Courses User History API
  slug: open-vectorsolutions-user-history-api
- collection_type: open
  name: TargetSolutions Courses Users API
  slug: open-vectorsolutions-users-api
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
  name: Vector Solutions MCP Server
  slug: vector-solutions-mcp-server
modified: '2026-07-21'
name: Vector Solutions
nav: Providers
network: true
overview: 'Vector Solutions publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Courses API, Credential Assignment API, Credential Categories API, and 11 more. Tagged areas include Training, Learning Management, Compliance, Public Safety, and Workforce Management.


  Vector Solutions'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 13.9
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 38.3
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vectorsolutions/refs/heads/main/screenshots/vectorsolutions-2026-09-02T165542.png
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
