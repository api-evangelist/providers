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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Argo Cd Agentic Access
  operation_count: 106
  slug: argo-cd-agentic-access
  summary_line: 106 operations · 50 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: The AccountService API from Argo CD — 6 operation(s) for accountservice.
  name: Argo CD AccountService API
  slug: argo-cd-accountservice-api
- description: The ApplicationService API from Argo CD — 26 operation(s) for applicationservice.
  name: Argo CD ApplicationService API
  slug: argo-cd-applicationservice-api
- description: The ApplicationSetService API from Argo CD — 6 operation(s) for applicationsetservice.
  name: Argo CD ApplicationSetService API
  slug: argo-cd-applicationsetservice-api
- description: The CertificateService API from Argo CD — 1 operation(s) for certificateservice.
  name: Argo CD CertificateService API
  slug: argo-cd-certificateservice-api
- description: The ClusterService API from Argo CD — 4 operation(s) for clusterservice.
  name: Argo CD ClusterService API
  slug: argo-cd-clusterservice-api
- description: The GPGKeyService API from Argo CD — 2 operation(s) for gpgkeyservice.
  name: Argo CD GPGKeyService API
  slug: argo-cd-gpgkeyservice-api
- description: The NotificationService API from Argo CD — 3 operation(s) for notificationservice.
  name: Argo CD NotificationService API
  slug: argo-cd-notificationservice-api
- description: The ProjectService API from Argo CD — 10 operation(s) for projectservice.
  name: Argo CD ProjectService API
  slug: argo-cd-projectservice-api
- description: The RepoCredsService API from Argo CD — 6 operation(s) for repocredsservice.
  name: Argo CD RepoCredsService API
  slug: argo-cd-repocredsservice-api
- description: The RepositoryService API from Argo CD — 13 operation(s) for repositoryservice.
  name: Argo CD RepositoryService API
  slug: argo-cd-repositoryservice-api
- description: The SessionService API from Argo CD — 2 operation(s) for sessionservice.
  name: Argo CD SessionService API
  slug: argo-cd-sessionservice-api
- description: The SettingsService API from Argo CD — 2 operation(s) for settingsservice.
  name: Argo CD SettingsService API
  slug: argo-cd-settingsservice-api
- description: The VersionService API from Argo CD — 1 operation(s) for versionservice.
  name: Argo CD VersionService API
  slug: argo-cd-versionservice-api
artifact_total: 850
collections:
- collection_type: open
  name: Argo CD
  slug: open-argo-cd
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argo-cd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argo-cd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argo-cd-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argoproj
- group: company
  title: ''
  type: Website
  url: https://argoproj.github.io/cd/
- group: docs
  title: ''
  type: Documentation
  url: https://argo-cd.readthedocs.io/en/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://argo-cd.readthedocs.io/en/stable/getting_started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/argoproj
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/argoproj/argo-cd
- group: company
  title: ''
  type: Blog
  url: https://blog.argoproj.io/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/argoproj/argo-cd/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/argoproj/argo-cd/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: CLI
  url: https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/argoproj/argo-cd/tree/master/pkg/apiclient
- group: operate
  title: ''
  type: Support
  url: https://github.com/argoproj/argo-cd/issues
- group: design
  title: ''
  type: SpectralRules
  url: rules/argo-cd-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/argo-cd-vocabulary.yaml
created: '2026-03-26'
description: Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes that automates the deployment of applications by using Git repositories as the source of truth for defining the desired application state. It supports multiple config management tools (Helm, Kustomize, Jsonnet, plain YAML), multi-cluster deployments, RBAC, SSO integrations, and a fully-loaded web UI. Part of the CNCF ecosystem and the Argo Project, governed by the Linux Foundation.
examples:
- key_count: 4
  name: Argo Cd Account Account Example
  slug: argo-cd-account-account-example
- key_count: 1
  name: Argo Cd Account Accounts List Example
  slug: argo-cd-account-accounts-list-example
- key_count: 1
  name: Argo Cd Account Can I Response Example
  slug: argo-cd-account-can-i-response-example
- key_count: 3
  name: Argo Cd Account Create Token Request Example
  slug: argo-cd-account-create-token-request-example
- key_count: 1
  name: Argo Cd Account Create Token Response Example
  slug: argo-cd-account-create-token-response-example
- key_count: 3
  name: Argo Cd Account Token Example
  slug: argo-cd-account-token-example
- key_count: 3
  name: Argo Cd Account Update Password Request Example
  slug: argo-cd-account-update-password-request-example
- key_count: 4
  name: Argo Cd Application Application Manifest Query With Files Example
  slug: argo-cd-application-application-manifest-query-with-files-example
- key_count: 2
  name: Argo Cd Application Application Manifest Query With Files Wrapper Example
  slug: argo-cd-application-application-manifest-query-with-files-wrapper-example
- key_count: 5
  name: Argo Cd Application Application Patch Request Example
  slug: argo-cd-application-application-patch-request-example
- key_count: 1
  name: Argo Cd Application Application Resource Response Example
  slug: argo-cd-application-application-resource-response-example
- key_count: 6
  name: Argo Cd Application Application Rollback Request Example
  slug: argo-cd-application-application-rollback-request-example
- key_count: 2
  name: Argo Cd Application Application Server Side Diff Response Example
  slug: argo-cd-application-application-server-side-diff-response-example
- key_count: 14
  name: Argo Cd Application Application Sync Request Example
  slug: argo-cd-application-application-sync-request-example
- key_count: 4
  name: Argo Cd Application Application Sync Window Example
  slug: argo-cd-application-application-sync-window-example
- key_count: 3
  name: Argo Cd Application Application Sync Windows Response Example
  slug: argo-cd-application-application-sync-windows-response-example
- key_count: 1
  name: Argo Cd Application File Chunk Example
  slug: argo-cd-application-file-chunk-example
- key_count: 4
  name: Argo Cd Application Link Info Example
  slug: argo-cd-application-link-info-example
- key_count: 1
  name: Argo Cd Application Links Response Example
  slug: argo-cd-application-links-response-example
- key_count: 5
  name: Argo Cd Application Log Entry Example
  slug: argo-cd-application-log-entry-example
- key_count: 1
  name: Argo Cd Application Managed Resources Response Example
  slug: argo-cd-application-managed-resources-response-example
- key_count: 2
  name: Argo Cd Application Resource Action Parameters Example
  slug: argo-cd-application-resource-action-parameters-example
- key_count: 10
  name: Argo Cd Application Resource Action Run Request V2 Example
  slug: argo-cd-application-resource-action-run-request-v2-example
- key_count: 1
  name: Argo Cd Application Resource Actions List Response Example
  slug: argo-cd-application-resource-actions-list-response-example
- key_count: 1
  name: Argo Cd Application Sync Options Example
  slug: argo-cd-application-sync-options-example
- key_count: 1
  name: Argo Cd Applicationset Application Set Generate Request Example
  slug: argo-cd-applicationset-application-set-generate-request-example
- key_count: 1
  name: Argo Cd Applicationset Application Set Generate Response Example
  slug: argo-cd-applicationset-application-set-generate-response-example
- key_count: 2
  name: Argo Cd Applicationset Application Set Response Example
  slug: argo-cd-applicationset-application-set-response-example
- key_count: 2
  name: Argo Cd Applicationv1Alpha1 Env Entry Example
  slug: argo-cd-applicationv1alpha1-env-entry-example
- key_count: 11
  name: Argo Cd Applicationv1Alpha1 Resource Status Example
  slug: argo-cd-applicationv1alpha1-resource-status-example
- key_count: 2
  name: Argo Cd Cluster Cluster Id Example
  slug: argo-cd-cluster-cluster-id-example
- key_count: 2
  name: Argo Cd Cluster Connector Example
  slug: argo-cd-cluster-connector-example
- key_count: 1
  name: Argo Cd Cluster Dex Config Example
  slug: argo-cd-cluster-dex-config-example
- key_count: 2
  name: Argo Cd Cluster Google Analytics Config Example
  slug: argo-cd-cluster-google-analytics-config-example
- key_count: 3
  name: Argo Cd Cluster Help Example
  slug: argo-cd-cluster-help-example
- key_count: 7
  name: Argo Cd Cluster Oidc Config Example
  slug: argo-cd-cluster-oidc-config-example
- key_count: 1
  name: Argo Cd Cluster Plugin Example
  slug: argo-cd-cluster-plugin-example
- key_count: 29
  name: Argo Cd Cluster Settings Example
  slug: argo-cd-cluster-settings-example
- key_count: 1
  name: Argo Cd Cluster Settings Plugins Response Example
  slug: argo-cd-cluster-settings-plugins-response-example
- key_count: 2
  name: Argo Cd Gpgkey Gnu Pg Public Key Create Response Example
  slug: argo-cd-gpgkey-gnu-pg-public-key-create-response-example
- key_count: 3
  name: Argo Cd Intstr Int Or String Example
  slug: argo-cd-intstr-int-or-string-example
- key_count: 1
  name: Argo Cd Notification Service Example
  slug: argo-cd-notification-service-example
- key_count: 1
  name: Argo Cd Notification Service List Example
  slug: argo-cd-notification-service-list-example
- key_count: 1
  name: Argo Cd Notification Template Example
  slug: argo-cd-notification-template-example
- key_count: 1
  name: Argo Cd Notification Template List Example
  slug: argo-cd-notification-template-list-example
- key_count: 1
  name: Argo Cd Notification Trigger Example
  slug: argo-cd-notification-trigger-example
- key_count: 1
  name: Argo Cd Notification Trigger List Example
  slug: argo-cd-notification-trigger-list-example
- key_count: 3
  name: Argo Cd Oidc Claim Example
  slug: argo-cd-oidc-claim-example
- key_count: 4
  name: Argo Cd Project Detailed Projects Response Example
  slug: argo-cd-project-detailed-projects-response-example
- key_count: 1
  name: Argo Cd Project Global Projects Response Example
  slug: argo-cd-project-global-projects-response-example
- key_count: 2
  name: Argo Cd Project Project Create Request Example
  slug: argo-cd-project-project-create-request-example
- key_count: 5
  name: Argo Cd Project Project Token Create Request Example
  slug: argo-cd-project-project-token-create-request-example
- key_count: 1
  name: Argo Cd Project Project Token Response Example
  slug: argo-cd-project-project-token-response-example
- key_count: 1
  name: Argo Cd Project Project Update Request Example
  slug: argo-cd-project-project-update-request-example
- key_count: 1
  name: Argo Cd Project Sync Windows Response Example
  slug: argo-cd-project-sync-windows-response-example
- key_count: 2
  name: Argo Cd Protobuf Any Example
  slug: argo-cd-protobuf-any-example
- key_count: 2
  name: Argo Cd Repository App Info Example
  slug: argo-cd-repository-app-info-example
- key_count: 5
  name: Argo Cd Repository Helm App Spec Example
  slug: argo-cd-repository-helm-app-spec-example
- key_count: 2
  name: Argo Cd Repository Helm Chart Example
  slug: argo-cd-repository-helm-chart-example
- key_count: 1
  name: Argo Cd Repository Helm Charts Response Example
  slug: argo-cd-repository-helm-charts-response-example
- key_count: 1
  name: Argo Cd Repository Kustomize App Spec Example
  slug: argo-cd-repository-kustomize-app-spec-example
- key_count: 7
  name: Argo Cd Repository Manifest Response Example
  slug: argo-cd-repository-manifest-response-example
- key_count: 9
  name: Argo Cd Repository Parameter Announcement Example
  slug: argo-cd-repository-parameter-announcement-example
- key_count: 1
  name: Argo Cd Repository Plugin App Spec Example
  slug: argo-cd-repository-plugin-app-spec-example
- key_count: 2
  name: Argo Cd Repository Refs Example
  slug: argo-cd-repository-refs-example
- key_count: 5
  name: Argo Cd Repository Repo App Details Query Example
  slug: argo-cd-repository-repo-app-details-query-example
- key_count: 5
  name: Argo Cd Repository Repo App Details Response Example
  slug: argo-cd-repository-repo-app-details-response-example
- key_count: 1
  name: Argo Cd Repository Repo Apps Response Example
  slug: argo-cd-repository-repo-apps-response-example
- key_count: 4
  name: Argo Cd Runtime Error Example
  slug: argo-cd-runtime-error-example
- key_count: 1
  name: Argo Cd Runtime Raw Extension Example
  slug: argo-cd-runtime-raw-extension-example
- key_count: 5
  name: Argo Cd Runtime Stream Error Example
  slug: argo-cd-runtime-stream-error-example
- key_count: 4
  name: Argo Cd Session Get User Info Response Example
  slug: argo-cd-session-get-user-info-response-example
- key_count: 3
  name: Argo Cd Session Session Create Request Example
  slug: argo-cd-session-session-create-request-example
- key_count: 1
  name: Argo Cd Session Session Response Example
  slug: argo-cd-session-session-response-example
- key_count: 15
  name: Argo Cd V1 Event Example
  slug: argo-cd-v1-event-example
- key_count: 2
  name: Argo Cd V1 Event List Example
  slug: argo-cd-v1-event-list-example
- key_count: 2
  name: Argo Cd V1 Event Series Example
  slug: argo-cd-v1-event-series-example
- key_count: 2
  name: Argo Cd V1 Event Source Example
  slug: argo-cd-v1-event-source-example
- key_count: 1
  name: Argo Cd V1 Fields V1 Example
  slug: argo-cd-v1-fields-v1-example
- key_count: 2
  name: Argo Cd V1 Group Kind Example
  slug: argo-cd-v1-group-kind-example
- key_count: 1
  name: Argo Cd V1 Json Example
  slug: argo-cd-v1-json-example
- key_count: 2
  name: Argo Cd V1 Label Selector Example
  slug: argo-cd-v1-label-selector-example
- key_count: 3
  name: Argo Cd V1 Label Selector Requirement Example
  slug: argo-cd-v1-label-selector-requirement-example
