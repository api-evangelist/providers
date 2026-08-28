---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Version 2 of the Paperless Parts REST API — 101 operations across 58 paths covering Quotes (headers, items, operations, add-ons, discounts, pricing items, files), Orders, Jobs and job operations, Part
  name: Paperless Parts API v2
  slug: paperless-parts-api-v2
- description: Version 1 of the Paperless Parts REST API — 54 operations across 33 paths covering Quotes, Quote Items, Orders, Customers (contacts, accounts, facilities, billing addresses, payment terms), Custom Tab
  name: Paperless Parts API v1
  slug: paperless-parts-api-v1
artifact_total: 8
asyncapis:
- description: ''
  name: Paperless Parts Events
  slug: paperless-parts-events
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paperless-parts-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.paperlessparts.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.paperlessparts.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paperlessparts.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paperlessparts.com/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://help.paperlessparts.com/s/article/integration-development-guide
- group: operate
  title: ''
  type: Support
  url: https://help.paperlessparts.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.paperlessparts.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/part-os
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paperlessparts.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.paperlessparts.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.paperlessparts.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.paperlessparts.com/s/article/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paperlessparts.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.paperlessparts.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.paperlessparts.com/product-updates/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paperless-parts-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/paperless-parts-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paperless-parts-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paperless-parts-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paperless-parts-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paperless-parts-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paperless-parts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paperless-parts-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paperless-parts-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paperless-parts-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paperless-parts-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paperless-parts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paperless-parts-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.paperlessparts.com/vulnerability-disclosure-policy/
- group: other
  title: ''
  type: Events
  url: asyncapi/paperless-parts-events.yml
- group: agent
  title: ''
  type: MCP
  url: mcp/paperless-parts-mcp.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/part-os/core-python
created: '2026-08-26'
description: Paperless Parts, Inc. is a Boston-based manufacturing software company founded in 2017 that builds a secure, ITAR-compliant cloud quoting and sales platform for custom part manufacturers — job shops, contract manufacturers and rapid-prototype businesses working in CNC machining, sheet metal fabrication, Swiss screw machining, wire EDM, waterjet and additive manufacturing. A patented geometry engine analyses uploaded CAD to automate costing, and the P3L pricing language lets a shop encode its own pricing logic. The company publishes a public REST API in two live versions (v1 and v2) at api.paperlessparts.com, covering quotes, quote items, orders, jobs, parts, processes, contacts and accounts, custom pricing tables, purchased components, and a managed integrations framework with a poll-based Streaming API for reacting to platform events. A first-party Python SDK is published on GitHub under the part-os organization.
image: https://paperlessparts.com/wp-content/uploads/paperless-parts-full-logo-2022.svg
layout: provider
modified: '2026-08-26'
name: Paperless Parts
nav: Providers
network: true
overview: 'Paperless Parts publishes 2 APIs on the [APIs.io](https://apis.io/) network: API v2 and API v1. Tagged areas include Company, Manufacturing, Quoting, CNC Machining, and Sheet Metal.


  The Paperless Parts catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paperless Parts'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Paperless Parts Plans Pricing
  plan_count: 0
  slug: paperless-parts-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Paperless Parts Rate Limits
  slug: paperless-parts-rate-limits
score:
  band: developing
  composite: 52.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 30.3
    contract_quality: 62.0
    developer_ergonomics: 49.4
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 28.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Paperless Parts Authentication
  slug: paperless-parts-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Paperless Parts Domain Security
  slug: paperless-parts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Paperless Parts Vulnerability Disclosure
  slug: paperless-parts-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: paperless-parts
tags:
- Company
- Manufacturing
- Quoting
- CNC Machining
- Sheet Metal
- ERP
- CRM
- Job Shops
- Aerospace and Defense
- Pricing
- Estimating
- Industrial
website: https://www.paperlessparts.com/
---
