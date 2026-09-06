---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldviz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.worldviz.com/
- group: company
  title: ''
  type: About
  url: https://www.worldviz.com/about-worldviz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.worldviz.com/vizard/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.worldviz.com/vizard/latest/commands/commandIndex.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.worldviz.com/vizard/latest/Installation.htm
- group: build
  title: ''
  type: Tools
  url: https://www.worldviz.com/virtual-reality-software-downloads
- group: operate
  title: ''
  type: Support
  url: https://www.worldviz.com/virtual-reality-support
- group: operate
  title: ''
  type: Community
  url: https://forum.worldviz.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.worldviz.com/
- group: operate
  title: ''
  type: FAQ
  url: https://www.worldviz.com/vizard-vr-software-faq
- group: company
  title: ''
  type: Blog
  url: https://www.worldviz.com/virtual-reality-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.worldviz.com/post/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worldviz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.worldviz.com/vizard/latest/Legal_stuff.htm
- group: build
  title: ''
  type: Packages
  url: packages/worldviz-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/worldviz-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/worldviz-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/worldviz-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worldviz-llms.txt
coverage:
  checked: '2026-09-04'
  detail: WorldViz publishes a complete, crawlable Vizard command reference — 1,182 individual command pages across 36 Python modules, sitemapped and readable by a human — but no OpenAPI, AsyncAPI, GraphQL SDL, JSON Schema, Postman collection or .well-known document exists on any of its eight hosts, because the toolkit is an installed Windows product rather than a hosted API.
  evidence:
  - status: 200
    url: https://docs.worldviz.com/vizard/latest/commands/commandIndex.htm
  - status: 200
    url: https://docs.worldviz.com/vizard/latest/Sitemap.xml
  - status: 404
    url: https://docs.worldviz.com/openapi.json
  - status: 404
    url: https://www.worldviz.com/openapi.json
  - status: 404
    url: https://www.worldviz.com/.well-known/api-catalog
  - status: 404
    url: https://www.worldviz.com/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-04'
description: 'WorldViz LLC is a Santa Barbara, California virtual reality company that builds VR software and turnkey systems for academic research, training and simulation. Its developer surface is Vizard, a Python 3.13 VR development toolkit and IDE for Windows with a documented command reference of roughly 1,182 commands across 36 modules, extended by the SightLab VR Pro experiment-authoring plugin, the Vizible collaboration product, PPT precision motion tracking, and PRISM projection and simulation room systems. WorldViz publishes no web API: no OpenAPI, AsyncAPI, GraphQL schema, MCP server, agent card or .well-known document was found on any of its eight public hosts. Its machine-relevant surface is the Vizard Python library reference, its dated release notes, and its downloadable installers.'
image: https://cdn.prod.website-files.com/5a9058c8f7462d00014ad4eb/5a9694b141e04900018b1626_worldviz%20logo%20thumbnail.png
layout: provider
modified: '2026-09-04'
name: WorldViz
nav: Providers
network: true
overview: 'WorldViz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Virtual Reality, Augmented Reality, Simulation, Research, and Training.


  WorldViz''s developer surface includes documentation, API reference, getting-started guide, tooling, support, FAQ, engineering blog, and 13 more developer resources.'
plans:
- name: Worldviz Plans Pricing
  plan_count: 4
  slug: worldviz-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Worldviz Rate Limits
  slug: worldviz-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 23.3
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Worldviz Domain Security
  slug: worldviz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worldviz
tags:
- Virtual Reality
- Augmented Reality
- Simulation
- Research
- Training
- 3D Graphics
- Eye Tracking
- Motion Tracking
- Python
- Software
website: https://www.worldviz.com/
---
