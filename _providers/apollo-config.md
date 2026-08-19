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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Apollo Config Agentic Access
  operation_count: 18
  slug: apollo-config-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 5
apis:
- description: Application management
  name: Apollo Config Apps API
  slug: apollo-config-apps-api
- description: Cluster management
  name: Apollo Config Clusters API
  slug: apollo-config-clusters-api
- description: Configuration item management
  name: Apollo Config Items API
  slug: apollo-config-items-api
- description: Namespace management
  name: Apollo Config Namespaces API
  slug: apollo-config-namespaces-api
- description: Release and publish management
  name: Apollo Config Releases API
  slug: apollo-config-releases-api
artifact_total: 69
collections:
- collection_type: postman
  name: Apollo Config Open Apps API
  slug: postman-apollo-config-apps-api
- collection_type: postman
  name: Apollo Config Open Apps Clusters API
  slug: postman-apollo-config-clusters-api
- collection_type: postman
  name: Apollo Config Open Apps Items API
  slug: postman-apollo-config-items-api
- collection_type: postman
  name: Apollo Config Open Apps Namespaces API
  slug: postman-apollo-config-namespaces-api
- collection_type: postman
  name: Apollo Config Open Apps Releases API
  slug: postman-apollo-config-releases-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apollo Config Open Apps API
  slug: open-apollo-config-apps-api
- collection_type: open
  name: Apollo Config Open Apps Clusters API
  slug: open-apollo-config-clusters-api
- collection_type: open
  name: Apollo Config Open Apps Items API
  slug: open-apollo-config-items-api
- collection_type: open
  name: Apollo Config Open Apps Namespaces API
  slug: open-apollo-config-namespaces-api
- collection_type: open
  name: Apollo Config Open Apps Releases API
  slug: open-apollo-config-releases-api
- collection_type: open
  name: Apollo Config Open API
  slug: open-apollo-open-api
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apolloconfig/apollo/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apolloconfig/apollo/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apolloconfig/apollo/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apolloconfig/apollo/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apollo-config/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-config-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-config-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-config-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.apolloconfig.com/#/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apolloconfig.com/#/en/deployment/quick-start
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apolloconfig/apollo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apolloconfig
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apolloconfig/apollo/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/apolloconfig/apollo/issues
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/apolloconfig/apollo-java
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/apolloconfig/apollo.net
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/apolloconfig/agollo
- group: build
  title: Java Demo
  type: CodeExamples
  url: https://github.com/apolloconfig/apollo-demo-java
- group: build
  title: Use Cases
  type: CodeExamples
  url: https://github.com/apolloconfig/apollo-use-cases
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-ld/apollo-config-open-api-context.jsonld
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/apolloconfig/apollo-skills
created: '2026-03-26'
description: Apollo is a reliable, open-source configuration management system suitable for microservice configuration management scenarios, providing centralized configuration management, real-time updates, versioning, and multi-environment support. Originally developed by Ctrip, now maintained by the apolloconfig community under Apache 2.0 license.
examples:
- key_count: 10
  name: Apollo Open Api App Example
  slug: apollo-open-api-app-example
- key_count: 6
  name: Apollo Open Api Cluster Example
  slug: apollo-open-api-cluster-example
- key_count: 10
  name: Apollo Open Api Item Example
  slug: apollo-open-api-item-example
- key_count: 11
  name: Apollo Open Api Namespace Example
  slug: apollo-open-api-namespace-example
- key_count: 12
  name: Apollo Open Api Release Example
  slug: apollo-open-api-release-example
features:
- description: Centralize configuration for all microservices in one place with real-time push updates.
  name: Centralized Configuration Management
- description: Push configuration changes to all clients instantly without application restarts.
  name: Real-Time Configuration Updates
- description: Manage configurations across DEV, FAT, UAT, and PRO environments independently.
  name: Multi-Environment Support
- description: Track configuration changes with full version history and rollback capability.
  name: Versioning and History
- description: Gradually roll out configuration changes to a subset of instances.
  name: Gray Release Support
- description: Organize configurations into namespaces supporting properties, JSON, YAML, XML, and text formats.
  name: Namespace Management
