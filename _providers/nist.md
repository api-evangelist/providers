---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nist Agentic Access
  operation_count: 2
  slug: nist-agentic-access
  summary_line: 2 operations
api_count: 1
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
  description: The Cvehistory API from National Institute of Standards and Technology (NIST) — 1 operation(s) for cvehistory.
  name: National Institute of Standards and Technology (NIST) Cvehistory API
  slug: nist-cvehistory-api
- baseURL: https://services.nvd.nist.gov/rest/json
  baseurl_source: declared
  description: The Cves API from National Institute of Standards and Technology (NIST) — 1 operation(s) for cves.
  name: National Institute of Standards and Technology (NIST) Cves API
  slug: nist-cves-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nist-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nist.gov/news-events/news/rss.xml
created: '2024-01-01'
description: APIs provided by the National Institute of Standards and Technology for accessing scientific and technical data, standards, and research information including vulnerability databases, chemistry data, and time services.
finops:
- name: Nist Finops
  service_category: Government Open Data
  slug: nist-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nist.png
layout: provider
modified: '2026-05-19'
name: National Institute of Standards and Technology (NIST)
nav: Providers
network: true
overview: 'National Institute of Standards and Technology (NIST) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cvehistory API and Cves API. Tagged areas include Cybersecurity, Government, Measurements, Research, and Scientific Data.


  National Institute of Standards and Technology (NIST)''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Nist Plans Pricing
  plan_count: 2
  slug: nist-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Nist Rate Limits
  slug: nist-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nist/refs/heads/main/screenshots/nist-2026-06-20T190331.png
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
---
