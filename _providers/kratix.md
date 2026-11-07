---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Kratix is an open-source framework for building internal developer platforms using Kubernetes. Platform teams author Promises that wrap complex services into self-service APIs delivered as Kubernetes '
  name: Kratix
  slug: kratix
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/kratix/plans/kratix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kratix-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kratix/rate-limits/kratix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kratix-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kratix/finops/kratix-finops.yml
  title: ''
  type: FinOps
  url: finops/kratix-finops.yml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/syntasso/kratix/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/syntasso/kratix/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/syntasso/kratix/blob/main/LICENSE
- group: auth
  href: https://artifacts.apis.io/kratix/security/kratix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kratix-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/syntasso
- group: company
  title: ''
  type: Website
  url: https://kratix.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kratix.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kratix.io/main/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.syntasso.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syntasso
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/syntasso/kratix
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/syntasso/kratix/issues
- group: other
  title: ''
  type: Marketplace
  url: https://docs.kratix.io/marketplace
- group: agent
  title: ''
  type: LlmsText
  url: https://kratix.io/llms.txt
created: '2026-03-27'
description: Kratix is an open-source framework for building internal developer platforms using Kubernetes, enabling platform teams to deliver customizable, composable Promises as a Service. Kratix exposes its capabilities through Kubernetes Custom Resource Definitions (Promise, Resource, WorkloadGroup, Destination, StateStore) rather than a traditional HTTP API.
finops:
- has_sources: false
  method: generated
  name: Kratix Finops
  primary_unit: request
  service_category: API
  slug: kratix-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kratix.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.kratix.io over HTTP; 10 tools listed.
  name: Kratix MCP Server
  slug: kratix
modified: '2026-04-28'
name: Kratix
nav: Providers
network: true
overview: 'Kratix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Experience, Internal Developer Platform, Kubernetes, Open Source, and Platform Engineering.


  Kratix''s developer surface includes documentation, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Kratix Plans Pricing
  plan_count: 3
  slug: kratix-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Kratix Rate Limits
  slug: kratix-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.7
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 19.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kratix/kratix-2026-06-20T184151.png
security:
- kind: domain-security
  name: Kratix Domain Security
  slug: kratix-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kratix
tags:
- Developer Experience
- Internal Developer Platform
- Kubernetes
- Open Source
- Platform Engineering
website: https://kratix.io
---
