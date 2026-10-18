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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearballotgroupinc/refs/heads/main/hosts/clearballotgroupinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearballotgroupinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearballotgroupinc/refs/heads/main/vendors/clearballotgroupinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearballotgroupinc-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.clearballot.com/contact-support
- group: auth
  title: ''
  type: Security
  url: https://www.clearballot.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearballot.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.clearballot.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearballotgroupinc/refs/heads/main/security/clearballotgroupinc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearballotgroupinc-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearballotgroupinc/refs/heads/main/security/clearballotgroupinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearballotgroupinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearballot.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.clearballot.com/mcp
  - status: 200
    url: https://www.clearballot.com
  - status: 403
    url: https://equityzen.com/company/clearballotgroupinc
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Clearballotgroupinc is a technology company focused on providing secure, transparent, and verifiable ballot handling solutions for elections and organizational voting. The platform aims to modernize the voting process through digital tools that ensure integrity, accessibility, and auditability, catering to both public sector elections and private organizational decision-making. While detailed public documentation is limited, the company positions itself as a bridge between traditional ballot methods and innovative digital solutions, emphasizing security and compliance with electoral standards.
image: https://www.clearballot.com/hubfs/FeaturedImage.jpg
layout: provider
modified: '2026-10-08'
name: Clearballotgroupinc
nav: Providers
network: true
overview: 'Clearballotgroupinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Elections, Voting, Security, and Technology.


  Clearballotgroupinc''s developer surface includes support and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 10.5
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
  name: Clearballotgroupinc Domain Security
  slug: clearballotgroupinc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clearballotgroupinc Vulnerability Disclosure
  slug: clearballotgroupinc-vulnerability-disclosure
  summary_line: no policy recorded
slug: clearballotgroupinc
tags:
- Company
- Elections
- Voting
- Security
- Technology
website: https://www.clearballot.com
---
