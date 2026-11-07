---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sas Agentic Access
  operation_count: 16
  slug: sas-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 1
apis:
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The CAS API from SAS Institute — 1 operation(s) for cas.
  name: SAS Institute CAS API
  slug: sas-cas-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Decisions API from SAS Institute — 2 operation(s) for decisions.
  name: SAS Institute Decisions API
  slug: sas-decisions-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Files API from SAS Institute — 1 operation(s) for files.
  name: SAS Institute Files API
  slug: sas-files-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Folders API from SAS Institute — 1 operation(s) for folders.
  name: SAS Institute Folders API
  slug: sas-folders-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Identities API from SAS Institute — 2 operation(s) for identities.
  name: SAS Institute Identities API
  slug: sas-identities-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Jobs API from SAS Institute — 2 operation(s) for jobs.
  name: SAS Institute Jobs API
  slug: sas-jobs-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Logon API from SAS Institute — 1 operation(s) for logon.
  name: SAS Institute Logon API
  slug: sas-logon-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Models API from SAS Institute — 2 operation(s) for models.
  name: SAS Institute Models API
  slug: sas-models-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Reports API from SAS Institute — 2 operation(s) for reports.
  name: SAS Institute Reports API
  slug: sas-reports-api
- baseURL_template: https://{viya-host}
  baseurl_source: spec_template
  description: The Business Rules API from SAS Institute — 1 operation(s) for business rules.
  name: SAS Institute Business Rules API
  slug: sas-business-rules-api
artifact_total: 59
collections:
- collection_type: open
  name: SAS Viya REST BusinessRules API
  slug: open-sas-businessrules-api
- collection_type: open
  name: SAS Viya REST BusinessRules CAS API
  slug: open-sas-cas-api
- collection_type: open
  name: SAS Viya REST BusinessRules Decisions API
  slug: open-sas-decisions-api
- collection_type: open
  name: SAS Viya REST BusinessRules Files API
  slug: open-sas-files-api
- collection_type: open
  name: SAS Viya REST BusinessRules Folders API
  slug: open-sas-folders-api
- collection_type: open
  name: SAS Viya REST BusinessRules Identities API
  slug: open-sas-identities-api
- collection_type: open
  name: SAS Viya REST BusinessRules Jobs API
  slug: open-sas-jobs-api
- collection_type: open
  name: SAS Viya REST BusinessRules Logon API
  slug: open-sas-logon-api
- collection_type: open
  name: SAS Viya REST BusinessRules Models API
  slug: open-sas-models-api
- collection_type: open
  name: SAS Viya REST BusinessRules Reports API
  slug: open-sas-reports-api
- collection_type: open
  name: SAS Viya REST API
  slug: open-sas-viya-rest-api
common:
- group: other
  href: https://artifacts.apis.io/sas/capabilities/sas-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sas-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sas/agentic-access/sas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sas-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sas/security/sas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sas-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sas/authentication/sas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sas-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sas/scopes/sas-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sas-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sassoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sas
- group: company
  title: ''
  type: Website
  url: https://www.sas.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sas.com/apis/rest/
- group: other
  title: ''
  type: APICatalog
  url: https://developer.sas.com/rest-apis
- group: build
  title: ''
  type: SDKs
  url: https://developer.sas.com/sdk/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sas.com/guides/get-started-rest-apis.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.sas.com/content/feed/
- group: design
  href: https://artifacts.apis.io/sas/rules/sas-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/sas-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/sas/vocabulary/sas-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sas-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/sas/plans/sas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sas-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sas/rate-limits/sas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sas-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sas/finops/sas-finops.yml
  title: ''
  type: FinOps
  url: finops/sas-finops.yml
created: '2026-05-05'
description: SAS Institute is a global leader in analytics, AI, and data management software. SAS Viya, its cloud-native platform, exposes a comprehensive catalog of REST APIs covering data management, machine learning, decisions, reports, identities, and platform administration. The Viya REST API surface enables embedding analytics, automating model lifecycles, and integrating governed AI into business workflows.
examples:
- key_count: 8
  name: Sas Viya Rest Api Get Report Example
  slug: sas-viya-rest-api-get-report-example
