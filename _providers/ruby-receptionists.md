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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/ruby-receptionists/well-known/ruby-receptionists-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ruby-receptionists-well-known.yml
- group: other
  href: https://artifacts.apis.io/ruby-receptionists/hosts/ruby-receptionists-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ruby-receptionists-hosts.yml
- group: other
  href: https://artifacts.apis.io/ruby-receptionists/vendors/ruby-receptionists-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ruby-receptionists-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ruby-receptionists/security/ruby-receptionists-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ruby-receptionists-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ruby.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ruby.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://rubyhelpcenter.helpjuice.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ruby.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ruby.com/plans-and-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ruby.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ruby.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://my.call-ruby.com/
coverage:
  checked: '2026-10-29'
  detail: Ruby Receptionists provides virtual receptionist services and does not expose a public API.
  evidence:
  - status: 200
    url: https://www.ruby.com/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Ruby Receptionists offers 24/7 live virtual receptionist support and live chat services for small businesses, ensuring every call is answered by a trained human, not a bot. Their solutions capture leads, schedule appointments, and integrate with existing tools across industries such as legal, home services, and financial services. With customizable coverage, businesses can choose full call handling or backup support, improving customer engagement and reducing missed opportunities.
image: https://www.ruby.com/wp-content/uploads/2022/07/On-Dark.svg
layout: provider
modified: '2026-10-28'
name: Ruby Receptionists
nav: Providers
network: true
overview: 'Ruby Receptionists is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include virtual-receptionist, live-chat, 24-7-support, small-business, and call-answering.


  Ruby Receptionists'' developer surface includes getting-started guide, support, engineering blog, pricing, signup flow, and 7 more developer resources.'
plans:
- name: Ruby Receptionists Plans Pricing
  plan_count: 0
  slug: ruby-receptionists-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Ruby Receptionists Rate Limits
  slug: ruby-receptionists-rate-limits
scopes:
- name: Ruby Receptionists Scopes
  scope_count: 0
  slug: ruby-receptionists-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ruby Receptionists Authentication
  slug: ruby-receptionists-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ruby Receptionists Domain Security
  slug: ruby-receptionists-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ruby-receptionists
tags:
- virtual-receptionist
- live-chat
- 24-7-support
- small-business
- call-answering
website: https://ruby.com/
---
