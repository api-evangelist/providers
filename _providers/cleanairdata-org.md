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
    error_semantics: derived
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
  score: 4.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Pilot documentation for the existing current AQI endpoint and the read-only MCP endpoint.
  name: CleanAirData Current AQI API
  slug: cleanairdata-current-aqi-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/cleanairdata-org/rules/cleanairdata-org-rules.yml
  title: ''
  type: Spectral
  url: rules/cleanairdata-org-rules.yml
- group: design
  href: https://artifacts.apis.io/cleanairdata-org/conformance/cleanairdata-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleanairdata-org-conformance.yml
- group: design
  href: https://artifacts.apis.io/cleanairdata-org/errors/cleanairdata-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cleanairdata-org-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/cleanairdata-org/llms/cleanairdata-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleanairdata-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/cleanairdata-org/mcp/cleanairdata-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cleanairdata-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/cleanairdata-org/hosts/cleanairdata-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleanairdata-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleanairdata-org/vendors/cleanairdata-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleanairdata-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleanairdata.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleanairdata.org/privacy
- group: company
  title: ''
  type: Blog
  url: https://cleanairdata.org/blog
- group: auth
  href: https://artifacts.apis.io/cleanairdata-org/security/cleanairdata-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanairdata-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleanairdata.org/
created: '2026-11-03'
description: Clean Air Data provides independent air quality rankings for over 1,000 U.S. cities using EPA monitoring data from 2021‑2025. Users can search current AQI, view historical trends, compare cities, and access detailed PM2.5 scores and other metrics to understand local air quality conditions.
image: https://cleanairdata.org/social-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cleanairdata.org.
  name: Clean Air Data MCP Server
  slug: cleanairdata-org-mcp-yml
modified: '2026-11-03'
name: Clean Air Data
nav: Providers
network: true
overview: 'Clean Air Data publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Air Quality, Data, EPA, US Cities, and Rankings.


  The Clean Air Data catalog on APIs.io includes 1 Spectral governance ruleset.


  Clean Air Data''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Clean Air Data API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: cleanairdata-org-rules
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleanairdata Org Domain Security
  slug: cleanairdata-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cleanairdata-org
tags:
- Air Quality
- Data
- EPA
- US Cities
- Rankings
website: https://cleanairdata.org/
---
