---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Jetbrains Agentic Access
  operation_count: 60
  slug: jetbrains-agentic-access
  summary_line: 60 operations · 9 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL_template: https://{instance}.youtrack.cloud/api
  baseurl_source: spec_template
  description: JetBrains Activities API provides access to activity feeds across JetBrains Space, enabling retrieval of recent events, notifications, and user actions for integration with external tools and services
  name: JetBrains Activities API
  slug: jetbrains-activities-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Agent pool management
  name: JetBrains Agent Pools API
  slug: jetbrains-agent-pools-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Build agent management
  name: JetBrains Agents API
  slug: jetbrains-agents-api
- baseURL_template: https://{instance}.youtrack.cloud/api
  baseurl_source: spec_template
  description: Agile board management
  name: JetBrains Agile Boards API
  slug: jetbrains-agile-boards-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: HTTP API model and metadata
  name: JetBrains API Model API
  slug: jetbrains-api-model-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: Application management
  name: JetBrains Applications API
  slug: jetbrains-applications-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: Automation and CI/CD operations
  name: JetBrains Automation API
  slug: jetbrains-automation-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Build type/configuration management
  name: JetBrains Build Configurations API
  slug: jetbrains-build-configurations-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Build queue management
  name: JetBrains Build Queue API
  slug: jetbrains-build-queue-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Build execution and results
  name: JetBrains Builds API
  slug: jetbrains-builds-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: VCS change tracking
  name: JetBrains Changes API
  slug: jetbrains-changes-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: Chat and messaging operations
  name: JetBrains Chats API
  slug: jetbrains-chats-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: User group management
  name: JetBrains Groups API
  slug: jetbrains-groups-api
- baseURL_template: https://{instance}.youtrack.cloud/api
  baseurl_source: spec_template
  description: Issue management operations
  name: JetBrains Issues API
  slug: jetbrains-issues-api
- baseURL_template: https://{instance}.youtrack.cloud/api
  baseurl_source: spec_template
  description: The IssueTags API from JetBrains — 1 operation(s) for issuetags.
  name: JetBrains IssueTags API
  slug: jetbrains-issuetags-api
- baseURL: https://plugins.jetbrains.com
  baseurl_source: spec
  description: License checking operations
  name: JetBrains Licenses API
  slug: jetbrains-licenses-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: Package repository operations
  name: JetBrains Packages API
  slug: jetbrains-packages-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: Permission management
  name: JetBrains Permissions API
  slug: jetbrains-permissions-api
- baseURL: https://plugins.jetbrains.com
  baseurl_source: spec
  description: Plugin download operations
  name: JetBrains Plugin Download API
  slug: jetbrains-plugin-download-api
- baseURL: https://plugins.jetbrains.com
  baseurl_source: spec
  description: Plugin upload operations
  name: JetBrains Plugin Upload API
  slug: jetbrains-plugin-upload-api
- baseURL: https://plugins.jetbrains.com
  baseurl_source: spec
  description: Plugin listing and search
  name: JetBrains Plugins API
  slug: jetbrains-plugins-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: Project management
  name: JetBrains Projects API
  slug: jetbrains-projects-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: Role management
  name: JetBrains Roles API
  slug: jetbrains-roles-api
- baseURL_template: https://{instance}.youtrack.cloud/api
  baseurl_source: spec_template
  description: Saved search query management
  name: JetBrains Saved Queries API
  slug: jetbrains-saved-queries-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Server information and metadata
  name: JetBrains Server API
  slug: jetbrains-server-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: The Services API from JetBrains — 1 operation(s) for services.
  name: JetBrains Services API
  slug: jetbrains-services-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: Team and member management
  name: JetBrains Team Directory API
  slug: jetbrains-team-directory-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Test result tracking
  name: JetBrains Tests API
  slug: jetbrains-tests-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: User management
  name: JetBrains Users API
  slug: jetbrains-users-api
- baseURL_template: https://{server}/app/rest
  baseurl_source: spec_template
  description: Version control system root management
  name: JetBrains VCS Roots API
  slug: jetbrains-vcs-roots-api
- baseURL_template: https://{instance}.youtrack.cloud/api
  baseurl_source: spec_template
  description: Time tracking and work item management
  name: JetBrains Work Items API
  slug: jetbrains-work-items-api
- baseURL_template: https://{instance}.youtrack.cloud/hub/api/rest
  baseurl_source: spec_template
  description: OAuth2 client management
  name: JetBrains O Auth2 API
  slug: jetbrains-oauth2-api
