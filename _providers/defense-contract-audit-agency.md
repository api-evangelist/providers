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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-defense-contract-audit-agency
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-contract-audit-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-contract-audit-agency
- group: company
  title: ''
  type: Website
  url: https://www.dcaa.mil
- group: company
  title: ''
  type: About
  url: https://www.dcaa.mil/About/
- group: other
  title: ''
  type: Publications
  url: https://www.dcaa.mil/Guidance/
- group: operate
  title: ''
  type: Contact
  url: https://www.dcaa.mil/Contact/
created: '2024-12-03'
description: The Defense Contract Audit Agency (DCAA), under the authority, direction, and control of the Under Secretary of Defense (Comptroller), provides audit and financial advisory services to Department of Defense and other federal entities responsible for acquisition and contract administration. DCAA publishes guidance, audit programs, and reports through its website but does not currently expose a public developer API.
finops:
- name: Defense Contract Audit Agency Finops
  service_category: API
  slug: defense-contract-audit-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-contract-audit-agency.png
layout: provider
modified: '2026-04-28'
name: Defense Contract Audit Agency
nav: Providers
network: true
overview: Defense Contract Audit Agency is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Defense, Department of Defense, Audit, and Contract Audit.
plans:
- name: Defense Contract Audit Agency Plans Pricing
  plan_count: 1
  slug: defense-contract-audit-agency-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Defense Contract Audit Agency Rate Limits
  slug: defense-contract-audit-agency-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-contract-audit-agency/refs/heads/main/screenshots/defense-contract-audit-agency-2026-06-20T175820.png
security:
- kind: domain-security
  name: Defense Contract Audit Agency Domain Security
  slug: defense-contract-audit-agency-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: defense-contract-audit-agency
tags:
- Federal-Government
- Defense
- Department of Defense
- Audit
- Contract Audit
- Financial
website: https://www.dcaa.mil
---
