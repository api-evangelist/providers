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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/sesamm-com/hosts/sesamm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sesamm-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sesamm-com/vendors/sesamm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sesamm-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sesamm.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.sesamm.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.sesamm.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sesamm.com/category/151-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.sesamm.com/
- group: auth
  href: https://artifacts.apis.io/sesamm-com/security/sesamm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sesamm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sesamm.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://sesamm.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: SESAMm provides AI‑powered ESG and reputational risk intelligence, monitoring controversies and exposure across over 5 million public and private companies. Leveraging more than 30 billion documents, its platform helps organizations assess ESG risks, track reputational issues, and make data‑driven decisions.
image: https://cdn.prod.website-files.com/693a7da195d28c9004c133fd/6a2681fe17a2bfa17b36967f_2626289a375cf9ae490fd05ab36a8e3b_Hompage%20Page%3A%20Open%20Graph%20Images%20for%20Website.png
layout: provider
modified: '2026-10-21'
name: SESAMm
nav: Providers
network: true
overview: 'SESAMm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include ESG, Risk Intelligence, Investment, Compliance, and Supply Chain.


  SESAMm''s developer surface includes engineering blog, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sesamm Com Domain Security
  slug: sesamm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sesamm-com
tags:
- ESG
- Risk Intelligence
- Investment
- Compliance
- Supply Chain
- AI
website: https://sesamm.com/
---
