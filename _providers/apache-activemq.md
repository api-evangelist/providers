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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apache Activemq Agentic Access
  operation_count: 5
  slug: apache-activemq-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 4
apis:
- description: The Jolokia JMX-HTTP bridge API provides HTTP access to JMX metrics and management operations for the ActiveMQ broker, enabling monitoring of broker health, queue depths, consumer counts, and other op
  name: Apache ActiveMQ Jolokia Management API
  slug: apache-activemq-jolokia-api
- description: The ActiveMQ Classic broker provides high-performance asynchronous messaging through multiple protocol interfaces including OpenWire, AMQP, STOMP, and MQTT. It includes a web-based management console,
  name: Apache ActiveMQ Broker
  slug: apache-activemq-broker
- description: Jolokia JMX-HTTP bridge for broker monitoring and management.
  name: Apache ActiveMQ Management API
  slug: apache-activemq-management-api
- description: Operations for producing and consuming messages from queues and topics.
  name: Apache ActiveMQ Messages API
  slug: apache-activemq-messages-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache ActiveMQ REST Management API
  slug: open-apache-activemq-management-api
- collection_type: open
  name: Apache ActiveMQ REST Management Messages API
  slug: open-apache-activemq-messages-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/activemq/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/activemq/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/activemq/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/activemq/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-activemq-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-activemq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-activemq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-activemq-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/activemq
- group: docs
  title: ''
  type: Documentation
  url: https://activemq.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://activemq.apache.org/components/classic/documentation/getting-started
- group: operate
  title: ''
  type: FAQ
  url: https://activemq.apache.org/faq
- group: operate
  title: ''
  type: Support
  url: https://activemq.apache.org/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: ChangeLog
  url: https://activemq.apache.org/components/classic/download
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/apache-activemq-rest-openapi.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-activemq-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rest-jolokia-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rest-jolokia-error-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-activemq-rest-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-activemq-vocabulary.yaml
created: '2026-03-16'
description: Apache ActiveMQ is an open-source, high-performance message broker written in Java, developed by the Apache Software Foundation. It implements the Jakarta Messaging (JMS) API and supports multiple messaging protocols including AMQP, STOMP, MQTT, OpenWire, and HTTP/WebSocket, enabling reliable asynchronous messaging between distributed applications and microservices. ActiveMQ provides features such as network of brokers, message persistence (KahaDB, JDBC), high availability, message scheduling, and a web console with REST and Jolokia management APIs.
examples:
- key_count: 4
  name: Rest Jolokia Error Example
  slug: rest-jolokia-error-example
- key_count: 4
  name: Rest Jolokia Response Example
  slug: rest-jolokia-response-example
features:
- description: Supports AMQP, STOMP, MQTT, OpenWire, JMS, Jakarta Messaging, HTTP, and WebSocket protocols for broad client compatibility.
  name: Multi-Protocol Support
- description: Provides KahaDB and JDBC-based message persistence options to ensure message durability across broker restarts.
  name: Message Persistence
- description: Enables distributed messaging topologies by linking multiple brokers in a network for load balancing and failover.
  name: Network of Brokers
- description: Supports shared storage and master-slave configurations for high availability deployments.
  name: High Availability
- description: Built-in message scheduling capabilities allow delayed or recurring message delivery.
  name: Message Scheduling
- description: HTTP-based REST API for producing and consuming messages from queues and topics without native JMS clients.
  name: REST Messaging API
- description: JMX-over-HTTP bridge via Jolokia for broker monitoring and management.
  name: Jolokia Management API
- description: HTML5 web-based management console accessible at /admin for queue and topic management, subscriber monitoring, and message browsing.
  name: Web Console
- description: Official Docker image apache/activemq-classic available on Docker Hub for containerized deployments.
  name: Docker Support
- description: ActiveMQ can be embedded directly into Java applications for in-process messaging.
  name: Embeddable Broker
finops:
- name: Apache Activemq Finops
  service_category: API
  slug: apache-activemq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-activemq.png
integrations:
- description: Deep integration with Spring and Spring Boot via spring-boot-starter-activemq.
  name: Spring Framework
- description: Native Apache Camel ActiveMQ component for enterprise integration patterns.
  name: Apache Camel
- description: Official Docker Hub image apache/activemq-classic for containerized deployments.
  name: Docker
- description: Deployable on Kubernetes using the official Docker image and StatefulSets.
  name: Kubernetes
- description: HTML5 management console integration via hawtio for advanced broker management.
  name: Hawtio
- description: Operational monitoring integration with RHQ for enterprise monitoring.
  name: RHQ
- description: OSGi integration with Apache Karaf for modular enterprise deployments.
  name: Apache Karaf
json_schemas:
- name: JolokiaError
  property_count: 4
  slug: rest-jolokia-error
- name: JolokiaResponse
  property_count: 4
  slug: rest-jolokia-response
json_structures:
- name: Rest Jolokia Error Structure
  property_count: 4
  slug: rest-jolokia-error-structure
- name: Rest Jolokia Response Structure
  property_count: 4
  slug: rest-jolokia-response-structure
jsonld:
- class_count: 2
  name: Apache Activemq Rest Context
  property_count: 6
  slug: apache-activemq-rest-context
layout: provider
modified: '2026-05-19'
name: Apache ActiveMQ
nav: Providers
network: true
overview: 'Apache ActiveMQ publishes 2 APIs on the [APIs.io](https://apis.io/) network: Management API and Messages API. Tagged areas include AMQP, Apache, Java, JMS, and Message Broker.


  The Apache ActiveMQ catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache ActiveMQ''s developer surface includes authentication, documentation, getting-started guide, FAQ, support, changelog, and 17 more developer resources.'
plans:
- name: Apache Activemq Plans Pricing
  plan_count: 3
  slug: apache-activemq-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Apache Activemq Rate Limits
  slug: apache-activemq-rate-limits
rules:
- name: Apache ActiveMQ API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-activemq-jsonschema-spectral-rules
- name: Apache ActiveMQ API Rules
  rule_count: 26
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 16
  slug: apache-activemq-spectral-rules
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 18.3
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-activemq/refs/heads/main/screenshots/apache-activemq-2026-06-20T172037.png
security:
- kind: authentication
  name: Apache Activemq Authentication
  slug: apache-activemq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Activemq Domain Security
  slug: apache-activemq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Activemq Vulnerability Disclosure
  slug: apache-activemq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-activemq
tags:
- AMQP
- Apache
- Java
- JMS
- Message Broker
- Messaging
- MQTT
- Open Source
- STOMP
use_cases:
- description: Decouple microservices using asynchronous message queues and topics for event-driven architectures.
  name: Microservices Messaging
- description: Connect disparate enterprise systems and applications using standard messaging protocols.
  name: Enterprise Integration
- description: Use MQTT protocol support for IoT device communication and telemetry data pipelines.
  name: IoT Messaging
- description: Distribute work items across consumer pools using competing consumers on queues.
  name: Workload Distribution
- description: Publish events to topics and fan out to multiple subscriber applications.
  name: Event Streaming
- description: Bridge legacy JMS-based applications with modern services using OpenWire and JMS API support.
  name: Legacy JMS Integration
---
