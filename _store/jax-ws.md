---
aid: jax-ws
name: JAX-WS
description: JAX-WS (Java API for XML Web Services) is a Java standard for building and consuming SOAP-based XML web services. Originally specified as JSR 224 under the Java Community Process, JAX-WS is now part of Jakarta EE as Jakarta XML Web Services. It defines annotations and runtime APIs that allow developers to expose Java methods as SOAP web service operations and to generate Java client stubs from WSDL documents. Reference implementations include the Eclipse Metro project and Apache CXF.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Jakarta EE
  - Java
  - JAX-WS
  - SOAP
  - Standard
  - Web Services
  - XML
url: https://raw.githubusercontent.com/api-evangelist/jax-ws/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jax-ws:jakarta-xml-web-services
    name: Jakarta XML Web Services (JAX-WS)
    description: The Jakarta EE specification for XML web services, formerly JSR 224 JAX-WS. Defines annotations such as @WebService, @WebMethod, and @WebParam, as well as runtime APIs for SOAP-based web service providers and clients.
    humanURL: https://jakarta.ee/specifications/xml-web-services/
    tags:
      - Jakarta EE
      - SOAP
      - Specification
      - Web Services
    properties:
      - type: Specification
        url: https://jakarta.ee/specifications/xml-web-services/4.0/
      - type: Documentation
        url: https://jakarta.ee/specifications/xml-web-services/
      - type: GitHub
        url: https://github.com/jakartaee/xml-web-services
  - aid: jax-ws:eclipse-metro
    name: Eclipse Metro
    description: Eclipse Metro is the reference implementation of Jakarta XML Web Services (JAX-WS), providing a high-performance, extensible SOAP web services stack for Java applications.
    humanURL: https://projects.eclipse.org/projects/ee4j.metro
    tags:
      - Eclipse
      - Implementation
      - JAX-WS
      - Reference Implementation
    properties:
      - type: Documentation
        url: https://eclipse-ee4j.github.io/metro-jax-ws/
      - type: GitHub
        url: https://github.com/eclipse-ee4j/metro-jax-ws
  - aid: jax-ws:apache-cxf
    name: Apache CXF
    description: Apache CXF is an open source services framework that supports JAX-WS and JAX-RS, providing tooling and runtime support for SOAP, REST, and other web service protocols.
    humanURL: https://cxf.apache.org/
    tags:
      - Apache
      - CXF
      - JAX-WS
      - SOAP
    properties:
      - type: Documentation
        url: https://cxf.apache.org/docs/index.html
      - type: GitHub
        url: https://github.com/apache/cxf
common:
  - type: Website
    url: https://jakarta.ee/specifications/xml-web-services/
  - type: Documentation
    url: https://jakarta.ee/specifications/xml-web-services/
  - type: GitHub Organization
    url: https://github.com/jakartaee
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
