---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Qu POS offers a developer portal for its restaurant POS platform, but API specifications are behind authentication.
  name: Qu POS API
  slug: qu-pos-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qu-pos/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qu-pos/refs/heads/main/well-known/qu-pos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qu-pos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qu-pos/refs/heads/main/hosts/qu-pos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qu-pos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qu-pos/refs/heads/main/vendors/qu-pos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qu-pos-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qubeyond.com/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qubeyond.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qubeyond.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.qubeyond.com/management
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qu-pos/refs/heads/main/security/qu-pos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qu-pos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qubeyond.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.qubeyond.com/platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stateofdigital.qubeyond.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.qubeyond.com/ordering/pos
- group: operate
  title: ''
  type: Support
  url: https://www.qubeyond.com/resource-center
coverage:
  checked: '2026-10-13'
  detail: Developer portal https://portal.qubeyond.com/ returns 401 Unauthorized for API spec endpoints
  evidence:
  - status: 401
    url: https://portal.qubeyond.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Qu POS provides a comprehensive restaurant point‑of‑sale (POS) and intelligent commerce platform. Their solutions span omnichannel ordering, kitchen orchestration, smart payment processing, and unified data reporting, enabling restaurants to streamline operations, enhance guest experiences, and leverage AI‑driven insights. The platform integrates POS, kiosk, drive‑thru, online, and third‑party ordering, as well as energy and equipment intelligence, positioning Qu POS as a versatile partner for modern food service businesses.
image: https://cdn.prod.website-files.com/695fbd17129a3b6e7df998c1/69987d839b3b8e146afd98d4_META.png
layout: provider
modified: '2026-10-13'
name: Qu POS
nav: Providers
network: true
overview: 'Qu POS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Point-of-Sale, Restaurant Technology, Unified Commerce, Kitchen Management, and Payments.


  Qu POS''s developer surface includes documentation, getting-started guide, support, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.1
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qu Pos Domain Security
  slug: qu-pos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qu-pos
tags:
- Point-of-Sale
- Restaurant Technology
- Unified Commerce
- Kitchen Management
- Payments
- Channel Management
- Data Reporting
website: https://www.qubeyond.com
---
