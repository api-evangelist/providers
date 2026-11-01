---
agent_readiness:
  band: agent-aware
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
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.gmx.net
- group: auth
  href: https://artifacts.apis.io/gmx-net/well-known/gmx-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gmx-net-security.txt
- group: auth
  href: https://artifacts.apis.io/gmx-net/well-known/gmx-net-gmx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gmx-net-gmx-security.txt
- group: auth
  href: https://artifacts.apis.io/gmx-net/well-known/gmx-net-connect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gmx-net-connect-security.txt
- group: agent
  href: https://artifacts.apis.io/gmx-net/well-known/gmx-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gmx-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/gmx-net/hosts/gmx-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gmx-net-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.gmx.net/magazine/news/
- group: start
  title: ''
  type: Login
  url: https://hilfe.gmx.net/account/login/index.html
- group: auth
  href: https://artifacts.apis.io/gmx-net/security/gmx-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gmx-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gmx-net/security/gmx-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gmx-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gmx.net/
- group: docs
  title: ''
  type: Documentation
  url: https://hilfe.gmx.net/
- group: operate
  title: ''
  type: Support
  url: https://hilfe.gmx.net/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gmx.net/datenschutz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gmx.net/impressum/
- group: company
  title: ''
  type: Blog
  url: https://www.gmx.net/magazine/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gmx.net/mail/premium/
coverage:
  checked: '2026-10-27'
  detail: GMX provides email services but does not offer a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://gmx.net/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: GMX (mail) is a German email and cloud service provider offering free webmail, cloud storage, news, and premium upgrades. It serves millions of users with web and mobile interfaces, providing features such as personal email addresses, cloud backup, and integrated news and entertainment content. The service emphasizes security, data protection, and a range of optional paid features for enhanced mailbox capacity and functionality.
layout: provider
modified: '2026-10-27'
name: GMX (mail)
nav: Providers
network: true
overview: 'GMX (mail) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Cloud, Free, and German.


  GMX (mail)''s developer surface includes documentation, support, engineering blog, pricing, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gmx Net Domain Security
  slug: gmx-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gmx Net Vulnerability Disclosure
  slug: gmx-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gmx-net
tags:
- Company
- Email
- Cloud
- Free
- German
website: https://gmx.net/
---
