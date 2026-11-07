---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dailystudio-app/mcp/dailystudio-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dailystudio-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dailystudio-app/well-known/dailystudio-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dailystudio-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/dailystudio-app/hosts/dailystudio-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dailystudio-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/dailystudio-app/vendors/dailystudio-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dailystudio-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dailystudio-app/security/dailystudio-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dailystudio-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dailystudio.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://dailystudio.app/plan
coverage:
  checked: '2026-11-04'
  detail: No machine‑readable API contract was found; the only endpoint discovered (/mcp) requires POST and returns 405.
  evidence:
  - status: 405
    url: https://dailystudio.app/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Daily Studio is a SaaS platform that helps creators plan, record, and publish video content. It provides a web‑based studio and an iPhone teleprompter, integrates with TikTok, Reels, Shorts, and YouTube, and offers AI‑assisted script generation via connectors for Claude, ChatGPT, and Gemini. Users can organize scripts into collections, schedule posts, and review content before publishing, all from a unified workflow.
layout: provider
mcp_servers:
- description: Remote MCP server at dailystudio.app.
  name: Daily Studio MCP Server
  slug: dailystudio-app-mcp-yml
modified: '2026-11-04'
name: Daily Studio
nav: Providers
network: true
overview: 'Daily Studio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Video, Content Creation, and Teleprompter.


  Daily Studio''s developer surface includes getting-started guide and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 45.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dailystudio App Domain Security
  slug: dailystudio-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dailystudio-app
tags:
- Company
- Software-as-a-Service
- Video
- Content Creation
- Teleprompter
- Artificial Intelligence
website: https://dailystudio.app/
---
