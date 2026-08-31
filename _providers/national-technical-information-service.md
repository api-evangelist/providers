---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The NTIS National Technical Reports Library (NTRL) offers online, free and open access to authenticated government technical reports and documents.
  name: National Technical Information Service
  slug: national-technical-information-service
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-technical-information-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-technical-information-service
- group: company
  title: ''
  type: Website
  url: https://www.ntis.gov/
- group: start
  title: ''
  type: Portal
  url: https://ntrl.ntis.gov/
created: '2024-12-03'
description: The National Technical Information Service (NTIS) is a government agency that serves as the largest central resource for government-funded scientific, technical, engineering, and business-related information, collecting, archiving, and disseminating data and reports on energy, aerospace, health, and environmental topics.
finops:
- name: National Technical Information Service Finops
  service_category: API
  slug: national-technical-information-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-technical-information-service.png
layout: provider
modified: '2026-04-28'
name: National Technical Information Service
nav: Providers
network: true
overview: 'National Technical Information Service publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Information, and Technical.


  National Technical Information Service''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: National Technical Information Service Plans Pricing
  plan_count: 3
  slug: national-technical-information-service-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: National Technical Information Service Rate Limits
  slug: national-technical-information-service-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-technical-information-service/refs/heads/main/screenshots/national-technical-information-service-2026-06-20T190042.png
security:
- kind: domain-security
  name: National Technical Information Service Domain Security
  slug: national-technical-information-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-technical-information-service
tags:
- Federal-Government
- Information
- Technical
website: https://www.ntis.gov/
---
