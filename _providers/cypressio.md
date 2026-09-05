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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Enterprise reporting API that returns test and run analytics and raw test-result data from Cypress Cloud. Requests are HTTP GET with an organization API key passed as the token query parameter, and da
  name: Cypress Cloud Data Extract API
  slug: cypress-cloud-data-extract-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cypressio-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cypress.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cypress.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cypress.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cypress.io/api/table-of-contents
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cypress.io/app/get-started/why-cypress
- group: operate
  title: ''
  type: Support
  url: https://www.cypress.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.cypress.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cypress-io
- group: operate
  title: ''
  type: Roadmap
  url: https://www.cypress.io/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cypress.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.cypress.io/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.cypress.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cypress.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cypress.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cypressstatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cypress.io/app/references/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cypressio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cypressio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cypressio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cypressio-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cypressio-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cypressio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cypressio-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cypressio-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cypressio-domain-security.yml
created: '2026-07-17'
description: Cypress.io, Inc. builds Cypress, an open-source, JavaScript-based end-to-end and component testing framework that runs tests directly in the browser with time-travel debugging, automatic waiting, and cross-browser support. Its commercial Cypress Cloud service adds test parallelization, smart orchestration, analytics, Test Replay, UI Coverage, and automated accessibility checks, plus an enterprise Data Extract API for exporting test and run analytics in CSV, JSON, or XLSX. Cypress is widely adopted across CI/CD pipelines for reliable, developer-friendly web application testing.
image: https://avatars.githubusercontent.com/u/8908513?v=4
layout: provider
modified: '2026-07-18'
name: Cypress.io
nav: Providers
network: true
overview: 'Cypress.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Testing, End-to-End Testing, Test Automation, and Quality Assurance.


  Cypress.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 37.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cypressio/refs/heads/main/screenshots/cypressio-2026-07-25T211057.png
security:
- kind: authentication
  name: Cypressio Authentication
  slug: cypressio-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cypressio Domain Security
  slug: cypressio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cypressio Trust Center
  slug: cypressio-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: cypressio
tags:
- Company
- Testing
- End-to-End Testing
- Test Automation
- Quality Assurance
- Developer Tools
- CI/CD
- Accessibility
- JavaScript
website: https://docs.cypress.io/
---
