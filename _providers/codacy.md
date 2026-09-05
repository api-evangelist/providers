---
access_model:
  confidence: medium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Codacy Agentic Access
  operation_count: 18
  slug: codacy-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Authenticated user account and API token operations.
  name: Codacy Account API
  slug: codacy-account-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Code coverage for pull requests and files.
  name: Codacy Coverage API
  slug: codacy-coverage-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Static analysis issues for a repository.
  name: Codacy Issues API
  slug: codacy-issues-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Git provider organizations the account belongs to.
  name: Codacy Organizations API
  slug: codacy-organizations-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Pull request analysis, files, issues, and AI review.
  name: Codacy Pull Requests API
  slug: codacy-pull-requests-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Quality and security gating settings for commits and pull requests.
  name: Codacy Quality Settings API
  slug: codacy-quality-settings-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Repository management and analysis state.
  name: Codacy Repositories API
  slug: codacy-repositories-api
- baseURL: https://api.codacy.com/api/v3
  baseurl_source: declared
  description: Repository SSH key administration.
  name: Codacy Security API
  slug: codacy-security-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Codacy Account API
  slug: open-codacy-account-api
- collection_type: open
  name: Codacy Account Coverage API
  slug: open-codacy-coverage-api
- collection_type: open
  name: Codacy Account Issues API
  slug: open-codacy-issues-api
- collection_type: open
  name: Codacy Account Organizations API
  slug: open-codacy-organizations-api
- collection_type: open
  name: Codacy Account Pull Requests API
  slug: open-codacy-pull-requests-api
- collection_type: open
  name: Codacy Account Quality Settings API
  slug: open-codacy-quality-settings-api
- collection_type: open
  name: Codacy Account Repositories API
  slug: open-codacy-repositories-api
- collection_type: open
  name: Codacy Account Security API
  slug: open-codacy-security-api
- collection_type: open
  name: Codacy API
  slug: open-codacy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codacy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codacy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codacy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codacy
- group: company
  title: ''
  type: Website
  url: https://www.codacy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codacy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/codacy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codacy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codacy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.codacy.com/rss.xml
created: '2026-06-21'
description: Codacy is an automated code quality and security platform that analyzes commits and pull requests across 49+ languages, surfacing issues, coverage, and security findings. The Codacy API v3 lets teams manage organizations, repositories, issues, pull requests, coverage, security, and quality settings programmatically.
finops:
- name: Codacy Finops
  service_category: Developer Tools
  slug: codacy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codacy.png
layout: provider
modified: '2026-06-21'
name: Codacy
nav: Providers
network: true
overview: 'Codacy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Coverage API, Issues API, and 5 more. Tagged areas include Code Quality, Static Analysis, Security, Code Coverage, and DevOps.


  Codacy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Codacy Plans Pricing
  plan_count: 3
  slug: codacy-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Codacy Rate Limits
  slug: codacy-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codacy/refs/heads/main/screenshots/codacy-2026-07-25T205855.png
security:
- kind: authentication
  name: Codacy Authentication
  slug: codacy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codacy Domain Security
  slug: codacy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codacy
tags:
- Code Quality
- Static Analysis
- Security
- Code Coverage
- DevOps
website: https://www.codacy.com
---
