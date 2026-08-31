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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 41
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wsdl-domain-security.yml
- group: docs
  title: WSDL 2.0 Part 1 Core Language
  type: Specification
  url: https://www.w3.org/TR/wsdl20/
- group: docs
  title: WSDL 2.0 Part 2 Adjuncts
  type: Specification
  url: https://www.w3.org/TR/wsdl20-adjuncts/
- group: docs
  title: WSDL 2.0 Part 0 Primer
  type: Specification
  url: https://www.w3.org/TR/wsdl20-primer/
- group: docs
  title: WSDL 2.0 RDF Mapping
  type: Specification
  url: https://www.w3.org/TR/wsdl20-rdf/
- group: company
  title: W3C Web Services Activity
  type: Website
  url: https://www.w3.org/standards/techs/wsdl
- group: docs
  title: WSDL 2.0 Technical Reports
  type: Documentation
  url: https://www.w3.org/TR/?tag=webservice
- group: build
  title: W3C GitHub
  type: GitHubOrganization
  url: https://github.com/w3c
- group: operate
  title: W3C Web Services Discussion
  type: Community
  url: https://lists.w3.org/Archives/Public/public-ws-desc/
- group: docs
  title: WSDL Description
  type: JSONSchema
  url: json-schema/wsdl-description.json
- group: docs
  title: WSDL Types
  type: JSONSchema
  url: json-schema/wsdl-types.json
- group: docs
  title: WSDL Interface
  type: JSONSchema
  url: json-schema/wsdl-interface.json
- group: docs
  title: WSDL Operation
  type: JSONSchema
  url: json-schema/wsdl-operation.json
- group: docs
  title: WSDL Interface Fault
  type: JSONSchema
  url: json-schema/wsdl-interface-fault.json
- group: docs
  title: WSDL Binding
  type: JSONSchema
  url: json-schema/wsdl-binding.json
- group: docs
  title: WSDL Service
  type: JSONSchema
  url: json-schema/wsdl-service.json
- group: docs
  title: WSDL Endpoint
  type: JSONSchema
  url: json-schema/wsdl-endpoint.json
- group: design
  title: WSDL JSON-LD Context
  type: JSONLDContext
  url: json-ld/wsdl-context.jsonld
- group: design
  title: WSDL Description Structure
  type: JSONStructure
  url: json-structure/wsdl-description-structure.json
- group: design
  title: WSDL Types Structure
  type: JSONStructure
  url: json-structure/wsdl-types-structure.json
- group: design
  title: WSDL Interface Structure
  type: JSONStructure
  url: json-structure/wsdl-interface-structure.json
- group: design
  title: WSDL Operation Structure
  type: JSONStructure
  url: json-structure/wsdl-operation-structure.json
- group: design
  title: WSDL Interface Fault Structure
  type: JSONStructure
  url: json-structure/wsdl-interface-fault-structure.json
- group: design
  title: WSDL Binding Structure
  type: JSONStructure
  url: json-structure/wsdl-binding-structure.json
- group: design
  title: WSDL Service Structure
  type: JSONStructure
  url: json-structure/wsdl-service-structure.json
- group: design
  title: WSDL Endpoint Structure
  type: JSONStructure
  url: json-structure/wsdl-endpoint-structure.json
- group: design
  title: WSDL Vocabulary
  type: Vocabulary
  url: vocabulary/wsdl-vocabulary.yaml
created: '2025'
description: WSDL (Web Services Description Language) is a W3C standard XML format for describing web service interfaces. It defines services as collections of network endpoints (ports) that exchange messages, specifying the abstract operations, message formats, and protocol bindings needed to interact with a web service. WSDL 2.0 became a W3C Recommendation on June 26, 2007, and adds support for all HTTP request methods, making it more suitable for RESTful web services than its predecessor WSDL 1.1.
features:
- description: Defines abstract interfaces separating service contract from protocol binding.
  name: Abstract Service Interface
- description: Supports In-Only, Robust In-Only, and In-Out message exchange patterns.
  name: Message Exchange Patterns
- description: Native SOAP 1.2 binding for web service interoperability.
  name: SOAP Binding
