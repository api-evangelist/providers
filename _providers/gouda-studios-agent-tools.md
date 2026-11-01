---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Gouda Studios Agent Tools Agentic Access
  operation_count: 6
  slug: gouda-studios-agent-tools-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.apify.com/v2
  baseurl_source: declared
  description: Pay-per-result data APIs for U.S. government datasets via Apify.
  name: Gouda Studios Agent Tools API
  slug: gouda-studios-agent-tools-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/gouda-studios-agent-tools/agentic-access/gouda-studios-agent-tools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gouda-studios-agent-tools-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gouda-studios-agent-tools/rules/gouda-studios-agent-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/gouda-studios-agent-tools-rules.yml
- group: agent
  href: https://artifacts.apis.io/gouda-studios-agent-tools/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gouda-studios-agent-tools/conformance/gouda-studios-agent-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gouda-studios-agent-tools-conformance.yml
- group: other
  href: https://artifacts.apis.io/gouda-studios-agent-tools/overlays/gouda-studios-agent-tools-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/gouda-studios-agent-tools-openapi-overlay.yml
- group: build
  href: https://artifacts.apis.io/gouda-studios-agent-tools/mcp/gouda-studios-agent-tools-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gouda-studios-agent-tools-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gouda-studios-agent-tools/mcp/gouda-studios-agent-tools-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gouda-studios-agent-tools-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gouda-studios-agent-tools/well-known/gouda-studios-agent-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gouda-studios-agent-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/gouda-studios-agent-tools/hosts/gouda-studios-agent-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gouda-studios-agent-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/gouda-studios-agent-tools/vendors/gouda-studios-agent-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gouda-studios-agent-tools-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gouda-studios-agent-tools/security/gouda-studios-agent-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gouda-studios-agent-tools-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gouda-studios-agent-tools/authentication/gouda-studios-agent-tools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gouda-studios-agent-tools-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gouda-studios-agent-tools.vercel.app
- group: docs
  title: ''
  type: Documentation
  url: https://gouda-studios-agent-tools.vercel.app/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://gouda-studios-agent-tools.vercel.app/openapi.json
created: '2026-10-28'
description: Gouda Studios Agent Tools provides pay-per-result data APIs for U.S. government datasets, including SAM.gov contract opportunities, SEC EDGAR filings, USAspending federal awards, and GLEIF LEI lookups, plus a website contact extraction service. All APIs return clean JSON via the Apify platform and are billed per record, enabling AI agents and developers to integrate authoritative public-sector data without managing keys or infrastructure.
image: https://aiagentslisting.com/gouda-studios-agent-tools/badge.svg?theme=light
layout: provider
mcp_servers:
- description: Remote MCP server at gouda-studios-agent-tools.vercel.app requiring OAuth.
  name: Gouda Studios Agent Tools MCP Server
  slug: gouda-studios-agent-tools-mcp-yml
modified: '2026-10-28'
name: Gouda Studios Agent Tools
nav: Providers
network: true
overview: 'Gouda Studios Agent Tools publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Government, Finance, API, and Pay-per-result.


  The Gouda Studios Agent Tools catalog on APIs.io includes 1 Spectral governance ruleset.


  Gouda Studios Agent Tools'' developer surface includes authentication, documentation, API reference, and 12 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Gouda Studios Agent Tools API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: gouda-studios-agent-tools-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 35.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gouda Studios Agent Tools Authentication
  slug: gouda-studios-agent-tools-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gouda Studios Agent Tools Domain Security
  slug: gouda-studios-agent-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 6
skills:
- name: run-gleif-company-lei-lookup
  slug: gouda-studios-agent-tools-run-gleif-company-lei-lookup
- name: run-sam-gov-opportunities-feed
  slug: gouda-studios-agent-tools-run-sam-gov-opportunities-feed
- name: run-sec-edgar-filings-feed
  slug: gouda-studios-agent-tools-run-sec-edgar-filings-feed
- name: run-usaspending-awards-search
  slug: gouda-studios-agent-tools-run-usaspending-awards-search
- name: run-website-contact-extractor
  slug: gouda-studios-agent-tools-run-website-contact-extractor
- name: run-youtube-transcript-extractor
  slug: gouda-studios-agent-tools-run-youtube-transcript-extractor
slug: gouda-studios-agent-tools
tags:
- Data
- Government
- Finance
- API
- Pay-per-result
website: https://gouda-studios-agent-tools.vercel.app
---
