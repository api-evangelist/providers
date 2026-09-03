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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Jakarta JSON Processing specification (formerly JSR 374) for parsing, generating, transforming, and querying JSON messages in Java applications. Provides an object model API and a streaming API fo
  name: Jakarta JSON Processing
  slug: json-p
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/json-processing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jakarta.ee/specifications/jsonp/
- group: docs
  title: ''
  type: Documentation
  url: https://jakarta.ee/specifications/jsonp/
- group: docs
  title: ''
  type: Specification
  url: https://jakarta.ee/specifications/jsonp/2.1/
- group: company
  title: ''
  type: Blog
  url: https://jakarta.ee/blogs/index.xml
created: '2025-01-01'
description: JSON Processing (JSON-P) is a Java API for parsing, generating, transforming, and querying JSON messages. Standardized as Jakarta JSON Processing, it provides both an object model API and a streaming API for working with JSON data in Java applications. The current stable release is Jakarta JSON Processing 2.1 (Jakarta EE 10), with version 2.2 under development for Jakarta EE 12.
finops:
- name: Json Processing Finops
  service_category: API
  slug: json-processing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/json-processing.png
layout: provider
modified: '2026-04-28'
name: JSON Processing
nav: Providers
network: true
overview: 'JSON Processing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Java, JSON, JSON Processing, Parsing, and Jakarta EE.


  JSON Processing''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Json Processing Plans Pricing
  plan_count: 3
  slug: json-processing-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Json Processing Rate Limits
  slug: json-processing-rate-limits
score:
  band: emerging
  composite: 13.9
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
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/json-processing/refs/heads/main/screenshots/json-processing-2026-06-20T183816.png
security:
- kind: domain-security
  name: Json Processing Domain Security
  slug: json-processing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: json-processing
tags:
- Java
- JSON
- JSON Processing
- Parsing
- Jakarta EE
- Streaming API
website: https://jakarta.ee/specifications/jsonp/
---
