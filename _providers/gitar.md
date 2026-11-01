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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-10-31'
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
- baseURL: https://api.gitar.ai/v1
  baseurl_source: declared
  description: The Organizations API from Gitar — 1 operation(s) for organizations.
  name: Gitar Organizations API
  slug: gitar-organizations-api
artifact_total: 16
collections:
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
- group: commercial
  href: https://artifacts.apis.io/gitar/plans/gitar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitar-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/gitar/capabilities/gitar-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gitar-capability-edges.yml
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
  href: https://artifacts.apis.io/gitar/security/gitar-trust-center.yml
  title: ''
  type: Compliance
  url: security/gitar-trust-center.yml
- group: docs
  href: https://artifacts.apis.io/gitar/openapi/_original/gitar-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/gitar-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/gitar/llms/gitar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitar-llms.txt
- group: agent
  href: https://artifacts.apis.io/gitar/mcp/gitar-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gitar-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gitar/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/gitar/overlays/gitar-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gitar-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/gitar/authentication/gitar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitar-authentication.yml
- group: design
  href: https://artifacts.apis.io/gitar/conventions/gitar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gitar-conventions.yml
- group: design
  href: https://artifacts.apis.io/gitar/errors/gitar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gitar-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gitar/lifecycle/gitar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gitar-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gitar/conformance/gitar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitar-conformance.yml
- group: design
  href: https://artifacts.apis.io/gitar/data-model/gitar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gitar-data-model.yml
- group: agent
  href: https://artifacts.apis.io/gitar/agentic-access/gitar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitar-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gitar/security/gitar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitar-domain-security.yml
created: '2026-07-17'
description: Gitar is an AI code review platform that goes beyond commenting on pull and merge requests — it automatically fixes broken builds, failing tests, linting errors, and code-review findings, and validates every change against your CI pipeline before it is pushed. It works directly in the GitHub and GitLab PR interface, analyzes CI failures, deduplicates flaky tests, and runs natural-language repository rules from a .gitar/rules directory. Built by engineers from Uber's development stack and acquired by Sonar (SonarQube), Gitar is used by teams including SoFi, DeepL, and Altruist. It exposes a Bearer-token External API (api.gitar.ai/v1) on the Enterprise plan for installation health checks and GitLab project onboarding, and integrates with Buildkite, CircleCI, Bitrise, Jira, Linear, and Slack.
finops:
- has_sources: true
  method: derived
  name: Gitar Finops
  primary_unit: user
  service_category: ''
  slug: gitar-finops
  template: false
image: https://gitar.ai/assets/meta-banner.png
layout: provider
modified: '2026-07-19'
name: Gitar
nav: Providers
network: true
overview: 'Gitar publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including GitLab MR Status API, GitLab Projects API, Installation Health API, and 1 more. Tagged areas include Company, Developer Tools, Code Review, CI/CD, and Code Quality.


  Gitar''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 24 more developer resources.'
plans:
- name: Gitar Plans Pricing
  plan_count: 6
  slug: gitar-plans-pricing
- name: Gitar Price Estimates
  plan_count: 0
  slug: gitar-price-estimates
random_paper: 7
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 56.3
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
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gitar/gitar-2026-07-25T215835.png
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
skill_count: 2
skills:
- name: Check Gitar installation health
  slug: gitar-check-installation-health
- name: Onboard a GitLab project to Gitar and verify its status
  slug: gitar-onboard-gitlab-project
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
