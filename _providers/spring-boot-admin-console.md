---
access_model:
  confidence: medium
  label: Enterprise · Open access
  onboarding: open
  pricing: enterprise
  public: true
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Spring Boot Admin Console Agentic Access
  operation_count: 15
  slug: spring-boot-admin-console-agentic-access
  summary_line: 15 operations · 4 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Manage registered Spring Boot applications. Applications are logical groupings of instances sharing the same name and management URL base.
  name: Applications API
  slug: applications-api
- description: Manage individual application instances. Each instance represents a running Spring Boot application registered with the Admin server. Supports health monitoring, Actuator endpoint proxying, and deregi
  name: Instances API
  slug: instances-api
- description: Lifecycle event stream for application instances using Server-Sent Events (SSE). Events include status changes, registration, deregistration, and info updates.
  name: Events API
  slug: events-api
- description: Configure and trigger notification channels for application lifecycle events. Supports email, Slack, PagerDuty, OpsGenie, Microsoft Teams, Telegram, and custom webhook notifications.
  name: Notifications API
  slug: notifications-api
- description: Application registration and management
  name: Spring Boot Admin Console Applications API
  slug: spring-boot-admin-console-applications-api
- description: Instance lifecycle event stream
  name: Spring Boot Admin Console Events API
  slug: spring-boot-admin-console-events-api
- description: Application instance monitoring and management
  name: Spring Boot Admin Console Instances API
  slug: spring-boot-admin-console-instances-api
artifact_total: 21
collections:
- collection_type: open
  name: Spring Boot Admin Server API
  slug: open-spring-boot-admin-console
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-boot-admin-console-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.codecentric.de/feed/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/codecentric/spring-boot-admin
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/codecentric/spring-boot-admin/issues
- group: start
  title: ''
  type: Getting Started Guide
  url: https://codecentric.github.io/spring-boot-admin/current/#getting-started
- group: docs
  title: ''
  type: Reference Documentation
  url: https://codecentric.github.io/spring-boot-admin/current/
- group: other
  title: ''
  type: Maven Central
  url: https://mvnrepository.com/artifact/de.codecentric/spring-boot-admin
- group: commercial
  title: ''
  type: License
  url: https://github.com/codecentric/spring-boot-admin/blob/master/LICENSE
- group: operate
  title: ''
  type: Community
  url: https://gitter.im/codecentric/spring-boot-admin
created: '2024-01-01'
description: Spring Boot Admin is a community project by codecentric AG that provides a web-based administration UI for managing and monitoring Spring Boot applications. It visualizes Spring Boot Actuator endpoints in a graphical interface and provides application registration, health monitoring, log level management, metric graphs, instance lifecycle event tracking, and notification integrations (email, Slack, PagerDuty, OpsGenie, Hipchat, Teams, Telegram).
examples:
- key_count: 2
  name: Spring Boot Admin Console Get Instance Health Example
  slug: spring-boot-admin-console-get-instance-health-example
- key_count: 2
  name: Spring Boot Admin Console List Applications Example
  slug: spring-boot-admin-console-list-applications-example
- key_count: 2
  name: Spring Boot Admin Console Register Application Example
  slug: spring-boot-admin-console-register-application-example
finops:
- name: Spring Boot Admin Console Finops
  service_category: Developer Tools
  slug: spring-boot-admin-console-finops
image: https://raw.githubusercontent.com/codecentric/spring-boot-admin/master/spring-boot-admin-docs/src/site/resources/images/spring-boot-admin-logo.png
json_schemas:
- name: Spring Boot Admin Instance Event
  property_count: 6
  slug: spring-boot-admin-console-event
- name: Spring Boot Admin Instance
  property_count: 10
  slug: spring-boot-admin-console-instance
json_structures:
- name: Spring Boot Admin Console Structure
  property_count: 0
  slug: spring-boot-admin-console-structure
jsonld:
- class_count: 6
  name: Spring Boot Admin Console Context
  property_count: 22
  slug: spring-boot-admin-console-context
layout: provider
modified: '2026-05-19'
name: Spring Boot Admin Console
nav: Providers
network: true
overview: 'Spring Boot Admin Console publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Events API, and Instances API. Tagged areas include Actuator, Administration, Java, Microservices, and Monitoring.


  The Spring Boot Admin Console catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Boot Admin Console''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Spring Boot Admin Console Plans Pricing
  plan_count: 1
  slug: spring-boot-admin-console-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Spring Boot Admin Console Rate Limits
  slug: spring-boot-admin-console-rate-limits
rules:
- name: Spring Boot Admin Console API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-boot-admin-console-jsonschema-spectral-rules
- name: Spring Boot Admin Console API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: spring-boot-admin-console-rules
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.0
    developer_ergonomics: 6.5
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
slug: spring-boot-admin-console
tags:
- Actuator
- Administration
- Java
- Microservices
- Monitoring
- Spring Boot
---
