---
aid: apache-tapestry
name: Apache Tapestry
description: Apache Tapestry is a component-oriented framework for creating highly scalable web applications in Java. It provides a component-based development model with live class reloading, built-in Ajax support, type-safe URL generation, strong convention-over-configuration principles, and deep IDE integration. Tapestry applications are highly testable and work well with dependency injection via Tapestry IoC. It is maintained by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Component-Based
  - Java
  - Web Applications
  - Web Framework
  - Open Source
  - Ajax
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-tapestry/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-tapestry:apache-tapestry-component-api
    name: Apache Tapestry Component API
    description: The Tapestry Component API provides Java annotations and interfaces for building reusable web components. Components are defined by a Java class and an HTML template file. The API includes @Component, @Property, @Parameter, @InjectPage, @OnEvent annotations for component wiring, event handling, and page navigation. Tapestry also provides built-in components for forms, loops, conditionals, and Ajax event handling.
    humanURL: https://tapestry.apache.org/component-classes.html
    tags:
      - Java
      - Components
      - Web Framework
      - Ajax
    properties:
      - type: Documentation
        url: https://tapestry.apache.org/component-classes.html
      - type: APIReference
        url: https://tapestry.apache.org/apidocs/
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.tapestry
        title: Maven Java SDK
common:
  - type: GitHubRepository
    url: https://github.com/apache/tapestry-5
  - type: Documentation
    url: https://tapestry.apache.org/documentation.html
  - type: Portal
    url: https://tapestry.apache.org/
  - type: GettingStarted
    url: https://tapestry.apache.org/getting-started.html
  - type: ReleaseNotes
    url: https://github.com/apache/tapestry-5/releases
  - type: Support
    url: https://tapestry.apache.org/community.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Live Class Reloading
        description: Hot class reloading during development without server restart for faster iteration.
      - name: Component Model
        description: Pure component-based development with isolated component state and event handling.
      - name: Tapestry IoC
        description: Built-in inversion of control container with service binding and decoration.
      - name: Ajax Support
        description: Built-in Zone components for partial page updates and Ajax event handling.
      - name: Type-Safe URLs
        description: Type-safe URL generation with automatic parameter encoding and SEO-friendly URLs.
      - name: Asset Pipeline
        description: Automatic asset minification, versioning, and CDN support for JavaScript and CSS.
  - type: UseCases
    data:
      - name: Enterprise Java Web Applications
        description: Large-scale enterprise applications with reusable component libraries.
      - name: Form-Heavy Applications
        description: Complex data entry applications with server-side validation and type coercion.
      - name: Single-Page Application Backends
        description: Ajax-driven UIs with partial page updates via Tapestry Zone components.
  - type: Integrations
    data:
      - name: Spring Framework
        description: Spring IoC integration for service injection into Tapestry pages and components.
      - name: Hibernate
        description: Hibernate ORM integration for database access from Tapestry pages.
      - name: JPA
        description: JPA integration module for entity management in Tapestry applications.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