- description: Manage configuration at the cluster level for multi-cluster deployments.
  name: Cluster Management
- description: REST API for programmatic configuration management and automation.
  name: Open API
- description: Kubernetes Operator for automated Apollo deployment in container environments.
  name: Kubernetes Operator
- description: Official Helm chart for Kubernetes deployments.
  name: Helm Chart Deployment
finops:
- name: Apollo Config Finops
  service_category: API
  slug: apollo-config-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-config.png
integrations:
- description: Official Java client library via apollo-java SDK.
  name: Java
- description: Official .NET client library via apollo.net SDK.
  name: .NET
- description: Go client library via agollo SDK.
  name: Go
- description: Apollo Operator and Helm chart for Kubernetes deployment.
  name: Kubernetes
- description: Spring Boot integration via Java SDK for auto-configuration refresh.
  name: Spring Boot
json_schemas:
- name: App
  property_count: 10
  slug: apollo-open-api-app
- name: Cluster
  property_count: 6
  slug: apollo-open-api-cluster
- name: Item
  property_count: 10
  slug: apollo-open-api-item
- name: Namespace
  property_count: 11
  slug: apollo-open-api-namespace
- name: Release
  property_count: 12
  slug: apollo-open-api-release
json_structures:
- name: Apollo Open Api App Structure
  property_count: 10
  slug: apollo-open-api-app-structure
- name: Apollo Open Api Cluster Structure
  property_count: 6
  slug: apollo-open-api-cluster-structure
- name: Apollo Open Api Item Structure
  property_count: 10
  slug: apollo-open-api-item-structure
- name: Apollo Open Api Namespace Structure
  property_count: 11
  slug: apollo-open-api-namespace-structure
- name: Apollo Open Api Release Structure
  property_count: 12
  slug: apollo-open-api-release-structure
jsonld:
- class_count: 6
  name: Apollo Config Open Api Context
  property_count: 22
  slug: apollo-config-open-api-context
layout: provider
modified: '2026-05-19'
name: Apollo Config
nav: Providers
network: true
overview: 'Apollo Config publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Clusters API, Items API, and 2 more. Tagged areas include Apache 2.0, Configuration Management, Ctrip, Distributed Systems, and Java.


  The Apollo Config catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apollo Config''s developer surface includes authentication, documentation, getting-started guide, release notes, support, code examples, and 15 more developer resources.'
plans:
- name: Apollo Config Plans Pricing
  plan_count: 3
  slug: apollo-config-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 5
  name: Apollo Config Rate Limits
  slug: apollo-config-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apollo Config API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apollo-config-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  delta: -5.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 65.5
    developer_ergonomics: 66.7
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/screenshots/apollo-config-2026-06-20T172307.png
security:
- kind: authentication
  name: Apollo Config Authentication
  slug: apollo-config-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apollo Config Domain Security
  slug: apollo-config-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 9
skills:
- name: apollo-community-review
  slug: apollo-community-review
- name: apollo-contributor-promotion-review
  slug: apollo-contributor-promotion-review
- name: apollo-helm-chart-release
  slug: apollo-helm-chart-release
- name: apollo-issue-review
  slug: apollo-issue-review
- name: apollo-issue-to-pr
  slug: apollo-issue-to-pr
- name: apollo-java-release
  slug: apollo-java-release
- name: apollo-pr-review
  slug: apollo-pr-review
- name: apollo-quick-start-release
  slug: apollo-quick-start-release
- name: apollo-release
  slug: apollo-release
slug: apollo-config
tags:
- Apache 2.0
- Configuration Management
- Ctrip
- Distributed Systems
- Java
- Microservices
- Open Source
- Real-Time Configuration
use_cases:
- description: Manage centralized configuration for distributed microservice architectures.
  name: Microservice Configuration
- description: Maintain separate configurations for development, testing, staging, and production.
  name: Multi-Environment Configuration
- description: Update application configuration at runtime without redeployment.
  name: Dynamic Configuration Updates
- description: Track who changed what configuration and when with full audit trail.
  name: Configuration Audit
- description: Manage configuration for containerized applications deployed on Kubernetes.
  name: Kubernetes Configuration Management
---
