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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 68
  human_in_the_loop: 60
  name: Devcycle Agentic Access
  operation_count: 112
  slug: devcycle-agentic-access
  summary_line: 112 operations · 68 acting · 60 human-in-the-loop
api_count: 25
apis:
- description: The Audiences API from DevCycle — 3 operation(s) for audiences.
  name: DevCycle Audiences API
  slug: devcycle-audiences-api
- description: The Audit Log API from DevCycle — 1 operation(s) for audit log.
  name: DevCycle Audit Log API
  slug: devcycle-audit-log-api
- description: The [Beta] Semantic Patch API from DevCycle — 1 operation(s) for [beta] semantic patch.
  name: DevCycle [Beta] Semantic Patch API
  slug: devcycle-beta-semantic-patch-api
- description: The Bucketing API API from DevCycle — 4 operation(s) for bucketing api.
  name: DevCycle Bucketing API API
  slug: devcycle-bucketing-api-api
- description: The Custom Properties API from DevCycle — 2 operation(s) for custom properties.
  name: DevCycle Custom Properties API
  slug: devcycle-custom-properties-api
- description: The [Deprecated] Features v1 API from DevCycle — 7 operation(s) for [deprecated] features v1.
  name: DevCycle [Deprecated] Features v1 API
  slug: devcycle-deprecated-features-v1-api
- description: The EdgeDB API from DevCycle — 1 operation(s) for edgedb.
  name: DevCycle EdgeDB API
  slug: devcycle-edgedb-api
- description: The Environments API from DevCycle — 4 operation(s) for environments.
  name: DevCycle Environments API
  slug: devcycle-environments-api
- description: The Feature Change Requests API from DevCycle — 7 operation(s) for feature change requests.
  name: DevCycle Feature Change Requests API
  slug: devcycle-feature-change-requests-api
- description: The Feature Configurations API from DevCycle — 1 operation(s) for feature configurations.
  name: DevCycle Feature Configurations API
  slug: devcycle-feature-configurations-api
- description: The Feature Opt-in API from DevCycle — 2 operation(s) for feature opt-in.
  name: DevCycle Feature Opt-in API
  slug: devcycle-feature-opt-in-api
- description: The Features v2 API from DevCycle — 6 operation(s) for features v2.
  name: DevCycle Features v2 API
  slug: devcycle-features-v2-api
- description: 'The Integrations: Dynatrace API from DevCycle — 2 operation(s) for integrations: dynatrace.'
  name: 'DevCycle Integrations: Dynatrace API'
  slug: devcycle-integrations-dynatrace-api
- description: 'The Integrations: Jira API from DevCycle — 3 operation(s) for integrations: jira.'
  name: 'DevCycle Integrations: Jira API'
  slug: devcycle-integrations-jira-api
- description: The Metric Associations API from DevCycle — 1 operation(s) for metric associations.
  name: DevCycle Metric Associations API
  slug: devcycle-metric-associations-api
- description: The Metrics API from DevCycle — 4 operation(s) for metrics.
  name: DevCycle Metrics API
  slug: devcycle-metrics-api
- description: 'See the OpenFeature documentation for more information: https://github.com/open-feature/protocol'
  name: DevCycle OpenFeature Remote Evaluation API (OFREP) API
  slug: devcycle-openfeature-remote-evaluation-api-ofrep-api
- description: The Overrides API from DevCycle — 3 operation(s) for overrides.
  name: DevCycle Overrides API
  slug: devcycle-overrides-api
- description: The Project Change Requests API from DevCycle — 1 operation(s) for project change requests.
  name: DevCycle Project Change Requests API
  slug: devcycle-project-change-requests-api
- description: The Projects API from DevCycle — 5 operation(s) for projects.
  name: DevCycle Projects API
  slug: devcycle-projects-api
- description: The Results API from DevCycle — 3 operation(s) for results.
  name: DevCycle Results API
  slug: devcycle-results-api
- description: The User Profiles API from DevCycle — 1 operation(s) for user profiles.
  name: DevCycle User Profiles API
  slug: devcycle-user-profiles-api
- description: The Variables API from DevCycle — 3 operation(s) for variables.
  name: DevCycle Variables API
  slug: devcycle-variables-api
- description: The Variations API from DevCycle — 2 operation(s) for variations.
  name: DevCycle Variations API
  slug: devcycle-variations-api
- description: The Webhooks API from DevCycle — 2 operation(s) for webhooks.
  name: DevCycle Webhooks API
  slug: devcycle-webhooks-api
