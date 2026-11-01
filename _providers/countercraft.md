---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.countercraftsec.com/security-policy/
- group: auth
  href: https://artifacts.apis.io/countercraft/well-known/countercraft-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/countercraft-security.txt
- group: agent
  href: https://artifacts.apis.io/countercraft/well-known/countercraft-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/countercraft-well-known.yml
- group: other
  href: https://artifacts.apis.io/countercraft/hosts/countercraft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/countercraft-hosts.yml
- group: other
  href: https://artifacts.apis.io/countercraft/vendors/countercraft-vendors.yml
  title: ''
  type: Vendors
  url: vendors/countercraft-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.countercraftsec.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://www.countercraftsec.com/register-a-deal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.countercraftsec.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.countercraftsec.com/news/a-note-from-our-executive-team/
- group: other
  title: ''
  type: Leadership
  url: https://www.countercraftsec.com/team/matt-gunston/
- group: company
  title: ''
  type: Blog
  url: https://www.countercraftsec.com/blog/
- group: auth
  href: https://artifacts.apis.io/countercraft/security/countercraft-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/countercraft-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/countercraft/security/countercraft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/countercraft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.countercraftsec.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.countercraftsec.com/mcp
  - status: 200
    url: https://www.countercraftsec.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: CounterCraft provides AI‑powered deception platforms that create high‑fidelity digital twins of enterprise environments. By deploying autonomous deception agents, it captures real attacker behavior, delivering actionable threat intelligence and real‑time engagement to neutralize threats before they impact production systems.
image: https://www.countercraftsec.com/resources/External-attack-e1722418253385.jpg
layout: provider
modified: '2026-10-25'
name: CounterCraft
nav: Providers
network: true
overview: 'CounterCraft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Deception, AI, Threat Intelligence, and Enterprise.


  CounterCraft''s developer surface includes signup flow, engineering blog, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Countercraft Domain Security
  slug: countercraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Countercraft Vulnerability Disclosure
  slug: countercraft-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: countercraft
tags:
- Cybersecurity
- Deception
- AI
- Threat Intelligence
- Enterprise
website: https://www.countercraftsec.com
---
