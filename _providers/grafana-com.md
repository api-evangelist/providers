---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 167
  human_in_the_loop: 23
  name: Grafana Com Agentic Access
  operation_count: 314
  slug: grafana-com-agentic-access
  summary_line: 314 operations · 167 acting · 23 human-in-the-loop
api_count: 1
apis:
- description: Manage Grafana Cloud stacks (instances), plugins, data sources, regions, access policies, and tokens at `https://grafana.com/api`. Authenticated with Cloud Access Policy bearer tokens. The recommended
  name: Grafana Cloud API
  slug: grafana-cloud-api
- description: Query and push logs to Grafana Loki. Endpoints include `/loki/api/v1/push` (log ingestion), `/loki/api/v1/query` and `/query_range` (LogQL), `/loki/api/v1/labels`, `/loki/api/v1/series`, `/loki/api/v1
  name: Grafana Loki HTTP API
  slug: loki-http-api
- description: Horizontally scalable, multi-tenant, long-term Prometheus-compatible metrics storage. Exposes Prometheus remote-write at `/api/v1/push`, the full Prometheus query API (`/api/v1/query`, `/query_range`,
  name: Grafana Mimir HTTP API
  slug: mimir-http-api
- description: High-volume, minimal-dependency distributed tracing backend. Supports OTLP ingestion, trace lookup by ID (`/api/traces/{traceID}`), TraceQL search (`/api/search`), tag and value listing, and metrics d
  name: Grafana Tempo HTTP API
  slug: tempo-http-api
- description: 'Continuous profiling backend. Ingest pprof and Pyroscope-format CPU, memory, and lock profiles, query flame graphs and merge profiles, and run profile-based comparisons. Pyroscope merged with Grafana '
  name: Grafana Pyroscope HTTP API
  slug: pyroscope-http-api
- description: Programmatically trigger, list, and manage cloud-hosted k6 load tests, projects, organizations, test runs, thresholds, and results. Pairs with the open-source `k6` CLI for JavaScript-authored performa
  name: Grafana k6 Cloud API
  slug: k6-cloud-api
- description: Programmatic access to OnCall alert groups, integrations, escalation chains, schedules, on-call shifts, routes, slack channels, webhooks, and users. Powers on-call rotation management and alert routin
  name: Grafana OnCall API
  slug: oncall-api
- description: Create and manage synthetic probes (HTTP, HTTPS, DNS, TCP, ICMP/ping, traceroute, multi-step scripted browser, gRPC) executed from Grafana Labs' global probe network plus optional private probes. Resu
  name: Grafana Synthetic Monitoring API
  slug: synthetic-monitoring-api
- baseURL: /api
  baseurl_source: spec
  description: 'The API can be used to create, update, get and list roles, and create or remove built-in role assignments. To use the API, you would need to enable fine-grained access control. This only available in '
  name: Grafana Access Control API
  slug: grafana-com-access-control-api
- baseURL: /api
  baseurl_source: spec
  description: The Admin HTTP API does not currently work with an API Token. API Tokens are currently only linked to an organization and an organization role. They cannot be given the permission of server admin, onl
  name: Grafana Admin API
  slug: grafana-com-admin-api
- baseURL: /api
  baseurl_source: spec
  description: The admin_ldap API from Grafana — 5 operation(s) for admin_ldap.
  name: Grafana Admin Ldap API
  slug: grafana-com-admin-ldap-api
- baseURL: /api
  baseurl_source: spec
  description: The admin_provisioning API from Grafana — 4 operation(s) for admin_provisioning.
  name: Grafana Admin Provisioning API
  slug: grafana-com-admin-provisioning-api
- baseURL: /api
  baseurl_source: spec
  description: The admin_users API from Grafana — 11 operation(s) for admin_users.
  name: Grafana Admin Users API
  slug: grafana-com-admin-users-api
- baseURL: /api
  baseurl_source: spec
  description: Grafana Annotations feature released in Grafana 4.6. Annotations are saved in the Grafana database (sqlite, mysql or postgres). Annotations can be organization annotations that can be shown on any das
  name: Grafana Annotations API
  slug: grafana-com-annotations-api
- baseURL: /api
  baseurl_source: spec
  description: The convert_prometheus API from Grafana — 6 operation(s) for convert_prometheus.
  name: Grafana Convert Prometheus API
  slug: grafana-com-convert-prometheus-api
- baseURL: /api
  baseurl_source: spec
  description: The correlations API from Grafana — 4 operation(s) for correlations.
  name: Grafana Correlations API
  slug: grafana-com-correlations-api
- baseURL: /api
  baseurl_source: spec
  description: The dashboard_public API from Grafana — 6 operation(s) for dashboard_public.
  name: Grafana Dashboard Public API
  slug: grafana-com-dashboard-public-api
- baseURL: /api
  baseurl_source: spec
  description: The dashboards API from Grafana — 20 operation(s) for dashboards.
  name: Grafana Dashboards API
  slug: grafana-com-dashboards-api
- baseURL: /api
  baseurl_source: spec
  description: The devices API from Grafana — 2 operation(s) for devices.
  name: Grafana Devices API
  slug: grafana-com-devices-api
- baseURL: /api
  baseurl_source: spec
  description: These are only available in Grafana Enterprise
  name: Grafana Enterprise API
  slug: grafana-com-enterprise-api
- baseURL: /api
  baseurl_source: spec
  description: 'Folders are identified by the identifier (id) and the unique identifier (uid). The identifier (id) of a folder is an auto-incrementing numeric value and is only unique per Grafana install. The unique '
  name: Grafana Folders API
  slug: grafana-com-folders-api
- baseURL: /api
  baseurl_source: spec
  description: The health API from Grafana — 2 operation(s) for health.
  name: Grafana Health API
  slug: grafana-com-health-api
- baseURL: /api
  baseurl_source: spec
  description: The invites API from Grafana — 2 operation(s) for invites.
  name: Grafana Invites API
  slug: grafana-com-invites-api
- baseURL: /api
  baseurl_source: spec
  description: The identifier (ID) of a library element is an auto-incrementing numeric value that is unique per Grafana install. The unique identifier (UID) of a library element uniquely identifies library elements
  name: Grafana Library Elements API
  slug: grafana-com-library-elements-api
- baseURL: /api
  baseurl_source: spec
  description: 'Licensing is only available in Grafana Enterprise. Read more about Grafana Enterprise. If you are running Grafana Enterprise and have Fine-grained access control enabled, for some endpoints you would '
  name: Grafana Licensing API
  slug: grafana-com-licensing-api
- baseURL: /api
  baseurl_source: spec
  description: The migrations API from Grafana — 10 operation(s) for migrations.
  name: Grafana Migrations API
  slug: grafana-com-migrations-api
- baseURL: /api
  baseurl_source: spec
  description: If you are running Grafana Enterprise and have Fine-grained access control enabled, for some endpoints you would need to have relevant permissions. Refer to specific resources to understand what permi
  name: Grafana Org API
  slug: grafana-com-org-api
- baseURL: /api
  baseurl_source: spec
  description: The Admin Organizations HTTP API does not currently work with an API Token. API Tokens are currently only linked to an organization and an organization role. They cannot be given the permission of ser
  name: Grafana Orgs API
  slug: grafana-com-orgs-api
- baseURL: /api
  baseurl_source: spec
  description: Permissions with `folderId=-1` are the default permissions for users with the Viewer and Editor roles. Permissions can be set for a user, a team or a role (Viewer or Editor). Permissions cannot be set
  name: Grafana Permissions API
  slug: grafana-com-permissions-api
- baseURL: /api
  baseurl_source: spec
  description: The playlists API from Grafana — 3 operation(s) for playlists.
  name: Grafana Playlists API
  slug: grafana-com-playlists-api
- baseURL: /api
  baseurl_source: spec
  description: The preferences API from Grafana — 3 operation(s) for preferences.
  name: Grafana Preferences API
  slug: grafana-com-preferences-api
- baseURL: /api
  baseurl_source: spec
  description: The provisioning API from Grafana — 17 operation(s) for provisioning.
  name: Grafana Provisioning API
  slug: grafana-com-provisioning-api
- baseURL: /api
  baseurl_source: spec
  description: 'The identifier (ID) of a query in query history is an auto-incrementing numeric value that is unique per Grafana install. The unique identifier (UID) of a query history uniquely identifies queries in '
  name: Grafana Query History API
  slug: grafana-com-query-history-api
- baseURL: /api
  baseurl_source: spec
  description: The quota API from Grafana — 6 operation(s) for quota.
  name: Grafana Quota API
  slug: grafana-com-quota-api
- baseURL: /api
  baseurl_source: spec
  description: The recording_rules API from Grafana — 4 operation(s) for recording_rules.
  name: Grafana Recording Rules API
  slug: grafana-com-recording-rules-api
- baseURL: /api
  baseurl_source: spec
  description: This API allows you to interact programmatically with the Reporting feature. Reporting is only available in Grafana Enterprise. Read more about Grafana Enterprise. If you have Fine-grained access Cont
  name: Grafana Reports API
  slug: grafana-com-reports-api
- baseURL: /api
  baseurl_source: spec
  description: The saml API from Grafana — 4 operation(s) for saml.
  name: Grafana SAML API
  slug: grafana-com-saml-api
- baseURL: /api
  baseurl_source: spec
  description: The search API from Grafana — 2 operation(s) for search.
  name: Grafana Search API
  slug: grafana-com-search-api
- baseURL: /api
  baseurl_source: spec
  description: If you are running Grafana Enterprise, for some endpoints you'll need to have specific permissions. Refer to [Role-based access control permissions](https://grafana.com/docs/grafana/latest/administrat
  name: Grafana Service Accounts API
  slug: grafana-com-service-accounts-api
- baseURL: /api
  baseurl_source: spec
  description: The signed_in_user API from Grafana — 10 operation(s) for signed_in_user.
  name: Grafana Signed In User API
  slug: grafana-com-signed-in-user-api
- baseURL: /api
  baseurl_source: spec
  description: The signing_keys API from Grafana — 1 operation(s) for signing_keys.
  name: Grafana Signing Keys API
  slug: grafana-com-signing-keys-api
- baseURL: /api
  baseurl_source: spec
  description: The snapshots API from Grafana — 5 operation(s) for snapshots.
  name: Grafana Snapshots API
  slug: grafana-com-snapshots-api
- baseURL: /api
  baseurl_source: spec
  description: The sso_settings API from Grafana — 2 operation(s) for sso_settings.
  name: Grafana SSO Settings API
  slug: grafana-com-sso-settings-api
- baseURL: /api
  baseurl_source: spec
  description: The sync_team_groups API from Grafana — 2 operation(s) for sync_team_groups.
  name: Grafana Sync Team Groups API
  slug: grafana-com-sync-team-groups-api
- baseURL: /api
  baseurl_source: spec
  description: This API can be used to create/update/delete Teams and to add/remove users to Teams. All actions require that the user has the Admin role for the organization.
  name: Grafana Teams API
  slug: grafana-com-teams-api
- baseURL: /api
  baseurl_source: spec
  description: The user API from Grafana — 1 operation(s) for user.
  name: Grafana User API
  slug: grafana-com-user-api
- baseURL: /api
  baseurl_source: spec
  description: The users API from Grafana — 6 operation(s) for users.
  name: Grafana Users API
  slug: grafana-com-users-api
- baseURL: /api
  baseurl_source: spec
  description: The versions API from Grafana — 3 operation(s) for versions.
  name: Grafana Versions API
  slug: grafana-com-versions-api
- baseURL: /api
  baseurl_source: spec
  description: If you are running Grafana Enterprise and have Fine-grained access control enabled, for some endpoints you would need to have relevant permissions. Refer to specific resources to understand what permi
  name: Grafana Data Sources API
  slug: grafana-com-data-sources-api
artifact_total: 97
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/agentic-access/grafana-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/grafana-com-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/finops/grafana-com-finops.yml
  title: ''
  type: FinOps
  url: finops/grafana-com-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/rate-limits/grafana-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/grafana-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/plans/grafana-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/grafana-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/rules/grafana-com-rules.yml
  title: ''
  type: Spectral
  url: rules/grafana-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/vocabulary/grafana-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/grafana-com-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/data-model/grafana-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/grafana-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/changelog/grafana-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/grafana-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.grafana.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/security/grafana-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/grafana-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/authentication/grafana-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grafana-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/errors/grafana-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grafana-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/conformance/grafana-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grafana-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/llms/grafana-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grafana-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/well-known/grafana-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/grafana-com-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/well-known/grafana-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grafana-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/hosts/grafana-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grafana-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/vendors/grafana-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grafana-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://grafana.com/press/
- group: start
  title: ''
  type: Login
  url: https://grafana.com/auth/sign-in/
- group: start
  title: ''
  type: GettingStarted
  url: https://grafana.com/docs/learning-paths/grafana-cloud-onboarding
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/security/grafana-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/grafana-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.grafana.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/security/grafana-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/grafana-com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/security/grafana-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grafana-com-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://grafana.com
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana-cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana/latest/developers/http_api/
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/grafana/grafana/blob/main/public/api-merged.json
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana/latest/developers/
- group: auth
  title: ''
  type: Authentication
  url: https://grafana.com/docs/grafana/latest/developers/http_api/authentication/
- group: auth
  title: ''
  type: Authentication
  url: https://grafana.com/docs/grafana-cloud/account-management/authentication-and-permissions/access-policies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grafana
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/grafana
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/grafana/dashboards/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/grafana/plugins/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/plugins/
- group: build
  title: ''
  type: Tools
  url: https://grafana.com/developers/plugin-tools/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/developers/scenes
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/developers/saga-design-system/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-foundation-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-openapi-client-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-api-golang-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/terraform-provider-grafana
- group: docs
  title: ''
  type: Documentation
  url: https://registry.terraform.io/providers/grafana/grafana/latest/docs
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/grafana-operator
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/helm-charts
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/grafana-image-renderer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafonnet
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/grizzly
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/loki
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/mimir
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/tempo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/pyroscope
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/k6
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/alloy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/beyla
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/faro-web-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/oncall
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/synthetic-monitoring-agent
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-plugin-sdk-go
- group: commercial
  title: ''
  type: Pricing
  url: https://grafana.com/pricing/
- group: commercial
  title: ''
  type: Pricing
  url: https://grafana.com/pricing/
- group: operate
  title: ''
  type: RateLimits
  url: https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/configure-rate-limit-data-source/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grafana.com
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/categories/engineering/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/about/team/
- group: other
  title: ''
  type: Events
  url: https://grafana.com/about/events/
- group: other
  title: ''
  type: Events
  url: https://grafana.com/events/grafanacon/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grafana.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grafana.com/legal/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.grafana.com/
- group: start
  title: ''
  type: Signup
  url: https://grafana.com/auth/sign-up
- group: start
  title: ''
  type: Portal
  url: https://grafana.com/products/cloud/
- group: start
  title: ''
  type: Portal
  url: https://grafana.com/products/enterprise/
- group: start
  title: ''
  type: Sandbox
  url: https://grafana.com/play/
- group: operate
  title: ''
  type: Forums
  url: https://community.grafana.com/
- group: operate
  title: ''
  type: Support
  url: https://grafana.com/contact
- group: operate
  title: ''
  type: Forums
  url: https://github.com/grafana/grafana/discussions
- group: learn
  title: ''
  type: Training
  url: https://grafana.com/tutorials/
- group: learn
  title: ''
  type: Training
  url: https://university.grafana.com/
- group: design
  title: ''
  type: Versioning
  url: https://grafana.com/docs/release-life-cycle/
- group: operate
  title: ''
  type: ChangeLog
  url: https://grafana.com/docs/grafana/latest/whatsnew/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/about/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grafana-labs
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/grafana
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Grafana
- group: company
  title: ''
  type: Mastodon
  url: https://fosstodon.org/@grafana
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.grafana.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-25T00:00:00.000Z'
description: Grafana Labs builds the open and composable observability stack used by millions of engineers to visualize, query, alert on, and explore their metrics, logs, traces, and profiles. The flagship Grafana OSS dashboarding platform is paired with Grafana Loki (logs), Grafana Mimir (Prometheus-compatible metrics), Grafana Tempo (distributed traces), and Grafana Pyroscope (continuous profiling) — all under the LGTM stack. Grafana Cloud delivers the entire portfolio as a managed SaaS with a generous free tier, while Grafana Enterprise extends self-managed deployments with premium plugins, reporting, RBAC, LBAC, and caching. The ecosystem extends to Grafana k6 (load testing), Grafana Alloy (OpenTelemetry-native collector), Grafana Beyla (eBPF auto-instrumentation), Grafana Faro (frontend observability), Grafana OnCall (incident response), and Synthetic Monitoring. A canonical OpenAPI specification at public/api-merged.json powers the official Go client, the Terraform provider, the Grafana
  Operator, and a deep dashboards-as-code toolchain (Foundation SDK, Grafonnet, Grizzly, Scenes).
features:
- Open-source Grafana — composable observability and dashboarding platform (AGPLv3)
- Grafana Cloud — fully managed observability SaaS with free tier
- Grafana Enterprise — self-managed commercial distribution with premium plugins and features
- Grafana Loki — Prometheus-style label model applied to logs with LogQL query language
- Grafana Mimir — horizontally scalable, multi-tenant, long-term Prometheus-compatible metrics storage
- Grafana Tempo — minimal-dependency distributed tracing backend with TraceQL search
- Grafana Pyroscope — continuous profiling backend (CPU, memory, lock, goroutine)
- Grafana k6 — JavaScript-authored load and performance testing with Cloud execution
- Grafana Alloy — OpenTelemetry-native distribution of the OpenTelemetry Collector
- Grafana Beyla — eBPF-based zero-instrumentation observability for HTTP/gRPC/SQL services
- Grafana Faro — frontend observability SDK for real user monitoring
- Grafana OnCall — on-call scheduling, escalation, and alert routing
- Grafana Incident and IRM (Incident Response Management) suite
- Grafana SLO — declarative service level objectives backed by Prometheus
- Grafana Synthetic Monitoring — global probe network for HTTP, DNS, TCP, ICMP, scripted browser, gRPC
- Grafana Application Observability — OpenTelemetry-driven APM
- Grafana Kubernetes Monitoring — preconfigured Kubernetes observability stack
- Adaptive Metrics — automated cardinality reduction (up to 80% savings)
- Adaptive Logs — log volume reduction (~50%)
- Adaptive Telemetry — unified Adaptive Metrics / Logs / Traces cost optimization
- 150+ data sources (Prometheus, InfluxDB, Elasticsearch, OpenSearch, MySQL, Postgres, MSSQL, CloudWatch, Azure Monitor, Google Cloud Monitoring, Snowflake, Splunk, Datadog, BigQuery, MongoDB, and more)
- 500+ community plugins (panels, data sources, apps)
- Library panels and library variables for reusable dashboard components
- Dashboards-as-code via Foundation SDK, Grafonnet, Grizzly, and Terraform Provider
- Grafana Operator for Kubernetes-native dashboard, alert, and data source provisioning
- Scenes framework for composable dashboard authoring
- Plugin SDK and create-plugin (plugin-tools) for community and enterprise plugin development
- RBAC with custom roles, service accounts, and folder/dashboard/data source permission grants
- SSO via SAML, OAuth, LDAP with team sync
- Public dashboards and snapshot sharing
- OpenTelemetry-first ingestion via Alloy with OTLP, Prometheus remote write, Loki, and Tempo protocols
- Unified Alerting with rule provisioning API, contact points, mute timings, notification templates
- Correlations between data sources for click-through pivots across metrics, logs, traces, profiles
- Data source Label-Based Access Control (LBAC) for tenant isolation
- Query and resource caching (Enterprise)
- Scheduled PDF/CSV reporting (Enterprise)
- Federal Cloud, Public Cloud, and Bring Your Own Cloud deployment options
- FedRAMP Moderate, SOC 2 Type II, PCI DSS, GDPR, HIPAA-eligible compliance posture
- Canonical OpenAPI 2.0 specification (api-merged.json) drives Go client, Terraform provider, and SDKs
finops:
- name: Grafana Com Finops
  service_category: Observability and Monitoring
  slug: grafana-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grafana-com.png
layout: provider
modified: '2026-05-25'
name: Grafana
nav: Providers
network: true
overview: 'Grafana publishes 49 APIs on the [APIs.io](https://apis.io/) network, including Access Control API, Admin API, Admin Ldap API, and 46 more. Tagged areas include Observability, Monitoring, Dashboards, Logs, and Metrics.


  The Grafana catalog on APIs.io includes 1 Spectral governance ruleset.


  Grafana''s developer surface includes changelog, authentication, getting-started guide, developer portal, documentation, tooling, pricing, and 85 more developer resources.'
plans:
- name: Grafana Com Plans Pricing
  plan_count: 5
  slug: grafana-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 7
  name: Grafana Com Rate Limits
  slug: grafana-com-rate-limits
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Grafana API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 6
  slug: grafana-com-rules
score:
  band: exemplar
  composite: 71.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.4
    catalog_earned_first_party: 0.0
    catalog_gap: 52.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.7
  facets:
    access_clarity: 96.8
    contract_governance: 22.0
    contract_quality: 47.3
    developer_ergonomics: 75.6
    discoverability: 66.1
    operational_transparency: 75.8
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/screenshots/grafana-com-2026-06-20T182343.png
security:
- kind: authentication
  name: Grafana Com Authentication
  slug: grafana-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Grafana Com Domain Security
  slug: grafana-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Grafana Com Vulnerability Disclosure
  slug: grafana-com-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Grafana Com Trust Center
  slug: grafana-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: grafana-com
tags:
- Observability
- Monitoring
- Dashboards
- Logs
- Metrics
- Traces
- Profiling
- Alerting
- Open Source
- Grafana Labs
website: https://www.grafana.com/
---
