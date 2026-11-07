---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: OpenAI- and Anthropic-compatible proxy API of the Manifest LLM gateway. Clients point at the gateway URL, send `auto` as the model and routing picks the real model; documented endpoints are POST /v1/c
  name: Manifest LLM Gateway API
  slug: llm-gateway-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/manifest/rate-limits/manifest-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/manifest-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/manifest/plans/manifest-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/manifest-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/manifest/cli/manifest-cli.yml
  title: ''
  type: CLI
  url: cli/manifest-cli.yml
- group: operate
  href: https://artifacts.apis.io/manifest/changelog/manifest-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/manifest-changelog.yml
- group: design
  href: https://artifacts.apis.io/manifest/conventions/manifest-conventions.yml
  title: ''
  type: Conventions
  url: conventions/manifest-conventions.yml
- group: auth
  href: https://artifacts.apis.io/manifest/authentication/manifest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/manifest-authentication.yml
- group: auth
  href: https://artifacts.apis.io/manifest/scopes/manifest-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/manifest-scopes.yml
- group: operate
  href: https://artifacts.apis.io/manifest/lifecycle/manifest-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/manifest-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/manifest/lifecycle/manifest-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/manifest-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/manifest/errors/manifest-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/manifest-error-codes.yml
- group: design
  href: https://artifacts.apis.io/manifest/conformance/manifest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/manifest-conformance.yml
- group: agent
  href: https://artifacts.apis.io/manifest/llms/manifest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/manifest-llms.txt
- group: other
  href: https://artifacts.apis.io/manifest/a2a/manifest-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/manifest-a2a.yml
- group: agent
  href: https://artifacts.apis.io/manifest/mcp/manifest-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/manifest-mcp.yml
- group: agent
  href: https://artifacts.apis.io/manifest/well-known/manifest-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/manifest-well-known.yml
- group: other
  href: https://artifacts.apis.io/manifest/hosts/manifest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/manifest-hosts.yml
- group: build
  href: https://artifacts.apis.io/manifest/integrations/manifest-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/manifest-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/manifest/vendors/manifest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/manifest-vendors.yml
- group: build
  href: https://artifacts.apis.io/manifest/packages/manifest-packages.yml
  title: ''
  type: SDKs
  url: packages/manifest-packages.yml
- group: build
  href: https://artifacts.apis.io/manifest/packages/manifest-packages.yml
  title: ''
  type: Packages
  url: packages/manifest-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.manifest.build</code
- group: auth
  href: https://artifacts.apis.io/manifest/security/manifest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/manifest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://manifest.build
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mnfst
- group: docs
  title: ''
  type: Documentation
  url: https://manifest.build/llm-gateway/docs/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://manifest.build/llm-gateway/docs/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.manifest.build/quickstart
- group: company
  title: ''
  type: Blog
  url: https://manifest.build/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://manifest.build/changelog/
- group: commercial
  title: ''
  type: Pricing
  url: https://manifest.build/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://manifest.build/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://manifest.build/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.manifest.build/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/FepAked3W7
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mnfst/manifest
- group: other
  title: ''
  type: DockerImage
  url: https://hub.docker.com/r/manifestdotbuild/manifest
coverage:
  checked: '2026-11-05'
  detail: Manifest documents its OpenAI/Anthropic-compatible gateway endpoints (/v1/chat/completions, /v1/responses, /v1/messages, /v1/models) only in markdown docs; app.manifest.build answers /openapi.json with its HTML app shell and /v1/openapi.json with 404.
  evidence:
  - status: 200
    url: https://app.manifest.build/openapi.json
  - status: 404
    url: https://app.manifest.build/v1/openapi.json
  - status: 200
    url: https://manifest.build/llm-gateway/docs/reference/api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Manifest is an open-source LLM gateway for AI agents and agentic workflows, connecting them to any model provider through one OpenAI-compatible endpoint. It routes requests across subscriptions, pay-per-token, bring-your-own-key, local models and custom providers, falls back when providers are down, autofixes broken requests on the fly, and tracks every request, token and dollar for observability. It can be self-hosted (Docker image manifestdotbuild/manifest, code at github.com/mnfst/manifest) or used as a cloud service at app.manifest.build.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manifest.png
layout: provider
mcp_servers:
- description: 'Official remote Model Context Protocol server run by the Manifest LLM gateway. It manages the authorizing user''s workspace (harnesses, provider connections, routing, models, prices, request log) over '
  name: Manifest MCP Server
  slug: manifest-mcp-server
modified: '2026-11-05'
name: Manifest
nav: Providers
network: true
overview: 'Manifest is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LLM Gateway, AI Agents, Artificial Intelligence, and Open Source.


  Manifest''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
plans:
- name: Manifest Plans Pricing
  plan_count: 3
  slug: manifest-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Manifest Rate Limits
  slug: manifest-rate-limits
scopes:
- name: Manifest Scopes
  scope_count: 3
  slug: manifest-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 46.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 60.5
  previous_composite: 2.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/manifest/manifest-2026-07-25T230047.png
security:
- kind: authentication
  name: Manifest Authentication
  slug: manifest-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Manifest Domain Security
  slug: manifest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: manifest
tags:
- Company
- LLM Gateway
- AI Agents
- Artificial Intelligence
- Open Source
- Observability
- OpenAI-Compatible
- Self-Hosted
website: https://manifest.build
---
