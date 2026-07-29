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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
api_count: 11
apis:
- description: Endpoints related to Develocity authentication and authorization. The permissions required for these endpoints vary. Consult the endpoint descriptions.
  name: Gradle Auth API
  slug: gradle-auth-api
- description: Endpoints related to configuring the Build Cache nodes of the Develocity instance. To access these endpoints the user requires the `Configure Build Caching` permission.
  name: Gradle BuildCache API
  slug: gradle-buildcache-api
- description: Endpoints related to retrieving details of a build from the Develocity instance. To access these endpoints the user requires the `Access build data via the API` permission.
  name: Gradle Builds API
  slug: gradle-builds-api
- description: Endpoints for comparing two builds to identify differences in work unit inputs, dependencies, and other dimensions. To access these endpoints the user requires the `Access build data via the API` perm
  name: Gradle Comparison API
  slug: gradle-comparison-api
- description: All endpoints of the Develocity API.
  name: Gradle Develocity API
  slug: gradle-develocity-api
- description: 'Endpoints related to retrieving details about failures of builds from the Develocity instance. To access these endpoints the user requires the `Access build data via the API` permission. **<mark>Beta:'
  name: Gradle Failures API
  slug: gradle-failures-api
- description: '**This tag is deprecated, use `Develocity` instead**. All endpoints of the Develocity API.'
  name: Gradle GradleEnterprise API
  slug: gradle-gradleenterprise-api
- description: Endpoints related to the Develocity installation and its state.
  name: Gradle Meta API
  slug: gradle-meta-api
- description: 'Endpoints related to the management of project-level access control in Develocity. To access these endpoints the user requires the `Administer Projects` permission. **<mark>Beta:</mark> _The Projects '
  name: Gradle Projects API
  slug: gradle-projects-api
- description: Endpoints related to the management of Test Distribution resources. To access these endpoints the user requires the `Admin` permission.
  name: Gradle TestDistribution API
  slug: gradle-testdistribution-api
- description: Endpoints related to retrieving details of tests of the Develocity instance. To access these endpoints the user requires the `Access build data via the API` permission. The Develocity installation als
  name: Gradle Tests API
  slug: gradle-tests-api
artifact_total: 16
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.develocity.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.develocity.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.develocity.ai/2026.2/reference/develocity-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.develocity.ai/2026.2/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://gradle.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gradle
- group: operate
  title: ''
  type: Support
  url: https://community.gradle.org/
- group: start
  title: ''
  type: SignUp
  url: https://scans.gradle.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gradle.com/help/legal-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gradle.com/legal/privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/gradle-develocity-openapi.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gradle-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/gradle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gradle-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gradle-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gradle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gradle-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gradle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gradle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gradle-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gradle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/gradle-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gradle-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gradle-develocity-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gradle-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gradle.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.develocity.ai/2026.2/miscellaneous/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gradle-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/gradle-cli.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gradle-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gradle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/gradle/.github/blob/master/SECURITY.md
- group: auth
  title: ''
  type: TrustCenter
  url: security/gradle-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Gradle Inc. (Gradle Technologies) is the company behind the open-source Gradle Build Tool, downloaded more than 25 million times a month across the Java, JVM, Android, Kotlin, C/C++, and native ecosystems, and Develocity (formerly Gradle Enterprise), its commercial Developer Productivity Engineering platform. Develocity adds Build Scan, Build Cache, Predictive Test Selection, and Test Distribution to accelerate and stabilize builds and tests. The Develocity API is a JSON REST API, described with OpenAPI, that provides programmatic access to build data, failures, tests, projects, project groups, Build Cache node configuration, Test Distribution agent pools, and short-lived access tokens on a self-hosted Develocity instance. Founded in 2009 and headquartered in San Francisco with offices in Berlin and Melbourne, Gradle raised a $27M Series C led by Triangle Peak Partners.
image: https://assets.gradle.com/logo/develocity-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: gradle-mcp.yml
  slug: gradle-mcpyml
modified: '2026-07-19'
name: Gradle
nav: Providers
network: true
overview: 'Gradle publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth API, BuildCache API, Builds API, and 8 more. Tagged areas include Company, Developer Tools, Build Automation, Developer Productivity, and CI/CD.


  Gradle''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 27 more developer resources.'
random_paper: 56
score:
  band: strong
  composite: 57.2
  delta: -1.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.2
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 58.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gradle/refs/heads/main/screenshots/gradle-2026-07-25T220203.png
security:
- kind: authentication
  name: Gradle Authentication
  slug: gradle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gradle Domain Security
  slug: gradle-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gradle Vulnerability Disclosure
  slug: gradle-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gradle Trust Center
  slug: gradle-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: gradle
tags:
- Company
- Developer Tools
- Build Automation
- Developer Productivity
- CI/CD
- Build Analytics
- Testing
- DevOps
- Java
- Build Cache
website: https://docs.develocity.ai/
---
