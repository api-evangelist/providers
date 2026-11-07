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
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: The authorizations API from OpenLattice — 1 operation(s) for authorizations.
  name: OpenLattice Authorizations API
  slug: openlattice-authorizations-api
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: API endpoints to reading and writing data.
  name: OpenLattice Data API
  slug: openlattice-data-api
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: API endpoints to the entity data model.
  name: OpenLattice Edm API
  slug: openlattice-edm-api
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: API endpoints related to organizations.
  name: OpenLattice Organizations API
  slug: openlattice-organizations-api
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: API endpoints for permissions for organisations, roles and users.
  name: OpenLattice Permissions API
  slug: openlattice-permissions-api
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: The principal API from OpenLattice — 5 operation(s) for principal.
  name: OpenLattice Principal API
  slug: openlattice-principal-api
- baseURL: https://api.openlattice.com
  baseurl_source: declared
  description: API endpoints to search data.
  name: OpenLattice Search API
  slug: openlattice-search-api
artifact_total: 23
collections:
- collection_type: open
  name: OpenLattice authorizations API
  slug: open-openlattice-authorizations-api
- collection_type: open
  name: OpenLattice authorizations data API
  slug: open-openlattice-data-api
- collection_type: open
  name: OpenLattice authorizations edm API
  slug: open-openlattice-edm-api
- collection_type: open
  name: OpenLattice authorizations organizations API
  slug: open-openlattice-organizations-api
- collection_type: open
  name: OpenLattice authorizations permissions API
  slug: open-openlattice-permissions-api
- collection_type: open
  name: OpenLattice authorizations principal API
  slug: open-openlattice-principal-api
- collection_type: open
  name: OpenLattice authorizations search API
  slug: open-openlattice-search-api
common:
- group: operate
  href: https://artifacts.apis.io/openlattice/rate-limits/openlattice-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openlattice-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: commercial
  href: https://artifacts.apis.io/openlattice/plans/openlattice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openlattice-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/openlattice/capabilities/openlattice-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openlattice-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/openlattice/overlays/openlattice-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openlattice-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/openlattice/security/openlattice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openlattice-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/openlattice/authentication/openlattice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openlattice-authentication.yml
- group: build
  href: https://artifacts.apis.io/openlattice/packages/openlattice-packages.yml
  title: ''
  type: Packages
  url: packages/openlattice-packages.yml
- group: build
  href: https://artifacts.apis.io/openlattice/packages/openlattice-packages.yml
  title: ''
  type: SDKs
  url: packages/openlattice-packages.yml
- group: design
  href: https://artifacts.apis.io/openlattice/components/openlattice-components.yml
  title: ''
  type: Components
  url: components/openlattice-components.yml
- group: design
  href: https://artifacts.apis.io/openlattice/conventions/openlattice-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openlattice-conventions.yml
- group: design
  href: https://artifacts.apis.io/openlattice/data-model/openlattice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openlattice-data-model.yml
- group: agent
  href: https://artifacts.apis.io/openlattice/mcp/openlattice-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/openlattice-mcp.yml
- group: agent
  href: https://artifacts.apis.io/openlattice/llms/openlattice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openlattice-llms.txt
- group: agent
  href: https://artifacts.apis.io/openlattice/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openlattice
- group: company
  title: ''
  type: Website
  url: https://github.com/openlattice
created: '2026-07-17'
description: OpenLattice was a data-integration and analytics platform built around an Entity Data Model (EDM) — a graph of entity types, property types, association types, and EntitySets — with a fine-grained ACL permissions model over organizations, roles, and principals. It was adopted by public-sector and criminal-justice programs such as reentry case management, community work programs, childcare, and courts. The company's hosted service and website (openlattice.com, api.openlattice.com) no longer resolve, but its OpenAPI 3.0 specification (91 operations), multi-language SDKs, and React UI kit remain published under the github.com/openlattice organization, from which this profile was enriched.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openlattice.png
layout: provider
modified: '2026-07-20'
name: OpenLattice
nav: Providers
network: true
overview: 'OpenLattice publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorizations API, Data API, Edm API, and 4 more. Tagged areas include Company, Data Integration, Entity Data Model, Public Sector, and Analytics.


  The OpenLattice catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenLattice''s developer surface includes pricing, authentication, and 15 more developer resources.'
plans:
- name: Openlattice Plans Pricing
  plan_count: 5
  slug: openlattice-plans-pricing
- name: Openlattice Price Estimates
  plan_count: 0
  slug: openlattice-price-estimates
random_paper: 0
rate_limits:
- limit_count: 0
  name: Openlattice Rate Limits
  slug: openlattice-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: OpenLattice API Rules
  rule_count: 55
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 5
  slug: openlattice-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 39.8
    developer_ergonomics: 28.0
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 33.4
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/openlattice/openlattice-2026-08-07T190610.png
security:
- kind: authentication
  name: Openlattice Authentication
  slug: openlattice-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Openlattice Domain Security
  slug: openlattice-domain-security
  summary_line: no transport/DNS hardening detected
skill_count: 3
skills:
- name: explore-entity-data-model
  slug: explore-entity-data-model
- name: manage-organization-permissions
  slug: manage-organization-permissions
- name: search-entity-neighbors
  slug: search-entity-neighbors
slug: openlattice
tags:
- Company
- Data Integration
- Entity Data Model
- Public Sector
- Analytics
- Graph
- Criminal Justice
---
