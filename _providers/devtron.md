---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Devtron Agentic Access
  operation_count: 110
  slug: devtron-agentic-access
  summary_line: 110 operations · 58 acting
api_count: 1
apis:
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Application management operations including creation, listing, and updates
  name: Devtron Applications API
  slug: devtron-applications-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Core authentication endpoints including login, token refresh, and auth verification.
  name: Devtron Authentication API
  slug: devtron-authentication-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The bulk_other API from Devtron — 2 operation(s) for bulk_other.
  name: Devtron bulk_other API
  slug: devtron-bulk-other-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The BulkUpdate API from Devtron — 5 operation(s) for bulkupdate.
  name: Devtron BulkUpdate API
  slug: devtron-bulkupdate-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Endpoints for managing authentication and authorization caches.
  name: Devtron Cache Management API
  slug: devtron-cache-management-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The Change Chart API from Devtron — 1 operation(s) for change chart.
  name: Devtron Change Chart API
  slug: devtron-change-chart-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The Clone Workflow API from Devtron — 1 operation(s) for clone workflow.
  name: Devtron Clone Workflow API
  slug: devtron-clone-workflow-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations related to clusters and environments
  name: Devtron Cluster Environment API
  slug: devtron-cluster-environment-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations related to cluster creation, update, and validation
  name: Devtron Cluster Management API
  slug: devtron-cluster-management-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Retrieves the deployment history for a specific CD pipeline based on various filter criteria.
  name: Devtron Deployment History API
  slug: devtron-deployment-history-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The Devtron Server version API from Devtron — 1 operation(s) for devtron server version.
  name: Devtron Devtron Server version API
  slug: devtron-devtron-server-version-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations for creating, updating, and deleting environments
  name: Devtron Environment Management API
  slug: devtron-environment-management-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The GitOps Validation API from Devtron — 2 operation(s) for gitops validation.
  name: Devtron GitOps Validation API
  slug: devtron-gitops-validation-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Helm chart deployment management and operations
  name: Devtron Helm Charts API
  slug: devtron-helm-charts-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Job management operations for creating, cloning, and retrieving jobs
  name: Devtron Jobs API
  slug: devtron-jobs-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The K8s API from Devtron — 1 operation(s) for k8s.
  name: Devtron K8s API
  slug: devtron-k8s-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: APIs for managing Kubernetes resources (get, create, update, delete, list).
  name: Devtron K8s Resource API
  slug: devtron-k8s-resource-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The Labels API from Devtron — 1 operation(s) for labels.
  name: Devtron Labels API
  slug: devtron-labels-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Application listing
  name: Devtron List Applications API
  slug: devtron-list-applications-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Application metadata and information retrieval
  name: Devtron Metadata API
  slug: devtron-metadata-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The Notifications API from Devtron — 3 operation(s) for notifications.
  name: Devtron Notifications API
  slug: devtron-notifications-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Endpoints for managing policies.
  name: Devtron Policy Management API
  slug: devtron-policy-management-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations related to Role-Based Access Control, like fetching default roles.
  name: Devtron RBAC API
  slug: devtron-rbac-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations related to resource recommendations for Kubernetes workloads.
  name: Devtron Resource Recommendation API
  slug: devtron-resource-recommendation-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations related to user role groups (CRUD, listing, bulk actions).
  name: Devtron Role Group Management API
  slug: devtron-role-group-management-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Manage Single Sign-On (SSO) provider configurations.
  name: Devtron SSO Configuration API
  slug: devtron-sso-configuration-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: Operations related to user accounts (CRUD, listing, bulk actions).
  name: Devtron User Management API
  slug: devtron-user-management-api
- baseURL: https://devtron.example.com/orchestrator
  baseurl_source: declared
  description: The Workflow Management API from Devtron — 2 operation(s) for workflow management.
  name: Devtron Workflow Management API
  slug: devtron-workflow-management-api
artifact_total: 61
asyncapis:
- description: ''
  name: Devtron Notifications Webhooks
  slug: devtron-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Devtron APIs Specs Applications API
  slug: open-devtron-applications-api
- collection_type: open
  name: Devtron APIs Specs Applications Authentication API
  slug: open-devtron-authentication-api
- collection_type: open
  name: Devtron APIs Specs Applications bulk_other API
  slug: open-devtron-bulk-other-api
- collection_type: open
  name: Devtron APIs Specs Applications BulkUpdate API
  slug: open-devtron-bulkupdate-api
- collection_type: open
  name: Devtron APIs Specs Applications Cache Management API
  slug: open-devtron-cache-management-api
- collection_type: open
  name: Devtron APIs Specs Applications Change Chart API
  slug: open-devtron-change-chart-api
