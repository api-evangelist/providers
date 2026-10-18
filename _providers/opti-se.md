---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opti-se/refs/heads/main/security/opti-se-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/opti-se-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opti-se/refs/heads/main/well-known/opti-se-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/opti-se-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opti-se/refs/heads/main/well-known/opti-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opti-se-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/opti-se/refs/heads/main/hosts/opti-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opti-se-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.opti.se/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opti-se/refs/heads/main/security/opti-se-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opti-se-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opti-se/refs/heads/main/security/opti-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opti-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opti.se/
- group: company
  title: ''
  type: Blog
  url: https://blog.opti.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.opti.se/om-oss
- group: start
  title: ''
  type: SignUp
  url: https://opti.app/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opti.se/integritet
coverage:
  checked: '2026-10-15'
  detail: The Opti website provides no machine‑readable API specification and no developer portal was found.
  evidence:
  - status: 200
    url: https://www.opti.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Opti is a Swedish fintech company offering digital savings and investment solutions. It provides a platform for personal and corporate customers to manage portfolios, pension funds, and sustainable investments. The service emphasizes transparent fees, automated savings, and a user-friendly interface, aiming to improve financial wellbeing through technology and data-driven insights.
image: https://www.opti.se/images/static/share.png
layout: provider
modified: '2026-10-15'
name: Opti
nav: Providers
network: true
overview: 'Opti is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Savings, Investment, and Sweden.


  Opti''s developer surface includes engineering blog, documentation, signup flow, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Opti Se Domain Security
  slug: opti-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opti Se Vulnerability Disclosure
  slug: opti-se-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opti-se
tags:
- Company
- Fintech
- Savings
- Investment
- Sweden
website: https://www.opti.se/
---
