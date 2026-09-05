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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gitar Agentic Access
  operation_count: 3
  slug: gitar-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.gitar.ai/v1
  baseurl_source: declared
  description: The GitLab MR Status API from Gitar — 1 operation(s) for gitlab mr status.
  name: Gitar GitLab MR Status API
  slug: gitar-gitlab-mr-status-api
- baseURL: https://api.gitar.ai/v1
  baseurl_source: declared
  description: The GitLab Projects API from Gitar — 1 operation(s) for gitlab projects.
  name: Gitar GitLab Projects API
  slug: gitar-gitlab-projects-api
- baseURL: https://api.gitar.ai/v1
  baseurl_source: declared
  description: The Installation Health API from Gitar — 1 operation(s) for installation health.
  name: Gitar Installation Health API
  slug: gitar-installation-health-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gitar External GitLab MR Status API
  slug: open-gitar-gitlab-mr-status-api
- collection_type: open
  name: Gitar External GitLab MR Status GitLab Projects API
  slug: open-gitar-gitlab-projects-api
- collection_type: open
  name: Gitar External GitLab MR Status Installation Health API
  slug: open-gitar-installation-health-api
common:
- group: company
  title: ''
  type: Website
  url: https://gitar.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gitar.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitar.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gitar.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gitar.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://gitar.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gitar.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gitar.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.gitar.ai/sign-in
- group: operate
  title: ''
  type: Support
  url: https://go.gitar.ai/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitarcode
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gitar.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitar.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitar.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gitar.ai/
- group: auth
  title: ''
  type: Compliance
  url: security/gitar-trust-center.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/gitar-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gitar-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gitar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gitar-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gitar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gitar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gitar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gitar-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gitar-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitar-domain-security.yml
created: '2026-07-17'
description: Gitar is an AI code review platform that goes beyond commenting on pull and merge requests — it automatically fixes broken builds, failing tests, linting errors, and code-review findings, and validates every change against your CI pipeline before it is pushed. It works directly in the GitHub and GitLab PR interface, analyzes CI failures, deduplicates flaky tests, and runs natural-language repository rules from a .gitar/rules directory. Built by engineers from Uber's development stack and acquired by Sonar (SonarQube), Gitar is used by teams including SoFi, DeepL, and Altruist. It exposes a Bearer-token External API (api.gitar.ai/v1) on the Enterprise plan for installation health checks and GitLab project onboarding, and integrates with Buildkite, CircleCI, Bitrise, Jira, Linear, and Slack.
image: https://gitar.ai/assets/meta-banner.png
layout: provider
modified: '2026-07-19'
name: Gitar
nav: Providers
network: true
overview: 'Gitar publishes 3 APIs on the [APIs.io](https://apis.io/) network: GitLab MR Status API, GitLab Projects API, and Installation Health API. Tagged areas include Company, Developer Tools, Code Review, CI/CD, and Code Quality.


  Gitar''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 55.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitar/refs/heads/main/screenshots/gitar-2026-07-25T215835.png
security:
- kind: authentication
  name: Gitar Authentication
  slug: gitar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gitar Domain Security
  slug: gitar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gitar Trust Center
  slug: gitar-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: gitar
tags:
- Company
- Developer Tools
- Code Review
- CI/CD
- Code Quality
- Artificial Intelligence
- Developer Productivity
- Automation
website: https://gitar.ai/
---
