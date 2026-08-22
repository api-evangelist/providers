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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'MHS Genesis, the Department of Defense electronic health record built on Oracle Health (Cerner), exposes a SMART on FHIR interface for authorized clinical applications to read and write patient data. '
  name: MHS Genesis SMART on FHIR API
  slug: mhs-genesis-smart-on-fhir
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-defense-health-agency
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-health-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-health-agency
- group: company
  title: ''
  type: Website
  url: https://www.health.mil
- group: company
  title: ''
  type: About DHA
  url: https://www.health.mil/About-MHS/OASDHA/Defense-Health-Agency
- group: other
  title: ''
  type: Publications
  url: https://health.mil/Reference-Center/DHA-Publications
- group: company
  title: ''
  type: News
  url: https://www.health.mil/News
created: '2024-12-03'
description: The Defense Health Agency (DHA) is a joint, integrated combat support agency that enables the Army, Navy, and Air Force medical services to provide a medically ready force and ready medical force to combatant commands. DHA operates the Military Health System (MHS), MHS Genesis electronic health record, the Military Health System Data Repository (MDR), and the Enterprise Intelligence and Data Solutions (EIDS) program. Data exchange inside MHS Genesis uses SMART on FHIR APIs, but DHA does not currently publish a general-purpose public developer API.
finops:
- name: Defense Health Agency Finops
  service_category: API
  slug: defense-health-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-health-agency.png
layout: provider
modified: '2026-04-28'
name: Defense Health Agency
nav: Providers
network: true
overview: 'Defense Health Agency publishes 1 API on the [APIs.io](https://apis.io/) network: MHS Genesis SMART on FHIR API. Tagged areas include Federal Government, Defense, Department of Defense, Health, and Military Health System.


  Defense Health Agency''s developer surface includes product news and 5 more developer resources.'
plans:
- name: Defense Health Agency Plans Pricing
  plan_count: 3
  slug: defense-health-agency-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Defense Health Agency Rate Limits
  slug: defense-health-agency-rate-limits
score:
  band: emerging
  composite: 15.5
  delta: -1.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-health-agency/refs/heads/main/screenshots/defense-health-agency-2026-06-20T175826.png
security:
- kind: domain-security
  name: Defense Health Agency Domain Security
  slug: defense-health-agency-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: defense-health-agency
tags:
- Federal Government
- Defense
- Department of Defense
- Health
- Military Health System
- MHS Genesis
- FHIR
- Health IT
website: https://www.health.mil
---
