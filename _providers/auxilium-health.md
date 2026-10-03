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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auxilium-health/refs/heads/main/llms/auxilium-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auxilium-health-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auxilium-health/refs/heads/main/mcp/auxilium-health-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/auxilium-health-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auxilium-health/refs/heads/main/hosts/auxilium-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auxilium-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auxilium-health/refs/heads/main/vendors/auxilium-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auxilium-health-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auxilium-health/refs/heads/main/security/auxilium-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auxilium-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auxiliumhealth.ca
- group: docs
  title: ''
  type: Documentation
  url: https://www.auxiliumhealth.ca/about
- group: operate
  title: ''
  type: Support
  url: https://www.auxiliumhealth.ca/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auxiliumhealth.ca/privacy-policy
coverage:
  checked: '2026-09-26'
  detail: Docs are rendered via Wix platform, preventing machine‑readable extraction of an API contract.
  evidence:
  - status: 200
    url: https://www.auxiliumhealth.ca/about
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Auxilium Health provides a comprehensive suite of patient support programs and services to streamline access to medical treatments for physicians and patients. Based in Toronto, Canada, the company offers dedicated portal programs, product provision, data insight, and optiCare services, ensuring high-quality, safe, and efficient patient care across the healthcare ecosystem.
image: https://static.wixstatic.com/media/410637_0a2011e0519745a2a2d88844ef9b6dd2%7Emv2.png/v1/fit/w_2500,h_1330,al_c/410637_0a2011e0519745a2a2d88844ef9b6dd2%7Emv2.png
layout: provider
mcp_servers:
- description: ''
  name: Auxilium Health MCP Server
  slug: auxilium-health-mcp-server
modified: '2026-09-26'
name: Auxilium Health
nav: Providers
network: true
overview: 'Auxilium Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Patient Support, Toronto, Canada, and Services.


  Auxilium Health''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auxilium Health Domain Security
  slug: auxilium-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auxilium-health
tags:
- Healthcare
- Patient Support
- Toronto
- Canada
- Services
website: https://www.auxiliumhealth.ca
---
