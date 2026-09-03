---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Motor Carrier Safety Administration Agentic Access
  operation_count: 7
  slug: federal-motor-carrier-safety-administration-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://mobile.fmcsa.dot.gov/qc/services
  baseurl_source: declared
  description: The Carriers API from Federal Motor Carrier Safety Administration — 7 operation(s) for carriers.
  name: Federal Motor Carrier Safety Administration Carriers API
  slug: federal-motor-carrier-safety-administration-carriers-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Federal Motor Carrier Safety Administration QCMobile Carriers API
  slug: open-federal-motor-carrier-safety-administration-carriers-api
- collection_type: open
  name: Federal Motor Carrier Safety Administration QCMobile API
  slug: open-federal-motor-carrier-safety-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-motor-carrier-safety-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-motor-carrier-safety-administration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-motor-carrier-safety-administration-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fmcsa
- group: company
  title: ''
  type: Website
  url: https://www.fmcsa.dot.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess
created: '2024-12-03'
description: As the lead federal government agency responsible for regulating and providing safety oversight of commercial motor vehicles (CMVs), FMCSA's mission is to reduce crashes, injuries, and fatalities involving large trucks and buses.
finops:
- name: Federal Motor Carrier Safety Administration Finops
  service_category: API
  slug: federal-motor-carrier-safety-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-motor-carrier-safety-administration.png
layout: provider
modified: '2026-05-19'
name: Federal Motor Carrier Safety Administration
nav: Providers
network: true
overview: 'Federal Motor Carrier Safety Administration publishes 1 API on the [APIs.io](https://apis.io/) network: Carriers API. Tagged areas include Federal-Government, Safety, and Transportation.


  Federal Motor Carrier Safety Administration''s developer surface includes authentication, documentation, and 4 more developer resources.'
plans:
- name: Federal Motor Carrier Safety Administration Plans Pricing
  plan_count: 3
  slug: federal-motor-carrier-safety-administration-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Federal Motor Carrier Safety Administration Rate Limits
  slug: federal-motor-carrier-safety-administration-rate-limits
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
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
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-motor-carrier-safety-administration/refs/heads/main/screenshots/federal-motor-carrier-safety-administration-2026-06-20T181123.png
security:
- kind: authentication
  name: Federal Motor Carrier Safety Administration Authentication
  slug: federal-motor-carrier-safety-administration-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Federal Motor Carrier Safety Administration Domain Security
  slug: federal-motor-carrier-safety-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-motor-carrier-safety-administration
tags:
- Federal-Government
- Safety
- Transportation
website: https://www.fmcsa.dot.gov/
---
