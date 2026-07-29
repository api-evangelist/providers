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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for security ratings, portfolios, scorecards, factor and issue data, historical scores, industry benchmarks, reporting, and webhook Rules.
  name: SecurityScorecard API
  slug: securityscorecard-api
artifact_total: 6
asyncapis:
- description: ''
  name: Security Scorecard Webhooks
  slug: security-scorecard-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://securityscorecard.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://securityscorecard.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://securityscorecard.readme.io/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://securityscorecard.readme.io/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://securityscorecard.readme.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://securityscorecard.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://securityscorecard.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://securityscorecard.com/free-account-trial/
- group: start
  title: ''
  type: Login
  url: https://platform.securityscorecard.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://securityscorecard.com/eusa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://securityscorecard.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/securityscorecard
- group: operate
  title: ''
  type: StatusPage
  url: https://securityscorecard.statuspage.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://securityscorecard.readme.io/reference/backwards-compatibility
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/security-scorecard-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/security-scorecard-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/security-scorecard-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/security-scorecard-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/security-scorecard-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/security-scorecard-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/security-scorecard-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/security-scorecard-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/security-scorecard-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/security-scorecard-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/security-scorecard-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/security-scorecard-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/security-scorecard-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/security-scorecard-domain-security.yml
created: '2026-07-17'
description: 'SecurityScorecard is a cybersecurity ratings and third-party risk management platform that continuously rates the security posture of any company from the outside in, producing an A-F security score across ten risk factors. Its REST API (base https://api.securityscorecard.io) lets customers manage portfolios of monitored companies, pull scorecards, factor scores, historical trends, issues/findings, industry benchmarks, and generate reports, and react to changes through webhook-driven Rules. Authentication is a static API token ("Authorization: Token <key>"), and first-party npm SDK and CLI packages are published under the @securityscorecard organization. Originally surfaced as a GV (Google Ventures) portfolio company, this profile has been enriched from SecurityScorecard''s public developer documentation.'
image: https://securityscorecard.com/wp-content/uploads/2023/01/ssc-logo.png
layout: provider
mcp_servers:
- description: ''
  name: security-scorecard-mcp.yml
  slug: security-scorecard-mcpyml
modified: '2026-07-21'
name: SecurityScorecard
nav: Providers
network: true
overview: 'SecurityScorecard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Cybersecurity, Security Ratings, and Third-Party Risk.


  The SecurityScorecard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SecurityScorecard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 43
score:
  band: developing
  composite: 52.4
  delta: 6.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 69.6
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.7
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Security Scorecard Authentication
  slug: security-scorecard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Security Scorecard Domain Security
  slug: security-scorecard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Security Scorecard Trust Center
  slug: security-scorecard-trust-center
  summary_line: ISO 27001, PCI DSS, HIPAA, GDPR
slug: security-scorecard
tags:
- Company
- Enterprise
- Cybersecurity
- Security Ratings
- Third-Party Risk
- Risk Management
- Attack Surface
- Compliance
website: https://securityscorecard.com
---
