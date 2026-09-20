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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Batch Agentic Access
  operation_count: 8
  slug: microsoft-azure-batch-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 2
apis:
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: 'The complete Azure Batch data-plane API, exactly as Microsoft publishes it: 51 paths, 72 operations, 236 schema definitions and 101 first-party request/response examples, at api-version 2025-06-01. Co'
  name: Azure Batch Service API
  slug: microsoft-azure-batch-batch-service-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: 'The Azure Batch control plane (Microsoft.Batch resource provider) as Microsoft publishes it: 29 paths, 42 operations, 152 schema definitions at api-version 2025-06-01, served from management.azure.com'
  name: Azure Batch Management API
  slug: microsoft-azure-batch-management-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Jobs API from microsoft-azure-batch — 1 operation(s) for jobs. Partial, API Evangelist-authored view; the complete provider contract is the Azure Batch Service API entry below.
  name: microsoft-azure-batch Jobs API
  slug: microsoft-azure-batch-jobs-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Pools API from microsoft-azure-batch — 2 operation(s) for pools. Partial, API Evangelist-authored view; the complete provider contract is the Azure Batch Service API entry below.
  name: microsoft-azure-batch Pools API
  slug: microsoft-azure-batch-pools-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Tasks API from microsoft-azure-batch — 1 operation(s) for tasks. Partial, API Evangelist-authored view; the complete provider contract is the Azure Batch Service API entry below.
  name: microsoft-azure-batch Tasks API
  slug: microsoft-azure-batch-tasks-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Batch Service REST Jobs API
  slug: open-microsoft-azure-batch-jobs-api
- collection_type: open
  name: Azure Batch Service REST Jobs Pools API
  slug: open-microsoft-azure-batch-pools-api
- collection_type: open
  name: Azure Batch Service REST Jobs Tasks API
  slug: open-microsoft-azure-batch-tasks-api
- collection_type: open
  name: Azure Batch Service REST API
  slug: open-microsoft-azure-batch
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/security/microsoft-azure-batch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-batch-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/security/microsoft-azure-batch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-batch-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/agentic-access/microsoft-azure-batch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-batch-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/security/microsoft-azure-batch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-batch-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/authentication/microsoft-azure-batch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-batch-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/scopes/microsoft-azure-batch-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-batch-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/batch/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/batchservice/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/batch/quick-create-portal
- group: start
  title: ''
  type: DeveloperPortal
  url: https://azure.microsoft.com/en-us/products/batch
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/packages/microsoft-azure-batch-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-batch-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/packages/microsoft-azure-batch-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-batch-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/cli/microsoft-azure-batch-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-batch-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/well-known/microsoft-azure-batch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-batch-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/well-known/microsoft-azure-batch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-batch-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/security/microsoft-azure-batch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-batch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/conformance/microsoft-azure-batch-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-batch-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/conformance/microsoft-azure-batch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-batch-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/errors/microsoft-azure-batch-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-batch-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/conventions/microsoft-azure-batch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-batch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/conventions/microsoft-azure-batch-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-batch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/lifecycle/microsoft-azure-batch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-batch-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/lifecycle/microsoft-azure-batch-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-azure-batch-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/changelog/microsoft-azure-batch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-batch-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/rate-limits/microsoft-azure-batch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-batch-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/plans/microsoft-azure-batch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-batch-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/data-model/microsoft-azure-batch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-batch-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/llms/microsoft-azure-batch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-batch-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/finops/microsoft-azure-batch-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-batch-finops.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/batch
created: '2026-03-13'
description: 'Azure Batch is Microsoft’s managed job-scheduling and cluster-management service for large-scale parallel and high-performance computing workloads. You describe pools of virtual machines, jobs and tasks through a REST API; Batch allocates the compute, schedules the work across it, retries failures, and scales the pool up and down against a formula you supply. Microsoft publishes two machine-readable contracts for it in the open azure-rest-api-specs repository: a 72-operation data plane per Batch account, and a 42-operation Azure Resource Manager control plane for the accounts themselves. There is no charge for Batch; you pay for the virtual machines, storage and networking the pools consume, with Spot VMs as the discount lever. Authentication is Microsoft Entra ID OAuth 2.0 (or a legacy shared key), and effective permission comes from Azure RBAC rather than from OAuth scopes.'
finops:
- name: Microsoft Azure Batch Finops
  service_category: API
  slug: microsoft-azure-batch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-batch.png
layout: provider
modified: '2026-09-17'
name: Microsoft Azure Batch
nav: Providers
network: true
overview: 'Microsoft Azure Batch publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Azure Batch Service API, Azure Batch Management API, microsoft-azure-batch Jobs API, and 2 more. Tagged areas include Batch, Compute, Job Scheduling, High Performance Computing, and Cloud.


  Microsoft Azure Batch''s developer surface includes authentication, developer portal, pricing, support, engineering blog, documentation, API reference, and 35 more developer resources.'
plans:
- name: Microsoft Azure Batch Plans Pricing
  plan_count: 0
  slug: microsoft-azure-batch-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 11
  name: Microsoft Azure Batch Rate Limits
  slug: microsoft-azure-batch-rate-limits
scopes:
- name: Microsoft Azure Batch Scopes
  scope_count: 2
  slug: microsoft-azure-batch-scopes
  summary_line: 2 scopes · implicit
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 73.2
    discoverability: 68.5
    operational_transparency: 84.2
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/screenshots/microsoft-azure-batch-2026-06-20T185401.png
security:
- kind: authentication
  name: Microsoft Azure Batch Authentication
  slug: microsoft-azure-batch-authentication
  summary_line: oauth2/shared-key · 3 schemes
- kind: domain-security
  name: Microsoft Azure Batch Domain Security
  slug: microsoft-azure-batch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Batch Vulnerability Disclosure
  slug: microsoft-azure-batch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Batch Trust Center
  slug: microsoft-azure-batch-trust-center
  summary_line: GDPR
slug: microsoft-azure-batch
tags:
- Batch
- Compute
- Job Scheduling
- High Performance Computing
- Cloud
- Microsoft
- Azure
- Parallel Processing
- Scheduling
- Infrastructure
website: https://www.microsoft.com/
---