- baseURL_template: https://{organization}.jetbrains.space/api/http
  baseurl_source: spec_template
  description: Code review operations
  name: JetBrains Codereviews API
  slug: jetbrains-codereviews-api
artifact_total: 91
collections:
- collection_type: open
  name: JetBrains Hub REST Activities API
  slug: open-jetbrains-activities-api
- collection_type: open
  name: JetBrains Hub REST Activities Agent Pools API
  slug: open-jetbrains-agent-pools-api
- collection_type: open
  name: JetBrains Hub REST Activities Agents API
  slug: open-jetbrains-agents-api
- collection_type: open
  name: JetBrains Hub REST Activities Agile Boards API
  slug: open-jetbrains-agile-boards-api
- collection_type: open
  name: JetBrains Hub REST Activities API Model API
  slug: open-jetbrains-api-model-api
- collection_type: open
  name: JetBrains Hub REST Activities Applications API
  slug: open-jetbrains-applications-api
- collection_type: open
  name: JetBrains Hub REST Activities Automation API
  slug: open-jetbrains-automation-api
- collection_type: open
  name: JetBrains Hub REST Activities Build Configurations API
  slug: open-jetbrains-build-configurations-api
- collection_type: open
  name: JetBrains Hub REST Activities Build Queue API
  slug: open-jetbrains-build-queue-api
- collection_type: open
  name: JetBrains Hub REST Activities Builds API
  slug: open-jetbrains-builds-api
- collection_type: open
  name: JetBrains Hub REST Activities Changes API
  slug: open-jetbrains-changes-api
- collection_type: open
  name: JetBrains Hub REST Activities Chats API
  slug: open-jetbrains-chats-api
- collection_type: open
  name: JetBrains Hub REST Activities Groups API
  slug: open-jetbrains-groups-api
- collection_type: open
  name: JetBrains Hub REST API
  slug: open-jetbrains-hub
- collection_type: open
  name: JetBrains Hub REST Activities Issues API
  slug: open-jetbrains-issues-api
- collection_type: open
  name: JetBrains Hub REST Activities IssueTags API
  slug: open-jetbrains-issuetags-api
- collection_type: open
  name: JetBrains Hub REST Activities Licenses API
  slug: open-jetbrains-licenses-api
- collection_type: open
  name: JetBrains Marketplace API
  slug: open-jetbrains-marketplace
- collection_type: open
  name: JetBrains Hub REST Activities OAuth2 API
  slug: open-jetbrains-oauth2-api
- collection_type: open
  name: JetBrains Hub REST Activities Packages API
  slug: open-jetbrains-packages-api
- collection_type: open
  name: JetBrains Hub REST Activities Permissions API
  slug: open-jetbrains-permissions-api
- collection_type: open
  name: JetBrains Hub REST Activities Plugin Download API
  slug: open-jetbrains-plugin-download-api
- collection_type: open
  name: JetBrains Hub REST Activities Plugin Upload API
  slug: open-jetbrains-plugin-upload-api
- collection_type: open
  name: JetBrains Hub REST Activities Plugins API
  slug: open-jetbrains-plugins-api
- collection_type: open
  name: JetBrains Hub REST Activities Projects API
  slug: open-jetbrains-projects-api
- collection_type: open
  name: JetBrains Hub REST Activities Roles API
  slug: open-jetbrains-roles-api
- collection_type: open
  name: JetBrains Hub REST Activities Saved Queries API
  slug: open-jetbrains-saved-queries-api
- collection_type: open
  name: JetBrains Hub REST Activities Server API
  slug: open-jetbrains-server-api
- collection_type: open
  name: JetBrains Hub REST Activities Services API
  slug: open-jetbrains-services-api
- collection_type: open
  name: JetBrains Space HTTP API
  slug: open-jetbrains-space
- collection_type: open
  name: JetBrains Hub REST Activities Team Directory API
  slug: open-jetbrains-team-directory-api
- collection_type: open
  name: JetBrains TeamCity REST API
  slug: open-jetbrains-teamcity
- collection_type: open
  name: JetBrains Hub REST Activities Tests API
  slug: open-jetbrains-tests-api
- collection_type: open
  name: JetBrains Hub REST Activities Users API
  slug: open-jetbrains-users-api
- collection_type: open
  name: JetBrains Hub REST Activities VCS Roots API
  slug: open-jetbrains-vcs-roots-api
- collection_type: open
  name: JetBrains Hub REST Activities Work Items API
  slug: open-jetbrains-work-items-api
- collection_type: open
  name: JetBrains YouTrack REST API
  slug: open-jetbrains-youtrack
