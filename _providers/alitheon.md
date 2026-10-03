---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alitheon/refs/heads/main/authentication/alitheon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alitheon-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alitheon/refs/heads/main/llms/alitheon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alitheon-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alitheon/refs/heads/main/hosts/alitheon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alitheon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alitheon/refs/heads/main/vendors/alitheon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alitheon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alitheon.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alitheon.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alitheon.com/docs/user-guide/9thid5p81kyai-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alitheon.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alitheon/refs/heads/main/security/alitheon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alitheon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alitheon.com
created: '2026-09-24'
description: Alitheon provides FeaturePrint®, an optical‑AI technology that creates a unique digital fingerprint of any physical object from a single photograph. It enables organizations to identify, authenticate, and trace items without labels, tags, or chips, serving sectors such as luxury goods, healthcare, automotive, government, and electronics.
image: https://www.alitheon.com/og-image.jpg
layout: provider
modified: '2026-09-24'
name: Alitheon
nav: Providers
network: true
overview: 'Alitheon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Anti‑Counterfeit, Asset Management, Supply Chain, and Physical Identity.


  Alitheon''s developer surface includes authentication, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alitheon Authentication
  slug: alitheon-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alitheon Domain Security
  slug: alitheon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alitheon
tags:
- Authentication
- Anti‑Counterfeit
- Asset Management
- Supply Chain
- Physical Identity
- Optical AI
website: https://alitheon.com
---
