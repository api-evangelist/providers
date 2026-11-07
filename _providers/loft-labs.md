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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
api_count: 5
apis:
- baseURL: https://github.com
  baseurl_source: declared
  description: The Healthz API from Loft Labs — 1 operation(s) for healthz.
  name: Loft Labs Healthz API
  slug: loft-labs-healthz-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Kubernetes API from Loft Labs — 9 operation(s) for kubernetes.
  name: Loft Labs Kubernetes API
  slug: loft-labs-kubernetes-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Loft Labs API API from Loft Labs — 1 operation(s) for loft labs api.
  name: Loft Labs Loft Labs API
  slug: loft-labs-loft-labs-api-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Loft Sh API from Loft Labs — 2 operation(s) for loft sh.
  name: Loft Labs Loft Sh API
  slug: loft-labs-loft-sh-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Node API from Loft Labs — 1 operation(s) for node.
  name: Loft Labs Node API
  slug: loft-labs-node-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/loft-labs/plans/loft-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loft-labs-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/loft-labs/rules/loft-labs-rules.yml
  title: ''
  type: Spectral
  url: rules/loft-labs-rules.yml
- group: build
  href: https://artifacts.apis.io/loft-labs/cli/loft-labs-cli.yml
  title: ''
  type: CLI
  url: cli/loft-labs-cli.yml
- group: auth
  href: https://artifacts.apis.io/loft-labs/authentication/loft-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loft-labs-authentication.yml
- group: design
  href: https://artifacts.apis.io/loft-labs/conformance/loft-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loft-labs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/loft-labs/llms/loft-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loft-labs-llms.txt
- group: agent
  href: https://artifacts.apis.io/loft-labs/well-known/loft-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loft-labs-well-known.yml
- group: other
  href: https://artifacts.apis.io/loft-labs/hosts/loft-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loft-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/loft-labs/vendors/loft-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loft-labs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vcluster.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://www.vcluster.com/tags/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vcluster.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loft-sh
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vcluster.com/releases
- group: auth
  href: https://artifacts.apis.io/loft-labs/security/loft-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loft-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loft.sh
- group: docs
  title: ''
  type: Documentation
  url: https://www.vcluster.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.vcluster.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vcluster.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.vcluster.com/blog
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing known API hosts.
  evidence:
  - status: 0
    url: https://api.vcluster.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Loft Labs, now operating as vCluster Labs, provides a platform for AI cloud providers to deliver managed Kubernetes, Slurm, and inference clusters with tenant isolation. Their solution enables turnkey AI infrastructure, offering both bare‑metal and virtual machine provisioning, multi‑tenant management, capacity planning, and observability. The company targets AI cloud providers, enterprises, and hyperscalers seeking scalable, secure compute clusters, and also offers vMetal to expose physical resources as a cloud service.
image: https://cdn.prod.website-files.com/68994d4ecac027f80ff70510/692cf1d4d7bea7f25053a45c_Blank%20Open%20Graph.png
layout: provider
modified: '2026-10-13'
name: Loft Labs
nav: Providers
network: true
overview: 'Loft Labs is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Healthz API, Kubernetes API, Loft Labs API, and 2 more. Tagged areas include Artificial Intelligence, Cloud, Kubernetes, Multi-Tenant, and Infrastructure.


  The Loft Labs catalog on APIs.io includes 1 Spectral governance ruleset.


  Loft Labs'' developer surface includes CLI, authentication, changelog, documentation, getting-started guide, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Loft Labs Plans Pricing
  plan_count: 2
  slug: loft-labs-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Loft Labs API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: loft-labs-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 11.9
    developer_ergonomics: 31.0
    discoverability: 78.6
    operational_transparency: 15.8
  previous_composite: 38.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/loft-labs/loft-labs-2026-11-03T135037.png
security:
- kind: authentication
  name: Loft Labs Authentication
  slug: loft-labs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Loft Labs Domain Security
  slug: loft-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loft-labs
tags:
- Artificial Intelligence
- Cloud
- Kubernetes
- Multi-Tenant
- Infrastructure
website: https://www.loft.sh
---
