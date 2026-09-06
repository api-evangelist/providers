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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints related to Develocity authentication and authorization. The permissions required for these endpoints vary. Consult the endpoint descriptions.
  name: Gradle Auth API
  slug: gradle-auth-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints related to configuring the Build Cache nodes of the Develocity instance. To access these endpoints the user requires the `Configure Build Caching` permission.
  name: Gradle BuildCache API
  slug: gradle-buildcache-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints related to retrieving details of a build from the Develocity instance. To access these endpoints the user requires the `Access build data via the API` permission.
  name: Gradle Builds API
  slug: gradle-builds-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints for comparing two builds to identify differences in work unit inputs, dependencies, and other dimensions. To access these endpoints the user requires the `Access build data via the API` perm
  name: Gradle Comparison API
  slug: gradle-comparison-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: 'Endpoints related to retrieving details about failures of builds from the Develocity instance. To access these endpoints the user requires the `Access build data via the API` permission. **<mark>Beta:'
  name: Gradle Failures API
  slug: gradle-failures-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints related to the Develocity installation and its state.
  name: Gradle Meta API
  slug: gradle-meta-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: 'Endpoints related to the management of project-level access control in Develocity. To access these endpoints the user requires the `Administer Projects` permission. **<mark>Beta:</mark> _The Projects '
  name: Gradle Projects API
  slug: gradle-projects-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints related to the management of Test Distribution resources. To access these endpoints the user requires the `Admin` permission.
  name: Gradle TestDistribution API
  slug: gradle-testdistribution-api
- baseURL: https://develocity.example.com/api
  baseurl_source: declared
  description: Endpoints related to retrieving details of tests of the Develocity instance. To access these endpoints the user requires the `Access build data via the API` permission. The Develocity installation als
  name: Gradle Tests API
  slug: gradle-tests-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Develocity Auth API
  slug: open-gradle-auth-api
- collection_type: open
  name: Develocity Auth BuildCache API
  slug: open-gradle-buildcache-api
- collection_type: open
  name: Develocity Auth Builds API
  slug: open-gradle-builds-api
- collection_type: open
  name: Develocity Auth Comparison API
  slug: open-gradle-comparison-api
- collection_type: open
  name: Auth Develocity API
  slug: open-gradle-develocity-api
- collection_type: open
  name: Develocity Auth Failures API
  slug: open-gradle-failures-api
- collection_type: open
  name: Develocity Auth GradleEnterprise API
  slug: open-gradle-gradleenterprise-api
- collection_type: open
  name: Develocity Auth Meta API
  slug: open-gradle-meta-api
- collection_type: open
  name: Develocity Auth Projects API
  slug: open-gradle-projects-api
- collection_type: open
  name: Develocity Auth TestDistribution API
  slug: open-gradle-testdistribution-api
- collection_type: open
  name: Develocity Auth Tests API
  slug: open-gradle-tests-api
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
  url: openapi/_original/gradle-develocity-openapi.yaml
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
- description: Develocity ships official Model Context Protocol servers that give AI agents access to Develocity build data and analytics. Because Develocity is self-hosted, the MCP server is exposed on the customer
  name: Gradle MCP Server
  slug: gradle-mcp-server
modified: '2026-07-19'
name: Gradle
nav: Providers
network: true
overview: 'Gradle publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, BuildCache API, Builds API, and 6 more. Tagged areas include Company, Developer Tools, Build Automation, Developer Productivity, and CI/CD.


  Gradle''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 27 more developer resources.'
random_paper: 14
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 58.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 54.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
