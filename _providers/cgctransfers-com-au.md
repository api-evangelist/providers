---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cgctransfers Com Au Agentic Access
  operation_count: 2
  slug: cgctransfers-com-au-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Public read endpoints for quotes and routes.
  name: CGC Airport Transfers Public API
  slug: cgc-airport-transfers-public-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/cgctransfers-com-au/agentic-access/cgctransfers-com-au-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cgctransfers-com-au-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cgctransfers-com-au/rules/cgctransfers-com-au-rules.yml
  title: ''
  type: Spectral
  url: rules/cgctransfers-com-au-rules.yml
- group: auth
  href: https://artifacts.apis.io/cgctransfers-com-au/security/cgctransfers-com-au-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cgctransfers-com-au-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/cgctransfers-com-au/conformance/cgctransfers-com-au-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cgctransfers-com-au-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cgctransfers-com-au/llms/cgctransfers-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cgctransfers-com-au-llms.txt
- group: other
  href: https://artifacts.apis.io/cgctransfers-com-au/a2a/cgctransfers-com-au-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cgctransfers-com-au-a2a.yml
- group: auth
  href: https://artifacts.apis.io/cgctransfers-com-au/well-known/cgctransfers-com-au-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cgctransfers-com-au-security.txt
- group: agent
  href: https://artifacts.apis.io/cgctransfers-com-au/well-known/cgctransfers-com-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cgctransfers-com-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/cgctransfers-com-au/hosts/cgctransfers-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cgctransfers-com-au-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cgctransfers-com-au/security/cgctransfers-com-au-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cgctransfers-com-au-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cgctransfers-com-au/security/cgctransfers-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cgctransfers-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cgctransfers.com.au/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cgctransfers.com.au/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cgctransfers.com.au/bookingtermsandconditions/
created: '2026-11-03'
description: CGC Airport Transfers provides private, pre‑booked airport transfer services on the Gold Coast and Brisbane. Customers can book fixed‑price rides from $55 for sedans or $85 for Kia Carnivals, with GST and tolls included. The service covers Gold Coast Airport (OOL), Brisbane Airport (BNE), Byron Bay and Northern NSW, offering door‑to‑door transport, in‑terminal meet‑and‑greet, 24/7 reservations via SMS or WhatsApp, and child‑seat options. Operating since 2020, the company holds a Queensland Booked Hire Service Licence and complies with Australian tax regulations, retaining records for five years.
image: https://cgctransfers.com.au/wp-content/uploads/2026/10/cgc-kia-carnival-black-1024x512.webp
layout: provider
modified: '2026-11-03'
name: CGC Airport Transfers
nav: Providers
network: true
overview: 'CGC Airport Transfers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Airport Transfers, PrivateTransport, Australia, GoldCoast, and Brisbane.


  The CGC Airport Transfers catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: CGC Airport Transfers API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: cgctransfers-com-au-rules
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cgctransfers Com Au Domain Security
  slug: cgctransfers-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cgctransfers Com Au Vulnerability Disclosure
  slug: cgctransfers-com-au-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cgctransfers-com-au
tags:
- Airport Transfers
- PrivateTransport
- Australia
- GoldCoast
- Brisbane
website: https://cgctransfers.com.au/
---
