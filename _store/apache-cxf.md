---
aid: apache-cxf
name: Apache CXF
description: Apache CXF is an open-source Java services framework governed by the Apache Software Foundation that helps build and develop web services using JAX-WS (SOAP) and JAX-RS (REST) frontend APIs. It supports contract-first (WSDL) and code-first development, full WS-* standards (WS-Security, WS-ReliableMessaging, WS-Addressing, WS-Policy), multiple transports (HTTP, JMS), and integrates with Spring Framework, OSGi/ServiceMix, and major Java EE servers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - JAX-RS
  - JAX-WS
  - Java
  - Open Source
  - REST
  - SOAP
  - WS-Security
  - Web Services
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-cxf:apache-cxf
    name: Apache CXF
    description: CXF provides Java APIs for building SOAP (JAX-WS) and REST (JAX-RS) web services with WSDL-first and code-first approaches, WS-* standards support, multiple data bindings (JAXB, Aegis, XMLBeans), pluggable transports (HTTP, JMS, In-VM), and code generation tools (wsdl2java, java2ws).
    humanURL: https://cxf.apache.org/docs/index.html
    tags:
      - CORBA
      - HTTP
      - JAX-RS
      - JAX-WS
      - Java
      - JMS
      - REST
      - SOAP
      - WSDL
      - WS-Security
      - Web Services
    properties:
      - type: Documentation
        url: https://cxf.apache.org/docs/index.html
      - type: GettingStarted
        url: https://cxf.apache.org/docs/a-simple-jax-ws-service.html
      - type: APIReference
        url: https://cxf.apache.org/javadoc/latest/
      - type: GitHubRepository
        url: https://github.com/apache/cxf
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.cxf/cxf-rt-frontend-jaxws
        title: cxf-rt-frontend-jaxws (Maven)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.cxf/cxf-rt-frontend-jaxrs
        title: cxf-rt-frontend-jaxrs (Maven)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.cxf/cxf-spring-boot-starter-jaxrs
        title: Spring Boot Starter JAX-RS (Maven)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.cxf/cxf-spring-boot-starter-jaxws
        title: Spring Boot Starter JAX-WS (Maven)
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-schema/apache-cxf-jaxrs-endpoint-schema.json
        title: Jaxrs Endpoint
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-schema/apache-cxf-jaxws-endpoint-schema.json
        title: Jaxws Endpoint
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-schema/apache-cxf-ws-security-config-schema.json
        title: Ws Security Config
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-structure/apache-cxf-jaxrs-endpoint-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-structure/apache-cxf-jaxws-endpoint-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-structure/apache-cxf-ws-security-config-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/json-ld/apache-cxf-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/examples/apache-cxf-jaxrs-endpoint-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/examples/apache-cxf-jaxws-endpoint-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/examples/apache-cxf-ws-security-config-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://cxf.apache.org/
  - type: Documentation
    url: https://cxf.apache.org/docs/index.html
  - type: GettingStarted
    url: https://cxf.apache.org/docs/a-simple-jax-ws-service.html
  - type: ReleaseNotes
    url: https://cxf.apache.org/download.html
  - type: GitHubRepository
    url: https://github.com/apache/cxf
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/apache-cxf
  - type: Features
    data:
      - name: JAX-WS SOAP Services
        description: Full JAX-WS implementation for building contract-first and code-first SOAP web services with WSDL support.
      - name: JAX-RS REST Services
        description: Full JAX-RS implementation for building RESTful services with JSON and XML support and OpenAPI integration.
      - name: WS-Security
        description: Comprehensive WS-Security support including XML Signature, XML Encryption, SAML tokens, Kerberos, and Username Tokens.
      - name: Multiple Transports
        description: Supports HTTP, Servlet, JMS, In-VM, and local transports for flexible service deployment.
      - name: Code Generation
        description: wsdl2java generates Java clients and server stubs from WSDL; java2ws generates WSDL and XSD from annotated Java classes.
      - name: Spring Integration
        description: Deep Spring Framework integration with Spring Boot starters for rapid JAX-WS and JAX-RS service development.
      - name: Data Bindings
        description: Supports JAXB 2.x, Aegis, XMLBeans, SDO, and JiBX data bindings for flexible XML/JSON marshalling.
      - name: WS-* Standards
        description: Implements WS-Addressing, WS-ReliableMessaging, WS-Policy, WS-MetadataExchange, and MTOM for enterprise-grade SOAP.
  - type: UseCases
    data:
      - name: Enterprise SOA
        description: Build and expose SOAP-based service-oriented architecture services in enterprise Java applications.
      - name: REST API Development
        description: Create RESTful APIs with JAX-RS annotations, OpenAPI documentation, and JSON/XML serialization.
      - name: Legacy SOAP Modernization
        description: Wrap or migrate legacy SOAP/WSDL services to REST/JSON while maintaining backward compatibility.
      - name: Spring Boot Microservices
        description: Use CXF Spring Boot starters to quickly expose JAX-RS or JAX-WS services in microservice architectures.
      - name: WS-Security Integration
        description: Secure web services with SAML, Kerberos, PKI, or WS-Username Tokens using CXF WSS4J integration.
  - type: Integrations
    data:
      - name: Spring Framework
        description: CXF provides deep Spring integration including Spring Boot starters for JAX-WS and JAX-RS.
      - name: Apache Karaf / OSGi
        description: CXF runs as OSGi bundles in Apache Karaf for modular service deployment.
      - name: Apache Tomcat / Jetty
        description: CXF services deploy as WAR files or embedded in Tomcat or Jetty servlet containers.
      - name: Apache WSS4J
        description: CXF uses WSS4J for WS-Security implementation including XML Signature and SAML.
      - name: OpenAPI / Swagger
        description: CXF integrates with Swagger/OpenAPI for automatic API documentation of JAX-RS services.
      - name: Apache Camel
        description: CXF provides a Camel component for integrating web services into Camel routing and mediation flows.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-cxf/refs/heads/main/vocabulary/apache-cxf-vocabulary.yaml
---
