---
aid: wsdl
name: WSDL
description: WSDL (Web Services Description Language) is a W3C standard XML format for describing web service interfaces. It defines services as collections of network endpoints (ports) that exchange messages, specifying the abstract operations, message formats, and protocol bindings needed to interact with a web service. WSDL 2.0 became a W3C Recommendation on June 26, 2007, and adds support for all HTTP request methods, making it more suitable for RESTful web services than its predecessor WSDL 1.1.
url: https://www.w3.org/TR/wsdl20/
tags:
  - Service Description
  - W3C
  - Web Services
  - WSDL
  - XML
  - SOAP
  - Standards
  - Protocols
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis: []
common:
  - type: Specification
    title: WSDL 2.0 Part 1 Core Language
    url: https://www.w3.org/TR/wsdl20/
    description: Core language specification defining the WSDL 2.0 component model, XML representation, and conformance requirements.
  - type: Specification
    title: WSDL 2.0 Part 2 Adjuncts
    url: https://www.w3.org/TR/wsdl20-adjuncts/
    description: Defines message exchange patterns, operation styles, and SOAP/HTTP binding extensions for WSDL 2.0.
  - type: Specification
    title: WSDL 2.0 Part 0 Primer
    url: https://www.w3.org/TR/wsdl20-primer/
    description: Non-normative introduction and tutorial for the WSDL 2.0 specification with worked examples.
  - type: Specification
    title: WSDL 2.0 RDF Mapping
    url: https://www.w3.org/TR/wsdl20-rdf/
    description: Normative mapping from WSDL 2.0 component model to RDF triples for linked data representation.
  - type: Website
    title: W3C Web Services Activity
    url: https://www.w3.org/standards/techs/wsdl
    description: W3C standards page for WSDL covering all versions and related specifications.
  - type: Documentation
    title: WSDL 2.0 Technical Reports
    url: https://www.w3.org/TR/?tag=webservice
    description: All W3C technical reports related to web services including WSDL.
  - type: GitHubOrganization
    title: W3C GitHub
    url: https://github.com/w3c
    description: W3C organization on GitHub where web standards tooling and schemas are maintained.
  - type: Community
    title: W3C Web Services Discussion
    url: https://lists.w3.org/Archives/Public/public-ws-desc/
    description: Public mailing list archive for the W3C Web Services Description Working Group.
  - type: json-schema
    title: WSDL Description
    url: json-schema/wsdl-description.json
  - type: json-schema
    title: WSDL Types
    url: json-schema/wsdl-types.json
  - type: json-schema
    title: WSDL Interface
    url: json-schema/wsdl-interface.json
  - type: json-schema
    title: WSDL Operation
    url: json-schema/wsdl-operation.json
  - type: json-schema
    title: WSDL Interface Fault
    url: json-schema/wsdl-interface-fault.json
  - type: json-schema
    title: WSDL Binding
    url: json-schema/wsdl-binding.json
  - type: json-schema
    title: WSDL Service
    url: json-schema/wsdl-service.json
  - type: json-schema
    title: WSDL Endpoint
    url: json-schema/wsdl-endpoint.json
  - type: json-ld-context
    title: WSDL JSON-LD Context
    url: json-ld/wsdl-context.jsonld
  - type: JSONStructure
    title: WSDL Description Structure
    url: json-structure/wsdl-description-structure.json
  - type: JSONStructure
    title: WSDL Types Structure
    url: json-structure/wsdl-types-structure.json
  - type: JSONStructure
    title: WSDL Interface Structure
    url: json-structure/wsdl-interface-structure.json
  - type: JSONStructure
    title: WSDL Operation Structure
    url: json-structure/wsdl-operation-structure.json
  - type: JSONStructure
    title: WSDL Interface Fault Structure
    url: json-structure/wsdl-interface-fault-structure.json
  - type: JSONStructure
    title: WSDL Binding Structure
    url: json-structure/wsdl-binding-structure.json
  - type: JSONStructure
    title: WSDL Service Structure
    url: json-structure/wsdl-service-structure.json
  - type: JSONStructure
    title: WSDL Endpoint Structure
    url: json-structure/wsdl-endpoint-structure.json
  - type: Vocabulary
    title: WSDL Vocabulary
    url: vocabulary/wsdl-vocabulary.yaml
  - type: Features
    data:
      - name: Abstract Service Interface
        description: Defines abstract interfaces separating service contract from protocol binding.
      - name: Message Exchange Patterns
        description: Supports In-Only, Robust In-Only, and In-Out message exchange patterns.
      - name: SOAP Binding
        description: Native SOAP 1.2 binding for web service interoperability.
      - name: HTTP Binding
        description: HTTP binding supporting all HTTP methods including GET, POST, PUT, DELETE.
      - name: RPC Style Operations
        description: RPC-style operation dispatch with input and output message wrappers.
      - name: Type System Integration
        description: Integrates with XML Schema for defining message types.
      - name: Multiple Endpoints
        description: Supports multiple endpoints per service with different protocol bindings.
      - name: Namespace and Modularity
        description: Uses XML namespaces to enable modular and reusable service descriptions.
      - name: Operation Safety Declaration
        description: Allows marking safe read-only operations per web architecture principles.
      - name: RDF Mapping
        description: Normative mapping to RDF for linked data and semantic web integration.
  - type: UseCases
    data:
      - name: SOAP Web Service Description
        description: Describing enterprise SOAP web services for automated client generation.
      - name: Service Contract Definition
        description: Defining service contracts between service providers and consumers.
      - name: Code Generation
        description: Generating client proxy code and server stubs from WSDL documents.
      - name: Service Discovery
        description: Enabling automated discovery and invocation of web services.
      - name: Interoperability Testing
        description: Validating interoperability between different SOAP implementations.
      - name: REST Service Description
        description: Describing RESTful services using WSDL 2.0 HTTP binding support.
  - type: Integrations
    data:
      - name: XML Schema
        description: WSDL 2.0 uses XML Schema for type definitions.
      - name: SOAP 1.2
        description: Native SOAP 1.2 binding defined in WSDL 2.0 Part 2.
      - name: HTTP 1.1
        description: HTTP binding supporting REST-style services.
      - name: UDDI
        description: WSDL documents are referenced in UDDI service registries.
      - name: WS-Policy
        description: Web services policy framework that annotates WSDL descriptions.
      - name: WS-Addressing
        description: Endpoint reference standards used with WSDL service endpoints.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
