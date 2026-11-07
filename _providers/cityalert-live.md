---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cityalert Live Agentic Access
  operation_count: 15
  slug: cityalert-live-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 1
apis:
- description: CityAlert.live API
  name: CityAlert.live API
  slug: cityalert-live-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: Machine-consumable interfaces
  name: CityAlert.live Agents API
  slug: cityalert-live-agents-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: User-submitted reports, votes and dashboards
  name: CityAlert.live Community API
  slug: cityalert-live-community-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: Syndication feeds
  name: CityAlert.live Feeds API
  slug: cityalert-live-feeds-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: Historical aggregates and year archives
  name: CityAlert.live History API
  slug: cityalert-live-history-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: Normalized live incident stream
  name: CityAlert.live Incidents API
  slug: cityalert-live-incidents-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: Region and source metadata
  name: CityAlert.live Meta API
  slug: cityalert-live-meta-api
- baseURL: https://cityalert.live
  baseurl_source: declared
  description: Regional safety news
  name: CityAlert.live News API
  slug: cityalert-live-news-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/cityalert-live/agentic-access/cityalert-live-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cityalert-live-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cityalert-live/plans/cityalert-live-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cityalert-live-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cityalert-live/rules/cityalert-live-rules.yml
  title: ''
  type: Spectral
  url: rules/cityalert-live-rules.yml
- group: design
  href: https://artifacts.apis.io/cityalert-live/vocabulary/cityalert-live-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cityalert-live-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cityalert-live/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/cityalert-live/changelog/cityalert-live-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cityalert-live-changelog.yml
- group: design
  href: https://artifacts.apis.io/cityalert-live/errors/cityalert-live-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cityalert-live-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cityalert-live/conformance/cityalert-live-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cityalert-live-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cityalert-live/llms/cityalert-live-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cityalert-live-llms.txt
- group: other
  href: https://artifacts.apis.io/cityalert-live/a2a/cityalert-live-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cityalert-live-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cityalert-live/mcp/cityalert-live-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cityalert-live-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cityalert-live/well-known/cityalert-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cityalert-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/cityalert-live/hosts/cityalert-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cityalert-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/cityalert-live/vendors/cityalert-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cityalert-live-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://cityalert.live/changelog
- group: auth
  href: https://artifacts.apis.io/cityalert-live/authentication/cityalert-live-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cityalert-live-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cityalert-live/security/cityalert-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cityalert-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cityalert.live/
created: '2026-11-03'
description: CityAlert.live provides a global incident map displaying live crime, fires, disasters, severe weather and community reports. It aggregates official police data, government feeds, meteorological services and satellite detections to deliver real‑time safety information for cities worldwide. Users can explore incidents, view historical trends, draw custom areas and share dashboards, all for free.
image: https://cityalert.live/opengraph-image?51b14ded727b30c9
layout: provider
mcp_servers:
- description: Remote MCP server at cityalert.live.
  name: CityAlert.live MCP Server
  slug: cityalert-live-mcp-yml
modified: '2026-11-03'
name: CityAlert.live
nav: Providers
network: true
overview: 'CityAlert.live publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Community API, Feeds API, and 5 more. Tagged areas include Safety, Mapping, Real-Time, Open Data, and Community.


  The CityAlert.live catalog on APIs.io includes 1 Spectral governance ruleset.


  CityAlert.live''s developer surface includes changelog, API reference, authentication, and 15 more developer resources.'
plans:
- name: Cityalert Live Plans Pricing
  plan_count: 8
  slug: cityalert-live-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: CityAlert.live API Rules
  rule_count: 55
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 3
  slug: cityalert-live-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 17.3
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cityalert Live Authentication
  slug: cityalert-live-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cityalert Live Domain Security
  slug: cityalert-live-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: cityalert-live-community-report
  slug: cityalert-live-community-report
slug: cityalert-live
tags:
- Safety
- Mapping
- Real-Time
- Open Data
- Community
website: https://cityalert.live/
---
