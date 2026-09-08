---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-defense-contract-management-agency
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/defense-contract-management-agency-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-contract-management-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dcma
- group: company
  title: ''
  type: Website
  url: https://www.dcma.mil
- group: company
  title: ''
  type: About
  url: https://www.dcma.mil/About-Us/
- group: company
  title: ''
  type: News
  url: https://www.dcma.mil/News/
- group: other
  title: ''
  type: Acquisition Policy and Innovation
  url: https://www.acq.osd.mil/asda/dpc/api/data-analytics.html
created: '2024-12-03'
description: The Defense Contract Management Agency (DCMA) is the Department of Defense component that works directly with defense suppliers to help ensure that DoD, federal, and allied government supplies and services are delivered on time, at projected cost, and meet performance requirements. DCMA performs contract administration, quality assurance, and earned value management oversight, but does not currently expose a public developer API.
finops:
- name: Defense Contract Management Agency Finops
  service_category: API
  slug: defense-contract-management-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-contract-management-agency.png
layout: provider
modified: '2026-09-07'
name: Defense Contract Management Agency
nav: Providers
network: true
overview: 'Defense Contract Management Agency is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Defense, Department of Defense, Contract Management, and Acquisition.


  Defense Contract Management Agency''s developer surface includes product news and 6 more developer resources.'
plans:
- name: Defense Contract Management Agency Plans Pricing
  plan_count: 0
  slug: defense-contract-management-agency-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Defense Contract Management Agency Rate Limits
  slug: defense-contract-management-agency-rate-limits
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-contract-management-agency/refs/heads/main/screenshots/defense-contract-management-agency-2026-06-20T175824.png
security:
- kind: domain-security
  name: Defense Contract Management Agency Domain Security
  slug: defense-contract-management-agency-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: defense-contract-management-agency
tags:
- Federal-Government
- Defense
- Department of Defense
- Contract Management
- Acquisition
- Earned Value Management
website: https://www.dcma.mil
---
