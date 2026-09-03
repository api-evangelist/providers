---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Argocd Agentic Access
  operation_count: 106
  slug: argocd-agentic-access
  summary_line: 106 operations · 50 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Argo CD ApplicationSets API (/api/v1/applicationsets) manages ApplicationSet resources — templated app generators (List, Cluster, Git, Matrix, Merge, Pull Request, SCM Provider) used to programmat
  name: Argo CD ApplicationSets API
  slug: argocd-applicationsets-api
- description: The Argo CD Projects API (/api/v1/projects) manages AppProject resources — multi-tenant boundaries that restrict the source repos, destination clusters/namespaces, and resource kinds available to a gr
  name: Argo CD Projects API
  slug: argocd-projects-api
- description: The Argo CD Clusters API (/api/v1/clusters) registers, updates, lists, and removes target Kubernetes clusters that Argo CD deploys into, including cluster credentials, sharding hints, and namespace sc
  name: Argo CD Clusters API
  slug: argocd-clusters-api
- description: The Argo CD Repositories API (/api/v1/repositories and /api/v1/repocreds) manages Git, Helm chart, and OCI-registry source repositories with credentials, certificates, and per-repo settings used by th
  name: Argo CD Repositories API
  slug: argocd-repositories-api
- description: The Argo CD Accounts API (/api/v1/account) manages local accounts and their API tokens (capability for service accounts), including password rotation and token issuance/revocation.
  name: Argo CD Accounts API
  slug: argocd-accounts-api
- description: The Argo CD Sessions API (/api/v1/session) issues bearer tokens for username/password and OIDC-authenticated sessions used by all other API endpoints.
  name: Argo CD Sessions API
  slug: argocd-sessions-api
- description: The Argo CD Settings API (/api/v1/settings) returns the active server configuration — UI banner, OIDC config, Helm/Kustomize plugin defaults, resource exclusions, application instance label key, and s
  name: Argo CD Settings API
  slug: argocd-settings-api
- description: The Argo CD Certificates API (/api/v1/certificates) manages TLS certificates and SSH known_hosts entries used to securely connect to private Git, Helm, and OCI repositories.
  name: Argo CD Certificates API
  slug: argocd-certificates-api
- description: The Argo CD GPG Keys API (/api/v1/gpgkeys) registers and removes GPG public keys used to verify signed commits before they are deployed.
  name: Argo CD GPG Keys API
  slug: argocd-gpgkeys-api
- description: The Argo CD Notifications subsystem delivers app lifecycle events (sync, health, deploy) to webhooks, Slack, MS Teams, email, GitHub commit status, and other channels via templated triggers.
  name: Argo CD Notifications API
  slug: argocd-notifications-api
- description: The Argo CD Version API (/api/version) returns the running argocd-server build version, Kustomize/Helm/Jsonnet versions, and Kubernetes server version.
  name: Argo CD Version API
  slug: argocd-version-api
- description: 'Argo CD defines an Application Custom Resource Definition (argoproj.io/v1alpha1, kind=Application) describing a desired sync of a single source (Git/Helm/OCI) to a destination cluster/namespace, with '
  name: Argo CD Application CRD
  slug: argocd-application-crd
- description: Argo CD defines an ApplicationSet Custom Resource Definition (argoproj.io/v1alpha1, kind=ApplicationSet) which templatizes Application creation across many targets via pluggable generators.
  name: Argo CD ApplicationSet CRD
  slug: argocd-applicationset-crd
- description: Argo CD defines an AppProject Custom Resource Definition (argoproj.io/v1alpha1, kind=AppProject) which scopes which sources, destinations, and resource kinds Applications inside the project may use, p
  name: Argo CD AppProject CRD
  slug: argocd-appproject-crd
- description: The AccountService API from Argo CD — 6 operation(s) for accountservice.
  name: Argo CD AccountService API
  slug: argocd-accountservice-api
- description: The ApplicationService API from Argo CD — 26 operation(s) for applicationservice.
  name: Argo CD ApplicationService API
  slug: argocd-applicationservice-api
- description: The ApplicationSetService API from Argo CD — 6 operation(s) for applicationsetservice.
  name: Argo CD ApplicationSetService API
  slug: argocd-applicationsetservice-api
- description: The CertificateService API from Argo CD — 1 operation(s) for certificateservice.
  name: Argo CD CertificateService API
  slug: argocd-certificateservice-api
- description: The ClusterService API from Argo CD — 4 operation(s) for clusterservice.
  name: Argo CD ClusterService API
  slug: argocd-clusterservice-api
- description: The GPGKeyService API from Argo CD — 2 operation(s) for gpgkeyservice.
  name: Argo CD GPGKeyService API
  slug: argocd-gpgkeyservice-api
- description: The NotificationService API from Argo CD — 3 operation(s) for notificationservice.
  name: Argo CD NotificationService API
  slug: argocd-notificationservice-api
- description: The ProjectService API from Argo CD — 10 operation(s) for projectservice.
  name: Argo CD ProjectService API
  slug: argocd-projectservice-api
- description: The RepoCredsService API from Argo CD — 6 operation(s) for repocredsservice.
  name: Argo CD RepoCredsService API
  slug: argocd-repocredsservice-api
- description: The RepositoryService API from Argo CD — 13 operation(s) for repositoryservice.
  name: Argo CD RepositoryService API
  slug: argocd-repositoryservice-api
