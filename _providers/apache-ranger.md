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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Ranger Agentic Access
  operation_count: 13
  slug: apache-ranger-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 5
apis:
- description: The Audit API from Apache Ranger — 1 operation(s) for audit.
  name: Apache Ranger Audit API
  slug: apache-ranger-audit-api
- description: The Groups API from Apache Ranger — 1 operation(s) for groups.
  name: Apache Ranger Groups API
  slug: apache-ranger-groups-api
- description: The Policies API from Apache Ranger — 2 operation(s) for policies.
  name: Apache Ranger Policies API
  slug: apache-ranger-policies-api
- description: The Services API from Apache Ranger — 2 operation(s) for services.
  name: Apache Ranger Services API
  slug: apache-ranger-services-api
- description: The Users API from Apache Ranger — 1 operation(s) for users.
  name: Apache Ranger Users API
  slug: apache-ranger-users-api
artifact_total: 76
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Ranger REST Audit API
  slug: open-apache-ranger-audit-api
- collection_type: open
  name: Apache Ranger REST Audit Groups API
  slug: open-apache-ranger-groups-api
- collection_type: open
  name: Apache Ranger REST Audit Policies API
  slug: open-apache-ranger-policies-api
- collection_type: open
  name: Apache Ranger REST Audit Services API
  slug: open-apache-ranger-services-api
- collection_type: open
  name: Apache Ranger REST Audit Users API
  slug: open-apache-ranger-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-ranger-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-ranger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-ranger-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-ranger-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/ranger
- group: docs
  title: ''
  type: Documentation
  url: https://ranger.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-ranger-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-ranger-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-ranger-context.jsonld
created: '2026-03-16'
description: Apache Ranger is a framework to enable, monitor, and manage comprehensive data security across the Hadoop platform. It provides centralized security administration for fine-grained authorization policies across Hadoop ecosystem components.
examples:
- key_count: 2
  name: Apache Ranger Access Type Example
  slug: apache-ranger-access-type-example
- key_count: 12
  name: Apache Ranger Audit Entry Example
  slug: apache-ranger-audit-entry-example
- key_count: 2
  name: Apache Ranger Audit List Example
  slug: apache-ranger-audit-list-example
- key_count: 2
  name: Apache Ranger Group List Example
  slug: apache-ranger-group-list-example
- key_count: 9
  name: Apache Ranger Policy Example
  slug: apache-ranger-policy-example
- key_count: 4
  name: Apache Ranger Policy Item Example
  slug: apache-ranger-policy-item-example
- key_count: 4
  name: Apache Ranger Policy List Example
  slug: apache-ranger-policy-list-example
- key_count: 3
  name: Apache Ranger Policy Resource Example
  slug: apache-ranger-policy-resource-example
- key_count: 4
  name: Apache Ranger Ranger Group Example
  slug: apache-ranger-ranger-group-example
- key_count: 6
  name: Apache Ranger Ranger Service Example
  slug: apache-ranger-ranger-service-example
- key_count: 7
  name: Apache Ranger Ranger User Example
  slug: apache-ranger-ranger-user-example
- key_count: 2
  name: Apache Ranger Service List Example
  slug: apache-ranger-service-list-example
- key_count: 2
  name: Apache Ranger User List Example
  slug: apache-ranger-user-list-example
features:
- description: Manage security policies for all Hadoop services from a single interface
  name: Centralized Policy Management
- description: Column-level, row-level, and data masking policies for Hive and HBase
  name: Fine-Grained Access Control
- description: Context-aware policies based on user attributes and tag classifications
  name: Attribute-Based Access Control
- description: Comprehensive audit trail of all resource access events
  name: Audit Logging
- description: Supports HDFS, Hive, HBase, Kafka, Storm, Solr, Kudu, and more
  name: Multi-Service Support
- description: Sync users and groups from Active Directory or LDAP
  name: LDAP/AD Integration
- description: Delegate policy administration with security zones
  name: Security Zones
finops:
- name: Apache Ranger Finops
  service_category: API
  slug: apache-ranger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-ranger.png
integrations:
- description: Native HDFS and YARN authorization integration
  name: Apache Hadoop
- description: Column-level and row-level security for Hive queries
  name: Apache Hive
- description: Table and column family security for HBase
  name: Apache HBase
- description: Topic-level authorization for Kafka producers and consumers
  name: Apache Kafka
