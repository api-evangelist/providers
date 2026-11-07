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
    well_known_catalog: true
  schema_version: '0.2'
  score: 3.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP payroll API providing calculations for CPP, EI, QPP, QPIP and provincial taxes.
  name: Payroll API
  slug: payroll-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/canada-payroll-ca/llms/canada-payroll-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canada-payroll-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/canada-payroll-ca/mcp/canada-payroll-ca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canada-payroll-ca-mcp.yml
- group: other
  href: https://artifacts.apis.io/canada-payroll-ca/hosts/canada-payroll-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canada-payroll-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/canada-payroll-ca/vendors/canada-payroll-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canada-payroll-ca-vendors.yml
- group: auth
  href: https://artifacts.apis.io/canada-payroll-ca/security/canada-payroll-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canada-payroll-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canada-payroll.ca/
- group: docs
  title: ''
  type: APIReference
  url: https://canada-payroll.ca/payroll-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://canada-payroll.ca/payroll-api/
- group: operate
  title: ''
  type: Support
  url: https://canada-payroll.ca/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://...
- group: auth
  href: https://artifacts.apis.io/canada-payroll-ca/security/canada-payroll-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canada-payroll-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canada-payroll.ca/
- group: docs
  title: ''
  type: APIReference
  url: https://canada-payroll.ca/payroll-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://canada-payroll.ca/payroll-api/
- group: operate
  title: ''
  type: Support
  url: https://canada-payroll.ca/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canada-payroll.ca/privacy.html
created: '2026-11-04'
description: Canada Payroll Calculators provides free, browser‑based payroll deduction calculators built on CRA’s 2026 T4127 formulas and cross‑checked against PDOC. It offers tools for nanny pay, first‑employee cost, commission capitalization, and a free MCP payroll API endpoint for developers and AI agents, covering CPP, EI, QPP, QPIP and provincial income tax across all 13 provinces and territories. No signup required; all calculations run locally in the browser.
image: https://canada-payroll.ca/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at canada-payroll.ca.
  name: Canada Payroll Calculators MCP Server
  slug: canada-payroll-ca-mcp-yml
modified: '2026-11-04'
name: Canada Payroll Calculators
nav: Providers
network: true
overview: 'Canada Payroll Calculators is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll, Canada, Tax, Calculators, and Open Source.


  Canada Payroll Calculators'' developer surface includes API reference, getting-started guide, support, and 13 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canada Payroll Ca Domain Security
  slug: canada-payroll-ca-domain-security
  summary_line: TLSv1.3
slug: canada-payroll-ca
tags:
- Payroll
- Canada
- Tax
- Calculators
- Open Source
website: https://canada-payroll.ca/
---
