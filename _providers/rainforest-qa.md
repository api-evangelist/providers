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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 64
  human_in_the_loop: 1
  name: Rainforest Qa Agentic Access
  operation_count: 113
  slug: rainforest-qa-agentic-access
  summary_line: 113 operations · 64 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: Operations about callbacks
  name: Rainforest QA callback API
  slug: rainforest-qa-callback-api
- description: Operations about clients
  name: Rainforest QA clients API
  slug: rainforest-qa-clients-api
- description: Operations about connections
  name: Rainforest QA connections API
  slug: rainforest-qa-connections-api
- description: Operations about credit_cards
  name: Rainforest QA credit_cards API
  slug: rainforest-qa-credit-cards-api
- description: Operations about environments
  name: Rainforest QA environments API
  slug: rainforest-qa-environments-api
- description: Operations about features
  name: Rainforest QA features API
  slug: rainforest-qa-features-api
- description: Operations about folders
  name: Rainforest QA folders API
  slug: rainforest-qa-folders-api
- description: Operations about generators
  name: Rainforest QA generators API
  slug: rainforest-qa-generators-api
- description: Operations about on_premise_crowds
  name: Rainforest QA on_premise_crowd API
  slug: rainforest-qa-on-premise-crowd-api
- description: Operations about run_groups
  name: Rainforest QA run_groups API
  slug: rainforest-qa-run-groups-api
- description: Operations about runs
  name: Rainforest QA runs API
  slug: rainforest-qa-runs-api
- description: Operations about site_environments
  name: Rainforest QA site_environments API
  slug: rainforest-qa-site-environments-api
- description: Operations about sites
  name: Rainforest QA sites API
  slug: rainforest-qa-sites-api
- description: Operations about tags
  name: Rainforest QA tags API
  slug: rainforest-qa-tags-api
- description: Operations about test_results
  name: Rainforest QA test_results API
  slug: rainforest-qa-test-results-api
- description: Operations about tests
  name: Rainforest QA tests API
  slug: rainforest-qa-tests-api
- description: Operations about users
  name: Rainforest QA users API
  slug: rainforest-qa-users-api
- description: Operations about vm_stacks
  name: Rainforest QA vm_stack API
  slug: rainforest-qa-vm-stack-api
artifact_total: 24
asyncapis:
- description: ''
  name: Rainforest Qa Webhooks
  slug: rainforest-qa-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.rainforestqa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.rainforestqa.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.rainforestqa.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.rainforestqa.com/docs/the-rainforest-api
- group: operate
  title: ''
  type: Support
  url: https://help.rainforestqa.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rainforestqa.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rainforestapp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rainforestqa.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.rainforestqa.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rainforestqa.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rainforestqa.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rainforestqa.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.rainforestqa.com/
- group: build
  title: ''
  type: CLI
  url: cli/rainforest-qa-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/rainforest-qa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rainforest-qa-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rainforest-qa-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rainforest-qa-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rainforest-qa-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rainforest-qa-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rainforest-qa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.rainforestqa.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rainforest-qa-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rainforest-qa-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rainforest-qa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rainforest-qa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rainforest-qa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rainforest-qa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rainforestqa.com/
created: '2026-07-17'
description: Rainforest QA is a no-code software testing platform that combines AI-powered test creation, crowdsourced manual QA, and automated browser testing in one place. Its REST API and command-line interface let teams create and manage tests, environments, sites and folders, trigger and rerun test runs, and pull JUnit results directly from CI/CD pipelines. Run-lifecycle webhooks (initializing_run, before_run, after_run) with HMAC-signed callbacks support advanced deploy-gated integrations. Authentication is via a CLIENT_TOKEN API key header.
image: https://files.readme.io/b4c4a73843894a94128b97dfacf7cd0936025ad438ac2bcff381bdfcae2125ec-VariationPrimary_AspectFull_ColorWhite2x.png
layout: provider
mcp_servers:
- description: ''
  name: rainforest-qa-mcp.yml
  slug: rainforest-qa-mcpyml
modified: '2026-07-20'
name: Rainforest QA
nav: Providers
network: true
overview: 'Rainforest QA publishes 18 APIs on the [APIs.io](https://apis.io/) network, including callback API, clients API, connections API, and 15 more. Tagged areas include Testing, QA, Test Automation, Software Testing, and CI/CD.


  The Rainforest QA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rainforest QA''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 23 more developer resources.'
random_paper: 44
score:
  band: strong
  composite: 58.6
  delta: -1.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.8
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rainforest Qa Authentication
  slug: rainforest-qa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rainforest Qa Domain Security
  slug: rainforest-qa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Rainforest Qa Trust Center
  slug: rainforest-qa-trust-center
  summary_line: SOC 2, HIPAA
slug: rainforest-qa
tags:
- Testing
- QA
- Test Automation
- Software Testing
- CI/CD
- Quality Assurance
- Crowdsourced Testing
- No-Code
- Developer Tools
website: https://www.rainforestqa.com/
---
