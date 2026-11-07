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
  name: Qualcomm Agentic Access
  operation_count: 1
  slug: qualcomm-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://developer.qualcomm.com/api
  baseurl_source: declared
  description: Semiconductors operations
  name: qualcomm Semiconductors API
  slug: qualcomm-semiconductors-api
artifact_total: 11
collections:
- collection_type: open
  name: Qualcomm Developer API
  slug: open-qualcomm-qualcomm-api
- collection_type: open
  name: Qualcomm Developer Semiconductors API
  slug: open-qualcomm-semiconductors-api
common:
- group: commercial
  href: https://artifacts.apis.io/qualcomm/plans/qualcomm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qualcomm-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/qualcomm/rate-limits/qualcomm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qualcomm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/qualcomm/finops/qualcomm-finops.yml
  title: ''
  type: FinOps
  url: finops/qualcomm-finops.yml
- group: company
  title: ''
  type: Website
  url: https://qualcomm.com
- group: agent
  href: https://artifacts.apis.io/qualcomm/agentic-access/qualcomm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qualcomm-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/qualcomm/security/qualcomm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualcomm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qualcomm/security/qualcomm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qualcomm-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/qualcomm/authentication/qualcomm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qualcomm-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qualcomm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qualcomm
- group: company
  title: ''
  type: Blog
  url: https://www.qualcomm.com/news
description: Qualcomm is a multinational semiconductor and telecommunications equipment company that creates intellectual property, semiconductors, software, and services related to wireless technology.
finops:
- has_sources: true
  method: generated
  name: Qualcomm Finops
  primary_unit: ''
  service_category: Semiconductors
  slug: qualcomm-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qualcomm.png
layout: provider
modified: '2026-09-16'
name: Qualcomm
nav: Providers
network: true
overview: 'Qualcomm publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Semiconductors API. Tagged areas include Fortune 500.


  The Qualcomm catalog on APIs.io includes 1 Spectral governance ruleset.


  Qualcomm''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Qualcomm Plans Pricing
  plan_count: 1
  slug: qualcomm-plans-pricing
press:
- date: ''
  title: Qualcomm - News & Events - Press Releases
  url: https://investor.qualcomm.com/news-events/press-releases/default.aspx
- date: ''
  title: QUALCOMM Incorporated (QCOM) Latest Press Releases ...
  url: https://ca.finance.yahoo.com/quote/QCOM/press-releases/
- date: ''
  title: AI Research Areas | Intelligence on Devices
  url: https://www.qualcomm.com/research/artificial-intelligence
- date: ''
  title: Investor Events
  url: https://investor.qualcomm.com/news-events/investor-events/default.aspx
- date: ''
  title: Qualcomm Technologies, Inc. News and Press Releases
  url: https://www.prnewswire.com/news/qualcomm-technologies%2C-inc./
random_paper: 23
rate_limits:
- limit_count: 1
  name: Qualcomm Rate Limits
  slug: qualcomm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Qualcomm API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: qualcomm-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.5
    catalog_earned_first_party: 0.0
    catalog_gap: 82.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 14.3
    discoverability: 42.9
    operational_transparency: 18.4
  previous_composite: 25.5
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
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/qualcomm/qualcomm-2026-06-20T192405.png
security:
- kind: authentication
  name: Qualcomm Authentication
  slug: qualcomm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qualcomm Domain Security
  slug: qualcomm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qualcomm Vulnerability Disclosure
  slug: qualcomm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: qualcomm
tags:
- Fortune 500
website: https://qualcomm.com
---
