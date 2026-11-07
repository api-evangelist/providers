---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the CaaMTech website at caam.tech: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: CaaMTech Website (WordPress REST)
  slug: caam-tech-website-wordpress-rest
artifact_total: 9
collections:
- collection_type: open
  name: CaaMTech WordPress REST MCP API
  slug: open-caamtech-mcp-api
- collection_type: open
  name: API Collection
  slug: open-caamtech-wordpress-rest-routes-original
common:
- group: agent
  href: https://artifacts.apis.io/caamtech/mcp/caamtech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caamtech-mcp.yml
- group: other
  href: https://artifacts.apis.io/caamtech/overlays/caamtech-wordpress-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caamtech-wordpress-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://caam.tech/
- group: company
  title: ''
  type: Blog
  url: https://caam.tech/updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://caam.tech/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caamtech
- group: auth
  href: https://artifacts.apis.io/caamtech/authentication/caamtech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caamtech-authentication.yml
- group: design
  href: https://artifacts.apis.io/caamtech/conventions/caamtech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/caamtech-conventions.yml
- group: design
  href: https://artifacts.apis.io/caamtech/errors/caamtech-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/caamtech-error-codes.yml
- group: design
  href: https://artifacts.apis.io/caamtech/lifecycle/caamtech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/caamtech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/caamtech/conformance/caamtech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caamtech-conformance.yml
- group: design
  href: https://artifacts.apis.io/caamtech/data-model/caamtech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/caamtech-data-model.yml
- group: auth
  href: https://artifacts.apis.io/caamtech/security/caamtech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caamtech-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/caamtech/llms/caamtech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caamtech-llms.txt
- group: agent
  href: https://artifacts.apis.io/caamtech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: CaaMTech is a pharmaceutical drug discovery company in Issaquah, Washington, founded by Dr. Andrew Chadeayne, engineering next-generation psychedelic-inspired small-molecule therapeutics for mental health conditions. It synthesizes and characterizes novel tryptamines, screens natural and synthetic compounds for safety and efficacy, publishes fundamental crystallographic and pharmacological research, and builds a patent portfolio around the results. CaaMTech operates no developer program and publishes no product API; the only machine-readable surface on caam.tech is the standard WordPress REST API that serves the company site, which does make its research updates, pages and media programmatically readable without credentials, alongside an authenticated WordPress MCP adapter endpoint.
image: https://caam.tech/wp-content/uploads/2019/12/cropped-caamtech-logo-on-green-2400-square.png
layout: provider
mcp_servers:
- description: Remote MCP server at caam.tech over HTTP.
  name: CaaMTech MCP Server
  slug: mcp-adapter-default-server
modified: '2026-08-08'
name: CaaMTech
nav: Providers
network: true
overview: 'CaaMTech publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Drug Discovery, and Biotechnology.


  The CaaMTech catalog on APIs.io includes 1 Spectral governance ruleset.


  CaaMTech''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: CaaMTech API Rules
  rule_count: 52
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 3
  slug: caamtech-rules
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 1.7
    developer_ergonomics: 20.8
    discoverability: 60.0
    operational_transparency: 0.0
  previous_composite: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/caamtech/caamtech-2026-09-02T144955.png
security:
- kind: authentication
  name: Caamtech Authentication
  slug: caamtech-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Caamtech Domain Security
  slug: caamtech-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Discover the CaaMTech machine-readable surface
  slug: caamtech-discover-site-surface
- name: Read CaaMTech research updates
  slug: caamtech-read-research-updates
slug: caamtech
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Biotechnology
- Chemistry
- Mental Health
- Research
- Psychedelics
- WordPress
website: https://caam.tech/
---
