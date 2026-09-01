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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Apache Openwhisk Agentic Access
  operation_count: 24
  slug: apache-openwhisk-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 6
apis:
- description: The Actions API from Apache OpenWhisk — 2 operation(s) for actions.
  name: Apache OpenWhisk Actions API
  slug: apache-openwhisk-actions-api
- description: The Activations API from Apache OpenWhisk — 2 operation(s) for activations.
  name: Apache OpenWhisk Activations API
  slug: apache-openwhisk-activations-api
- description: The Namespaces API from Apache OpenWhisk — 3 operation(s) for namespaces.
  name: Apache OpenWhisk Namespaces API
  slug: apache-openwhisk-namespaces-api
- description: The Packages API from Apache OpenWhisk — 2 operation(s) for packages.
  name: Apache OpenWhisk Packages API
  slug: apache-openwhisk-packages-api
- description: The Rules API from Apache OpenWhisk — 2 operation(s) for rules.
  name: Apache OpenWhisk Rules API
  slug: apache-openwhisk-rules-api
- description: The Triggers API from Apache OpenWhisk — 2 operation(s) for triggers.
  name: Apache OpenWhisk Triggers API
  slug: apache-openwhisk-triggers-api
artifact_total: 95
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache OpenWhisk REST Actions API
  slug: open-apache-openwhisk-actions-api
- collection_type: open
  name: Apache OpenWhisk REST Actions Activations API
  slug: open-apache-openwhisk-activations-api
- collection_type: open
  name: Apache OpenWhisk REST Actions Namespaces API
  slug: open-apache-openwhisk-namespaces-api
- collection_type: open
  name: Apache OpenWhisk REST Actions Packages API
  slug: open-apache-openwhisk-packages-api
- collection_type: open
  name: Apache OpenWhisk REST Actions Rules API
  slug: open-apache-openwhisk-rules-api
- collection_type: open
  name: Apache OpenWhisk REST Actions Triggers API
  slug: open-apache-openwhisk-triggers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-openwhisk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-openwhisk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-openwhisk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-openwhisk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/openwhisk
- group: docs
  title: ''
  type: Documentation
  url: https://openwhisk.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-openwhisk-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-openwhisk-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-openwhisk-context.jsonld
created: '2026-03-16'
description: Apache OpenWhisk is an open-source serverless cloud platform that executes functions in response to events at any scale. It supports multiple programming languages and provides a rich programming model for creating serverless APIs and event-driven applications.
examples:
- key_count: 9
  name: Apache Openwhisk Action Example
  slug: apache-openwhisk-action-example
- key_count: 4
  name: Apache Openwhisk Action Exec Example
  slug: apache-openwhisk-action-exec-example
- key_count: 3
  name: Apache Openwhisk Action Limits Example
  slug: apache-openwhisk-action-limits-example
- key_count: 4
  name: Apache Openwhisk Action Request Example
  slug: apache-openwhisk-action-request-example
- key_count: 11
  name: Apache Openwhisk Activation Example
  slug: apache-openwhisk-activation-example
- key_count: 1
  name: Apache Openwhisk Activation Ref Example
  slug: apache-openwhisk-activation-ref-example
- key_count: 4
  name: Apache Openwhisk Activation Response Example
  slug: apache-openwhisk-activation-response-example
- key_count: 5
  name: Apache Openwhisk Activation Summary Example
  slug: apache-openwhisk-activation-summary-example
- key_count: 2
  name: Apache Openwhisk Entity Ref Example
  slug: apache-openwhisk-entity-ref-example
- key_count: 2
  name: Apache Openwhisk Key Value Example
  slug: apache-openwhisk-key-value-example
- key_count: 3
  name: Apache Openwhisk Namespace Entities Example
  slug: apache-openwhisk-namespace-entities-example
- key_count: 3
  name: Apache Openwhisk Namespace Limits Example
  slug: apache-openwhisk-namespace-limits-example
- key_count: 9
  name: Apache Openwhisk Package Example
  slug: apache-openwhisk-package-example
- key_count: 2
  name: Apache Openwhisk Package Request Example
  slug: apache-openwhisk-package-request-example
- key_count: 7
  name: Apache Openwhisk Rule Example
  slug: apache-openwhisk-rule-example
- key_count: 2
  name: Apache Openwhisk Rule Request Example
  slug: apache-openwhisk-rule-request-example
- key_count: 7
  name: Apache Openwhisk Trigger Example
  slug: apache-openwhisk-trigger-example
- key_count: 2
  name: Apache Openwhisk Trigger Request Example
  slug: apache-openwhisk-trigger-request-example
features:
- description: Execute stateless functions in response to events without managing infrastructure
  name: Serverless Functions
- description: Supports Node.js, Python, Java, Go, PHP, Ruby, Swift, and custom Docker runtimes
  name: Multi-Language Support
- description: Named event channels that fire actions based on external events
  name: Event Triggers
- description: Compose multiple actions into sequential pipelines
  name: Action Sequences
- description: Pre-built integrations via /whisk.system namespace
  name: Package System
- description: Full REST API for managing all platform resources programmatically
  name: REST API
- description: Custom runtime support via Docker containers for any language
  name: Docker Actions
finops:
- name: Apache Openwhisk Finops
  service_category: API
  slug: apache-openwhisk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-openwhisk.png
integrations:
- description: Respond to Slack events and slash commands
  name: Slack
- description: Automate workflows based on GitHub repository events
  name: GitHub
- description: Process Kafka message stream events
  name: Apache Kafka
- description: React to CouchDB/Cloudant database changes
  name: Cloudant
- description: Available as IBM Cloud Functions on IBM Cloud
  name: IBM Cloud
