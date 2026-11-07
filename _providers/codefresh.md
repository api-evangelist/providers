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
  - '{''url'': ''https://codefresh.io'', ''status'': 301, ''note'': ''declared website redirects to https://octopus.com/codefresh — a different registrable domain (codefresh.io -> octopus.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 3
  name: Codefresh Agentic Access
  operation_count: 27
  slug: codefresh-agentic-access
  summary_line: 27 operations · 11 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: REST API for managing Codefresh pipelines, builds, clusters, environments, repositories, and audit data. Authentication uses API key tokens passed via the Authorization header, with granular scopes in
  name: Codefresh REST API
  slug: rest-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Accounts API from Codefresh — 1 operation(s) for accounts.
  name: Codefresh Accounts API
  slug: codefresh-accounts-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Annotations API from Codefresh — 1 operation(s) for annotations.
  name: Codefresh Annotations API
  slug: codefresh-annotations-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Audit API from Codefresh — 1 operation(s) for audit.
  name: Codefresh Audit API
  slug: codefresh-audit-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Builds API from Codefresh — 2 operation(s) for builds.
  name: Codefresh Builds API
  slug: codefresh-builds-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Clusters API from Codefresh — 1 operation(s) for clusters.
  name: Codefresh Clusters API
  slug: codefresh-clusters-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Contexts API from Codefresh — 1 operation(s) for contexts.
  name: Codefresh Contexts API
  slug: codefresh-contexts-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Environments API from Codefresh — 1 operation(s) for environments.
  name: Codefresh Environments API
  slug: codefresh-environments-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Features API from Codefresh — 1 operation(s) for features.
  name: Codefresh Features API
  slug: codefresh-features-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The Helm API from Codefresh — 2 operation(s) for helm.
  name: Codefresh Helm API
  slug: codefresh-helm-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: abac
  name: Codefresh Abac API
  slug: codefresh-abac-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The account API from Codefresh — 1 operation(s) for account.
  name: Codefresh Account API
  slug: codefresh-account-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The accounts.getArchiveList API from Codefresh — 1 operation(s) for accounts.getarchivelist.
  name: Codefresh Accounts.get Archive List API
  slug: codefresh-accounts-getarchivelist-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: Manage and serve Codefresh Runners
  name: Codefresh Agents API
  slug: codefresh-agents-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The analytic API from Codefresh — 1 operation(s) for analytic.
  name: Codefresh Analytic API
  slug: codefresh-analytic-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: Approval
  name: Codefresh Approval API
  slug: codefresh-approval-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The charts API from Codefresh — 1 operation(s) for charts.
  name: Codefresh Charts API
  slug: codefresh-charts-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: compositions
  name: Codefresh Compositions API
  slug: codefresh-compositions-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The customer API from Codefresh — 3 operation(s) for customer.
  name: Codefresh Customer API
  slug: codefresh-customer-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The customers API from Codefresh — 10 operation(s) for customers.
  name: Codefresh Customers API
  slug: codefresh-customers-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The download API from Codefresh — 1 operation(s) for download.
  name: Codefresh Download API
  slug: codefresh-download-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: environments v2
  name: Codefresh Environments V2 API
  slug: codefresh-environments-v2-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: Execution Contexts
  name: Codefresh Execution Contexts API
  slug: codefresh-execution-contexts-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The favorites API from Codefresh — 3 operation(s) for favorites.
  name: Codefresh Favorites API
  slug: codefresh-favorites-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The form-metadata API from Codefresh — 4 operation(s) for form-metadata.
  name: Codefresh Form Metadata API
  slug: codefresh-form-metadata-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: Gitops
  name: Codefresh Gitops API
  slug: codefresh-gitops-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The gitops-application API from Codefresh — 5 operation(s) for gitops-application.
  name: Codefresh Gitops Application API
  slug: codefresh-gitops-application-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The helm.board-pipelines-config API from Codefresh — 1 operation(s) for helm.board-pipelines-config.
  name: Codefresh Helm.board Pipelines Config API
  slug: codefresh-helm-board-pipelines-config-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: helm.boards
  name: Codefresh Helm Boards API
  slug: codefresh-helm-boards-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: helm.charts
  name: Codefresh Helm Charts API
  slug: codefresh-helm-charts-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: helm.cluster-config
  name: Codefresh Helm Cluster Configs API
  slug: codefresh-helm-cluster-configs-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The helm.release-config API from Codefresh — 1 operation(s) for helm.release-config.
  name: Codefresh Helm.release Config API
  slug: codefresh-helm-release-config-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: helm.releases
  name: Codefresh Helm Releases API
  slug: codefresh-helm-releases-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: helm.repos
  name: Codefresh Helm Repos API
  slug: codefresh-helm-repos-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: helm.sections
  name: Codefresh Helm Sections API
  slug: codefresh-helm-sections-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The idp API from Codefresh — 3 operation(s) for idp.
  name: Codefresh Idp API
  slug: codefresh-idp-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: images
  name: Codefresh Images API
  slug: codefresh-images-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: kubernetes
  name: Codefresh Kubernetes API
  slug: codefresh-kubernetes-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: OpenID Connect (OIDC)
  name: Codefresh OIDC API
  slug: codefresh-oidc-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: pipelines
  name: Codefresh Pipelines API
  slug: codefresh-pipelines-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: Platform Analytics
  name: Codefresh Platform Analytics API
  slug: codefresh-platform-analytics-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: progress
  name: Codefresh Progress API
  slug: codefresh-progress-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: projects
  name: Codefresh Projects API
  slug: codefresh-projects-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: providers
  name: Codefresh Providers API
  slug: codefresh-providers-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: registries
  name: Codefresh Registries API
  slug: codefresh-registries-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: repos
  name: Codefresh Repos API
  slug: codefresh-repos-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The runner-installation API from Codefresh — 2 operation(s) for runner-installation.
  name: Codefresh Runner Installation API
  slug: codefresh-runner-installation-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: onPrem.runtimeEnvs.account
  name: Codefresh Runtime Environments (Account) API
  slug: codefresh-runtime-environments-account-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: runtimeEnvs
  name: Codefresh Runtime Environments API
  slug: codefresh-runtime-environments-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: onPrem.runtimeEnvs.plan
  name: Codefresh Runtime Environments (Plan) API
  slug: codefresh-runtime-environments-plan-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: onPrem.runtimeEnvs.system
  name: Codefresh Runtime Environments (System) API
  slug: codefresh-runtime-environments-system-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The runtimeEnvs.health-check API from Codefresh — 1 operation(s) for runtimeenvs.health-check.
  name: Codefresh Runtime Envs.health Check API
  slug: codefresh-runtimeenvs-health-check-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The segment API from Codefresh — 1 operation(s) for segment.
  name: Codefresh Segment API
  slug: codefresh-segment-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The service-users API from Codefresh — 3 operation(s) for service-users.
  name: Codefresh Service Users API
  slug: codefresh-service-users-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: step-types
  name: Codefresh Step Types API
  slug: codefresh-step-types-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: teams
  name: Codefresh Teams API
  slug: codefresh-teams-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: tokens
  name: Codefresh Tokens API
  slug: codefresh-tokens-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: Only for registry, helm and cron triggers
  name: Codefresh Triggers API
  slug: codefresh-triggers-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: triggers.events
  name: Codefresh Triggers Events API
  slug: codefresh-triggers-events-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: triggers.types
  name: Codefresh Triggers Types API
  slug: codefresh-triggers-types-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The user API from Codefresh — 6 operation(s) for user.
  name: Codefresh User API
  slug: codefresh-user-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The verification API from Codefresh — 2 operation(s) for verification.
  name: Codefresh Verification API
  slug: codefresh-verification-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: views
  name: Codefresh Views API
  slug: codefresh-views-api
- baseURL: https://g.codefresh.io/api
  baseurl_source: declared
  description: The whereami API from Codefresh — 1 operation(s) for whereami.
  name: Codefresh Whereami API
  slug: codefresh-whereami-api
artifact_total: 82
collections:
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
- group: other
  href: https://artifacts.apis.io/codefresh/capabilities/codefresh-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/codefresh-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/codefresh/agentic-access/codefresh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/codefresh-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/codefresh/security/codefresh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codefresh-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/codefresh/authentication/codefresh-authentication.yml
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
overview: 'Codefresh publishes 64 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Annotations API, Audit API, and 61 more. Tagged areas include CI/CD, Continuous Delivery, GitOps, Argo, and Kubernetes.


  The Codefresh catalog on APIs.io includes 1 Spectral governance ruleset.


  Codefresh''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Codefresh API Rules
  rule_count: 57
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 14
  slug: codefresh-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 49.3
    developer_ergonomics: 31.0
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 81.8
      total: 77
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/codefresh/codefresh-2026-06-20T174700.png
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
- Developer Tools
website: https://codefresh.io
---
