---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Industry And Security Agentic Access
  operation_count: 2
  slug: bureau-of-industry-and-security-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
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
artifact_total: 14
collections:
- collection_type: open
  name: Consolidated Screening List (CSL) Search API
  slug: open-bureau-of-industry-and-security-search-api
- collection_type: open
  name: Consolidated Screening List (CSL) API
  slug: open-bureau-of-industry-and-security
common:
- group: other
  href: https://artifacts.apis.io/bureau-of-industry-and-security/capabilities/bureau-of-industry-and-security-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bureau-of-industry-and-security-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-industry-and-security/agentic-access/bureau-of-industry-and-security-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-industry-and-security-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-industry-and-security/security/bureau-of-industry-and-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bureau-of-industry-and-security-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-industry-and-security/authentication/bureau-of-industry-and-security-authentication.yml
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
  href: https://artifacts.apis.io/bureau-of-industry-and-security/lifecycle/bureau-of-industry-and-security-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-industry-and-security-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-industry-and-security/conventions/bureau-of-industry-and-security-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bureau-of-industry-and-security-conventions.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-industry-and-security/errors/bureau-of-industry-and-security-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-industry-and-security-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-industry-and-security/conformance/bureau-of-industry-and-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bureau-of-industry-and-security-conformance.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-industry-and-security/data-model/bureau-of-industry-and-security-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bureau-of-industry-and-security-data-model.yml
- group: build
  href: https://artifacts.apis.io/bureau-of-industry-and-security/packages/bureau-of-industry-and-security-packages.yml
  title: ''
  type: Packages
  url: packages/bureau-of-industry-and-security-packages.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-industry-and-security/llms/bureau-of-industry-and-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-industry-and-security-llms.txt
- group: agent
  href: https://artifacts.apis.io/bureau-of-industry-and-security/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bureau-of-industry-and-security/mcp/bureau-of-industry-and-security-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-industry-and-security-mcp.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-industry-and-security/rate-limits/bureau-of-industry-and-security-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-industry-and-security-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-industry-and-security/plans/bureau-of-industry-and-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bureau-of-industry-and-security-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/bureau-of-industry-and-security/finops/bureau-of-industry-and-security-finops.yml
  title: ''
  type: FinOps
  url: finops/bureau-of-industry-and-security-finops.yml
- group: start
  href: https://artifacts.apis.io/bureau-of-industry-and-security/sandbox/bureau-of-industry-and-security-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bureau-of-industry-and-security-sandbox.yml
created: '2024-11-25'
description: The Bureau of Industry and Security (BIS), a division of the U.S. Department of Commerce, advances U.S. national security, foreign policy, and economic objectives by administering an effective export control and treaty compliance system. BIS maintains the Commerce Control List (CCL), administers the Consolidated Screening List (CSL), and operates the SNAP-R licensing system.
finops:
- has_sources: true
  method: derived
  name: Bureau Of Industry And Security Finops
  primary_unit: ''
  service_category: ''
  slug: bureau-of-industry-and-security-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-industry-and-security.png
layout: provider
modified: '2026-09-05'
name: Bureau of Industry and Security
nav: Providers
network: true
overview: 'Bureau of Industry and Security publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Search API, and 2 more. Tagged areas include Compliance, Export Control, Federal Government, Industries, and National Security.


  The Bureau of Industry and Security catalog on APIs.io includes 1 Spectral governance ruleset.


  Bureau of Industry and Security''s developer surface includes authentication, signup flow, support, engineering blog, developer console, changelog, sandbox, and 25 more developer resources.'
plans:
- name: Bureau Of Industry And Security Plans Pricing
  plan_count: 1
  slug: bureau-of-industry-and-security-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Bureau Of Industry And Security Rate Limits
  slug: bureau-of-industry-and-security-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Bureau of Industry and Security API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: bureau-of-industry-and-security-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 51.4
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bureau-of-industry-and-security/bureau-of-industry-and-security-2026-06-20T173808.png
security:
- kind: authentication
  name: Bureau Of Industry And Security Authentication
  slug: bureau-of-industry-and-security-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bureau Of Industry And Security Domain Security
  slug: bureau-of-industry-and-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: load-the-consolidated-screening-list-in-bulk
  slug: bureau-of-industry-and-security-bulk-screening-feed
- name: screen-a-party-against-the-consolidated-screening-list
  slug: bureau-of-industry-and-security-screen-a-party
slug: bureau-of-industry-and-security
tags:
- Compliance
- Export Control
- Federal Government
- Industries
- National Security
- Screening Lists
- Security
website: https://www.bis.gov
---