- description: Deploy OpenWhisk on Kubernetes using Helm charts
  name: Kubernetes
json_schemas:
- name: ActionExec
  property_count: 4
  slug: apache-openwhisk-action-exec
- name: ActionLimits
  property_count: 3
  slug: apache-openwhisk-action-limits
- name: ActionRequest
  property_count: 4
  slug: apache-openwhisk-action-request
- name: Action
  property_count: 9
  slug: apache-openwhisk-action
- name: ActivationRef
  property_count: 1
  slug: apache-openwhisk-activation-ref
- name: ActivationResponse
  property_count: 4
  slug: apache-openwhisk-activation-response
- name: Activation
  property_count: 11
  slug: apache-openwhisk-activation
- name: ActivationSummary
  property_count: 5
  slug: apache-openwhisk-activation-summary
- name: EntityRef
  property_count: 2
  slug: apache-openwhisk-entity-ref
- name: KeyValue
  property_count: 2
  slug: apache-openwhisk-key-value
- name: NamespaceEntities
  property_count: 3
  slug: apache-openwhisk-namespace-entities
- name: NamespaceLimits
  property_count: 3
  slug: apache-openwhisk-namespace-limits
- name: PackageRequest
  property_count: 2
  slug: apache-openwhisk-package-request
- name: Package
  property_count: 9
  slug: apache-openwhisk-package
- name: RuleRequest
  property_count: 2
  slug: apache-openwhisk-rule-request
- name: Rule
  property_count: 7
  slug: apache-openwhisk-rule
- name: TriggerRequest
  property_count: 2
  slug: apache-openwhisk-trigger-request
- name: Trigger
  property_count: 7
  slug: apache-openwhisk-trigger
json_structures:
- name: Apache Openwhisk Action Exec Structure
  property_count: 4
  slug: apache-openwhisk-action-exec-structure
- name: Apache Openwhisk Action Limits Structure
  property_count: 3
  slug: apache-openwhisk-action-limits-structure
- name: Apache Openwhisk Action Request Structure
  property_count: 4
  slug: apache-openwhisk-action-request-structure
- name: Apache Openwhisk Action Structure
  property_count: 9
  slug: apache-openwhisk-action-structure
- name: Apache Openwhisk Activation Ref Structure
  property_count: 1
  slug: apache-openwhisk-activation-ref-structure
- name: Apache Openwhisk Activation Response Structure
  property_count: 4
  slug: apache-openwhisk-activation-response-structure
- name: Apache Openwhisk Activation Structure
  property_count: 11
  slug: apache-openwhisk-activation-structure
- name: Apache Openwhisk Activation Summary Structure
  property_count: 5
  slug: apache-openwhisk-activation-summary-structure
- name: Apache Openwhisk Entity Ref Structure
  property_count: 2
  slug: apache-openwhisk-entity-ref-structure
- name: Apache Openwhisk Key Value Structure
  property_count: 2
  slug: apache-openwhisk-key-value-structure
- name: Apache Openwhisk Namespace Entities Structure
  property_count: 3
  slug: apache-openwhisk-namespace-entities-structure
- name: Apache Openwhisk Namespace Limits Structure
  property_count: 3
  slug: apache-openwhisk-namespace-limits-structure
- name: Apache Openwhisk Package Request Structure
  property_count: 2
  slug: apache-openwhisk-package-request-structure
- name: Apache Openwhisk Package Structure
  property_count: 9
  slug: apache-openwhisk-package-structure
- name: Apache Openwhisk Rule Request Structure
  property_count: 2
  slug: apache-openwhisk-rule-request-structure
- name: Apache Openwhisk Rule Structure
  property_count: 7
  slug: apache-openwhisk-rule-structure
- name: Apache Openwhisk Trigger Request Structure
  property_count: 2
  slug: apache-openwhisk-trigger-request-structure
- name: Apache Openwhisk Trigger Structure
  property_count: 7
  slug: apache-openwhisk-trigger-structure
jsonld:
- class_count: 18
  name: Apache Openwhisk Context
  property_count: 37
  slug: apache-openwhisk-context
layout: provider
modified: '2026-05-19'
name: Apache OpenWhisk
nav: Providers
network: true
overview: 'Apache OpenWhisk publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Activations API, Namespaces API, and 3 more. Tagged areas include Cloud-Native, Event-Driven, Function-as-a-Service, Serverless, and Apache.


  The Apache OpenWhisk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache OpenWhisk''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Apache Openwhisk Plans Pricing
  plan_count: 3
  slug: apache-openwhisk-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Apache Openwhisk Rate Limits
  slug: apache-openwhisk-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache OpenWhisk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-openwhisk-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Apache OpenWhisk API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 8
  slug: apache-openwhisk-spectral-rules
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 20.5
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 23.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-openwhisk/refs/heads/main/screenshots/apache-openwhisk-2026-06-20T172129.png
security:
- kind: authentication
  name: Apache Openwhisk Authentication
  slug: apache-openwhisk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Openwhisk Domain Security
  slug: apache-openwhisk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Openwhisk Vulnerability Disclosure
  slug: apache-openwhisk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-openwhisk
tags:
- Cloud-Native
- Event-Driven
- Function-as-a-Service
- Serverless
- Apache
- Open-Source
- Functions
use_cases:
- description: Build loosely coupled microservices that respond to events
  name: Event-Driven Microservices
- description: Process sensor and device events at scale without infrastructure management
  name: IoT Data Processing
- description: Create REST APIs backed by serverless functions
  name: API Backend
- description: Run periodic jobs using alarm triggers
  name: Scheduled Tasks
- description: Handle Slack, GitHub, and other webhook events
  name: Chatbots & Webhooks
---
