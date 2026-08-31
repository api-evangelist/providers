---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: N3Rgy Agentic Access
  operation_count: 26
  slug: n3rgy-agentic-access
  summary_line: 26 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Create Export Profiles API from n3rgy — 1 operation(s) for create export profiles.
  name: n3rgy Create Export Profiles API
  slug: n3rgy-create-export-profiles-api
- description: The Customer Service API V2 API from n3rgy — 1 operation(s) for customer service api v2.
  name: n3rgy Customer Service API V2 API
  slug: n3rgy-customer-service-api-v2-api
- description: The Find Mpxn API from n3rgy — 2 operation(s) for find mpxn.
  name: n3rgy Find Mpxn API
  slug: n3rgy-find-mpxn-api
- description: The Get Update Frequencies API from n3rgy — 1 operation(s) for get update frequencies.
  name: n3rgy Get Update Frequencies API
  slug: n3rgy-get-update-frequencies-api
- description: The Internal API from n3rgy — 1 operation(s) for internal.
  name: n3rgy Internal API
  slug: n3rgy-internal-api
- description: The Mpxn API from n3rgy — 3 operation(s) for mpxn.
  name: n3rgy Mpxn API
  slug: n3rgy-mpxn-api
- description: The Push API from n3rgy — 2 operation(s) for push.
  name: n3rgy Push API
  slug: n3rgy-push-api
- description: The Read Inventory API from n3rgy — 1 operation(s) for read inventory.
  name: n3rgy Read Inventory API
  slug: n3rgy-read-inventory-api
- description: The Reset All Update Frequencies API from n3rgy — 1 operation(s) for reset all update frequencies.
  name: n3rgy Reset All Update Frequencies API
  slug: n3rgy-reset-all-update-frequencies-api
- description: The Set Defaults API from n3rgy — 1 operation(s) for set defaults.
  name: n3rgy Set Defaults API
  slug: n3rgy-set-defaults-api
- description: The Set Meter Update Frequency API from n3rgy — 1 operation(s) for set meter update frequency.
  name: n3rgy Set Meter Update Frequency API
  slug: n3rgy-set-meter-update-frequency-api
- description: The Update Now API from n3rgy — 1 operation(s) for update now.
  name: n3rgy Update Now API
  slug: n3rgy-update-now-api
- description: The Upload API from n3rgy — 4 operation(s) for upload.
  name: n3rgy Upload API
  slug: n3rgy-upload-api
artifact_total: 26
asyncapis:
- description: ''
  name: N3Rgy Push Notifications Webhooks
  slug: n3rgy-push-notifications-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/n3rgy-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/n3rgy-customer-service-api-v2-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/n3rgy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/n3rgy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n3rgy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/n3rgy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.n3rgy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://customer-api-user-manuals.data.n3rgy.com/
- group: start
  title: ''
  type: SignUp
  url: https://data.n3rgy.com/business-sign-up
- group: start
  title: ''
  type: Login
  url: https://www.n3rgy.com/business-login/
- group: start
  title: ''
  type: Portal
  url: https://data.n3rgy.com/consumer-login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.n3rgy.com/business/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.n3rgy.com/wp-content/uploads/2023/04/N3rgyDataLimited.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.n3rgy.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.n3rgy.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://www.n3rgy.com/about-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n3rgy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://customer-api-user-manuals.data.n3rgy.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.n3rgy.com/support/home
- group: build
  title: ''
  type: Packages
  url: packages/n3rgy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/n3rgy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/n3rgy-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/n3rgy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/n3rgy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/n3rgy-changelog.yml
created: '2026-07-27'
description: 'n3rgy data limited is a United Kingdom smart-energy data platform, registered in England (No. 11712674) and owned by Smart Metering Systems Ltd. It sits between Great Britain''s mandated smart-metering infrastructure — the DCC network, SMETS2 home area networks (HANs), and the ESME/GSME electricity and gas meters behind them — and the organisations that want to read from it, letting a business collect consumption, production, and tariff data for a property (addressed by MPAN/MPRN, collectively MPxN) once the occupant has granted consent, without that business having to become a DCC user in its own right. Its API posture is public in documentation and closed in access: a genuinely anonymous MkDocs developer guide and a complete OpenAPI 3.0.1 contract for the Customer Service API V2 are served to anyone, while every operation is x-api-key gated and live keys must be enabled by the n3rgy back office after a business sign-up. Britain mandated the metering infrastructure, not a
  consumer data right, so nothing here is a Consumer Data Right or Green Button implementation — n3rgy publishes no open grid or market data at all, and the formerly public consumer API is, by the company''s own statement, no longer available.'
examples:
- key_count: 1
  name: N3Rgy Error Bad Request Example
  slug: n3rgy-error-bad-request-example
- key_count: 1
  name: N3Rgy Error Forbidden Example
  slug: n3rgy-error-forbidden-example
- key_count: 3
  name: N3Rgy Push Configuration Request Example
  slug: n3rgy-push-configuration-request-example
- key_count: 2
  name: N3Rgy Push Configuration Response Example
  slug: n3rgy-push-configuration-response-example
- key_count: 3
  name: N3Rgy Push Status Response Example
  slug: n3rgy-push-status-response-example
- key_count: 6
  name: N3Rgy Retrieve Consented Mpxns Empty Example
  slug: n3rgy-retrieve-consented-mpxns-empty-example
- key_count: 6
  name: N3Rgy Retrieve Consented Mpxns Example
  slug: n3rgy-retrieve-consented-mpxns-example
image: https://www.n3rgy.com/wp-content/uploads/2023/03/Group.png
layout: provider
mcp_servers:
- description: n3rgy operates no MCP server. This is a CANDIDATE tool surface derived mechanically from the 26 operations of the Customer Service API V2 so an agent builder can stand one up without guessing. Every t
  name: n3rgy MCP Server
  slug: n3rgy-mcp-server
modified: '2026-07-27'
name: n3rgy
nav: Providers
network: true
overview: 'n3rgy publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Create Export Profiles API, Customer Service API V2 API, Find Mpxn API, and 10 more. Tagged areas include Energy, United Kingdom, Utilities, Smart Metering, and Electricity.


  The n3rgy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  n3rgy''s developer surface includes authentication, documentation, signup flow, developer portal, pricing, support, changelog, and 19 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 4
  name: N3Rgy Rate Limits
  slug: n3rgy-rate-limits
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 65.7
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 60.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/n3rgy/refs/heads/main/screenshots/n3rgy-2026-08-07T184554.png
security:
- kind: authentication
  name: N3Rgy Authentication
  slug: n3rgy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: N3Rgy Domain Security
  slug: n3rgy-domain-security
  summary_line: TLSv1.3 · HSTS
slug: n3rgy
tags:
- Energy
- United Kingdom
- Utilities
- Smart Metering
- Electricity
- Gas
- Smart Meter Data
- Consent
- Metering
- Energy Data
website: https://www.n3rgy.com/
---
