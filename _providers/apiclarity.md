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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 46
  human_in_the_loop: 19
  name: Apiclarity Agentic Access
  operation_count: 100
  slug: apiclarity-agentic-access
  summary_line: 100 operations · 46 acting · 19 human-in-the-loop
api_count: 12
apis:
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: Control-plane endpoints for trace sources and discovered APIs.
  name: APIClarity Control API
  slug: apiclarity-control-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: Enabled features in the deployment.
  name: APIClarity Features API
  slug: apiclarity-features-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The ApiEvents API from APIClarity — 4 operation(s) for apievents.
  name: APIClarity API Events API
  slug: apiclarity-apievents-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The ApiFindings API from APIClarity — 2 operation(s) for apifindings.
  name: APIClarity API Findings API
  slug: apiclarity-apifindings-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The ApiInventory API from APIClarity — 11 operation(s) for apiinventory.
  name: APIClarity API Inventory API
  slug: apiclarity-apiinventory-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The bfla API from APIClarity — 16 operation(s) for bfla.
  name: APIClarity Bfla API
  slug: apiclarity-bfla-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Dashboard API from APIClarity — 3 operation(s) for dashboard.
  name: APIClarity Dashboard API
  slug: apiclarity-dashboard-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Enable API from APIClarity — 1 operation(s) for enable.
  name: APIClarity Enable API
  slug: apiclarity-enable-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The EventAnnotations API from APIClarity — 1 operation(s) for eventannotations.
  name: APIClarity Event Annotations API
  slug: apiclarity-eventannotations-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The fuzzer API from APIClarity — 8 operation(s) for fuzzer.
  name: APIClarity Fuzzer API
  slug: apiclarity-fuzzer-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The HostsToTrace API from APIClarity — 1 operation(s) for hoststotrace.
  name: APIClarity Hosts To Trace API
  slug: apiclarity-hoststotrace-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The local-bfla API from APIClarity — 10 operation(s) for local-bfla.
  name: APIClarity Local Bfla API
  slug: apiclarity-local-bfla-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The local-fuzzer API from APIClarity — 10 operation(s) for local-fuzzer.
  name: APIClarity Local Fuzzer API
  slug: apiclarity-local-fuzzer-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Modules API from APIClarity — 14 operation(s) for modules.
  name: APIClarity Modules API
  slug: apiclarity-modules-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Notification API from APIClarity — 1 operation(s) for notification.
  name: APIClarity Notification API
  slug: apiclarity-notification-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Start API from APIClarity — 1 operation(s) for start.
  name: APIClarity Start API
  slug: apiclarity-start-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The State API from APIClarity — 1 operation(s) for state.
  name: APIClarity State API
  slug: apiclarity-state-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Stop API from APIClarity — 1 operation(s) for stop.
  name: APIClarity Stop API
  slug: apiclarity-stop-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Telemetry API from APIClarity — 1 operation(s) for telemetry.
  name: APIClarity Telemetry API
  slug: apiclarity-telemetry-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Version API from APIClarity — 1 operation(s) for version.
  name: APIClarity Version API
  slug: apiclarity-version-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The API Usage API from APIClarity — 1 operation(s) for api usage.
  name: APIClarity API Usage API
  slug: apiclarity-api-usage-api
artifact_total: 46
asyncapis:
- description: ''
  name: Apiclarity Notifications Webhooks
  slug: apiclarity-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIClarity API Events API
  slug: open-apiclarity-api-events-api
- collection_type: open
  name: APIClarity API Events API Inventory API
  slug: open-apiclarity-api-inventory-api
- collection_type: open
  name: APIClarity API Events Control API
  slug: open-apiclarity-control-api
- collection_type: open
  name: APIClarity API Events Features API
  slug: open-apiclarity-features-api
- collection_type: open
  name: APIClarity API
  slug: open-apiclarity
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-api-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-api-events-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-api-inventory-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-api-inventory-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-bfla-module-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-bfla-module-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-fuzzer-module-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-fuzzer-module-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/skills/apiclarity-run-a-fuzz-test.md
  title: ''
  type: AgentSkill
  url: skills/apiclarity-run-a-fuzz-test.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-trace-analyzer-module-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-trace-analyzer-module-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-spec-differ-module-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-spec-differ-module-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/skills/apiclarity-hunt-shadow-and-zombie-apis.md
  title: ''
  type: AgentSkill
  url: skills/apiclarity-hunt-shadow-and-zombie-apis.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-spec-reconstructor-module-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-spec-reconstructor-module-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/skills/apiclarity-reconstruct-and-approve-a-spec.md
  title: ''
  type: AgentSkill
  url: skills/apiclarity-reconstruct-and-approve-a-spec.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-plugins-telemetry-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-plugins-telemetry-swagger-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/overlays/apiclarity-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiclarity-notifications-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/agentic-access/apiclarity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apiclarity-agentic-access.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/packages/apiclarity-packages.yml
  title: ''
  type: Packages
  url: packages/apiclarity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/packages/apiclarity-packages.yml
  title: ''
  type: SDKs
  url: packages/apiclarity-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/conventions/apiclarity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apiclarity-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/conformance/apiclarity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiclarity-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/errors/apiclarity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiclarity-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/lifecycle/apiclarity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apiclarity-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/changelog/apiclarity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apiclarity-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/sandbox/apiclarity-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apiclarity-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/data-model/apiclarity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiclarity-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/asyncapi/apiclarity-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apiclarity-notifications-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/llms/apiclarity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiclarity-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/mcp/apiclarity-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apiclarity-mcp.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/plans/apiclarity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apiclarity-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/rate-limits/apiclarity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apiclarity-rate-limits.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/openclarity/apiclarity#getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/openclarity/apiclarity/tree/master/api3
