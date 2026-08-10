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
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Reference resources and tooling for SOA governance, service registries, and enterprise service management. Includes patterns for service discovery, versioning, SLA management, and policy enforcement i
  name: SOA Governance and Registry
  slug: soa-governance
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/soa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soa-domain-security.yml
- group: docs
  title: ''
  type: Reference Documentation
  url: https://en.wikipedia.org/wiki/Service-oriented_architecture
- group: docs
  title: ''
  type: W3C SOAP Specification
  url: https://www.w3.org/TR/soap12/
- group: docs
  title: ''
  type: W3C WSDL Specification
  url: https://www.w3.org/TR/wsdl20/
- group: docs
  title: ''
  type: OASIS SOA Reference Model
  url: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=soa-rm
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/soa-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/soa-service-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/soa-service-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/soa-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/soa-service-registry-example.json
created: '2025'
description: Service-Oriented Architecture (SOA) is an architectural style for building software applications as a collection of loosely coupled, interoperable services. Each service encapsulates a specific business capability and communicates with others through well-defined interfaces, commonly using SOAP, REST, or messaging protocols. SOA enables enterprise integration, reusability, and flexibility across heterogeneous systems.
examples:
- key_count: 3
  name: Soa Service Registry Example
  slug: soa-service-registry-example
finops:
- name: Soa Finops
  service_category: API
  slug: soa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soa.png
json_schemas:
- name: SOA Service
  property_count: 12
  slug: soa-service
json_structures:
- name: Soa Service Structure
  property_count: 0
  slug: soa-service-structure
jsonld:
- class_count: 28
  name: Soa Context
  property_count: 6
  slug: soa-context
layout: provider
modified: '2026-05-02'
name: SOA
nav: Providers
network: true
overview: 'SOA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SOA, Service-Oriented Architecture, Enterprise Integration, Web Services, and SOAP.


  The SOA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SOA''s developer surface includes code examples and 10 more developer resources.'
plans:
- name: Soa Plans Pricing
  plan_count: 3
  slug: soa-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 5
  name: Soa Rate Limits
  slug: soa-rate-limits
rules:
- name: SOA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: soa-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 29.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soa/refs/heads/main/screenshots/soa-2026-06-20T194116.png
security:
- kind: domain-security
  name: Soa Domain Security
  slug: soa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Soa Vulnerability Disclosure
  slug: soa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: soa
tags:
- SOA
- Service-Oriented Architecture
- Enterprise Integration
- Web Services
- SOAP
- ESB
- Microservices
- API Design
---