arazzos:
- description: Create a feature flag, a variable, and a variation via the DevCycle Management API.
  name: DevCycle - create a feature with a variable and variation
  slug: devcycle-create-feature
- description: Fetch all variables and features for a user context and report an event.
  name: DevCycle - evaluate feature flags for a user (Bucketing API)
  slug: devcycle-evaluate-flags
artifact_total: 85
asyncapis:
- description: ''
  name: Devcycle Webhooks
  slug: devcycle-webhooks
collections:
- collection_type: postman
  name: DevCycle Bucketing Audiences API
  slug: postman-devcycle-audiences-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Audit Log API
  slug: postman-devcycle-audit-log-api
- collection_type: postman
  name: DevCycle Bucketing Audiences [Beta] Semantic Patch API
  slug: postman-devcycle-beta-semantic-patch-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Bucketing API API
  slug: postman-devcycle-bucketing-api-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Custom Properties API
  slug: postman-devcycle-custom-properties-api
- collection_type: postman
  name: DevCycle Bucketing Audiences [Deprecated] Features v1 API
  slug: postman-devcycle-deprecated-features-v1-api
- collection_type: postman
  name: DevCycle Bucketing Audiences EdgeDB API
  slug: postman-devcycle-edgedb-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Environments API
  slug: postman-devcycle-environments-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Feature Change Requests API
  slug: postman-devcycle-feature-change-requests-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Feature Configurations API
  slug: postman-devcycle-feature-configurations-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Feature Opt-in API
  slug: postman-devcycle-feature-opt-in-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Features v2 API
  slug: postman-devcycle-features-v2-api
- collection_type: postman
  name: 'DevCycle Bucketing Audiences Integrations: Dynatrace API'
  slug: postman-devcycle-integrations-dynatrace-api
- collection_type: postman
  name: 'DevCycle Bucketing Audiences Integrations: Jira API'
  slug: postman-devcycle-integrations-jira-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Metric Associations API
  slug: postman-devcycle-metric-associations-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Metrics API
  slug: postman-devcycle-metrics-api
- collection_type: postman
  name: DevCycle Bucketing Audiences OpenFeature Remote Evaluation API (OFREP) API
  slug: postman-devcycle-openfeature-remote-evaluation-api-ofrep-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Overrides API
  slug: postman-devcycle-overrides-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Project Change Requests API
  slug: postman-devcycle-project-change-requests-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Projects API
  slug: postman-devcycle-projects-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Results API
  slug: postman-devcycle-results-api
- collection_type: postman
  name: DevCycle Bucketing Audiences User Profiles API
  slug: postman-devcycle-user-profiles-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Variables API
  slug: postman-devcycle-variables-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Variations API
  slug: postman-devcycle-variations-api
- collection_type: postman
  name: DevCycle Bucketing Audiences Webhooks API
  slug: postman-devcycle-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DevCycle Bucketing Audiences API
  slug: open-devcycle-audiences-api
- collection_type: open
  name: DevCycle Bucketing Audiences Audit Log API
  slug: open-devcycle-audit-log-api
- collection_type: open
  name: DevCycle Bucketing Audiences [Beta] Semantic Patch API
  slug: open-devcycle-beta-semantic-patch-api
- collection_type: open
  name: DevCycle Bucketing Audiences Bucketing API API
  slug: open-devcycle-bucketing-api-api
- collection_type: open
  name: DevCycle Bucketing Audiences Custom Properties API
  slug: open-devcycle-custom-properties-api
- collection_type: open
  name: DevCycle Bucketing Audiences [Deprecated] Features v1 API
  slug: open-devcycle-deprecated-features-v1-api
- collection_type: open
  name: DevCycle Bucketing Audiences EdgeDB API
  slug: open-devcycle-edgedb-api
- collection_type: open
  name: DevCycle Bucketing Audiences Environments API
  slug: open-devcycle-environments-api
- collection_type: open
  name: DevCycle Bucketing Audiences Feature Change Requests API
  slug: open-devcycle-feature-change-requests-api
- collection_type: open
  name: DevCycle Bucketing Audiences Feature Configurations API
  slug: open-devcycle-feature-configurations-api
- collection_type: open
  name: DevCycle Bucketing Audiences Feature Opt-in API
  slug: open-devcycle-feature-opt-in-api
- collection_type: open
  name: DevCycle Bucketing Audiences Features v2 API
  slug: open-devcycle-features-v2-api
