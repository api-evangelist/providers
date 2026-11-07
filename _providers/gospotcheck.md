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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Gospotcheck Agentic Access
  operation_count: 53
  slug: gospotcheck-agentic-access
  summary_line: 53 operations · 27 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The AsyncJobs API from GoSpotCheck — 1 operation(s) for asyncjobs.
  name: GoSpotCheck AsyncJobs API
  slug: gospotcheck-asyncjobs-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Catalogs API from GoSpotCheck — 2 operation(s) for catalogs.
  name: GoSpotCheck Catalogs API
  slug: gospotcheck-catalogs-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The CustomViews API from GoSpotCheck — 3 operation(s) for customviews.
  name: GoSpotCheck CustomViews API
  slug: gospotcheck-customviews-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The MissionResponses API from GoSpotCheck — 2 operation(s) for missionresponses.
  name: GoSpotCheck MissionResponses API
  slug: gospotcheck-missionresponses-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Missions API from GoSpotCheck — 2 operation(s) for missions.
  name: GoSpotCheck Missions API
  slug: gospotcheck-missions-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The PlaceGroups API from GoSpotCheck — 4 operation(s) for placegroups.
  name: GoSpotCheck PlaceGroups API
  slug: gospotcheck-placegroups-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Places API from GoSpotCheck — 2 operation(s) for places.
  name: GoSpotCheck Places API
  slug: gospotcheck-places-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The TaskResponses API from GoSpotCheck — 2 operation(s) for taskresponses.
  name: GoSpotCheck TaskResponses API
  slug: gospotcheck-taskresponses-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Tasks API from GoSpotCheck — 2 operation(s) for tasks.
  name: GoSpotCheck Tasks API
  slug: gospotcheck-tasks-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Teams API from GoSpotCheck — 4 operation(s) for teams.
  name: GoSpotCheck Teams API
  slug: gospotcheck-teams-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The UserPlaceAssignments API from GoSpotCheck — 2 operation(s) for userplaceassignments.
  name: GoSpotCheck UserPlaceAssignments API
  slug: gospotcheck-userplaceassignments-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Users API from GoSpotCheck — 4 operation(s) for users.
  name: GoSpotCheck Users API
  slug: gospotcheck-users-api
- baseURL: https://api.gospotcheck.com
  baseurl_source: declared
  description: The Catalog Items API from GoSpotCheck — 2 operation(s) for catalog items.
  name: GoSpotCheck Catalog Items API
  slug: gospotcheck-catalog-items-api
artifact_total: 38
collections:
- collection_type: open
  name: GoSpotCheck External AsyncJobs API
  slug: open-gospotcheck-asyncjobs-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs CatalogItems API
  slug: open-gospotcheck-catalogitems-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs Catalogs API
  slug: open-gospotcheck-catalogs-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs CustomViews API
  slug: open-gospotcheck-customviews-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs MissionResponses API
  slug: open-gospotcheck-missionresponses-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs Missions API
  slug: open-gospotcheck-missions-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs PlaceGroups API
  slug: open-gospotcheck-placegroups-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs Places API
  slug: open-gospotcheck-places-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs TaskResponses API
  slug: open-gospotcheck-taskresponses-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs Tasks API
  slug: open-gospotcheck-tasks-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs Teams API
  slug: open-gospotcheck-teams-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs UserPlaceAssignments API
  slug: open-gospotcheck-userplaceassignments-api
- collection_type: open
  name: GoSpotCheck External AsyncJobs Users API
  slug: open-gospotcheck-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/gospotcheck/plans/gospotcheck-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gospotcheck-plans-pricing.yml
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
  href: https://artifacts.apis.io/gospotcheck/authentication/gospotcheck-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gospotcheck-authentication.yml
- group: docs
  href: https://artifacts.apis.io/gospotcheck/openapi/_original/gospotcheck-external-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/gospotcheck-external-openapi.yml
