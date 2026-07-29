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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Launchable (CloudBees Smart Tests) service API that the Launchable CLI calls to record builds, create test sessions, upload test results, request predictive test subsets and split subsets for para
  name: Launchable API
  slug: launchable-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.cloudbees.com/capabilities/cloudbees-smart-tests
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.launchableinc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.launchableinc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.launchableinc.com/resources/cli-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.launchableinc.com/getting-started/
- group: docs
  title: ''
  type: ProductDocumentation
  url: https://docs.cloudbees.com/docs/cloudbees-smart-tests/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/launchableinc
- group: company
  title: ''
  type: Blog
  url: https://www.cloudbees.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.cloudbees.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudbees.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.launchableinc.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.launchableinc.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudbees.com/legal/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/launchable-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/launchable-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/launchable-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/launchable-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/launchable-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/launchable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cloudbees.com/company/trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/launchable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/launchable-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/launchable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cloudbees.com/legal/security-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/launchable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudbeesstatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/launchable-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/launchable-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/launchable-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/launchable-sandbox.yml
created: '2026-07-17'
description: 'Launchable is a software development intelligence platform for continuous integration that applies machine learning to CI and test data to speed up software delivery. Its flagship capability, Predictive Test Selection, records builds, test sessions and test results from a team''s CI pipeline and returns a prioritized subset of tests most likely to fail for a given change, letting teams run a fraction of a suite while retaining most of its failure-detection power. The platform also provides test suite parallelization, flaky/unhealthy test detection, trends and test reporting, and Slack and GitHub notifications. Access is CLI-mediated: the open-source Launchable CLI (now the CloudBees Smart Tests CLI) wraps the service REST API and integrates with more than twenty test runners and build tools across Java, Python, Ruby, Go, JavaScript, .NET and Perl. Launchable was founded by Jenkins creator Kohsuke Kawaguchi and is now part of CloudBees, where the product ships as CloudBees Smart
  Tests.'
image: https://cdn.prod.website-files.com/695e1939655d6c0175b126da/69a531b363ec7c7abb4b8a30_OG-Smart-Tests.png
layout: provider
modified: '2026-07-19'
name: Launchable
nav: Providers
network: true
overview: 'Launchable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Continuous Integration, Testing, Test Automation, and Developer Tools.


  Launchable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 39.4
  delta: 0.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 38.5
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/launchable/refs/heads/main/screenshots/launchable-2026-07-25T224613.png
security:
- kind: authentication
  name: Launchable Authentication
  slug: launchable-authentication
  summary_line: apiKey/openIdConnect · 2 schemes
- kind: domain-security
  name: Launchable Domain Security
  slug: launchable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Launchable Vulnerability Disclosure
  slug: launchable-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Launchable Trust Center
  slug: launchable-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2025, CSA STAR, NIST CSF 2.0, GDPR, CCPA
slug: launchable
tags:
- Company
- Continuous Integration
- Testing
- Test Automation
- Developer Tools
- DevOps
- Machine Learning
- Software Delivery
- Predictive Test Selection
- CI/CD
website: https://www.cloudbees.com/capabilities/cloudbees-smart-tests
---
