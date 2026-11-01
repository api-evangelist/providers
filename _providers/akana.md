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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/akana/well-known/akana-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/akana-well-known.yml
- group: other
  href: https://artifacts.apis.io/akana/hosts/akana-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akana-hosts.yml
- group: other
  href: https://artifacts.apis.io/akana/vendors/akana-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akana-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.perforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.akana.com/content/current/home.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perforce.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.perforce.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://www.perforce.com/products/akana/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.perforce.com/s/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.perforce.com/products/akana/api-platform/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.perforce.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.akana.com/
- group: auth
  href: https://artifacts.apis.io/akana/security/akana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.perforce.com/products/akana/api-platform
coverage:
  checked: '2026-10-19'
  detail: The Akana API Platform page provides only HTML documentation and no machine‑readable OpenAPI/Swagger/GraphQL spec.
  evidence:
  - status: 200
    url: https://www.perforce.com/products/akana/api-platform
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Perforce, operating under the Akana brand, provides a comprehensive API management platform that enables enterprises to design, secure, publish, and monitor APIs at scale. The solution supports full lifecycle management, developer portal capabilities, and robust security features, helping organizations accelerate digital transformation and integrate services across cloud and on-premises environments. Akana’s platform is used by large enterprises to streamline API governance, enforce policies, and provide analytics for performance optimization.
image: https://www.perforce.com/sites/default/files/image-social-share-default.jpg
layout: provider
modified: '2026-10-19'
name: Akana
nav: Providers
network: true
overview: 'Akana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Management, Enterprise, Integration, and Platform.


  Akana''s developer surface includes support, getting-started guide, changelog, engineering blog, documentation, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Akana Domain Security
  slug: akana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akana
tags:
- Company
- API Management
- Enterprise
- Integration
- Platform
website: https://www.perforce.com/products/akana/api-platform
---
