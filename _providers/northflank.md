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
    agent_skills: unknown
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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Northflank Agentic Access
  operation_count: 13
  slug: northflank-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 4
apis:
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Jobs API from Northflank — 2 operation(s) for jobs.
  name: Northflank Jobs API
  slug: northflank-jobs-api
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Projects API from Northflank — 1 operation(s) for projects.
  name: Northflank Projects API
  slug: northflank-projects-api
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Services API from Northflank — 2 operation(s) for services.
  name: Northflank Services API
  slug: northflank-services-api
- baseURL: https://api.northflank.com/v1
  baseurl_source: declared
  description: The Add Ons API from Northflank — 2 operation(s) for add ons.
  name: Northflank Add Ons API
  slug: northflank-add-ons-api
artifact_total: 19
collections:
- collection_type: open
  name: Northflank Addons API
  slug: open-northflank-addons-api
- collection_type: open
  name: Northflank Addons Jobs API
  slug: open-northflank-jobs-api
- collection_type: open
  name: Northflank Addons Projects API
  slug: open-northflank-projects-api
- collection_type: open
  name: Northflank Addons Services API
  slug: open-northflank-services-api
- collection_type: open
  name: Northflank API
  slug: open-northflank
common:
- group: commercial
  href: https://artifacts.apis.io/northflank/plans/northflank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/northflank-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/northflank/rate-limits/northflank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/northflank-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/northflank/finops/northflank-finops.yml
  title: ''
  type: FinOps
  url: finops/northflank-finops.yml
- group: agent
  href: https://artifacts.apis.io/northflank/agentic-access/northflank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/northflank-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/northflank/security/northflank-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/northflank-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/northflank/security/northflank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/northflank-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/northflank/security/northflank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/northflank-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/northflank/authentication/northflank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/northflank-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://northflank.com/blog/rss/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northflank
- group: company
  title: ''
  type: Website
  url: https://northflank.com
- group: docs
  title: ''
  type: Documentation
  url: https://northflank.com/docs
- group: docs
  title: ''
  type: API Documentation
  url: https://northflank.com/docs/v1/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/northflank
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/northflank/skills
created: '2026-03-27'
description: Northflank is an internal developer platform providing self-service deployment, scaling, and management of applications, databases, and jobs across cloud providers.
finops:
- has_sources: false
  method: generated
  name: Northflank Finops
  primary_unit: request
  service_category: API
  slug: northflank-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northflank.png
layout: provider
modified: '2026-05-19'
name: Northflank
nav: Providers
network: true
overview: 'Northflank is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Jobs API, Projects API, Services API, and 1 more. Tagged areas include Cloud Deployment, Developer Experience, Internal Developer Platform, and Platform Engineering.


  The Northflank catalog on APIs.io includes 1 Spectral governance ruleset.


  Northflank''s developer surface includes authentication, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Northflank Plans Pricing
  plan_count: 3
  slug: northflank-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Northflank Rate Limits
  slug: northflank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Northflank API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: northflank-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 42.9
    developer_ergonomics: 37.4
    discoverability: 53.6
    operational_transparency: 21.1
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/northflank/northflank-2026-06-20T190419.png
security:
- kind: authentication
  name: Northflank Authentication
  slug: northflank-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Northflank Domain Security
  slug: northflank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Northflank Vulnerability Disclosure
  slug: northflank-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Northflank Trust Center
  slug: northflank-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
skill_count: 1
skills:
- name: northflank
  slug: northflank
slug: northflank
tags:
- Cloud Deployment
- Developer Experience
- Internal Developer Platform
- Platform Engineering
website: https://northflank.com
---
