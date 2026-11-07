---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Themuse Agentic Access
  operation_count: 4
  slug: themuse-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://www.themuse.com/api/public
  baseurl_source: declared
  description: Employer company profiles that back the job listings.
  name: The Muse Companies API
  slug: themuse-companies-api
- baseURL: https://www.themuse.com/api/public
  baseurl_source: declared
  description: Live job openings, searchable by category, level, company, and location.
  name: The Muse Jobs API
  slug: themuse-jobs-api
artifact_total: 11
collections:
- collection_type: open
  name: The Muse Public Companies API
  slug: open-themuse-companies-api
- collection_type: open
  name: The Muse Public Companies Jobs API
  slug: open-themuse-jobs-api
- collection_type: open
  name: The Muse Public API
  slug: open-themuse
common:
- group: agent
  href: https://artifacts.apis.io/themuse/agentic-access/themuse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/themuse-agentic-access.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-muse
- group: company
  title: ''
  type: Website
  url: https://www.themuse.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.themuse.com/developers/api/v2
- group: commercial
  href: https://artifacts.apis.io/themuse/plans/themuse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/themuse-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/themuse/rate-limits/themuse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/themuse-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/themuse/finops/themuse-finops.yml
  title: ''
  type: FinOps
  url: finops/themuse-finops.yml
- group: auth
  href: https://artifacts.apis.io/themuse/security/themuse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/themuse-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-07-11'
description: The Muse is a careers and company-profiles platform that helps people find jobs at companies whose values match their own. Its free, documented public REST API (v2) exposes hundreds of thousands of live job openings - searchable by category, experience level, company, and location - alongside rich employer company profiles (industry, size, locations, and behind-the-scenes content). An optional api_key raises rate limits. This makes The Muse a strong source for "job openings", jobs, careers, and recruiting use cases and for building job boards, career sites, and employer-branding integrations.
finops:
- has_sources: true
  method: generated
  name: Themuse Finops
  primary_unit: ''
  service_category: Careers and Recruiting Data
  slug: themuse-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/themuse.png
layout: provider
modified: '2026-08-08'
name: The Muse
nav: Providers
network: true
overview: 'The Muse publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Companies API and Jobs API. Tagged areas include Job Postings, Job, Careers, Recruiting, and Employment.


  The The Muse catalog on APIs.io includes 1 Spectral governance ruleset.


  The Muse''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Themuse Plans Pricing
  plan_count: 3
  slug: themuse-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Themuse Rate Limits
  slug: themuse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: The Muse API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: themuse-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 50.2
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 25.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/themuse/themuse-2026-06-20T195325.png
security:
- kind: domain-security
  name: Themuse Domain Security
  slug: themuse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: themuse
tags:
- Job Postings
- Job
- Careers
- Recruiting
- Employment
- Company Profiles
- Job Search
- Hiring
- Human Resources
website: https://www.themuse.com
---