- key_count: 4
  name: Argo Cd V1 List Meta Example
  slug: argo-cd-v1-list-meta-example
- key_count: 4
  name: Argo Cd V1 Load Balancer Ingress Example
  slug: argo-cd-v1-load-balancer-ingress-example
- key_count: 7
  name: Argo Cd V1 Managed Fields Entry Example
  slug: argo-cd-v1-managed-fields-entry-example
- key_count: 2
  name: Argo Cd V1 Micro Time Example
  slug: argo-cd-v1-micro-time-example
- key_count: 1
  name: Argo Cd V1 Node Swap Status Example
  slug: argo-cd-v1-node-swap-status-example
- key_count: 11
  name: Argo Cd V1 Node System Info Example
  slug: argo-cd-v1-node-system-info-example
- key_count: 15
  name: Argo Cd V1 Object Meta Example
  slug: argo-cd-v1-object-meta-example
- key_count: 7
  name: Argo Cd V1 Object Reference Example
  slug: argo-cd-v1-object-reference-example
- key_count: 6
  name: Argo Cd V1 Owner Reference Example
  slug: argo-cd-v1-owner-reference-example
- key_count: 3
  name: Argo Cd V1 Port Status Example
  slug: argo-cd-v1-port-status-example
- key_count: 3
  name: Argo Cd V1Alpha1 App Health Status Example
  slug: argo-cd-v1alpha1-app-health-status-example
- key_count: 3
  name: Argo Cd V1Alpha1 App Project Example
  slug: argo-cd-v1alpha1-app-project-example
- key_count: 2
  name: Argo Cd V1Alpha1 App Project List Example
  slug: argo-cd-v1alpha1-app-project-list-example
- key_count: 14
  name: Argo Cd V1Alpha1 App Project Spec Example
  slug: argo-cd-v1alpha1-app-project-spec-example
- key_count: 1
  name: Argo Cd V1Alpha1 App Project Status Example
  slug: argo-cd-v1alpha1-app-project-status-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Condition Example
  slug: argo-cd-v1alpha1-application-condition-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Destination Example
  slug: argo-cd-v1alpha1-application-destination-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Destination Service Account Example
  slug: argo-cd-v1alpha1-application-destination-service-account-example
- key_count: 4
  name: Argo Cd V1Alpha1 Application Example
  slug: argo-cd-v1alpha1-application-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application List Example
  slug: argo-cd-v1alpha1-application-list-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Match Expression Example
  slug: argo-cd-v1alpha1-application-match-expression-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Preserved Fields Example
  slug: argo-cd-v1alpha1-application-preserved-fields-example
- key_count: 6
  name: Argo Cd V1Alpha1 Application Set Application Status Example
  slug: argo-cd-v1alpha1-application-set-application-status-example
- key_count: 5
  name: Argo Cd V1Alpha1 Application Set Condition Example
  slug: argo-cd-v1alpha1-application-set-condition-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Set Example
  slug: argo-cd-v1alpha1-application-set-example
- key_count: 10
  name: Argo Cd V1Alpha1 Application Set Generator Example
  slug: argo-cd-v1alpha1-application-set-generator-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Set List Example
  slug: argo-cd-v1alpha1-application-set-list-example
- key_count: 10
  name: Argo Cd V1Alpha1 Application Set Nested Generator Example
  slug: argo-cd-v1alpha1-application-set-nested-generator-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Set Resource Ignore Differences Example
  slug: argo-cd-v1alpha1-application-set-resource-ignore-differences-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Set Rollout Step Example
  slug: argo-cd-v1alpha1-application-set-rollout-step-example
- key_count: 1
  name: Argo Cd V1Alpha1 Application Set Rollout Strategy Example
  slug: argo-cd-v1alpha1-application-set-rollout-strategy-example
- key_count: 10
  name: Argo Cd V1Alpha1 Application Set Spec Example
  slug: argo-cd-v1alpha1-application-set-spec-example
- key_count: 5
  name: Argo Cd V1Alpha1 Application Set Status Example
  slug: argo-cd-v1alpha1-application-set-status-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Set Strategy Example
  slug: argo-cd-v1alpha1-application-set-strategy-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Set Sync Policy Example
  slug: argo-cd-v1alpha1-application-set-sync-policy-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Set Template Example
  slug: argo-cd-v1alpha1-application-set-template-example
- key_count: 5
  name: Argo Cd V1Alpha1 Application Set Template Meta Example
  slug: argo-cd-v1alpha1-application-set-template-meta-example
- key_count: 1
  name: Argo Cd V1Alpha1 Application Set Tree Example
  slug: argo-cd-v1alpha1-application-set-tree-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Set Watch Event Example
  slug: argo-cd-v1alpha1-application-set-watch-event-example
- key_count: 4
  name: Argo Cd V1Alpha1 Application Source Directory Example
  slug: argo-cd-v1alpha1-application-source-directory-example
- key_count: 10
  name: Argo Cd V1Alpha1 Application Source Example
  slug: argo-cd-v1alpha1-application-source-example
- key_count: 15
  name: Argo Cd V1Alpha1 Application Source Helm Example
  slug: argo-cd-v1alpha1-application-source-helm-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Source Jsonnet Example
  slug: argo-cd-v1alpha1-application-source-jsonnet-example
- key_count: 18
  name: Argo Cd V1Alpha1 Application Source Kustomize Example
  slug: argo-cd-v1alpha1-application-source-kustomize-example
- key_count: 3
  name: Argo Cd V1Alpha1 Application Source Plugin Example
  slug: argo-cd-v1alpha1-application-source-plugin-example
- key_count: 4
  name: Argo Cd V1Alpha1 Application Source Plugin Parameter Example
  slug: argo-cd-v1alpha1-application-source-plugin-parameter-example
- key_count: 9
  name: Argo Cd V1Alpha1 Application Spec Example
  slug: argo-cd-v1alpha1-application-spec-example
- key_count: 14
  name: Argo Cd V1Alpha1 Application Status Example
  slug: argo-cd-v1alpha1-application-status-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Summary Example
  slug: argo-cd-v1alpha1-application-summary-example
- key_count: 4
  name: Argo Cd V1Alpha1 Application Tree Example
  slug: argo-cd-v1alpha1-application-tree-example
- key_count: 2
  name: Argo Cd V1Alpha1 Application Watch Event Example
  slug: argo-cd-v1alpha1-application-watch-event-example
- key_count: 3
  name: Argo Cd V1Alpha1 Aws Auth Config Example
  slug: argo-cd-v1alpha1-aws-auth-config-example
- key_count: 3
  name: Argo Cd V1Alpha1 Backoff Example
  slug: argo-cd-v1alpha1-backoff-example
- key_count: 2
  name: Argo Cd V1Alpha1 Basic Auth Bitbucket Server Example
  slug: argo-cd-v1alpha1-basic-auth-bitbucket-server-example
- key_count: 1
  name: Argo Cd V1Alpha1 Bearer Token Bitbucket Cloud Example
  slug: argo-cd-v1alpha1-bearer-token-bitbucket-cloud-example
- key_count: 1
  name: Argo Cd V1Alpha1 Bearer Token Bitbucket Example
  slug: argo-cd-v1alpha1-bearer-token-bitbucket-example
- key_count: 3
  name: Argo Cd V1Alpha1 Chart Details Example
  slug: argo-cd-v1alpha1-chart-details-example
- key_count: 3
  name: Argo Cd V1Alpha1 Cluster Cache Info Example
  slug: argo-cd-v1alpha1-cluster-cache-info-example
- key_count: 8
  name: Argo Cd V1Alpha1 Cluster Config Example
  slug: argo-cd-v1alpha1-cluster-config-example
- key_count: 13
  name: Argo Cd V1Alpha1 Cluster Example
  slug: argo-cd-v1alpha1-cluster-example
- key_count: 4
  name: Argo Cd V1Alpha1 Cluster Generator Example
  slug: argo-cd-v1alpha1-cluster-generator-example
- key_count: 5
  name: Argo Cd V1Alpha1 Cluster Info Example
  slug: argo-cd-v1alpha1-cluster-info-example
- key_count: 2
  name: Argo Cd V1Alpha1 Cluster List Example
  slug: argo-cd-v1alpha1-cluster-list-example
- key_count: 3
  name: Argo Cd V1Alpha1 Cluster Resource Restriction Item Example
  slug: argo-cd-v1alpha1-cluster-resource-restriction-item-example
- key_count: 2
  name: Argo Cd V1Alpha1 Command Example
  slug: argo-cd-v1alpha1-command-example
- key_count: 6
  name: Argo Cd V1Alpha1 Commit Metadata Example
  slug: argo-cd-v1alpha1-commit-metadata-example
- key_count: 4
  name: Argo Cd V1Alpha1 Compared To Example
  slug: argo-cd-v1alpha1-compared-to-example
- key_count: 4
  name: Argo Cd V1Alpha1 Config Management Plugin Example
  slug: argo-cd-v1alpha1-config-management-plugin-example
- key_count: 2
  name: Argo Cd V1Alpha1 Config Map Key Ref Example
  slug: argo-cd-v1alpha1-config-map-key-ref-example
- key_count: 3
  name: Argo Cd V1Alpha1 Connection State Example
  slug: argo-cd-v1alpha1-connection-state-example
- key_count: 7
  name: Argo Cd V1Alpha1 Dry Source Example
  slug: argo-cd-v1alpha1-dry-source-example
- key_count: 6
  name: Argo Cd V1Alpha1 Duck Type Generator Example
  slug: argo-cd-v1alpha1-duck-type-generator-example
- key_count: 5
  name: Argo Cd V1Alpha1 Exec Provider Config Example
  slug: argo-cd-v1alpha1-exec-provider-config-example
- key_count: 2
  name: Argo Cd V1Alpha1 Git Directory Generator Item Example
  slug: argo-cd-v1alpha1-git-directory-generator-item-example
- key_count: 2
  name: Argo Cd V1Alpha1 Git File Generator Item Example
  slug: argo-cd-v1alpha1-git-file-generator-item-example
- key_count: 8
  name: Argo Cd V1Alpha1 Git Generator Example
  slug: argo-cd-v1alpha1-git-generator-example
- key_count: 6
  name: Argo Cd V1Alpha1 Gnu Pg Public Key Example
  slug: argo-cd-v1alpha1-gnu-pg-public-key-example
- key_count: 2
  name: Argo Cd V1Alpha1 Gnu Pg Public Key List Example
  slug: argo-cd-v1alpha1-gnu-pg-public-key-list-example
- key_count: 3
  name: Argo Cd V1Alpha1 Health Status Example
  slug: argo-cd-v1alpha1-health-status-example
- key_count: 2
  name: Argo Cd V1Alpha1 Helm File Parameter Example
  slug: argo-cd-v1alpha1-helm-file-parameter-example
- key_count: 3
  name: Argo Cd V1Alpha1 Helm Parameter Example
  slug: argo-cd-v1alpha1-helm-parameter-example
- key_count: 4
  name: Argo Cd V1Alpha1 Host Info Example
  slug: argo-cd-v1alpha1-host-info-example
- key_count: 4
  name: Argo Cd V1Alpha1 Host Resource Info Example
  slug: argo-cd-v1alpha1-host-resource-info-example
- key_count: 7
  name: Argo Cd V1Alpha1 Hydrate Operation Example
  slug: argo-cd-v1alpha1-hydrate-operation-example
- key_count: 1
  name: Argo Cd V1Alpha1 Hydrate To Example
  slug: argo-cd-v1alpha1-hydrate-to-example
- key_count: 2
  name: Argo Cd V1Alpha1 Info Example
  slug: argo-cd-v1alpha1-info-example
- key_count: 2
  name: Argo Cd V1Alpha1 Info Item Example
  slug: argo-cd-v1alpha1-info-item-example
- key_count: 3
  name: Argo Cd V1Alpha1 Jsonnet Var Example
  slug: argo-cd-v1alpha1-jsonnet-var-example
- key_count: 3
  name: Argo Cd V1Alpha1 Jwt Token Example
  slug: argo-cd-v1alpha1-jwt-token-example
- key_count: 1
  name: Argo Cd V1Alpha1 Jwt Tokens Example
  slug: argo-cd-v1alpha1-jwt-tokens-example
- key_count: 2
  name: Argo Cd V1Alpha1 Known Type Field Example
  slug: argo-cd-v1alpha1-known-type-field-example
- key_count: 3
  name: Argo Cd V1Alpha1 Kustomize Gvk Example
  slug: argo-cd-v1alpha1-kustomize-gvk-example
- key_count: 3
  name: Argo Cd V1Alpha1 Kustomize Options Example
  slug: argo-cd-v1alpha1-kustomize-options-example
- key_count: 4
  name: Argo Cd V1Alpha1 Kustomize Patch Example
  slug: argo-cd-v1alpha1-kustomize-patch-example
- key_count: 2
  name: Argo Cd V1Alpha1 Kustomize Replica Example
  slug: argo-cd-v1alpha1-kustomize-replica-example
- key_count: 3
  name: Argo Cd V1Alpha1 Kustomize Res Id Example
  slug: argo-cd-v1alpha1-kustomize-res-id-example
- key_count: 3
  name: Argo Cd V1Alpha1 Kustomize Selector Example
  slug: argo-cd-v1alpha1-kustomize-selector-example
- key_count: 3
  name: Argo Cd V1Alpha1 Kustomize Version Example
  slug: argo-cd-v1alpha1-kustomize-version-example
- key_count: 3
  name: Argo Cd V1Alpha1 List Generator Example
  slug: argo-cd-v1alpha1-list-generator-example
- key_count: 2
  name: Argo Cd V1Alpha1 Managed Namespace Metadata Example
  slug: argo-cd-v1alpha1-managed-namespace-metadata-example
- key_count: 2
  name: Argo Cd V1Alpha1 Matrix Generator Example
  slug: argo-cd-v1alpha1-matrix-generator-example
- key_count: 3
  name: Argo Cd V1Alpha1 Merge Generator Example
  slug: argo-cd-v1alpha1-merge-generator-example
