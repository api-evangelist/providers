---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: GraphQL endpoint for Boreastechnologies product data
  name: GraphQL API
  slug: graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boreastechnologies/refs/heads/main/llms/boreastechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boreastechnologies-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boreastechnologies/refs/heads/main/well-known/boreastechnologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boreastechnologies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boreastechnologies/refs/heads/main/hosts/boreastechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boreastechnologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boreastechnologies/refs/heads/main/vendors/boreastechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boreastechnologies-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.boreas.ca/pages/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boreas.ca/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.boreas.ca/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.boreas.ca/account/login
- group: company
  title: ''
  type: Blog
  url: https://pages.boreas.ca/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boreastechnologies/refs/heads/main/security/boreastechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boreastechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boreas.ca/
created: '2026-10-02'
description: Boréastechnologies, operating as Boréas Technologies, designs and manufactures ultra‑low power piezoelectric drivers and haptic solutions for smartphones, automotive, and IoT devices. Their product line includes CapDrive® drivers, development kits, and software tools, supported by extensive technical documentation, integration guides, and a developer portal.
image: http://www.boreas.ca/cdn/shop/files/AdobeStock_4269328161_6ba023a9-4ca6-4512-82c3-f5b4afd365ba.jpg?v=1772650251
layout: provider
modified: '2026-10-02'
name: Boréastechnologies
nav: Providers
network: true
overview: 'Boréastechnologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Haptics, Piezoelectric, and IoT.


  Boréastechnologies'' developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boreastechnologies Domain Security
  slug: boreastechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boreastechnologies
tags:
- Company
- Hardware
- Haptics
- Piezoelectric
- IoT
- Automotive
website: https://www.boreas.ca/
---