- collection_type: open
  name: Devtron APIs Specs Applications Clone Workflow API
  slug: open-devtron-clone-workflow-api
- collection_type: open
  name: Devtron APIs Specs Applications Cluster Environment API
  slug: open-devtron-cluster-environment-api
- collection_type: open
  name: Devtron APIs Specs Applications Cluster Management API
  slug: open-devtron-cluster-management-api
- collection_type: open
  name: Devtron APIs Specs Applications Deployment History API
  slug: open-devtron-deployment-history-api
- collection_type: open
  name: Devtron APIs Specs Applications Devtron Server version API
  slug: open-devtron-devtron-server-version-api
- collection_type: open
  name: Devtron APIs Specs Applications Environment Management API
  slug: open-devtron-environment-management-api
- collection_type: open
  name: Devtron APIs Specs Applications GitOps Validation API
  slug: open-devtron-gitops-validation-api
- collection_type: open
  name: Devtron APIs Specs Applications Helm Charts API
  slug: open-devtron-helm-charts-api
- collection_type: open
  name: Devtron APIs Specs Applications Jobs API
  slug: open-devtron-jobs-api
- collection_type: open
  name: Devtron APIs Specs Applications K8s API
  slug: open-devtron-k8s-api
- collection_type: open
  name: Devtron APIs Specs Applications K8s Resource API
  slug: open-devtron-k8s-resource-api
- collection_type: open
  name: Devtron APIs Specs Applications Labels API
  slug: open-devtron-labels-api
- collection_type: open
  name: Devtron APIs Specs Applications List Applications API
  slug: open-devtron-list-applications-api
- collection_type: open
  name: Devtron APIs Specs Applications Metadata API
  slug: open-devtron-metadata-api
- collection_type: open
  name: Devtron APIs Specs Applications Notifications API
  slug: open-devtron-notifications-api
- collection_type: open
  name: Devtron APIs Specs Applications Policy Management API
  slug: open-devtron-policy-management-api
- collection_type: open
  name: Devtron APIs Specs Applications RBAC API
  slug: open-devtron-rbac-api
- collection_type: open
  name: Devtron APIs Specs Applications Resource Recommendation API
  slug: open-devtron-resource-recommendation-api
- collection_type: open
  name: Devtron APIs Specs Applications Role Group Management API
  slug: open-devtron-role-group-management-api
- collection_type: open
  name: Devtron APIs Specs Applications SSO Configuration API
  slug: open-devtron-sso-configuration-api
- collection_type: open
  name: Devtron APIs Specs Applications User Management API
  slug: open-devtron-user-management-api
- collection_type: open
  name: Devtron APIs Specs Applications Workflow Management API
  slug: open-devtron-workflow-management-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/devtron-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/devtron-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://devtron.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.devtron.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devtron.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.devtron.ai/specs/swagger/openapi.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.devtron.ai/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://devtron.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devtron-labs
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/jsRG5qx2gp
- group: commercial
  title: ''
  type: Pricing
  url: https://devtron.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devtron.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devtron.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/devtron-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devtron-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/devtron-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/devtron-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devtron-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devtron-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devtron-agentic-access.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/devtron-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/devtron-notifications-webhooks.yml
created: '2026-07-17'
description: Devtron is an open-source, AI-native Kubernetes management and software delivery platform that unifies application, infrastructure, and cost management for engineering, DevOps, and SRE teams. It provides Kubernetes-native CI/CD, GitOps (ArgoCD/FluxCD), multi-cluster operations, security and compliance governance, observability, and FinOps in a single interface, with 100+ tool integrations and an agentic SRE assistant. Devtron exposes a programmable orchestrator REST API (OpenAPI 3.0, 110 operations) covering application, job, Helm chart, deployment, bulk-action, RBAC, SSO, cluster/environment and notification management, authenticated with RBAC-scoped API tokens. Backed by Insight Partners. Enriched by the API Evangelist pipeline from Devtron's public developer surface.
image: https://avatars.githubusercontent.com/u/60952665?v=4
layout: provider
modified: '2026-07-18'
name: Devtron
nav: Providers
network: true
overview: 'Devtron publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, bulk_other API, and 25 more. Tagged areas include Company, DevOps, Kubernetes, CI/CD, and GitOps.


  The Devtron catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Devtron''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, changelog, and 16 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 50.5
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devtron/refs/heads/main/screenshots/devtron-2026-07-25T211825.png
security:
- kind: authentication
  name: Devtron Authentication
  slug: devtron-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Devtron Domain Security
  slug: devtron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: devtron
tags:
- Company
- DevOps
- Kubernetes
- CI/CD
- GitOps
- Platform Engineering
- Software Delivery
- FinOps
- Observability
website: https://devtron.ai/
---
