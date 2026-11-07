---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Findlocal Agentic Access
  operation_count: 3
  slug: findlocal-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: Search upcoming events and look up a single event across 85 US and UK metros.
  name: FindLocal Events API
  slug: findlocal-events-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Venues API from FindLocal — 1 operation(s) for venues.
  name: FindLocal Venues API
  slug: findlocal-venues-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/findlocal/agentic-access/findlocal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/findlocal-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/findlocal/finops/findlocal-finops.yml
  title: ''
  type: FinOps
  url: finops/findlocal-finops.yml
- group: operate
  href: https://artifacts.apis.io/findlocal/rate-limits/findlocal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/findlocal-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/findlocal/json-ld/findlocal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/findlocal-context.jsonld
- group: design
  href: https://artifacts.apis.io/findlocal/vocabulary/findlocal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/findlocal-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/findlocal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/findlocal/data-model/findlocal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/findlocal-data-model.yml
- group: design
  href: https://artifacts.apis.io/findlocal/components/findlocal-components.yml
  title: ''
  type: Components
  url: components/findlocal-components.yml
- group: operate
  href: https://artifacts.apis.io/findlocal/changelog/findlocal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/findlocal-changelog.yml
- group: start
  href: https://artifacts.apis.io/findlocal/sandbox/findlocal-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/findlocal-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/findlocal/lifecycle/findlocal-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/findlocal-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/findlocal/lifecycle/findlocal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/findlocal-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/findlocal/errors/findlocal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/findlocal-problem-types.yml
- group: other
  href: https://artifacts.apis.io/findlocal/overlays/findlocal-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/findlocal-events-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/findlocal/mcp/findlocal-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/findlocal-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/findlocal/well-known/findlocal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/findlocal-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/findlocal/plans/findlocal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/findlocal-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/findlocal/rules/findlocal-rules.yml
  title: ''
  type: Spectral
  url: rules/findlocal-rules.yml
- group: design
  href: https://artifacts.apis.io/findlocal/conventions/findlocal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/findlocal-conventions.yml
- group: auth
  href: https://artifacts.apis.io/findlocal/authentication/findlocal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/findlocal-authentication.yml
- group: design
  href: https://artifacts.apis.io/findlocal/conformance/findlocal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findlocal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/findlocal/llms/findlocal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findlocal-llms.txt
- group: other
  href: https://artifacts.apis.io/findlocal/hosts/findlocal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/findlocal-hosts.yml
- group: other
  href: https://artifacts.apis.io/findlocal/vendors/findlocal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/findlocal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://findlocal.community/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://findlocal.community/privacy
- group: company
  title: ''
  type: Blog
  url: https://findlocal.community/blog
- group: auth
  href: https://artifacts.apis.io/findlocal/security/findlocal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findlocal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://findlocal.community/
- group: docs
  title: ''
  type: Documentation
  url: https://findlocal.community/docs
- group: docs
  title: ''
  type: APIReference
  url: https://findlocal.community/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://findlocal.community/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://findlocal.community/pricing
- group: start
  title: ''
  type: SignUp
  url: https://findlocal.community/signup
- group: start
  title: ''
  type: Login
  url: https://findlocal.community/login
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.findlocal.community/mcp
created: '2026-09-25'
description: 'FindLocal is a hyper-local events API covering 85 metros across the US and UK (84 US metros plus London), with 86,000+ upcoming events from 15,000+ venues: concerts, comedy, theater, author readings, film, talks, classes and community events. Data comes from venues'' own calendars and is updated daily, available through a JSON REST API, an MCP server and free embeddable widgets.'
finops:
- has_sources: true
  method: derived
  name: Findlocal Finops
  primary_unit: ''
  service_category: ''
  slug: findlocal-finops
  template: true
image: https://findlocal.community/og-default.png
json_schemas:
- name: Event
  property_count: 27
  slug: findlocal-event
- name: Venue
  property_count: 13
  slug: findlocal-venue
jsonld:
- class_count: 3
  name: Findlocal Context
  property_count: 37
  slug: findlocal-context
layout: provider
mcp_servers:
- description: 'FindLocal remote MCP server (same API key as the REST API). Docs: https://findlocal.community/mcp'
  name: FindLocal MCP Server
  slug: mcp
modified: '2026-11-04'
name: FindLocal
nav: Providers
network: true
overview: 'FindLocal publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Events API and Venues API. Tagged areas include Event, Hyperlocal, Community, Data, and Open Data.


  The FindLocal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FindLocal''s developer surface includes changelog, sandbox, authentication, engineering blog, documentation, API reference, getting-started guide, and 29 more developer resources.'
plans:
- name: Findlocal Plans Pricing
  plan_count: 4
  slug: findlocal-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Findlocal Rate Limits
  slug: findlocal-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: FindLocal API Rules
  rule_count: 51
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 2
  slug: findlocal-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 80.2
    catalog_earned_first_party: 24.0
    catalog_gap: 34.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.6
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 65.6
    developer_ergonomics: 36.3
    discoverability: 73.2
    operational_transparency: 55.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/findlocal/findlocal-2026-10-11T104451.png
security:
- kind: authentication
  name: Findlocal Authentication
  slug: findlocal-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Findlocal Domain Security
  slug: findlocal-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: discover-venues-in-a-metro
  slug: findlocal-discover-venues-in-a-metro
- name: find-events-in-a-metro
  slug: findlocal-find-events-in-a-metro
slug: findlocal
tags:
- Event
- Hyperlocal
- Community
- Data
- Open Data
website: https://findlocal.community/
---
