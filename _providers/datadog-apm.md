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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: The Service Definitions API from Datadog APM — 2 operation(s) for service definitions.
  name: Datadog APM Service Definitions API
  slug: datadog-apm-service-definitions-api
- description: The Services API from Datadog APM — 1 operation(s) for services.
  name: Datadog APM Services API
  slug: datadog-apm-services-api
- description: The SLOs API from Datadog APM — 3 operation(s) for slos.
  name: Datadog APM SL Os API
  slug: datadog-apm-slos-api
- description: The Spans API from Datadog APM — 2 operation(s) for spans.
  name: Datadog APM Spans API
  slug: datadog-apm-spans-api
- description: The Traces API from Datadog APM — 1 operation(s) for traces.
  name: Datadog APM Traces API
  slug: datadog-apm-traces-api
artifact_total: 14
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
overview: 'Datadog APM publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Service Definitions API, Services API, SL Os API, and 2 more. Tagged areas include APM, Distributed Tracing, Microservices, Observability, and Performance Monitoring.


  The Datadog APM catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Datadog APM''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Datadog Apm Plans Pricing
  plan_count: 3
  slug: datadog-apm-plans-pricing
random_paper: 43
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
  composite: 52.9
  delta: -0.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 69.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 53.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
