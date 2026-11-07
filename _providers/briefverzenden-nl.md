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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/briefverzenden-nl/llms/briefverzenden-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/briefverzenden-nl-llms.txt
- group: agent
  href: https://artifacts.apis.io/briefverzenden-nl/mcp/briefverzenden-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/briefverzenden-nl-mcp.yml
- group: agent
  href: https://artifacts.apis.io/briefverzenden-nl/well-known/briefverzenden-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/briefverzenden-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/briefverzenden-nl/hosts/briefverzenden-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/briefverzenden-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/briefverzenden-nl/vendors/briefverzenden-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/briefverzenden-nl-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.briefverzenden.nl/en/registered-email
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.briefverzenden.nl/privacy
- group: auth
  href: https://artifacts.apis.io/briefverzenden-nl/security/briefverzenden-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/briefverzenden-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://briefverzenden.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://www.briefverzenden.nl/agents
- group: company
  title: ''
  type: About
  url: https://www.briefverzenden.nl/over-ons
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.briefverzenden.nl/voorwaarden
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found despite a documented API reference page.
  evidence:
  - status: 200
    url: https://www.briefverzenden.nl/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Briefverzenden biedt een online service waarmee je in ongeveer 30 seconden een brief kunt versturen zonder printer. Je uploadt eenvoudig een PDF, wij printen en verzenden de brief binnen 24 uur. De service omvat ook aangetekende verzending, zonder dat je een postzegel of een account nodig hebt. Het platform richt zich op snelle, papierloze postverzending voor zowel particulieren als bedrijven, met een gebruiksvriendelijke interface en transparante prijzen.
layout: provider
mcp_servers:
- description: Remote MCP server at www.briefverzenden.nl.
  name: Briefverzenden MCP Server
  slug: briefverzenden-nl-mcp-yml
modified: '2026-11-03'
name: Briefverzenden
nav: Providers
network: true
overview: 'Briefverzenden is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Online, Postal, PDF, and Netherlands.


  Briefverzenden''s developer surface includes signup flow, documentation, and 10 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 45.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Briefverzenden Nl Domain Security
  slug: briefverzenden-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: briefverzenden-nl
tags:
- Company
- Online
- Postal
- PDF
- Netherlands
website: https://briefverzenden.nl/
---
