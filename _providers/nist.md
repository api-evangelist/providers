---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nist Agentic Access
  operation_count: 2
  slug: nist-agentic-access
  summary_line: 2 operations
api_count: 5
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
- description: The Cvehistory API from National Institute of Standards and Technology (NIST) — 1 operation(s) for cvehistory.
  name: National Institute of Standards and Technology (NIST) Cvehistory API
  slug: nist-cvehistory-api
- description: The Cves API from National Institute of Standards and Technology (NIST) — 1 operation(s) for cves.
  name: National Institute of Standards and Technology (NIST) Cves API
  slug: nist-cves-api
artifact_total: 12
collections:
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
random_paper: 61
rate_limits:
- limit_count: 3
  name: Nist Rate Limits
  slug: nist-rate-limits
score:
  band: thin
  composite: 31.9
  delta: -2.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.5
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.4
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
