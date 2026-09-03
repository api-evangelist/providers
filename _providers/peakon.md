---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.peakon.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.workday.com/en-us/products/employee-voice/overview.html — a different registrable domain (peakon.com -> workday.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Peakon Agentic Access
  operation_count: 24
  slug: peakon-agentic-access
  summary_line: 24 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Retrieving actions
  name: Peakon Actions API
  slug: peakon-actions-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: The Answers API from Peakon — 1 operation(s) for answers.
  name: Peakon Answers API
  slug: peakon-answers-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Retrieving company audit log
  name: Peakon Audits API
  slug: peakon-audits-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Authenticating with the API
  name: Peakon Authentication API
  slug: peakon-authentication-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Manage employees
  name: Peakon Employees API
  slug: peakon-employees-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Retrieving engagement scores
  name: Peakon Engagement API
  slug: peakon-engagement-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Retrieving scores
  name: Peakon Scores API
  slug: peakon-scores-api
- baseURL: https://api.peakon.com/api/v1/
  baseurl_source: declared
  description: Retrieving segments
  name: Peakon Segments API
  slug: peakon-segments-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Peakon Actions API
  slug: open-peakon-actions-api
- collection_type: open
  name: Peakon Actions Answers API
  slug: open-peakon-answers-api
- collection_type: open
  name: Peakon Actions Audits API
  slug: open-peakon-audits-api
- collection_type: open
  name: Peakon Actions Authentication API
  slug: open-peakon-authentication-api
- collection_type: open
  name: Peakon Actions Employees API
  slug: open-peakon-employees-api
- collection_type: open
  name: Peakon Actions Engagement API
  slug: open-peakon-engagement-api
- collection_type: open
  name: Peakon Actions Scores API
  slug: open-peakon-scores-api
- collection_type: open
  name: Peakon Actions Segments API
  slug: open-peakon-segments-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/workday/
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
  type: X-MCPServerCandidate
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
modified: '2026-07-20'
name: Peakon
nav: Providers
network: true
overview: 'Peakon publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Answers API, Audits API, and 5 more. Tagged areas include Company, Software-as-a-Service, Employee Engagement, Employee Experience, and HR Tech.


  Peakon''s developer surface includes documentation, API reference, getting-started guide, authentication, support, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 46.2
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 32.2
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peakon/refs/heads/main/screenshots/peakon-2026-08-07T191724.png
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
- Software-as-a-Service
- Employee Engagement
- Employee Experience
- HR Tech
- Surveys
- People Analytics
- Workday
website: https://www.peakon.com
---
