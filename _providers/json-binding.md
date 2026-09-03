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
api_count: 1
apis:
- description: 'The Jakarta JSON Binding specification for marshaling Java objects to JSON and unmarshaling JSON back into Java objects. Provides a default mapping algorithm and customization through annotations and '
  name: Jakarta JSON Binding
  slug: json-b
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/json-binding-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jakarta.ee/specifications/jsonb/
- group: docs
  title: ''
  type: Documentation
  url: https://jakarta.ee/specifications/jsonb/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jakartaee/jsonb-api
created: '2025-01-01'
description: Jakarta JSON Binding (JSON-B) defines a standard binding layer for converting Java objects to and from JSON documents. It specifies a default mapping algorithm for serializing and deserializing existing Java classes to and from JSON, while enabling developers to customize the mapping process through a Java API. JSON-B 3.0 is the stable release shipped with Jakarta EE 10, with version 3.1 under development for Jakarta EE 12.
finops:
- name: Json Binding Finops
  service_category: API
  slug: json-binding-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/json-binding.png
layout: provider
modified: '2026-04-28'
name: JSON Binding
nav: Providers
network: true
overview: 'JSON Binding publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Java, JSON, JSON Binding, Jakarta EE, and Serialization.


  JSON Binding''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Json Binding Plans Pricing
  plan_count: 3
  slug: json-binding-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Json Binding Rate Limits
  slug: json-binding-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/json-binding/refs/heads/main/screenshots/json-binding-2026-06-20T183814.png
security:
- kind: domain-security
  name: Json Binding Domain Security
  slug: json-binding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: json-binding
tags:
- Java
- JSON
- JSON Binding
- Jakarta EE
- Serialization
website: https://jakarta.ee/specifications/jsonb/
---
