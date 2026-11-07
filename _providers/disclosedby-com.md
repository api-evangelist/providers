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
- description: disclosedby provides searchable subprocessor lists via its web interface and guides.
  name: disclosedby API
  slug: disclosedby-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/disclosedby-com/plans/disclosedby-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/disclosedby-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/disclosedby-com/mcp/disclosedby-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/disclosedby-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/disclosedby-com/hosts/disclosedby-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disclosedby-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://disclosedby.com/vendor/vanta.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disclosedby.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://disclosedby.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://disclosedby.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://disclosedby.com/guides
- group: auth
  href: https://artifacts.apis.io/disclosedby-com/security/disclosedby-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disclosedby-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disclosedby.com/
created: '2026-11-05'
description: disclosedby provides a searchable archive of subprocessor lists for over 450 companies, preserving each version with dates to enable verification of data handling changes. The service tracks entries, companies, and changes, offering a paid watch feature for continuous monitoring. Updated through November 2026, it aims to improve transparency in vendor data processing.
image: https://disclosedby.com/share/record.png?v=3f7e896e
layout: provider
mcp_servers:
- description: Remote MCP server at disclosedby.com.
  name: disclosedby MCP Server
  slug: disclosedby-com-mcp-yml
modified: '2026-11-05'
name: disclosedby
nav: Providers
network: true
overview: 'disclosedby is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Transparency, Privacy, Vendor Management, Subprocessor Lists, and Monitoring.


  disclosedby''s developer surface includes pricing, documentation, and 8 more developer resources.'
plans:
- name: Disclosedby Com Plans Pricing
  plan_count: 1
  slug: disclosedby-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Disclosedby Com Domain Security
  slug: disclosedby-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: disclosedby-com
tags:
- Data Transparency
- Privacy
- Vendor Management
- Subprocessor Lists
- Monitoring
website: https://disclosedby.com/
---
