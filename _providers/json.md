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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: JSON (JavaScript Object Notation) specification and related resources. Standardized by IETF as RFC 8259 (December 2017, edited by Tim Bray) and by Ecma International as ECMA-404. Defines the grammar a
  name: JSON
  slug: json
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/json-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.json.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.json.org/
- group: docs
  title: ''
  type: Reference
  url: https://www.rfc-editor.org/rfc/rfc8259
created: '2025-01-01'
description: JSON (JavaScript Object Notation) is a lightweight, text-based, language-independent data interchange format that uses human-readable text to represent structured data as key-value pairs and arrays. JSON is standardized by RFC 8259 (December 2017), which obsoletes RFC 7159 (2014) and RFC 4627 (2006). It has become the de facto standard for data exchange in web APIs, configuration files, and NoSQL databases due to its simplicity and broad language support.
finops:
- name: Json Finops
  service_category: API
  slug: json-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/json.png
json_schemas:
- name: JSON Patch and JSON Merge Patch
  property_count: 0
  slug: json-patch
- name: JSON Schema Draft 2020-12 Meta-Schema
  property_count: 0
  slug: json-schema-meta
jsonld:
- class_count: 0
  name: Json Context
  property_count: 21
  slug: json-context
layout: provider
modified: '2026-04-28'
name: JSON
nav: Providers
network: true
overview: 'JSON publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Format, Serialization, Web Development, JSON, and RFC 8259.


  The JSON catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JSON''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Json Plans Pricing
  plan_count: 3
  slug: json-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Json Rate Limits
  slug: json-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: JSON API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: json-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 16.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/json/refs/heads/main/screenshots/json-2026-06-20T183812.png
security:
- kind: domain-security
  name: Json Domain Security
  slug: json-domain-security
  summary_line: TLSv1.3 · DMARC
slug: json
tags:
- Data Format
- Serialization
- Web Development
- JSON
- RFC 8259
website: https://www.json.org/
---
