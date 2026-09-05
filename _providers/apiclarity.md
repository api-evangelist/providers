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
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 3
  name: Apiclarity Agentic Access
  operation_count: 27
  slug: apiclarity-agentic-access
  summary_line: 27 operations · 8 acting · 3 human-in-the-loop
api_count: 5
apis:
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: Captured API traffic events.
  name: APIClarity API Events API
  slug: apiclarity-api-events-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: Discovered APIs and their reconstructed specifications.
  name: APIClarity API Inventory API
  slug: apiclarity-api-inventory-api
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
- baseURL: https://apiclarity-server/api/modules/bfla
  baseurl_source: declared
  description: 'Broken Function Level Authorization detection. Learns an authorization model from observed API interactions — which callers are supposed to invoke which operations — then flags violations against it. '
  name: APIClarity BFLA Module API
  slug: apiclarity-bfla-module-api
- baseURL: https://apiclarity-server/api/modules/fuzzer
  baseurl_source: declared
  description: Active security testing. Drives generated traffic at an API based on its specification to find implementation flaws, then returns a severity-ranked report and a specification annotated with the findin
  name: APIClarity Fuzzer Module API
  slug: apiclarity-fuzzer-module-api
- baseURL: https://apiclarity-server/api/modules/traceanalyzer
  baseurl_source: declared
  description: Analyzes the path, headers and body of observed requests and responses for weak authentication, exposure of sensitive information and potential broken object level authorization. Served under /api/mod
  name: APIClarity Trace Analyzer Module API
  slug: apiclarity-trace-analyzer-module-api
- baseURL: https://apiclarity-server/api/modules/spec_differ
  baseurl_source: declared
  description: Compares observed API traces against the provided or reconstructed specification to surface shadow APIs (observed but undocumented), zombie APIs (observed but marked deprecated) and drift. Served unde
  name: APIClarity Spec Differ Module API
  slug: apiclarity-spec-differ-module-api
- baseURL: https://apiclarity-server/api/modules/specreconstructor
  baseurl_source: declared
  description: Controls reconstruction of an OpenAPI specification from live traffic for a discovered API. Served under /api/modules/specreconstructor.
  name: APIClarity Spec Reconstructor Module API
  slug: apiclarity-spec-reconstructor-module-api
- baseURL: https://apiclarity-server/api
  baseurl_source: declared
  description: The Swagger 2.0 contract every APIClarity traffic-source plugin implements to push captured traffic into a deployment — POST /telemetry, GET /hostsToTrace and POST /control/newDiscoveredAPIs. Authenti
  name: APIClarity Plugins Telemetry API
  slug: apiclarity-plugins-telemetry-api
- baseURL: /
  baseurl_source: spec
  description: 'An inverted contract — the endpoint a registered listener must implement, which APIClarity POSTs to. Six notification types share one polymorphic envelope discriminated on notificationType: NewDiscove'
  name: APIClarity Notifications API
  slug: apiclarity-notifications-api
artifact_total: 36
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apiclarity-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/apiclarity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apiclarity-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apiclarity-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apiclarity-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apiclarity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apiclarity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apiclarity-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apiclarity-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apiclarity-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apiclarity-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apiclarity-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apiclarity-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apiclarity-plans-pricing.yml
- group: operate
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
  title: ''
  type: DomainSecurity
  url: security/apiclarity-domain-security.yml
- group: auth
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
overview: 'APIClarity publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Events API, API Inventory API, Control API, and 8 more. Tagged areas include API Observability, API Security, API Traffic Analysis, Cisco, and Kubernetes.


  The APIClarity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  APIClarity''s developer surface includes changelog, sandbox, getting-started guide, API reference, support, authentication, documentation, and 22 more developer resources.'
plans:
- name: Apiclarity Plans Pricing
  plan_count: 0
  slug: apiclarity-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Apiclarity Rate Limits
  slug: apiclarity-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.4
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 61.3
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
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
