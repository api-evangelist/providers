---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Themuse Agentic Access
  operation_count: 4
  slug: themuse-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Employer company profiles that back the job listings.
  name: The Muse Companies API
  slug: themuse-companies-api
- description: Live job openings, searchable by category, level, company, and location.
  name: The Muse Jobs API
  slug: themuse-jobs-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: Plans
  url: plans/themuse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/themuse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/themuse-finops.yml
- group: auth
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
- name: Themuse Finops
  service_category: Careers and Recruiting Data
  slug: themuse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/themuse.png
layout: provider
modified: '2026-08-08'
name: The Muse
nav: Providers
network: true
overview: 'The Muse publishes 2 APIs on the [APIs.io](https://apis.io/) network: Companies API and Jobs API. Tagged areas include Job Openings, Job, Careers, Recruiting, and Employment.


  The Muse''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Themuse Plans Pricing
  plan_count: 3
  slug: themuse-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Themuse Rate Limits
  slug: themuse-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/themuse/refs/heads/main/screenshots/themuse-2026-06-20T195325.png
security:
- kind: domain-security
  name: Themuse Domain Security
  slug: themuse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: themuse
tags:
- Job Openings
- Job
- Careers
- Recruiting
- Employment
- Company Profiles
- Job Search
- Hiring
- HR Tech
website: https://www.themuse.com
---
