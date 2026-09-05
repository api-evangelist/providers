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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apache Livy Agentic Access
  operation_count: 15
  slug: apache-livy-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 1
apis:
- baseURL: http://localhost:8998
  baseurl_source: spec
  description: Batch Spark job submission
  name: Apache Livy Batches API
  slug: apache-livy-batches-api
- baseURL: http://localhost:8998
  baseurl_source: spec
  description: Interactive Spark session management
  name: Apache Livy Sessions API
  slug: apache-livy-sessions-api
- baseURL: http://localhost:8998
  baseurl_source: spec
  description: Code statement execution within sessions
  name: Apache Livy Statements API
  slug: apache-livy-statements-api
artifact_total: 68
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Livy REST Batches API
  slug: open-apache-livy-batches-api
- collection_type: open
  name: Apache Livy REST Batches Sessions API
  slug: open-apache-livy-sessions-api
- collection_type: open
  name: Apache Livy REST Batches Statements API
  slug: open-apache-livy-statements-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/incubator-livy/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/incubator-livy/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-livy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-livy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-livy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/incubator-livy
- group: docs
  title: ''
  type: Documentation
  url: https://livy.apache.org/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://livy.apache.org/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://livy.apache.org/download/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-livy-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-livy-vocabulary.yaml
created: '2026-03-16'
description: Apache Livy is a service that enables easy interaction with a Spark cluster over a REST interface. It allows submitting Spark jobs or snippets of Spark code, retrieving results synchronously or asynchronously, and managing Spark contexts across multiple users. Licensed under Apache 2.0.
examples:
- key_count: 5
  name: Rest Api Batch Example
  slug: rest-api-batch-example
- key_count: 3
  name: Rest Api Batch List Example
  slug: rest-api-batch-list-example
- key_count: 2
  name: Rest Api Batch State Example
  slug: rest-api-batch-state-example
- key_count: 10
  name: Rest Api Create Batch Request Example
  slug: rest-api-create-batch-request-example
- key_count: 11
  name: Rest Api Create Session Request Example
  slug: rest-api-create-session-request-example
- key_count: 4
  name: Rest Api Log Example
  slug: rest-api-log-example
- key_count: 8
  name: Rest Api Session Example
  slug: rest-api-session-example
- key_count: 3
  name: Rest Api Session List Example
  slug: rest-api-session-list-example
- key_count: 2
  name: Rest Api Session State Example
  slug: rest-api-session-state-example
- key_count: 4
  name: Rest Api Statement Example
  slug: rest-api-statement-example
- key_count: 2
  name: Rest Api Statement List Example
  slug: rest-api-statement-list-example
- key_count: 2
  name: Rest Api Statement Request Example
  slug: rest-api-statement-request-example
features:
- description: Create persistent Spark contexts for interactive code execution in Python, Scala, R, and SQL.
  name: Interactive Spark Sessions
- description: Submit batch Spark jobs without creating an interactive session.
  name: Batch Job Submission
- description: Execute code in PySpark, Spark (Scala), SparkR, and SQL.
  name: Multi-Language Support
- description: Proxy user support for multi-tenant Spark cluster access.
  name: Multi-User Impersonation
- description: Submit jobs and poll for results asynchronously.
  name: Asynchronous Execution
- description: Retrieve driver and executor logs for debugging.
  name: Log Access
- description: Simple HTTP REST API for Spark cluster interaction without native clients.
  name: REST Interface
finops:
- name: Apache Livy Finops
  service_category: API
  slug: apache-livy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-livy.png
integrations:
- description: Livy requires a Spark cluster and acts as the REST gateway to Spark.
  name: Apache Spark
- description: Zeppelin notebook backend using Livy for distributed Spark execution.
  name: Apache Zeppelin
- description: Jupyter sparkmagic extension uses Livy for remote Spark kernel access.
  name: Jupyter Notebook
