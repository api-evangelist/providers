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
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Assertible Agentic Access
  operation_count: 1
  slug: assertible-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://assertible.com
  baseurl_source: declared
  description: 'Assertible''s public programmatic surface, used to drive test runs from a CI/CD pipeline. It consists of two documented POST operations on assertible.com: a trigger URL that runs a web service''s tests '
  name: Assertible API
  slug: assertible-api
- baseURL: https://assertible.com
  baseurl_source: declared
  description: Notify Assertible of deployments and trigger tests
  name: Assertible Deployments API
  slug: assertible-deployments-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Assertible Deployments API
  slug: open-assertible-deployments-api
- collection_type: open
  name: Assertible API
  slug: open-assertible
common:
- group: company
  title: ''
  type: Website
  url: https://assertible.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/assertible-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assertible-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/assertible-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/assertible-conventions.yml
- group: design
  title: Idempotency and reversibility semantics
  type: Idempotency
  url: conventions/assertible-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/assertible-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/assertible-lifecycle.yml
- group: operate
  title: Assertible Status
  type: StatusPage
  url: http://status.assertible.com
- group: design
  title: ''
  type: Conformance
  url: conformance/assertible-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/assertible-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/assertible-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/assertible-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/assertible-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/assertible-plans-pricing.yml
- group: commercial
  title: Plans and Pricing
  type: Pricing
  url: https://assertible.com/plans
- group: commercial
  title: Terms of Service
  type: TermsOfService
  url: https://assertible.com/termsofservice
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://assertible.com/privacypolicy
- group: operate
  title: Contact Assertible
  type: Support
  url: https://assertible.com/contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AssertibleApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/assertible
- group: start
  title: Assertible Website
  type: Portal
  url: https://assertible.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://assertible.com/docs
- group: company
  title: Blog
  type: Blog
  url: https://assertible.com/blog
- group: start
  title: Sign Up
  type: SignUp
  url: https://assertible.com/signup
- group: start
  title: Login
  type: Login
  url: https://assertible.com/login
- group: build
  title: Assertible GitHub Organization
  type: GitHubOrganization
  url: https://github.com/assertible
created: '2025-01-08'
description: Assertible provides a reliable first line of defense against web service failures by providing simple and powerful assertions to test and monitor APIs. It enables automated API testing with assertions on response status, headers, body content, and performance, with integrations for CI/CD pipelines and notifications. Assertible supports scheduled API monitoring, deployment testing triggered via webhooks, and team collaboration for API quality assurance workflows. The platform integrates with GitHub, Slack, PagerDuty, and other tools for seamless notification and incident management.
features:
- description: Define assertions on API response status codes, headers, response body content, JSON Schema compliance, and response time to validate API behavior.
  name: API Test Assertions
- description: Run API tests on a scheduled basis (hourly, daily, etc.) to continuously monitor production APIs for availability and correctness.
  name: Scheduled Monitoring
- description: Trigger Assertible test suites automatically after deployments via webhooks, ensuring API quality gates are enforced in CI/CD pipelines.
  name: Deployment Testing
- description: Validate API responses against JSON Schema definitions to ensure response payloads match expected data structures.
  name: JSON Schema Validation
- description: Share test suites and API monitoring configurations across teams with role-based access and shared notification channels.
  name: Team Collaboration
finops:
- name: Assertible Finops
  service_category: API
  slug: assertible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/assertible.png
integrations:
- description: Integration with GitHub for triggering tests on pull requests and deployment events through GitHub Actions and webhooks.
  name: GitHub
- description: Slack notifications for test failures, alerts, and monitoring events from Assertible test runs.
  name: Slack
- description: PagerDuty integration for escalating API monitoring failures to on-call teams for incident response.
  name: PagerDuty
- description: Integration with CircleCI pipelines for running Assertible test suites as part of continuous integration workflows.
  name: CircleCI
layout: provider
modified: '2026-09-04'
name: Assertible
nav: Providers
network: true
overview: 'Assertible publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Deployments API, and 1 more. Tagged areas include API Testing, Monitoring, Quality Assurance, Testing, and CI/CD.


  Assertible''s developer surface includes authentication, pricing, support, developer portal, documentation, engineering blog, signup flow, and 21 more developer resources.'
plans:
- name: Assertible Plans Pricing
  plan_count: 4
  slug: assertible-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Assertible Rate Limits
  slug: assertible-rate-limits
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.5
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 28.6
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 66.7
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/assertible/refs/heads/main/screenshots/assertible-2026-06-20T172506.png
security:
- kind: authentication
  name: Assertible Authentication
  slug: assertible-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Assertible Domain Security
  slug: assertible-domain-security
  summary_line: TLSv1.2 · DMARC
slug: assertible
tags:
- API Testing
- Monitoring
- Quality Assurance
- Testing
- CI/CD
use_cases:
- description: Development teams trigger Assertible test suites after each deployment to verify APIs are functioning correctly before traffic shifts.
  name: Post-Deployment Validation
- description: Operations teams use scheduled Assertible tests to monitor API availability and receive alerts when endpoints fail.
  name: API Uptime Monitoring
- description: QA teams use JSON Schema assertions to validate that API responses match documented contracts and catch breaking changes.
  name: API Contract Testing
website: https://assertible.com/
---
