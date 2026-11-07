---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP endpoint providing tool list for AZAV Doku.
  name: AZAV Doku MCP
  slug: azav-doku-mcp
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/azav-doku-de/plans/azav-doku-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azav-doku-de-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/azav-doku-de/llms/azav-doku-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azav-doku-de-llms.txt
- group: agent
  href: https://artifacts.apis.io/azav-doku-de/mcp/azav-doku-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/azav-doku-de-mcp.yml
- group: other
  href: https://artifacts.apis.io/azav-doku-de/hosts/azav-doku-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azav-doku-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/azav-doku-de/vendors/azav-doku-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azav-doku-de-vendors.yml
- group: auth
  href: https://artifacts.apis.io/azav-doku-de/security/azav-doku-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azav-doku-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://azav-doku.de/
- group: commercial
  title: ''
  type: Pricing
  url: https://azav-doku.de/preise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azav-doku.de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azav-doku.de/datenschutz
- group: operate
  title: ''
  type: Support
  url: https://azav-doku.de/impressum
- group: docs
  title: ''
  type: APIReference
  url: https://azav-doku.de/mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://azav-doku.de/llms.txt
created: '2026-11-02'
description: AZAV-Doku provides free web-based tools for AVGS documentation for AZAV-certified providers and coaches in Germany. It offers digital signatures for session records, deadline calculators, official BA forms (participation report, absence notifications), billing, and data export. The platform runs on Google Cloud in Frankfurt, stores data securely, and complies with German regulations. All features are available without subscription.
image: https://azav-doku.de/og.png
json_schemas:
- name: Azav Doku De Mcp
  property_count: 0
  slug: azav-doku-de-mcp
layout: provider
mcp_servers:
- description: Remote MCP server at azav-doku.de; 4 tools listed.
  name: AZAV-Doku MCP Server
  slug: azav-doku-de-mcp-yml
modified: '2026-11-02'
name: AZAV-Doku
nav: Providers
network: true
overview: 'AZAV-Doku is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AVGS, Documentation, Digital Signature, Free, and German.


  AZAV-Doku''s developer surface includes pricing, support, API reference, documentation, and 9 more developer resources.'
plans:
- name: Azav Doku De Plans Pricing
  plan_count: 1
  slug: azav-doku-de-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Azav Doku De Rate Limits
  slug: azav-doku-de-rate-limits
scopes:
- name: Azav Doku De Scopes
  scope_count: 0
  slug: azav-doku-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Azav Doku De Authentication
  slug: azav-doku-de-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Azav Doku De Domain Security
  slug: azav-doku-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azav-doku-de
tags:
- AVGS
- Documentation
- Digital Signature
- Free
- German
- Healthcare
website: https://azav-doku.de/
---
