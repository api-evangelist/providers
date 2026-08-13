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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Gospotcheck Agentic Access
  operation_count: 53
  slug: gospotcheck-agentic-access
  summary_line: 53 operations · 27 acting · 2 human-in-the-loop
api_count: 13
apis:
- description: The AsyncJobs API from GoSpotCheck — 1 operation(s) for asyncjobs.
  name: GoSpotCheck AsyncJobs API
  slug: gospotcheck-asyncjobs-api
- description: The CatalogItems API from GoSpotCheck — 2 operation(s) for catalogitems.
  name: GoSpotCheck CatalogItems API
  slug: gospotcheck-catalogitems-api
- description: The Catalogs API from GoSpotCheck — 2 operation(s) for catalogs.
  name: GoSpotCheck Catalogs API
  slug: gospotcheck-catalogs-api
- description: The CustomViews API from GoSpotCheck — 3 operation(s) for customviews.
  name: GoSpotCheck CustomViews API
  slug: gospotcheck-customviews-api
- description: The MissionResponses API from GoSpotCheck — 2 operation(s) for missionresponses.
  name: GoSpotCheck MissionResponses API
  slug: gospotcheck-missionresponses-api
- description: The Missions API from GoSpotCheck — 2 operation(s) for missions.
  name: GoSpotCheck Missions API
  slug: gospotcheck-missions-api
- description: The PlaceGroups API from GoSpotCheck — 4 operation(s) for placegroups.
  name: GoSpotCheck PlaceGroups API
  slug: gospotcheck-placegroups-api
- description: The Places API from GoSpotCheck — 2 operation(s) for places.
  name: GoSpotCheck Places API
  slug: gospotcheck-places-api
- description: The TaskResponses API from GoSpotCheck — 2 operation(s) for taskresponses.
  name: GoSpotCheck TaskResponses API
  slug: gospotcheck-taskresponses-api
- description: The Tasks API from GoSpotCheck — 2 operation(s) for tasks.
  name: GoSpotCheck Tasks API
  slug: gospotcheck-tasks-api
- description: The Teams API from GoSpotCheck — 4 operation(s) for teams.
  name: GoSpotCheck Teams API
  slug: gospotcheck-teams-api
- description: The UserPlaceAssignments API from GoSpotCheck — 2 operation(s) for userplaceassignments.
  name: GoSpotCheck UserPlaceAssignments API
  slug: gospotcheck-userplaceassignments-api
- description: The Users API from GoSpotCheck — 4 operation(s) for users.
  name: GoSpotCheck Users API
  slug: gospotcheck-users-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://gospotcheck.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gsc.docs.apiary.io/
- group: docs
  title: ''
  type: Documentation
  url: https://gsc.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://gsc.docs.apiary.io/
- group: operate
  title: ''
  type: Support
  url: https://support.gospotcheck.com
- group: company
  title: ''
  type: Blog
  url: https://www.gospotcheck.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gospotcheck
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gospotcheck.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admin.gospotcheck.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gospotcheck.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gospotcheck.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gospotcheck.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/gospotcheck-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/gospotcheck-external-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gospotcheck-external-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/gospotcheck-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gospotcheck-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gospotcheck-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gospotcheck-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gospotcheck-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gospotcheck-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gospotcheck-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/gospotcheck-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gospotcheck-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gospotcheck-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gospotcheck-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gospotcheck-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gospotcheck-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.gospotcheck.com/about/disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gospotcheck-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gospotcheck-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gospotcheck-domain-security.yml
created: '2026-07-17'
description: GoSpotCheck (by FORM) is a mobile field-execution and retail-execution platform used by field teams to collect store-level data, complete surveys and tasks ("missions") at places, and audit merchandising and compliance. Its External API lets developers sync people, places, place groups, teams, catalogs, and catalog items, and pull MissionResponse and TaskResponse data out of GoSpotCheck to build custom reports and integrations. The API is REST over HTTPS with OAuth2 bearer authentication, a standard response envelope (request/paging/data/errors), page-number pagination, field-operator filtering, related-resource includes, and asynchronous CSV export for large datasets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gospotcheck.png
layout: provider
mcp_servers:
- description: ''
  name: gospotcheck-mcp.yml
  slug: gospotcheck-mcpyml
modified: '2026-07-19'
name: GoSpotCheck
nav: Providers
network: true
overview: 'GoSpotCheck publishes 13 APIs on the [APIs.io](https://apis.io/) network, including AsyncJobs API, CatalogItems API, Catalogs API, and 10 more. Tagged areas include Company, Retail Execution, Field Service, Data Collection, and Surveys.


  GoSpotCheck''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 26 more developer resources.'
random_paper: 98
rate_limits:
- limit_count: 3
  name: Gospotcheck Rate Limits
  slug: gospotcheck-rate-limits
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 55.6
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 71.1
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gospotcheck/refs/heads/main/screenshots/gospotcheck-2026-07-25T220116.png
security:
- kind: authentication
  name: Gospotcheck Authentication
  slug: gospotcheck-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gospotcheck Domain Security
  slug: gospotcheck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gospotcheck Vulnerability Disclosure
  slug: gospotcheck-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gospotcheck Trust Center
  slug: gospotcheck-trust-center
  summary_line: trust center published
slug: gospotcheck
tags:
- Company
- Retail Execution
- Field Service
- Data Collection
- Surveys
- Merchandising
- CPG
- Mobile
website: https://gospotcheck.com
---
