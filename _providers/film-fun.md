---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for agents and scripts to create productions, generate media (image, video, voice, music), edit assets, and manage credits.
  name: Splice API
  slug: splice-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/film-fun/plans/film-fun-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/film-fun-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/film-fun/cli/film-fun-cli.yml
  title: ''
  type: CLI
  url: cli/film-fun-cli.yml
- group: auth
  href: https://artifacts.apis.io/film-fun/authentication/film-fun-authentication.yml
  title: ''
  type: Authentication
  url: authentication/film-fun-authentication.yml
- group: design
  href: https://artifacts.apis.io/film-fun/conformance/film-fun-conformance.yml
  title: ''
  type: Conformance
  url: conformance/film-fun-conformance.yml
- group: agent
  href: https://artifacts.apis.io/film-fun/llms/film-fun-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/film-fun-llms.txt
- group: agent
  href: https://artifacts.apis.io/film-fun/mcp/film-fun-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/film-fun-mcp.yml
- group: auth
  href: https://artifacts.apis.io/film-fun/well-known/film-fun-splice-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/film-fun-splice-security.txt
- group: agent
  href: https://artifacts.apis.io/film-fun/well-known/film-fun-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/film-fun-well-known.yml
- group: other
  href: https://artifacts.apis.io/film-fun/hosts/film-fun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/film-fun-hosts.yml
- group: other
  href: https://artifacts.apis.io/film-fun/vendors/film-fun-vendors.yml
  title: ''
  type: Vendors
  url: vendors/film-fun-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.film.fun/help
- group: start
  title: ''
  type: SignUp
  url: https://splice.film.fun/signup?redirectTo=%2Fdashboard%2Ftemplates%2Fremix%2Fe27bbc52-f11b-4a79-9ec5-9248d0a6fb21%3Futm_source%3Dcommunity%26utm_medium%3Dwebsite%26utm_campaign%3Dtemplates%26utm_content%3Dcard&utm_source=community&utm_medium=website&utm_campaign=templates&utm_content=card
- group: docs
  title: ''
  type: APIReference
  url: https://splice.film.fun/api-docs
- group: auth
  href: https://artifacts.apis.io/film-fun/security/film-fun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/film-fun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://film.fun/
- group: docs
  title: ''
  type: Documentation
  url: https://splice.film.fun/developers
- group: start
  title: ''
  type: DeveloperPortal
  url: https://splice.film.fun/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://splice.film.fun/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.film.fun/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.film.fun/privacy
created: '2026-10-30'
description: Film Fun provides an AI-powered video editing and filmmaking platform that lets creators generate, edit, and assemble movies using artificial intelligence. Users can create scripts, storyboards, shot lists, and final cuts with AI‑generated footage and effects, all within a browser‑based interface. The service offers free credits, a marketplace of templates, and integrates with popular AI models like Claude, ChatGPT, Grok, and Codex. It targets filmmakers, marketers, and content creators seeking rapid, cost‑effective video production.
image: https://www.film.fun/ff-social.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at splice.film.fun.
  name: film-fun MCP Server
  slug: film-fun-mcp-yml
modified: '2026-10-30'
name: film-fun
nav: Providers
network: true
overview: 'film-fun is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, VideoEditing, Filmmaking, and Platform.


  film-fun''s developer surface includes CLI, authentication, support, signup flow, API reference, documentation, pricing, and 13 more developer resources.'
plans:
- name: Film Fun Plans Pricing
  plan_count: 4
  slug: film-fun-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Film Fun Authentication
  slug: film-fun-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Film Fun Domain Security
  slug: film-fun-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: film-fun
tags:
- Company
- AI
- VideoEditing
- Filmmaking
- Platform
website: https://film.fun/
---
