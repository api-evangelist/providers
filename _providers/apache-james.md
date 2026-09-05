---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache James Agentic Access
  operation_count: 16
  slug: apache-james-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- description: The JMAP (JSON Meta Application Protocol) implementation in James provides a modern, efficient email protocol for synchronizing messages, mailboxes, contacts, and calendars for email clients.
  name: Apache James JMAP API
  slug: jmap-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: Email domain management
  name: Apache James Domains API
  slug: apache-james-domains-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: System health monitoring
  name: Apache James HealthCheck API
  slug: apache-james-healthcheck-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: Mailbox management
  name: Apache James Mailboxes API
  slug: apache-james-mailboxes-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: Mail queue management
  name: Apache James MailQueues API
  slug: apache-james-mailqueues-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: Mail repository management
  name: Apache James MailRepositories API
  slug: apache-james-mailrepositories-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: Storage and message quota management
  name: Apache James Quotas API
  slug: apache-james-quotas-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: Asynchronous task management
  name: Apache James Tasks API
  slug: apache-james-tasks-api
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: User account management
  name: Apache James Users API
  slug: apache-james-users-api
artifact_total: 72
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache James WebAdmin REST Domains API
  slug: open-apache-james-domains-api
- collection_type: open
  name: Apache James WebAdmin REST Domains HealthCheck API
  slug: open-apache-james-healthcheck-api
- collection_type: open
  name: Apache James WebAdmin REST Domains Mailboxes API
  slug: open-apache-james-mailboxes-api
- collection_type: open
  name: Apache James WebAdmin REST Domains MailQueues API
  slug: open-apache-james-mailqueues-api
- collection_type: open
  name: Apache James WebAdmin REST Domains MailRepositories API
  slug: open-apache-james-mailrepositories-api
- collection_type: open
  name: Apache James WebAdmin REST Domains Quotas API
  slug: open-apache-james-quotas-api
- collection_type: open
  name: Apache James WebAdmin REST Domains Tasks API
  slug: open-apache-james-tasks-api
- collection_type: open
  name: Apache James WebAdmin REST Domains Users API
  slug: open-apache-james-users-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/james-project/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-james-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-james-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-james-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-james-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/james-project
- group: docs
  title: ''
  type: Documentation
  url: https://james.apache.org/documentation.html
- group: start
  title: ''
  type: GettingStarted
  url: https://james.apache.org/server/quick-start.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: company
  title: ''
  type: Blog
  url: https://james.apache.org/blog/
- group: design
  title: ''
  type: Versioning
  url: https://james.apache.org/download.cgi
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-james-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-james-vocabulary.yaml
created: '2026-03-16'
description: Apache James (Java Apache Mail Enterprise Server) is a portable and enterprise-ready mail server built entirely in Java. It implements SMTP, IMAP, POP3, and JMAP protocols and provides a modular architecture with a comprehensive administration REST API and Cassandra-backed distributed deployment.
examples:
- key_count: 4
  name: Webadmin Rest Api Component Check Example
  slug: webadmin-rest-api-component-check-example
- key_count: 1
  name: Webadmin Rest Api Domain Request Example
  slug: webadmin-rest-api-domain-request-example
- key_count: 2
  name: Webadmin Rest Api Health Check Result Example
  slug: webadmin-rest-api-health-check-result-example
- key_count: 2
  name: Webadmin Rest Api Mail Repository Example
  slug: webadmin-rest-api-mail-repository-example
- key_count: 2
  name: Webadmin Rest Api Mailbox Example
  slug: webadmin-rest-api-mailbox-example
- key_count: 2
  name: Webadmin Rest Api Quota Example
  slug: webadmin-rest-api-quota-example
- key_count: 6
  name: Webadmin Rest Api Task Example
  slug: webadmin-rest-api-task-example
- key_count: 1
  name: Webadmin Rest Api User Example
  slug: webadmin-rest-api-user-example
- key_count: 2
  name: Webadmin Rest Api User Request Example
  slug: webadmin-rest-api-user-request-example
features:
- description: Full SMTP server implementation with TLS, DKIM, SPF, and DMARC support.
  name: SMTP Server
- description: IMAP4 server with full RFC compliance for email client access.
  name: IMAP Server
- description: Modern JMAP protocol implementation for efficient email synchronization.
  name: JMAP Support
- description: HTTP REST API for complete server administration without downtime.
  name: WebAdmin REST API
