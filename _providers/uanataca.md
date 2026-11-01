---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/uanataca/a2a/uanataca-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/uanataca-a2a.yml
- group: agent
  href: https://artifacts.apis.io/uanataca/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/uanataca/llms/uanataca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uanataca-llms.txt
- group: auth
  href: https://artifacts.apis.io/uanataca/well-known/uanataca-namirial-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uanataca-namirial-security.txt
- group: auth
  href: https://artifacts.apis.io/uanataca/well-known/uanataca-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uanataca-api-security.txt
- group: agent
  href: https://artifacts.apis.io/uanataca/well-known/uanataca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uanataca-well-known.yml
- group: other
  href: https://artifacts.apis.io/uanataca/hosts/uanataca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uanataca-hosts.yml
- group: other
  href: https://artifacts.apis.io/uanataca/vendors/uanataca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uanataca-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.namirial.com/es/blog/trust/
- group: company
  title: ''
  type: Newsroom
  url: https://www.namirial.com/es/news/
- group: company
  title: ''
  type: Blog
  url: https://www.namirial.com/es/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.namirial.com/onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://developers.uanataca.com/
- group: auth
  href: https://artifacts.apis.io/uanataca/security/uanataca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uanataca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uanataca.com/
coverage:
  checked: '2026-10-27'
  detail: The provider’s website redirects to a JavaScript‑heavy site with no machine‑readable API spec.
  evidence:
  - status: 301
    url: https://web.uanataca.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Uanataca is a digital identity and electronic signature solutions provider, operating under the Namirial group. It offers wallet services, onboarding, verification, and secure document signing for enterprises and public administrations, focusing on compliance and user-friendly integration across multiple languages.
layout: provider
modified: '2026-10-27'
name: Uanataca
nav: Providers
network: true
overview: 'Uanataca is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DigitalIdentity, ElectronicSignature, Wallet, and Enterprise.


  Uanataca''s developer surface includes engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 30.2
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Uanataca Domain Security
  slug: uanataca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uanataca
tags:
- Company
- DigitalIdentity
- ElectronicSignature
- Wallet
- Enterprise
website: https://uanataca.com/
---
