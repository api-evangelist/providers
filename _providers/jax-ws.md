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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: The Jakarta EE specification for XML web services, formerly JSR 224 JAX-WS. Defines annotations such as @WebService, @WebMethod, and @WebParam, as well as runtime APIs for SOAP-based web service provi
  name: Jakarta XML Web Services (JAX-WS)
  slug: jakarta-xml-web-services
- description: Eclipse Metro is the reference implementation of Jakarta XML Web Services (JAX-WS), providing a high-performance, extensible SOAP web services stack for Java applications.
  name: Eclipse Metro
  slug: eclipse-metro
- description: Apache CXF is an open source services framework that supports JAX-WS and JAX-RS, providing tooling and runtime support for SOAP, REST, and other web service protocols.
  name: Apache CXF
  slug: apache-cxf
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jax-ws-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jakarta.ee/specifications/xml-web-services/
- group: docs
  title: ''
  type: Documentation
  url: https://jakarta.ee/specifications/xml-web-services/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jakartaee
created: '2025-01-01'
description: JAX-WS (Java API for XML Web Services) is a Java standard for building and consuming SOAP-based XML web services. Originally specified as JSR 224 under the Java Community Process, JAX-WS is now part of Jakarta EE as Jakarta XML Web Services. It defines annotations and runtime APIs that allow developers to expose Java methods as SOAP web service operations and to generate Java client stubs from WSDL documents. Reference implementations include the Eclipse Metro project and Apache CXF.
finops:
- name: Jax Ws Finops
  service_category: API
  slug: jax-ws-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jax-ws.png
layout: provider
modified: '2026-04-28'
name: JAX-WS
nav: Providers
network: true
overview: 'JAX-WS publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Jakarta EE, Java, JAX-WS, SOAP, and Standard.


  JAX-WS''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Jax Ws Plans Pricing
  plan_count: 3
  slug: jax-ws-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Jax Ws Rate Limits
  slug: jax-ws-rate-limits
score:
  band: emerging
  composite: 20.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jax-ws/refs/heads/main/screenshots/jax-ws-2026-06-20T183703.png
security:
- kind: domain-security
  name: Jax Ws Domain Security
  slug: jax-ws-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jax-ws
tags:
- Jakarta EE
- Java
- JAX-WS
- SOAP
- Standard
- Web Services
- XML
website: https://jakarta.ee/specifications/xml-web-services/
---
