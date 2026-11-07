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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/aptedge/well-known/aptedge-aptedge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aptedge-aptedge-security.txt
- group: agent
  href: https://artifacts.apis.io/aptedge/well-known/aptedge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aptedge-well-known.yml
- group: other
  href: https://artifacts.apis.io/aptedge/hosts/aptedge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aptedge-hosts.yml
- group: other
  href: https://artifacts.apis.io/aptedge/vendors/aptedge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aptedge-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.aptedge.io/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://aptedge.statuspage.io/
- group: auth
  href: https://artifacts.apis.io/aptedge/security/aptedge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aptedge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aptedge.io/
created: '2026-10-29'
description: AptEdge provides AI-powered autonomous support agents for B2B technical support, enabling enterprises to resolve tickets, bridge knowledge gaps, and assist engineers across CRM and knowledge bases. Their platform includes products like Autonomous Support Response, Knowledge Gap Analysis, Engineer Assist, Customer Self Service, and an MCP Server for custom AI workflows, targeting support leaders, engineers, and CX teams.
image: https://aptedge.io/images/og-default.png
layout: provider
modified: '2026-10-29'
name: AptEdge
nav: Providers
network: true
overview: 'AptEdge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, B2B, Support, Automation, and Knowledge Management.


  AptEdge''s developer surface includes support and 7 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aptedge/aptedge-2026-11-03T121052.png
security:
- kind: domain-security
  name: Aptedge Domain Security
  slug: aptedge-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aptedge
tags:
- Artificial Intelligence
- B2B
- Support
- Automation
- Knowledge Management
website: https://aptedge.io/
---
