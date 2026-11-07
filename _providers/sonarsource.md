---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 87
  human_in_the_loop: 2
  name: Sonarsource Agentic Access
  operation_count: 156
  slug: sonarsource-agentic-access
  summary_line: 156 operations · 87 acting · 2 human-in-the-loop
api_count: 33
apis:
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Handle authentication.
  name: SonarSource Authentication API
  slug: sonarsource-authentication-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get information on Compute Engine tasks.
  name: SonarSource Ce API
  slug: sonarsource-ce-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get information about a component (file, directory, project, ...) and its ancestors or descendants. Update a project or module key.
  name: SonarSource Components API
  slug: sonarsource-components-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get duplication information for a project.
  name: SonarSource Duplications API
  slug: sonarsource-duplications-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage user favorites
  name: SonarSource Favorites API
  slug: sonarsource-favorites-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Removed since 6.3, please use api/favorites instead
  name: SonarSource Favourites API
  slug: sonarsource-favourites-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Read and update Security Hotspots. Hotspots are deprecated and replaced by security issues (software quality) and vulnerabilities (type). Please use the API of security issues / vulnerabilities instea
  name: SonarSource Hotspots API
  slug: sonarsource-hotspots-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Read and update issues.
  name: SonarSource Issues API
  slug: sonarsource-issues-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get the list of programming languages supported in this instance.
  name: SonarSource Languages API
  slug: sonarsource-languages-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get components or children with specified measures.
  name: SonarSource Measures API
  slug: sonarsource-measures-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get information on automatic metrics, and manage custom metrics. See also api/custom_measures.
  name: SonarSource Metrics API
  slug: sonarsource-metrics-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage notifications of the authenticated user
  name: SonarSource Notifications API
  slug: sonarsource-notifications-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage permission templates, and the granting and revoking of permissions at the global and project levels.
  name: SonarSource Permissions API
  slug: sonarsource-permissions-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage project analyses.
  name: SonarSource Project Analyses API
  slug: sonarsource-project-analyses-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Generate badges based on quality gates or measures
  name: SonarSource Project Badges API
  slug: sonarsource-project-badges-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage branch (only available when the Branch plugin is installed)
  name: SonarSource Project Branches API
  slug: sonarsource-project-branches-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage projects links.
  name: SonarSource Project Links API
  slug: sonarsource-project-links-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage pull request (only available when the Branch plugin is installed)
  name: SonarSource Project Pull Requests API
  slug: sonarsource-project-pull-requests-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage project tags
  name: SonarSource Project Tags API
  slug: sonarsource-project-tags-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage project existence.
  name: SonarSource Projects API
  slug: sonarsource-projects-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: This web service is deprecated, please use api/settings instead.
  name: SonarSource Properties API
  slug: sonarsource-properties-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage quality profiles.
  name: SonarSource Qualityprofiles API
  slug: sonarsource-qualityprofiles-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get and update some details of automatic rules, and manage custom rules.
  name: SonarSource Rules API
  slug: sonarsource-rules-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage settings.
  name: SonarSource Settings API
  slug: sonarsource-settings-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get details on source files. See also api/tests.
  name: SonarSource Sources API
  slug: sonarsource-sources-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage user groups.
  name: SonarSource User Groups API
  slug: sonarsource-user-groups-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Removed since 6.3, please use api/favorites and api/notifications instead
  name: SonarSource User Properties API
  slug: sonarsource-user-properties-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: List, create, and delete a user's access tokens.
  name: SonarSource User Tokens API
  slug: sonarsource-user-tokens-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage users.
  name: SonarSource Users API
  slug: sonarsource-users-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Webhooks allow to notify external services when a project analysis is done
  name: SonarSource Webhooks API
  slug: sonarsource-webhooks-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Manage quality gates, including conditions and project association.
  name: SonarSource Quality Gates API
  slug: sonarsource-quality-gates-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Removed since 6.3, please use api/measures/search_history instead
  name: SonarSource Time Machine API
  slug: sonarsource-time-machine-api
- baseURL: https://sonarcloud.io/api
  baseurl_source: declared
  description: Get information on the web api supported on this instance.
  name: SonarSource Web Services API
  slug: sonarsource-web-services-api
artifact_total: 78
collections:
- collection_type: open
  name: SonarQube Cloud Web authentication API
  slug: open-sonarsource-authentication-api
- collection_type: open
  name: SonarQube Cloud Web authentication ce API
  slug: open-sonarsource-ce-api
- collection_type: open
  name: SonarQube Cloud Web authentication components API
  slug: open-sonarsource-components-api
- collection_type: open
  name: SonarQube Cloud Web authentication duplications API
  slug: open-sonarsource-duplications-api
