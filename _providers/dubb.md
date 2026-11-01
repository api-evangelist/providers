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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Dubb provides video communication and sales enablement APIs as described on their pricing page.
  name: Dubb API
  slug: dubb-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://dubb.com/security
- group: agent
  href: https://artifacts.apis.io/dubb/llms/dubb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dubb-llms.txt
- group: auth
  href: https://artifacts.apis.io/dubb/well-known/dubb-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dubb-support-security.txt
- group: agent
  href: https://artifacts.apis.io/dubb/well-known/dubb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dubb-well-known.yml
- group: other
  href: https://artifacts.apis.io/dubb/hosts/dubb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dubb-hosts.yml
- group: other
  href: https://artifacts.apis.io/dubb/vendors/dubb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dubb-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dubb.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.dubb.com
- group: auth
  title: ''
  type: Security
  url: https://dubb.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dubb.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dubb.com/pricing
- group: start
  title: ''
  type: Login
  url: https://ai.dubb.com/login
- group: company
  title: ''
  type: Blog
  url: https://dubb.com/blog
- group: auth
  href: https://artifacts.apis.io/dubb/security/dubb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dubb-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dubb/security/dubb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dubb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dubb.com/
coverage:
  checked: '2026-10-28'
  detail: Pricing and documentation pages are rendered via JavaScript and block automated spec discovery.
  evidence:
  - status: 200
    url: https://dubb.com/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: 'Dubb is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://do.dubbcdn.com/img/dubb-og.png
layout: provider
modified: '2026-10-28'
name: Dubb
nav: Providers
network: true
overview: 'Dubb is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Dubb''s developer surface includes support, pricing, engineering blog, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 10.5
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
  name: Dubb Domain Security
  slug: dubb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Dubb Trust Center
  slug: dubb-trust-center
  summary_line: HIPAA, GDPR
slug: dubb
tags:
- Company
website: https://dubb.com/
---
