---
aid: apache-struts
name: Apache Struts
description: Apache Struts is a free, open-source, MVC framework for creating elegant, modern Java web applications. It provides a clean separation between the model, view, and controller layers with a powerful convention-over-configuration approach, interceptor-based AOP support, type-safe configuration, and built-in REST plugin. Apache Struts is maintained by the Apache Software Foundation and is widely used in enterprise Java web development.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Java
  - MVC
  - Web Applications
  - Web Framework
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-struts/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-struts:apache-struts-rest-plugin
    name: Apache Struts REST Plugin
    description: The Struts REST Plugin provides a convention-based REST API framework for building RESTful services. It maps HTTP methods to action methods (GET→index/show, POST→create, PUT→update, DELETE→destroy) and supports multiple content type negotiation for JSON, XML, and HTML responses via content type headers and URL extensions.
    humanURL: https://struts.apache.org/plugins/rest/
    tags:
      - REST
      - Java
      - MVC
      - JSON
      - XML
    properties:
      - type: Documentation
        url: https://struts.apache.org/plugins/rest/
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.struts2
        title: Maven Java SDK
common:
  - type: GitHubRepository
    url: https://github.com/apache/struts
  - type: Documentation
    url: https://struts.apache.org/documentation.html
  - type: Portal
    url: https://struts.apache.org/
  - type: GettingStarted
    url: https://struts.apache.org/getting-started/index.html
  - type: ReleaseNotes
    url: https://github.com/apache/struts/releases
  - type: Support
    url: https://struts.apache.org/support.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: FAQ
    url: https://struts.apache.org/faq.html
  - type: Features
    data:
      - name: Convention-Over-Configuration
        description: Zero-XML configuration with naming conventions for action and result mapping.
      - name: Interceptor Framework
        description: AOP-style interceptors for cross-cutting concerns like validation, logging, and security.
      - name: Type Conversion
        description: Automatic type conversion between HTTP request parameters and Java types.
      - name: OGNL Expression Language
        description: Object-Graph Navigation Language for dynamic data binding and expression evaluation.
      - name: Tiles Integration
        description: Template composition via Apache Tiles for reusable page layouts.
      - name: REST Plugin
        description: Convention-based REST API support with content type negotiation.
      - name: Spring Integration
        description: Native Spring Framework integration for dependency injection.
  - type: UseCases
    data:
      - name: Enterprise Java Web Applications
        description: Build large-scale Java web applications with clean MVC separation.
      - name: RESTful Web Services
        description: Create REST APIs using the Struts REST plugin with JSON/XML content negotiation.
      - name: Form-Based Applications
        description: Complex form processing with server-side validation and type conversion.
  - type: Integrations
    data:
      - name: Spring Framework
        description: Native Spring IoC container integration for dependency injection.
      - name: Hibernate
        description: Hibernate ORM integration for database persistence in action classes.
      - name: Apache Tiles
        description: Template composition framework for reusable page layouts and components.
      - name: FreeMarker
        description: FreeMarker template engine support as an alternative to JSP views.
      - name: Velocity
        description: Apache Velocity template engine for HTML view rendering.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
