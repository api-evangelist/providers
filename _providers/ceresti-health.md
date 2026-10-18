---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Ceresti Health platform providing caregiver‑enabled dementia care services
  name: Ceresti Health API
  slug: ceresti-health-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ceresti-health/refs/heads/main/conformance/ceresti-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ceresti-health-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ceresti-health/refs/heads/main/llms/ceresti-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ceresti-health-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceresti-health/refs/heads/main/hosts/ceresti-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceresti-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceresti-health/refs/heads/main/vendors/ceresti-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceresti-health-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.ceresti.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceresti-health/refs/heads/main/security/ceresti-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceresti-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ceresti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ceresti.com/guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ceresti.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.ceresti.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.ceresti.com/in-the-news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ceresti.com/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://guide.ceresti.com/mcp
  - status: 200
    url: https://www.ceresti.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Ceresti Health provides a caregiver‑enabled dementia care platform that helps families monitor and intervene early to reduce hospitalizations for people living with dementia. By combining data‑driven alerts with personalized support, Ceresti aims to lower Medicare costs and improve outcomes for patients, health plans, and ACOs. The company offers health‑plan specific programs, tools for caregivers, and validated cost‑savings evidence.
image: https://cdn.prod.website-files.com/66f60052b41443d22a41c8da/66f603e56435dbdf8b70e954_OPEN%20GRAPH.webp
layout: provider
modified: '2026-10-07'
name: Ceresti Health
nav: Providers
network: true
overview: 'Ceresti Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Dementia, CaregiverSupport, and Health Tech.


  Ceresti Health''s developer surface includes documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ceresti Health Domain Security
  slug: ceresti-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ceresti-health
tags:
- Company
- Healthcare
- Dementia
- CaregiverSupport
- Health Tech
website: https://www.ceresti.com/
---
