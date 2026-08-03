---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ensurance-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ensurance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ensurance-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ensurance-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ensurance-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ensurance.com.au/
- group: company
  title: ''
  type: Website
  url: https://www.chaseunderwriting.com.au/capabilities/professional-risks/
- group: company
  title: ''
  type: Website
  url: https://3rdp.ensurance.com.au/
created: '2026-07-25'
description: 'Ensurance Limited (ASX:ENA) was an Australian ASX-listed insurance underwriting agency headquartered in Perth, Western Australia, marketing itself as "innovating the online insurance sector." Its Australian arm, Ensurance Underwriting Australia, operated as a wholesale underwriting agency under an Australian Financial Services Licence, assembling a consortium of local and international capacity — including Lloyd''s, Swiss Re and XL Catlin — behind construction-specific products sold exclusively through intermediaries: Licensed Builder Annual Construction, Plant and Liability, Project-Specific Construction, Trades Liability, Owner Builder, and Home and Contents insurance, distributed to a broker network the company described as 340-plus intermediaries. A sister company, Ensurance UK Limited, ran as a Managing General Agent authorised and regulated by the UK Financial Conduct Authority and a coverholder at Lloyd''s. The group''s API posture is nil and always was. Ensurance never
  published a public developer portal, API reference, OpenAPI or Swagger definition, Postman collection, GraphQL endpoint, webhook or event catalogue. What the company called its "customised online platform" for intermediaries was BOB (bob.ensurance.com.au), a form-based, session-login ASP.NET MVC quote-and-proposal wizard keyed to per-agent codes — an agent login wall, not a programmable interface. No ACORD, AL3, ACORD XML or NGDS reference appears anywhere in the company''s live or archived web estate. As of this review the ensurance.com.au TLS certificate has expired and every path on the domain, along with the ensurance.ltd domain family, blanket 301-redirects to Chase Underwriting Solutions Pty Ltd, an Australian professional-lines underwriting agency that likewise publishes no API. Ensurance is recorded here as a partner-gated, no-public-API insurance provider in the Australian market — a faithful data point for a sector where the Consumer Data Right was designated for general insurance
  and then deferred, leaving carriers and underwriting agencies with no forcing function to expose anything.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Ensurance
nav: Providers
network: true
overview: Ensurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Underwriting, Property and Casualty, and Construction Insurance.
random_paper: 14
score:
  band: minimal
  composite: 8.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 8.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ensurance/refs/heads/main/screenshots/ensurance-2026-07-25T213422.png
security:
- kind: domain-security
  name: Ensurance Domain Security
  slug: ensurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ensurance
tags:
- Insurance
- Australia
- Underwriting
- Property and Casualty
- Construction Insurance
- Managing General Agent
- Broker
- Wholesale Insurance
- Insurtech
- Partner Gated
- No Public API
website: https://ensurance.com.au/
---
