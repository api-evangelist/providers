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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spring Batch 51 Agentic Access
  operation_count: 8
  slug: spring-batch-51-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Spring Boot Actuator-based monitoring endpoints for Spring Batch 5.1 applications providing job health, execution status, and Micrometer metrics visibility.
  name: Spring Batch 5.1 Actuator Monitoring
  slug: spring-batch-51-actuator-monitoring
- baseURL: https://github.com/spring-projects/spring-batch
  baseurl_source: declared
  description: Batch job execution management and monitoring
  name: Spring Batch 5.1 Batch Jobs API
  slug: spring-batch-51-batch-jobs-api
- baseURL: https://github.com/spring-projects/spring-batch
  baseurl_source: declared
  description: Application and component health checks
  name: Spring Batch 5.1 Health API
  slug: spring-batch-51-health-api
- baseURL: https://github.com/spring-projects/spring-batch
  baseurl_source: declared
  description: Micrometer-based application metrics
  name: Spring Batch 5.1 Metrics API
  slug: spring-batch-51-metrics-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spring Batch 5.1 Actuator Batch Jobs API
  slug: open-spring-batch-51-batch-jobs-api
- collection_type: open
  name: Spring Batch 5.1 Actuator Batch Jobs Health API
  slug: open-spring-batch-51-health-api
- collection_type: open
  name: Spring Batch 5.1 Actuator Batch Jobs Metrics API
  slug: open-spring-batch-51-metrics-api
- collection_type: open
  name: Spring Batch 5.1 Actuator API
  slug: open-spring-batch-51
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spring-projects/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spring-projects/spring-batch/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-batch-51-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-batch-51-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-batch-51-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/batch
- group: operate
  title: ''
  type: Support
  url: https://spring.io/support
- group: operate
  title: ''
  type: Forums
  url: https://stackoverflow.com/questions/tagged/spring-batch
- group: build
  title: ''
  type: GitHubIssues
  url: https://github.com/spring-projects/spring-batch/issues
- group: other
  title: ''
  type: Maven Central
  url: https://search.maven.org/search?q=g:org.springframework.batch
created: '2024-01-15'
description: Spring Batch 5.1 is the latest enterprise batch processing framework release for the Spring ecosystem. Designed to enable development of robust batch applications vital for daily operations of enterprise systems. Version 5.1 delivers Micrometer metrics, virtual thread support (Java 21), and enhanced chunk-oriented processing with retry, skip, and restart capabilities.
examples:
- key_count: 2
  name: Spring Batch 51 Get Health Example
  slug: spring-batch-51-get-health-example
- key_count: 2
  name: Spring Batch 51 Get Metric Example
  slug: spring-batch-51-get-metric-example
- key_count: 2
  name: Spring Batch 51 List Job Executions Example
  slug: spring-batch-51-list-job-executions-example
finops:
- name: Spring Batch 51 Finops
  service_category: API
  slug: spring-batch-51-finops
image: https://spring.io/img/projects/spring-batch.svg
json_schemas:
- name: Spring Batch Job Execution
  property_count: 13
  slug: spring-batch-51-job-execution
- name: Spring Batch Job Parameters
  property_count: 0
  slug: spring-batch-51-job-parameters
json_structures:
- name: Spring Batch 51 Job Execution Structure
  property_count: 0
  slug: spring-batch-51-job-execution-structure
jsonld:
- class_count: 6
  name: Spring Batch 51 Context
  property_count: 25
  slug: spring-batch-51-context
layout: provider
modified: '2026-05-19'
name: Spring Batch 5.1
nav: Providers
network: true
overview: 'Spring Batch 5.1 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch Jobs API, Health API, and Metrics API. Tagged areas include Batch Processing, Data Processing, Enterprise, ETL, and Java.


  The Spring Batch 5.1 catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Batch 5.1''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Spring Batch 51 Plans Pricing
  plan_count: 3
  slug: spring-batch-51-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Spring Batch 51 Rate Limits
  slug: spring-batch-51-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spring Batch 5.1 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-batch-51-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Spring Batch 5.1 API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: spring-batch-51-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 49.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 53.3
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-batch-51/refs/heads/main/screenshots/spring-batch-51-2026-06-20T194406.png
security:
- kind: domain-security
  name: Spring Batch 51 Domain Security
  slug: spring-batch-51-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Batch 51 Vulnerability Disclosure
  slug: spring-batch-51-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-batch-51
tags:
- Batch Processing
- Data Processing
- Enterprise
- ETL
- Java
- Job Scheduling
- Spring Framework
website: https://spring.io/projects/spring-batch
---