- description: The SessionService API from Argo CD — 2 operation(s) for sessionservice.
  name: Argo CD SessionService API
  slug: argocd-sessionservice-api
- description: The SettingsService API from Argo CD — 2 operation(s) for settingsservice.
  name: Argo CD SettingsService API
  slug: argocd-settingsservice-api
- description: The VersionService API from Argo CD — 1 operation(s) for versionservice.
  name: Argo CD VersionService API
  slug: argocd-versionservice-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Consolidate Services AccountService API
  slug: open-argocd-accountservice-api
- collection_type: open
  name: Consolidate Services AccountService ApplicationService API
  slug: open-argocd-applicationservice-api
- collection_type: open
  name: Consolidate Services AccountService ApplicationSetService API
  slug: open-argocd-applicationsetservice-api
- collection_type: open
  name: Consolidate Services AccountService CertificateService API
  slug: open-argocd-certificateservice-api
- collection_type: open
  name: Consolidate Services AccountService ClusterService API
  slug: open-argocd-clusterservice-api
- collection_type: open
  name: Consolidate Services AccountService GPGKeyService API
  slug: open-argocd-gpgkeyservice-api
- collection_type: open
  name: Consolidate Services AccountService NotificationService API
  slug: open-argocd-notificationservice-api
- collection_type: open
  name: Consolidate Services AccountService ProjectService API
  slug: open-argocd-projectservice-api
- collection_type: open
  name: Consolidate Services AccountService RepoCredsService API
  slug: open-argocd-repocredsservice-api
- collection_type: open
  name: Consolidate Services AccountService RepositoryService API
  slug: open-argocd-repositoryservice-api
- collection_type: open
  name: Consolidate Services
  slug: open-argocd-server
- collection_type: open
  name: Consolidate Services AccountService SessionService API
  slug: open-argocd-sessionservice-api
- collection_type: open
  name: Consolidate Services AccountService SettingsService API
  slug: open-argocd-settingsservice-api
- collection_type: open
  name: Consolidate Services AccountService VersionService API
  slug: open-argocd-versionservice-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argocd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argocd-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argoproj
- group: company
  title: ''
  type: Website
  url: https://argo-cd.readthedocs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://argo-cd.readthedocs.io/en/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://argo-cd.readthedocs.io/en/stable/getting_started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/argoproj
- group: other
  title: ''
  type: Source
  url: https://github.com/argoproj/argo-cd
- group: commercial
  title: ''
  type: License
  url: https://github.com/argoproj/argo-cd/blob/master/LICENSE
- group: other
  title: ''
  type: CNCF Project
  url: https://www.cncf.io/projects/argo/
- group: other
  title: ''
  type: Helm Chart
  url: https://github.com/argoproj/argo-helm/tree/main/charts/argo-cd
- group: operate
  title: ''
  type: Slack Community
  url: https://argoproj.github.io/community/join-slack/
- group: company
  title: ''
  type: Blog
  url: https://blog.argoproj.io/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/argoproj
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ArgoProj
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/argoproj/argo-cd/releases
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/argoproj/argo-cd/blob/master/docs/roadmap.md
- group: docs
  title: ''
  type: Contribution Guide
  url: https://argo-cd.readthedocs.io/en/stable/developer-guide/contributors-quickstart-guide/
- group: docs
  title: ''
  type: Operator Manual
  url: https://argo-cd.readthedocs.io/en/stable/operator-manual/
- group: docs
  title: ''
  type: User Guide
  url: https://argo-cd.readthedocs.io/en/stable/user-guide/
- group: commercial
  title: ''
  type: Plans
  url: plans/argocd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/argocd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/argocd-finops.yml
created: '2026-05-08'
description: Argo CD is a declarative GitOps continuous-delivery tool for Kubernetes, part of the CNCF Graduated Argo project. The argocd-server component exposes a gRPC and REST API used by the Web UI, the argocd CLI, and CI/CD systems. APIs cover applications, projects, clusters, repositories, accounts, certificates, GPG keys, sessions, settings, and notifications. Argo CD is also a Kubernetes operator that defines first-class CRDs (Application, ApplicationSet, AppProject) — those CRDs are themselves a Kubernetes-native API. Argo CD is open-source under the Apache 2.0 license; commercial offerings are provided by third parties (notably Akuity, founded by the Argo project's creators) rather than the Argo CD project itself.
finops:
- name: Argocd Finops
  service_category: DevOps / GitOps
  slug: argocd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argocd.png
layout: provider
modified: '2026-05-19'
name: Argo CD
nav: Providers
network: true
overview: 'Argo CD publishes 13 APIs on the [APIs.io](https://apis.io/) network, including AccountService API, ApplicationService API, ApplicationSetService API, and 10 more. Tagged areas include DevOps, GitOps, Kubernetes, Continuous Delivery, and CNCF.


  Argo CD''s developer surface includes documentation, API reference, getting-started guide, engineering blog, YouTube channel, release notes, and 18 more developer resources.'
plans:
- name: Argocd Plans Pricing
  plan_count: 2
  slug: argocd-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Argocd Rate Limits
  slug: argocd-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 39.3
    developer_ergonomics: 31.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argocd/refs/heads/main/screenshots/argocd-2026-06-20T172419.png
security:
- kind: domain-security
  name: Argocd Domain Security
  slug: argocd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: argocd
tags:
- DevOps
- GitOps
- Kubernetes
- Continuous Delivery
- CNCF
- Open-Source
- Operator
website: https://argo-cd.readthedocs.io/
---
