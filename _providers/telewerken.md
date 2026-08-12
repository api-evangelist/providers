---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telewerken-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.telewerken.be/
- group: docs
  title: ''
  type: Documentation
  url: https://www.telewerken.be/
- group: other
  title: ''
  type: Statistics
  url: https://www.telewerken.be/in-cijfers/telewerken-in-het-buitenland/
- group: other
  title: ''
  type: Government Resource
  url: https://werk.belgie.be/nl/themas/welzijn-op-het-werk/telewerk
- group: other
  title: ''
  type: Federal Public Service
  url: https://fedweb.belgium.be/nl/verlof_afwezigheid_en_werktijd/werktijd/telewerk
description: Telewerken.be is a Belgian information platform dedicated to remote work (telewerken), operated jointly by Vias Institute and the FOD Mobiliteit en Vervoer (Federal Public Service for Mobility and Transport). The platform provides comprehensive resources on Belgian telework legislation, regulations, employer obligations, employee rights, and telework statistics. Belgium's remote work framework is governed by Collective Bargaining Agreement No. 85 (CBA 85) and the Law of 5 March 2017 on feasible and workable work. The platform serves both employers and employees navigating Belgium's structured telework policy landscape.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telewerken.png
json_schemas:
- name: Belgian Telework Policy
  property_count: 9
  slug: telewerken-policy
jsonld:
- class_count: 3
  name: Telewerken Context
  property_count: 5
  slug: telewerken-context
layout: provider
modified: '2026-05-03'
name: Telewerken
nav: Providers
network: true
overview: 'Telewerken is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Belgium, Government Resource, Policy, Remote Work, and Telework.


  The Telewerken catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Telewerken''s developer surface includes documentation and 5 more developer resources.'
random_paper: 34
rules:
- name: Telewerken API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: telewerken-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 8.1
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telewerken/refs/heads/main/screenshots/telewerken-2026-06-20T195045.png
security:
- kind: domain-security
  name: Telewerken Domain Security
  slug: telewerken-domain-security
  summary_line: TLSv1.3 · DMARC
slug: telewerken
tags:
- Belgium
- Government Resource
- Policy
- Remote Work
- Telework
- Work-Life Balance
website: https://www.telewerken.be/
---
