---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'The production JSON API behind the Sdui school-communication platform, serving the Sdui web app, the iOS/Android clients and the WebUntis messenger integration. Every resource path probed (/v1/users, '
  name: Sdui Platform API
  slug: sdui-platform-api
- description: 'A Model Context Protocol server exposed by the sdui.de WordPress site through the `mcp` REST namespace and advertised at /.well-known/oauth-protected-resource. The endpoint answers JSON-RPC over HTTP '
  name: Sdui Website MCP Server
  slug: sdui-website-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://sdui.de/?lang=en
- group: operate
  title: ''
  type: Support
  url: https://support.sdui.de/
- group: company
  title: ''
  type: Blog
  url: https://sdui.de/blog/?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sdui.de/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sdui.de/privacy-policy/?lang=en
- group: start
  title: ''
  type: SignUp
  url: https://sdui.app/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sdui.de/
- group: auth
  title: ''
  type: Security
  url: https://support.sdui.de/en_US/96472-allgemeine-fragen/security-concern-what-to-do
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sdui-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sdui-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sdui-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sdui-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sdui-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sdui-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/sdui-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sdui-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sdui-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sdui-rate-limits.yml
created: '2026-08-26'
description: Sdui is a Koblenz, Germany based education-technology company (Sdui GmbH, part of the Sdui Group / Seven Education) that builds GDPR-compliant digital communication, organisation and administration software for schools, preschools and school authorities across Germany, Switzerland, France and Spain. The platform spans three suites — Communication and Organisation (the Sdui messenger app, chat, video conferencing, calendar and announcements), Planning and Administration (timetabling, resource planning, an AI timetable planner and document management), and Learning and Grade Management (digital gradebook and lesson planning) — and the group also operates the Pupil, Additio, Konecto, Fox Education and OSS Messenger brands. Sdui runs a production JSON API at https://api.sdui.app/v1 that powers its own web and mobile clients and its WebUntis messenger integration, but it publishes no public developer portal, API reference or machine-readable specification; integration access is arranged
  through the partner and sales channel.
image: https://sdui.de/wp-content/uploads/2024/02/Sdui-Gruppe-Logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Sdui Website MCP Server
  slug: sdui-website-mcp-server
modified: '2026-08-26'
name: Sdui
nav: Providers
network: true
overview: 'Sdui publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Schools, and Communications.


  Sdui''s developer surface includes support, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Sdui Plans Pricing
  plan_count: 0
  slug: sdui-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Sdui Rate Limits
  slug: sdui-rate-limits
scopes:
- name: Sdui Scopes
  scope_count: 0
  slug: sdui-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 27.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sdui Authentication
  slug: sdui-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sdui Domain Security
  slug: sdui-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sdui Vulnerability Disclosure
  slug: sdui-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sdui
tags:
- Company
- Education
- EdTech
- Schools
- Communications
- Messaging
- Timetabling
- Grade Management
- Germany
- GDPR
website: https://sdui.de/?lang=en
---
