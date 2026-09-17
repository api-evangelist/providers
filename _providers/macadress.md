---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Macadress Agentic Access
  operation_count: 4
  slug: macadress-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.macadress.com
  baseurl_source: declared
  description: 'The Healthz API from MAC Address Lookup: Find Vendor, OUI & Device Type — 1 operation(s) for healthz.'
  name: 'MAC Address Lookup: Find Vendor, OUI & Device Type Healthz API'
  slug: macadress-healthz-api
- baseURL: https://api.macadress.com
  baseurl_source: declared
  description: 'The Mac API from MAC Address Lookup: Find Vendor, OUI & Device Type — 2 operation(s) for mac.'
  name: 'MAC Address Lookup: Find Vendor, OUI & Device Type Mac API'
  slug: macadress-mac-api
- baseURL: https://api.macadress.com
  baseurl_source: declared
  description: 'The Vendors API from MAC Address Lookup: Find Vendor, OUI & Device Type — 1 operation(s) for vendors.'
  name: 'MAC Address Lookup: Find Vendor, OUI & Device Type Vendors API'
  slug: macadress-vendors-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.macadress.com/mcp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/overlays/macadress-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/macadress-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.macadress.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/security/macadress-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/macadress-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/security/macadress-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/macadress-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/authentication/macadress-authentication.yml
  title: ''
  type: Authentication
  url: authentication/macadress-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/packages/macadress-packages.yml
  title: ''
  type: Packages
  url: packages/macadress-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/well-known/macadress-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/macadress-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/well-known/macadress-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/macadress-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/mcp/macadress-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/macadress-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/conventions/macadress-conventions.yml
  title: ''
  type: Conventions
  url: conventions/macadress-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/lifecycle/macadress-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/macadress-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/lifecycle/macadress-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/macadress-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/errors/macadress-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/macadress-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/conformance/macadress-conformance.yml
  title: ''
  type: Conformance
  url: conformance/macadress-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/data-model/macadress-data-model.yml
  title: ''
  type: DataModel
  url: data-model/macadress-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/vocabulary/macadress-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/macadress-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/rate-limits/macadress-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/macadress-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/plans/macadress-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/macadress-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/agentic-access/macadress-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/macadress-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/security/macadress-vulnerability-disclosure.yml
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
- description: ''
  name: 'MAC Address Lookup: Find Vendor, OUI & Device Type MCP Server'
  slug: mac-address-lookup-find-vendor-oui-device-type-mcp-server
modified: '2026-08-28'
name: 'MAC Address Lookup: Find Vendor, OUI & Device Type'
nav: Providers
network: true
overview: 'MAC Address Lookup: Find Vendor, OUI & Device Type publishes 3 APIs on the [APIs.io](https://apis.io/) network: Healthz API, Mac API, and Vendors API. Tagged areas include Networking, Network Access Control, Security, SecOps, and IoT.


  MAC Address Lookup: Find Vendor, OUI & Device Type''s developer surface includes authentication, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Macadress Plans Pricing
  plan_count: 4
  slug: macadress-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Macadress Rate Limits
  slug: macadress-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.3
    catalog_earned_first_party: 24.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 76.3
    contract_governance: 3.8
    contract_quality: 54.2
    developer_ergonomics: 44.6
    discoverability: 75.9
    operational_transparency: 50.0
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/macadress/refs/heads/main/screenshots/macadress-2026-09-02T150341.png
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
website: https://www.macadress.com/
---
