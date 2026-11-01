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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/caravelo/conformance/caravelo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caravelo-conformance.yml
- group: other
  href: https://artifacts.apis.io/caravelo/hosts/caravelo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caravelo-hosts.yml
- group: other
  href: https://artifacts.apis.io/caravelo/vendors/caravelo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caravelo-vendors.yml
- group: build
  href: https://artifacts.apis.io/caravelo/packages/caravelo-packages.yml
  title: ''
  type: SDKs
  url: packages/caravelo-packages.yml
- group: build
  href: https://artifacts.apis.io/caravelo/packages/caravelo-packages.yml
  title: ''
  type: Packages
  url: packages/caravelo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caravelo.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caravelo.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.caravelo.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://docs.caravelo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caravelo
- group: auth
  href: https://artifacts.apis.io/caravelo/security/caravelo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caravelo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caravelo.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.caravelo.com/mcp
  - status: 200
    url: https://www.caravelo.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Caravelo provides travel subscription solutions that increase revenue and market share, reduce seasonality, and create better customer experiences. It offers a platform for travel operators to sell subscription-based travel plans, enabling flexible, recurring travel purchases and improving cash flow.
image: https://www.caravelo.com/wp-content/uploads/2023/07/Travel-subscription-company-1-1024x654.png
layout: provider
modified: '2026-10-25'
name: Caravelo
nav: Providers
network: true
overview: 'Caravelo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Subscription, Platform, and SaaS.


  Caravelo''s developer surface includes documentation and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caravelo Domain Security
  slug: caravelo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caravelo
tags:
- Company
- Travel
- Subscription
- Platform
- SaaS
website: https://www.caravelo.com
---