- group: operate
  title: ''
  type: Support
  url: https://github.com/openclarity/apiclarity/issues
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/security/apiclarity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiclarity-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/authentication/apiclarity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiclarity-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/openclarity/apiclarity
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openclarity
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openclarity/apiclarity
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/openclarity/apiclarity#readme
- group: operate
  title: ''
  type: Issues
  url: https://github.com/openclarity/apiclarity/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/openclarity/apiclarity/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/openclarity/apiclarity/blob/master/LICENSE
- group: operate
  title: ''
  type: Slack
  url: https://outshift.slack.com
created: '2026-03-26'
description: 'APIClarity is an open source (Apache-2.0) API security and observability tool that captures API traffic in a Kubernetes environment, reconstructs OpenAPI specifications from what it observes, and detects shadow APIs, zombie APIs, specification drift and broken function-level authorization. It integrates with Istio, Kong, Tyk, Kuma, a tap DaemonSet and an OpenTelemetry Collector as traffic sources, and ships as a Helm chart you deploy into your own cluster — there is no hosted service, no vendor account and no vendor API host. It was part of the OpenClarity project. APIClarity has reached end of life: the source repository was archived read-only by its owner on 2026-05-29, the last release was v0.14.5 on 2023-05-05, and both project websites (openclarity.io and apiclarity.io) now return HTTP 404. The source, the eleven published specifications, the Helm chart repository and the container images all remain publicly readable, which is what this profile is built from.'
features:
- description: Automatically reconstruct OpenAPI specifications from observed live API traffic without code instrumentation.
  name: OpenAPI Spec Reconstruction
- description: Identify undocumented shadow APIs being called in production that are not reflected in official specifications.
  name: Shadow API Detection
- description: Detect deprecated or decommissioned API endpoints still receiving traffic in production.
  name: Zombie API Detection
- description: Compare observed API behavior against documented specifications to identify drifts, changes, and violations.
  name: API Diff Analysis
- description: Generate security findings and alerts based on API traffic analysis and specification violations.
  name: API Security Alerts
- description: Deploy as a sidecar or via Helm charts for integration with Kubernetes service meshes and API gateways.
  name: Kubernetes Integration
- description: Automatically build and maintain an inventory of all APIs discovered in the environment.
  name: API Inventory
finops:
- name: Apiclarity Finops
  service_category: API
  slug: apiclarity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiclarity.png
layout: provider
modified: '2026-09-04'
name: APIClarity
nav: Providers
network: true
overview: 'APIClarity publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Control API, Features API, API Events API, and 18 more. Tagged areas include API Observability, API Security, API Traffic Analysis, Cisco, and Kubernetes.


  The APIClarity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  APIClarity''s developer surface includes changelog, sandbox, getting-started guide, API reference, support, authentication, documentation, and 34 more developer resources.'
plans:
- name: Apiclarity Plans Pricing
  plan_count: 0
  slug: apiclarity-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Apiclarity Rate Limits
  slug: apiclarity-rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 50.1
    developer_ergonomics: 61.3
    discoverability: 74.1
    operational_transparency: 26.3
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/screenshots/apiclarity-2026-06-20T172238.png
security:
- kind: authentication
  name: Apiclarity Authentication
  slug: apiclarity-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apiclarity Domain Security
  slug: apiclarity-domain-security
  summary_line: no transport/DNS hardening detected
slug: apiclarity
tags:
- API Observability
- API Security
- API Traffic Analysis
- Cisco
- Kubernetes
- Open-Source
- OpenAPI Reconstruction
- OpenClarity
- Service Mesh
- Shadow APIs
use_cases:
- description: Discover all APIs running in a Kubernetes environment including undocumented and shadow APIs.
  name: API Discovery
- description: Assess API security by detecting shadow APIs, spec violations, and suspicious traffic patterns.
  name: API Security Posture Assessment
- description: Generate OpenAPI specifications from live traffic for APIs that lack formal documentation.
  name: API Specification Generation
- description: Enforce API consistency by detecting deviations between actual API behavior and official specifications.
  name: API Governance
- description: Investigate API security incidents using traffic analysis, API inventory, and spec diff data.
  name: Incident Response
---
