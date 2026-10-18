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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.getinge.com/int/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getinge/refs/heads/main/mcp/getinge-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getinge-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getinge/refs/heads/main/well-known/getinge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getinge-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getinge/refs/heads/main/well-known/getinge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getinge-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getinge/refs/heads/main/hosts/getinge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getinge-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.getinge.com/csm
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getinge/refs/heads/main/security/getinge-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getinge-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getinge/refs/heads/main/security/getinge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getinge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getinge.com/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at discovered API host.
  evidence:
  - status: NXDOMAIN
    url: https://api.getinge.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Getinge is a global medical technology company that develops, manufactures and supplies products and solutions within the areas of surgery, intensive care, infection control and sterile reprocessing. The company focuses on improving patient outcomes and enhancing the efficiency of healthcare providers through innovative devices, digital health solutions, and services. Getinge operates worldwide, serving hospitals and healthcare facilities with a broad portfolio that includes surgical tables, ventilators, patient monitoring systems, and sterilization equipment.
layout: provider
mcp_servers:
- description: Remote MCP server at support.getinge.com.
  name: Getinge MCP Server
  slug: getinge-mcp-yml
modified: '2026-10-12'
name: Getinge
nav: Providers
network: true
overview: 'Getinge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MedicalTechnology, Healthcare, Devices, and Digital Health.


  Getinge''s developer surface includes support and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.3
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getinge Domain Security
  slug: getinge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getinge Vulnerability Disclosure
  slug: getinge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: getinge
tags:
- Company
- MedicalTechnology
- Healthcare
- Devices
- Digital Health
website: https://www.getinge.com/
---
