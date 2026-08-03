---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Jetbrains Agentic Access
  operation_count: 60
  slug: jetbrains-agentic-access
  summary_line: 60 operations · 9 acting · 1 human-in-the-loop
api_count: 33
apis:
- description: Activity feed operations
  name: JetBrains Activities API
  slug: jetbrains-activities-api
- description: Agent pool management
  name: JetBrains Agent Pools API
  slug: jetbrains-agent-pools-api
- description: Build agent management
  name: JetBrains Agents API
  slug: jetbrains-agents-api
- description: Agile board management
  name: JetBrains Agile Boards API
  slug: jetbrains-agile-boards-api
- description: HTTP API model and metadata
  name: JetBrains API Model API
  slug: jetbrains-api-model-api
- description: Application management
  name: JetBrains Applications API
  slug: jetbrains-applications-api
- description: Automation and CI/CD operations
  name: JetBrains Automation API
  slug: jetbrains-automation-api
- description: Build type/configuration management
  name: JetBrains Build Configurations API
  slug: jetbrains-build-configurations-api
- description: Build queue management
  name: JetBrains Build Queue API
  slug: jetbrains-build-queue-api
- description: Build execution and results
  name: JetBrains Builds API
  slug: jetbrains-builds-api
- description: VCS change tracking
  name: JetBrains Changes API
  slug: jetbrains-changes-api
- description: Chat and messaging operations
  name: JetBrains Chats API
  slug: jetbrains-chats-api
- description: Code review operations
  name: JetBrains Code Reviews API
  slug: jetbrains-code-reviews-api
- description: User group management
  name: JetBrains Groups API
  slug: jetbrains-groups-api
- description: Issue management operations
  name: JetBrains Issues API
  slug: jetbrains-issues-api
- description: The IssueTags API from JetBrains — 1 operation(s) for issuetags.
  name: JetBrains IssueTags API
  slug: jetbrains-issuetags-api
- description: License checking operations
  name: JetBrains Licenses API
  slug: jetbrains-licenses-api
- description: OAuth2 client management
  name: JetBrains OAuth2 API
  slug: jetbrains-oauth2-api
- description: Package repository operations
  name: JetBrains Packages API
  slug: jetbrains-packages-api
- description: Permission management
  name: JetBrains Permissions API
  slug: jetbrains-permissions-api
- description: Plugin download operations
  name: JetBrains Plugin Download API
  slug: jetbrains-plugin-download-api
- description: Plugin upload operations
  name: JetBrains Plugin Upload API
  slug: jetbrains-plugin-upload-api
- description: Plugin listing and search
  name: JetBrains Plugins API
  slug: jetbrains-plugins-api
- description: Project management
  name: JetBrains Projects API
  slug: jetbrains-projects-api
- description: Role management
  name: JetBrains Roles API
  slug: jetbrains-roles-api
- description: Saved search query management
  name: JetBrains Saved Queries API
  slug: jetbrains-saved-queries-api
- description: Server information and metadata
  name: JetBrains Server API
  slug: jetbrains-server-api
- description: The Services API from JetBrains — 1 operation(s) for services.
  name: JetBrains Services API
  slug: jetbrains-services-api
- description: Team and member management
  name: JetBrains Team Directory API
  slug: jetbrains-team-directory-api
- description: Test result tracking
  name: JetBrains Tests API
  slug: jetbrains-tests-api
- description: User management
  name: JetBrains Users API
  slug: jetbrains-users-api
- description: Version control system root management
  name: JetBrains VCS Roots API
  slug: jetbrains-vcs-roots-api
- description: Time tracking and work item management
  name: JetBrains Work Items API
  slug: jetbrains-work-items-api
artifact_total: 54
collections:
- collection_type: open
  name: JetBrains Hub REST API
  slug: open-jetbrains-hub
- collection_type: open
  name: JetBrains Marketplace API
  slug: open-jetbrains-marketplace
- collection_type: open
  name: JetBrains Space HTTP API
  slug: open-jetbrains-space
- collection_type: open
  name: JetBrains TeamCity REST API
  slug: open-jetbrains-teamcity
- collection_type: open
  name: JetBrains YouTrack REST API
  slug: open-jetbrains-youtrack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jetbrains-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jetbrains-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetbrains-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jetbrains-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jetbrains
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jetbrains
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetbrains.com/help/
- group: company
  title: ''
  type: Blog
  url: https://blog.jetbrains.com/
- group: operate
  title: ''
  type: Support
  url: https://www.jetbrains.com/support/
- group: operate
  title: ''
  type: Issues
  url: https://youtrack.jetbrains.com/
created: '2025-01-01'
description: JetBrains is a software development company that provides integrated development environments, CI/CD tools, issue tracking, and team collaboration platforms for software developers. Their product suite includes IntelliJ IDEA, TeamCity, YouTrack, Space, Hub, and the JetBrains Marketplace, all of which offer APIs for programmatic integration and automation of development workflows.
finops:
- name: Jetbrains Finops
  service_category: Developer Tools
  slug: jetbrains-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jetbrains.png
json_schemas:
- name: JetBrains TeamCity Build Agent
  property_count: 9
  slug: build-agent
- name: JetBrains TeamCity Build
  property_count: 12
  slug: build
- name: JetBrains YouTrack Issue
  property_count: 11
  slug: issue
- name: JetBrains Marketplace Plugin
  property_count: 10
  slug: plugin
- name: JetBrains Project
  property_count: 6
  slug: project
- name: JetBrains User
  property_count: 7
  slug: user
json_structures:
- name: Jetbrains Structure
  property_count: 0
  slug: jetbrains-structure
jsonld:
- class_count: 11
  name: Jetbrains Context
  property_count: 7
  slug: jetbrains-context
layout: provider
modified: '2026-05-19'
name: JetBrains
nav: Providers
network: true
overview: 'JetBrains publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Agent Pools API, Agents API, and 30 more. Tagged areas include CI/CD, Developer Tools, and IDE.


  The JetBrains catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JetBrains'' developer surface includes authentication, documentation, engineering blog, support, and 6 more developer resources.'
plans:
- name: Jetbrains Plans Pricing
  plan_count: 7
  slug: jetbrains-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Jetbrains Rate Limits
  slug: jetbrains-rate-limits
rules:
- name: JetBrains API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jetbrains-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 74.3
    developer_ergonomics: 26.1
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jetbrains/refs/heads/main/screenshots/jetbrains-2026-06-20T183725.png
security:
- kind: authentication
  name: Jetbrains Authentication
  slug: jetbrains-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Jetbrains Domain Security
  slug: jetbrains-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jetbrains Vulnerability Disclosure
  slug: jetbrains-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jetbrains
tags:
- CI/CD
- Developer Tools
- IDE
---
