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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/cgi/security/cgi-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cgi-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/cgi/llms/cgi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cgi-llms.txt
- group: auth
  href: https://artifacts.apis.io/cgi/well-known/cgi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cgi-security.txt
- group: auth
  href: https://artifacts.apis.io/cgi/well-known/cgi-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cgi-data-security.txt
- group: auth
  href: https://artifacts.apis.io/cgi/well-known/cgi-cgi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cgi-cgi-security.txt
- group: agent
  href: https://artifacts.apis.io/cgi/well-known/cgi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cgi-well-known.yml
- group: other
  href: https://artifacts.apis.io/cgi/hosts/cgi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cgi-hosts.yml
- group: other
  href: https://artifacts.apis.io/cgi/vendors/cgi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cgi-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.cgi.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cgi.com/en/newsroom
- group: auth
  href: https://artifacts.apis.io/cgi/security/cgi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cgi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cgi/security/cgi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cgi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cgi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cgi.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.cgi.com/en/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cgi.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cgi.com/en/privacy
created: '2026-10-20'
description: CGI is a global IT and business consulting services firm offering end‑to‑end solutions across digital transformation, cloud and hybrid IT, cybersecurity, data analytics, artificial intelligence, quantum computing, and industry‑specific services. With a presence in over 40 countries, CGI partners with enterprises to design, implement, and manage technology solutions that drive innovation and operational efficiency.
layout: provider
modified: '2026-10-20'
name: CGI
nav: Providers
network: true
overview: 'CGI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IT, Consulting, Cloud, and Cybersecurity.


  CGI''s developer surface includes support, documentation, engineering blog, and 14 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cgi Domain Security
  slug: cgi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cgi Vulnerability Disclosure
  slug: cgi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cgi
tags:
- Company
- IT
- Consulting
- Cloud
- Cybersecurity
website: https://cgi.com/
---
