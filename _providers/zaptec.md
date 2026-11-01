---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Zaptec Agentic Access
  operation_count: 19
  slug: zaptec-agentic-access
  summary_line: 19 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The ChargeHistory API from Zaptec — 2 operation(s) for chargehistory.
  name: Zaptec Charge History API
  slug: zaptec-chargehistory-api
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The Charger API from Zaptec — 5 operation(s) for charger.
  name: Zaptec Charger API
  slug: zaptec-charger-api
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The ChargerFirmware API from Zaptec — 1 operation(s) for chargerfirmware.
  name: Zaptec Charger Firmware API
  slug: zaptec-chargerfirmware-api
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The Constants API from Zaptec — 1 operation(s) for constants.
  name: Zaptec Constants API
  slug: zaptec-constants-api
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The Installation API from Zaptec — 5 operation(s) for installation.
  name: Zaptec Installation API
  slug: zaptec-installation-api
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The Session API from Zaptec — 3 operation(s) for session.
  name: Zaptec Session API
  slug: zaptec-session-api
- baseURL: https://api.zaptec.com
  baseurl_source: declared
  description: The User Group API from Zaptec — 1 operation(s) for user group.
  name: Zaptec User Group API
  slug: zaptec-user-group-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/zaptec/agentic-access/zaptec-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zaptec-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/zaptec/rate-limits/zaptec-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zaptec-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/zaptec/rules/zaptec-rules.yml
  title: ''
  type: Spectral
  url: rules/zaptec-rules.yml
- group: design
  href: https://artifacts.apis.io/zaptec/json-ld/zaptec-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zaptec-context.jsonld
- group: design
  href: https://artifacts.apis.io/zaptec/vocabulary/zaptec-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zaptec-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zaptec/data-model/zaptec-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zaptec-data-model.yml
- group: auth
  href: https://artifacts.apis.io/zaptec/authentication/zaptec-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zaptec-authentication.yml
- group: operate
  href: https://artifacts.apis.io/zaptec/lifecycle/zaptec-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/zaptec-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/zaptec/lifecycle/zaptec-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zaptec-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/zaptec/errors/zaptec-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zaptec-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zaptec/conformance/zaptec-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zaptec-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zaptec/llms/zaptec-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zaptec-llms.txt
- group: agent
  href: https://artifacts.apis.io/zaptec/mcp/zaptec-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zaptec-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zaptec/well-known/zaptec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zaptec-well-known.yml
- group: other
  href: https://artifacts.apis.io/zaptec/hosts/zaptec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zaptec-hosts.yml
- group: other
  href: https://artifacts.apis.io/zaptec/vendors/zaptec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zaptec-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zaptec.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zaptec.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zaptec.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zaptec.com/reference/api_chargehistory_get
- group: auth
  href: https://artifacts.apis.io/zaptec/security/zaptec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zaptec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zaptec.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zaptec.com/info-hub
- group: operate
  title: ''
  type: Support
  url: https://www.zaptec.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.zaptec.com/press-room
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zaptec.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zaptec.com/policies/privacy-policy
created: '2026-10-28'
description: Zaptec provides smart electric vehicle (EV) charging solutions for homes, businesses, and public spaces. Their platform offers scalable hardware and cloud‑based management, enabling partners and installers to deliver reliable, efficient charging experiences. Zaptec’s products include the Zaptec Go home charger, Zaptec Go 2, and the enterprise‑grade Zaptec Pro, all featuring patented technology for power efficiency and user‑friendly operation. The company also offers an information hub, partner programs, and sustainability initiatives, positioning itself as a leader in the transition to clean mobility.
image: https://zaptec.objects.frb.io/assets/New-brand-imagery-2025/New-imagery-Zaptec-Go-2/_1200x630_crop_center-center_82_none/Zaptec_Go2_Home_Charging_2367.jpg?mtime=1760424885
jsonld:
- class_count: 77
  name: Zaptec Context
  property_count: 293
  slug: zaptec-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.zaptec.com.
  name: Zaptec MCP Server
  slug: zaptec-mcp-yml
modified: '2026-10-28'
name: Zaptec
nav: Providers
network: true
overview: 'Zaptec publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charge History API, Charger API, Charger Firmware API, and 4 more. Tagged areas include Company, EVCharging, SmartCharging, Energy, and Sustainability.


  The Zaptec catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zaptec''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, support, engineering blog, and 20 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 2
  name: Zaptec Rate Limits
  slug: zaptec-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Zaptec API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 3
  slug: zaptec-rules
scopes:
- name: Zaptec Scopes
  scope_count: 0
  slug: zaptec-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.8
    catalog_earned_first_party: 8.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 57.1
    discoverability: 56.7
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 34.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zaptec Authentication
  slug: zaptec-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zaptec Domain Security
  slug: zaptec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zaptec
tags:
- Company
- EVCharging
- SmartCharging
- Energy
- Sustainability
- Platform
website: https://zaptec.com/
---