- key_count: 7
  name: Argo Cd V1Alpha1 Oci Metadata Example
  slug: argo-cd-v1alpha1-oci-metadata-example
- key_count: 4
  name: Argo Cd V1Alpha1 Operation Example
  slug: argo-cd-v1alpha1-operation-example
- key_count: 2
  name: Argo Cd V1Alpha1 Operation Initiator Example
  slug: argo-cd-v1alpha1-operation-initiator-example
- key_count: 7
  name: Argo Cd V1Alpha1 Operation State Example
  slug: argo-cd-v1alpha1-operation-state-example
- key_count: 3
  name: Argo Cd V1Alpha1 Orphaned Resource Key Example
  slug: argo-cd-v1alpha1-orphaned-resource-key-example
- key_count: 2
  name: Argo Cd V1Alpha1 Orphaned Resources Monitor Settings Example
  slug: argo-cd-v1alpha1-orphaned-resources-monitor-settings-example
- key_count: 3
  name: Argo Cd V1Alpha1 Override Ignore Diff Example
  slug: argo-cd-v1alpha1-override-ignore-diff-example
- key_count: 1
  name: Argo Cd V1Alpha1 Plugin Config Map Ref Example
  slug: argo-cd-v1alpha1-plugin-config-map-ref-example
- key_count: 5
  name: Argo Cd V1Alpha1 Plugin Generator Example
  slug: argo-cd-v1alpha1-plugin-generator-example
- key_count: 1
  name: Argo Cd V1Alpha1 Plugin Input Example
  slug: argo-cd-v1alpha1-plugin-input-example
- key_count: 5
  name: Argo Cd V1Alpha1 Project Role Example
  slug: argo-cd-v1alpha1-project-role-example
- key_count: 6
  name: Argo Cd V1Alpha1 Pull Request Generator Azure Dev Ops Example
  slug: argo-cd-v1alpha1-pull-request-generator-azure-dev-ops-example
- key_count: 5
  name: Argo Cd V1Alpha1 Pull Request Generator Bitbucket Example
  slug: argo-cd-v1alpha1-pull-request-generator-bitbucket-example
- key_count: 7
  name: Argo Cd V1Alpha1 Pull Request Generator Bitbucket Server Example
  slug: argo-cd-v1alpha1-pull-request-generator-bitbucket-server-example
- key_count: 11
  name: Argo Cd V1Alpha1 Pull Request Generator Example
  slug: argo-cd-v1alpha1-pull-request-generator-example
- key_count: 3
  name: Argo Cd V1Alpha1 Pull Request Generator Filter Example
  slug: argo-cd-v1alpha1-pull-request-generator-filter-example
- key_count: 7
  name: Argo Cd V1Alpha1 Pull Request Generator Git Lab Example
  slug: argo-cd-v1alpha1-pull-request-generator-git-lab-example
- key_count: 6
  name: Argo Cd V1Alpha1 Pull Request Generator Gitea Example
  slug: argo-cd-v1alpha1-pull-request-generator-gitea-example
- key_count: 6
  name: Argo Cd V1Alpha1 Pull Request Generator Github Example
  slug: argo-cd-v1alpha1-pull-request-generator-github-example
- key_count: 23
  name: Argo Cd V1Alpha1 Repo Creds Example
  slug: argo-cd-v1alpha1-repo-creds-example
- key_count: 2
  name: Argo Cd V1Alpha1 Repo Creds List Example
  slug: argo-cd-v1alpha1-repo-creds-list-example
- key_count: 5
  name: Argo Cd V1Alpha1 Repository Certificate Example
  slug: argo-cd-v1alpha1-repository-certificate-example
- key_count: 2
  name: Argo Cd V1Alpha1 Repository Certificate List Example
  slug: argo-cd-v1alpha1-repository-certificate-list-example
- key_count: 32
  name: Argo Cd V1Alpha1 Repository Example
  slug: argo-cd-v1alpha1-repository-example
- key_count: 2
  name: Argo Cd V1Alpha1 Repository List Example
  slug: argo-cd-v1alpha1-repository-list-example
- key_count: 5
  name: Argo Cd V1Alpha1 Resource Action Example
  slug: argo-cd-v1alpha1-resource-action-example
- key_count: 1
  name: Argo Cd V1Alpha1 Resource Action Param Example
  slug: argo-cd-v1alpha1-resource-action-param-example
- key_count: 12
  name: Argo Cd V1Alpha1 Resource Diff Example
  slug: argo-cd-v1alpha1-resource-diff-example
- key_count: 7
  name: Argo Cd V1Alpha1 Resource Ignore Differences Example
  slug: argo-cd-v1alpha1-resource-ignore-differences-example
- key_count: 5
  name: Argo Cd V1Alpha1 Resource Networking Info Example
  slug: argo-cd-v1alpha1-resource-networking-info-example
- key_count: 7
  name: Argo Cd V1Alpha1 Resource Node Example
  slug: argo-cd-v1alpha1-resource-node-example
- key_count: 6
  name: Argo Cd V1Alpha1 Resource Override Example
  slug: argo-cd-v1alpha1-resource-override-example
- key_count: 6
  name: Argo Cd V1Alpha1 Resource Ref Example
  slug: argo-cd-v1alpha1-resource-ref-example
- key_count: 11
  name: Argo Cd V1Alpha1 Resource Result Example
  slug: argo-cd-v1alpha1-resource-result-example
- key_count: 3
  name: Argo Cd V1Alpha1 Retry Strategy Example
  slug: argo-cd-v1alpha1-retry-strategy-example
- key_count: 8
  name: Argo Cd V1Alpha1 Revision History Example
  slug: argo-cd-v1alpha1-revision-history-example
- key_count: 6
  name: Argo Cd V1Alpha1 Revision Metadata Example
  slug: argo-cd-v1alpha1-revision-metadata-example
- key_count: 1
  name: Argo Cd V1Alpha1 Revision Reference Example
  slug: argo-cd-v1alpha1-revision-reference-example
- key_count: 4
  name: Argo Cd V1Alpha1 Scm Provider Generator Aws Code Commit Example
  slug: argo-cd-v1alpha1-scm-provider-generator-aws-code-commit-example
- key_count: 5
  name: Argo Cd V1Alpha1 Scm Provider Generator Azure Dev Ops Example
  slug: argo-cd-v1alpha1-scm-provider-generator-azure-dev-ops-example
- key_count: 4
  name: Argo Cd V1Alpha1 Scm Provider Generator Bitbucket Example
  slug: argo-cd-v1alpha1-scm-provider-generator-bitbucket-example
- key_count: 7
  name: Argo Cd V1Alpha1 Scm Provider Generator Bitbucket Server Example
  slug: argo-cd-v1alpha1-scm-provider-generator-bitbucket-server-example
- key_count: 12
  name: Argo Cd V1Alpha1 Scm Provider Generator Example
  slug: argo-cd-v1alpha1-scm-provider-generator-example
- key_count: 5
  name: Argo Cd V1Alpha1 Scm Provider Generator Filter Example
  slug: argo-cd-v1alpha1-scm-provider-generator-filter-example
- key_count: 6
  name: Argo Cd V1Alpha1 Scm Provider Generator Gitea Example
  slug: argo-cd-v1alpha1-scm-provider-generator-gitea-example
- key_count: 6
  name: Argo Cd V1Alpha1 Scm Provider Generator Github Example
  slug: argo-cd-v1alpha1-scm-provider-generator-github-example
- key_count: 10
  name: Argo Cd V1Alpha1 Scm Provider Generator Gitlab Example
  slug: argo-cd-v1alpha1-scm-provider-generator-gitlab-example
- key_count: 2
  name: Argo Cd V1Alpha1 Secret Ref Example
  slug: argo-cd-v1alpha1-secret-ref-example
- key_count: 1
  name: Argo Cd V1Alpha1 Signature Key Example
  slug: argo-cd-v1alpha1-signature-key-example
- key_count: 3
  name: Argo Cd V1Alpha1 Source Hydrator Example
  slug: argo-cd-v1alpha1-source-hydrator-example
- key_count: 2
  name: Argo Cd V1Alpha1 Source Hydrator Status Example
  slug: argo-cd-v1alpha1-source-hydrator-status-example
- key_count: 3
  name: Argo Cd V1Alpha1 Successful Hydrate Operation Example
  slug: argo-cd-v1alpha1-successful-hydrate-operation-example
- key_count: 11
  name: Argo Cd V1Alpha1 Sync Operation Example
  slug: argo-cd-v1alpha1-sync-operation-example
- key_count: 4
  name: Argo Cd V1Alpha1 Sync Operation Resource Example
  slug: argo-cd-v1alpha1-sync-operation-resource-example
- key_count: 6
  name: Argo Cd V1Alpha1 Sync Operation Result Example
  slug: argo-cd-v1alpha1-sync-operation-result-example
- key_count: 4
  name: Argo Cd V1Alpha1 Sync Policy Automated Example
  slug: argo-cd-v1alpha1-sync-policy-automated-example
- key_count: 4
  name: Argo Cd V1Alpha1 Sync Policy Example
  slug: argo-cd-v1alpha1-sync-policy-example
- key_count: 2
  name: Argo Cd V1Alpha1 Sync Source Example
  slug: argo-cd-v1alpha1-sync-source-example
- key_count: 4
  name: Argo Cd V1Alpha1 Sync Status Example
  slug: argo-cd-v1alpha1-sync-status-example
- key_count: 1
  name: Argo Cd V1Alpha1 Sync Strategy Apply Example
  slug: argo-cd-v1alpha1-sync-strategy-apply-example
- key_count: 2
  name: Argo Cd V1Alpha1 Sync Strategy Example
  slug: argo-cd-v1alpha1-sync-strategy-example
- key_count: 1
  name: Argo Cd V1Alpha1 Sync Strategy Hook Example
  slug: argo-cd-v1alpha1-sync-strategy-hook-example
- key_count: 11
  name: Argo Cd V1Alpha1 Sync Window Example
  slug: argo-cd-v1alpha1-sync-window-example
- key_count: 2
  name: Argo Cd V1Alpha1 Tag Filter Example
  slug: argo-cd-v1alpha1-tag-filter-example
- key_count: 5
  name: Argo Cd V1Alpha1 Tls Client Config Example
  slug: argo-cd-v1alpha1-tls-client-config-example
- key_count: 13
  name: Argo Cd Version Version Message Example
  slug: argo-cd-version-version-message-example
features:
- description: Defines application deployment state in Git repositories and automatically reconciles cluster state to match.
  name: Declarative GitOps Delivery
- description: Deploy and manage applications across multiple Kubernetes clusters from a single control plane.
  name: Multi-Cluster Deployment
- description: Automates creation of Argo CD Applications from templates across many clusters and namespaces.
  name: ApplicationSet Controller
- description: Supports Helm, Kustomize, Jsonnet, plain YAML, and custom plugins for application templating.
  name: Multiple Config Management Tools
- description: Fully-loaded graphical interface for visualizing application sync status, resource trees, and deployment history.
  name: Web UI
- description: Fine-grained role-based access control with project-level isolation for multi-team environments.
  name: RBAC and Multi-Tenancy
- description: Built-in SSO support for OIDC, OAuth2, LDAP, SAML 2.0, GitHub, GitLab, Microsoft, and LinkedIn.
  name: SSO Integration
- description: Continuously monitors Git and automatically syncs application state to match the desired state.
  name: Automated Sync
- description: PreSync, Sync, and PostSync hooks for complex rollout strategies including blue/green and canary.
  name: Sync Hooks
- description: Receives webhooks from GitHub, GitLab, and Bitbucket for instant sync on push events.
  name: Webhook Support
- description: Complete audit log of all deployment events and configuration changes.
  name: Audit Trail
- description: Built-in and custom health checks for Kubernetes resources to assess application health status.
  name: Health Assessment
- description: Configurable notifications via email, Slack, and other channels on sync events and health changes.
  name: Notifications
- description: Verifies GPG signatures on Git commits for enhanced supply chain security.
  name: GPG Commit Verification
finops:
- name: Argo Cd Finops
  service_category: API
  slug: argo-cd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argo-cd.png
integrations:
- description: Native support for Helm chart rendering and deployment with value overrides.
  name: Helm
- description: Native support for Kustomize overlays for environment-specific configuration.
  name: Kustomize
- description: Integrates with Vault for secret management using the argocd-vault-plugin.
  name: HashiCorp Vault
- description: Trigger Argo CD syncs or check sync status as part of GitHub Actions CI pipelines.
  name: GitHub Actions
- description: Integrate Argo CD sync steps into Jenkins CI/CD pipelines.
  name: Jenkins
- description: Exposes metrics for Prometheus scraping to monitor application sync health and performance.
  name: Prometheus
- description: Pre-built dashboards for visualizing Argo CD metrics in Grafana.
  name: Grafana
- description: Enforce admission policies via OPA and Gatekeeper before Argo CD syncs resources.
  name: Open Policy Agent
- description: Native integration with Argo Rollouts for progressive delivery (canary, blue/green).
  name: Argo Rollouts
- description: Trigger Argo Workflows as part of sync hooks for complex multi-step pipelines.
  name: Argo Workflows
- description: Send deployment notifications and alerts to Slack channels.
  name: Slack
- description: Manage applications on Amazon EKS clusters with AWS IAM authentication support.
  name: AWS EKS
- description: Deploy to Google Kubernetes Engine clusters with GKE authentication.
  name: Google GKE
- description: Manage applications on Azure Kubernetes Service with Azure AD authentication.
  name: Azure AKS
json_schemas:
- name: accountAccount
  property_count: 4
  slug: argo-cd-account-account
- name: accountAccountsList
  property_count: 1
  slug: argo-cd-account-accounts-list
- name: accountCanIResponse
  property_count: 1
  slug: argo-cd-account-can-i-response
- name: accountCreateTokenRequest
  property_count: 3
  slug: argo-cd-account-create-token-request
- name: accountCreateTokenResponse
  property_count: 1
  slug: argo-cd-account-create-token-response
