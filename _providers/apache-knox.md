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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apache Knox Agentic Access
  operation_count: 12
  slug: apache-knox-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: The Knox gateway proxies and secures access to Hadoop ecosystem services including HDFS WebHDFS, Hive, HBase REST, YARN, Oozie, Ambari, and Ranger with authentication and authorization enforcement.
  name: Apache Knox Gateway API
  slug: gateway-api
- baseURL: https://localhost:8443/gateway/admin
  baseurl_source: spec
  description: Simple descriptor management
  name: Apache Knox Descriptors API
  slug: apache-knox-descriptors-api
- baseURL: https://localhost:8443/gateway/admin
  baseurl_source: spec
  description: Provider configuration management
  name: Apache Knox Providers API
  slug: apache-knox-providers-api
- baseURL: https://localhost:8443/gateway/admin
  baseurl_source: spec
  description: Gateway topology management
  name: Apache Knox Topologies API
  slug: apache-knox-topologies-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Knox Admin REST Descriptors API
  slug: open-apache-knox-descriptors-api
- collection_type: open
  name: Apache Knox Admin REST Descriptors Providers API
  slug: open-apache-knox-providers-api
- collection_type: open
  name: Apache Knox Admin REST Descriptors Topologies API
  slug: open-apache-knox-topologies-api
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/knox/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/knox/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-knox-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-knox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-knox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-knox-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/knox
- group: docs
  title: ''
  type: Documentation
  url: https://knox.apache.org/books/knox-2-0-0/user-guide.html
- group: start
  title: ''
  type: GettingStarted
  url: https://knox.apache.org/books/knox-2-0-0/user-guide.html#Quick+Start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://knox.apache.org/books/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-knox-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-knox-vocabulary.yaml
created: '2026-03-16'
description: Apache Knox is a REST API and application gateway for the Apache Hadoop ecosystem. It provides a single access point for all REST and HTTP interactions with Apache Hadoop clusters, with authentication, authorization, SSO, and audit capabilities. Governed by the Apache Software Foundation under Apache 2.0.
examples:
- key_count: 6
  name: Admin Api Descriptor Example
  slug: admin-api-descriptor-example
- key_count: 1
  name: Admin Api Descriptor List Example
  slug: admin-api-descriptor-list-example
- key_count: 2
  name: Admin Api Knox Version Example
  slug: admin-api-knox-version-example
- key_count: 3
  name: Admin Api Topology Example
  slug: admin-api-topology-example
- key_count: 1
  name: Admin Api Topology List Example
  slug: admin-api-topology-list-example
features:
- description: Unified gateway for all Hadoop REST services eliminating direct cluster access.
  name: Single Access Point
- description: Kerberos, LDAP, OAuth2, and JWT authentication support.
  name: Authentication
- description: SAML2-based SSO and token-based federation across Hadoop services.
  name: SSO Integration
- description: Fine-grained authorization via Apache Ranger integration.
  name: Authorization
- description: SSL/TLS termination at the gateway for encrypted communication.
  name: SSL/TLS Termination
- description: Automatic service discovery via Ambari and Cloudera Manager integration.
  name: Service Discovery
- description: Dynamic topology configuration without gateway restarts.
  name: Topology Management
- description: Comprehensive audit logs for all gateway interactions.
  name: Audit Logging
finops:
- name: Apache Knox Finops
  service_category: API
  slug: apache-knox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-knox.png
integrations:
- description: WebHDFS REST API proxied and secured through Knox.
  name: Apache Hadoop HDFS
- description: Hive JDBC and REST API access via Knox gateway.
  name: Apache Hive
- description: HBase REST API proxied through Knox with authentication.
  name: Apache HBase
- description: Authorization policy enforcement via Ranger Knox plugin.
  name: Apache Ranger
- description: Ambari REST API proxied through Knox for cluster management.
  name: Apache Ambari
- type: Blog
  url: https://cwiki.apache.org/confluence/display/KNOX/News
json_schemas:
- name: DescriptorList
  property_count: 1
  slug: admin-api-descriptor-list
- name: Descriptor
  property_count: 6
  slug: admin-api-descriptor
- name: KnoxVersion
  property_count: 2
  slug: admin-api-knox-version
- name: TopologyList
  property_count: 1
  slug: admin-api-topology-list
- name: Topology
  property_count: 3
  slug: admin-api-topology
json_structures:
- name: Admin Api Descriptor List Structure
  property_count: 1
  slug: admin-api-descriptor-list-structure
- name: Admin Api Descriptor Structure
  property_count: 6
  slug: admin-api-descriptor-structure
- name: Admin Api Knox Version Structure
  property_count: 2
  slug: admin-api-knox-version-structure
- name: Admin Api Topology List Structure
  property_count: 1
  slug: admin-api-topology-list-structure
- name: Admin Api Topology Structure
  property_count: 3
  slug: admin-api-topology-structure
jsonld:
- class_count: 3
  name: Apache Knox Admin Api Descriptor Context
  property_count: 6
  slug: apache-knox-admin-api-descriptor-context
- class_count: 2
  name: Apache Knox Admin Api Knox Context
  property_count: 1
  slug: apache-knox-admin-api-knox-context
- class_count: 3
  name: Apache Knox Admin Api Topology Context
  property_count: 4
  slug: apache-knox-admin-api-topology-context
layout: provider
modified: '2026-05-19'
name: Apache Knox
nav: Providers
network: true
overview: 'Apache Knox publishes 3 APIs on the [APIs.io](https://apis.io/) network: Descriptors API, Providers API, and Topologies API. Tagged areas include API Gateway, Authentication, Hadoop, Open-Source, and Security.


  The Apache Knox catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Apache Knox''s developer surface includes authentication, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Apache Knox Plans Pricing
  plan_count: 3
  slug: apache-knox-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Apache Knox Rate Limits
  slug: apache-knox-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Knox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-knox-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Apache Knox API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 6
  slug: apache-knox-spectral-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 53.3
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 50.0
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-knox/refs/heads/main/screenshots/apache-knox-2026-06-20T172116.png
security:
- kind: authentication
  name: Apache Knox Authentication
  slug: apache-knox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Knox Domain Security
  slug: apache-knox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Knox Vulnerability Disclosure
  slug: apache-knox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-knox
tags:
- API Gateway
- Authentication
- Hadoop
- Open-Source
- Security
- SSO
use_cases:
- description: Secure and centralize access to all Hadoop REST APIs through Knox.
  name: Hadoop Cluster Security
- description: Provide secure REST access to EMR, HDInsight, and Dataproc clusters.
  name: Cloud Hadoop Access
- description: Enable single sign-on across Ambari, Hue, Spark UI, and other Hadoop UIs.
  name: Hadoop SSO
- description: Proxy WebHDFS, Hive JDBC/REST, HBase REST, and YARN REST through Knox.
  name: REST API Proxying
---
