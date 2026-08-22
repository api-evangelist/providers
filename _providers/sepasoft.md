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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: A manufacturing execution system (MES) is used to control, track, and document the transformation of raw materials into finished goods in real-time. MES systems are capable of tracking production by t
  name: Sepasoft
  slug: sepasoft
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sepasoft-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sepasoft-domain-security.yml
created: '2025-03-01'
description: A manufacturing execution system (MES) is used to control, track, and document the transformation of raw materials into finished goods in real-time. MES systems are capable of tracking production by the second and, in some cases, less than one second.
finops:
- name: Sepasoft Finops
  service_category: API
  slug: sepasoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sepasoft.png
jsonld:
- class_count: 19
  name: Sepasoft Context
  property_count: 19
  slug: sepasoft-context
layout: provider
modified: '2026-03-16'
name: Sepasoft
nav: Providers
network: true
overview: 'Sepasoft publishes 1 API on the [APIs.io](https://apis.io/) network.


  The Sepasoft catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Sepasoft Plans Pricing
  plan_count: 3
  slug: sepasoft-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Sepasoft Rate Limits
  slug: sepasoft-rate-limits
score:
  band: emerging
  composite: 14.6
  delta: -0.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 15.5
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 15.2
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Sepasoft Domain Security
  slug: sepasoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sepasoft Trust Center
  slug: sepasoft-trust-center
  summary_line: SOC 2, ISO 27001
slug: sepasoft
---
