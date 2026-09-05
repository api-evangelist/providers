---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-04'
api_count: 9
apis:
- description: Launches, feeds and reads results from Business Processes (BPs) and Manual Tasks on the Work.AI platform. Covers the BP lifecycle (draft, processing, paused, completed) with create/start/pause/stop ac
  name: WorkFusion REST API
  slug: workfusion-rest-api
- description: Remote management of Work.AI Data Stores over JSON. Exposes SQL select and execute against ds_-prefixed stores, plus createOrUpdate, insert and delete on a named Data Store.
  name: Data Store REST API
  slug: data-store-rest-api
- description: Credential management for automations. Retrieves, saves, updates and deletes secure entries by alias; passwords are supplied Bcrypt-encoded at strength 10. Responses use the platform's responseStatus/
  name: Secrets Vault API
  slug: secrets-vault-api
- description: Manages database and S3 data purging plus data archival and restoration configurations, including cron-scheduled runs and execution history. Paged and sorted with page, size, sort and sortDirection qu
  name: Data Management API
  slug: data-management-api
- description: Migrates Business Processes across Control Tower instances by packaging runs and Data Stores, with CREATE_WITH_NEW_NAME, REPLACE_EXISTING and SKIP_IMPORT conflict resolution. Uses HTTP Basic authentic
  name: Packages API
  slug: packages-api
- description: Imports and exports AI Agent Asset Bundles and Variation Asset Bundles between Control Tower instances, with REPLACE and SKIP_DATASTORES conflict strategies, md5 checksum validation and asynchronous i
  name: AI Agent Asset Bundle Migration API
  slug: asset-bundle-migration-api
- description: Access to shared Workspace resources — assignments, draft and submitted answers, users, user groups and Workspace metadata. Assignment states are READY_TO_PROCESS, IN_PROGRESS, COMPLETED, EXPIRED, INA
  name: Workspace Shared API
  slug: workspace-shared-api
- description: Document recognition service used by Intelligent Document Processing. submitImage/processImage accept a file and OCR parameters, getTaskStatus polls by task id, and download returns the converted resu
  name: OCR REST API
  slug: ocr-rest-api
- description: Decisioning services the customer runs alongside the platform. POST /decisionRules evaluates a data object against a decision-rules configuration and returns the rules fired plus the decision; POST /g
  name: Rule Builder and GenAI Rules REST API
  slug: rules-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.workfusion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.workfusion.com/platform/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.workfusion.com/platform/docs/api/workfusion-rest-api
- group: operate
  title: ''
  type: Support
  url: https://www.workfusion.com/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://www.workfusion.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WorkFusion
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workfusion.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workfusion.com/aup/
- group: auth
  title: ''
  type: Compliance
  url: https://doc.workfusion.com/platform/support/policies/customer-data-processing-agreement
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.workfusion.com/platform/releases/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/workfusion-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://doc.workfusion.com/enterprise/docs/iac/releases/iac-10-1-deprecations
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workfusion-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workfusion-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workfusion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workfusion-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/workfusion-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workfusion-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/workfusion-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workfusion-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/workfusion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workfusion-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workfusion
- group: other
  title: ''
  type: X
  url: https://twitter.com/workfusion
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC5tOI66hnD7AbRR9A0AvHGg
created: '2026-09-04'
description: 'WorkFusion, Inc. is a New York headquartered enterprise AI company whose Work.AI platform (formerly WorkFusion Intelligent Automation Cloud) ships pre-built AI Agents — Evelyn, Evan, Tara, Edward, Isaac and Kayla — that review financial-crime compliance alerts for banks and financial institutions: name and PEP sanctions screening, payment sanctions screening, adverse media monitoring, enhanced due diligence, AML transaction monitoring and KYC onboarding. The platform is delivered as customer-tenant cloud services or self-hosted software, and its REST API family — Business Process orchestration, Data Stores, Secrets Vault, Packages, Asset Bundle migration, Workspace, OCR and Rules — is documented publicly at doc.workfusion.com but is served only from a customer''s own Control Tower instance. No OpenAPI is published: the platform''s Springfox Swagger UI is disabled by default and requires a login to the customer instance.'
image: https://www.workfusion.com/wp-content/uploads/2023/01/favicon.png
layout: provider
modified: '2026-09-04'
name: WorkFusion
nav: Providers
network: true
overview: 'WorkFusion publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Financial Crime Compliance, Anti-Money Laundering, Sanctions Screening, and Know Your Customer.


  WorkFusion''s developer surface includes documentation, API reference, support, engineering blog, changelog, authentication, YouTube channel, and 18 more developer resources.'
plans:
- name: Workfusion Plans Pricing
  plan_count: 0
  slug: workfusion-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Workfusion Rate Limits
  slug: workfusion-rate-limits
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 28.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Workfusion Authentication
  slug: workfusion-authentication
  summary_line: http/apiKey/mutualTLS/openIdConnect · 5 schemes
- kind: domain-security
  name: Workfusion Domain Security
  slug: workfusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workfusion
tags:
- AI Agents
- Financial Crime Compliance
- Anti-Money Laundering
- Sanctions Screening
- Know Your Customer
- Transaction Monitoring
- Adverse Media Monitoring
- Intelligent Document Processing
- Robotic Process Automation
- Banking
website: https://www.workfusion.com/
---
