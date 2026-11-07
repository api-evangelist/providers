---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 5
  name: Smol Machines Agentic Access
  operation_count: 83
  slug: smol-machines-agentic-access
  summary_line: 83 operations · 49 acting · 5 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Long-running app deployments
  name: Smol Machines Apps API
  slug: smol-machines-apps-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Self-service account and metering
  name: Smol Machines Billing API
  slug: smol-machines-billing-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Container management within sandboxes
  name: Smol Machines Containers API
  slug: smol-machines-containers-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Command execution in sandboxes
  name: Smol Machines Execution API
  slug: smol-machines-execution-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Health, probes, and metrics
  name: Smol Machines Health API
  slug: smol-machines-health-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: OCI image management
  name: Smol Machines Images API
  slug: smol-machines-images-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Log streaming
  name: Smol Machines Logs API
  slug: smol-machines-logs-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: First-class machine lifecycle and exec
  name: Smol Machines API
  slug: smol-machines-machines-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Persistent microVM management
  name: Smol Machines MicroVMs API
  slug: smol-machines-microvms-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Cluster node enrollment and status
  name: Smol Machines Nodes API
  slug: smol-machines-nodes-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Async operations
  name: Smol Machines Operations API
  slug: smol-machines-operations-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Quota + rate + budget plans
  name: Smol Machines Plans API
  slug: smol-machines-plans-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Warm machine pools
  name: Smol Machines Pools API
  slug: smol-machines-pools-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Sandbox lifecycle management
  name: Smol Machines Sandboxes API
  slug: smol-machines-sandboxes-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Customer accounts (product-backend)
  name: Smol Machines Tenants API
  slug: smol-machines-tenants-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Node join tokens
  name: Smol Machines Tokens API
  slug: smol-machines-tokens-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Usage and billing
  name: Smol Machines Usage API
  slug: smol-machines-usage-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: Persistent volumes
  name: Smol Machines Volumes API
  slug: smol-machines-volumes-api
- baseURL: https://api.smolmachines.com
  baseurl_source: declared
  description: API key management
  name: Smol Machines API Keys API
  slug: smol-machines-api-keys-api
artifact_total: 48
collections:
- collection_type: open
  name: smolfleet apikeys API
  slug: open-smol-machines-apikeys-api
- collection_type: open
  name: smolfleet apikeys apps API
  slug: open-smol-machines-apps-api
- collection_type: open
  name: smolfleet apikeys billing API
  slug: open-smol-machines-billing-api
- collection_type: open
  name: smolfleet apikeys Containers API
  slug: open-smol-machines-containers-api
- collection_type: open
  name: smolfleet apikeys Execution API
  slug: open-smol-machines-execution-api
- collection_type: open
  name: smolfleet apikeys health API
  slug: open-smol-machines-health-api
- collection_type: open
  name: smolfleet apikeys Images API
  slug: open-smol-machines-images-api
- collection_type: open
  name: smolfleet apikeys Logs API
  slug: open-smol-machines-logs-api
- collection_type: open
  name: smolfleet apikeys machines API
  slug: open-smol-machines-machines-api
- collection_type: open
  name: smolfleet apikeys MicroVMs API
  slug: open-smol-machines-microvms-api
- collection_type: open
  name: smolfleet apikeys nodes API
  slug: open-smol-machines-nodes-api
- collection_type: open
  name: smolfleet apikeys operations API
  slug: open-smol-machines-operations-api
- collection_type: open
  name: smolfleet apikeys plans API
  slug: open-smol-machines-plans-api
- collection_type: open
  name: smolfleet apikeys pools API
  slug: open-smol-machines-pools-api
- collection_type: open
  name: smolfleet apikeys Sandboxes API
  slug: open-smol-machines-sandboxes-api
- collection_type: open
  name: smolfleet apikeys tenants API
  slug: open-smol-machines-tenants-api
- collection_type: open
  name: smolfleet apikeys tokens API
  slug: open-smol-machines-tokens-api
- collection_type: open
  name: smolfleet apikeys usage API
  slug: open-smol-machines-usage-api
- collection_type: open
  name: smolfleet apikeys volumes API
  slug: open-smol-machines-volumes-api
common:
- group: commercial
  href: https://artifacts.apis.io/smol-machines/plans/smol-machines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smol-machines-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/smol-machines/capabilities/smol-machines-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smol-machines-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.smolmachines.com/
- group: other
  href: https://artifacts.apis.io/smol-machines/overlays/smol-machines-smolfleet-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/smol-machines-smolfleet-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/smol-machines/authentication/smol-machines-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smol-machines-authentication.yml
- group: auth
  href: https://artifacts.apis.io/smol-machines/security/smol-machines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smol-machines-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/smol-machines/agentic-access/smol-machines-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smol-machines-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://smolmachines.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://smolmachines.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://smolmachines.com/docs/cloud-api
- group: start
  title: ''
  type: GettingStarted
  url: https://smolmachines.com/docs/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://smolmachines.com/docs/cloud-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://smolmachines.com/console
