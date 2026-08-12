---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Devtron Agentic Access
  operation_count: 110
  slug: devtron-agentic-access
  summary_line: 110 operations · 58 acting
api_count: 28
apis:
- description: Application management operations including creation, listing, and updates
  name: Devtron Applications API
  slug: devtron-applications-api
- description: Core authentication endpoints including login, token refresh, and auth verification.
  name: Devtron Authentication API
  slug: devtron-authentication-api
- description: The bulk_other API from Devtron — 2 operation(s) for bulk_other.
  name: Devtron bulk_other API
  slug: devtron-bulk-other-api
- description: The BulkUpdate API from Devtron — 5 operation(s) for bulkupdate.
  name: Devtron BulkUpdate API
  slug: devtron-bulkupdate-api
- description: Endpoints for managing authentication and authorization caches.
  name: Devtron Cache Management API
  slug: devtron-cache-management-api
- description: The Change Chart API from Devtron — 1 operation(s) for change chart.
  name: Devtron Change Chart API
  slug: devtron-change-chart-api
- description: The Clone Workflow API from Devtron — 1 operation(s) for clone workflow.
  name: Devtron Clone Workflow API
  slug: devtron-clone-workflow-api
- description: Operations related to clusters and environments
  name: Devtron Cluster Environment API
  slug: devtron-cluster-environment-api
- description: Operations related to cluster creation, update, and validation
  name: Devtron Cluster Management API
  slug: devtron-cluster-management-api
- description: Retrieves the deployment history for a specific CD pipeline based on various filter criteria.
  name: Devtron Deployment History API
  slug: devtron-deployment-history-api
- description: The Devtron Server version API from Devtron — 1 operation(s) for devtron server version.
  name: Devtron Devtron Server version API
  slug: devtron-devtron-server-version-api
- description: Operations for creating, updating, and deleting environments
  name: Devtron Environment Management API
  slug: devtron-environment-management-api
- description: The GitOps Validation API from Devtron — 2 operation(s) for gitops validation.
  name: Devtron GitOps Validation API
  slug: devtron-gitops-validation-api
- description: Helm chart deployment management and operations
  name: Devtron Helm Charts API
  slug: devtron-helm-charts-api
- description: Job management operations for creating, cloning, and retrieving jobs
  name: Devtron Jobs API
  slug: devtron-jobs-api
- description: The K8s API from Devtron — 1 operation(s) for k8s.
  name: Devtron K8s API
  slug: devtron-k8s-api
- description: APIs for managing Kubernetes resources (get, create, update, delete, list).
  name: Devtron K8s Resource API
  slug: devtron-k8s-resource-api
- description: The Labels API from Devtron — 1 operation(s) for labels.
  name: Devtron Labels API
  slug: devtron-labels-api
- description: Application listing
  name: Devtron List Applications API
  slug: devtron-list-applications-api
- description: Application metadata and information retrieval
  name: Devtron Metadata API
  slug: devtron-metadata-api
- description: The Notifications API from Devtron — 3 operation(s) for notifications.
  name: Devtron Notifications API
  slug: devtron-notifications-api
- description: Endpoints for managing policies.
  name: Devtron Policy Management API
  slug: devtron-policy-management-api
- description: Operations related to Role-Based Access Control, like fetching default roles.
  name: Devtron RBAC API
  slug: devtron-rbac-api
- description: Operations related to resource recommendations for Kubernetes workloads.
  name: Devtron Resource Recommendation API
  slug: devtron-resource-recommendation-api
- description: Operations related to user role groups (CRUD, listing, bulk actions).
  name: Devtron Role Group Management API
  slug: devtron-role-group-management-api
- description: Manage Single Sign-On (SSO) provider configurations.
  name: Devtron SSO Configuration API
  slug: devtron-sso-configuration-api
- description: Operations related to user accounts (CRUD, listing, bulk actions).
  name: Devtron User Management API
  slug: devtron-user-management-api
- description: The Workflow Management API from Devtron — 2 operation(s) for workflow management.
  name: Devtron Workflow Management API
  slug: devtron-workflow-management-api
artifact_total: 33
asyncapis:
- description: ''
  name: Devtron Notifications Webhooks
  slug: devtron-notifications-webhooks
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: devtron-mcp.yml
  slug: devtron-mcpyml
modified: '2026-07-18'
name: Devtron
nav: Providers
network: true
overview: 'Devtron publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, bulk_other API, and 25 more. Tagged areas include Company, DevOps, Kubernetes, CI/CD, and GitOps.


  The Devtron catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Devtron''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, changelog, and 15 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 44.4
  delta: -0.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 54.5
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.0
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
