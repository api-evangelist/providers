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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for managing TestFairy projects, builds, testers, tester groups, sites, webhooks, permissions, feedback, and audit trails. Authenticated with HTTP Basic (email:api-key) or OIDC bearer tokens.
  name: TestFairy REST API
  slug: testfairy-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Testfairy Webhooks Asyncapi
  slug: testfairy-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://testfairy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.saucelabs.com/testfairy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.saucelabs.com/testfairy/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.saucelabs.com/testfairy/api-reference/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.saucelabs.com/testfairy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/testfairy
- group: start
  title: ''
  type: SignUp
  url: https://app.testfairy.com/login
- group: start
  title: ''
  type: Login
  url: https://app.testfairy.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://saucelabs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saucelabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saucelabs.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.saucelabs.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.saucelabs.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/testfairy-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/testfairy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/testfairy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/testfairy-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/testfairy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/testfairy-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/testfairy-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/testfairy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/testfairy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/testfairy-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/testfairy-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/testfairy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.saucelabs.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/testfairy-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/testfairy-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/testfairy-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/testfairy-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/testfairy-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testfairy-domain-security.yml
created: '2026-07-17'
description: TestFairy is a mobile app testing and distribution platform, now part of Sauce Labs, that lets teams upload iOS and Android builds, distribute them to beta testers, and record video sessions of testers using the app alongside device logs, crash reports, and CPU/memory/network telemetry for debugging. It exposes a REST API for managing projects, builds, testers, tester groups, sites, webhooks, and audit trails, plus a separate Upload API for pushing APK/AAB/IPA packages and symbol files from CI. Native SDKs (iOS, Android) and cross-platform wrappers (React Native, Flutter, Cordova, Unity, Xamarin, NativeScript) instrument apps, and command-line uploaders integrate with Jenkins, fastlane, Travis, and CircleCI. Authentication is HTTP Basic (email + API key) or OIDC bearer tokens.
image: https://raw.githubusercontent.com/api-evangelist/testfairy/main/testfairy.png
layout: provider
mcp_servers:
- description: ''
  name: testfairy-mcp.yml
  slug: testfairy-mcpyml
modified: '2026-07-21'
name: TestFairy
nav: Providers
network: true
overview: 'TestFairy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Testing, App Distribution, and Beta Testing.


  The TestFairy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TestFairy''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, authentication, and 25 more developer resources.'
random_paper: 93
score:
  band: developing
  composite: 53.4
  delta: -0.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 54.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testfairy/refs/heads/main/screenshots/testfairy-2026-08-17T082325.png
security:
- kind: authentication
  name: Testfairy Authentication
  slug: testfairy-authentication
  summary_line: http/bearer/apiKey · 3 schemes
- kind: domain-security
  name: Testfairy Domain Security
  slug: testfairy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Testfairy Trust Center
  slug: testfairy-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001, GDPR, CCPA, CSA, FSQS (EMEA financial services)
slug: testfairy
tags:
- Company
- Mobile
- Testing
- App Distribution
- Beta Testing
- Quality Assurance
- Developer Tools
- Session Recording
- Crash Reporting
- DevOps
website: https://testfairy.com
---
