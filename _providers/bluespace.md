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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluespace/refs/heads/main/vendors/bluespace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluespace-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluespace/refs/heads/main/security/bluespace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluespace-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluespace/refs/heads/main/hosts/bluespace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluespace-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: company
  title: ''
  type: website
  url: https://www.bluespace.ai
- group: docs
  title: ''
  type: documentation
  url: https://www.bluespace.ai/technology
- group: company
  title: ''
  type: blog
  url: https://www.bluespace.ai/blog
- group: commercial
  title: ''
  type: termsOfService
  url: https://www.bluespace.ai/terms-of-service
- group: operate
  title: ''
  type: support
  url: https://www.bluespace.ai/contact
created: '2026-09-29'
description: BlueSpace is a technology services company that provides cloud integration, digital workspace solutions, and AI capabilities for public sector and commercial enterprises. Founded over 30 years ago, it partners with major technology vendors to deliver secure, reliable, and cost-effective IT solutions, focusing on modern infrastructure, networking, and security services.
layout: provider
modified: '2026-09-29'
name: BlueSpace
nav: Providers
network: true
overview: 'BlueSpace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Integration, Artificial Intelligence, Services, and Enterprise.


  BlueSpace''s developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluespace Domain Security
  slug: bluespace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluespace
tags:
- Cloud
- Integration
- Artificial Intelligence
- Services
- Enterprise
website: https://www.nasdaqprivatemarket.com/
---
