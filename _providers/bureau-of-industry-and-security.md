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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Industry And Security Agentic Access
  operation_count: 2
  slug: bureau-of-industry-and-security-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- baseURL: https://data.trade.gov/consolidated_screening_list/v1
  baseurl_source: declared
  description: The Consolidated Screening List (CSL) API consolidates export screening lists from the Departments of Commerce, State, and Treasury. It includes the Entity List, Denied Persons List, Unverified List (
  name: Consolidated Screening List (CSL) API
  slug: consolidated-screening-list-api
- description: SNAP-R (Simplified Network Application Process Redesign) is the BIS online system for applying for export licenses, classifications, and authorizations under the Export Administration Regulations (EAR
  name: SNAP-R Export License Application System
  slug: snap-r
- description: STELA (System for Tracking Export License Applications) allows applicants to check the status of export license applications submitted to BIS.
  name: STELA Export License Tracking
  slug: stela
- baseURL: https://data.trade.gov/consolidated_screening_list/v1
  baseurl_source: declared
  description: Search the Consolidated Screening List
  name: Bureau of Industry and Security Search API
  slug: bureau-of-industry-and-security-search-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Consolidated Screening List (CSL) Search API
  slug: open-bureau-of-industry-and-security-search-api
- collection_type: open
  name: Consolidated Screening List (CSL) API
  slug: open-bureau-of-industry-and-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-industry-and-security-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-industry-and-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-industry-and-security-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-industry-and-security-u-s-department-of-commerce
- group: company
  title: ''
  type: Website
  url: https://www.bis.gov
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bis.gov/privacy-policy
- group: other
  title: ''
  type: Consolidated Screening List
  url: https://www.trade.gov/consolidated-screening-list
- group: other
  title: ''
  type: Export Administration Regulations
  url: https://www.bis.gov/regulations/ear
- group: other
  title: ''
  type: Commerce Control List
  url: https://www.bis.gov/licensing/classify-your-item
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.trade.gov/
- group: start
  title: ''
  type: SignUp
  url: https://developer.trade.gov/signup
- group: operate
  title: ''
  type: Support
  url: https://www.bis.gov/about-bis/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.bis.gov/news-updates
- group: start
  title: ''
  type: Console
  url: https://developer.trade.gov/api-details#api=consolidated-screening-list&operation=search
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.trade.gov/api-changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.trade.gov/csl-api-is-changing
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://developer.trade.gov/service-level-agreement
- group: other
  title: ''
  type: APICatalog
  url: https://www.bis.gov/data.json
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-industry-and-security-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-industry-and-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-industry-and-security-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-industry-and-security-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-industry-and-security-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-industry-and-security-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-industry-and-security-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-industry-and-security-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-industry-and-security-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-industry-and-security-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bureau-of-industry-and-security-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bureau-of-industry-and-security-sandbox.yml
created: '2024-11-25'
description: The Bureau of Industry and Security (BIS), a division of the U.S. Department of Commerce, advances U.S. national security, foreign policy, and economic objectives by administering an effective export control and treaty compliance system. BIS maintains the Commerce Control List (CCL), administers the Consolidated Screening List (CSL), and operates the SNAP-R licensing system.
finops:
- name: Bureau Of Industry And Security Finops
  service_category: API
  slug: bureau-of-industry-and-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-industry-and-security.png
layout: provider
modified: '2026-09-05'
name: Bureau of Industry and Security
nav: Providers
network: true
overview: 'Bureau of Industry and Security publishes 2 APIs on the [APIs.io](https://apis.io/) network: Consolidated Screening List (CSL) API and Search API. Tagged areas include Compliance, Export Controls, Federal-Government, Industries, and National Security.


  Bureau of Industry and Security''s developer surface includes authentication, signup flow, support, engineering blog, developer console, changelog, sandbox, and 24 more developer resources.'
plans:
- name: Bureau Of Industry And Security Plans Pricing
  plan_count: 1
  slug: bureau-of-industry-and-security-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Bureau Of Industry And Security Rate Limits
  slug: bureau-of-industry-and-security-rate-limits
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 54.2
    discoverability: 77.8
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-industry-and-security/refs/heads/main/screenshots/bureau-of-industry-and-security-2026-06-20T173808.png
security:
- kind: authentication
  name: Bureau Of Industry And Security Authentication
  slug: bureau-of-industry-and-security-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bureau Of Industry And Security Domain Security
  slug: bureau-of-industry-and-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-industry-and-security
tags:
- Compliance
- Export Controls
- Federal-Government
- Industries
- National Security
- Screening Lists
- Security
website: https://www.bis.gov
---