- collection_type: open
  name: 'DevCycle Bucketing Audiences Integrations: Dynatrace API'
  slug: open-devcycle-integrations-dynatrace-api
- collection_type: open
  name: 'DevCycle Bucketing Audiences Integrations: Jira API'
  slug: open-devcycle-integrations-jira-api
- collection_type: open
  name: DevCycle Bucketing Audiences Metric Associations API
  slug: open-devcycle-metric-associations-api
- collection_type: open
  name: DevCycle Bucketing Audiences Metrics API
  slug: open-devcycle-metrics-api
- collection_type: open
  name: DevCycle Bucketing Audiences OpenFeature Remote Evaluation API (OFREP) API
  slug: open-devcycle-openfeature-remote-evaluation-api-ofrep-api
- collection_type: open
  name: DevCycle Bucketing Audiences Overrides API
  slug: open-devcycle-overrides-api
- collection_type: open
  name: DevCycle Bucketing Audiences Project Change Requests API
  slug: open-devcycle-project-change-requests-api
- collection_type: open
  name: DevCycle Bucketing Audiences Projects API
  slug: open-devcycle-projects-api
- collection_type: open
  name: DevCycle Bucketing Audiences Results API
  slug: open-devcycle-results-api
- collection_type: open
  name: DevCycle Bucketing Audiences User Profiles API
  slug: open-devcycle-user-profiles-api
- collection_type: open
  name: DevCycle Bucketing Audiences Variables API
  slug: open-devcycle-variables-api
- collection_type: open
  name: DevCycle Bucketing Audiences Variations API
  slug: open-devcycle-variations-api
- collection_type: open
  name: DevCycle Bucketing Audiences Webhooks API
  slug: open-devcycle-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/devcycle-bucketing-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/devcycle/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.devcycle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devcycle.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.devcycle.com/management-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.devcycle.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.devcycle.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://devcycle.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devcycle.com/company/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devcycle.com/company/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://docs.devcycle.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.devcycle.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevCycleHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://devcycle.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.devcycle.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.devcycle.com/sdk/lifecycle/
- group: auth
  title: ''
  type: Compliance
  url: https://devcycle.com/security
- group: company
  title: ''
  type: Website
  url: https://www.devcycle.com/
- group: build
  title: ''
  type: Packages
  url: packages/devcycle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/devcycle-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/devcycle-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/devcycle-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/devcycle-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/devcycle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/devcycle-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devcycle-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/devcycle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/devcycle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devcycle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devcycle-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/devcycle-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/devcycle-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devcycle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devcycle-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/devcycle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/DevCycleHQ/.github/blob/main/.github/SECURITY.md
- group: auth
  title: ''
  type: TrustCenter
  url: security/devcycle-trust-center.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/devcycle-create-feature.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/devcycle-evaluate-flags.yml
created: '2026-07-17'
description: DevCycle is an OpenFeature-native feature flag and feature management platform (a Dynatrace company) for creating, targeting, rolling out, and cleaning up feature flags without disrupting developer workflow. It exposes a Management API for administering projects, environments, features, variables, variations, and audiences, and a Bucketing API for server-side flag evaluation, backed by client and server SDKs across every major language, OpenFeature providers, a `dvc` CLI, a Terraform provider, and an official hosted MCP server for AI coding agents.
image: https://devcycle.com/social-default.png
layout: provider
mcp_servers:
- description: ''
  name: devcycle-mcp.yml
  slug: devcycle-mcpyml
modified: '2026-07-18'
name: DevCycle
nav: Providers
network: true
overview: 'DevCycle publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Audit Log API, [Beta] Semantic Patch API, and 22 more. Tagged areas include Company, Enterprise Saas, Feature Flags, Feature Management, and Feature Flags as a Service.


  The DevCycle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DevCycle''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 33 more developer resources.'
random_paper: 7
score:
  band: strong
  composite: 62.1
  delta: -2.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 66.2
    developer_ergonomics: 83.3
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 52.6
  previous_composite: 64.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devcycle/refs/heads/main/screenshots/devcycle-2026-07-25T211810.png
security:
- kind: authentication
  name: Devcycle Authentication
  slug: devcycle-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Devcycle Domain Security
  slug: devcycle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Devcycle Vulnerability Disclosure
  slug: devcycle-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Devcycle Trust Center
  slug: devcycle-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: devcycle
tags:
- Company
- Enterprise Saas
- Feature Flags
- Feature Management
- Feature Flags as a Service
- Experimentation
- OpenFeature
- Developer Tools
- DevOps
website: https://www.devcycle.com/
---
