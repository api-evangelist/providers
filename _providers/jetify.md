---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://search.devbox.sh/v2
  baseurl_source: declared
  description: The Pkg API from Jetify — 1 operation(s) for pkg.
  name: Jetify Pkg API
  slug: jetify-pkg-api
- baseURL: https://search.devbox.sh/v2
  baseurl_source: declared
  description: The Resolve API from Jetify — 1 operation(s) for resolve.
  name: Jetify Resolve API
  slug: jetify-resolve-api
- baseURL: https://search.devbox.sh/v2
  baseurl_source: declared
  description: The Search API from Jetify — 1 operation(s) for search.
  name: Jetify Search API
  slug: jetify-search-api
artifact_total: 12
collections:
- collection_type: open
  name: Nixhub Pkg API
  slug: open-jetify-pkg-api
- collection_type: open
  name: Nixhub Pkg Resolve API
  slug: open-jetify-resolve-api
- collection_type: open
  name: Nixhub Pkg Search API
  slug: open-jetify-search-api
common:
- group: other
  href: https://artifacts.apis.io/jetify/capabilities/jetify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jetify-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/jetify/plans/jetify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jetify-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/jetify/overlays/jetify-nixhub-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jetify-nixhub-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.jetify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.jetify.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetify.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.jetify.com/docs/nixhub/
- group: company
  title: ''
  type: Blog
  url: https://www.jetify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jetify-com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jetify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.jetify.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jetify.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jetify.com/legal/privacy
- group: build
  href: https://artifacts.apis.io/jetify/packages/jetify-packages.yml
  title: ''
  type: SDKs
  url: packages/jetify-packages.yml
- group: build
  href: https://artifacts.apis.io/jetify/packages/jetify-packages.yml
  title: ''
  type: Packages
  url: packages/jetify-packages.yml
- group: build
  href: https://artifacts.apis.io/jetify/cli/jetify-cli.yml
  title: ''
  type: CLI
  url: cli/jetify-cli.yml
- group: agent
  href: https://artifacts.apis.io/jetify/llms/jetify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jetify-llms.txt
- group: agent
  href: https://artifacts.apis.io/jetify/well-known/jetify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jetify-well-known.yml
- group: auth
  href: https://artifacts.apis.io/jetify/security/jetify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jetify-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jetify/authentication/jetify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jetify-authentication.yml
- group: design
  href: https://artifacts.apis.io/jetify/conventions/jetify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jetify-conventions.yml
- group: design
  href: https://artifacts.apis.io/jetify/conventions/jetify-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jetify-conventions.yml
- group: design
  href: https://artifacts.apis.io/jetify/lifecycle/jetify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jetify-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/jetify/lifecycle/jetify-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/jetify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jetify/conformance/jetify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jetify-conformance.yml
- group: design
  href: https://artifacts.apis.io/jetify/errors/jetify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jetify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jetify/data-model/jetify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jetify-data-model.yml
- group: agent
  href: https://artifacts.apis.io/jetify/mcp/jetify-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/jetify-mcp.yml
- group: agent
  href: https://artifacts.apis.io/jetify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Jetify builds developer tooling for reproducible environments and package management, backed by the Nix ecosystem. Its open-source Devbox CLI creates instant, isolated, predictable development shells; Jetify Cloud adds team secrets management, a private Nix package cache, and deployments; Nixhub indexes over one million package versions across 100,000+ Nix packages and exposes a free, public REST API for searching and resolving them; and Testpilot is an AI agent for autonomous end-to-end testing. Jetify is backed by GV and Homebrew. This profile was enriched by the API Evangelist pipeline from Jetify's public docs, npm/Go registries, and live API probes.
finops:
- has_sources: true
  method: derived
  name: Jetify Finops
  primary_unit: gb
  service_category: ''
  slug: jetify-finops
  template: false
image: https://avatars.githubusercontent.com/u/65328393?v=4
layout: provider
modified: '2026-07-19'
name: Jetify
nav: Providers
network: true
overview: 'Jetify publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Pkg API, Resolve API, and Search API. Tagged areas include Company, Enterprise, Developer Tools, Nix, and Package Management.


  Jetify''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, CLI, authentication, and 22 more developer resources.'
plans:
- name: Jetify Plans Pricing
  plan_count: 7
  slug: jetify-plans-pricing
- name: Jetify Price Estimates
  plan_count: 0
  slug: jetify-price-estimates
random_paper: 3
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 46.5
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jetify/jetify-2026-07-25T223137.png
security:
- kind: authentication
  name: Jetify Authentication
  slug: jetify-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Jetify Domain Security
  slug: jetify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: jetify-resolve-nix-package
  slug: jetify-resolve-package
slug: jetify
tags:
- Company
- Enterprise
- Developer Tools
- Nix
- Package Management
- Developer Environments
- Reproducible Builds
- CLI
- Search
website: https://www.jetify.com
---
