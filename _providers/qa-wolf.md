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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Continuous integration triggers and pipeline gating
  name: QA Wolf CI API
  slug: qa-wolf-ci-api
- description: Deployment and environment lifecycle notifications to QA Wolf
  name: QA Wolf Webhooks API
  slug: qa-wolf-webhooks-api
artifact_total: 7
asyncapis:
- description: ''
  name: Qa Wolf Webhooks
  slug: qa-wolf-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.qawolf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qawolf.com/qawolf/Welcome-to-QA-Wolf
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qawolf.com/qawolf/Welcome-to-QA-Wolf
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qawolf.com/qawolf/rest-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qawolf.com/qawolf/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.qawolf.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qawolf
- group: operate
  title: ''
  type: Support
  url: mailto:hello@qawolf.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qawolf.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qawolf.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.qawolf.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qawolf.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qawolf.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qawolf.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.qawolf.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/qa-wolf-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qa-wolf-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qa-wolf-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/qa-wolf-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qa-wolf-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qa-wolf-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qa-wolf-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qa-wolf-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qa-wolf-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qa-wolf-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qa-wolf-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qa-wolf-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qa-wolf-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qa-wolf-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'QA Wolf is a hybrid platform and service that takes QA off software teams'' plates: AI maps an application''s user journeys, converts plain-language prompts into Playwright and Appium tests, and runs those flows in massively parallel cloud infrastructure across web, iOS, and Android. Alongside the platform QA Wolf offers coverage-as-a-service staffed by dedicated QA engineers. For developers it ships a first-party TypeScript toolchain — the qawolf CLI, a CI SDK, and the @qawolf/flows, @qawolf/emails, @qawolf/testkit, and @qawolf/pom libraries — plus a small v0 REST API and CI webhooks for triggering runs and gating deployment pipelines. This profile was enriched by the API Evangelist pipeline from QA Wolf''s public developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qa-wolf.png
layout: provider
mcp_servers:
- description: ''
  name: qa-wolf-mcp.yml
  slug: qa-wolf-mcpyml
modified: '2026-07-20'
name: QA Wolf
nav: Providers
network: true
overview: 'QA Wolf publishes 2 APIs on the [APIs.io](https://apis.io/) network: CI API and Webhooks API. Tagged areas include Company, Devtools, Testing, Test Automation, and QA.


  The QA Wolf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  QA Wolf''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 47
score:
  band: developing
  composite: 54.6
  delta: -4.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.3
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 58.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Qa Wolf Authentication
  slug: qa-wolf-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qa Wolf Domain Security
  slug: qa-wolf-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Qa Wolf Trust Center
  slug: qa-wolf-trust-center
  summary_line: SOC 2, HIPAA
slug: qa-wolf
tags:
- Company
- Devtools
- Testing
- Test Automation
- QA
- CI/CD
- Playwright
- Developer Tools
website: https://www.qawolf.com/
---
