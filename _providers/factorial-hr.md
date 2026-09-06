---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Factorial Hr Agentic Access
  operation_count: 5
  slug: factorial-hr-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: Subscribe to lifecycle events fired by Factorial (employee created, employee terminated, attendance clock-in/out, ATS application created/updated, time-off leave created/approved, document created, et
  name: Factorial Webhooks API
  slug: factorial-webhooks-api
- description: Applicant Tracking surface — Candidates, Applications, Application Phases, Job Postings, Feedback, Evaluation Forms, Answers. Read, create, update, and delete candidates and applications, plus phase p
  name: Factorial ATS API
  slug: factorial-ats-api
- description: 'Manage attendance shifts, breaks, overtime requests, timesheet edits, and attendance reviews. v2026-04-01 introduces an api_source field on shift DTOs so integrations can identify themselves on clock '
  name: Factorial Attendance API
  slug: factorial-attendance-api
- description: 'Time-off leaves, leave types, and time-off allowances with enriched statistics. Trigger webhooks on leave creation, update, and approval. Combine with the Approvals API to programmatically approve or '
  name: Factorial Time Off API
  slug: factorial-time-off-api
- description: Manage contract versions and compensation records. v2026-04-01 is a breaking-change release that removes legacy job catalog fields (job_title, professional_category_id, professional_category_descripti
  name: Factorial Contracts and Compensations API
  slug: factorial-contracts-compensations-api
- description: Payroll supplements, payroll identifiers, family situations, and bookkeeper resources. Backs Factorial's integrations with country- specific payroll engines.
  name: Factorial Payroll API
  slug: factorial-payroll-api
- description: Bank accounts, transactions, ledger accounts, journal entries, tax rates and tax types, cost centers, cost center memberships, and budgets. Cost center memberships are bulk-updatable so percentage spl
  name: Factorial Finance and Banking API
  slug: factorial-finance-banking-api
- description: Submit, approve, and reconcile employee expenses, mileage claims, and per-diem requests.
  name: Factorial Expenses API
  slug: factorial-expenses-api
- description: Manage company- and employee-scoped documents and folders. Create, update, retrieve, and delete documents, request legal e-signatures, and fire document_created webhook events. Admin-only for document
  name: Factorial Documents API
  slug: factorial-documents-api
- description: Performance reviews, review processes, evaluations, and performance agreements. Configurable review cycles backed by the Job Catalog Tree introduced in v2026-01-01.
  name: Factorial Performance API
  slug: factorial-performance-api
- description: Manage training programs and training classes, expanded in v2026-04-01 with new class-level capabilities.
  name: Factorial Trainings API
  slug: factorial-trainings-api
- description: Job levels, roles, functions, and the hierarchical Job Catalog Tree introduced in v2026-01-01. Replaces the legacy free-text job_title on contracts via job_catalog_tree_node_uuid.
  name: Factorial Job Catalog API
  slug: factorial-job-catalog-api
- description: Projects, subprojects, tasks, project workers, planned and flexible time records, and budget strategies (full CRUD added in v2026-04-01).
  name: Factorial Project Management API
  slug: factorial-project-management-api
- description: IT asset and IT model endpoints (added in v2026-01-01) backing the SaaS, Inventory, MDM, and Cybersecurity modules.
  name: Factorial IT Management API
  slug: factorial-it-management-api
- description: Purchase orders, purchase requests, and purchase types. Added in v2026-01-01.
  name: Factorial Procurement API
  slug: factorial-procurement-api
- description: Programmatically approve or reject pending steps of a materialized approval flow, either by id or by resource_id+resource_type. Added in v2026-04-01.
  name: Factorial Approvals API
  slug: factorial-approvals-api
- description: Company locations, work areas, and company holidays.
  name: Factorial Locations and Holidays API
  slug: factorial-locations-holidays-api
- description: Groups, posts, and comments backing the Communities V2 feature. Requires Communities V2 to be enabled on the company.
  name: Factorial Posts and Communities API
  slug: factorial-posts-communities-api
- description: Integrations Framework and Marketplace endpoints used by partner integrations to register, surface, and operate within the Factorial app.
  name: Factorial Marketplace and Integrations API
  slug: factorial-marketplace-integrations-api
- description: 'Two authentication methods. OAuth2 (authorization code flow at /oauth/authorize and /oauth/token) is used to act on behalf of a user; Credentials/API Keys (x-api-key header) are used to act on behalf '
  name: Factorial Keys and OAuth API
  slug: factorial-keys-oauth-api
- baseURL: https://api.factorialhr.com/api
  baseurl_source: spec
  description: The Core::Employees::V2 API from Factorial — 2 operation(s) for core::employees::v2.
  name: Factorial Core::Employees::V2 API
  slug: factorial-hr-core-employees-v2-api
- baseURL: https://api.factorialhr.com/api
  baseurl_source: spec
  description: The Core::Me API from Factorial — 1 operation(s) for core::me.
  name: Factorial Core::Me API
  slug: factorial-hr-core-me-api
- description: Versioned REST API for managing employees, contracts, leaves, attendance shifts, time off, documents, and other HR resources in Factorial. Supports API key (Bearer token) and OAuth 2.0 authentication,
  name: Factorial Developer API
  slug: developer-api
- baseURL: https://api.factorialhr.com
  baseurl_source: declared
  description: The Resources API from Factorial — 16 operation(s) for resources.
  name: Factorial Resources API
  slug: factorial-resources-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Factorial Core::Employees::V2 API
  slug: open-factorial-hr-core-employees-v2-api
- collection_type: open
  name: Factorial Core::Employees::V2 Core::Me API
  slug: open-factorial-hr-core-me-api
- collection_type: open
  name: Factorial API
  slug: open-factorial
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/factorial-hr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/factorial-hr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/factorial-hr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/factorial-hr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/factorial-hr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/factorial-hr-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://factorialhr.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidoc.factorialhr.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/first-steps
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/oauth-2
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/oauth-scopes
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/api-keys
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/api-versioning
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/production-and-demo
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/pagination
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/faqs
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidoc.factorialhr.com/changelog
- group: design
  title: ''
  type: Webhooks
  url: https://apidoc.factorialhr.com/docs/manage-webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/webhooks-policies
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/integrations-framework
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/payroll-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.factorialhr.com/docs/finance-integrations
- group: commercial
  title: ''
  type: Pricing
  url: https://factorialhr.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://factorialhr.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.factorialhr.com/users/sign_in
- group: operate
  title: ''
  type: StatusPage
  url: https://factorial.statuspage.io/
- group: company
  title: ''
  type: Blog
  url: https://factorialhr.com/blog
- group: other
  title: ''
  type: Customers
  url: https://factorialhr.com/customers
- group: operate
  title: ''
  type: Support
  url: https://apidoc.factorialhr.com/docs/contact-page
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/factorialco
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas/tree/main/sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas/tree/main/sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas/tree/main/sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas/tree/main/sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas/tree/main/sdk-typescript-axios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/factorialco/oas/tree/main/sdk-nodejs-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/factorialco/f0
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://factorialhr.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://factorialhr.com/terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/factorial-hr/
- group: commercial
  title: ''
  type: Plans
  url: plans/factorial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/factorial-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/factorial-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/factorial-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/factorial-hr-vocabulary.yml
created: '2026-05-25'
description: Factorial is an all-in-one HR, payroll, time, talent, finance, and IT management platform headquartered in Barcelona, Spain, used by 16,000+ companies worldwide. The Factorial public API is a date-versioned REST API (current major 2026-04-01 "Legendre") covering employees, contracts, attendance, time off, payroll, ATS, performance, trainings, projects, finance, banking, procurement, IT assets, documents, webhooks, and an Approvals workflow surface. Authentication uses OAuth2 (on behalf of a user) or an x-api-key header (on behalf of the company), with 30+ scopes for granular partner access. Factorial publishes the OpenAPI schema and generated SDKs (Ruby, Python, Java, PHP, TypeScript, Node.js) at github.com/factorialco/oas and exposes an llms.txt index for AI agents.
examples:
- key_count: 2
  name: Factorial Create Employee Example
  slug: factorial-create-employee-example
- key_count: 8
  name: Factorial Get Current User Example
  slug: factorial-get-current-user-example
features:
- All-in-one HR, payroll, time, finance, talent, and IT modules
- Public REST API with dated, major-versioned releases (current 2026-04-01 "Legendre")
- Two auth schemes - OAuth2 authorization code on behalf of a user and x-api-key on behalf of the company
- 30+ OAuth scopes for fine-grained partner access
- Production and Demo environments (api.factorialhr.com vs api.demo.factorialhr.com)
- 681+ documented endpoints across 30+ resource domains
- Webhook subscriptions with documented event catalogue and retry policy
- Approvals API for programmatic approve/reject of pending workflows
- Job Catalog Tree replacing free-text job titles on contracts
- Bulk endpoints (e.g. cost-center memberships) to reduce roundtrips
- Integrations Framework, Payroll and Finance Integrations partner programs
- Marketplace surface for distributing partner integrations inside the Factorial app
- Officially generated SDKs for Ruby, Python, Java, PHP, TypeScript (axios), and Node.js server
- llms.txt endpoint for AI agents at https://apidoc.factorialhr.com/llms.txt
- 16,000+ companies on platform; HQ in Barcelona, Spain
finops:
- name: Factorial Finops
  service_category: ''
  slug: factorial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/factorial-hr.png
json_schemas:
- name: Factorial Employee
  property_count: 22
  slug: factorial-employee
- name: Factorial Webhook Subscription
  property_count: 6
  slug: factorial-webhook-subscription
jsonld:
- class_count: 26
  name: Factorial Hr Context
  property_count: 0
  slug: factorial-hr-context
layout: provider
modified: '2026-05-25'
name: Factorial
nav: Providers
network: true
overview: 'Factorial publishes 3 APIs on the [APIs.io](https://apis.io/) network: Core::Employees::V2 API, Core::Me API, and Resources API. Tagged areas include HR, Human Resources, Payroll, Time Off, and Time Tracking.


  The Factorial catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Factorial''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, pricing, signup flow, and 42 more developer resources.'
plans:
- name: Factorial Plans Pricing
  plan_count: 5
  slug: factorial-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Factorial Rate Limits
  slug: factorial-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Factorial API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: factorial-hr-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Factorial API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: factorial-rules
scopes:
- name: Factorial Hr Scopes
  scope_count: 2
  slug: factorial-hr-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 28.8
    contract_quality: 65.2
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 30.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/factorial-hr/refs/heads/main/screenshots/factorial-hr-2026-06-20T181038.png
security:
- kind: authentication
  name: Factorial Hr Authentication
  slug: factorial-hr-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Factorial Hr Domain Security
  slug: factorial-hr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Factorial Hr Vulnerability Disclosure
  slug: factorial-hr-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Factorial Hr Trust Center
  slug: factorial-hr-trust-center
  summary_line: SOC 2, ISO 27001
slug: factorial-hr
tags:
- HR
- Human Resources
- Payroll
- Time Off
- Time Tracking
- ATS
- Performance
- Finance
- Expenses
- Spain
- Barcelona
- All-in-One
website: https://factorialhr.com
---