- name: accountEmptyResponse
  property_count: 0
  slug: argo-cd-account-empty-response
- name: accountToken
  property_count: 3
  slug: argo-cd-account-token
- name: accountUpdatePasswordRequest
  property_count: 3
  slug: argo-cd-account-update-password-request
- name: accountUpdatePasswordResponse
  property_count: 0
  slug: argo-cd-account-update-password-response
- name: applicationApplicationManifestQueryWithFiles
  property_count: 4
  slug: argo-cd-application-application-manifest-query-with-files
- name: applicationApplicationManifestQueryWithFilesWrapper
  property_count: 2
  slug: argo-cd-application-application-manifest-query-with-files-wrapper
- name: applicationApplicationPatchRequest
  property_count: 5
  slug: argo-cd-application-application-patch-request
- name: applicationApplicationResourceResponse
  property_count: 1
  slug: argo-cd-application-application-resource-response
- name: applicationApplicationResponse
  property_count: 0
  slug: argo-cd-application-application-response
- name: applicationApplicationRollbackRequest
  property_count: 6
  slug: argo-cd-application-application-rollback-request
- name: applicationApplicationServerSideDiffResponse
  property_count: 2
  slug: argo-cd-application-application-server-side-diff-response
- name: applicationApplicationSyncRequest
  property_count: 14
  slug: argo-cd-application-application-sync-request
- name: applicationApplicationSyncWindow
  property_count: 4
  slug: argo-cd-application-application-sync-window
- name: applicationApplicationSyncWindowsResponse
  property_count: 3
  slug: argo-cd-application-application-sync-windows-response
- name: applicationFileChunk
  property_count: 1
  slug: argo-cd-application-file-chunk
- name: applicationLinkInfo
  property_count: 4
  slug: argo-cd-application-link-info
- name: applicationLinksResponse
  property_count: 1
  slug: argo-cd-application-links-response
- name: applicationLogEntry
  property_count: 5
  slug: argo-cd-application-log-entry
- name: applicationManagedResourcesResponse
  property_count: 1
  slug: argo-cd-application-managed-resources-response
- name: applicationOperationTerminateResponse
  property_count: 0
  slug: argo-cd-application-operation-terminate-response
- name: applicationResourceActionParameters
  property_count: 2
  slug: argo-cd-application-resource-action-parameters
- name: applicationResourceActionRunRequestV2
  property_count: 10
  slug: argo-cd-application-resource-action-run-request-v2
- name: applicationResourceActionsListResponse
  property_count: 1
  slug: argo-cd-application-resource-actions-list-response
- name: applicationSyncOptions
  property_count: 1
  slug: argo-cd-application-sync-options
- name: applicationsetApplicationSetGenerateRequest
  property_count: 1
  slug: argo-cd-applicationset-application-set-generate-request
- name: applicationsetApplicationSetGenerateResponse
  property_count: 1
  slug: argo-cd-applicationset-application-set-generate-response
- name: applicationsetApplicationSetResponse
  property_count: 2
  slug: argo-cd-applicationset-application-set-response
- name: applicationv1alpha1EnvEntry
  property_count: 2
  slug: argo-cd-applicationv1alpha1-env-entry
- name: applicationv1alpha1ResourceStatus
  property_count: 11
  slug: argo-cd-applicationv1alpha1-resource-status
- name: clusterClusterID
  property_count: 2
  slug: argo-cd-cluster-cluster-id
- name: clusterClusterResponse
  property_count: 0
  slug: argo-cd-cluster-cluster-response
- name: clusterConnector
  property_count: 2
  slug: argo-cd-cluster-connector
- name: clusterDexConfig
  property_count: 1
  slug: argo-cd-cluster-dex-config
- name: clusterGoogleAnalyticsConfig
  property_count: 2
  slug: argo-cd-cluster-google-analytics-config
- name: clusterHelp
  property_count: 3
  slug: argo-cd-cluster-help
- name: clusterOIDCConfig
  property_count: 7
  slug: argo-cd-cluster-oidc-config
- name: clusterPlugin
  property_count: 1
  slug: argo-cd-cluster-plugin
- name: clusterSettingsPluginsResponse
  property_count: 1
  slug: argo-cd-cluster-settings-plugins-response
- name: clusterSettings
  property_count: 29
  slug: argo-cd-cluster-settings
- name: gpgkeyGnuPGPublicKeyCreateResponse
  property_count: 2
  slug: argo-cd-gpgkey-gnu-pg-public-key-create-response
- name: gpgkeyGnuPGPublicKeyResponse
  property_count: 0
  slug: argo-cd-gpgkey-gnu-pg-public-key-response
- name: intstrIntOrString
  property_count: 3
  slug: argo-cd-intstr-int-or-string
- name: notificationServiceList
  property_count: 1
  slug: argo-cd-notification-service-list
- name: notificationService
  property_count: 1
  slug: argo-cd-notification-service
- name: notificationTemplateList
  property_count: 1
  slug: argo-cd-notification-template-list
- name: notificationTemplate
  property_count: 1
  slug: argo-cd-notification-template
- name: notificationTriggerList
  property_count: 1
  slug: argo-cd-notification-trigger-list
- name: notificationTrigger
  property_count: 1
  slug: argo-cd-notification-trigger
- name: oidcClaim
  property_count: 3
  slug: argo-cd-oidc-claim
- name: projectDetailedProjectsResponse
  property_count: 4
  slug: argo-cd-project-detailed-projects-response
- name: projectEmptyResponse
  property_count: 0
  slug: argo-cd-project-empty-response
- name: projectGlobalProjectsResponse
  property_count: 1
  slug: argo-cd-project-global-projects-response
- name: projectProjectCreateRequest
  property_count: 2
  slug: argo-cd-project-project-create-request
- name: projectProjectTokenCreateRequest
  property_count: 5
  slug: argo-cd-project-project-token-create-request
- name: projectProjectTokenResponse
  property_count: 1
  slug: argo-cd-project-project-token-response
- name: projectProjectUpdateRequest
  property_count: 1
  slug: argo-cd-project-project-update-request
- name: projectSyncWindowsResponse
  property_count: 1
  slug: argo-cd-project-sync-windows-response
- name: protobufAny
  property_count: 2
  slug: argo-cd-protobuf-any
- name: repocredsRepoCredsResponse
  property_count: 0
  slug: argo-cd-repocreds-repo-creds-response
- name: repositoryAppInfo
  property_count: 2
  slug: argo-cd-repository-app-info
- name: repositoryDirectoryAppSpec
  property_count: 0
  slug: argo-cd-repository-directory-app-spec
- name: repositoryHelmAppSpec
  property_count: 5
  slug: argo-cd-repository-helm-app-spec
- name: repositoryHelmChart
  property_count: 2
  slug: argo-cd-repository-helm-chart
- name: repositoryHelmChartsResponse
  property_count: 1
  slug: argo-cd-repository-helm-charts-response
- name: repositoryKustomizeAppSpec
  property_count: 1
  slug: argo-cd-repository-kustomize-app-spec
- name: repositoryManifestResponse
  property_count: 7
  slug: argo-cd-repository-manifest-response
- name: repositoryParameterAnnouncement
  property_count: 9
  slug: argo-cd-repository-parameter-announcement
- name: repositoryPluginAppSpec
  property_count: 1
  slug: argo-cd-repository-plugin-app-spec
- name: repositoryRefs
  property_count: 2
  slug: argo-cd-repository-refs
- name: repositoryRepoAppDetailsQuery
  property_count: 5
  slug: argo-cd-repository-repo-app-details-query
- name: repositoryRepoAppDetailsResponse
  property_count: 5
  slug: argo-cd-repository-repo-app-details-response
- name: repositoryRepoAppsResponse
  property_count: 1
  slug: argo-cd-repository-repo-apps-response
- name: repositoryRepoResponse
  property_count: 0
  slug: argo-cd-repository-repo-response
- name: runtimeError
  property_count: 4
  slug: argo-cd-runtime-error
- name: runtimeRawExtension
  property_count: 1
  slug: argo-cd-runtime-raw-extension
- name: runtimeStreamError
  property_count: 5
  slug: argo-cd-runtime-stream-error
- name: sessionGetUserInfoResponse
  property_count: 4
  slug: argo-cd-session-get-user-info-response
- name: sessionSessionCreateRequest
  property_count: 3
  slug: argo-cd-session-session-create-request
- name: sessionSessionResponse
  property_count: 1
  slug: argo-cd-session-session-response
- name: v1EventList
  property_count: 2
  slug: argo-cd-v1-event-list
- name: v1Event
  property_count: 15
  slug: argo-cd-v1-event
- name: v1EventSeries
  property_count: 2
  slug: argo-cd-v1-event-series
- name: v1EventSource
  property_count: 2
  slug: argo-cd-v1-event-source
- name: v1FieldsV1
  property_count: 1
  slug: argo-cd-v1-fields-v1
- name: v1GroupKind
  property_count: 2
  slug: argo-cd-v1-group-kind
- name: v1JSON
  property_count: 1
  slug: argo-cd-v1-json
- name: v1LabelSelectorRequirement
  property_count: 3
  slug: argo-cd-v1-label-selector-requirement
- name: v1LabelSelector
  property_count: 2
  slug: argo-cd-v1-label-selector
- name: v1ListMeta
  property_count: 4
  slug: argo-cd-v1-list-meta
- name: v1LoadBalancerIngress
  property_count: 4
  slug: argo-cd-v1-load-balancer-ingress
- name: v1ManagedFieldsEntry
  property_count: 7
  slug: argo-cd-v1-managed-fields-entry
- name: v1MicroTime
  property_count: 2
  slug: argo-cd-v1-micro-time
- name: v1NodeSwapStatus
  property_count: 1
  slug: argo-cd-v1-node-swap-status
- name: v1NodeSystemInfo
  property_count: 11
  slug: argo-cd-v1-node-system-info
- name: v1ObjectMeta
  property_count: 15
  slug: argo-cd-v1-object-meta
- name: v1ObjectReference
  property_count: 7
  slug: argo-cd-v1-object-reference
- name: v1OwnerReference
  property_count: 6
  slug: argo-cd-v1-owner-reference
- name: v1PortStatus
  property_count: 3
  slug: argo-cd-v1-port-status
- name: v1Time
  property_count: 0
  slug: argo-cd-v1-time
- name: v1alpha1AppHealthStatus
  property_count: 3
  slug: argo-cd-v1alpha1-app-health-status
- name: v1alpha1AppProjectList
  property_count: 2
  slug: argo-cd-v1alpha1-app-project-list
- name: v1alpha1AppProject
  property_count: 3
  slug: argo-cd-v1alpha1-app-project
- name: v1alpha1AppProjectSpec
  property_count: 14
  slug: argo-cd-v1alpha1-app-project-spec
- name: v1alpha1AppProjectStatus
  property_count: 1
  slug: argo-cd-v1alpha1-app-project-status
- name: v1alpha1ApplicationCondition
  property_count: 3
  slug: argo-cd-v1alpha1-application-condition
- name: v1alpha1ApplicationDestination
  property_count: 3
  slug: argo-cd-v1alpha1-application-destination
- name: v1alpha1ApplicationDestinationServiceAccount
  property_count: 3
  slug: argo-cd-v1alpha1-application-destination-service-account
- name: v1alpha1ApplicationList
  property_count: 2
  slug: argo-cd-v1alpha1-application-list
- name: v1alpha1ApplicationMatchExpression
  property_count: 3
  slug: argo-cd-v1alpha1-application-match-expression
- name: v1alpha1ApplicationPreservedFields
  property_count: 2
  slug: argo-cd-v1alpha1-application-preserved-fields
- name: v1alpha1Application
  property_count: 4
  slug: argo-cd-v1alpha1-application
- name: v1alpha1ApplicationSetApplicationStatus
  property_count: 6
  slug: argo-cd-v1alpha1-application-set-application-status
- name: v1alpha1ApplicationSetCondition
  property_count: 5
  slug: argo-cd-v1alpha1-application-set-condition
- name: v1alpha1ApplicationSetGenerator
  property_count: 10
  slug: argo-cd-v1alpha1-application-set-generator
- name: v1alpha1ApplicationSetList
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-list
- name: v1alpha1ApplicationSetNestedGenerator
  property_count: 10
  slug: argo-cd-v1alpha1-application-set-nested-generator
- name: v1alpha1ApplicationSetResourceIgnoreDifferences
  property_count: 3
  slug: argo-cd-v1alpha1-application-set-resource-ignore-differences
- name: v1alpha1ApplicationSetRolloutStep
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-rollout-step
- name: v1alpha1ApplicationSetRolloutStrategy
  property_count: 1
  slug: argo-cd-v1alpha1-application-set-rollout-strategy
- name: v1alpha1ApplicationSet
  property_count: 3
  slug: argo-cd-v1alpha1-application-set
- name: v1alpha1ApplicationSetSpec
  property_count: 10
  slug: argo-cd-v1alpha1-application-set-spec
- name: v1alpha1ApplicationSetStatus
  property_count: 5
  slug: argo-cd-v1alpha1-application-set-status
- name: v1alpha1ApplicationSetStrategy
  property_count: 3
  slug: argo-cd-v1alpha1-application-set-strategy
- name: v1alpha1ApplicationSetSyncPolicy
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-sync-policy
- name: v1alpha1ApplicationSetTemplateMeta
  property_count: 5
  slug: argo-cd-v1alpha1-application-set-template-meta
- name: v1alpha1ApplicationSetTemplate
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-template
- name: v1alpha1ApplicationSetTree
  property_count: 1
  slug: argo-cd-v1alpha1-application-set-tree
- name: v1alpha1ApplicationSetWatchEvent
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-watch-event
- name: v1alpha1ApplicationSourceDirectory
  property_count: 4
  slug: argo-cd-v1alpha1-application-source-directory
- name: v1alpha1ApplicationSourceHelm
  property_count: 15
  slug: argo-cd-v1alpha1-application-source-helm
