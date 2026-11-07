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
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://choruskeepsake.com/api
  baseurl_source: declared
  description: API for creating and managing Chorus Keepsake books.
  name: Chorus API
  slug: chorus-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/choruskeepsake-com/conformance/choruskeepsake-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/choruskeepsake-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/choruskeepsake-com/llms/choruskeepsake-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/choruskeepsake-com-llms.txt
- group: build
  href: https://artifacts.apis.io/choruskeepsake-com/mcp/choruskeepsake-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/choruskeepsake-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/choruskeepsake-com/mcp/choruskeepsake-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/choruskeepsake-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/choruskeepsake-com/well-known/choruskeepsake-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/choruskeepsake-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/choruskeepsake-com/hosts/choruskeepsake-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/choruskeepsake-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/choruskeepsake-com/vendors/choruskeepsake-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/choruskeepsake-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://choruskeepsake.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://choruskeepsake.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://choruskeepsake.com/guides/how-to-save-someones-voice/
- group: company
  title: ''
  type: Blog
  url: https://choruskeepsake.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://choruskeepsake.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/choruskeepsake-com/security/choruskeepsake-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/choruskeepsake-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://choruskeepsake.com/
created: '2026-11-03'
description: Chorus Keepsake offers a platform that lets users collect voice, video, text, and photo memories into a physical book. Gathering stories is free, and the service provides a simple way to record messages for birthdays, weddings, new babies, or in memory of loved ones. The company emphasizes easy sharing and preserving cherished moments in a tangible format.
image: https://choruskeepsake.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at choruskeepsake.com.
  name: Chorus Keepsake MCP Server
  slug: choruskeepsake-com-mcp-yml
modified: '2026-11-03'
name: Chorus Keepsake
nav: Providers
network: true
overview: 'Chorus Keepsake is listed with 1 API on the [APIs.io](https://apis.io/) network: Chorus API. Tagged areas include Company, Memories, Gifts, PhotoBook, and Voice.


  Chorus Keepsake''s developer surface includes documentation, engineering blog, API reference, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 34.4
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Choruskeepsake Com Domain Security
  slug: choruskeepsake-com-domain-security
  summary_line: TLSv1.3
slug: choruskeepsake-com
tags:
- Company
- Memories
- Gifts
- PhotoBook
- Voice
- Video
website: https://choruskeepsake.com/
---
