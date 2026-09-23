---
access_model:
  confidence: high
  label: Free and open source (Apache-2.0)
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-09-23'
api_count: 3
apis:
- description: Envoy Gateway's configuration API is a set of Kubernetes Custom Resource Definitions in the gateway.envoyproxy.io/v1alpha1 group — Backend, BackendTrafficPolicy, ClientTrafficPolicy, EnvoyExtensionPol
  name: Envoy Gateway
  slug: envoy-gateway
- description: 'A gRPC contract an operator implements to extend Envoy Gateway. Envoy Gateway is the client: during xDS translation it calls the six EnvoyGatewayExtension RPCs — PostRouteModify, PostVirtualHostModify'
  name: Envoy Gateway Extension Server
  slug: envoy-gateway-extension-server
- description: A gRPC contract added in v1.9.0 that lets an operator supply their own infrastructure management strategy in place of Envoy Gateway creating Kubernetes workloads itself. Four RPCs on EnvoyGatewayRemot
  name: Envoy Gateway Remote Infrastructure Provider
  slug: envoy-gateway-remote-infrastructure
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://gateway.envoyproxy.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gateway.envoyproxy.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://gateway.envoyproxy.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://gateway.envoyproxy.io/docs/api/extension_types/
- group: start
  title: ''
  type: GettingStarted
  url: https://gateway.envoyproxy.io/docs/tasks/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://github.com/envoyproxy/gateway/issues
- group: operate
  title: ''
  type: Roadmap
  url: https://gateway.envoyproxy.io/community/roadmap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envoyproxy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/envoyproxy/gateway
- group: commercial
  title: ''
  type: License
  url: https://github.com/envoyproxy/gateway/blob/main/LICENSE
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/envoyproxy/gateway/releases
- group: operate
  title: ''
  type: Slack
  url: https://www.envoyproxy.io/slack
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/llms/envoy-gateway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/envoy-gateway-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/json-schema/envoy-gateway-json-schema.yml
  title: ''
  type: JSONSchema
  url: json-schema/envoy-gateway-json-schema.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/grpc/envoy-gateway-grpc.yml
  title: ''
  type: Protobuf
  url: grpc/envoy-gateway-grpc.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/conformance/envoy-gateway-conformance.yml
  title: ''
  type: Conformance
  url: conformance/envoy-gateway-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/packages/envoy-gateway-packages.yml
  title: ''
  type: Packages
  url: packages/envoy-gateway-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/packages/envoy-gateway-packages.yml
  title: ''
  type: SDKs
  url: packages/envoy-gateway-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/cli/envoy-gateway-cli.yml
  title: ''
  type: CLI
  url: cli/envoy-gateway-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/conventions/envoy-gateway-conventions.yml
  title: ''
  type: Conventions
  url: conventions/envoy-gateway-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/conventions/envoy-gateway-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/envoy-gateway-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/data-model/envoy-gateway-data-model.yml
  title: ''
  type: DataModel
  url: data-model/envoy-gateway-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/authentication/envoy-gateway-authentication.yml
  title: ''
  type: Authentication
  url: authentication/envoy-gateway-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/lifecycle/envoy-gateway-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/envoy-gateway-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/lifecycle/envoy-gateway-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/envoy-gateway-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/changelog/envoy-gateway-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/envoy-gateway-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/security/envoy-gateway-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/envoy-gateway-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/security/envoy-gateway-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/envoy-gateway-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/security/envoy-gateway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/envoy-gateway-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/plans/envoy-gateway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/envoy-gateway-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/rate-limits/envoy-gateway-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/envoy-gateway-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/finops/envoy-gateway-finops.yml
  title: ''
  type: FinOps
  url: finops/envoy-gateway-finops.yml
created: '2026-03-27'
description: 'Envoy Gateway is a CNCF project that manages Envoy Proxy as a standalone or Kubernetes-based application gateway. It implements the Kubernetes Gateway API and extends it with its own API group, gateway.envoyproxy.io, whose eight Custom Resource Definitions cover infrastructure shape, client and backend traffic behaviour, security policy, extensibility and direct xDS patching. There is no REST API and no hosted endpoint: the machine-readable contract is the CRD structural schemas plus two first-party gRPC services — an extension server hook and a remote infrastructure provider — that Envoy Gateway calls out to. Apache-2.0 licensed and free, with a published compatibility matrix giving every release a dated end of life, and Gateway API v1.6.1 core and extended conformance certified by report in the standard body''s own repository.'
finops:
- name: Envoy Gateway Finops
  service_category: API
  slug: envoy-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envoy-gateway.png
layout: provider
modified: '2026-09-07'
name: Envoy Gateway
nav: Providers
network: true
overview: 'Envoy Gateway publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, CNCF, Envoy, Kubernetes, and Open-Source.


  Envoy Gateway''s developer surface includes documentation, API reference, getting-started guide, support, release notes, CLI, authentication, and 26 more developer resources.'
plans:
- name: Envoy Gateway Plans Pricing
  plan_count: 0
  slug: envoy-gateway-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Envoy Gateway Rate Limits
  slug: envoy-gateway-rate-limits
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 40.0
    developer_ergonomics: 76.2
    discoverability: 81.5
    operational_transparency: 42.1
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/screenshots/envoy-gateway-2026-06-20T180742.png
security:
- kind: authentication
  name: Envoy Gateway Authentication
  slug: envoy-gateway-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Envoy Gateway Domain Security
  slug: envoy-gateway-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Envoy Gateway Vulnerability Disclosure
  slug: envoy-gateway-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: envoy-gateway
tags:
- API Gateway
- CNCF
- Envoy
- Kubernetes
- Open-Source
- Gateway API
- Ingress
- Service Mesh
- Cloud-Native
- gRPC
website: https://gateway.envoyproxy.io/
---
