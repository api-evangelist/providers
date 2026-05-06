---
aid: apache-sling
name: Apache Sling
description: Apache Sling is a RESTful web framework built on top of the Java Content Repository (JCR) standard. It maps HTTP requests to content resources using a resource-oriented URL decomposition model and uses scripts or servlets to render responses, supporting multiple scripting languages including HTL, JSP, Groovy, and server-side JavaScript. Apache Sling forms the foundation of Adobe Experience Manager (AEM) and is an Apache Software Foundation project with 300+ modular OSGi bundles.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Content Management
  - Java
  - JCR
  - OSGi
  - REST
  - Web Framework
  - Open Source
  - Adobe Experience Manager
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-sling/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-sling:apache-sling-resource-api
    name: Apache Sling Resource API
    description: 'The Sling Resource API provides RESTful access to JCR content repository nodes via HTTP. Every content node is addressable as a URL, supporting GET, POST, PUT, DELETE, and MOVE operations through the Sling Default GET/POST Servlets. Content is accessible in multiple formats via selector and extension: .json for structured data, .xml for XML export, .infinity.json for deep tree traversal, and .tidy.json for formatted output. The POST Servlet (SlingPostServlet) handles content creation, modification, deletion, move, copy, and import operations.'
    humanURL: https://sling.apache.org/documentation/the-sling-engine/resources.html
    tags:
      - REST
      - JCR
      - Content Management
      - Resources
      - Java
    properties:
      - type: Documentation
        url: https://sling.apache.org/documentation/the-sling-engine/resources.html
      - type: Documentation
        url: https://sling.apache.org/documentation/bundles/manipulating-content-the-slingpostservlet-servlets-post.html
  - aid: apache-sling:apache-sling-scripting-api
    name: Apache Sling Scripting API
    description: The Sling Scripting API enables server-side rendering through multiple scripting engines. Scripts are resolved from the content repository based on resource type and selectors, supporting HTL (HTML Template Language / Sightly), JSP (JavaServer Pages), Groovy, FreeMarker, Thymeleaf, and server-side JavaScript via Rhino. The ScriptEngine API allows integration of any JSR-223 compatible scripting language.
    humanURL: https://sling.apache.org/documentation/bundles/scripting.html
    tags:
      - Scripting
      - HTL
      - JSP
      - Groovy
      - Templates
      - Java
    properties:
      - type: Documentation
        url: https://sling.apache.org/documentation/bundles/scripting.html
      - type: Documentation
        url: https://sling.apache.org/documentation/bundles/scripting/scripting-htl.html
  - aid: apache-sling:apache-sling-event-api
    name: Apache Sling Event API
    description: The Sling Event API provides a job processing and eventing system built on OSGi EventAdmin. It supports distributed job queuing, scheduled job execution, event broadcasting across cluster nodes, and workflow triggering. The JobManager API enables job creation, monitoring, and management through a programmatic interface and also provides REST endpoints via the Web Console integration.
    humanURL: https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html
    tags:
      - Events
      - Jobs
      - Async
      - OSGi
      - Workflow
    properties:
      - type: Documentation
        url: https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html
common:
  - type: GitHubOrganization
    url: https://github.com/apache/sling-org-apache-sling-api
  - type: GitHubRepository
    url: https://github.com/apache/sling
  - type: Documentation
    url: https://sling.apache.org/documentation.html
  - type: Portal
    url: https://sling.apache.org/
  - type: GettingStarted
    url: https://sling.apache.org/documentation/getting-started.html
  - type: Blog
    url: https://sling.apache.org/news.html
  - type: Support
    url: https://sling.apache.org/project-information/mailing-lists.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: FAQ
    url: https://cwiki.apache.org/confluence/display/SLING/
  - type: SDK
    url: https://search.maven.org/search?q=org.apache.sling
    title: Maven Central Packages
  - type: Features
    data:
      - name: Resource-Oriented REST API
        description: Every JCR node is a REST resource accessible via URL with GET, POST, PUT, DELETE operations.
      - name: URL Decomposition
        description: Flexible URL decomposition into resource path, selectors, extension, and suffix for content negotiation.
      - name: SlingPostServlet
        description: Powerful POST servlet for content CRUD operations, supporting create, modify, delete, move, copy, and import.
      - name: Multi-Language Scripting
        description: Server-side rendering with HTL, JSP, Groovy, FreeMarker, Thymeleaf, and Rhino JavaScript.
      - name: OSGi Modular Architecture
        description: 300+ modular OSGi bundles with hot-deploy capability and dynamic configuration.
      - name: Resource Type Hierarchy
        description: Sling Resource Type system enables component inheritance and script resolution.
      - name: Event and Job Processing
        description: Distributed job queue and event system for asynchronous content processing.
      - name: Health Check Framework
        description: Extensible health check system for monitoring Sling instance components.
      - name: Replication and Distribution
        description: Content distribution bundles for replicating content between Sling instances.
  - type: UseCases
    data:
      - name: Content Management Systems
        description: Build REST-based CMS solutions with JCR-backed content repositories.
      - name: Adobe Experience Manager
        description: Foundation framework for AEM digital experience platform implementations.
      - name: Headless CMS
        description: Serve structured JSON content via Sling's resource API for headless front-end applications.
      - name: Web Application Framework
        description: Build OSGi-based Java web applications with RESTful resource routing.
      - name: Digital Asset Management
        description: Manage and serve digital assets stored in JCR with metadata and rendition support.
  - type: Integrations
    data:
      - name: Adobe Experience Manager
        description: Apache Sling is the foundational framework for Adobe Experience Manager (AEM).
      - name: Apache Jackrabbit Oak
        description: JCR implementation providing the content repository backend for Sling.
      - name: Apache Felix
        description: OSGi framework container that hosts Sling bundles and manages the service registry.
      - name: Apache Karaf
        description: OSGi runtime alternative for deploying Sling-based applications.
      - name: Maven
        description: Maven plugin (slingstart-maven-plugin) and Maven archetypes for Sling development.
      - name: Elasticsearch
        description: Search integration for indexing JCR content via Sling's indexing framework.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
