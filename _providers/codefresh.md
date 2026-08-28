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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 11
  human_in_the_loop: 3
  name: Codefresh Agentic Access
  operation_count: 27
  slug: codefresh-agentic-access
  summary_line: 27 operations · 11 acting · 3 human-in-the-loop
api_count: 14
apis:
- description: REST API for managing Codefresh pipelines, builds, clusters, environments, repositories, and audit data. Authentication uses API key tokens passed via the Authorization header, with granular scopes in
  name: Codefresh REST API
  slug: rest-api
- description: The Access Control API from Codefresh — 4 operation(s) for access control.
  name: Codefresh Access Control API
  slug: codefresh-access-control-api
- description: The Accounts API from Codefresh — 1 operation(s) for accounts.
  name: Codefresh Accounts API
  slug: codefresh-accounts-api
- description: The Admin API from Codefresh — 2 operation(s) for admin.
  name: Codefresh Admin API
  slug: codefresh-admin-api
- description: The Annotations API from Codefresh — 1 operation(s) for annotations.
  name: Codefresh Annotations API
  slug: codefresh-annotations-api
- description: The Audit API from Codefresh — 1 operation(s) for audit.
  name: Codefresh Audit API
  slug: codefresh-audit-api
- description: The Auth API from Codefresh — 2 operation(s) for auth.
  name: Codefresh Auth API
  slug: codefresh-auth-api
- description: The Builds API from Codefresh — 2 operation(s) for builds.
  name: Codefresh Builds API
  slug: codefresh-builds-api
- description: The Clusters API from Codefresh — 1 operation(s) for clusters.
  name: Codefresh Clusters API
  slug: codefresh-clusters-api
- description: The Contexts API from Codefresh — 1 operation(s) for contexts.
  name: Codefresh Contexts API
  slug: codefresh-contexts-api
- description: The Environments API from Codefresh — 1 operation(s) for environments.
  name: Codefresh Environments API
  slug: codefresh-environments-api
- description: The Features API from Codefresh — 1 operation(s) for features.
  name: Codefresh Features API
  slug: codefresh-features-api
- description: The Helm API from Codefresh — 2 operation(s) for helm.
  name: Codefresh Helm API
  slug: codefresh-helm-api
- description: The Workflows API from Codefresh — 1 operation(s) for workflows.
  name: Codefresh Workflows API
  slug: codefresh-workflows-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Codefresh REST Access Control API
  slug: open-codefresh-access-control-api
- collection_type: open
  name: Codefresh REST Access Control Accounts API
  slug: open-codefresh-accounts-api
- collection_type: open
  name: Codefresh REST Access Control Admin API
  slug: open-codefresh-admin-api
- collection_type: open
  name: Codefresh REST Access Control Annotations API
  slug: open-codefresh-annotations-api
- collection_type: open
  name: Codefresh REST Access Control Audit API
  slug: open-codefresh-audit-api
- collection_type: open
  name: Codefresh REST Access Control Auth API
  slug: open-codefresh-auth-api
- collection_type: open
  name: Codefresh REST Access Control Builds API
  slug: open-codefresh-builds-api
- collection_type: open
  name: Codefresh REST Access Control Clusters API
  slug: open-codefresh-clusters-api
- collection_type: open
  name: Codefresh REST Access Control Contexts API
  slug: open-codefresh-contexts-api
- collection_type: open
  name: Codefresh REST Access Control Environments API
  slug: open-codefresh-environments-api
- collection_type: open
  name: Codefresh REST Access Control Features API
  slug: open-codefresh-features-api
- collection_type: open
  name: Codefresh REST Access Control Helm API
  slug: open-codefresh-helm-api
- collection_type: open
  name: Codefresh REST Access Control Workflows API
  slug: open-codefresh-workflows-api
- collection_type: open
  name: Codefresh REST API
  slug: open-codefresh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codefresh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codefresh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codefresh-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codefresh-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codefresh
- group: company
  title: ''
  type: Website
  url: https://codefresh.io
- group: docs
  title: ''
  type: Documentation
  url: https://codefresh.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://codefresh.io/pricing/
- group: start
  title: ''
  type: Signup
  url: https://g.codefresh.io/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://codefresh.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://codefresh.io/feed/
created: '2026-05-11'
description: Codefresh is an Argo-based CI/CD platform that enables engineering teams to build, test, and deploy applications using GitOps workflows powered by Argo Workflows, Argo CD, Argo Events, and Argo Rollouts. The platform provides pipelines, environments, runtime management, and progressive delivery for Kubernetes-native software delivery. The Codefresh REST API offers programmatic access to pipelines, builds, clusters, environments, and repositories, authenticated via API key tokens with granular scopes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codefresh.png
layout: provider
modified: '2026-05-11'
name: Codefresh
nav: Providers
network: true
overview: 'Codefresh publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Access Control API, Accounts API, Admin API, and 10 more. Tagged areas include CI/CD, Continuous Delivery, GitOps, Argo, and Kubernetes.


  Codefresh''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 32.0
  delta: 1.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codefresh/refs/heads/main/screenshots/codefresh-2026-06-20T174700.png
security:
- kind: authentication
  name: Codefresh Authentication
  slug: codefresh-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codefresh Domain Security
  slug: codefresh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codefresh
tags:
- CI/CD
- Continuous Delivery
- GitOps
- Argo
- Kubernetes
- DevOps
- Pipelines
website: https://codefresh.io
---