- description: Airflow LivyOperator for submitting Spark batch jobs from DAGs.
  name: Apache Airflow
- description: Livy is available as an EMR application for REST-based Spark access.
  name: Amazon EMR
json_schemas:
- name: BatchList
  property_count: 3
  slug: rest-api-batch-list
- name: Batch
  property_count: 5
  slug: rest-api-batch
- name: BatchState
  property_count: 2
  slug: rest-api-batch-state
- name: CreateBatchRequest
  property_count: 10
  slug: rest-api-create-batch-request
- name: CreateSessionRequest
  property_count: 11
  slug: rest-api-create-session-request
- name: Log
  property_count: 4
  slug: rest-api-log
- name: SessionList
  property_count: 3
  slug: rest-api-session-list
- name: Session
  property_count: 8
  slug: rest-api-session
- name: SessionState
  property_count: 2
  slug: rest-api-session-state
- name: StatementList
  property_count: 2
  slug: rest-api-statement-list
- name: StatementRequest
  property_count: 2
  slug: rest-api-statement-request
- name: Statement
  property_count: 4
  slug: rest-api-statement
json_structures:
- name: Rest Api Batch List Structure
  property_count: 3
  slug: rest-api-batch-list-structure
- name: Rest Api Batch State Structure
  property_count: 2
  slug: rest-api-batch-state-structure
- name: Rest Api Batch Structure
  property_count: 5
  slug: rest-api-batch-structure
- name: Rest Api Create Batch Request Structure
  property_count: 10
  slug: rest-api-create-batch-request-structure
- name: Rest Api Create Session Request Structure
  property_count: 11
  slug: rest-api-create-session-request-structure
- name: Rest Api Log Structure
  property_count: 4
  slug: rest-api-log-structure
- name: Rest Api Session List Structure
  property_count: 3
  slug: rest-api-session-list-structure
- name: Rest Api Session State Structure
  property_count: 2
  slug: rest-api-session-state-structure
- name: Rest Api Session Structure
  property_count: 8
  slug: rest-api-session-structure
- name: Rest Api Statement List Structure
  property_count: 2
  slug: rest-api-statement-list-structure
- name: Rest Api Statement Request Structure
  property_count: 2
  slug: rest-api-statement-request-structure
- name: Rest Api Statement Structure
  property_count: 4
  slug: rest-api-statement-structure
jsonld:
- class_count: 12
  name: Apache Livy Rest Api Context
  property_count: 31
  slug: apache-livy-rest-api-context
layout: provider
modified: '2026-05-19'
name: Apache Livy
nav: Providers
network: true
overview: 'Apache Livy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batches API, Sessions API, and Statements API. Tagged areas include Big Data, Interactive Computing, Open-Source, REST, and Spark.


  The Apache Livy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Livy''s developer surface includes documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Apache Livy Plans Pricing
  plan_count: 3
  slug: apache-livy-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Apache Livy Rate Limits
  slug: apache-livy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Livy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-livy-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Apache Livy API Rules
  rule_count: 18
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 7
  slug: apache-livy-spectral-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 15
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
    contract_quality: 54.4
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 15.0
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-livy/refs/heads/main/screenshots/apache-livy-2026-06-20T172116.png
security:
- kind: domain-security
  name: Apache Livy Domain Security
  slug: apache-livy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Livy Vulnerability Disclosure
  slug: apache-livy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-livy
tags:
- Big Data
- Interactive Computing
- Open-Source
- REST
- Spark
use_cases:
- description: Power Jupyter, Zeppelin, and other notebooks with Spark backends via Livy.
  name: Notebook Integration
- description: Submit Spark batch jobs from orchestration tools like Airflow and Oozie.
  name: Data Engineering Pipelines
- description: Execute ad-hoc Spark code for exploratory data analysis.
  name: Interactive Data Exploration
- description: Enable multiple users to share a Spark cluster with isolation via Livy sessions.
  name: Multi-Tenant Spark Access
---
