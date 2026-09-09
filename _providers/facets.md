---
access_model:
  confidence: high
  label: Paid with a 14-day free trial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-09-08'
api_count: 1
apis:
- baseURL: https://{account-id}.console.facets.cloud
  baseurl_source: declared
  description: The Facets Control Plane REST API. 519 paths and 629 operations across blueprints (stacks), environments (clusters), releases, resources, overrides, artifacts and builds, modules, variables and secret
  name: Facets Control Plane API
  slug: facets
artifact_total: 8
asyncapis:
- description: ''
  name: Facets Webhooks
  slug: facets-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.facets.cloud/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.facets.cloud/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.facets.cloud/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.facets.cloud/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.facets.cloud/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.facets.cloud/docs/support
- group: company
  title: ''
  type: Blog
  url: https://www.facets.cloud/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.facets.cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.facets.cloud/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.facets.cloud/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.facets.cloud/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Facets-cloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/facets-cloud
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.facets.cloud/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.facets.cloud/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/facets-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.facets.cloud/product/deployment
- group: auth
  title: ''
  type: Authentication
  url: authentication/facets-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/facets-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/facets-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/facets-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/facets-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/facets-cli.yml
- group: design
  title: ''
  type: Components
  url: components/facets-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/facets-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/facets-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/facets-domain-security.yml
created: '2025-02-08'
description: Facets is an AI-native SDLC orchestrator and platform-engineering control plane that unifies infrastructure provisioning, CI/CD and configuration management into a single declarative blueprint model, so product teams get self-serve, drift-free cloud environments without writing Terraform by hand. The Facets Control Plane exposes a 629-operation REST API - published as OpenAPI 3.0.1 at /v3/api-docs on each customer's own control-plane host - covering blueprints, projects, environments, releases, resources, artifacts, modules, notifications and access control. Facets also ships two first-party CLIs (raptor and praxis), three MCP servers, a Terraform provider, and Praxis, a set of AI agents that automate platform operations across the SDLC.
finops:
- name: Facets Finops
  service_category: API
  slug: facets-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/facets.png
layout: provider
mcp_servers:
- description: ''
  name: Facets MCP Server
  slug: facets-mcp-server
modified: '2026-09-07'
name: Facets
nav: Providers
network: true
overview: 'Facets publishes 1 API on the [APIs.io](https://apis.io/) network: Control Plane API. Tagged areas include Automation, Infrastructure, Orchestration, Platform Engineering, and DevOps.


  The Facets catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Facets'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Facets Plans Pricing
  plan_count: 2
  slug: facets-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Facets Rate Limits
  slug: facets-rate-limits
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 60.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/facets/refs/heads/main/screenshots/facets-2026-06-20T181034.png
security:
- kind: authentication
  name: Facets Authentication
  slug: facets-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Facets Domain Security
  slug: facets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: facets
tags:
- Automation
- Infrastructure
- Orchestration
- Platform Engineering
- DevOps
- Internal Developer Platform
- Terraform
- Kubernetes
- Continuous Delivery
- AI Agents
website: https://www.facets.cloud/
---
