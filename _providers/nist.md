---
access_model:
  confidence: medium
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
  name: Nist Agentic Access
  operation_count: 2
  slug: nist-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Access to chemical and physical property data for thousands of chemical species.
  name: NIST Chemistry WebBook API
  slug: nist-chemistry-webbook-api
- description: Provides access to NIST's scientific and technical databases across multiple domains.
  name: NIST Data Gateway
  slug: nist-data-gateway
- description: Provides access to official NIST time services for time synchronization.
  name: NIST Time API
  slug: nist-time-api
- baseURL: https://services.nvd.nist.gov/rest/json
  baseurl_source: declared
  description: The Cves API from National Institute of Standards and Technology (NIST) — 1 operation(s) for cves.
  name: National Institute of Standards and Technology (NIST) Cves API
  slug: nist-cves-api
- baseURL: https://webbook.nist.gov/cgi
  baseurl_source: declared
  description: Common Platform Enumeration
  name: National Institute of Standards and Technology (NIST) CPE API
  slug: nist-cpe-api
- baseURL: https://webbook.nist.gov/cgi
  baseurl_source: declared
  description: The CVE History API from National Institute of Standards and Technology (NIST) — 1 operation(s) for cve history.
  name: National Institute of Standards and Technology (NIST) CVE History API
  slug: nist-cve-history-api
artifact_total: 16
collections:
- collection_type: open
  name: NIST NVD CVE Cvehistory API
  slug: open-nist-cvehistory-api
- collection_type: open
  name: NIST NVD CVE Cvehistory Cves API
  slug: open-nist-cves-api
- collection_type: open
  name: NIST NVD CVE API
  slug: open-nist-nvd-cve
common:
- group: commercial
  href: https://artifacts.apis.io/nist/plans/nist-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nist-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nist/rate-limits/nist-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nist-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nist/finops/nist-finops.yml
  title: ''
  type: FinOps
  url: finops/nist-finops.yml
- group: other
  href: https://artifacts.apis.io/nist/capabilities/nist-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nist-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://nist.gov
- group: agent
  href: https://artifacts.apis.io/nist/agentic-access/nist-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nist-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nist/security/nist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nist-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nist/authentication/nist-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nist-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nist.gov/news-events/news/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usnistgov
- group: start
  title: ''
  type: Portal
  url: https://nvd.nist.gov/developers
- group: docs
  title: ''
  type: Documentation
  url: https://nvd.nist.gov/developers/vulnerabilities
created: '2024-01-01'
description: APIs provided by the National Institute of Standards and Technology for accessing scientific and technical data, standards, and research information including vulnerability databases, chemistry data, and time services.
finops:
- has_sources: true
  method: generated
  name: Nist Finops
  primary_unit: ''
  service_category: Government Open Data
  slug: nist-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nist.png
layout: provider
modified: '2026-09-16'
name: National Institute of Standards and Technology (NIST)
nav: Providers
network: true
overview: 'National Institute of Standards and Technology (NIST) publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cves API, CPE API, CVE History API, and 3 more. Tagged areas include Cybersecurity, Government, Measurements, Research, and Scientific Data.


  The National Institute of Standards and Technology (NIST) catalog on APIs.io includes 1 Spectral governance ruleset.


  National Institute of Standards and Technology (NIST)''s developer surface includes authentication, engineering blog, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Nist Plans Pricing
  plan_count: 2
  slug: nist-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Nist Rate Limits
  slug: nist-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: National Institute of Standards and Technology (NIST) API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: nist-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 50.2
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/nist/nist-2026-06-20T190331.png
security:
- kind: authentication
  name: Nist Authentication
  slug: nist-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nist Domain Security
  slug: nist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nist
tags:
- Cybersecurity
- Government
- Measurements
- Research
- Scientific Data
- Standards
website: https://nist.gov
---
