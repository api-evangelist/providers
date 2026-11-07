---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AutoGen is a Microsoft framework for building multi-agent conversational AI systems.
  name: AutoGen
  slug: autogen
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/autogen/hosts/autogen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autogen-hosts.yml
- group: other
  href: https://artifacts.apis.io/autogen/vendors/autogen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autogen-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/autogen/plans/autogen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autogen-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/autogen/rate-limits/autogen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autogen-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/autogen/finops/autogen-finops.yml
  title: ''
  type: FinOps
  url: finops/autogen-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://microsoft.github.io/autogen/0.2/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://microsoft.github.io/autogen/
- group: docs
  title: ''
  type: Documentation
  url: https://microsoft.github.io/autogen/stable/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://microsoft.github.io/autogen/stable/reference/index.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/autogen
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
coverage:
  checked: '2026-11-04'
  detail: AutoGen is an open-source Python/.NET library documented at microsoft.github.io/autogen with no hosted HTTP API, OpenAPI, llms.txt (404) or MCP endpoint; its surface is the PyPI packages.
  evidence:
  - status: 200
    url: https://microsoft.github.io/autogen/stable/index.html
  - status: 404
    url: https://microsoft.github.io/autogen/llms.txt
  - status: 200
    url: https://microsoft.github.io/autogen/stable/reference/index.html
  reason: no-developer-program
  state: none
created: '2026-03-27'
description: 'AutoGen is an open-source Microsoft framework for building multi-agent conversational AI systems, distributed as Python packages (autogen-agentchat, autogen-core, autogen-ext, autogenstudio) and a .NET preview. It is a library, not a hosted service: there is no public HTTP API, OpenAPI contract or hosted MCP endpoint.'
finops:
- has_sources: false
  method: generated
  name: Autogen Finops
  primary_unit: request
  service_category: API
  slug: autogen-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autogen.png
layout: provider
modified: '2026-11-04'
name: AutoGen
nav: Providers
network: true
overview: 'AutoGen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, AI Automation, Multi-Agent Systems, Open Source, and Python.


  AutoGen''s developer surface includes engineering blog, documentation, API reference, and 8 more developer resources.'
plans:
- name: Autogen Plans Pricing
  plan_count: 3
  slug: autogen-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Autogen Rate Limits
  slug: autogen-rate-limits
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 4.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/autogen/autogen-2026-06-20T172641.png
slug: autogen
tags:
- AI Agents
- AI Automation
- Multi-Agent Systems
- Open Source
- Python
- Framework
website: https://microsoft.github.io/autogen/
---
