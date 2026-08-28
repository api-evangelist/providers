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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: CXF provides Java APIs for building SOAP (JAX-WS) and REST (JAX-RS) web services with WSDL-first and code-first approaches, WS-* standards support, multiple data bindings (JAXB, Aegis, XMLBeans), plug
  name: Apache CXF
  slug: apache-cxf
artifact_total: 36
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/cxf/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/cxf/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-cxf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-cxf-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://cxf.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://cxf.apache.org/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cxf.apache.org/docs/a-simple-jax-ws-service.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cxf.apache.org/download.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/cxf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apache-cxf
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/vocabulary/apache-cxf-vocabulary.yaml
created: '2026-03-16'
description: Apache CXF is an open-source Java services framework governed by the Apache Software Foundation that helps build and develop web services using JAX-WS (SOAP) and JAX-RS (REST) frontend APIs. It supports contract-first (WSDL) and code-first development, full WS-* standards (WS-Security, WS-ReliableMessaging, WS-Addressing, WS-Policy), multiple transports (HTTP, JMS), and integrates with Spring Framework, OSGi/ServiceMix, and major Java EE servers.
examples:
- key_count: 5
  name: Apache Cxf Jaxrs Endpoint Example
  slug: apache-cxf-jaxrs-endpoint-example
- key_count: 7
  name: Apache Cxf Jaxws Endpoint Example
  slug: apache-cxf-jaxws-endpoint-example
- key_count: 8
  name: Apache Cxf Ws Security Config Example
  slug: apache-cxf-ws-security-config-example
features:
- description: Full JAX-WS implementation for building contract-first and code-first SOAP web services with WSDL support.
  name: JAX-WS SOAP Services
- description: Full JAX-RS implementation for building RESTful services with JSON and XML support and OpenAPI integration.
  name: JAX-RS REST Services
- description: Comprehensive WS-Security support including XML Signature, XML Encryption, SAML tokens, Kerberos, and Username Tokens.
  name: WS-Security
- description: Supports HTTP, Servlet, JMS, In-VM, and local transports for flexible service deployment.
  name: Multiple Transports
- description: wsdl2java generates Java clients and server stubs from WSDL; java2ws generates WSDL and XSD from annotated Java classes.
  name: Code Generation
- description: Deep Spring Framework integration with Spring Boot starters for rapid JAX-WS and JAX-RS service development.
  name: Spring Integration
- description: Supports JAXB 2.x, Aegis, XMLBeans, SDO, and JiBX data bindings for flexible XML/JSON marshalling.
  name: Data Bindings
- description: Implements WS-Addressing, WS-ReliableMessaging, WS-Policy, WS-MetadataExchange, and MTOM for enterprise-grade SOAP.
  name: WS-* Standards
finops:
- name: Apache Cxf Finops
  service_category: API
  slug: apache-cxf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-cxf.png
integrations:
- description: CXF provides deep Spring integration including Spring Boot starters for JAX-WS and JAX-RS.
  name: Spring Framework
- description: CXF runs as OSGi bundles in Apache Karaf for modular service deployment.
  name: Apache Karaf / OSGi
- description: CXF services deploy as WAR files or embedded in Tomcat or Jetty servlet containers.
  name: Apache Tomcat / Jetty
- description: CXF uses WSS4J for WS-Security implementation including XML Signature and SAML.
  name: Apache WSS4J
- description: CXF integrates with Swagger/OpenAPI for automatic API documentation of JAX-RS services.
  name: OpenAPI / Swagger
- description: CXF provides a Camel component for integrating web services into Camel routing and mediation flows.
  name: Apache Camel
json_schemas:
- name: JaxRsEndpoint
  property_count: 5
  slug: apache-cxf-jaxrs-endpoint
- name: JaxWsEndpoint
  property_count: 7
  slug: apache-cxf-jaxws-endpoint
- name: WsSecurityConfig
  property_count: 8
  slug: apache-cxf-ws-security-config
json_structures:
- name: Apache Cxf Jaxrs Endpoint Structure
  property_count: 5
  slug: apache-cxf-jaxrs-endpoint-structure
- name: Apache Cxf Jaxws Endpoint Structure
  property_count: 7
  slug: apache-cxf-jaxws-endpoint-structure
- name: Apache Cxf Ws Security Config Structure
  property_count: 8
  slug: apache-cxf-ws-security-config-structure
jsonld:
- class_count: 3
  name: Apache Cxf Context
  property_count: 19
  slug: apache-cxf-context
layout: provider
modified: '2026-04-19'
name: Apache CXF
nav: Providers
network: true
overview: 'Apache CXF publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, JAX-RS, JAX-WS, Java, and Open-Source.


  The Apache CXF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache CXF''s developer surface includes developer portal, documentation, getting-started guide, release notes, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Apache Cxf Plans Pricing
  plan_count: 3
  slug: apache-cxf-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Apache Cxf Rate Limits
  slug: apache-cxf-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache CXF API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-cxf-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.7
  delta: 6.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 30.7
    developer_ergonomics: 54.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 27.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/screenshots/apache-cxf-2026-06-20T172051.png
security:
- kind: domain-security
  name: Apache Cxf Domain Security
  slug: apache-cxf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Cxf Vulnerability Disclosure
  slug: apache-cxf-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-cxf
tags:
- Apache
- JAX-RS
- JAX-WS
- Java
- Open-Source
- REST
- SOAP
- WS-Security
- Web Services
use_cases:
- description: Build and expose SOAP-based service-oriented architecture services in enterprise Java applications.
  name: Enterprise SOA
- description: Create RESTful APIs with JAX-RS annotations, OpenAPI documentation, and JSON/XML serialization.
  name: REST API Development
- description: Wrap or migrate legacy SOAP/WSDL services to REST/JSON while maintaining backward compatibility.
  name: Legacy SOAP Modernization
- description: Use CXF Spring Boot starters to quickly expose JAX-RS or JAX-WS services in microservice architectures.
  name: Spring Boot Microservices
- description: Secure web services with SAML, Kerberos, PKI, or WS-Username Tokens using CXF WSS4J integration.
  name: WS-Security Integration
website: https://cxf.apache.org/
---
