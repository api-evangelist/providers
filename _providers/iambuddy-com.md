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
- group: agent
  href: https://artifacts.apis.io/iambuddy-com/llms/iambuddy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iambuddy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/iambuddy-com/hosts/iambuddy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iambuddy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/iambuddy-com/vendors/iambuddy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iambuddy-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.buddy.insure/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.buddy.insure/
- group: auth
  href: https://artifacts.apis.io/iambuddy-com/security/iambuddy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iambuddy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buddy.insure/
- group: docs
  title: ''
  type: Documentation
  url: https://www.buddy.insure/terms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buddy.insure/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buddy.insure/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.buddy.insure/buddy-blog
created: '2026-10-24'
description: Buddy (formerly iambuddy.com) provides a digital commerce platform for insurance, enabling companies to configure and deploy buying experiences across channels quickly. Backed by Techstars and part of the VC portfolio, Buddy offers the Model Context Protocol (MCP) to quote, bind, and collect payments on insurance policies via AI tools. The platform integrates with carriers, supports real-time pricing, and aims to simplify insurance distribution for businesses.
image: https://buddy.insure/images/buddy-wordmark.svg
layout: provider
modified: '2026-10-24'
name: iambuddy.com
nav: Providers
network: true
overview: 'iambuddy.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Platform, DigitalCommerce, MCP, and Techstars.


  iambuddy.com''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 11.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Iambuddy Com Domain Security
  slug: iambuddy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iambuddy-com
tags:
- Insurance
- Platform
- DigitalCommerce
- MCP
- Techstars
- AI
website: https://www.buddy.insure/
---