- collection_type: open
  name: SonarQube Cloud Web authentication favorites API
  slug: open-sonarsource-favorites-api
- collection_type: open
  name: SonarQube Cloud Web authentication favourites API
  slug: open-sonarsource-favourites-api
- collection_type: open
  name: SonarQube Cloud Web authentication hotspots API
  slug: open-sonarsource-hotspots-api
- collection_type: open
  name: SonarQube Cloud Web authentication issues API
  slug: open-sonarsource-issues-api
- collection_type: open
  name: SonarQube Cloud Web authentication languages API
  slug: open-sonarsource-languages-api
- collection_type: open
  name: SonarQube Cloud Web authentication measures API
  slug: open-sonarsource-measures-api
- collection_type: open
  name: SonarQube Cloud Web authentication metrics API
  slug: open-sonarsource-metrics-api
- collection_type: open
  name: SonarQube Cloud Web authentication notifications API
  slug: open-sonarsource-notifications-api
- collection_type: open
  name: SonarQube Cloud Web authentication permissions API
  slug: open-sonarsource-permissions-api
- collection_type: open
  name: SonarQube Cloud Web authentication project_analyses API
  slug: open-sonarsource-project-analyses-api
- collection_type: open
  name: SonarQube Cloud Web authentication project_badges API
  slug: open-sonarsource-project-badges-api
- collection_type: open
  name: SonarQube Cloud Web authentication project_branches API
  slug: open-sonarsource-project-branches-api
- collection_type: open
  name: SonarQube Cloud Web authentication project_links API
  slug: open-sonarsource-project-links-api
- collection_type: open
  name: SonarQube Cloud Web authentication project_pull_requests API
  slug: open-sonarsource-project-pull-requests-api
- collection_type: open
  name: SonarQube Cloud Web authentication project_tags API
  slug: open-sonarsource-project-tags-api
- collection_type: open
  name: SonarQube Cloud Web authentication projects API
  slug: open-sonarsource-projects-api
- collection_type: open
  name: SonarQube Cloud Web authentication properties API
  slug: open-sonarsource-properties-api
- collection_type: open
  name: SonarQube Cloud Web authentication qualitygates API
  slug: open-sonarsource-qualitygates-api
- collection_type: open
  name: SonarQube Cloud Web authentication qualityprofiles API
  slug: open-sonarsource-qualityprofiles-api
- collection_type: open
  name: SonarQube Cloud Web authentication rules API
  slug: open-sonarsource-rules-api
- collection_type: open
  name: SonarQube Cloud Web authentication settings API
  slug: open-sonarsource-settings-api
- collection_type: open
  name: SonarQube Cloud Web authentication sources API
  slug: open-sonarsource-sources-api
- collection_type: open
  name: SonarQube Cloud Web authentication timemachine API
  slug: open-sonarsource-timemachine-api
- collection_type: open
  name: SonarQube Cloud Web authentication user_groups API
  slug: open-sonarsource-user-groups-api
- collection_type: open
  name: SonarQube Cloud Web authentication user_properties API
  slug: open-sonarsource-user-properties-api
- collection_type: open
  name: SonarQube Cloud Web authentication user_tokens API
  slug: open-sonarsource-user-tokens-api
- collection_type: open
  name: SonarQube Cloud Web authentication users API
  slug: open-sonarsource-users-api
- collection_type: open
  name: SonarQube Cloud Web authentication webhooks API
  slug: open-sonarsource-webhooks-api
- collection_type: open
  name: SonarQube Cloud Web authentication webservices API
  slug: open-sonarsource-webservices-api
common:
- group: design
  href: https://artifacts.apis.io/sonarsource/rules/sonarsource-rules.yml
  title: ''
  type: Spectral
  url: rules/sonarsource-rules.yml
- group: other
  href: https://artifacts.apis.io/sonarsource/hosts/sonarsource-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sonarsource-hosts.yml
- group: build
  href: https://artifacts.apis.io/sonarsource/integrations/sonarsource-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/sonarsource-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/sonarsource/vendors/sonarsource-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sonarsource-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sonarsource.com/
- group: auth
  title: ''
  type: Security
  url: https://www.sonarsource.com/solutions/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sonarsource.com/company/newsroom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sonarsource.com/developers/
- group: commercial
  href: https://artifacts.apis.io/sonarsource/finops/sonarsource-finops.yml
  title: ''
  type: FinOps
  url: finops/sonarsource-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sonar/overview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonarsource
- group: design
  href: https://artifacts.apis.io/sonarsource/vocabulary/sonarsource-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sonarsource-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/SonarSource/sonarqube-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sonarsource.com/llms.txt
