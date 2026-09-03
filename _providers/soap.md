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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: SOAP Version 1.2 (W3C Recommendation, 2003/2007 Second Edition) is a lightweight protocol for exchanging structured information in a decentralized, distributed environment. It defines an XML message f
  name: SOAP 1.2 Protocol
  slug: soap-protocol
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soap-domain-security.yml
- group: docs
  title: ''
  type: W3C SOAP 1.2 Specification
  url: https://www.w3.org/TR/soap12-part1/
- group: other
  title: ''
  type: W3C SOAP 1.2 Adjuncts
  url: https://www.w3.org/TR/soap12-part2/
- group: docs
  title: ''
  type: W3C SOAP Specifications Index
  url: https://www.w3.org/TR/soap/
- group: other
  title: ''
  type: SOAP 1.1 Note
  url: https://www.w3.org/TR/2000/NOTE-SOAP-20000508/
- group: other
  title: ''
  type: W3C XML Protocol Working Group
  url: https://www.w3.org/2000/xp/Group/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/SOAP
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/soap-envelope.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/soap-header.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/soap-body.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/soap-fault.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/soap-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/soap-vocabulary.yml
created: '2025'
description: SOAP (Simple Object Access Protocol) is an XML-based messaging protocol for exchanging structured information in web services, standardized by W3C as SOAP 1.2 (2003). It provides a platform-independent, language-neutral framework for web service communication with built-in standards for security (WS-Security), reliable messaging (WS-ReliableMessaging), and transactions (WS-Transaction). SOAP messages consist of an Envelope containing an optional Header and a required Body.
examples:
- key_count: 4
  name: Soap Envelope Example
  slug: soap-envelope-example
finops:
- name: Soap Finops
  service_category: API
  slug: soap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soap.png
json_schemas:
- name: SOAP Body
  property_count: 2
  slug: soap-body
- name: SOAP Envelope
  property_count: 3
  slug: soap-envelope
- name: SOAP Fault
  property_count: 5
  slug: soap-fault
- name: SOAP Header Block
  property_count: 6
  slug: soap-header-block
- name: SOAP Header
  property_count: 1
  slug: soap-header
json_structures:
- name: Soap Envelope Structure
  property_count: 0
  slug: soap-envelope-structure
jsonld:
- class_count: 6
  name: Soap Context
  property_count: 13
  slug: soap-context
layout: provider
modified: '2026-05-02'
name: SOAP
nav: Providers
network: true
overview: 'SOAP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SOAP, Messaging Protocol, Web Services, XML, and W3C Standard.


  The SOAP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Soap Plans Pricing
  plan_count: 3
  slug: soap-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Soap Rate Limits
  slug: soap-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SOAP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: soap-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 34.7
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 22.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soap/refs/heads/main/screenshots/soap-2026-06-20T194116.png
security:
- kind: domain-security
  name: Soap Domain Security
  slug: soap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soap
tags:
- SOAP
- Messaging Protocol
- Web Services
- XML
- W3C Standard
- Enterprise Integration
- WS-Star
website: https://www.w3.org/TR/soap12/
---
