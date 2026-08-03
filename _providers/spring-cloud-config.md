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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Spring Cloud Config Agentic Access
  operation_count: 13
  slug: spring-cloud-config-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 4
apis:
- description: Fetch application configuration
  name: Spring Cloud Config Configuration API
  slug: spring-cloud-config-configuration-api
- description: Encrypt and decrypt configuration values
  name: Spring Cloud Config Encryption API
  slug: spring-cloud-config-encryption-api
- description: Webhook and monitoring endpoints
  name: Spring Cloud Config Monitoring API
  slug: spring-cloud-config-monitoring-api
- description: Fetch resource files from the config repository
  name: Spring Cloud Config Resources API
  slug: spring-cloud-config-resources-api
artifact_total: 20
collections:
- collection_type: open
  name: Spring Cloud Config Server API
  slug: open-spring-cloud-config-server-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-cloud-config-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-cloud-config-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-cloud-config-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spring-cloud-config-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog.atom
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-cloud-config
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io/spring-cloud-config/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://spring.io/guides/gs/centralized-configuration/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spring-cloud/spring-cloud-config
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-cloud
- group: operate
  title: ''
  type: Issues
  url: https://github.com/spring-cloud/spring-cloud-config/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-cloud/spring-cloud-config/releases
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-cloud-config
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-config-server
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spring-cloud-config-vocabulary.yml
created: '2026-03-26'
description: Spring Cloud Config provides server-side and client-side support for externalized configuration in a distributed system. It offers a central place to manage external properties for applications across all environments, backed by Git, SVN, or filesystem repositories with support for encryption, decryption, and runtime refresh.
examples:
- key_count: 7
  name: Spring Cloud Config Encrypt Value Example
  slug: spring-cloud-config-encrypt-value-example
- key_count: 6
  name: Spring Cloud Config Get Environment Example
  slug: spring-cloud-config-get-environment-example
finops:
- name: Spring Cloud Config Finops
  service_category: API
  slug: spring-cloud-config-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spring-cloud-config.png
json_schemas:
- name: Spring Cloud Config Environment
  property_count: 6
  slug: spring-cloud-config-environment
- name: Spring Cloud Config Server Configuration
  property_count: 1
  slug: spring-cloud-config-server-configuration
json_structures:
- name: Spring Cloud Config Environment Structure
  property_count: 0
  slug: spring-cloud-config-environment-structure
jsonld:
- class_count: 5
  name: Spring Cloud Config Context
  property_count: 9
  slug: spring-cloud-config-context
layout: provider
modified: '2026-05-19'
name: Spring Cloud Config
nav: Providers
network: true
overview: 'Spring Cloud Config publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Encryption API, Monitoring API, and 1 more. Tagged areas include Configuration Management, Distributed Systems, Externalized Configuration, Git, and Java.


  The Spring Cloud Config catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Cloud Config''s developer surface includes authentication, engineering blog, documentation, getting-started guide, GitHub presence, release notes, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Spring Cloud Config Plans Pricing
  plan_count: 3
  slug: spring-cloud-config-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Spring Cloud Config Rate Limits
  slug: spring-cloud-config-rate-limits
rules:
- name: Spring Cloud Config API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-cloud-config-jsonschema-spectral-rules
- name: Spring Cloud Config API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: spring-cloud-config-rules
score:
  band: developing
  composite: 54.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.3
    developer_ergonomics: 32.6
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-cloud-config/refs/heads/main/screenshots/spring-cloud-config-2026-06-20T194410.png
security:
- kind: authentication
  name: Spring Cloud Config Authentication
  slug: spring-cloud-config-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Spring Cloud Config Domain Security
  slug: spring-cloud-config-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Cloud Config Vulnerability Disclosure
  slug: spring-cloud-config-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-cloud-config
tags:
- Configuration Management
- Distributed Systems
- Externalized Configuration
- Git
- Java
- Microservices
- Spring
- Spring Cloud
website: https://spring.io/projects/spring-cloud-config
---
