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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/llms/arcana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcana-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/mcp/arcana-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arcana-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/well-known/arcana-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcana-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/well-known/arcana-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcana-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/hosts/arcana-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcana-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/vendors/arcana-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcana-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arcana.io/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.arcana.io/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arcana.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.arcana.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://help.arcana.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcana/refs/heads/main/security/arcana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arcana.io/
coverage:
  checked: 2026-09-25
  detail: Documentation is only available as markdown pages without a machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.arcana.io/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Arcana provides portfolio intelligence solutions for hedge funds and asset managers, offering tools for portfolio construction, performance attribution, risk management, research, and mock portfolio tracking. Their platform enables systematic performance improvement, real‑time risk analysis, and integrated research knowledge bases, targeting institutional investors seeking advanced analytics and operational efficiency.
image: https://cdn.prod.website-files.com/678a5c827d7385f94755baf7/6a909fde79d2d809300c91f6_Arcana%20%7C%20Portfolio%20Intelligence%20for%20Hedge%20Funds%20%26%20Asset%20Managers.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.arcana.io.
  name: Arcana MCP Server
  slug: arcana-mcp-yml
modified: '2026-09-25'
name: Arcana
nav: Providers
network: true
overview: 'Arcana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Portfolio Management, Hedge Funds, Asset Management, and Analytics.


  Arcana''s developer surface includes support, documentation, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arcana Domain Security
  slug: arcana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arcana
tags:
- Fintech
- Portfolio Management
- Hedge Funds
- Asset Management
- Analytics
website: https://www.arcana.io/
---