- key_count: 4
  name: Sas Viya Rest Api List Jobs Example
  slug: sas-viya-rest-api-list-jobs-example
features:
- description: REST access to in-memory CAS server for high-performance analytics on large datasets
  name: Cloud Analytic Services (CAS)
- description: Register, monitor, compare, and govern machine learning model lifecycles
  name: Model Management
- description: Author, version, and execute decision flows and business rule sets
  name: Decisions and Business Rules
- description: Create, read, update, and export SAS Visual Analytics reports
  name: Reports and Visual Analytics
- description: Manage data sources, tables, lineage, and quality rules with governance
  name: Data Quality and Catalog
- description: Standard OAuth flows through the SAS Logon Manager for secure API access
  name: OAuth 2.0 via SAS Logon
- description: Screen parties and payments against illegal-activity watchlists in real time
  name: Real-Time Watchlist Screening
- description: Deploy and monitor streaming analytics through Event Stream Manager and Studio
  name: Event Stream Processing
finops:
- has_sources: false
  method: generated
  name: Sas Finops
  primary_unit: ''
  service_category: ''
  slug: sas-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sas.png
integrations:
- description: Open-source clients call SAS Viya REST APIs from Python and R workflows
  name: Python and R
- description: Deploy SAS Viya on major cloud providers and integrate with native services
  name: AWS, Azure, and GCP
- description: Java SDK and REST clients for embedding SAS analytics in enterprise apps
  name: Java
- description: SAS Viya SDK for JavaScript embeds dashboards and content in web apps
  name: JavaScript and Web Portals
- description: Connect SAS Event Stream Processing to Kafka, MQTT, and IoT pipelines
  name: Event Streams
json_schemas:
- name: SAS Viya Decision
  property_count: 9
  slug: sas-viya-rest-api-decision
- name: SAS Viya Job
  property_count: 8
  slug: sas-viya-rest-api-job
- name: SAS Viya Report
  property_count: 8
  slug: sas-viya-rest-api-report
json_structures:
- name: Sas Viya Rest Api Job Structure
  property_count: 0
  slug: sas-viya-rest-api-job-structure
jsonld:
- class_count: 8
  name: Sas Context
  property_count: 15
  slug: sas-context
- class_count: 12
  name: Sas Viya Rest Api Context
  property_count: 0
  slug: sas-viya-rest-api-context
layout: provider
modified: '2026-05-19'
name: SAS Institute
nav: Providers
network: true
overview: 'SAS Institute publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including CAS API, Decisions API, Files API, and 7 more. Tagged areas include Analytics, Data Management, Artificial Intelligence, Machine Learning, and Software.


  The SAS Institute catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  SAS Institute''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Sas Plans Pricing
  plan_count: 3
  slug: sas-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Sas Rate Limits
  slug: sas-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SAS Institute — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sas-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: SAS Institute API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: sas-rules
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: SAS Institute API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 7
  slug: sas-spectral-rules
scopes:
- name: Sas Scopes
  scope_count: 1
  slug: sas-scopes
  summary_line: 1 scope · password
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 66.0
    catalog_earned_first_party: 0.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 31.8
    contract_quality: 52.2
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 7.9
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sas/sas-2026-06-20T193436.png
security:
- kind: authentication
  name: Sas Authentication
  slug: sas-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sas Domain Security
  slug: sas-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: sas-create-and-retrieve-job
  slug: sas-create-and-retrieve-job
slug: sas
tags:
- Analytics
- Data Management
- Artificial Intelligence
- Machine Learning
- Software
use_cases:
- description: Operationalize SAS Fraud and Compliance rules to score transactions in real time
  name: Fraud Detection
- description: Embed SAS Viya reports and insights into custom portals and applications
  name: Embedded Analytics
- description: Automate the model lifecycle from training to publish to monitoring via REST
  name: MLOps Automation
- description: Score risk decisions and govern compliance through decisioning APIs
  name: Risk Management
- description: Drive marketing journeys with SAS Customer Intelligence 360 event collection
  name: Customer Intelligence
- description: Manage clinical jobs and clinical repository content via SAS Clinical APIs
  name: Health and Life Sciences
website: https://www.sas.com/
---
