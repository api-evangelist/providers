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
  score: 2.9
  scored_at: '2026-11-06'
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
  composite: 11.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 45.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gmx-net/gmx-net-2026-11-03T132854.png
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
