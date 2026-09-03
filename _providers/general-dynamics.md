---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: General Dynamics Agentic Access
  operation_count: 3
  slug: general-dynamics-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.gdmissionsystems.com
  baseurl_source: declared
  description: Technology products operations
  name: General Dynamics Products API
  slug: general-dynamics-products-api
- baseURL: https://api.gdmissionsystems.com
  baseurl_source: declared
  description: Mission systems operations
  name: General Dynamics Systems API
  slug: general-dynamics-systems-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: General Dynamics Mission Systems API
  slug: open-general-dynamics-mission-systems-api
- collection_type: open
  name: General Dynamics Mission Systems Products API
  slug: open-general-dynamics-products-api
- collection_type: open
  name: General Dynamics Mission Products Systems API
  slug: open-general-dynamics-systems-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/general-dynamics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/general-dynamics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/general-dynamics
- group: company
  title: ''
  type: Website
  url: https://www.gd.com
- group: other
  title: ''
  type: Mission Systems
  url: https://gdmissionsystems.com
description: 'General Dynamics Corporation is a global aerospace and defense company headquartered in Reston, Virginia. The company operates across five business segments: Aerospace, Marine Systems, Combat Systems, Technologies, and Mission Systems, providing business aviation, ship construction, land combat vehicles, weapons systems, and technology products and services.'
finops:
- name: General Dynamics Finops
  service_category: Defense & Aerospace
  slug: general-dynamics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/general-dynamics.png
layout: provider
modified: '2026-05-19'
name: General Dynamics
nav: Providers
network: true
overview: 'General Dynamics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Products API and Systems API. Tagged areas include Aerospace, Defense, Mission Systems, Government, and Fortune 100.'
plans:
- name: General Dynamics Plans Pricing
  plan_count: 1
  slug: general-dynamics-plans-pricing
press:
- date: '2026-05-25'
  title: GENERAL | definition in the Cambridge English Dictionary
  url: https://dictionary.cambridge.org/us/dictionary/english/general
- date: '2026-05-25'
  title: The General® Car Insurance | Get a Quote to Insure Your Car
  url: https://www.thegeneral.com/
- date: '2026-05-25'
  title: GENERAL Definition & Meaning
  url: https://www.merriam-webster.com/dictionary/general
- date: '2026-05-25'
  title: General (United States)
  url: https://en.wikipedia.org/wiki/General_(United_States)
- date: '2026-05-25'
  title: 'General Motors: Iconic Vehicles for Every Drive'
  url: https://www.gm.com/
random_paper: 18
rate_limits:
- limit_count: 1
  name: General Dynamics Rate Limits
  slug: general-dynamics-rate-limits
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 61.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/general-dynamics/refs/heads/main/screenshots/general-dynamics-2026-06-20T181724.png
security:
- kind: domain-security
  name: General Dynamics Domain Security
  slug: general-dynamics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: general-dynamics
tags:
- Aerospace
- Defense
- Mission Systems
- Government
- Fortune 100
website: https://www.gd.com
---
