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
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: The BSEE Well API provides multiregional offshore well information retrieval across Alaska, Atlantic, Gulf of America, and Pacific regions. Query by API well number, company name, well status, field n
  name: BSEE Well API Online Query
  slug: bsee-well-api
- description: The BSEE Data Center provides online query services and data downloads for offshore oil and gas operations. Data covers company information, leasing, pipelines, wells, production, platforms, and permi
  name: BSEE Data Center
  slug: bsee-data-center
- description: The Technical Information Management System (TIMS) / eWell system enables permit submissions and well activity reporting for offshore operations. Operators use this system to submit Applications for P
  name: BSEE eWell Permitting System (TIMS)
  slug: tims-eplanning
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-safety-and-environmental-enforcement-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-safety-and-environmental-enforcement-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-safety-and-environmental-enforcement
- group: company
  title: ''
  type: Website
  url: https://www.bsee.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.data.bsee.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bsee.gov/privacy-policy
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=bsee-gov
- group: company
  title: ''
  type: Blog
  url: https://www.bsee.gov/rss.xml
created: '2024-11-30'
description: The Bureau of Safety and Environmental Enforcement (BSEE) works to promote safety, protect the environment, and conserve resources offshore through vigorous regulatory oversight and enforcement.
finops:
- name: Bureau Of Safety And Environmental Enforcement Finops
  service_category: API
  slug: bureau-of-safety-and-environmental-enforcement-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-safety-and-environmental-enforcement.png
layout: provider
modified: '2026-04-23'
name: Bureau of Safety and Environmental Enforcement
nav: Providers
network: true
overview: 'Bureau of Safety and Environmental Enforcement publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enforcement, Environment, Federal-Government, Safety, and Offshore.


  Bureau of Safety and Environmental Enforcement''s developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Bureau Of Safety And Environmental Enforcement Plans Pricing
  plan_count: 3
  slug: bureau-of-safety-and-environmental-enforcement-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Bureau Of Safety And Environmental Enforcement Rate Limits
  slug: bureau-of-safety-and-environmental-enforcement-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-safety-and-environmental-enforcement/refs/heads/main/screenshots/bureau-of-safety-and-environmental-enforcement-2026-06-20T173818.png
security:
- kind: domain-security
  name: Bureau Of Safety And Environmental Enforcement Domain Security
  slug: bureau-of-safety-and-environmental-enforcement-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Safety And Environmental Enforcement Vulnerability Disclosure
  slug: bureau-of-safety-and-environmental-enforcement-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bureau-of-safety-and-environmental-enforcement
tags:
- Enforcement
- Environment
- Federal-Government
- Safety
- Offshore
- Oil and Gas
- Wells
website: https://www.bsee.gov/
---