- description: Cassandra-backed distributed deployment for high availability.
  name: Distributed Architecture
- description: Pluggable architecture supporting custom protocols, storage, and authentication.
  name: Modular Design
- description: Persistent mail queuing with configurable retry strategies.
  name: Mail Queuing
- description: Per-user, per-domain, and global mailbox and message quota enforcement.
  name: Quota Management
finops:
- name: Apache James Finops
  service_category: API
  slug: apache-james-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-james.png
integrations:
- description: Distributed mail storage backend for high availability deployments.
  name: Apache Cassandra
- description: Event bus integration for distributed James deployments.
  name: Apache Kafka
- description: AMQP message queue for inter-node communication.
  name: RabbitMQ
- description: Full-text mail search indexing via Elasticsearch integration.
  name: Elasticsearch/OpenSearch
- description: LDAP authentication and directory integration for user management.
  name: OpenLDAP
json_schemas:
- name: ComponentCheck
  property_count: 4
  slug: webadmin-rest-api-component-check
- name: DomainRequest
  property_count: 1
  slug: webadmin-rest-api-domain-request
- name: HealthCheckResult
  property_count: 2
  slug: webadmin-rest-api-health-check-result
- name: MailRepository
  property_count: 2
  slug: webadmin-rest-api-mail-repository
- name: Mailbox
  property_count: 2
  slug: webadmin-rest-api-mailbox
- name: Quota
  property_count: 2
  slug: webadmin-rest-api-quota
- name: Task
  property_count: 6
  slug: webadmin-rest-api-task
- name: UserRequest
  property_count: 2
  slug: webadmin-rest-api-user-request
- name: User
  property_count: 1
  slug: webadmin-rest-api-user
json_structures:
- name: Webadmin Rest Api Component Check Structure
  property_count: 4
  slug: webadmin-rest-api-component-check-structure
- name: Webadmin Rest Api Domain Request Structure
  property_count: 1
  slug: webadmin-rest-api-domain-request-structure
- name: Webadmin Rest Api Health Check Result Structure
  property_count: 2
  slug: webadmin-rest-api-health-check-result-structure
- name: Webadmin Rest Api Mail Repository Structure
  property_count: 2
  slug: webadmin-rest-api-mail-repository-structure
- name: Webadmin Rest Api Mailbox Structure
  property_count: 2
  slug: webadmin-rest-api-mailbox-structure
- name: Webadmin Rest Api Quota Structure
  property_count: 2
  slug: webadmin-rest-api-quota-structure
- name: Webadmin Rest Api Task Structure
  property_count: 6
  slug: webadmin-rest-api-task-structure
- name: Webadmin Rest Api User Request Structure
  property_count: 2
  slug: webadmin-rest-api-user-request-structure
- name: Webadmin Rest Api User Structure
  property_count: 1
  slug: webadmin-rest-api-user-structure
jsonld:
- class_count: 9
  name: Apache James Webadmin Rest Api Context
  property_count: 19
  slug: apache-james-webadmin-rest-api-context
layout: provider
modified: '2026-05-19'
name: Apache James
nav: Providers
network: true
overview: 'Apache James publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Domains API, HealthCheck API, Mailboxes API, and 5 more. Tagged areas include Email, IMAP, Java, JMAP, and Mail Server.


  The Apache James catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache James'' developer surface includes authentication, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Apache James Plans Pricing
  plan_count: 3
  slug: apache-james-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Apache James Rate Limits
  slug: apache-james-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache James API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-james-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Apache James API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 9
  slug: apache-james-spectral-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 58.2
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-james/refs/heads/main/screenshots/apache-james-2026-06-20T172110.png
security:
- kind: authentication
  name: Apache James Authentication
  slug: apache-james-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache James Domain Security
  slug: apache-james-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache James Vulnerability Disclosure
  slug: apache-james-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-james
tags:
- Email
- IMAP
- Java
- JMAP
- Mail Server
- Open-Source
- SMTP
use_cases:
- description: Deploy a full-featured enterprise mail server with SMTP, IMAP, and JMAP.
  name: Enterprise Mail Server
- description: Migrate from other mail servers with full protocol compatibility.
  name: Mail Server Migration
- description: Build automated email pipelines using James mailet and matcher APIs.
  name: Automated Email Processing
- description: Deploy distributed James clusters with Cassandra and RabbitMQ for HA.
  name: High-Availability Mail
---
