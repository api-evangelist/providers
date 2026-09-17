---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 89
  human_in_the_loop: 10
  name: Goharbor Agentic Access
  operation_count: 206
  slug: goharbor-agentic-access
  summary_line: 206 operations · 89 acting · 10 human-in-the-loop
api_count: 2
apis:
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The health API from GoHarbor — 2 operation(s) for health.
  name: GoHarbor health API
  slug: goharbor-health-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The replication API from GoHarbor — 2 operation(s) for replication.
  name: GoHarbor replication API
  slug: goharbor-replication-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The scan API from GoHarbor — 1 operation(s) for scan.
  name: GoHarbor scan API
  slug: goharbor-scan-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The search API from GoHarbor — 1 operation(s) for search.
  name: GoHarbor search API
  slug: goharbor-search-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The artifact API from GoHarbor — 9 operation(s) for artifact.
  name: GoHarbor Artifact API
  slug: goharbor-artifact-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The configure API from GoHarbor — 2 operation(s) for configure.
  name: GoHarbor Configure API
  slug: goharbor-configure-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The gc API from GoHarbor — 4 operation(s) for gc.
  name: GoHarbor Gc API
  slug: goharbor-gc-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The icon API from GoHarbor — 1 operation(s) for icon.
  name: GoHarbor Icon API
  slug: goharbor-icon-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The immutable API from GoHarbor — 2 operation(s) for immutable.
  name: GoHarbor Immutable API
  slug: goharbor-immutable-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The label API from GoHarbor — 2 operation(s) for label.
  name: GoHarbor Label API
  slug: goharbor-label-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The Ldap API from GoHarbor — 4 operation(s) for ldap.
  name: GoHarbor Ldap API
  slug: goharbor-ldap-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The member API from GoHarbor — 2 operation(s) for member.
  name: GoHarbor Member API
  slug: goharbor-member-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The oidc API from GoHarbor — 1 operation(s) for oidc.
  name: GoHarbor Oidc API
  slug: goharbor-oidc-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The permissions API from GoHarbor — 1 operation(s) for permissions.
  name: GoHarbor Permissions API
  slug: goharbor-permissions-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The ping API from GoHarbor — 1 operation(s) for ping.
  name: GoHarbor Ping API
  slug: goharbor-ping-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The preheat API from GoHarbor — 11 operation(s) for preheat.
  name: GoHarbor Preheat API
  slug: goharbor-preheat-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The project API from GoHarbor — 9 operation(s) for project.
  name: GoHarbor Project API
  slug: goharbor-project-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The projectMetadata API from GoHarbor — 2 operation(s) for projectmetadata.
  name: GoHarbor Project Metadata API
  slug: goharbor-projectmetadata-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The purge API from GoHarbor — 4 operation(s) for purge.
  name: GoHarbor Purge API
  slug: goharbor-purge-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The quota API from GoHarbor — 2 operation(s) for quota.
  name: GoHarbor Quota API
  slug: goharbor-quota-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The registry API from GoHarbor — 6 operation(s) for registry.
  name: GoHarbor Registry API
  slug: goharbor-registry-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The repository API from GoHarbor — 3 operation(s) for repository.
  name: GoHarbor Repository API
  slug: goharbor-repository-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The Retention API from GoHarbor — 7 operation(s) for retention.
  name: GoHarbor Retention API
  slug: goharbor-retention-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The robot API from GoHarbor — 2 operation(s) for robot.
  name: GoHarbor Robot API
  slug: goharbor-robot-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The scan data export API from GoHarbor — 4 operation(s) for scan data export.
  name: GoHarbor scan data export API
  slug: goharbor-scan-data-export-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The scanAll API from GoHarbor — 4 operation(s) for scanall.
  name: GoHarbor Scan All API
  slug: goharbor-scanall-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The scanner API from GoHarbor — 7 operation(s) for scanner.
  name: GoHarbor Scanner API
  slug: goharbor-scanner-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The schedule API from GoHarbor — 2 operation(s) for schedule.
  name: GoHarbor Schedule API
  slug: goharbor-schedule-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The securityhub API from GoHarbor — 2 operation(s) for securityhub.
  name: GoHarbor Securityhub API
  slug: goharbor-securityhub-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The statistic API from GoHarbor — 1 operation(s) for statistic.
  name: GoHarbor Statistic API
  slug: goharbor-statistic-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The SystemCVEAllowlist API from GoHarbor — 1 operation(s) for systemcveallowlist.
  name: GoHarbor System CVE Allowlist API
  slug: goharbor-systemcveallowlist-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The user API from GoHarbor — 8 operation(s) for user.
  name: GoHarbor User API
  slug: goharbor-user-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The webhook API from GoHarbor — 7 operation(s) for webhook.
  name: GoHarbor Webhook API
  slug: goharbor-webhook-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The webhookjob API from GoHarbor — 1 operation(s) for webhookjob.
  name: GoHarbor Webhookjob API
  slug: goharbor-webhookjob-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The Audit Log API from GoHarbor — 3 operation(s) for audit log.
  name: GoHarbor Audit Log API
  slug: goharbor-audit-log-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The Job Service API from GoHarbor — 6 operation(s) for job service.
  name: GoHarbor Job Service API
  slug: goharbor-job-service-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The System Info API from GoHarbor — 3 operation(s) for system info.
  name: GoHarbor System Info API
  slug: goharbor-system-info-api
- baseURL: https://{host}/api/v2.0
  baseurl_source: declared
  description: The User Group API from GoHarbor — 3 operation(s) for user group.
  name: GoHarbor User Group API
  slug: goharbor-user-group-api
