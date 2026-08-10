---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apache Tomcat Agentic Access
  operation_count: 19
  slug: apache-tomcat-agentic-access
  summary_line: 19 operations · 1 acting
api_count: 5
apis:
- description: 'The Tomcat Manager application provides an HTTP text protocol API for deploying, undeploying, starting, stopping, and reloading web applications remotely. Key endpoints include: /manager/text/list (li'
  name: Apache Tomcat Manager API
  slug: apache-tomcat-manager-api
- description: The Tomcat JMX API exposes management and monitoring beans for Connectors, Engines, Hosts, Contexts, Sessions, DataSources, thread pools, and memory via Java Management Extensions. JMX can be accessed
  name: Apache Tomcat JMX API
  slug: apache-tomcat-jmx-api
- description: Manage deployed web applications
  name: Apache Tomcat applications API
  slug: apache-tomcat-applications-api
- description: Server, JVM, and SSL/TLS information
  name: Apache Tomcat server API
  slug: apache-tomcat-server-api
- description: Inspect and expire HTTP sessions
  name: Apache Tomcat sessions API
  slug: apache-tomcat-sessions-api
artifact_total: 29
collections:
- collection_type: open
  name: Apache Tomcat Manager Text API
  slug: open-apache-tomcat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-tomcat-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-tomcat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-tomcat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-tomcat-authentication.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tomcat
- group: docs
  title: ''
  type: Documentation
  url: https://tomcat.apache.org/tomcat-10.1-doc/
- group: start
  title: ''
  type: Portal
  url: https://tomcat.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://tomcat.apache.org/tomcat-10.1-doc/setup.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://tomcat.apache.org/tomcat-10.1-doc/changelog.html
- group: operate
  title: ''
  type: Support
  url: https://tomcat.apache.org/lists.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2024-01-15'
description: Apache Tomcat is an open-source implementation of the Java Servlet, JavaServer Pages (JSP), Java Expression Language, and Java WebSocket technologies. It provides a pure Java HTTP web server and servlet container for hosting Java web applications. Tomcat exposes management APIs via the Manager application (HTTP text protocol), JMX for monitoring, and a Virtual Host Manager for configuration management. It is maintained by the Apache Software Foundation and is one of the most widely deployed Java application servers.
features:
- description: Jakarta Servlet 6.0 (formerly Java EE) compliant servlet container.
  name: Servlet Container
- description: JavaServer Pages compiler and runtime engine for dynamic HTML generation.
  name: JSP Engine
- description: Jakarta WebSocket 2.1 implementation for full-duplex browser-server communication.
  name: WebSocket Support
- description: HTTP/2 multiplexing and server push via APR/Native connector.
  name: HTTP/2 Support
- description: Built-in SSL/TLS support via JSSE or APR/OpenSSL connectors.
  name: SSL/TLS Termination
- description: DBCP2-based database connection pool management via JNDI DataSource.
  name: Connection Pooling
- description: Session replication across Tomcat cluster nodes via DeltaManager or BackupManager.
  name: Clustering
finops:
- name: Apache Tomcat Finops
  service_category: API
  slug: apache-tomcat-finops
image: https://tomcat.apache.org/res/images/tomcat.png
integrations:
- description: Embedded Tomcat as the default servlet container in Spring Boot applications.
  name: Spring Boot
- description: mod_jk and mod_proxy_ajp for load balancing between Apache httpd and Tomcat.
  name: Apache HTTP Server
- description: Nginx reverse proxy for Tomcat with SSL termination and load balancing.
  name: Nginx
- description: JMX Exporter for exposing Tomcat metrics in Prometheus format.
  name: Prometheus
- description: Official Docker image for containerized Tomcat deployment.
  name: Docker
layout: provider
modified: '2026-04-19'
name: Apache Tomcat
nav: Providers
network: true
overview: 'Apache Tomcat publishes 3 APIs on the [APIs.io](https://apis.io/) network: applications API, server API, and sessions API. Tagged areas include Application Server, Java, JSP, Open Source, and Servlet.


  Apache Tomcat''s developer surface includes authentication, documentation, developer portal, getting-started guide, release notes, support, and 5 more developer resources.'
plans:
- name: Apache Tomcat Plans Pricing
  plan_count: 3
  slug: apache-tomcat-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Apache Tomcat Rate Limits
  slug: apache-tomcat-rate-limits
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.5
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-tomcat/refs/heads/main/screenshots/apache-tomcat-2026-06-20T172155.png
security:
- kind: authentication
  name: Apache Tomcat Authentication
  slug: apache-tomcat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Tomcat Domain Security
  slug: apache-tomcat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Tomcat Vulnerability Disclosure
  slug: apache-tomcat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-tomcat
tags:
- Application Server
- Java
- JSP
- Open Source
- Servlet
- Web Server
use_cases:
- description: Deploy and host Java Servlet/JSP web applications.
  name: Java Web Application Hosting
- description: Host REST API backends built with Spring MVC, JAX-RS, or plain servlets.
  name: API Gateway Backend
- description: Embedded Tomcat in Spring Boot for microservices deployment.
  name: Microservices Container
- description: Host Java EE applications during cloud migration.
  name: Legacy Application Migration
website: https://tomcat.apache.org/
---
