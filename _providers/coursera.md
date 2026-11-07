---
access_model:
  confidence: low
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coursera Agentic Access
  operation_count: 4
  slug: coursera-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Public REST API for browsing Coursera's catalog of courses, specializations, instructors, partners, and categories. Verified live at api.coursera.org/api/courses.v1 with 21,000+ courses.
  name: Coursera Catalog API
  slug: catalog-api
- description: API for affiliate marketing partners to retrieve catalog data and tracking links.
  name: Coursera Affiliate API
  slug: affiliate-api
- baseURL: https://api.coursera.org
  baseurl_source: declared
  description: Public catalog browsing
  name: Coursera Catalog API
  slug: coursera-catalog-api
artifact_total: 11
collections:
- collection_type: open
  name: Coursera Catalog API
  slug: open-coursera-catalog-api
- collection_type: open
  name: Coursera Catalog API
  slug: open-coursera
common:
- group: other
  href: https://artifacts.apis.io/coursera/capabilities/coursera-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coursera-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/coursera/agentic-access/coursera-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coursera-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coursera/security/coursera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coursera-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coursera
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coursera
- group: company
  title: ''
  type: Website
  url: https://www.coursera.org/
- group: other
  title: ''
  type: Developer
  url: https://building.coursera.org/
- group: commercial
  href: https://artifacts.apis.io/coursera/plans/coursera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coursera-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coursera/rate-limits/coursera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coursera-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coursera/finops/coursera-finops.yml
  title: ''
  type: FinOps
  url: finops/coursera-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.coursera.org/feed/
created: '2026-05-08'
description: Coursera is a global online learning platform offering courses, specializations, professional certificates, and degrees. The Catalog API provides public, read-only access to courses, instructors, partners, and categories; the Affiliate API supports partner programs.
finops:
- has_sources: true
  method: generated
  name: Coursera Finops
  primary_unit: ''
  service_category: Education & Training
  slug: coursera-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coursera.png
layout: provider
modified: '2026-05-08'
name: Coursera
nav: Providers
network: true
overview: 'Coursera publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, and 2 more. Tagged areas include EdTech, E-Learning, Catalog, and MOOC.


  The Coursera catalog on APIs.io includes 1 Spectral governance ruleset.


  Coursera''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Coursera Plans Pricing
  plan_count: 2
  slug: coursera-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Coursera Rate Limits
  slug: coursera-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Coursera API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: coursera-rules
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.5
    catalog_earned_first_party: 0.0
    catalog_gap: 79.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 30.8
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 16.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 25.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/coursera/coursera-2026-06-20T175124.png
security:
- kind: domain-security
  name: Coursera Domain Security
  slug: coursera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coursera
tags:
- EdTech
- E-Learning
- Catalog
- MOOC
website: https://www.coursera.org/
---
