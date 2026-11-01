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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/frapea-com/llms/frapea-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/frapea-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/frapea-com/mcp/frapea-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/frapea-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/frapea-com/hosts/frapea-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/frapea-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/frapea-com/vendors/frapea-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/frapea-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/frapea-com/packages/frapea-com-packages.yml
  title: ''
  type: SDKs
  url: packages/frapea-com-packages.yml
- group: build
  href: https://artifacts.apis.io/frapea-com/packages/frapea-com-packages.yml
  title: ''
  type: Packages
  url: packages/frapea-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/frapea-com/security/frapea-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frapea-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frapea.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://frapea.com/connect
- group: operate
  title: ''
  type: Support
  url: https://frapea.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://frapea.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://frapea.com/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://frapea.com/mcp
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.frapea.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Frapea provides a professional AI‑powered video editor that runs entirely in the browser. Users can connect large language models like Claude, ChatGPT, Cursor or Codex to edit videos, add captions, titles, and export results, all without installing software. The platform offers a range of use‑cases, from quick AI‑driven cuts to detailed timeline editing, and includes a free tier for basic editing.
image: https://frapea.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.frapea.com.
  name: frapea-com MCP Server
  slug: frapea-com-mcp-yml
modified: '2026-10-30'
name: frapea-com
nav: Providers
network: true
overview: 'frapea-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video Editing, AI, Browser-based, No-install, and Creative Tools.


  frapea-com''s developer surface includes getting-started guide, support, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.3
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Frapea Com Domain Security
  slug: frapea-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: frapea-com
tags:
- Video Editing
- AI
- Browser-based
- No-install
- Creative Tools
website: https://frapea.com/
---
