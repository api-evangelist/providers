---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SmartAdvocate API (no public machine‑readable specification found).
  name: SmartAdvocate API
  slug: smartadvocate-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/smartadvocate/mcp/smartadvocate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smartadvocate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/smartadvocate/well-known/smartadvocate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smartadvocate-well-known.yml
- group: other
  href: https://artifacts.apis.io/smartadvocate/hosts/smartadvocate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smartadvocate-hosts.yml
- group: other
  href: https://artifacts.apis.io/smartadvocate/vendors/smartadvocate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smartadvocate-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartadvocate.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartadvocate.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.smartadvocate.com/
- group: auth
  href: https://artifacts.apis.io/smartadvocate/security/smartadvocate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartadvocate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smartadvocate.com/
- group: operate
  title: ''
  type: Support
  url: https://www.smartadvocate.com/support
coverage:
  checked: '2026-10-29'
  detail: Developer portal https://dev.smartadvocate.com/ returns a generic placeholder page with no API documentation or machine‑readable spec.
  evidence:
  - status: 200
    url: https://dev.smartadvocate.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SmartAdvocate provides award‑winning legal case management software serving over 20,000 legal professionals nationwide, including solo practitioners and large litigation firms. The cloud‑based and on‑premise platform offers automated client intake, workflow automation, document management with merge codes, batch scanning, integrated calendaring, deadline tracking, customizable dashboards, reporting, billing, invoicing, a client portal, mobile apps, and AI‑powered SmartIntelligence tools for summarization, translation, and transcription.
image: https://cdn.prod.website-files.com/65a3f5312672e379fd7c7e4d/65d408d3d8b67f4dedd8d23c_SmartAdvocate-2024%20%284%29.webp
layout: provider
mcp_servers:
- description: Remote MCP server at dev.smartadvocate.com.
  name: SmartAdvocate MCP Server
  slug: smartadvocate-mcp-yml
modified: '2026-10-28'
name: SmartAdvocate
nav: Providers
network: true
overview: 'SmartAdvocate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LegalTech, CaseManagement, Software, Litigation, and Cloud.


  SmartAdvocate''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Smartadvocate Rate Limits
  slug: smartadvocate-rate-limits
scopes:
- name: Smartadvocate Scopes
  scope_count: 0
  slug: smartadvocate-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Smartadvocate Authentication
  slug: smartadvocate-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Smartadvocate Domain Security
  slug: smartadvocate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartadvocate
tags:
- LegalTech
- CaseManagement
- Software
- Litigation
- Cloud
website: https://smartadvocate.com/
---
