---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wearabledocs Com Agentic Access
  operation_count: 8
  slug: wearabledocs-com-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Read-only public data API for state requirements and page index. Provides JSON access to medical directive information.
  name: WearableDocs API
  slug: wearabledocs-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/wearabledocs-com/agentic-access/wearabledocs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wearabledocs-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/wearabledocs-com/plans/wearabledocs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wearabledocs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wearabledocs-com/rules/wearabledocs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/wearabledocs-com-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://wearabledocs.com/security
- group: design
  href: https://artifacts.apis.io/wearabledocs-com/errors/wearabledocs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wearabledocs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wearabledocs-com/conformance/wearabledocs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wearabledocs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wearabledocs-com/llms/wearabledocs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wearabledocs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/wearabledocs-com/a2a/wearabledocs-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/wearabledocs-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/wearabledocs-com/mcp/wearabledocs-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wearabledocs-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/wearabledocs-com/mcp/wearabledocs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wearabledocs-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/wearabledocs-com/well-known/wearabledocs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wearabledocs-com-security.txt
- group: agent
  href: https://artifacts.apis.io/wearabledocs-com/well-known/wearabledocs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wearabledocs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wearabledocs-com/hosts/wearabledocs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wearabledocs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wearabledocs-com/vendors/wearabledocs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wearabledocs-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wearabledocs.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://wearabledocs.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wearabledocs.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.wearabledocs.com/signin
- group: auth
  href: https://artifacts.apis.io/wearabledocs-com/security/wearabledocs-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wearabledocs-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/wearabledocs-com/security/wearabledocs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wearabledocs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wearabledocs-com/security/wearabledocs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wearabledocs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wearabledocs.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://wearabledocs.com/how
- group: commercial
  title: ''
  type: Pricing
  url: https://wearabledocs.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://wearabledocs.com/help
- group: docs
  title: ''
  type: Documentation
  url: https://wearabledocs.com/about
created: '2026-10-31'
description: WearableDocs provides a digital platform for emergency medical directives and health refusals, allowing individuals to store and share signed documents that emergency responders can access instantly via QR codes. The service offers secure storage, encryption, and real-time alerts, targeting patients, families, and healthcare providers who need reliable, portable medical consent documentation.
image: https://wearabledocs.com/images/card-front.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at wearabledocs.com.
  name: wearabledocs-com MCP Server
  slug: wearabledocs-com-mcp-yml
modified: '2026-10-31'
name: wearabledocs-com
nav: Providers
network: true
overview: 'wearabledocs-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health Tech, Digital Health, Emergency Care, Document Management, and Wearables.


  The wearabledocs-com catalog on APIs.io includes 1 Spectral governance ruleset.


  wearabledocs-com''s developer surface includes getting-started guide, pricing, support, documentation, and 22 more developer resources.'
plans:
- name: Wearabledocs Com Plans Pricing
  plan_count: 2
  slug: wearabledocs-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: wearabledocs-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: wearabledocs-com-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wearabledocs Com Domain Security
  slug: wearabledocs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wearabledocs Com Vulnerability Disclosure
  slug: wearabledocs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Wearabledocs Com Trust Center
  slug: wearabledocs-com-trust-center
  summary_line: SOC 2, PCI DSS
slug: wearabledocs-com
tags:
- Health Tech
- Digital Health
- Emergency Care
- Document Management
- Wearables
website: https://wearabledocs.com/
---