- description: Tag-based policies using Atlas data classifications
  name: Apache Atlas
json_schemas:
- name: AccessType
  property_count: 2
  slug: apache-ranger-access-type
- name: AuditEntry
  property_count: 12
  slug: apache-ranger-audit-entry
- name: AuditList
  property_count: 2
  slug: apache-ranger-audit-list
- name: GroupList
  property_count: 2
  slug: apache-ranger-group-list
- name: PolicyItem
  property_count: 4
  slug: apache-ranger-policy-item
- name: PolicyList
  property_count: 4
  slug: apache-ranger-policy-list
- name: PolicyResource
  property_count: 3
  slug: apache-ranger-policy-resource
- name: Policy
  property_count: 9
  slug: apache-ranger-policy
- name: RangerGroup
  property_count: 4
  slug: apache-ranger-ranger-group
- name: RangerService
  property_count: 6
  slug: apache-ranger-ranger-service
- name: RangerUser
  property_count: 7
  slug: apache-ranger-ranger-user
- name: ServiceList
  property_count: 2
  slug: apache-ranger-service-list
- name: UserList
  property_count: 2
  slug: apache-ranger-user-list
json_structures:
- name: Apache Ranger Access Type Structure
  property_count: 2
  slug: apache-ranger-access-type-structure
- name: Apache Ranger Audit Entry Structure
  property_count: 12
  slug: apache-ranger-audit-entry-structure
- name: Apache Ranger Audit List Structure
  property_count: 2
  slug: apache-ranger-audit-list-structure
- name: Apache Ranger Group List Structure
  property_count: 2
  slug: apache-ranger-group-list-structure
- name: Apache Ranger Policy Item Structure
  property_count: 4
  slug: apache-ranger-policy-item-structure
- name: Apache Ranger Policy List Structure
  property_count: 4
  slug: apache-ranger-policy-list-structure
- name: Apache Ranger Policy Resource Structure
  property_count: 3
  slug: apache-ranger-policy-resource-structure
- name: Apache Ranger Policy Structure
  property_count: 9
  slug: apache-ranger-policy-structure
- name: Apache Ranger Ranger Group Structure
  property_count: 4
  slug: apache-ranger-ranger-group-structure
- name: Apache Ranger Ranger Service Structure
  property_count: 6
  slug: apache-ranger-ranger-service-structure
- name: Apache Ranger Ranger User Structure
  property_count: 7
  slug: apache-ranger-ranger-user-structure
- name: Apache Ranger Service List Structure
  property_count: 2
  slug: apache-ranger-service-list-structure
- name: Apache Ranger User List Structure
  property_count: 2
  slug: apache-ranger-user-list-structure
jsonld:
- class_count: 13
  name: Apache Ranger Context
  property_count: 42
  slug: apache-ranger-context
layout: provider
modified: '2026-05-19'
name: Apache Ranger
nav: Providers
network: true
overview: 'Apache Ranger publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Groups API, Policies API, and 2 more. Tagged areas include Access Control, Authorization, Hadoop, Policy Management, and Security.


  The Apache Ranger catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Ranger''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Apache Ranger Plans Pricing
  plan_count: 3
  slug: apache-ranger-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Apache Ranger Rate Limits
  slug: apache-ranger-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Ranger API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-ranger-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Apache Ranger API Rules
  rule_count: 15
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 9
  slug: apache-ranger-spectral-rules
score:
  band: thin
  composite: 35.1
  delta: -3.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 62.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-ranger/refs/heads/main/screenshots/apache-ranger-2026-06-20T172136.png
security:
- kind: authentication
  name: Apache Ranger Authentication
  slug: apache-ranger-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Ranger Domain Security
  slug: apache-ranger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Ranger Vulnerability Disclosure
  slug: apache-ranger-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-ranger
tags:
- Access Control
- Authorization
- Hadoop
- Policy Management
- Security
- Apache
- Open Source
use_cases:
- description: Enforce column and row-level security on Hadoop data lake
  name: Data Lake Security
- description: Meet GDPR, HIPAA, and SOX requirements with audit logs and masking
  name: Regulatory Compliance
- description: Isolate access between teams and business units
  name: Multi-Tenant Authorization
- description: Control which applications can produce and consume Kafka topics
  name: Kafka Topic Authorization
---