- name: v1alpha1ApplicationSourceJsonnet
  property_count: 3
  slug: argo-cd-v1alpha1-application-source-jsonnet
- name: v1alpha1ApplicationSourceKustomize
  property_count: 18
  slug: argo-cd-v1alpha1-application-source-kustomize
- name: v1alpha1ApplicationSourcePluginParameter
  property_count: 4
  slug: argo-cd-v1alpha1-application-source-plugin-parameter
- name: v1alpha1ApplicationSourcePlugin
  property_count: 3
  slug: argo-cd-v1alpha1-application-source-plugin
- name: v1alpha1ApplicationSource
  property_count: 10
  slug: argo-cd-v1alpha1-application-source
- name: v1alpha1ApplicationSpec
  property_count: 9
  slug: argo-cd-v1alpha1-application-spec
- name: v1alpha1ApplicationStatus
  property_count: 14
  slug: argo-cd-v1alpha1-application-status
- name: v1alpha1ApplicationSummary
  property_count: 2
  slug: argo-cd-v1alpha1-application-summary
- name: v1alpha1ApplicationTree
  property_count: 4
  slug: argo-cd-v1alpha1-application-tree
- name: v1alpha1ApplicationWatchEvent
  property_count: 2
  slug: argo-cd-v1alpha1-application-watch-event
- name: v1alpha1AWSAuthConfig
  property_count: 3
  slug: argo-cd-v1alpha1-aws-auth-config
- name: v1alpha1Backoff
  property_count: 3
  slug: argo-cd-v1alpha1-backoff
- name: v1alpha1BasicAuthBitbucketServer
  property_count: 2
  slug: argo-cd-v1alpha1-basic-auth-bitbucket-server
- name: v1alpha1BearerTokenBitbucketCloud
  property_count: 1
  slug: argo-cd-v1alpha1-bearer-token-bitbucket-cloud
- name: v1alpha1BearerTokenBitbucket
  property_count: 1
  slug: argo-cd-v1alpha1-bearer-token-bitbucket
- name: v1alpha1ChartDetails
  property_count: 3
  slug: argo-cd-v1alpha1-chart-details
- name: v1alpha1ClusterCacheInfo
  property_count: 3
  slug: argo-cd-v1alpha1-cluster-cache-info
- name: v1alpha1ClusterConfig
  property_count: 8
  slug: argo-cd-v1alpha1-cluster-config
- name: v1alpha1ClusterGenerator
  property_count: 4
  slug: argo-cd-v1alpha1-cluster-generator
- name: v1alpha1ClusterInfo
  property_count: 5
  slug: argo-cd-v1alpha1-cluster-info
- name: v1alpha1ClusterList
  property_count: 2
  slug: argo-cd-v1alpha1-cluster-list
- name: v1alpha1ClusterResourceRestrictionItem
  property_count: 3
  slug: argo-cd-v1alpha1-cluster-resource-restriction-item
- name: v1alpha1Cluster
  property_count: 13
  slug: argo-cd-v1alpha1-cluster
- name: v1alpha1Command
  property_count: 2
  slug: argo-cd-v1alpha1-command
- name: v1alpha1CommitMetadata
  property_count: 6
  slug: argo-cd-v1alpha1-commit-metadata
- name: v1alpha1ComparedTo
  property_count: 4
  slug: argo-cd-v1alpha1-compared-to
- name: v1alpha1ConfigManagementPlugin
  property_count: 4
  slug: argo-cd-v1alpha1-config-management-plugin
- name: v1alpha1ConfigMapKeyRef
  property_count: 2
  slug: argo-cd-v1alpha1-config-map-key-ref
- name: v1alpha1ConnectionState
  property_count: 3
  slug: argo-cd-v1alpha1-connection-state
- name: v1alpha1DrySource
  property_count: 7
  slug: argo-cd-v1alpha1-dry-source
- name: v1alpha1DuckTypeGenerator
  property_count: 6
  slug: argo-cd-v1alpha1-duck-type-generator
- name: v1alpha1ExecProviderConfig
  property_count: 5
  slug: argo-cd-v1alpha1-exec-provider-config
- name: v1alpha1GitDirectoryGeneratorItem
  property_count: 2
  slug: argo-cd-v1alpha1-git-directory-generator-item
- name: v1alpha1GitFileGeneratorItem
  property_count: 2
  slug: argo-cd-v1alpha1-git-file-generator-item
- name: v1alpha1GitGenerator
  property_count: 8
  slug: argo-cd-v1alpha1-git-generator
- name: v1alpha1GnuPGPublicKeyList
  property_count: 2
  slug: argo-cd-v1alpha1-gnu-pg-public-key-list
- name: v1alpha1GnuPGPublicKey
  property_count: 6
  slug: argo-cd-v1alpha1-gnu-pg-public-key
- name: v1alpha1HealthStatus
  property_count: 3
  slug: argo-cd-v1alpha1-health-status
- name: v1alpha1HelmFileParameter
  property_count: 2
  slug: argo-cd-v1alpha1-helm-file-parameter
- name: v1alpha1HelmParameter
  property_count: 3
  slug: argo-cd-v1alpha1-helm-parameter
- name: v1alpha1HostInfo
  property_count: 4
  slug: argo-cd-v1alpha1-host-info
- name: v1alpha1HostResourceInfo
  property_count: 4
  slug: argo-cd-v1alpha1-host-resource-info
- name: v1alpha1HydrateOperation
  property_count: 7
  slug: argo-cd-v1alpha1-hydrate-operation
- name: v1alpha1HydrateTo
  property_count: 1
  slug: argo-cd-v1alpha1-hydrate-to
- name: v1alpha1InfoItem
  property_count: 2
  slug: argo-cd-v1alpha1-info-item
- name: v1alpha1Info
  property_count: 2
  slug: argo-cd-v1alpha1-info
- name: v1alpha1JsonnetVar
  property_count: 3
  slug: argo-cd-v1alpha1-jsonnet-var
- name: v1alpha1JWTToken
  property_count: 3
  slug: argo-cd-v1alpha1-jwt-token
- name: v1alpha1JWTTokens
  property_count: 1
  slug: argo-cd-v1alpha1-jwt-tokens
- name: v1alpha1KnownTypeField
  property_count: 2
  slug: argo-cd-v1alpha1-known-type-field
- name: v1alpha1KustomizeGvk
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-gvk
- name: v1alpha1KustomizeOptions
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-options
- name: v1alpha1KustomizePatch
  property_count: 4
  slug: argo-cd-v1alpha1-kustomize-patch
- name: v1alpha1KustomizeReplica
  property_count: 2
  slug: argo-cd-v1alpha1-kustomize-replica
- name: v1alpha1KustomizeResId
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-res-id
- name: v1alpha1KustomizeSelector
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-selector
- name: v1alpha1KustomizeVersion
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-version
- name: v1alpha1ListGenerator
  property_count: 3
  slug: argo-cd-v1alpha1-list-generator
- name: v1alpha1ManagedNamespaceMetadata
  property_count: 2
  slug: argo-cd-v1alpha1-managed-namespace-metadata
- name: v1alpha1MatrixGenerator
  property_count: 2
  slug: argo-cd-v1alpha1-matrix-generator
- name: v1alpha1MergeGenerator
  property_count: 3
  slug: argo-cd-v1alpha1-merge-generator
- name: v1alpha1OCIMetadata
  property_count: 7
  slug: argo-cd-v1alpha1-oci-metadata
- name: v1alpha1OperationInitiator
  property_count: 2
  slug: argo-cd-v1alpha1-operation-initiator
- name: v1alpha1Operation
  property_count: 4
  slug: argo-cd-v1alpha1-operation
- name: v1alpha1OperationState
  property_count: 7
  slug: argo-cd-v1alpha1-operation-state
- name: v1alpha1OrphanedResourceKey
  property_count: 3
  slug: argo-cd-v1alpha1-orphaned-resource-key
- name: v1alpha1OrphanedResourcesMonitorSettings
  property_count: 2
  slug: argo-cd-v1alpha1-orphaned-resources-monitor-settings
- name: v1alpha1OverrideIgnoreDiff
  property_count: 3
  slug: argo-cd-v1alpha1-override-ignore-diff
- name: v1alpha1PluginConfigMapRef
  property_count: 1
  slug: argo-cd-v1alpha1-plugin-config-map-ref
- name: v1alpha1PluginGenerator
  property_count: 5
  slug: argo-cd-v1alpha1-plugin-generator
- name: v1alpha1PluginInput
  property_count: 1
  slug: argo-cd-v1alpha1-plugin-input
- name: v1alpha1ProjectRole
  property_count: 5
  slug: argo-cd-v1alpha1-project-role
- name: v1alpha1PullRequestGeneratorAzureDevOps
  property_count: 6
  slug: argo-cd-v1alpha1-pull-request-generator-azure-dev-ops
- name: v1alpha1PullRequestGeneratorBitbucket
  property_count: 5
  slug: argo-cd-v1alpha1-pull-request-generator-bitbucket
- name: v1alpha1PullRequestGeneratorBitbucketServer
  property_count: 7
  slug: argo-cd-v1alpha1-pull-request-generator-bitbucket-server
- name: v1alpha1PullRequestGeneratorFilter
  property_count: 3
  slug: argo-cd-v1alpha1-pull-request-generator-filter
- name: v1alpha1PullRequestGeneratorGitLab
  property_count: 7
  slug: argo-cd-v1alpha1-pull-request-generator-git-lab
- name: v1alpha1PullRequestGeneratorGitea
  property_count: 6
  slug: argo-cd-v1alpha1-pull-request-generator-gitea
- name: v1alpha1PullRequestGeneratorGithub
  property_count: 6
  slug: argo-cd-v1alpha1-pull-request-generator-github
- name: v1alpha1PullRequestGenerator
  property_count: 11
  slug: argo-cd-v1alpha1-pull-request-generator
- name: v1alpha1RepoCredsList
  property_count: 2
  slug: argo-cd-v1alpha1-repo-creds-list
- name: v1alpha1RepoCreds
  property_count: 23
  slug: argo-cd-v1alpha1-repo-creds
- name: v1alpha1RepositoryCertificateList
  property_count: 2
  slug: argo-cd-v1alpha1-repository-certificate-list
- name: v1alpha1RepositoryCertificate
  property_count: 5
  slug: argo-cd-v1alpha1-repository-certificate
- name: v1alpha1RepositoryList
  property_count: 2
  slug: argo-cd-v1alpha1-repository-list
- name: v1alpha1Repository
  property_count: 32
  slug: argo-cd-v1alpha1-repository
- name: v1alpha1ResourceActionParam
  property_count: 1
  slug: argo-cd-v1alpha1-resource-action-param
- name: v1alpha1ResourceAction
  property_count: 5
  slug: argo-cd-v1alpha1-resource-action
- name: v1alpha1ResourceDiff
  property_count: 12
  slug: argo-cd-v1alpha1-resource-diff
- name: v1alpha1ResourceIgnoreDifferences
  property_count: 7
  slug: argo-cd-v1alpha1-resource-ignore-differences
- name: v1alpha1ResourceNetworkingInfo
  property_count: 5
  slug: argo-cd-v1alpha1-resource-networking-info
- name: v1alpha1ResourceNode
  property_count: 7
  slug: argo-cd-v1alpha1-resource-node
- name: v1alpha1ResourceOverride
  property_count: 6
  slug: argo-cd-v1alpha1-resource-override
- name: v1alpha1ResourceRef
  property_count: 6
  slug: argo-cd-v1alpha1-resource-ref
- name: v1alpha1ResourceResult
  property_count: 11
  slug: argo-cd-v1alpha1-resource-result
- name: v1alpha1RetryStrategy
  property_count: 3
  slug: argo-cd-v1alpha1-retry-strategy
- name: v1alpha1RevisionHistory
  property_count: 8
  slug: argo-cd-v1alpha1-revision-history
- name: v1alpha1RevisionMetadata
  property_count: 6
  slug: argo-cd-v1alpha1-revision-metadata
- name: v1alpha1RevisionReference
  property_count: 1
  slug: argo-cd-v1alpha1-revision-reference
- name: v1alpha1SCMProviderGeneratorAWSCodeCommit
  property_count: 4
  slug: argo-cd-v1alpha1-scm-provider-generator-aws-code-commit
- name: v1alpha1SCMProviderGeneratorAzureDevOps
  property_count: 5
  slug: argo-cd-v1alpha1-scm-provider-generator-azure-dev-ops
- name: v1alpha1SCMProviderGeneratorBitbucket
  property_count: 4
  slug: argo-cd-v1alpha1-scm-provider-generator-bitbucket
- name: v1alpha1SCMProviderGeneratorBitbucketServer
  property_count: 7
  slug: argo-cd-v1alpha1-scm-provider-generator-bitbucket-server
- name: v1alpha1SCMProviderGeneratorFilter
  property_count: 5
  slug: argo-cd-v1alpha1-scm-provider-generator-filter
- name: v1alpha1SCMProviderGeneratorGitea
  property_count: 6
  slug: argo-cd-v1alpha1-scm-provider-generator-gitea
- name: v1alpha1SCMProviderGeneratorGithub
  property_count: 6
  slug: argo-cd-v1alpha1-scm-provider-generator-github
- name: v1alpha1SCMProviderGeneratorGitlab
  property_count: 10
  slug: argo-cd-v1alpha1-scm-provider-generator-gitlab
- name: v1alpha1SCMProviderGenerator
  property_count: 12
  slug: argo-cd-v1alpha1-scm-provider-generator
- name: v1alpha1SecretRef
  property_count: 2
  slug: argo-cd-v1alpha1-secret-ref
- name: v1alpha1SignatureKey
  property_count: 1
  slug: argo-cd-v1alpha1-signature-key
- name: v1alpha1SourceHydrator
  property_count: 3
  slug: argo-cd-v1alpha1-source-hydrator
- name: v1alpha1SourceHydratorStatus
  property_count: 2
  slug: argo-cd-v1alpha1-source-hydrator-status
