---
aid: apache-wicket
name: Apache Wicket
description: Apache Wicket is a component-based web application framework for Java that provides a clean separation of markup and logic with a stateful component model. It enables developers to build web applications using pure Java and HTML, without XML configuration. Wicket's stateful model stores component state on the server side while providing Ajax integration, type-safe page parameters, and deep testability. It is maintained by the Apache Software Foundation.
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
url: https://raw.githubusercontent.com/api-evangelist/apache-wicket/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-wicket:apache-wicket-component-api
    name: Apache Wicket Component API
    description: The Wicket Component API provides the core Java classes for building web UIs. Pages extend WebPage, components extend Panel, Form, Link, Button, and other base classes. The model system uses IModel<T> for type-safe data binding. The AjaxRequestTarget enables partial page updates. Wicket provides built-in components for forms (TextField, DropDownChoice, CheckBox), containers (RepeatingView, ListView, DataView), feedback, and navigation.
    humanURL: https://wicket.apache.org/learn/
    tags:
      - Java
      - Components
      - Web Framework
      - Ajax
    properties:
      - type: Documentation
        url: https://wicket.apache.org/learn/
      - type: APIReference
        url: https://ci.apache.org/projects/wicket/apidocs/10.x/
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.wicket
        title: Maven Java SDK
common:
  - type: GitHubRepository
    url: https://github.com/apache/wicket
  - type: Documentation
    url: https://wicket.apache.org/learn/
  - type: Portal
    url: https://wicket.apache.org/
  - type: GettingStarted
    url: https://wicket.apache.org/start/quickstart.html
  - type: ReleaseNotes
    url: https://github.com/apache/wicket/releases
  - type: Support
    url: https://wicket.apache.org/help/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Stateful Component Model
        description: Server-side stateful component model with automatic state serialization and clustering support.
      - name: Pure Java and HTML
        description: No JSP, no annotations on HTML, no XML mappings - just Java classes and plain HTML templates.
      - name: Type-Safe URLs
        description: Type-safe page parameters using PageParameters with automatic encoding/decoding.
      - name: Ajax Integration
        description: Built-in Ajax behaviors and components for partial page updates without JavaScript coding.
      - name: Testability
        description: WicketTester class provides comprehensive unit testing without a running servlet container.
      - name: Security
        description: Built-in CSRF protection, authorization strategies, and secure page parameters.
  - type: UseCases
    data:
      - name: Enterprise Java Web Applications
        description: Complex business applications with rich server-side state management.
      - name: Form-Intensive Applications
        description: Data entry applications with complex validation and type conversion.
      - name: Content Management Systems
        description: CMS backends with hierarchical content management and editorial workflows.
  - type: Integrations
    data:
      - name: Spring Framework
        description: SpringComponentInjector for Spring bean injection into Wicket components.
      - name: CDI
        description: CDI/Weld integration for Jakarta EE dependency injection in Wicket.
      - name: Hibernate
        description: Hibernate model integration for domain objects bound to Wicket components.
      - name: Bootstrap
        description: Wicket Bootstrap library for Bootstrap CSS integration.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
