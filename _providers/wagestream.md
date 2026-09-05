---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Wagestream Agentic Access
  operation_count: 11
  slug: wagestream-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 2
apis:
- baseURL: https://publicapi.wagestream.io/pushapi-prod
  baseurl_source: declared
  description: Operations relating to absences
  name: Wagestream Absences API
  slug: wagestream-absences-api
- baseURL: https://publicapi.wagestream.io/pushapi-prod
  baseurl_source: declared
  description: Operations relating to employees
  name: Wagestream Employees API
  slug: wagestream-employees-api
- baseURL: https://publicapi.wagestream.io/pushapi-prod
  baseurl_source: declared
  description: Operations relating to enrolling employees in Wagestream
  name: Wagestream Enrollment API
  slug: wagestream-enrollment-api
- baseURL: https://publicapi.wagestream.io/pushapi-prod
  baseurl_source: declared
  description: Operations relating to off-cycle payments
  name: Wagestream Off Cycle Payment API
  slug: wagestream-off-cycle-payment-api
- baseURL: https://publicapi.wagestream.io/pushapi-prod
  baseurl_source: declared
  description: Operations relating to Shifts
  name: Wagestream Shifts API
  slug: wagestream-shifts-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wagestream Integrations Absences API
  slug: open-wagestream-absences-api
- collection_type: open
  name: Wagestream Integrations Employees API
  slug: open-wagestream-employees-api
- collection_type: open
  name: Wagestream Integrations Enrollment API
  slug: open-wagestream-enrollment-api
- collection_type: open
  name: Wagestream Integrations Off Cycle Payment API
  slug: open-wagestream-off-cycle-payment-api
- collection_type: open
  name: Wagestream Integrations Shifts API
  slug: open-wagestream-shifts-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wagestream-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wagestream-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wagestream-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stream.co/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://connect.stream.co/
- group: docs
  title: ''
  type: Documentation
  url: https://connect.stream.co/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://connect.stream.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://connect.stream.co/docs/overview-1
- group: operate
  title: ''
  type: Support
  url: https://help.stream.co/
- group: company
  title: ''
  type: Blog
  url: https://stream.co/en/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wagestream
- group: start
  title: ''
  type: SignUp
  url: https://stream.co/en/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://stream.co/en-us/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stream.co/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stream.co/en/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.stream.co/
- group: auth
  title: ''
  type: Compliance
  url: https://stream.co/en-us/stream-licenses-compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stream.co/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wagestream-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wagestream-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/wagestream-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wagestream-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/wagestream-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wagestream-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wagestream-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wagestream-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wagestream-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wagestream-integrations-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wagestream-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: Wagestream — trading as Stream since its 2025 rebrand — is a UK-founded, B Corp certified workplace financial wellbeing platform that gives hourly and salaried employees earned wage access (flexible pay), shift and pay tracking, workplace savings, budgeting tools, salary-deducted workplace loans, benefits and state-benefit claim support, financial coaching and discounts, delivered as a mobile app funded by the employer rather than the worker. Employers connect their HR, workforce management and payroll systems to Stream through the Wagestream Integrations API — a small, batch-oriented REST push API over employees, shifts (time and attendance), absences, off-cycle payments and Stream-generated enrolment banking records — or via SFTP file feeds and browser upload into the employer administration portal. The API is API-key authenticated, asynchronous (every write returns a transaction id polled through a matching GET), and idempotent through an optional per-request nonce.
image: https://stream.co/api/media/file/Home_Hero_Left.webp
layout: provider
modified: '2026-08-05'
name: Wagestream
nav: Providers
network: true
overview: 'Wagestream publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Employees API, Enrollment API, and 2 more. Tagged areas include Financial Wellbeing, Earned Wage Access, Fintech, Payroll, and Human Resources.


  Wagestream''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 23 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 54.2
    developer_ergonomics: 41.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wagestream/refs/heads/main/screenshots/wagestream-2026-08-17T082831.png
security:
- kind: authentication
  name: Wagestream Authentication
  slug: wagestream-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wagestream Domain Security
  slug: wagestream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wagestream Trust Center
  slug: wagestream-trust-center
  summary_line: trust center published
slug: wagestream
tags:
- Financial Wellbeing
- Earned Wage Access
- Fintech
- Payroll
- Human Resources
- Workforce Management
- Time and Attendance
- Employee Benefits
- Workplace Savings
- HR Integrations
- B Corp
- United Kingdom
website: https://stream.co/en
---
