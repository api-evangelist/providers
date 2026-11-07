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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Create a scribe animation, poll its status, download the watermarked preview, optionally unlock the clean video, or delete the session. Session files expire within 24 hours.
  name: The Scribble Thing Agent API
  slug: the-scribble-thing-agent-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/boringstuff-club/plans/boringstuff-club-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boringstuff-club-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/boringstuff-club/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/boringstuff-club/conformance/boringstuff-club-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boringstuff-club-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boringstuff-club/llms/boringstuff-club-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boringstuff-club-llms.txt
- group: build
  href: https://artifacts.apis.io/boringstuff-club/mcp/boringstuff-club-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/boringstuff-club-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/boringstuff-club/mcp/boringstuff-club-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boringstuff-club-mcp.yml
- group: other
  href: https://artifacts.apis.io/boringstuff-club/hosts/boringstuff-club-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boringstuff-club-hosts.yml
- group: other
  href: https://artifacts.apis.io/boringstuff-club/vendors/boringstuff-club-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boringstuff-club-vendors.yml
- group: auth
  href: https://artifacts.apis.io/boringstuff-club/security/boringstuff-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boringstuff-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boringstuff.club/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scribble.boringstuff.club/
- group: docs
  title: ''
  type: Documentation
  url: https://scribble.boringstuff.club/docs/agent-api
- group: docs
  title: ''
  type: APIReference
  url: https://scribble.boringstuff.club/docs/agent-api
- group: start
  title: ''
  type: GettingStarted
  url: https://scribble.boringstuff.club/
- group: operate
  title: ''
  type: Support
  url: https://scribble.boringstuff.club/contact?feature=general
- group: commercial
  title: ''
  type: Pricing
  url: https://scribble.boringstuff.club/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scribble.boringstuff.club/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scribble.boringstuff.club/privacy
created: '2026-11-02'
description: Boring Stuff Club provides a platform that turns line art into hand‑drawn style animation using AI. Users can upload simple illustrations, add optional audio, and receive a finished video without needing animation expertise. The service offers a free preview, watermark‑free videos for a low fee, and integrates with AI agents for automated storytelling. It targets creators, marketers, and developers needing quick animated content for demos, explainer videos, or social media.
image: https://scribble.boringstuff.club/static/the-scribble-thing-demo-poster.png
layout: provider
mcp_servers:
- description: Remote MCP server at scribble.boringstuff.club.
  name: Boring Stuff Club MCP Server
  slug: boringstuff-club-mcp-yml
modified: '2026-11-02'
name: Boring Stuff Club
nav: Providers
network: true
overview: 'Boring Stuff Club is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Animation, Illustration, Product Demo, and Education.


  Boring Stuff Club''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 13 more developer resources.'
plans:
- name: Boringstuff Club Plans Pricing
  plan_count: 3
  slug: boringstuff-club-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boringstuff Club Domain Security
  slug: boringstuff-club-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: boringstuff-club-agent
  slug: boringstuff-club-agent
slug: boringstuff-club
tags:
- Animation
- Illustration
- Product Demo
- Education
website: https://boringstuff.club/
---