- group: other
  href: https://artifacts.apis.io/gospotcheck/overlays/gospotcheck-external-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gospotcheck-external-overlay.yaml
- group: design
  href: https://artifacts.apis.io/gospotcheck/conventions/gospotcheck-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gospotcheck-conventions.yml
- group: design
  href: https://artifacts.apis.io/gospotcheck/errors/gospotcheck-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gospotcheck-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/gospotcheck/rate-limits/gospotcheck-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gospotcheck-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/gospotcheck/lifecycle/gospotcheck-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gospotcheck-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/gospotcheck/lifecycle/gospotcheck-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gospotcheck-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gospotcheck/data-model/gospotcheck-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gospotcheck-data-model.yml
- group: design
  href: https://artifacts.apis.io/gospotcheck/conformance/gospotcheck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gospotcheck-conformance.yml
- group: build
  href: https://artifacts.apis.io/gospotcheck/packages/gospotcheck-packages.yml
  title: ''
  type: Packages
  url: packages/gospotcheck-packages.yml
- group: agent
  href: https://artifacts.apis.io/gospotcheck/mcp/gospotcheck-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gospotcheck-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gospotcheck/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/gospotcheck/agentic-access/gospotcheck-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gospotcheck-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/gospotcheck/llms/gospotcheck-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gospotcheck-llms.txt
- group: agent
  href: https://artifacts.apis.io/gospotcheck/well-known/gospotcheck-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gospotcheck-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gospotcheck/well-known/gospotcheck-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gospotcheck-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.gospotcheck.com/about/disclosure-program
- group: auth
  href: https://artifacts.apis.io/gospotcheck/security/gospotcheck-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gospotcheck-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gospotcheck/security/gospotcheck-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gospotcheck-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gospotcheck/security/gospotcheck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gospotcheck-domain-security.yml
created: '2026-07-17'
description: GoSpotCheck (by FORM) is a mobile field-execution and retail-execution platform used by field teams to collect store-level data, complete surveys and tasks ("missions") at places, and audit merchandising and compliance. Its External API lets developers sync people, places, place groups, teams, catalogs, and catalog items, and pull MissionResponse and TaskResponse data out of GoSpotCheck to build custom reports and integrations. The API is REST over HTTPS with OAuth2 bearer authentication, a standard response envelope (request/paging/data/errors), page-number pagination, field-operator filtering, related-resource includes, and asynchronous CSV export for large datasets.
finops:
- has_sources: true
  method: derived
  name: Gospotcheck Finops
  primary_unit: user
  service_category: ''
  slug: gospotcheck-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gospotcheck.png
layout: provider
modified: '2026-07-19'
name: GoSpotCheck
nav: Providers
network: true
overview: 'GoSpotCheck publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including AsyncJobs API, Catalogs API, CustomViews API, and 10 more. Tagged areas include Company, Retail Execution, Field Service Management, Data Collection, and Surveys.


  The GoSpotCheck catalog on APIs.io includes 1 Spectral governance ruleset.


  GoSpotCheck''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Gospotcheck Plans Pricing
  plan_count: 2
  slug: gospotcheck-plans-pricing
- name: Gospotcheck Price Estimates
  plan_count: 0
  slug: gospotcheck-price-estimates
random_paper: 2
rate_limits:
- limit_count: 3
  name: Gospotcheck Rate Limits
  slug: gospotcheck-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: GoSpotCheck API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: gospotcheck-rules
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 55.0
    developer_ergonomics: 33.9
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 54.9
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gospotcheck/gospotcheck-2026-07-25T220116.png
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
skill_count: 2
skills:
- name: Export mission and task response data
  slug: gospotcheck-export-mission-responses
- name: Sync places into GoSpotCheck
  slug: gospotcheck-sync-places
slug: gospotcheck
tags:
- Company
- Retail Execution
- Field Service Management
- Data Collection
- Surveys
- Merchandising
- Consumer Packaged Goods
- Mobile
website: https://gospotcheck.com
---