- name: v1alpha1SuccessfulHydrateOperation
  property_count: 3
  slug: argo-cd-v1alpha1-successful-hydrate-operation
- name: v1alpha1SyncOperationResource
  property_count: 4
  slug: argo-cd-v1alpha1-sync-operation-resource
- name: v1alpha1SyncOperationResult
  property_count: 6
  slug: argo-cd-v1alpha1-sync-operation-result
- name: v1alpha1SyncOperation
  property_count: 11
  slug: argo-cd-v1alpha1-sync-operation
- name: v1alpha1SyncPolicyAutomated
  property_count: 4
  slug: argo-cd-v1alpha1-sync-policy-automated
- name: v1alpha1SyncPolicy
  property_count: 4
  slug: argo-cd-v1alpha1-sync-policy
- name: v1alpha1SyncSource
  property_count: 2
  slug: argo-cd-v1alpha1-sync-source
- name: v1alpha1SyncStatus
  property_count: 4
  slug: argo-cd-v1alpha1-sync-status
- name: v1alpha1SyncStrategyApply
  property_count: 1
  slug: argo-cd-v1alpha1-sync-strategy-apply
- name: v1alpha1SyncStrategyHook
  property_count: 1
  slug: argo-cd-v1alpha1-sync-strategy-hook
- name: v1alpha1SyncStrategy
  property_count: 2
  slug: argo-cd-v1alpha1-sync-strategy
- name: v1alpha1SyncWindow
  property_count: 11
  slug: argo-cd-v1alpha1-sync-window
- name: v1alpha1TagFilter
  property_count: 2
  slug: argo-cd-v1alpha1-tag-filter
- name: v1alpha1TLSClientConfig
  property_count: 5
  slug: argo-cd-v1alpha1-tls-client-config
- name: versionVersionMessage
  property_count: 13
  slug: argo-cd-version-version-message
json_structures:
- name: Argo Cd Account Account Structure
  property_count: 4
  slug: argo-cd-account-account-structure
- name: Argo Cd Account Accounts List Structure
  property_count: 1
  slug: argo-cd-account-accounts-list-structure
- name: Argo Cd Account Can I Response Structure
  property_count: 1
  slug: argo-cd-account-can-i-response-structure
- name: Argo Cd Account Create Token Request Structure
  property_count: 3
  slug: argo-cd-account-create-token-request-structure
- name: Argo Cd Account Create Token Response Structure
  property_count: 1
  slug: argo-cd-account-create-token-response-structure
- name: Argo Cd Account Empty Response Structure
  property_count: 0
  slug: argo-cd-account-empty-response-structure
- name: Argo Cd Account Token Structure
  property_count: 3
  slug: argo-cd-account-token-structure
- name: Argo Cd Account Update Password Request Structure
  property_count: 3
  slug: argo-cd-account-update-password-request-structure
- name: Argo Cd Account Update Password Response Structure
  property_count: 0
  slug: argo-cd-account-update-password-response-structure
- name: Argo Cd Application Application Manifest Query With Files Structure
  property_count: 4
  slug: argo-cd-application-application-manifest-query-with-files-structure
- name: Argo Cd Application Application Manifest Query With Files Wrapper Structure
  property_count: 2
  slug: argo-cd-application-application-manifest-query-with-files-wrapper-structure
- name: Argo Cd Application Application Patch Request Structure
  property_count: 5
  slug: argo-cd-application-application-patch-request-structure
- name: Argo Cd Application Application Resource Response Structure
  property_count: 1
  slug: argo-cd-application-application-resource-response-structure
- name: Argo Cd Application Application Response Structure
  property_count: 0
  slug: argo-cd-application-application-response-structure
- name: Argo Cd Application Application Rollback Request Structure
  property_count: 6
  slug: argo-cd-application-application-rollback-request-structure
- name: Argo Cd Application Application Server Side Diff Response Structure
  property_count: 2
  slug: argo-cd-application-application-server-side-diff-response-structure
- name: Argo Cd Application Application Sync Request Structure
  property_count: 14
  slug: argo-cd-application-application-sync-request-structure
- name: Argo Cd Application Application Sync Window Structure
  property_count: 4
  slug: argo-cd-application-application-sync-window-structure
- name: Argo Cd Application Application Sync Windows Response Structure
  property_count: 3
  slug: argo-cd-application-application-sync-windows-response-structure
- name: Argo Cd Application File Chunk Structure
  property_count: 1
  slug: argo-cd-application-file-chunk-structure
- name: Argo Cd Application Link Info Structure
  property_count: 4
  slug: argo-cd-application-link-info-structure
- name: Argo Cd Application Links Response Structure
  property_count: 1
  slug: argo-cd-application-links-response-structure
- name: Argo Cd Application Log Entry Structure
  property_count: 5
  slug: argo-cd-application-log-entry-structure
- name: Argo Cd Application Managed Resources Response Structure
  property_count: 1
  slug: argo-cd-application-managed-resources-response-structure
- name: Argo Cd Application Operation Terminate Response Structure
  property_count: 0
  slug: argo-cd-application-operation-terminate-response-structure
- name: Argo Cd Application Resource Action Parameters Structure
  property_count: 2
  slug: argo-cd-application-resource-action-parameters-structure
- name: Argo Cd Application Resource Action Run Request V2 Structure
  property_count: 10
  slug: argo-cd-application-resource-action-run-request-v2-structure
- name: Argo Cd Application Resource Actions List Response Structure
  property_count: 1
  slug: argo-cd-application-resource-actions-list-response-structure
- name: Argo Cd Application Sync Options Structure
  property_count: 1
  slug: argo-cd-application-sync-options-structure
- name: Argo Cd Applicationset Application Set Generate Request Structure
  property_count: 1
  slug: argo-cd-applicationset-application-set-generate-request-structure
- name: Argo Cd Applicationset Application Set Generate Response Structure
  property_count: 1
  slug: argo-cd-applicationset-application-set-generate-response-structure
- name: Argo Cd Applicationset Application Set Response Structure
  property_count: 2
  slug: argo-cd-applicationset-application-set-response-structure
- name: Argo Cd Applicationv1Alpha1 Env Entry Structure
  property_count: 2
  slug: argo-cd-applicationv1alpha1-env-entry-structure
- name: Argo Cd Applicationv1Alpha1 Resource Status Structure
  property_count: 11
  slug: argo-cd-applicationv1alpha1-resource-status-structure
- name: Argo Cd Cluster Cluster Id Structure
  property_count: 2
  slug: argo-cd-cluster-cluster-id-structure
- name: Argo Cd Cluster Cluster Response Structure
  property_count: 0
  slug: argo-cd-cluster-cluster-response-structure
- name: Argo Cd Cluster Connector Structure
  property_count: 2
  slug: argo-cd-cluster-connector-structure
- name: Argo Cd Cluster Dex Config Structure
  property_count: 1
  slug: argo-cd-cluster-dex-config-structure
- name: Argo Cd Cluster Google Analytics Config Structure
  property_count: 2
  slug: argo-cd-cluster-google-analytics-config-structure
- name: Argo Cd Cluster Help Structure
  property_count: 3
  slug: argo-cd-cluster-help-structure
- name: Argo Cd Cluster Oidc Config Structure
  property_count: 7
  slug: argo-cd-cluster-oidc-config-structure
- name: Argo Cd Cluster Plugin Structure
  property_count: 1
  slug: argo-cd-cluster-plugin-structure
- name: Argo Cd Cluster Settings Plugins Response Structure
  property_count: 1
  slug: argo-cd-cluster-settings-plugins-response-structure
- name: Argo Cd Cluster Settings Structure
  property_count: 29
  slug: argo-cd-cluster-settings-structure
- name: Argo Cd Gpgkey Gnu Pg Public Key Create Response Structure
  property_count: 2
  slug: argo-cd-gpgkey-gnu-pg-public-key-create-response-structure
- name: Argo Cd Gpgkey Gnu Pg Public Key Response Structure
  property_count: 0
  slug: argo-cd-gpgkey-gnu-pg-public-key-response-structure
- name: Argo Cd Intstr Int Or String Structure
  property_count: 3
  slug: argo-cd-intstr-int-or-string-structure
- name: Argo Cd Notification Service List Structure
  property_count: 1
  slug: argo-cd-notification-service-list-structure
- name: Argo Cd Notification Service Structure
  property_count: 1
  slug: argo-cd-notification-service-structure
- name: Argo Cd Notification Template List Structure
  property_count: 1
  slug: argo-cd-notification-template-list-structure
- name: Argo Cd Notification Template Structure
  property_count: 1
  slug: argo-cd-notification-template-structure
- name: Argo Cd Notification Trigger List Structure
  property_count: 1
  slug: argo-cd-notification-trigger-list-structure
- name: Argo Cd Notification Trigger Structure
  property_count: 1
  slug: argo-cd-notification-trigger-structure
- name: Argo Cd Oidc Claim Structure
  property_count: 3
  slug: argo-cd-oidc-claim-structure
- name: Argo Cd Project Detailed Projects Response Structure
  property_count: 4
  slug: argo-cd-project-detailed-projects-response-structure
- name: Argo Cd Project Empty Response Structure
  property_count: 0
  slug: argo-cd-project-empty-response-structure
- name: Argo Cd Project Global Projects Response Structure
  property_count: 1
  slug: argo-cd-project-global-projects-response-structure
- name: Argo Cd Project Project Create Request Structure
  property_count: 2
  slug: argo-cd-project-project-create-request-structure
- name: Argo Cd Project Project Token Create Request Structure
  property_count: 5
  slug: argo-cd-project-project-token-create-request-structure
- name: Argo Cd Project Project Token Response Structure
  property_count: 1
  slug: argo-cd-project-project-token-response-structure
- name: Argo Cd Project Project Update Request Structure
  property_count: 1
  slug: argo-cd-project-project-update-request-structure
- name: Argo Cd Project Sync Windows Response Structure
  property_count: 1
  slug: argo-cd-project-sync-windows-response-structure
- name: Argo Cd Protobuf Any Structure
  property_count: 2
  slug: argo-cd-protobuf-any-structure
- name: Argo Cd Repocreds Repo Creds Response Structure
  property_count: 0
  slug: argo-cd-repocreds-repo-creds-response-structure
- name: Argo Cd Repository App Info Structure
  property_count: 2
  slug: argo-cd-repository-app-info-structure
- name: Argo Cd Repository Directory App Spec Structure
  property_count: 0
  slug: argo-cd-repository-directory-app-spec-structure
- name: Argo Cd Repository Helm App Spec Structure
  property_count: 5
  slug: argo-cd-repository-helm-app-spec-structure
- name: Argo Cd Repository Helm Chart Structure
  property_count: 2
  slug: argo-cd-repository-helm-chart-structure
- name: Argo Cd Repository Helm Charts Response Structure
  property_count: 1
  slug: argo-cd-repository-helm-charts-response-structure
- name: Argo Cd Repository Kustomize App Spec Structure
  property_count: 1
  slug: argo-cd-repository-kustomize-app-spec-structure
- name: Argo Cd Repository Manifest Response Structure
  property_count: 7
  slug: argo-cd-repository-manifest-response-structure
- name: Argo Cd Repository Parameter Announcement Structure
  property_count: 8
  slug: argo-cd-repository-parameter-announcement-structure
- name: Argo Cd Repository Plugin App Spec Structure
  property_count: 1
  slug: argo-cd-repository-plugin-app-spec-structure
- name: Argo Cd Repository Refs Structure
  property_count: 2
  slug: argo-cd-repository-refs-structure
- name: Argo Cd Repository Repo App Details Query Structure
  property_count: 5
  slug: argo-cd-repository-repo-app-details-query-structure
- name: Argo Cd Repository Repo App Details Response Structure
  property_count: 5
  slug: argo-cd-repository-repo-app-details-response-structure
- name: Argo Cd Repository Repo Apps Response Structure
  property_count: 1
  slug: argo-cd-repository-repo-apps-response-structure
- name: Argo Cd Repository Repo Response Structure
  property_count: 0
  slug: argo-cd-repository-repo-response-structure
- name: Argo Cd Runtime Error Structure
  property_count: 4
  slug: argo-cd-runtime-error-structure
- name: Argo Cd Runtime Raw Extension Structure
  property_count: 1
  slug: argo-cd-runtime-raw-extension-structure
- name: Argo Cd Runtime Stream Error Structure
  property_count: 5
  slug: argo-cd-runtime-stream-error-structure
- name: Argo Cd Session Get User Info Response Structure
  property_count: 4
  slug: argo-cd-session-get-user-info-response-structure
- name: Argo Cd Session Session Create Request Structure
  property_count: 3
  slug: argo-cd-session-session-create-request-structure
- name: Argo Cd Session Session Response Structure
  property_count: 1
  slug: argo-cd-session-session-response-structure
- name: Argo Cd V1 Event List Structure
  property_count: 2
  slug: argo-cd-v1-event-list-structure
- name: Argo Cd V1 Event Series Structure
  property_count: 2
  slug: argo-cd-v1-event-series-structure
- name: Argo Cd V1 Event Source Structure
  property_count: 2
  slug: argo-cd-v1-event-source-structure
- name: Argo Cd V1 Event Structure
  property_count: 15
  slug: argo-cd-v1-event-structure
- name: Argo Cd V1 Fields V1 Structure
  property_count: 1
  slug: argo-cd-v1-fields-v1-structure
- name: Argo Cd V1 Group Kind Structure
  property_count: 2
  slug: argo-cd-v1-group-kind-structure
- name: Argo Cd V1 Json Structure
  property_count: 1
  slug: argo-cd-v1-json-structure
- name: Argo Cd V1 Label Selector Requirement Structure
  property_count: 3
  slug: argo-cd-v1-label-selector-requirement-structure
- name: Argo Cd V1 Label Selector Structure
  property_count: 2
  slug: argo-cd-v1-label-selector-structure
- name: Argo Cd V1 List Meta Structure
  property_count: 4
  slug: argo-cd-v1-list-meta-structure
