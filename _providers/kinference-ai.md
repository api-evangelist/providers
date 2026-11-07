---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The kinference.v1 Picker gRPC service used by the Kinference router - given an inference request it picks a model and destination (a local inference engine pod or an off-cluster provider), with stream
  name: Kinference Picker gRPC API
  slug: kinference-picker-grpc-api
- description: Kubernetes custom resources in the kinference.buoyant.io/v1alpha1 group (InferencePolicy, InferencePool, InferenceProvider, InferenceWorkerSet, plus GatewayBackend) used to declaratively configure the
  name: Kinference Kubernetes CRD API
  slug: kinference-kubernetes-crd-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/kinference-ai/plans/kinference-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kinference-ai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/kinference-ai/cli/kinference-ai-cli.yml
  title: ''
  type: CLI
  url: cli/kinference-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/kinference-ai/changelog/kinference-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kinference-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/kinference-ai/conventions/kinference-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kinference-ai-conventions.yml
- group: start
  href: https://artifacts.apis.io/kinference-ai/sandbox/kinference-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kinference-ai-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/kinference-ai/authentication/kinference-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kinference-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/kinference-ai/lifecycle/kinference-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kinference-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kinference-ai/errors/kinference-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/kinference-ai-error-codes.yml
- group: design
  href: https://artifacts.apis.io/kinference-ai/conformance/kinference-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kinference-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/kinference-ai/hosts/kinference-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kinference-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/kinference-ai/integrations/kinference-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/kinference-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/kinference-ai/vendors/kinference-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kinference-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/kinference-ai/packages/kinference-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/kinference-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/kinference-ai/packages/kinference-ai-packages.yml
  title: ''
  type: Packages
  url: packages/kinference-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/kinference-ai/security/kinference-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinference-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kinference.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://kinference.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://kinference.ai/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://kinference.ai/docs/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kinference-AI
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Kinference-AI/kinference
- group: company
  title: ''
  type: Blog
  url: https://buoyant.io/tag/inference
- group: other
  title: ''
  type: Enterprise
  url: https://www.buoyant.io/products/kinference-enterprise-buoyant-ai
created: '2026-11-05'
description: Kinference (pronounced "kay-inference") is an open-source inference control plane for Kubernetes and vLLM, built by Buoyant, Inc. (the company behind Linkerd). It turns any GPU-enabled Kubernetes cluster into a distributed inference platform with a traffic gateway that accepts OpenAI and Anthropic inference APIs, per-tenant token rate limits, policy-driven model routing, KV cache-aware load balancing, semantic classification, model aliases, and Prometheus/Grafana metrics, configured declaratively through Kubernetes CRDs and the kinfctl CLI. A commercial Kinference Enterprise edition is offered by Buoyant.
image: https://kinference.ai/images/kinference-opengraph.png
json_schemas:
- name: InferencePolicy (kinference.buoyant.io/v1alpha1)
  property_count: 5
  slug: kinference-ai-inferencepolicy
- name: InferencePool (kinference.buoyant.io/v1alpha1)
  property_count: 5
  slug: kinference-ai-inferencepool
- name: InferenceProvider (kinference.buoyant.io/v1alpha1)
  property_count: 5
  slug: kinference-ai-inferenceprovider
- name: InferenceWorkerSet (kinference.buoyant.io/v1alpha1)
  property_count: 5
  slug: kinference-ai-inferenceworkerset
layout: provider
modified: '2026-11-05'
name: Kinference
nav: Providers
network: true
overview: 'Kinference is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Inference, Kubernetes, vLLM, and LLM Gateway.


  Kinference''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 16 more developer resources.'
plans:
- name: Kinference Ai Plans Pricing
  plan_count: 1
  slug: kinference-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Kinference Ai Rate Limits
  slug: kinference-ai-rate-limits
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 8.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 12.0
    developer_ergonomics: 64.3
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kinference Ai Authentication
  slug: kinference-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kinference Ai Domain Security
  slug: kinference-ai-domain-security
  summary_line: TLSv1.3
slug: kinference-ai
tags:
- Company
- Inference
- Kubernetes
- vLLM
- LLM Gateway
- Rate Limiting
- Load Balancing
- Open Source
- Platform Engineering
website: https://kinference.ai/
---
