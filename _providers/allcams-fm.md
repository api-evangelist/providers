---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
api_count: 1
apis:
- description: MCP server providing tool list for AI agents.
  name: Allcams MCP
  slug: allcams-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/allcams-fm/llms/allcams-fm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allcams-fm-llms.txt
- group: build
  href: https://artifacts.apis.io/allcams-fm/mcp/allcams-fm-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/allcams-fm-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/allcams-fm/mcp/allcams-fm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/allcams-fm-mcp.yml
- group: agent
  href: https://artifacts.apis.io/allcams-fm/well-known/allcams-fm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allcams-fm-well-known.yml
- group: other
  href: https://artifacts.apis.io/allcams-fm/hosts/allcams-fm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allcams-fm-hosts.yml
- group: other
  href: https://artifacts.apis.io/allcams-fm/vendors/allcams-fm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allcams-fm-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allcams
- group: auth
  href: https://artifacts.apis.io/allcams-fm/security/allcams-fm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allcams-fm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allcams.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://allcams.fm/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://allcams.fm/mcp/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allcams.fm/en/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allcams.fm/en/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://allcams.fm/en/legal/contact/
created: '2026-11-01'
description: Allcams is an adult live cam aggregator that indexes streams from multiple adult cam platforms, providing a unified searchable directory without hosting any content itself. The site offers age‑verification compliance, affiliate disclosures, and earns commission via referral links. It maintains legal compliance with U.S. 2257 record‑keeping, GDPR and CCPA, and provides a developer MCP server for AI agents. Allcams aims to keep listings honest by removing dead or duplicate entries and supporting multiple languages.
image: https://allcams.fm/images/logo-2.svg
layout: provider
mcp_servers:
- description: Remote MCP server at allcams.fm.
  name: Allcams MCP Server
  slug: allcams-fm-mcp-yml
modified: '2026-11-01'
name: Allcams
nav: Providers
network: true
overview: 'Allcams is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Adult, Cam Aggregator, Live Streaming, Entertainment, and Adult Content.


  Allcams'' developer surface includes documentation, support, and 12 more developer resources.'
random_paper: 5
scopes:
- name: Allcams Fm Scopes
  scope_count: 0
  slug: allcams-fm-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 17.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Allcams Fm Authentication
  slug: allcams-fm-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Allcams Fm Domain Security
  slug: allcams-fm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allcams-fm
tags:
- Adult
- Cam Aggregator
- Live Streaming
- Entertainment
- Adult Content
website: https://allcams.fm/
---