- group: operate
  href: https://artifacts.apis.io/sonarsource/rate-limits/sonarsource-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sonarsource-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sonarsource/plans/sonarsource-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sonarsource-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.sonarsource.com/
- group: other
  href: https://artifacts.apis.io/sonarsource/capabilities/sonarsource-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sonarsource-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/sonarsource/security/sonarsource-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sonarsource-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/sonarsource/agentic-access/sonarsource-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sonarsource-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sonarsource/authentication/sonarsource-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sonarsource-authentication.yml
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
  href: https://artifacts.apis.io/sonarsource/packages/sonarsource-packages.yml
  title: ''
  type: Packages
  url: packages/sonarsource-packages.yml
- group: build
  href: https://artifacts.apis.io/sonarsource/packages/sonarsource-packages.yml
  title: ''
  type: SDKs
  url: packages/sonarsource-packages.yml
- group: build
  href: https://artifacts.apis.io/sonarsource/cli/sonarsource-cli.yml
  title: ''
  type: CLI
  url: cli/sonarsource-cli.yml
- group: design
  href: https://artifacts.apis.io/sonarsource/conventions/sonarsource-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sonarsource-conventions.yml
- group: design
  href: https://artifacts.apis.io/sonarsource/lifecycle/sonarsource-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sonarsource-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sonarsource/changelog/sonarsource-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sonarsource-changelog.yml
- group: agent
  href: https://artifacts.apis.io/sonarsource/llms/sonarsource-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sonarsource-llms.txt
- group: agent
  href: https://artifacts.apis.io/sonarsource/well-known/sonarsource-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sonarsource-well-known.yml
- group: agent
  href: https://artifacts.apis.io/sonarsource/mcp/sonarsource-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sonarsource-mcp.yml
- group: design
  href: https://artifacts.apis.io/sonarsource/errors/sonarsource-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sonarsource-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sonarsource/conformance/sonarsource-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sonarsource-conformance.yml
- group: other
  href: https://artifacts.apis.io/sonarsource/overlays/sonarsource-web-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sonarsource-web-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/sonarsource/data-model/sonarsource-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sonarsource-data-model.yml
- group: agent
  href: https://artifacts.apis.io/sonarsource/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SonarSource (Sonar) builds the industry-standard tooling for code quality and code security, trusted by large engineering organizations to keep code Clean. Its product line spans SonarQube Cloud (formerly SonarCloud, the hosted SaaS analysis service), SonarQube Server (self-managed), SonarQube for IDE (formerly SonarLint), and the SonarQube Community Build. SonarQube Cloud exposes a REST Web API for programmatically managing projects, issues, quality gates, quality profiles, rules, measures, hotspots, permissions, webhooks, and user tokens, plus a family of first-party scanners (npm, PyPI, Maven, Gradle, .NET, and Docker) for wiring analysis into CI/CD pipelines.
finops:
- has_sources: true
  method: derived
  name: Sonarsource Finops
  primary_unit: organization
  service_category: ''
  slug: sonarsource-finops
  template: false
image: https://avatars.githubusercontent.com/u/545988?v=4
layout: provider
mcp_servers:
- description: ''
  name: SonarSource MCP Server
  slug: sonarqube-mcp-server
modified: '2026-07-21'
name: SonarSource
nav: Providers
network: true
overview: 'SonarSource is listed with 33 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Ce API, Components API, and 30 more. Tagged areas include Company, Code Quality, Static Analysis, Code Security, and SAST.


  The SonarSource catalog on APIs.io includes 1 Spectral governance ruleset.


  SonarSource''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 41 more developer resources.'
plans:
- name: Sonarsource Plans Pricing
  plan_count: 5
  slug: sonarsource-plans-pricing
- name: Sonarsource Price Estimates
  plan_count: 0
  slug: sonarsource-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Sonarsource Rate Limits
  slug: sonarsource-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: SonarSource API Rules
  rule_count: 55
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 6
  slug: sonarsource-rules
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.5
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 14.5
    developer_ergonomics: 74.4
    discoverability: 80.4
    operational_transparency: 57.9
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 34
      marker_coverage: 100.0
      total: 34
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/sonarsource/sonarsource-2026-08-17T082000.png
security:
- kind: authentication
  name: Sonarsource Authentication
  slug: sonarsource-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Sonarsource Domain Security
  slug: sonarsource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: sonarsource-check-quality-gate
  slug: sonarsource-check-quality-gate
- name: sonarsource-provision-project
  slug: sonarsource-provision-project
- name: sonarsource-triage-issues
  slug: sonarsource-triage-issues
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
- CI/CD
- Security
- SonarCloud
website: https://www.sonarsource.com/
---