- name: Argo Cd V1 Load Balancer Ingress Structure
  property_count: 4
  slug: argo-cd-v1-load-balancer-ingress-structure
- name: Argo Cd V1 Managed Fields Entry Structure
  property_count: 7
  slug: argo-cd-v1-managed-fields-entry-structure
- name: Argo Cd V1 Micro Time Structure
  property_count: 2
  slug: argo-cd-v1-micro-time-structure
- name: Argo Cd V1 Node Swap Status Structure
  property_count: 1
  slug: argo-cd-v1-node-swap-status-structure
- name: Argo Cd V1 Node System Info Structure
  property_count: 11
  slug: argo-cd-v1-node-system-info-structure
- name: Argo Cd V1 Object Meta Structure
  property_count: 15
  slug: argo-cd-v1-object-meta-structure
- name: Argo Cd V1 Object Reference Structure
  property_count: 7
  slug: argo-cd-v1-object-reference-structure
- name: Argo Cd V1 Owner Reference Structure
  property_count: 6
  slug: argo-cd-v1-owner-reference-structure
- name: Argo Cd V1 Port Status Structure
  property_count: 3
  slug: argo-cd-v1-port-status-structure
- name: Argo Cd V1 Time Structure
  property_count: 0
  slug: argo-cd-v1-time-structure
- name: Argo Cd V1Alpha1 App Health Status Structure
  property_count: 3
  slug: argo-cd-v1alpha1-app-health-status-structure
- name: Argo Cd V1Alpha1 App Project List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-app-project-list-structure
- name: Argo Cd V1Alpha1 App Project Spec Structure
  property_count: 14
  slug: argo-cd-v1alpha1-app-project-spec-structure
- name: Argo Cd V1Alpha1 App Project Status Structure
  property_count: 1
  slug: argo-cd-v1alpha1-app-project-status-structure
- name: Argo Cd V1Alpha1 App Project Structure
  property_count: 3
  slug: argo-cd-v1alpha1-app-project-structure
- name: Argo Cd V1Alpha1 Application Condition Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-condition-structure
- name: Argo Cd V1Alpha1 Application Destination Service Account Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-destination-service-account-structure
- name: Argo Cd V1Alpha1 Application Destination Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-destination-structure
- name: Argo Cd V1Alpha1 Application List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-list-structure
- name: Argo Cd V1Alpha1 Application Match Expression Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-match-expression-structure
- name: Argo Cd V1Alpha1 Application Preserved Fields Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-preserved-fields-structure
- name: Argo Cd V1Alpha1 Application Set Application Status Structure
  property_count: 6
  slug: argo-cd-v1alpha1-application-set-application-status-structure
- name: Argo Cd V1Alpha1 Application Set Condition Structure
  property_count: 5
  slug: argo-cd-v1alpha1-application-set-condition-structure
- name: Argo Cd V1Alpha1 Application Set Generator Structure
  property_count: 10
  slug: argo-cd-v1alpha1-application-set-generator-structure
- name: Argo Cd V1Alpha1 Application Set List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-list-structure
- name: Argo Cd V1Alpha1 Application Set Nested Generator Structure
  property_count: 10
  slug: argo-cd-v1alpha1-application-set-nested-generator-structure
- name: Argo Cd V1Alpha1 Application Set Resource Ignore Differences Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-set-resource-ignore-differences-structure
- name: Argo Cd V1Alpha1 Application Set Rollout Step Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-rollout-step-structure
- name: Argo Cd V1Alpha1 Application Set Rollout Strategy Structure
  property_count: 1
  slug: argo-cd-v1alpha1-application-set-rollout-strategy-structure
- name: Argo Cd V1Alpha1 Application Set Spec Structure
  property_count: 10
  slug: argo-cd-v1alpha1-application-set-spec-structure
- name: Argo Cd V1Alpha1 Application Set Status Structure
  property_count: 5
  slug: argo-cd-v1alpha1-application-set-status-structure
- name: Argo Cd V1Alpha1 Application Set Strategy Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-set-strategy-structure
- name: Argo Cd V1Alpha1 Application Set Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-set-structure
- name: Argo Cd V1Alpha1 Application Set Sync Policy Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-sync-policy-structure
- name: Argo Cd V1Alpha1 Application Set Template Meta Structure
  property_count: 5
  slug: argo-cd-v1alpha1-application-set-template-meta-structure
- name: Argo Cd V1Alpha1 Application Set Template Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-template-structure
- name: Argo Cd V1Alpha1 Application Set Tree Structure
  property_count: 1
  slug: argo-cd-v1alpha1-application-set-tree-structure
- name: Argo Cd V1Alpha1 Application Set Watch Event Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-set-watch-event-structure
- name: Argo Cd V1Alpha1 Application Source Directory Structure
  property_count: 4
  slug: argo-cd-v1alpha1-application-source-directory-structure
- name: Argo Cd V1Alpha1 Application Source Helm Structure
  property_count: 15
  slug: argo-cd-v1alpha1-application-source-helm-structure
- name: Argo Cd V1Alpha1 Application Source Jsonnet Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-source-jsonnet-structure
- name: Argo Cd V1Alpha1 Application Source Kustomize Structure
  property_count: 18
  slug: argo-cd-v1alpha1-application-source-kustomize-structure
- name: Argo Cd V1Alpha1 Application Source Plugin Parameter Structure
  property_count: 4
  slug: argo-cd-v1alpha1-application-source-plugin-parameter-structure
- name: Argo Cd V1Alpha1 Application Source Plugin Structure
  property_count: 3
  slug: argo-cd-v1alpha1-application-source-plugin-structure
- name: Argo Cd V1Alpha1 Application Source Structure
  property_count: 10
  slug: argo-cd-v1alpha1-application-source-structure
- name: Argo Cd V1Alpha1 Application Spec Structure
  property_count: 9
  slug: argo-cd-v1alpha1-application-spec-structure
- name: Argo Cd V1Alpha1 Application Status Structure
  property_count: 14
  slug: argo-cd-v1alpha1-application-status-structure
- name: Argo Cd V1Alpha1 Application Structure
  property_count: 4
  slug: argo-cd-v1alpha1-application-structure
- name: Argo Cd V1Alpha1 Application Summary Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-summary-structure
- name: Argo Cd V1Alpha1 Application Tree Structure
  property_count: 4
  slug: argo-cd-v1alpha1-application-tree-structure
- name: Argo Cd V1Alpha1 Application Watch Event Structure
  property_count: 2
  slug: argo-cd-v1alpha1-application-watch-event-structure
- name: Argo Cd V1Alpha1 Aws Auth Config Structure
  property_count: 3
  slug: argo-cd-v1alpha1-aws-auth-config-structure
- name: Argo Cd V1Alpha1 Backoff Structure
  property_count: 3
  slug: argo-cd-v1alpha1-backoff-structure
- name: Argo Cd V1Alpha1 Basic Auth Bitbucket Server Structure
  property_count: 2
  slug: argo-cd-v1alpha1-basic-auth-bitbucket-server-structure
- name: Argo Cd V1Alpha1 Bearer Token Bitbucket Cloud Structure
  property_count: 1
  slug: argo-cd-v1alpha1-bearer-token-bitbucket-cloud-structure
- name: Argo Cd V1Alpha1 Bearer Token Bitbucket Structure
  property_count: 1
  slug: argo-cd-v1alpha1-bearer-token-bitbucket-structure
- name: Argo Cd V1Alpha1 Chart Details Structure
  property_count: 3
  slug: argo-cd-v1alpha1-chart-details-structure
- name: Argo Cd V1Alpha1 Cluster Cache Info Structure
  property_count: 3
  slug: argo-cd-v1alpha1-cluster-cache-info-structure
- name: Argo Cd V1Alpha1 Cluster Config Structure
  property_count: 8
  slug: argo-cd-v1alpha1-cluster-config-structure
- name: Argo Cd V1Alpha1 Cluster Generator Structure
  property_count: 4
  slug: argo-cd-v1alpha1-cluster-generator-structure
- name: Argo Cd V1Alpha1 Cluster Info Structure
  property_count: 5
  slug: argo-cd-v1alpha1-cluster-info-structure
- name: Argo Cd V1Alpha1 Cluster List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-cluster-list-structure
- name: Argo Cd V1Alpha1 Cluster Resource Restriction Item Structure
  property_count: 3
  slug: argo-cd-v1alpha1-cluster-resource-restriction-item-structure
- name: Argo Cd V1Alpha1 Cluster Structure
  property_count: 13
  slug: argo-cd-v1alpha1-cluster-structure
- name: Argo Cd V1Alpha1 Command Structure
  property_count: 2
  slug: argo-cd-v1alpha1-command-structure
- name: Argo Cd V1Alpha1 Commit Metadata Structure
  property_count: 6
  slug: argo-cd-v1alpha1-commit-metadata-structure
- name: Argo Cd V1Alpha1 Compared To Structure
  property_count: 4
  slug: argo-cd-v1alpha1-compared-to-structure
- name: Argo Cd V1Alpha1 Config Management Plugin Structure
  property_count: 4
  slug: argo-cd-v1alpha1-config-management-plugin-structure
- name: Argo Cd V1Alpha1 Config Map Key Ref Structure
  property_count: 2
  slug: argo-cd-v1alpha1-config-map-key-ref-structure
- name: Argo Cd V1Alpha1 Connection State Structure
  property_count: 3
  slug: argo-cd-v1alpha1-connection-state-structure
- name: Argo Cd V1Alpha1 Dry Source Structure
  property_count: 7
  slug: argo-cd-v1alpha1-dry-source-structure
- name: Argo Cd V1Alpha1 Duck Type Generator Structure
  property_count: 6
  slug: argo-cd-v1alpha1-duck-type-generator-structure
- name: Argo Cd V1Alpha1 Exec Provider Config Structure
  property_count: 5
  slug: argo-cd-v1alpha1-exec-provider-config-structure
- name: Argo Cd V1Alpha1 Git Directory Generator Item Structure
  property_count: 2
  slug: argo-cd-v1alpha1-git-directory-generator-item-structure
- name: Argo Cd V1Alpha1 Git File Generator Item Structure
  property_count: 2
  slug: argo-cd-v1alpha1-git-file-generator-item-structure
- name: Argo Cd V1Alpha1 Git Generator Structure
  property_count: 8
  slug: argo-cd-v1alpha1-git-generator-structure
- name: Argo Cd V1Alpha1 Gnu Pg Public Key List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-gnu-pg-public-key-list-structure
- name: Argo Cd V1Alpha1 Gnu Pg Public Key Structure
  property_count: 6
  slug: argo-cd-v1alpha1-gnu-pg-public-key-structure
- name: Argo Cd V1Alpha1 Health Status Structure
  property_count: 3
  slug: argo-cd-v1alpha1-health-status-structure
- name: Argo Cd V1Alpha1 Helm File Parameter Structure
  property_count: 2
  slug: argo-cd-v1alpha1-helm-file-parameter-structure
- name: Argo Cd V1Alpha1 Helm Parameter Structure
  property_count: 3
  slug: argo-cd-v1alpha1-helm-parameter-structure
- name: Argo Cd V1Alpha1 Host Info Structure
  property_count: 4
  slug: argo-cd-v1alpha1-host-info-structure
- name: Argo Cd V1Alpha1 Host Resource Info Structure
  property_count: 4
  slug: argo-cd-v1alpha1-host-resource-info-structure
- name: Argo Cd V1Alpha1 Hydrate Operation Structure
  property_count: 7
  slug: argo-cd-v1alpha1-hydrate-operation-structure
- name: Argo Cd V1Alpha1 Hydrate To Structure
  property_count: 1
  slug: argo-cd-v1alpha1-hydrate-to-structure
- name: Argo Cd V1Alpha1 Info Item Structure
  property_count: 2
  slug: argo-cd-v1alpha1-info-item-structure
- name: Argo Cd V1Alpha1 Info Structure
  property_count: 2
  slug: argo-cd-v1alpha1-info-structure
- name: Argo Cd V1Alpha1 Jsonnet Var Structure
  property_count: 3
  slug: argo-cd-v1alpha1-jsonnet-var-structure
- name: Argo Cd V1Alpha1 Jwt Token Structure
  property_count: 3
  slug: argo-cd-v1alpha1-jwt-token-structure
- name: Argo Cd V1Alpha1 Jwt Tokens Structure
  property_count: 1
  slug: argo-cd-v1alpha1-jwt-tokens-structure
- name: Argo Cd V1Alpha1 Known Type Field Structure
  property_count: 2
  slug: argo-cd-v1alpha1-known-type-field-structure
- name: Argo Cd V1Alpha1 Kustomize Gvk Structure
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-gvk-structure
- name: Argo Cd V1Alpha1 Kustomize Options Structure
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-options-structure
- name: Argo Cd V1Alpha1 Kustomize Patch Structure
  property_count: 4
  slug: argo-cd-v1alpha1-kustomize-patch-structure
- name: Argo Cd V1Alpha1 Kustomize Replica Structure
  property_count: 2
  slug: argo-cd-v1alpha1-kustomize-replica-structure
- name: Argo Cd V1Alpha1 Kustomize Res Id Structure
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-res-id-structure
- name: Argo Cd V1Alpha1 Kustomize Selector Structure
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-selector-structure
- name: Argo Cd V1Alpha1 Kustomize Version Structure
  property_count: 3
  slug: argo-cd-v1alpha1-kustomize-version-structure
- name: Argo Cd V1Alpha1 List Generator Structure
  property_count: 3
  slug: argo-cd-v1alpha1-list-generator-structure
- name: Argo Cd V1Alpha1 Managed Namespace Metadata Structure
  property_count: 2
  slug: argo-cd-v1alpha1-managed-namespace-metadata-structure
- name: Argo Cd V1Alpha1 Matrix Generator Structure
  property_count: 2
  slug: argo-cd-v1alpha1-matrix-generator-structure
- name: Argo Cd V1Alpha1 Merge Generator Structure
  property_count: 3
  slug: argo-cd-v1alpha1-merge-generator-structure
