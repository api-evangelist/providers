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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authenticvision/refs/heads/main/llms/authenticvision-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authenticvision-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/authenticvision/refs/heads/main/hosts/authenticvision-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authenticvision-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/authenticvision/refs/heads/main/vendors/authenticvision-vendors.yml
  title: ''
  type: Vendors
  url: vendors/authenticvision-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authenticvision/refs/heads/main/packages/authenticvision-packages.yml
  title: ''
  type: SDKs
  url: packages/authenticvision-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authenticvision/refs/heads/main/packages/authenticvision-packages.yml
  title: ''
  type: Packages
  url: packages/authenticvision-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.authenticvision.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.authenticvision.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/authenticvision
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authenticvision/refs/heads/main/security/authenticvision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authenticvision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.authenticvision.com
- group: company
  title: ''
  type: About
  url: https://www.authenticvision.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.authenticvision.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.authenticvision.com/privacy-policy-html/
- group: other
  title: ''
  type: Imprint
  url: https://www.authenticvision.com/imprint/
- group: operate
  title: ''
  type: Support
  url: https://www.authenticvision.com/contact/
created: '2026-09-26'
description: Authenticvision provides anti-counterfeiting and digital product passport solutions, helping brands protect products across industries such as automotive, healthcare, and finance. Their platform enables instant verification via smartphones, offers brand protection as a service, and supports circular economy initiatives through blockchain-backed product data.
layout: provider
modified: '2026-09-26'
name: Authenticvision
nav: Providers
network: true
overview: 'Authenticvision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Anti-Counterfeiting, Digital Product Passport, Blockchain, and Brand Protection.


  Authenticvision''s developer surface includes documentation, engineering blog, support, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Authenticvision Domain Security
  slug: authenticvision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authenticvision
tags:
- Company
- Anti-Counterfeiting
- Digital Product Passport
- Blockchain
- Brand Protection
website: https://www.authenticvision.com
---
