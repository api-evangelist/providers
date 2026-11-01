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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/austrian-post/security/austrian-post-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/austrian-post-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/austrian-post/well-known/austrian-post-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/austrian-post-security.txt
- group: auth
  href: https://artifacts.apis.io/austrian-post/well-known/austrian-post-post-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/austrian-post-post-security.txt
- group: auth
  href: https://artifacts.apis.io/austrian-post/well-known/austrian-post-ella-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/austrian-post-ella-security.txt
- group: agent
  href: https://artifacts.apis.io/austrian-post/well-known/austrian-post-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/austrian-post-well-known.yml
- group: other
  href: https://artifacts.apis.io/austrian-post/hosts/austrian-post-hosts.yml
  title: ''
  type: Hosts
  url: hosts/austrian-post-hosts.yml
- group: other
  href: https://artifacts.apis.io/austrian-post/vendors/austrian-post-vendors.yml
  title: ''
  type: Vendors
  url: vendors/austrian-post-vendors.yml
- group: auth
  href: https://artifacts.apis.io/austrian-post/security/austrian-post-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/austrian-post-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/austrian-post/security/austrian-post-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/austrian-post-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://post.at/
- group: docs
  title: ''
  type: Documentation
  url: https://www.post.at/en
- group: company
  title: ''
  type: Blog
  url: https://www.post.at/en/p/blog
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.post.at/en/ir/c/investor-relations
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.post.at/en/i/c/data-protection
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.post.at/en/i/c/gtc
- group: operate
  title: ''
  type: Support
  url: https://www.post.at/en/p/c/faq
created: '2026-10-27'
description: Austrian Post (Post AG) is Austria’s national postal service provider, offering a wide range of mail, parcel, logistics, and digital services. The company operates an extensive network of post offices and delivery infrastructure, supporting both domestic and international shipments. Its online platform provides rate calculators, tracking, e‑letter services, and business solutions such as bulk mailing and e‑commerce fulfillment. The website also hosts corporate information, investor relations, sustainability initiatives, and a blog with updates on services and innovations.
image: https://assets.post.at/-/media/Bilder/Open-Graph/OG-Post-Start.jpg?rev=69a56f14-d066-426a-96a5-21e57281f7d8
layout: provider
modified: '2026-10-27'
name: Austrian Post (Post AG)
nav: Providers
network: true
overview: 'Austrian Post (Post AG) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Postal, Logistics, Austria, and Services.


  Austrian Post (Post AG)''s developer surface includes documentation, engineering blog, support, and 13 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
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
  name: Austrian Post Domain Security
  slug: austrian-post-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Austrian Post Vulnerability Disclosure
  slug: austrian-post-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: austrian-post
tags:
- Company
- Postal
- Logistics
- Austria
- Services
website: https://post.at/
---
