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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Hyperping Agentic Access
  operation_count: 35
  slug: hyperping-agentic-access
  summary_line: 35 operations · 22 acting
api_count: 2
apis:
- baseURL: https://api.hyperping.io/v1
  baseurl_source: declared
  description: Status page incident lifecycle and updates.
  name: Hyperping Incidents API
  slug: hyperping-incidents-api
- baseURL: https://api.hyperping.io/v1
  baseurl_source: declared
  description: Scheduled maintenance windows.
  name: Hyperping Maintenance API
  slug: hyperping-maintenance-api
- baseURL: https://api.hyperping.io/v1
  baseurl_source: declared
  description: Create, retrieve, update, and delete uptime monitors.
  name: Hyperping Monitors API
  slug: hyperping-monitors-api
- baseURL: https://api.hyperping.io/v1
  baseurl_source: declared
  description: On-call outage acknowledgement, resolution, and escalation.
  name: Hyperping Outages API
  slug: hyperping-outages-api
- baseURL: https://api.hyperping.io/v1
  baseurl_source: declared
  description: Uptime, SLA, and MTTR reporting for monitors.
  name: Hyperping Reports API
  slug: hyperping-reports-api
- baseURL: https://api.hyperping.io/v1
  baseurl_source: declared
  description: Public machine-readable status feed for a status page.
  name: Hyperping Status Pages API
  slug: hyperping-status-pages-api
- baseURL: https://api.hyperping.io
  baseurl_source: declared
  description: Cron job and scheduled task monitoring
  name: Hyperping Health Checks API
  slug: hyperping-health-checks-api
artifact_total: 22
collections:
- collection_type: open
  name: Hyperping Healthchecks API
  slug: open-hyperping-healthchecks-api
- collection_type: open
  name: Hyperping Healthchecks Incidents API
  slug: open-hyperping-incidents-api
- collection_type: open
  name: Hyperping Healthchecks Maintenance API
  slug: open-hyperping-maintenance-api
- collection_type: open
  name: Hyperping Healthchecks Monitors API
  slug: open-hyperping-monitors-api
- collection_type: open
  name: Hyperping Healthchecks Outages API
  slug: open-hyperping-outages-api
- collection_type: open
  name: Hyperping Healthchecks Reports API
  slug: open-hyperping-reports-api
- collection_type: open
  name: Hyperping Healthchecks Status Pages API
  slug: open-hyperping-status-pages-api
- collection_type: open
  name: Hyperping API
  slug: open-hyperping
common:
- group: other
  href: https://artifacts.apis.io/hyperping/capabilities/hyperping-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hyperping-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/hyperping/vendor-facets/hyperping-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/hyperping-vendor-facets.yml
- group: agent
  href: https://artifacts.apis.io/hyperping/agentic-access/hyperping-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperping-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hyperping/security/hyperping-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hyperping-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hyperping/authentication/hyperping-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hyperping-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyperping
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperping
- group: company
  title: ''
  type: Website
  url: https://hyperping.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hyperping.com/docs
- group: commercial
  href: https://artifacts.apis.io/hyperping/plans/hyperping-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hyperping-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hyperping/rate-limits/hyperping-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hyperping-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hyperping/finops/hyperping-finops.yml
  title: ''
  type: FinOps
  url: finops/hyperping-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hyperping.com/blog
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/hyperping/hyperping-go/blob/7be4590be32b4c81669d41d45bfd335f5ab828b0/.spectral.yaml
created: '2026-06-21'
description: Hyperping is an uptime monitoring and status page platform. Its REST API lets teams programmatically manage HTTP, ping, port, keyword, DNS, and browser monitors, run scheduled-task healthchecks, operate public status pages through incidents and maintenance windows, manage on-call outages, and pull uptime and SLA reporting.
finops:
- has_sources: true
  method: generated
  name: Hyperping Finops
  primary_unit: ''
  service_category: Management and Governance
  slug: hyperping-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperping.png
layout: provider
modified: '2026-06-21'
name: Hyperping
nav: Providers
network: true
overview: 'Hyperping publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Incidents API, Maintenance API, Monitors API, and 4 more. Tagged areas include Uptime Monitoring, Status Pages, Incident Management, Observability, and On-Call.


  The Hyperping catalog on APIs.io includes 1 Spectral governance ruleset.


  Hyperping''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Hyperping Plans Pricing
  plan_count: 5
  slug: hyperping-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Hyperping Rate Limits
  slug: hyperping-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Hyperping — hyperping go rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: hyperping-hyperping-go-spectral-rules
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.0
    catalog_earned_first_party: 5.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 7.9
    contract_governance: 15.2
    contract_quality: 46.8
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hyperping/hyperping-2026-07-25T221925.png
security:
- kind: authentication
  name: Hyperping Authentication
  slug: hyperping-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hyperping Domain Security
  slug: hyperping-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hyperping
tags:
- Uptime Monitoring
- Status Pages
- Incident Management
- Observability
- On-Call
website: https://hyperping.com/
---
