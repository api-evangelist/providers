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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Swarmia Agentic Access
  operation_count: 12
  slug: swarmia-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Ingestion of usage data from external AI assistant tools.
  name: Swarmia Additional AI integrations API
  slug: swarmia-additional-ai-integrations-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Machine-readable versions of major reports found in the Swarmia app.
  name: Swarmia Built-in reports API
  slug: swarmia-built-in-reports-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Saved custom reports created in the Swarmia explore view.
  name: Swarmia Custom reports API
  slug: swarmia-custom-reports-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Deployment and fix-deployment event ingestion for delivery and DORA metrics.
  name: Swarmia Deployments API
  slug: swarmia-deployments-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Programmatic management of teams and memberships.
  name: Swarmia Team management API
  slug: swarmia-team-management-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Create, read, update, and delete employee time-off periods.
  name: Swarmia Time off API
  slug: swarmia-time-off-api
artifact_total: 21
collections:
- collection_type: open
  name: Swarmia Additional AI integrations API
  slug: open-swarmia-additional-ai-integrations-api
- collection_type: open
  name: Swarmia Additional AI integrations Built-in reports API
  slug: open-swarmia-built-in-reports-api
- collection_type: open
  name: Swarmia Additional AI integrations Custom reports API
  slug: open-swarmia-custom-reports-api
- collection_type: open
  name: Swarmia Additional AI integrations Deployments API
  slug: open-swarmia-deployments-api
- collection_type: open
  name: Swarmia Additional AI integrations Team management API
  slug: open-swarmia-team-management-api
- collection_type: open
  name: Swarmia Additional AI integrations Time off API
  slug: open-swarmia-time-off-api
- collection_type: open
  name: Swarmia API
  slug: open-swarmia
common:
- group: other
  href: https://artifacts.apis.io/swarmia/capabilities/swarmia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/swarmia-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/swarmia/agentic-access/swarmia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/swarmia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/swarmia/security/swarmia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/swarmia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/swarmia/security/swarmia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swarmia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/swarmia/authentication/swarmia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/swarmia-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swarmia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swarmia
- group: company
  title: ''
  type: Website
  url: https://www.swarmia.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.swarmia.com
- group: commercial
  href: https://artifacts.apis.io/swarmia/plans/swarmia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/swarmia-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/swarmia/rate-limits/swarmia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/swarmia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/swarmia/finops/swarmia-finops.yml
  title: ''
  type: FinOps
  url: finops/swarmia-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.swarmia.com/rss.xml
created: '2026-06-21'
description: Swarmia is an engineering-effectiveness analytics platform that combines software delivery metrics (DORA), developer experience, investment balance, and AI adoption insights. Its REST API lets teams export built-in and custom reports, ingest deployment and events data, manage teams and memberships, and record time off, authenticated with Bearer API tokens.
finops:
- has_sources: true
  method: generated
  name: Swarmia Finops
  primary_unit: ''
  service_category: Developer Tools
  slug: swarmia-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swarmia.png
layout: provider
modified: '2026-06-21'
name: Swarmia
nav: Providers
network: true
overview: 'Swarmia publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Additional AI integrations API, Built-in reports API, Custom reports API, and 3 more. Tagged areas include Engineering Effectiveness, Developer Productivity, DORA, Software Delivery, and Analytics.


  The Swarmia catalog on APIs.io includes 1 Spectral governance ruleset.


  Swarmia''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Swarmia Plans Pricing
  plan_count: 4
  slug: swarmia-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Swarmia Rate Limits
  slug: swarmia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Swarmia API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: swarmia-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 51.0
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/swarmia/swarmia-2026-09-02T161344.png
security:
- kind: authentication
  name: Swarmia Authentication
  slug: swarmia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Swarmia Domain Security
  slug: swarmia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Swarmia Vulnerability Disclosure
  slug: swarmia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swarmia
tags:
- Engineering Effectiveness
- Developer Productivity
- DORA
- Software Delivery
- Analytics
website: https://www.swarmia.com
---
