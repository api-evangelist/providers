---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Macadress Agentic Access
  operation_count: 4
  slug: macadress-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: 'REST/JSON API for single and batch MAC/OUI lookups, vendor directory search, and health checks. Requires a free API key via Authorization Bearer or api_key query/body. Live API at api.macadress.com: G'
  name: macadress.com API
  slug: macadresscom-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/macadress-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macadress-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/macadress-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/macadress-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/macadress-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/macadress-security.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/macadress-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/macadress-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/macadress-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/macadress-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/macadress-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/macadress-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/macadress-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/macadress-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/macadress-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/macadress-plans-pricing.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/macadress-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: security/macadress-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://macadress.com/mac-address-api
- group: operate
  title: ''
  type: Support
  url: https://macadress.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://macadress.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://macadress.com/signup
- group: start
  title: ''
  type: Login
  url: https://macadress.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://macadress.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://macadress.com/privacy
created: '2026-08-28'
description: REST/JSON API, hosted MCP server, and reference data for MAC address / OUI lookup — resolving vendor, IEEE registration block, device category, and randomization confidence. Data synced twice daily from IEEE MA-L/MA-M/MA-S/IAB/CID registries. Operated by ApisOS FZE (macadress.com).
examples:
- key_count: 5
  name: Macadress Batch Lookup Example
  slug: macadress-batch-lookup-example
- key_count: 4
  name: Macadress Healthz Example
  slug: macadress-healthz-example
- key_count: 5
  name: Macadress Lookup Mac Example
  slug: macadress-lookup-mac-example
- key_count: 4
  name: Macadress Search Vendors Example
  slug: macadress-search-vendors-example
- key_count: 4
  name: Macadress Unauthorized Example
  slug: macadress-unauthorized-example
image: https://macadress.com/static/og-image.png
layout: provider
mcp_servers:
- description: The endpoint is on the mcp. SUBDOMAIN. macadress.com/mcp is the documentation page and answers 405 to POST -- probing it as the endpoint reads as absence. Streamable HTTP, stateless; returns 401 "no b
  name: 'MAC Address Lookup: Find Vendor, OUI & Device Type MCP Server'
  slug: mac-address-lookup-find-vendor-oui-device-type-mcp-server
modified: '2026-08-28'
name: 'MAC Address Lookup: Find Vendor, OUI & Device Type'
nav: Providers
network: true
overview: 'MAC Address Lookup: Find Vendor, OUI & Device Type publishes 1 API on the [APIs.io](https://apis.io/) network: macadress.com API. Tagged areas include Networking, Network Access Control, Security, SecOps, and IoT.


  MAC Address Lookup: Find Vendor, OUI & Device Type''s developer surface includes authentication, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Macadress Plans Pricing
  plan_count: 4
  slug: macadress-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Macadress Rate Limits
  slug: macadress-rate-limits
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 49.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 15.2
    contract_quality: 50.3
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 15.2
    operational_transparency: 50.0
  previous_composite: 53.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Macadress Authentication
  slug: macadress-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Macadress Domain Security
  slug: macadress-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Macadress Vulnerability Disclosure
  slug: macadress-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: macadress
tags:
- Networking
- Network Access Control
- Security
- SecOps
- IoT
- Device Fleet Management
- MDM
- Reference Data
- IEEE OUI Lookup
- Developer Tools
- MCP
- agent-native
website: https://macadress.com/mac-address-api
---