- group: commercial
  title: ''
  type: Pricing
  url: https://smolmachines.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smolmachines.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smolmachines.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://smolmachines.com/engineering
- group: operate
  title: ''
  type: StatusPage
  url: https://smolmachines.com/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smol-machines
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/E5r8rEWY9J
- group: start
  title: ''
  type: Registry
  url: https://smolmachines.com/registry
- group: docs
  href: https://artifacts.apis.io/smol-machines/openapi/_original/smol-machines-smolfleet-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/smol-machines-smolfleet-openapi.json
- group: docs
  href: https://artifacts.apis.io/smol-machines/openapi/_original/smol-machines-smolvm-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/smol-machines-smolvm-openapi.json
- group: agent
  href: https://artifacts.apis.io/smol-machines/llms/smol-machines-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smol-machines-llms.txt
- group: build
  href: https://artifacts.apis.io/smol-machines/packages/smol-machines-packages.yml
  title: ''
  type: Packages
  url: packages/smol-machines-packages.yml
- group: build
  href: https://artifacts.apis.io/smol-machines/packages/smol-machines-packages.yml
  title: ''
  type: SDKs
  url: packages/smol-machines-packages.yml
- group: build
  href: https://artifacts.apis.io/smol-machines/cli/smol-machines-cli.yml
  title: ''
  type: CLI
  url: cli/smol-machines-cli.yml
- group: agent
  href: https://artifacts.apis.io/smol-machines/mcp/smol-machines-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/smol-machines-mcp.yml
- group: agent
  href: https://artifacts.apis.io/smol-machines/well-known/smol-machines-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smol-machines-well-known.yml
- group: design
  href: https://artifacts.apis.io/smol-machines/conformance/smol-machines-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smol-machines-conformance.yml
- group: design
  href: https://artifacts.apis.io/smol-machines/errors/smol-machines-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/smol-machines-problem-types.yml
- group: design
  href: https://artifacts.apis.io/smol-machines/lifecycle/smol-machines-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/smol-machines-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/smol-machines/conventions/smol-machines-conventions.yml
  title: ''
  type: Conventions
  url: conventions/smol-machines-conventions.yml
- group: operate
  href: https://artifacts.apis.io/smol-machines/changelog/smol-machines-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/smol-machines-changelog.yml
- group: design
  href: https://artifacts.apis.io/smol-machines/data-model/smol-machines-data-model.yml
  title: ''
  type: DataModel
  url: data-model/smol-machines-data-model.yml
- group: agent
  href: https://artifacts.apis.io/smol-machines/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Smol Machines (smol machines, inc.) is a Y Combinator-backed developer infrastructure company building portable, self-contained Linux microVMs. Its open-source `smolvm` engine and `smol` CLI (both Rust, Apache-2.0) boot hardware-isolated virtual machines from any OCI image in under 200ms — on a laptop, in the smolfleet cloud, or self-hosted — with no daemon and no Docker. The same Machine API runs locally as an in-process microVM or against the hosted smolfleet control plane at api.smolmachines.com, so teams sandbox untrusted code and AI-agent workloads, ship stateful `.smolmachine` artifacts, and deploy machines across a cluster without changing a line. Node and Python SDKs (`smolmachines`), a local REST API, and a cloud REST API are all public.
finops:
- has_sources: true
  method: derived
  name: Smol Machines Finops
  primary_unit: monthly fee
  service_category: ''
  slug: smol-machines-finops
  template: false
image: https://smolmachines.com/install.sh
layout: provider
modified: '2026-09-16'
name: Smol Machines
nav: Providers
network: true
overview: 'Smol Machines publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Billing API, Containers API, and 16 more. Tagged areas include Company, MicroVM, Sandbox, Virtualization, and Developer Tools.


  The Smol Machines catalog on APIs.io includes 1 Spectral governance ruleset.


  Smol Machines'' developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, signup flow, pricing, and 29 more developer resources.'
plans:
- name: Smol Machines Plans Pricing
  plan_count: 9
  slug: smol-machines-plans-pricing
- name: Smol Machines Price Estimates
  plan_count: 0
  slug: smol-machines-price-estimates
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Smol Machines API Rules
  rule_count: 53
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 11
  slug: smol-machines-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 41.8
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 68.4
      derived: 0
      marker_coverage: 68.4
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smol-machines/smol-machines-2026-08-17T081934.png
security:
- kind: authentication
  name: Smol Machines Authentication
  slug: smol-machines-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Smol Machines Domain Security
  slug: smol-machines-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Deploy and scale an app on smolfleet
  slug: smol-machines-deploy-and-scale-app
- name: Sandbox and run code on the local smolvm API
  slug: smol-machines-local-sandbox-exec
- name: Run untrusted code in a cloud microVM
  slug: smol-machines-run-untrusted-code-cloud
slug: smol-machines
tags:
- Company
- MicroVM
- Sandbox
- Virtualization
- Developer Tools
- Infrastructure
- AI Agents
- Code Execution
- Containers
- Cloud
website: https://www.smolmachines.com/
---
