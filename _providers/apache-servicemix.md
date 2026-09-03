---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Apache Servicemix Agentic Access
  operation_count: 9
  slug: apache-servicemix-agentic-access
  summary_line: 9 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://servicemix.example.com/api
  baseurl_source: spec
  description: The Bundles API from Apache ServiceMix — 2 operation(s) for bundles.
  name: Apache ServiceMix Bundles API
  slug: apache-servicemix-bundles-api
- baseURL: https://servicemix.example.com/api
  baseurl_source: spec
  description: The Endpoints API from Apache ServiceMix — 1 operation(s) for endpoints.
  name: Apache ServiceMix Endpoints API
  slug: apache-servicemix-endpoints-api
- baseURL: https://servicemix.example.com/api
  baseurl_source: spec
  description: The Messaging API from Apache ServiceMix — 1 operation(s) for messaging.
  name: Apache ServiceMix Messaging API
  slug: apache-servicemix-messaging-api
- baseURL: https://servicemix.example.com/api
  baseurl_source: spec
  description: The Routes API from Apache ServiceMix — 4 operation(s) for routes.
  name: Apache ServiceMix Routes API
  slug: apache-servicemix-routes-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache ServiceMix REST Bundles API
  slug: open-apache-servicemix-bundles-api
- collection_type: open
  name: Apache ServiceMix REST Bundles Endpoints API
  slug: open-apache-servicemix-endpoints-api
- collection_type: open
  name: Apache ServiceMix REST Bundles Messaging API
  slug: open-apache-servicemix-messaging-api
- collection_type: open
  name: Apache ServiceMix REST Bundles Routes API
  slug: open-apache-servicemix-routes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-servicemix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-servicemix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-servicemix-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/servicemix
- group: docs
  title: ''
  type: Documentation
  url: https://servicemix.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-servicemix-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-servicemix-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-servicemix-context.jsonld
created: '2026-03-16'
description: Apache ServiceMix is a flexible, open-source integration container that unifies the features and functionality of Apache ActiveMQ, Camel, CXF, and Karaf into a powerful runtime for building enterprise integration solutions.
examples:
- key_count: 6
  name: Apache Servicemix Bundle Example
  slug: apache-servicemix-bundle-example
- key_count: 2
  name: Apache Servicemix Bundle List Example
  slug: apache-servicemix-bundle-list-example
- key_count: 1
  name: Apache Servicemix Bundle State Request Example
  slug: apache-servicemix-bundle-state-request-example
- key_count: 4
  name: Apache Servicemix Endpoint Example
  slug: apache-servicemix-endpoint-example
- key_count: 1
  name: Apache Servicemix Endpoint List Example
  slug: apache-servicemix-endpoint-list-example
- key_count: 5
  name: Apache Servicemix Queue Example
  slug: apache-servicemix-queue-example
- key_count: 1
  name: Apache Servicemix Queue List Example
  slug: apache-servicemix-queue-list-example
- key_count: 7
  name: Apache Servicemix Route Example
  slug: apache-servicemix-route-example
- key_count: 1
  name: Apache Servicemix Route List Example
  slug: apache-servicemix-route-list-example
features:
- description: Apache Karaf-based OSGi container for modular deployment
  name: OSGi Container
- description: Rich integration routing with 300+ Camel components
  name: Apache Camel Routes
- description: SOAP and REST web service hosting with CXF
  name: Apache CXF
- description: Built-in JMS messaging with Apache ActiveMQ
  name: ActiveMQ Messaging
- description: Dynamic deployment of bundles and routes without restart
  name: Hot Deployment
- description: Support for EIP patterns including routing, transformation, and mediation
  name: Enterprise Patterns
finops:
- name: Apache Servicemix Finops
  service_category: API
  slug: apache-servicemix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-servicemix.png
integrations:
- description: Core integration framework providing routing and mediation
  name: Apache Camel
- description: SOAP and REST web service framework
  name: Apache CXF
- description: JMS message broker for asynchronous messaging
  name: Apache ActiveMQ
- description: OSGi container and runtime
  name: Apache Karaf
- description: Spring integration for bean management and transactions
  name: Spring Framework
json_schemas:
- name: BundleList
  property_count: 2
  slug: apache-servicemix-bundle-list
- name: Bundle
  property_count: 6
  slug: apache-servicemix-bundle
- name: BundleStateRequest
  property_count: 1
  slug: apache-servicemix-bundle-state-request
- name: EndpointList
  property_count: 1
  slug: apache-servicemix-endpoint-list
- name: Endpoint
  property_count: 4
  slug: apache-servicemix-endpoint
- name: QueueList
  property_count: 1
  slug: apache-servicemix-queue-list
- name: Queue
  property_count: 5
  slug: apache-servicemix-queue
- name: RouteList
  property_count: 1
  slug: apache-servicemix-route-list
- name: Route
  property_count: 7
  slug: apache-servicemix-route
json_structures:
- name: Apache Servicemix Bundle List Structure
  property_count: 2
  slug: apache-servicemix-bundle-list-structure
- name: Apache Servicemix Bundle State Request Structure
  property_count: 1
  slug: apache-servicemix-bundle-state-request-structure
- name: Apache Servicemix Bundle Structure
  property_count: 6
  slug: apache-servicemix-bundle-structure
- name: Apache Servicemix Endpoint List Structure
  property_count: 1
  slug: apache-servicemix-endpoint-list-structure
- name: Apache Servicemix Endpoint Structure
  property_count: 4
  slug: apache-servicemix-endpoint-structure
- name: Apache Servicemix Queue List Structure
  property_count: 1
  slug: apache-servicemix-queue-list-structure
- name: Apache Servicemix Queue Structure
  property_count: 5
  slug: apache-servicemix-queue-structure
- name: Apache Servicemix Route List Structure
  property_count: 1
  slug: apache-servicemix-route-list-structure
- name: Apache Servicemix Route Structure
  property_count: 7
  slug: apache-servicemix-route-structure
jsonld:
- class_count: 9
  name: Apache Servicemix Context
  property_count: 24
  slug: apache-servicemix-context
layout: provider
modified: '2026-05-19'
name: Apache ServiceMix
nav: Providers
network: true
overview: 'Apache ServiceMix publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bundles API, Endpoints API, Messaging API, and 1 more. Tagged areas include Enterprise Integration, ESB, Integration, Messaging, and OSGi.


  The Apache ServiceMix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache ServiceMix''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Apache Servicemix Plans Pricing
  plan_count: 3
  slug: apache-servicemix-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Apache Servicemix Rate Limits
  slug: apache-servicemix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache ServiceMix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-servicemix-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Apache ServiceMix API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 7
  slug: apache-servicemix-spectral-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 52.4
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-servicemix/refs/heads/main/screenshots/apache-servicemix-2026-06-20T172139.png
security:
- kind: domain-security
  name: Apache Servicemix Domain Security
  slug: apache-servicemix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Servicemix Vulnerability Disclosure
  slug: apache-servicemix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-servicemix
tags:
- Enterprise Integration
- ESB
- Integration
- Messaging
- OSGi
- Apache
- Open-Source
use_cases:
- description: Connect legacy SOAP services with modern REST APIs
  name: Legacy System Integration
- description: Route JMS messages between queues and topics
  name: Message Routing
- description: Orchestrate multiple services into composite workflows
  name: Service Orchestration
- description: Transform between HTTP, JMS, JDBC, and file protocols
  name: Protocol Mediation
---
