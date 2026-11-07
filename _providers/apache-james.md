---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
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
- baseURL: http://localhost:8000
  baseurl_source: spec
  description: System health monitoring
  name: Apache James Health Check API
  slug: apache-james-health-check-api
artifact_total: 71
collections:
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
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-james/overview
- group: commercial
  href: https://artifacts.apis.io/apache-james/plans/apache-james-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apache-james-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/apache-james/rate-limits/apache-james-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apache-james-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apache-james/finops/apache-james-finops.yml
  title: ''
  type: FinOps
  url: finops/apache-james-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.apache.org/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/james-project/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/apache-james/agentic-access/apache-james-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-james-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/apache-james/security/apache-james-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-james-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/apache-james/security/apache-james-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apache-james-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/apache-james/authentication/apache-james-authentication.yml
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
  href: https://artifacts.apis.io/apache-james/rules/apache-james-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/apache-james-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/apache-james/vocabulary/apache-james-vocabulary.yaml
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
- has_sources: false
  method: generated
  name: Apache James Finops
  primary_unit: request
  service_category: API
  slug: apache-james-finops
  template: true
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
overview: 'Apache James publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Domains API, Mailboxes API, MailQueues API, and 6 more. Tagged areas include Email, IMAP, Java, JMAP, and Mail Server.


  The Apache James catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache James'' developer surface includes authentication, documentation, getting-started guide, engineering blog, and 16 more developer resources.'
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
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Apache James — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-james-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 64
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
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 18.4
    contract_governance: 27.3
    contract_quality: 53.1
    developer_ergonomics: 34.5
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apache-james/apache-james-2026-06-20T172110.png
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
- Open Source
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
website: https://www.apache.org/
---
