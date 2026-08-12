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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 87
  human_in_the_loop: 2
  name: Sonarsource Agentic Access
  operation_count: 156
  slug: sonarsource-agentic-access
  summary_line: 156 operations · 87 acting · 2 human-in-the-loop
api_count: 33
apis:
- description: Handle authentication.
  name: SonarSource authentication API
  slug: sonarsource-authentication-api
- description: Get information on Compute Engine tasks.
  name: SonarSource ce API
  slug: sonarsource-ce-api
- description: Get information about a component (file, directory, project, ...) and its ancestors or descendants. Update a project or module key.
  name: SonarSource components API
  slug: sonarsource-components-api
- description: Get duplication information for a project.
  name: SonarSource duplications API
  slug: sonarsource-duplications-api
- description: Manage user favorites
  name: SonarSource favorites API
  slug: sonarsource-favorites-api
- description: Removed since 6.3, please use api/favorites instead
  name: SonarSource favourites API
  slug: sonarsource-favourites-api
- description: Read and update Security Hotspots. Hotspots are deprecated and replaced by security issues (software quality) and vulnerabilities (type). Please use the API of security issues / vulnerabilities instea
  name: SonarSource hotspots API
  slug: sonarsource-hotspots-api
- description: Read and update issues.
  name: SonarSource issues API
  slug: sonarsource-issues-api
- description: Get the list of programming languages supported in this instance.
  name: SonarSource languages API
  slug: sonarsource-languages-api
- description: Get components or children with specified measures.
  name: SonarSource measures API
  slug: sonarsource-measures-api
- description: Get information on automatic metrics, and manage custom metrics. See also api/custom_measures.
  name: SonarSource metrics API
  slug: sonarsource-metrics-api
- description: Manage notifications of the authenticated user
  name: SonarSource notifications API
  slug: sonarsource-notifications-api
- description: Manage permission templates, and the granting and revoking of permissions at the global and project levels.
  name: SonarSource permissions API
  slug: sonarsource-permissions-api
- description: Manage project analyses.
  name: SonarSource project_analyses API
  slug: sonarsource-project-analyses-api
- description: Generate badges based on quality gates or measures
  name: SonarSource project_badges API
  slug: sonarsource-project-badges-api
- description: Manage branch (only available when the Branch plugin is installed)
  name: SonarSource project_branches API
  slug: sonarsource-project-branches-api
- description: Manage projects links.
  name: SonarSource project_links API
  slug: sonarsource-project-links-api
- description: Manage pull request (only available when the Branch plugin is installed)
  name: SonarSource project_pull_requests API
  slug: sonarsource-project-pull-requests-api
- description: Manage project tags
  name: SonarSource project_tags API
  slug: sonarsource-project-tags-api
- description: Manage project existence.
  name: SonarSource projects API
  slug: sonarsource-projects-api
- description: This web service is deprecated, please use api/settings instead.
  name: SonarSource properties API
  slug: sonarsource-properties-api
- description: Manage quality gates, including conditions and project association.
  name: SonarSource qualitygates API
  slug: sonarsource-qualitygates-api
- description: Manage quality profiles.
  name: SonarSource qualityprofiles API
  slug: sonarsource-qualityprofiles-api
- description: Get and update some details of automatic rules, and manage custom rules.
  name: SonarSource rules API
  slug: sonarsource-rules-api
- description: Manage settings.
  name: SonarSource settings API
  slug: sonarsource-settings-api
- description: Get details on source files. See also api/tests.
  name: SonarSource sources API
  slug: sonarsource-sources-api
- description: Removed since 6.3, please use api/measures/search_history instead
  name: SonarSource timemachine API
  slug: sonarsource-timemachine-api
- description: Manage user groups.
  name: SonarSource user_groups API
  slug: sonarsource-user-groups-api
- description: Removed since 6.3, please use api/favorites and api/notifications instead
  name: SonarSource user_properties API
  slug: sonarsource-user-properties-api
- description: List, create, and delete a user's access tokens.
  name: SonarSource user_tokens API
  slug: sonarsource-user-tokens-api
- description: Manage users.
  name: SonarSource users API
  slug: sonarsource-users-api
- description: Webhooks allow to notify external services when a project analysis is done
  name: SonarSource webhooks API
  slug: sonarsource-webhooks-api
- description: Get information on the web api supported on this instance.
  name: SonarSource webservices API
  slug: sonarsource-webservices-api
artifact_total: 37
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonarsource-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sonarsource-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonarsource-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sonarsource.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonarsource.com/sonarqube-cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sonarsource.com/sonarqube-cloud/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://community.sonarsource.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sonarsource.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SonarSource
- group: operate
  title: ''
  type: Roadmap
  url: https://www.sonarsource.com/products/sonarcloud/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sonarsource.com/plans-and-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://sonarcloud.io/sessions/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonarsource.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonarsource.com/company/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonarcloud.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.sonarsource.com/sonarqube-cloud/deprecations-and-removals/
- group: build
  title: ''
  type: Packages
  url: packages/sonarsource-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sonarsource-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sonarsource-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sonarsource-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sonarsource-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sonarsource-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonarsource-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sonarsource-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sonarsource-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sonarsource-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sonarsource-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sonarsource-web-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/sonarsource-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SonarSource (Sonar) builds the industry-standard tooling for code quality and code security, trusted by large engineering organizations to keep code Clean. Its product line spans SonarQube Cloud (formerly SonarCloud, the hosted SaaS analysis service), SonarQube Server (self-managed), SonarQube for IDE (formerly SonarLint), and the SonarQube Community Build. SonarQube Cloud exposes a REST Web API for programmatically managing projects, issues, quality gates, quality profiles, rules, measures, hotspots, permissions, webhooks, and user tokens, plus a family of first-party scanners (npm, PyPI, Maven, Gradle, .NET, and Docker) for wiring analysis into CI/CD pipelines.
image: https://avatars.githubusercontent.com/u/545988?v=4
layout: provider
mcp_servers:
- description: ''
  name: sonarsource-mcp.yml
  slug: sonarsource-mcpyml
modified: '2026-07-21'
name: SonarSource
nav: Providers
network: true
overview: 'SonarSource publishes 33 APIs on the [APIs.io](https://apis.io/) network, including authentication API, ce API, components API, and 30 more. Tagged areas include Company, Code Quality, Static Analysis, Code Security, and SAST.


  SonarSource''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 44
score:
  band: developing
  composite: 54.7
  delta: -1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.7
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Sonarsource Authentication
  slug: sonarsource-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Sonarsource Domain Security
  slug: sonarsource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonarsource
tags:
- Company
- Code Quality
- Static Analysis
- Code Security
- SAST
- Developer Tools
- DevOps
- Code Review
- SonarQube
website: https://www.sonarsource.com/
---
