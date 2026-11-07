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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 71
  human_in_the_loop: 2
  name: Lakefs Agentic Access
  operation_count: 134
  slug: lakefs-agentic-access
  summary_line: 134 operations · 71 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: /api/v1
  baseurl_source: spec
  description: The actions API from lakeFS — 4 operation(s) for actions.
  name: lakeFS Actions API
  slug: lakefs-actions-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The auth API from lakeFS — 23 operation(s) for auth.
  name: lakeFS Auth API
  slug: lakefs-auth-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The branches API from lakeFS — 5 operation(s) for branches.
  name: lakeFS Branches API
  slug: lakefs-branches-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The commits API from lakeFS — 2 operation(s) for commits.
  name: lakeFS Commits API
  slug: lakefs-commits-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The config API from lakeFS — 1 operation(s) for config.
  name: lakeFS Config API
  slug: lakefs-config-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The experimental API from lakeFS — 14 operation(s) for experimental.
  name: lakeFS Experimental API
  slug: lakefs-experimental-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The external API from lakeFS — 4 operation(s) for external.
  name: lakeFS External API
  slug: lakefs-external-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The import API from lakeFS — 1 operation(s) for import.
  name: lakeFS Import API
  slug: lakefs-import-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The internal API from lakeFS — 24 operation(s) for internal.
  name: lakeFS Internal API
  slug: lakefs-internal-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The metadata API from lakeFS — 2 operation(s) for metadata.
  name: lakeFS Metadata API
  slug: lakefs-metadata-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The objects API from lakeFS — 8 operation(s) for objects.
  name: lakeFS Objects API
  slug: lakefs-objects-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The pulls API from lakeFS — 3 operation(s) for pulls.
  name: lakeFS Pulls API
  slug: lakefs-pulls-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The refs API from lakeFS — 3 operation(s) for refs.
  name: lakeFS Refs API
  slug: lakefs-refs-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The repositories API from lakeFS — 7 operation(s) for repositories.
  name: lakeFS Repositories API
  slug: lakefs-repositories-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The staging API from lakeFS — 1 operation(s) for staging.
  name: lakeFS Staging API
  slug: lakefs-staging-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The tags API from lakeFS — 2 operation(s) for tags.
  name: lakeFS Tags API
  slug: lakefs-tags-api
- baseURL: /api/v1
  baseurl_source: spec
  description: The Health Check API from lakeFS — 1 operation(s) for health check.
  name: lakeFS Health Check API
  slug: lakefs-health-check-api
artifact_total: 42
collections:
- collection_type: open
  name: lakeFS actions API
  slug: open-lakefs-actions-api
- collection_type: open
  name: lakeFS actions auth API
  slug: open-lakefs-auth-api
- collection_type: open
  name: lakeFS actions branches API
  slug: open-lakefs-branches-api
- collection_type: open
  name: lakeFS actions commits API
  slug: open-lakefs-commits-api
- collection_type: open
  name: lakeFS actions config API
  slug: open-lakefs-config-api
- collection_type: open
  name: lakeFS actions experimental API
  slug: open-lakefs-experimental-api
- collection_type: open
  name: lakeFS actions external API
  slug: open-lakefs-external-api
- collection_type: open
  name: lakeFS actions healthCheck API
  slug: open-lakefs-healthcheck-api
- collection_type: open
  name: lakeFS actions import API
  slug: open-lakefs-import-api
- collection_type: open
  name: lakeFS actions internal API
  slug: open-lakefs-internal-api
- collection_type: open
  name: lakeFS actions metadata API
  slug: open-lakefs-metadata-api
- collection_type: open
  name: lakeFS actions objects API
  slug: open-lakefs-objects-api
- collection_type: open
  name: lakeFS actions pulls API
  slug: open-lakefs-pulls-api
- collection_type: open
  name: lakeFS actions refs API
  slug: open-lakefs-refs-api
- collection_type: open
  name: lakeFS actions repositories API
  slug: open-lakefs-repositories-api
- collection_type: open
  name: lakeFS actions staging API
  slug: open-lakefs-staging-api
- collection_type: open
  name: lakeFS actions tags API
  slug: open-lakefs-tags-api
- collection_type: open
  name: lakeFS API
  slug: open-lakefs
common:
- group: commercial
  href: https://artifacts.apis.io/lakefs/plans/lakefs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lakefs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lakefs/rate-limits/lakefs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lakefs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lakefs/finops/lakefs-finops.yml
  title: ''
  type: FinOps
  url: finops/lakefs-finops.yml
- group: other
  href: https://artifacts.apis.io/lakefs/capabilities/lakefs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lakefs-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lakefs/agentic-access/lakefs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lakefs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lakefs/security/lakefs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lakefs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lakefs/authentication/lakefs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lakefs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lakefs-treeverse
- group: company
  title: ''
  type: Website
  url: https://lakefs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakefs.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/treeverse/lakeFS
- group: agent
  title: ''
  type: LlmsText
  url: https://lakefs.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lakefs.io/feed
created: '2025-02-08'
description: Manage your data as code using Git-like operations and achieve reproducible, high-quality data pipelines. Start locally, run on-prem or in the cloud.
finops:
- has_sources: false
  method: generated
  name: Lakefs Finops
  primary_unit: request
  service_category: API
  slug: lakefs-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lakefs.png
layout: provider
modified: '2026-05-19'
name: lakeFS
nav: Providers
network: true
overview: 'lakeFS publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Auth API, Branches API, and 14 more. Tagged areas include Data Version Control, Data Lake, Git-like, and Open Source.


  The lakeFS catalog on APIs.io includes 1 Spectral governance ruleset.


  lakeFS''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Lakefs Plans Pricing
  plan_count: 3
  slug: lakefs-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Lakefs Rate Limits
  slug: lakefs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: lakeFS API Rules
  rule_count: 59
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 15
  slug: lakefs-rules
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.5
    catalog_earned_first_party: 0.0
    catalog_gap: 82.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 43.7
    developer_ergonomics: 23.8
    discoverability: 46.4
    operational_transparency: 10.5
  previous_composite: 23.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
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
screenshot: https://apis.io/screenshots/lakefs/lakefs-2026-06-20T184245.png
security:
- kind: authentication
  name: Lakefs Authentication
  slug: lakefs-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Lakefs Domain Security
  slug: lakefs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lakefs
tags:
- Data Version Control
- Data Lake
- Git-like
- Open Source
website: https://lakefs.io/
---