artifact_total: 63
asyncapis:
- description: ''
  name: Goharbor Webhooks
  slug: goharbor-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harbor artifacts API
  slug: open-goharbor-artifacts-api
- collection_type: open
  name: Harbor artifacts audit API
  slug: open-goharbor-audit-api
- collection_type: open
  name: Harbor artifacts health API
  slug: open-goharbor-health-api
- collection_type: open
  name: Harbor artifacts projects API
  slug: open-goharbor-projects-api
- collection_type: open
  name: Harbor artifacts quotas API
  slug: open-goharbor-quotas-api
- collection_type: open
  name: Harbor artifacts registries API
  slug: open-goharbor-registries-api
- collection_type: open
  name: Harbor artifacts replication API
  slug: open-goharbor-replication-api
- collection_type: open
  name: Harbor artifacts repositories API
  slug: open-goharbor-repositories-api
- collection_type: open
  name: Harbor artifacts robots API
  slug: open-goharbor-robots-api
- collection_type: open
  name: Harbor artifacts scan API
  slug: open-goharbor-scan-api
- collection_type: open
  name: Harbor artifacts search API
  slug: open-goharbor-search-api
- collection_type: open
  name: Harbor artifacts tags API
  slug: open-goharbor-tags-api
- collection_type: open
  name: Harbor artifacts usergroups API
  slug: open-goharbor-usergroups-api
- collection_type: open
  name: Harbor artifacts webhooks API
  slug: open-goharbor-webhooks-api
- collection_type: open
  name: Harbor API
  slug: open-goharbor
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/goharbor/harbor/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/goharbor/harbor/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/goharbor/harbor/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/goharbor/harbor/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/goharbor/harbor/blob/main/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/agentic-access/goharbor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/goharbor-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/security/goharbor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goharbor-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/authentication/goharbor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/goharbor-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://goharbor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://goharbor.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goharbor
- group: company
  title: ''
  type: Blog
  url: https://goharbor.io/blog/index.xml
- group: docs
  title: ''
  type: APIReference
  url: https://goharbor.io/docs/2.15.0/working-with-projects/using-api-explorer/
- group: start
  title: ''
  type: GettingStarted
  url: https://goharbor.io/docs/2.15.0/install-config/
- group: operate
  title: ''
  type: Support
  url: https://goharbor.io/community/
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/goharbor/harbor/blob/main/ROADMAP.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goharbor.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/security/goharbor-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/goharbor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/security/goharbor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/goharbor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/conformance/goharbor-conformance.yml
  title: ''
  type: Compliance
  url: conformance/goharbor-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/conformance/goharbor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goharbor-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/lifecycle/goharbor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/goharbor-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/changelog/goharbor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/goharbor-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/conventions/goharbor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goharbor-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/errors/goharbor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/goharbor-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/data-model/goharbor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/goharbor-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/scopes/goharbor-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/goharbor-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/packages/goharbor-packages.yml
  title: ''
  type: Packages
  url: packages/goharbor-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/packages/goharbor-packages.yml
  title: ''
  type: SDKs
  url: packages/goharbor-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/cli/goharbor-cli.yml
  title: ''
  type: CLI
  url: cli/goharbor-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/sandbox/goharbor-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/goharbor-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/asyncapi/goharbor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/goharbor-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/llms/goharbor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goharbor-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/overlays/goharbor-harbor-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/goharbor-harbor-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/mcp/goharbor-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/goharbor-mcp.yml
created: '2025-02-17'
description: 'Harbor is an open source, CNCF-hosted registry that stores, signs and scans OCI artifacts, adding the policy and identity layer a plain container registry lacks: projects, RBAC and robot accounts, vulnerability scanning and SBOM generation, Cosign content trust, tag retention and immutability, quotas, replication between registries and P2P preheat. It is Apache-2.0 and self-hosted, so every API base URL is the operator''s own deployment rather than a vendor endpoint. Harbor publishes a 203-operation v2.0 REST API in its own repository, serves a live Swagger UI from every instance at /devcenter-api-2.0, speaks the OCI Distribution Specification on /v2/, emits ten project event types over webhooks in CloudEvents 1.0 format, and ships an official CLI, Go client, Helm chart and Terraform provider.'
finops:
- name: Goharbor Finops
  service_category: API
  slug: goharbor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goharbor.png
layout: provider
modified: '2026-09-12'
name: GoHarbor
nav: Providers
network: true
overview: 'GoHarbor publishes 38 APIs on the [APIs.io](https://apis.io/) network, including health API, replication API, scan API, and 35 more. Tagged areas include Container Registry, Containers, Artifacts, Vulnerability Scanning, and Supply Chain Security.


  The GoHarbor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoHarbor''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, changelog, and 31 more developer resources.'
plans:
- name: Goharbor Plans Pricing
  plan_count: 0
  slug: goharbor-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Goharbor Rate Limits
  slug: goharbor-rate-limits
scopes:
- name: Goharbor Scopes
  scope_count: 0
  slug: goharbor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 70.8
    discoverability: 70.4
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 85.0
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/screenshots/goharbor-2026-06-20T181946.png
security:
- kind: authentication
  name: Goharbor Authentication
  slug: goharbor-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Goharbor Domain Security
  slug: goharbor-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Goharbor Vulnerability Disclosure
  slug: goharbor-vulnerability-disclosure
  summary_line: disclosure policy published
slug: goharbor
tags:
- Container Registry
- Containers
- Artifacts
- Vulnerability Scanning
- Supply Chain Security
- OCI
- Open-Source
- Kubernetes
- DevOps
- Replication
website: https://goharbor.io/
---
