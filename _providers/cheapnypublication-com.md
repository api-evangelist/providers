---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
- description: API for New York LLC publication services
  name: Cheap NY Publication API
  slug: cheap-ny-publication-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cheapnypublication-com/plans/cheapnypublication-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cheapnypublication-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cheapnypublication-com/conformance/cheapnypublication-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cheapnypublication-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cheapnypublication-com/llms/cheapnypublication-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cheapnypublication-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cheapnypublication-com/mcp/cheapnypublication-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cheapnypublication-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/cheapnypublication-com/hosts/cheapnypublication-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cheapnypublication-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cheapnypublication-com/vendors/cheapnypublication-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cheapnypublication-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheapnypublication.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheapnypublication.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cheapnypublication.com/pricing
- group: other
  title: ''
  type: Leadership
  url: https://cheapnypublication.com/team
- group: docs
  title: ''
  type: APIReference
  url: https://cheapnypublication.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/cheapnypublication-com/security/cheapnypublication-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cheapnypublication-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cheapnypublication.com/
created: '2026-11-04'
description: Cheap NY Publication provides a full-service New York LLC publication solution, handling newspaper filings, affidavits, and state certificate filing for a flat fee of $349 (including the $50 state fee). The service covers all counties, ensuring compliance with NY §206 publication requirements, and offers support via phone and email.
image: https://cheapnypublication.com/opengraph-image?9ca1941a7d354baf
layout: provider
mcp_servers:
- description: Remote MCP server at cheapnypublication.com.
  name: Cheap NY Publication MCP Server
  slug: cheapnypublication-com-mcp-yml
modified: '2026-11-04'
name: Cheap NY Publication
nav: Providers
network: true
overview: 'Cheap NY Publication is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LLC Publication, Business Formation, State Filing, New York, and Publication Service.


  Cheap NY Publication''s developer surface includes pricing, API reference, and 11 more developer resources.'
plans:
- name: Cheapnypublication Com Plans Pricing
  plan_count: 12
  slug: cheapnypublication-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.8
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
  name: Cheapnypublication Com Domain Security
  slug: cheapnypublication-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cheapnypublication-com
tags:
- LLC Publication
- Business Formation
- State Filing
- New York
- Publication Service
website: https://cheapnypublication.com/
---
