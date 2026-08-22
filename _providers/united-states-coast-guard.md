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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: United States Coast Guard Agentic Access
  operation_count: 8
  slug: united-states-coast-guard-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: The Vessel Information Verification Service (VIVS) is a NAVCEN web service that allows retrieval of a vessel's broadcasted AIS static data, including Maritime Mobile Service Identity (MMSI), call sign
  name: NAVCEN AIS Vessel Information Verification Service
  slug: navcen-ais-vessel-information
- description: USCG approved equipment certification data
  name: United States Coast Guard Equipment API
  slug: united-states-coast-guard-equipment-api
- description: Incident Investigation Report data
  name: United States Coast Guard Incident Reports API
  slug: united-states-coast-guard-incident-reports-api
- description: Port State Information Exchange vessel safety data
  name: United States Coast Guard Port State Information API
  slug: united-states-coast-guard-port-state-information-api
- description: National Vessel Documentation Center vessel records
  name: United States Coast Guard Vessel Documentation API
  slug: united-states-coast-guard-vessel-documentation-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CGMIX Maritime Information Exchange API
  slug: open-cgmix-maritime-information-exchange
- collection_type: open
  name: CGMIX Maritime Information Exchange Equipment API
  slug: open-united-states-coast-guard-equipment-api
- collection_type: open
  name: CGMIX Maritime Information Exchange Equipment Incident Reports API
  slug: open-united-states-coast-guard-incident-reports-api
- collection_type: open
  name: CGMIX Maritime Information Exchange Equipment Port State Information API
  slug: open-united-states-coast-guard-port-state-information-api
- collection_type: open
  name: CGMIX Maritime Information Exchange Equipment Vessel Documentation API
  slug: open-united-states-coast-guard-vessel-documentation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-coast-guard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-coast-guard-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uscoastguard
created: '2024-12-03'
description: The United States Coast Guard is a branch of the military responsible for enforcing maritime laws, protecting the nation's waterways and coastlines, and ensuring the safety and security of seafarers. They conduct search and rescue operations, respond to environmental disasters, combat illegal drug trafficking and immigration, and conduct security patrols to thwart terrorism threats. The USCG provides public APIs and data services through the CGMIX Maritime Information Exchange, the Navigation Center (NAVCEN), and the National Vessel Documentation Center (NVDC).
examples:
- key_count: 3
  name: Cgmix Get Equipment Details Example
  slug: cgmix-get-equipment-details-example
- key_count: 3
  name: Cgmix Get Vessel Cases Example
  slug: cgmix-get-vessel-cases-example
- key_count: 3
  name: Cgmix Get Vessel Summary Example
  slug: cgmix-get-vessel-summary-example
finops:
- name: United States Coast Guard Finops
  service_category: API
  slug: united-states-coast-guard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-coast-guard.png
json_schemas:
- name: CGMIX Vessel Inspection Case
  property_count: 11
  slug: cgmix-vessel-case
- name: CGMIX Vessel
  property_count: 16
  slug: cgmix-vessel
json_structures:
- name: Cgmix Vessel Structure
  property_count: 0
  slug: cgmix-vessel-structure
jsonld:
- class_count: 5
  name: United States Coast Guard Context
  property_count: 19
  slug: united-states-coast-guard-context
layout: provider
modified: '2026-05-19'
name: United States Coast Guard
nav: Providers
network: true
overview: 'United States Coast Guard publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Equipment API, Incident Reports API, Port State Information API, and 1 more. Tagged areas include Federal Government, Maritime Safety, Vessel Documentation, Emergency Response, and Law Enforcement.


  The United States Coast Guard catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: United States Coast Guard Plans Pricing
  plan_count: 3
  slug: united-states-coast-guard-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: United States Coast Guard Rate Limits
  slug: united-states-coast-guard-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: United States Coast Guard API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: cgmix-maritime-information-exchange-rules
- effective_rule_count: 5
  extends: []
  name: United States Coast Guard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-coast-guard-jsonschema-spectral-rules
score:
  band: thin
  composite: 26.9
  delta: -1.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 60.1
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 7.9
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-coast-guard/refs/heads/main/screenshots/united-states-coast-guard-2026-06-20T200050.png
security:
- kind: domain-security
  name: United States Coast Guard Domain Security
  slug: united-states-coast-guard-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: united-states-coast-guard
tags:
- Federal Government
- Maritime Safety
- Vessel Documentation
- Emergency Response
- Law Enforcement
---