- description: HTTP binding supporting all HTTP methods including GET, POST, PUT, DELETE.
  name: HTTP Binding
- description: RPC-style operation dispatch with input and output message wrappers.
  name: RPC Style Operations
- description: Integrates with XML Schema for defining message types.
  name: Type System Integration
- description: Supports multiple endpoints per service with different protocol bindings.
  name: Multiple Endpoints
- description: Uses XML namespaces to enable modular and reusable service descriptions.
  name: Namespace and Modularity
- description: Allows marking safe read-only operations per web architecture principles.
  name: Operation Safety Declaration
- description: Normative mapping to RDF for linked data and semantic web integration.
  name: RDF Mapping
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wsdl.png
integrations:
- description: WSDL 2.0 uses XML Schema for type definitions.
  name: XML Schema
- description: Native SOAP 1.2 binding defined in WSDL 2.0 Part 2.
  name: SOAP 1.2
- description: HTTP binding supporting REST-style services.
  name: HTTP 1.1
- description: WSDL documents are referenced in UDDI service registries.
  name: UDDI
- description: Web services policy framework that annotates WSDL descriptions.
  name: WS-Policy
- description: Endpoint reference standards used with WSDL service endpoints.
  name: WS-Addressing
json_schemas:
- name: WSDL Binding
  property_count: 5
  slug: wsdl-binding
- name: WSDL Description
  property_count: 5
  slug: wsdl-description
- name: WSDL Endpoint
  property_count: 3
  slug: wsdl-endpoint
- name: WSDL Interface Fault
  property_count: 2
  slug: wsdl-interface-fault
- name: WSDL Interface
  property_count: 5
  slug: wsdl-interface
- name: WSDL Operation
  property_count: 8
  slug: wsdl-operation
- name: WSDL Service
  property_count: 3
  slug: wsdl-service
- name: WSDL Types
  property_count: 2
  slug: wsdl-types
json_structures:
- name: Wsdl Binding Structure
  property_count: 5
  slug: wsdl-binding-structure
- name: Wsdl Description Structure
  property_count: 5
  slug: wsdl-description-structure
- name: Wsdl Endpoint Structure
  property_count: 3
  slug: wsdl-endpoint-structure
- name: Wsdl Interface Fault Structure
  property_count: 2
  slug: wsdl-interface-fault-structure
- name: Wsdl Interface Structure
  property_count: 5
  slug: wsdl-interface-structure
- name: Wsdl Operation Structure
  property_count: 8
  slug: wsdl-operation-structure
- name: Wsdl Service Structure
  property_count: 3
  slug: wsdl-service-structure
- name: Wsdl Types Structure
  property_count: 2
  slug: wsdl-types-structure
jsonld:
- class_count: 6
  name: Wsdl Context
  property_count: 20
  slug: wsdl-context
layout: provider
modified: '2026-05-03'
name: WSDL
nav: Providers
network: true
overview: 'WSDL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Service Description, W3C, Web Services, WSDL, and XML.


  The WSDL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WSDL''s developer surface includes documentation and 26 more developer resources.'
random_paper: 1
rules:
- effective_rule_count: 5
  extends: []
  name: WSDL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wsdl-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 68.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 14.7
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 25.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 16.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wsdl/refs/heads/main/screenshots/wsdl-2026-06-20T201632.png
security:
- kind: domain-security
  name: Wsdl Domain Security
  slug: wsdl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wsdl
tags:
- Service Description
- W3C
- Web Services
- WSDL
- XML
- SOAP
- Standards
- Protocols
use_cases:
- description: Describing enterprise SOAP web services for automated client generation.
  name: SOAP Web Service Description
- description: Defining service contracts between service providers and consumers.
  name: Service Contract Definition
- description: Generating client proxy code and server stubs from WSDL documents.
  name: Code Generation
- description: Enabling automated discovery and invocation of web services.
  name: Service Discovery
- description: Validating interoperability between different SOAP implementations.
  name: Interoperability Testing
- description: Describing RESTful services using WSDL 2.0 HTTP binding support.
  name: REST Service Description
website: https://www.w3.org/standards/techs/wsdl
---
