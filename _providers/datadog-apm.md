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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Datadog APM REST API for traces, spans, services, service definitions, and SLOs. Provides endpoints for searching traces, managing service catalog entries, and configuring service level objectives.
  name: Datadog APM API
  slug: datadog-apm-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/datadog-apm-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/datadog-apm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datadog-apm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datadoghq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datadoghq.com/tracing/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datadoghq.com/getting_started/tracing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DataDog
- group: company
  title: ''
  type: Blog
  url: https://www.datadoghq.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datadoghq.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.datadoghq.com/free-datadog-trial/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/datadog-apm-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/datadog-apm-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/datadog-apm-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/datadog-apm-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.datadoghq.com/llms.txt
created: '2026-03-26'
description: Datadog APM provides end-to-end distributed tracing, continuous profiling, and real-time performance monitoring for applications and microservices. It automatically instruments applications to provide deep visibility into request traces, latency, and error rates across distributed systems.
finops:
- name: Datadog Apm Finops
  service_category: API
  slug: datadog-apm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datadog-apm.png
jsonld:
- class_count: 0
  name: Datadog Apm Context
  property_count: 5
  slug: datadog-apm-context
layout: provider
modified: '2026-04-28'
name: Datadog APM
nav: Providers
network: true
overview: 'Datadog APM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include APM, Distributed Tracing, Microservices, Observability, and Performance Monitoring.


  The Datadog APM catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Datadog APM''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Datadog Apm Plans Pricing
  plan_count: 3
  slug: datadog-apm-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Datadog Apm Rate Limits
  slug: datadog-apm-rate-limits
rules:
- name: Datadog APM API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: datadog-apm-jsonschema-spectral-rules
- name: Datadog APM API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: datadog-apm-rules
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 53.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datadog-apm/refs/heads/main/screenshots/datadog-apm-2026-06-20T175636.png
security:
- kind: domain-security
  name: Datadog Apm Domain Security
  slug: datadog-apm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datadog Apm Vulnerability Disclosure
  slug: datadog-apm-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Datadog Apm Trust Center
  slug: datadog-apm-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: datadog-apm
tags:
- APM
- Distributed Tracing
- Microservices
- Observability
- Performance Monitoring
website: https://www.datadoghq.com/
---