- name: Argo Cd V1Alpha1 Oci Metadata Structure
  property_count: 7
  slug: argo-cd-v1alpha1-oci-metadata-structure
- name: Argo Cd V1Alpha1 Operation Initiator Structure
  property_count: 2
  slug: argo-cd-v1alpha1-operation-initiator-structure
- name: Argo Cd V1Alpha1 Operation State Structure
  property_count: 7
  slug: argo-cd-v1alpha1-operation-state-structure
- name: Argo Cd V1Alpha1 Operation Structure
  property_count: 4
  slug: argo-cd-v1alpha1-operation-structure
- name: Argo Cd V1Alpha1 Orphaned Resource Key Structure
  property_count: 3
  slug: argo-cd-v1alpha1-orphaned-resource-key-structure
- name: Argo Cd V1Alpha1 Orphaned Resources Monitor Settings Structure
  property_count: 2
  slug: argo-cd-v1alpha1-orphaned-resources-monitor-settings-structure
- name: Argo Cd V1Alpha1 Override Ignore Diff Structure
  property_count: 3
  slug: argo-cd-v1alpha1-override-ignore-diff-structure
- name: Argo Cd V1Alpha1 Plugin Config Map Ref Structure
  property_count: 1
  slug: argo-cd-v1alpha1-plugin-config-map-ref-structure
- name: Argo Cd V1Alpha1 Plugin Generator Structure
  property_count: 5
  slug: argo-cd-v1alpha1-plugin-generator-structure
- name: Argo Cd V1Alpha1 Plugin Input Structure
  property_count: 1
  slug: argo-cd-v1alpha1-plugin-input-structure
- name: Argo Cd V1Alpha1 Project Role Structure
  property_count: 5
  slug: argo-cd-v1alpha1-project-role-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Azure Dev Ops Structure
  property_count: 6
  slug: argo-cd-v1alpha1-pull-request-generator-azure-dev-ops-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Bitbucket Server Structure
  property_count: 7
  slug: argo-cd-v1alpha1-pull-request-generator-bitbucket-server-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Bitbucket Structure
  property_count: 5
  slug: argo-cd-v1alpha1-pull-request-generator-bitbucket-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Filter Structure
  property_count: 3
  slug: argo-cd-v1alpha1-pull-request-generator-filter-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Git Lab Structure
  property_count: 7
  slug: argo-cd-v1alpha1-pull-request-generator-git-lab-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Gitea Structure
  property_count: 6
  slug: argo-cd-v1alpha1-pull-request-generator-gitea-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Github Structure
  property_count: 6
  slug: argo-cd-v1alpha1-pull-request-generator-github-structure
- name: Argo Cd V1Alpha1 Pull Request Generator Structure
  property_count: 11
  slug: argo-cd-v1alpha1-pull-request-generator-structure
- name: Argo Cd V1Alpha1 Repo Creds List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-repo-creds-list-structure
- name: Argo Cd V1Alpha1 Repo Creds Structure
  property_count: 23
  slug: argo-cd-v1alpha1-repo-creds-structure
- name: Argo Cd V1Alpha1 Repository Certificate List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-repository-certificate-list-structure
- name: Argo Cd V1Alpha1 Repository Certificate Structure
  property_count: 5
  slug: argo-cd-v1alpha1-repository-certificate-structure
- name: Argo Cd V1Alpha1 Repository List Structure
  property_count: 2
  slug: argo-cd-v1alpha1-repository-list-structure
- name: Argo Cd V1Alpha1 Repository Structure
  property_count: 32
  slug: argo-cd-v1alpha1-repository-structure
- name: Argo Cd V1Alpha1 Resource Action Param Structure
  property_count: 1
  slug: argo-cd-v1alpha1-resource-action-param-structure
- name: Argo Cd V1Alpha1 Resource Action Structure
  property_count: 5
  slug: argo-cd-v1alpha1-resource-action-structure
- name: Argo Cd V1Alpha1 Resource Diff Structure
  property_count: 12
  slug: argo-cd-v1alpha1-resource-diff-structure
- name: Argo Cd V1Alpha1 Resource Ignore Differences Structure
  property_count: 7
  slug: argo-cd-v1alpha1-resource-ignore-differences-structure
- name: Argo Cd V1Alpha1 Resource Networking Info Structure
  property_count: 5
  slug: argo-cd-v1alpha1-resource-networking-info-structure
- name: Argo Cd V1Alpha1 Resource Node Structure
  property_count: 7
  slug: argo-cd-v1alpha1-resource-node-structure
- name: Argo Cd V1Alpha1 Resource Override Structure
  property_count: 6
  slug: argo-cd-v1alpha1-resource-override-structure
- name: Argo Cd V1Alpha1 Resource Ref Structure
  property_count: 6
  slug: argo-cd-v1alpha1-resource-ref-structure
- name: Argo Cd V1Alpha1 Resource Result Structure
  property_count: 11
  slug: argo-cd-v1alpha1-resource-result-structure
- name: Argo Cd V1Alpha1 Retry Strategy Structure
  property_count: 3
  slug: argo-cd-v1alpha1-retry-strategy-structure
- name: Argo Cd V1Alpha1 Revision History Structure
  property_count: 8
  slug: argo-cd-v1alpha1-revision-history-structure
- name: Argo Cd V1Alpha1 Revision Metadata Structure
  property_count: 6
  slug: argo-cd-v1alpha1-revision-metadata-structure
- name: Argo Cd V1Alpha1 Revision Reference Structure
  property_count: 1
  slug: argo-cd-v1alpha1-revision-reference-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Aws Code Commit Structure
  property_count: 4
  slug: argo-cd-v1alpha1-scm-provider-generator-aws-code-commit-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Azure Dev Ops Structure
  property_count: 5
  slug: argo-cd-v1alpha1-scm-provider-generator-azure-dev-ops-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Bitbucket Server Structure
  property_count: 7
  slug: argo-cd-v1alpha1-scm-provider-generator-bitbucket-server-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Bitbucket Structure
  property_count: 4
  slug: argo-cd-v1alpha1-scm-provider-generator-bitbucket-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Filter Structure
  property_count: 5
  slug: argo-cd-v1alpha1-scm-provider-generator-filter-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Gitea Structure
  property_count: 6
  slug: argo-cd-v1alpha1-scm-provider-generator-gitea-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Github Structure
  property_count: 6
  slug: argo-cd-v1alpha1-scm-provider-generator-github-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Gitlab Structure
  property_count: 10
  slug: argo-cd-v1alpha1-scm-provider-generator-gitlab-structure
- name: Argo Cd V1Alpha1 Scm Provider Generator Structure
  property_count: 12
  slug: argo-cd-v1alpha1-scm-provider-generator-structure
- name: Argo Cd V1Alpha1 Secret Ref Structure
  property_count: 2
  slug: argo-cd-v1alpha1-secret-ref-structure
- name: Argo Cd V1Alpha1 Signature Key Structure
  property_count: 1
  slug: argo-cd-v1alpha1-signature-key-structure
- name: Argo Cd V1Alpha1 Source Hydrator Status Structure
  property_count: 2
  slug: argo-cd-v1alpha1-source-hydrator-status-structure
- name: Argo Cd V1Alpha1 Source Hydrator Structure
  property_count: 3
  slug: argo-cd-v1alpha1-source-hydrator-structure
- name: Argo Cd V1Alpha1 Successful Hydrate Operation Structure
  property_count: 3
  slug: argo-cd-v1alpha1-successful-hydrate-operation-structure
- name: Argo Cd V1Alpha1 Sync Operation Resource Structure
  property_count: 4
  slug: argo-cd-v1alpha1-sync-operation-resource-structure
- name: Argo Cd V1Alpha1 Sync Operation Result Structure
  property_count: 6
  slug: argo-cd-v1alpha1-sync-operation-result-structure
- name: Argo Cd V1Alpha1 Sync Operation Structure
  property_count: 11
  slug: argo-cd-v1alpha1-sync-operation-structure
- name: Argo Cd V1Alpha1 Sync Policy Automated Structure
  property_count: 4
  slug: argo-cd-v1alpha1-sync-policy-automated-structure
- name: Argo Cd V1Alpha1 Sync Policy Structure
  property_count: 4
  slug: argo-cd-v1alpha1-sync-policy-structure
- name: Argo Cd V1Alpha1 Sync Source Structure
  property_count: 2
  slug: argo-cd-v1alpha1-sync-source-structure
- name: Argo Cd V1Alpha1 Sync Status Structure
  property_count: 4
  slug: argo-cd-v1alpha1-sync-status-structure
- name: Argo Cd V1Alpha1 Sync Strategy Apply Structure
  property_count: 1
  slug: argo-cd-v1alpha1-sync-strategy-apply-structure
- name: Argo Cd V1Alpha1 Sync Strategy Hook Structure
  property_count: 1
  slug: argo-cd-v1alpha1-sync-strategy-hook-structure
- name: Argo Cd V1Alpha1 Sync Strategy Structure
  property_count: 2
  slug: argo-cd-v1alpha1-sync-strategy-structure
- name: Argo Cd V1Alpha1 Sync Window Structure
  property_count: 11
  slug: argo-cd-v1alpha1-sync-window-structure
- name: Argo Cd V1Alpha1 Tag Filter Structure
  property_count: 2
  slug: argo-cd-v1alpha1-tag-filter-structure
- name: Argo Cd V1Alpha1 Tls Client Config Structure
  property_count: 5
  slug: argo-cd-v1alpha1-tls-client-config-structure
- name: Argo Cd Version Version Message Structure
  property_count: 13
  slug: argo-cd-version-version-message-structure
jsonld:
- class_count: 10
  name: Argo Cd Account Context
  property_count: 12
  slug: argo-cd-account-context
- class_count: 24
  name: Argo Cd Application Context
  property_count: 43
  slug: argo-cd-application-context
- class_count: 3
  name: Argo Cd Applicationset Context
  property_count: 4
  slug: argo-cd-applicationset-context
- class_count: 4
  name: Argo Cd Applicationv1Alpha1 Context
  property_count: 10
  slug: argo-cd-applicationv1alpha1-context
- class_count: 12
  name: Argo Cd Cluster Context
  property_count: 42
  slug: argo-cd-cluster-context
- class_count: 2
  name: Argo Cd Gpgkey Context
  property_count: 2
  slug: argo-cd-gpgkey-context
- class_count: 1
  name: Argo Cd Intstr Context
  property_count: 3
  slug: argo-cd-intstr-context
- class_count: 7
  name: Argo Cd Notification Context
  property_count: 1
  slug: argo-cd-notification-context
- class_count: 1
  name: Argo Cd Oidc Context
  property_count: 3
  slug: argo-cd-oidc-context
- class_count: 9
  name: Argo Cd Project Context
  property_count: 11
  slug: argo-cd-project-context
- class_count: 1
  name: Argo Cd Protobuf Context
  property_count: 2
  slug: argo-cd-protobuf-context
- class_count: 1
  name: Argo Cd Repocreds Context
  property_count: 0
  slug: argo-cd-repocreds-context
- class_count: 15
  name: Argo Cd Repository Context
  property_count: 36
  slug: argo-cd-repository-context
- class_count: 3
  name: Argo Cd Runtime Context
  property_count: 8
  slug: argo-cd-runtime-context
- class_count: 3
  name: Argo Cd Session Context
  property_count: 6
  slug: argo-cd-session-context
- class_count: 20
  name: Argo Cd V1 Context
  property_count: 75
  slug: argo-cd-v1-context
- class_count: 161
  name: Argo Cd V1Alpha1 Context
  property_count: 378
  slug: argo-cd-v1alpha1-context
- class_count: 1
  name: Argo Cd Version Context
  property_count: 13
  slug: argo-cd-version-context
layout: provider
modified: '2026-05-19'
name: Argo CD
nav: Providers
network: true
overview: 'Argo CD publishes 13 APIs on the [APIs.io](https://apis.io/) network, including AccountService API, ApplicationService API, ApplicationSetService API, and 10 more. Tagged areas include Continuous Delivery, Containers, Deployment, GitOps, and Kubernetes.


  The Argo CD catalog on APIs.io includes 18 JSON-LD contexts and 2 Spectral governance rulesets.


  Argo CD''s developer surface includes authentication, documentation, getting-started guide, engineering blog, release notes, changelog, CLI, and 10 more developer resources.'
plans:
- name: Argo Cd Plans Pricing
  plan_count: 3
  slug: argo-cd-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Argo Cd Rate Limits
  slug: argo-cd-rate-limits
rules:
- name: Argo CD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: argo-cd-jsonschema-spectral-rules
- name: Argo CD API Rules
  rule_count: 21
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 11
  slug: argo-cd-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 25.8
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argo-cd/refs/heads/main/screenshots/argo-cd-2026-06-20T172417.png
security:
- kind: authentication
  name: Argo Cd Authentication
  slug: argo-cd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Argo Cd Domain Security
  slug: argo-cd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: argo-cd
tags:
- Continuous Delivery
- Containers
- Deployment
- GitOps
- Kubernetes
- CNCF
- Open Source
use_cases:
- description: Automate application releases to Kubernetes clusters with every Git commit triggering a reconciliation cycle.
  name: Continuous Deployment to Kubernetes
- description: Promote application versions across dev, staging, and production environments using Git branch strategies.
  name: Multi-Environment Promotion
- description: Manage application deployments consistently across dozens of Kubernetes clusters from a central Argo CD instance.
  name: Multi-Cluster GitOps
- description: Automatically deploy infrastructure add-ons (CNI, CSI, monitoring) to all clusters using ApplicationSet.
  name: Cluster Add-On Management
- description: Allow development teams to manage their own applications within project-scoped RBAC boundaries.
  name: Tenant Self-Service
- description: Quickly restore application state to any prior Git commit in case of production incidents.
  name: Disaster Recovery
- description: Maintain a complete audit trail of all deployment changes via Git history and Argo CD event logs.
  name: Compliance and Auditability
website: https://argoproj.github.io/cd/
---
