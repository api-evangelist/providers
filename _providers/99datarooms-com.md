---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/99datarooms-com/plans/99datarooms-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/99datarooms-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://99datarooms.com/trust/
- group: agent
  href: https://artifacts.apis.io/99datarooms-com/llms/99datarooms-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/99datarooms-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/99datarooms-com/mcp/99datarooms-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/99datarooms-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/99datarooms-com/well-known/99datarooms-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/99datarooms-com-security.txt
- group: agent
  href: https://artifacts.apis.io/99datarooms-com/well-known/99datarooms-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/99datarooms-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/99datarooms-com/hosts/99datarooms-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/99datarooms-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/99datarooms-com/vendors/99datarooms-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/99datarooms-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://99datarooms.com/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://99datarooms.com/status/
- group: auth
  title: ''
  type: Security
  url: https://99datarooms.com/security/
- group: auth
  href: https://artifacts.apis.io/99datarooms-com/security/99datarooms-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/99datarooms-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/99datarooms-com/security/99datarooms-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/99datarooms-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/99datarooms-com/security/99datarooms-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/99datarooms-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://99datarooms.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://99datarooms.com/mcp/
- group: commercial
  title: ''
  type: Pricing
  url: https://99datarooms.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://99datarooms.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://99datarooms.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://99datarooms.com/legal/
coverage:
  checked: '2026-10-31'
  detail: No public developer program or API documentation is provided on the site.
  evidence:
  - status: 200
    url: https://99datarooms.com/mcp/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: 99 Data Rooms (operated by 99 Developers Ltd) provides a UK‑hosted virtual data room platform that enables secure document sharing, e‑signature, and page‑by‑page viewer analytics. The service offers revocable links, a free tier for three rooms, GDPR‑ready compliance, and advanced tracking features for businesses of all sizes.
image: https://99datarooms.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.99datarooms.com.
  name: 99 Data Rooms MCP Server
  slug: 99datarooms-com-mcp-yml
modified: '2026-10-31'
name: 99 Data Rooms
nav: Providers
network: true
overview: '99 Data Rooms is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Virtual Data Room, Secure Sharing, E-Signature, UK-hosted, and GDPR.


  99 Data Rooms'' developer surface includes support, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: 99Datarooms Com Plans Pricing
  plan_count: 4
  slug: 99datarooms-com-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.3
    operational_transparency: 13.2
  previous_composite: 29.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 99Datarooms Com Domain Security
  slug: 99datarooms-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 99Datarooms Com Vulnerability Disclosure
  slug: 99datarooms-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: 99Datarooms Com Trust Center
  slug: 99datarooms-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: 99datarooms-com
tags:
- Virtual Data Room
- Secure Sharing
- E-Signature
- UK-hosted
- GDPR
website: https://99datarooms.com/
---
