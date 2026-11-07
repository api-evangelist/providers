---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Home Depot Agentic Access
  operation_count: 1
  slug: home-depot-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.homedepot.com
  baseurl_source: declared
  description: Retail operations
  name: home-depot Retail API
  slug: home-depot-retail-api
artifact_total: 10
collections:
- collection_type: open
  name: Home Depot API
  slug: open-home-depot-home-depot-api
- collection_type: open
  name: Home Depot Retail API
  slug: open-home-depot-retail-api
common:
- group: commercial
  href: https://artifacts.apis.io/home-depot/plans/home-depot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/home-depot-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/home-depot/rate-limits/home-depot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/home-depot-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/home-depot/finops/home-depot-finops.yml
  title: ''
  type: FinOps
  url: finops/home-depot-finops.yml
- group: company
  title: ''
  type: Website
  url: https://homedepot.com
- group: agent
  href: https://artifacts.apis.io/home-depot/agentic-access/home-depot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/home-depot-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/home-depot/security/home-depot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/home-depot-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/home-depot/authentication/home-depot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/home-depot-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/homedepot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-home-depot
description: The Home Depot is the world's largest home improvement retailer, offering tools, construction products, appliances, and services through stores, websites, and apps in the United States, Canada, and Mexico.
finops:
- has_sources: true
  method: generated
  name: Home Depot Finops
  primary_unit: varies
  service_category: Retail / E-Commerce
  slug: home-depot-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/home-depot.png
layout: provider
modified: '2026-09-16'
name: The Home Depot
nav: Providers
network: true
overview: 'The Home Depot publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: home-depot Retail API. Tagged areas include Fortune 100.


  The The Home Depot catalog on APIs.io includes 1 Spectral governance ruleset.


  The Home Depot''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Home Depot Plans Pricing
  plan_count: 1
  slug: home-depot-plans-pricing
press:
- date: ''
  title: The Home Depot Launches AI-Powered Material Lists to ...
  url: https://corporate.homedepot.com/news/company/home-depot-launches-ai-powered-material-lists-help-pros-save-time-building-complete
- date: ''
  title: 'Home Depot Uses AI Agents: 10 Ways to Use AI [In-Depth ...'
  url: https://www.klover.ai/home-depot-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/
- date: ''
  title: The Home Depot and Google Cloud Launch Agentic AI ...
  url: https://corporate.homedepot.com/news/partnerships/home-depot-and-google-cloud-launch-agentic-ai-tools-help-customers-and-associates
- date: ''
  title: The Home Depot Delivers Customer Support Four Times ...
  url: https://www.prnewswire.com/news-releases/the-home-depot-delivers-customer-support-four-times-faster-using-google-clouds-gemini-enterprise-for-customer-experience-302749232.html
- date: ''
  title: The Home Depot Introduces Magic Apron, a Suite of ...
  url: https://ir.homedepot.com/news-releases/2025/03-06-2025-130241718
random_paper: 2
rate_limits:
- limit_count: 1
  name: Home Depot Rate Limits
  slug: home-depot-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: The Home Depot API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: home-depot-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 7.9
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/home-depot/home-depot-2026-06-20T182823.png
security:
- kind: authentication
  name: Home Depot Authentication
  slug: home-depot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Home Depot Domain Security
  slug: home-depot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: home-depot
tags:
- Fortune 100
website: https://homedepot.com
---