common:
- group: commercial
  href: https://artifacts.apis.io/jetbrains/finops/jetbrains-finops.yml
  title: ''
  type: FinOps
  url: finops/jetbrains-finops.yml
- group: operate
  href: https://artifacts.apis.io/jetbrains/rate-limits/jetbrains-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jetbrains-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/jetbrains/rules/jetbrains-rules.yml
  title: ''
  type: Spectral
  url: rules/jetbrains-rules.yml
- group: design
  href: https://artifacts.apis.io/jetbrains/rules/jetbrains-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/jetbrains-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/jetbrains/vocabulary/jetbrains-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jetbrains-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/jetbrains/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/jetbrains/conformance/jetbrains-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jetbrains-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jetbrains/llms/jetbrains-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jetbrains-llms.txt
- group: auth
  href: https://artifacts.apis.io/jetbrains/well-known/jetbrains-youtrack-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jetbrains-youtrack-security.txt
- group: auth
  href: https://artifacts.apis.io/jetbrains/well-known/jetbrains-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jetbrains-status-security.txt
- group: auth
  href: https://artifacts.apis.io/jetbrains/well-known/jetbrains-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jetbrains-security.txt
- group: auth
  href: https://artifacts.apis.io/jetbrains/well-known/jetbrains-jetbrains-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jetbrains-jetbrains-security.txt
- group: auth
  href: https://artifacts.apis.io/jetbrains/well-known/jetbrains-hub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jetbrains-hub-security.txt
- group: agent
  href: https://artifacts.apis.io/jetbrains/well-known/jetbrains-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jetbrains-well-known.yml
- group: other
  href: https://artifacts.apis.io/jetbrains/hosts/jetbrains-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jetbrains-hosts.yml
- group: other
  href: https://artifacts.apis.io/jetbrains/vendors/jetbrains-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jetbrains-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jetbrains.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.jetbrains.com/teamcity/signup/cloud-enterprise/
- group: auth
  title: ''
  type: Security
  url: https://blog.jetbrains.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jetbrains.com/legal/docs/privacy/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jetbrains.com/youtrack/features/onboarding_pack.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jetbrains.com/store/?section=commercial&billing=yearly
- group: commercial
  href: https://artifacts.apis.io/jetbrains/plans/jetbrains-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jetbrains-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.jetbrains.com/
- group: other
  href: https://artifacts.apis.io/jetbrains/capabilities/jetbrains-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jetbrains-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/jetbrains/agentic-access/jetbrains-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jetbrains-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jetbrains/security/jetbrains-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jetbrains-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jetbrains/security/jetbrains-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jetbrains-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jetbrains/authentication/jetbrains-authentication.yml
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
- has_sources: true
  method: derived
  name: Jetbrains Finops
  primary_unit: user
  service_category: ''
  slug: jetbrains-finops
  template: false
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
overview: 'JetBrains publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Agent Pools API, Agents API, and 30 more. Tagged areas include CI/CD, Developer Tools, IDE, JetBrains, and IDEs.


  The JetBrains catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  JetBrains'' developer surface includes signup flow, getting-started guide, pricing, authentication, documentation, engineering blog, support, and 28 more developer resources.'
plans:
- name: Jetbrains Plans Pricing
  plan_count: 14
  slug: jetbrains-plans-pricing
- name: Jetbrains Price Estimates
  plan_count: 0
  slug: jetbrains-price-estimates
random_paper: 2
rate_limits:
- limit_count: 4
  name: Jetbrains Rate Limits
  slug: jetbrains-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: JetBrains — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jetbrains-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: JetBrains API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: jetbrains-rules
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 79.0
    catalog_earned_first_party: 12.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 56.6
    contract_governance: 31.8
    contract_quality: 61.1
    developer_ergonomics: 36.3
    discoverability: 69.6
    operational_transparency: 23.7
  previous_composite: 55.0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jetbrains/jetbrains-2026-06-20T183725.png
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
skill_count: 3
skills:
- name: jetbrains-build-queue-trigger-and-list
  slug: jetbrains-build-queue-trigger-and-list
- name: jetbrains-chats-send-message
  slug: jetbrains-chats-send-message
- name: jetbrains-create-issue-with-comment
  slug: jetbrains-create-issue-with-comment
slug: jetbrains
tags:
- CI/CD
- Developer Tools
- IDE
- JetBrains
- IDEs
- Continuous Integration
- Project Management
- Code Quality
- Data Science
- AI Coding - CI/CD - Developer Tools - IDE - JetBrains
website: https://www.jetbrains.com/
---
