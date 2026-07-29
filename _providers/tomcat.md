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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tomcat Agentic Access
  operation_count: 21
  slug: tomcat-agentic-access
  summary_line: 21 operations · 1 acting
api_count: 8
apis:
- description: The Apache Tomcat JMX Proxy Servlet provides HTTP-based access to JMX MBeans for querying, getting, setting, and invoking operations on server management beans. Useful for server diagnostics, performa
  name: Apache Tomcat JMX Proxy API
  slug: tomcat-jmx-proxy-api
- description: Web application deployment and lifecycle management
  name: Apache Tomcat Applications API
  slug: tomcat-applications-api
- description: Server configuration management
  name: Apache Tomcat Configuration API
  slug: tomcat-configuration-api
- description: Server diagnostics and thread management
  name: Apache Tomcat Diagnostics API
  slug: tomcat-diagnostics-api
- description: JMX proxy operations for MBean access
  name: Apache Tomcat JMX API
  slug: tomcat-jmx-api
- description: Session management and statistics
  name: Apache Tomcat Sessions API
  slug: tomcat-sessions-api
- description: SSL/TLS certificate and cipher management
  name: Apache Tomcat SSL API
  slug: tomcat-ssl-api
- description: Server status and metrics
  name: Apache Tomcat Status API
  slug: tomcat-status-api
artifact_total: 21
collections:
- collection_type: open
  name: Apache Tomcat Manager API
  slug: open-tomcat-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tomcat-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tomcat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tomcat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tomcat-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tomcat.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://tomcat.apache.org/tomcat-10.1-doc/
- group: docs
  title: ''
  type: Manager API Documentation
  url: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html
- group: other
  title: ''
  type: Downloads
  url: https://tomcat.apache.org/download-10.cgi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tomcat
- group: other
  title: ''
  type: Apache Software Foundation
  url: https://www.apache.org/
- group: other
  title: ''
  type: Mailing Lists
  url: https://tomcat.apache.org/lists.html
- group: auth
  title: ''
  type: Security
  url: https://tomcat.apache.org/security.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://tomcat.apache.org/tomcat-10.1-doc/changelog.html
created: '2025-01-01'
description: Apache Tomcat is an open-source implementation of the Jakarta Servlet, Jakarta Server Pages, and other Jakarta EE technologies, providing a pure Java HTTP web server environment for running Java code. The Tomcat Manager application exposes an HTTP API for deploying, managing, and monitoring web applications. The JMX Proxy Servlet provides programmatic access to JMX MBeans for server diagnostics and configuration. Governed by the Apache Software Foundation.
examples:
- key_count: 2
  name: Tomcat Deploy Application Example
  slug: tomcat-deploy-application-example
- key_count: 2
  name: Tomcat List Applications Example
  slug: tomcat-list-applications-example
finops:
- name: Tomcat Finops
  service_category: API
  slug: tomcat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tomcat.png
json_structures:
- name: Tomcat Application Structure
  property_count: 0
  slug: tomcat-application-structure
jsonld:
- class_count: 9
  name: Tomcat Context
  property_count: 1
  slug: tomcat-context
layout: provider
modified: '2026-05-19'
name: Apache Tomcat
nav: Providers
network: true
overview: 'Apache Tomcat publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Configuration API, Diagnostics API, and 4 more. Tagged areas include Application Server, Java, Servlet Container, Web Server, and Open Source.


  The Apache Tomcat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache Tomcat''s developer surface includes authentication, documentation, changelog, and 10 more developer resources.'
plans:
- name: Tomcat Plans Pricing
  plan_count: 3
  slug: tomcat-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Tomcat Rate Limits
  slug: tomcat-rate-limits
rules:
- name: Apache Tomcat API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: tomcat-rules
score:
  band: developing
  composite: 43.9
  delta: -3.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.1
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 57.9
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tomcat/refs/heads/main/screenshots/tomcat-2026-06-20T195439.png
security:
- kind: authentication
  name: Tomcat Authentication
  slug: tomcat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tomcat Domain Security
  slug: tomcat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tomcat Vulnerability Disclosure
  slug: tomcat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tomcat
tags:
- Application Server
- Java
- Servlet Container
- Web Server
- Open Source
- Apache
website: https://tomcat.apache.org/
---
