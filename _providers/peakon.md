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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Peakon Agentic Access
  operation_count: 24
  slug: peakon-agentic-access
  summary_line: 24 operations · 4 acting
api_count: 8
apis:
- description: Retrieving actions
  name: Peakon Actions API
  slug: peakon-actions-api
- description: The Answers API from Peakon — 1 operation(s) for answers.
  name: Peakon Answers API
  slug: peakon-answers-api
- description: Retrieving company audit log
  name: Peakon Audits API
  slug: peakon-audits-api
- description: Authenticating with the API
  name: Peakon Authentication API
  slug: peakon-authentication-api
- description: Manage employees
  name: Peakon Employees API
  slug: peakon-employees-api
- description: Retrieving engagement scores
  name: Peakon Engagement API
  slug: peakon-engagement-api
- description: Retrieving scores
  name: Peakon Scores API
  slug: peakon-scores-api
- description: Retrieving segments
  name: Peakon Segments API
  slug: peakon-segments-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peakon-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.peakon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.peakon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.peakon.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.peakon.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/peakon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/peakon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/peakon-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/peakon-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/peakon-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/peakon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peakon-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/peakon-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.peakon.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peakon-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://support.peakon.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peakon
- group: other
  title: ''
  type: Overlay
  url: overlays/peakon-openapi-overlay.yaml
created: '2026-07-17'
description: Peakon (now Workday Peakon Employee Voice) is an employee engagement and experience platform for measuring and improving engagement through continuous surveys, driver analytics, and action-taking. Founded in Copenhagen and backed by Atomico and Balderton Capital, it was acquired by Workday in 2021. Peakon exposes a public REST API (v1.1.0, JSON:API) for reading engagement overviews, drivers, segment and category scores, survey answers, and audits, plus managing employees; it also offers a SCIM 2.0 provisioning API for continuous HRIS-driven user sync. Applications authenticate by exchanging a custom-app access token for a session bearer JWT scoped by per-app permissions.
image: https://files.readme.io/2b612560a84c6544f0ffcaf0abeef8c1da4cd1ec5ac568f569f1b0d4058082db-small-wd-dub-reversed.png
layout: provider
mcp_servers:
- description: ''
  name: peakon-mcp.yml
  slug: peakon-mcpyml
modified: '2026-07-20'
name: Peakon
nav: Providers
network: true
overview: 'Peakon publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Answers API, Audits API, and 5 more. Tagged areas include Company, Saas, Employee Engagement, Employee Experience, and HR Tech.


  Peakon''s developer surface includes documentation, API reference, getting-started guide, authentication, support, and 15 more developer resources.'
random_paper: 73
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 48.5
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Peakon Authentication
  slug: peakon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Peakon Domain Security
  slug: peakon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peakon
tags:
- Company
- Saas
- Employee Engagement
- Employee Experience
- HR Tech
- Surveys
- People Analytics
- Workday
website: https://www.peakon.com
---
