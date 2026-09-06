---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 566
  human_in_the_loop: 29
  name: Canvas Agentic Access
  operation_count: 1148
  slug: canvas-agentic-access
  summary_line: 1148 operations · 566 acting · 29 human-in-the-loop
api_count: 145
apis:
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Canvas LMS REST API provides programmatic access to courses, assignments, quizzes, grades, users, enrollments, accounts, discussions, files, modules, rubrics, submissions, SIS imports, and account
  name: Canvas LMS REST API
  slug: canvas-lms-rest-api
- description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and ag
  name: Canvas LMS GraphQL API
  slug: canvas-lms-graphql-api
- description: Canvas supports Learning Tools Interoperability (LTI 1.1 and LTI 1.3 / Advantage) for embedding external tools, assignments, and content into courses with deep linking, grade passback, and names-and-r
  name: Canvas LTI Integrations
  slug: canvas-lti-integrations
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Courses resource of the Canvas LMS REST API — 31 operations covering course creation, settings, users and enrollment counts, course copy, blueprint associations, effective due dates, bulk course u
  name: Canvas Courses API
  slug: canvas-courses-api
artifact_total: 18
asyncapis:
- description: ''
  name: Canvas Live Events Webhooks
  slug: canvas-live-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canvas LMS REST API ( subset) Courses API
  slug: open-canvas-courses-api
- collection_type: open
  name: Canvas LMS REST API (Courses subset)
  slug: open-canvas
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canvas-scopes.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/instructure/canvas-lms/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/instructure/canvas-lms/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/instructure/canvas-lms/blob/master/code_of_conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/instructure/canvas-lms/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/instructure/canvas-lms/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/canvas-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canvas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canvas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canvas-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/canvaslms
- group: company
  title: ''
  type: Website
  url: https://www.instructure.com/canvas
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instructure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/instructure/canvas-lms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instructure.com/
- group: operate
  title: ''
  type: Community
  url: https://community.canvaslms.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instructure.com/policies/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.instructure.com/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instructure.com/policies/acceptable-use
- group: build
  title: ''
  type: Packages
  url: packages/canvas-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/canvas-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canvas-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/canvas-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canvas-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/canvas-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canvas-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.instructure.com/trust-center
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canvas-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canvas-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://community.canvaslms.com/t5/Change-Log/tkb-p/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/canvas-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canvas-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/canvas-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/canvas-cli.yml
- group: design
  title: ''
  type: Components
  url: components/canvas-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canvas-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/canvas-live-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/canvas-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/canvas-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.instructure.com/trust-center/vulnerability-disclosure
- group: other
  title: ''
  type: Overlay
  url: overlays/canvas-canvas-lms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/canvas-canvas-courses-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developerdocs.instructure.com/services/canvas
- group: docs
  title: ''
  type: APIReference
  url: https://canvas.instructure.com/doc/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth
- group: operate
  title: ''
  type: Support
  url: https://community.canvaslms.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.instructure.com/canvas/free-for-teacher
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instructure.com/canvas
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/canvas-mcp.yml
created: '2025-01-14'
description: Canvas is Instructure's open-source learning management system (LMS) used by K-12, higher education, and corporate training organizations to deliver courses, assessments, and learner communication. Canvas exposes a comprehensive REST API and a GraphQL endpoint for reading and modifying courses, assignments, quizzes, grades, users, enrollments, content, and account administration, and it integrates with external tools through LTI, Caliper, and live event streams.
finops:
- name: Canvas Finops
  service_category: API
  slug: canvas-finops
graphqls:
- description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and ag
  name: Canvas GraphQL API
  slug: canvas-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canvas.png
layout: provider
modified: '2026-09-05'
name: Canvas
nav: Providers
network: true
overview: 'Canvas publishes 2 APIs on the [APIs.io](https://apis.io/) network: LMS REST API and Courses API. Tagged areas include Education, EdTech, GraphQL, Learning Management System, and LMS.


  The Canvas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canvas'' developer surface includes authentication, documentation, engineering blog, changelog, sandbox, CLI, API reference, and 45 more developer resources.'
plans:
- name: Canvas Plans Pricing
  plan_count: 1
  slug: canvas-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Canvas Rate Limits
  slug: canvas-rate-limits
scopes:
- name: Canvas Scopes
  scope_count: 1117
  slug: canvas-scopes
  summary_line: 1117 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.0
    catalog_earned_first_party: 16.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 39.7
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 24.4
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 81.6
  open_source:
    applies: true
    score: 75.0
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/screenshots/canvas-2026-06-20T173929.png
security:
- kind: authentication
  name: Canvas Authentication
  slug: canvas-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canvas Domain Security
  slug: canvas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canvas Vulnerability Disclosure
  slug: canvas-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Canvas Trust Center
  slug: canvas-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: canvas
tags:
- Education
- EdTech
- GraphQL
- Learning Management System
- LMS
- LTI
- Open-Source
- REST
website: https://www.instructure.com/canvas
---
