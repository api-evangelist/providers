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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 33
  human_in_the_loop: 3
  name: Nevercode Agentic Access
  operation_count: 85
  slug: nevercode-agentic-access
  summary_line: 85 operations · 33 acting · 3 human-in-the-loop
api_count: 13
apis:
- description: REST API endpoints for app previews.
  name: Nevercode App Previews API
  slug: nevercode-app-previews-api
- description: REST API endpoints for applications.
  name: Nevercode Applications API
  slug: nevercode-applications-api
- description: REST API endpoints for billing.
  name: Nevercode Billing API
  slug: nevercode-billing-api
- description: REST API endpoints for build dashboards.
  name: Nevercode Build Dashboards API
  slug: nevercode-build-dashboards-api
- description: REST API endpoints for builds.
  name: Nevercode Builds API
  slug: nevercode-builds-api
- description: REST API endpoints for meta data.
  name: Nevercode Meta API
  slug: nevercode-meta-api
- description: REST API endpoints for over-the-air updates.
  name: Nevercode Over-the-air Updates API
  slug: nevercode-over-the-air-updates-api
- description: REST API endpoints for environment variables.
  name: Nevercode Secrets and Environment Vars API
  slug: nevercode-secrets-and-environment-vars-api
- description: REST API endpoints for team invitations.
  name: Nevercode Team Invitations API
  slug: nevercode-team-invitations-api
- description: REST API endpoints for team members.
  name: Nevercode Team Members API
  slug: nevercode-team-members-api
- description: REST API endpoints for teams.
  name: Nevercode Teams API
  slug: nevercode-teams-api
- description: REST API endpoints for tester groups.
  name: Nevercode Tester Groups API
  slug: nevercode-tester-groups-api
- description: REST API endpoints for users.
  name: Nevercode Users API
  slug: nevercode-users-api
artifact_total: 17
common:
- group: build
  title: ''
  type: Packages
  url: packages/nevercode-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nevercode-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://codemagic.io/security-statement
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nevercode-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nevercode-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nevercode-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nevercode-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nevercode-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nevercode-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nevercode-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nevercode-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nevercode-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nevercode-problem-types.yml
- group: company
  title: ''
  type: Website
  url: https://codemagic.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.codemagic.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codemagic.io
- group: docs
  title: ''
  type: APIReference
  url: https://codemagic.io/api/v3/schema
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codemagic.io/getting-started/about-codemagic/
- group: company
  title: ''
  type: Blog
  url: https://blog.codemagic.io
- group: operate
  title: ''
  type: Support
  url: https://github.com/orgs/codemagic-ci-cd/discussions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codemagic-ci-cd
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codemagic.io
- group: commercial
  title: ''
  type: Pricing
  url: https://codemagic.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://codemagic.io/signup
- group: start
  title: ''
  type: Login
  url: https://codemagic.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codemagic.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codemagic.io/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://codemagic.io/security-statement
created: '2026-07-17'
description: Codemagic (built by Nevercode, founded in Estonia) is a continuous integration and delivery (CI/CD) platform purpose-built for mobile app teams. It automates building, testing, code signing, and releasing apps across Flutter, React Native, native iOS and Android, Unity, Ionic, and .NET MAUI, and integrates with GitHub, GitLab, Bitbucket, and Azure DevOps. Its REST API (v3) exposes applications, builds, artifacts, teams, tester groups, secrets and environment variables, over-the-air updates, app previews, and billing so teams can trigger builds and manage their CI/CD pipelines programmatically.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nevercode.png
layout: provider
mcp_servers:
- description: ''
  name: nevercode-mcp.yml
  slug: nevercode-mcpyml
modified: '2026-07-20'
name: Nevercode
nav: Providers
network: true
overview: 'Nevercode publishes 13 APIs on the [APIs.io](https://apis.io/) network, including App Previews API, Applications API, Billing API, and 10 more. Tagged areas include Company, Continuous Integration, Continuous Delivery, CI/CD, and DevOps.


  Nevercode''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, support, and 22 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 52.7
  delta: -0.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 55.3
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nevercode Authentication
  slug: nevercode-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nevercode Domain Security
  slug: nevercode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nevercode
tags:
- Company
- Continuous Integration
- Continuous Delivery
- CI/CD
- DevOps
- Mobile
- Flutter
- Builds
- App Distribution
- Code Signing
website: https://codemagic.io
---
