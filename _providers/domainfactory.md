---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/domainfactory/well-known/domainfactory-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainfactory-www-security.txt
- group: auth
  title: ''
  type: Security
  url: https://df.eu/whitehat/policy
- group: auth
  href: https://artifacts.apis.io/domainfactory/well-known/domainfactory-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainfactory-status-security.txt
- group: auth
  href: https://artifacts.apis.io/domainfactory/well-known/domainfactory-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainfactory-security.txt
- group: auth
  href: https://artifacts.apis.io/domainfactory/well-known/domainfactory-df-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainfactory-df-security.txt
- group: auth
  href: https://artifacts.apis.io/domainfactory/well-known/domainfactory-admin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainfactory-admin-security.txt
- group: agent
  href: https://artifacts.apis.io/domainfactory/well-known/domainfactory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domainfactory-well-known.yml
- group: other
  href: https://artifacts.apis.io/domainfactory/hosts/domainfactory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainfactory-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.df.eu/
- group: auth
  href: https://artifacts.apis.io/domainfactory/security/domainfactory-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/domainfactory-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/domainfactory/security/domainfactory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainfactory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://df.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.df.eu/de/
- group: operate
  title: ''
  type: Support
  url: https://www.df.eu/de/support/
- group: company
  title: ''
  type: Blog
  url: https://www.df.eu/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.df.eu/de/preislisten/
coverage:
  checked: '2026-10-27'
  detail: No public developer documentation or API specifications are provided on the website.
  evidence:
  - status: 200
    url: https://www.df.eu/de/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: DomainFactory is a German provider of domain registration, web hosting, and related online services. It offers a range of products including domain transfer, shared and managed web hosting, WordPress hosting, VPS, SSL certificates, and website builder tools. Customers can manage their services via a client portal and benefit from support, service level agreements, and integration with Microsoft 365. The company emphasizes easy domain migration and a comprehensive hosting platform for businesses and individuals.
layout: provider
modified: '2026-10-27'
name: DomainFactory
nav: Providers
network: true
overview: 'DomainFactory is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Domains, WebHosting, and SSL.


  DomainFactory''s developer surface includes documentation, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domainfactory Domain Security
  slug: domainfactory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Domainfactory Vulnerability Disclosure
  slug: domainfactory-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: domainfactory
tags:
- Company
- Hosting
- Domains
- WebHosting
- SSL
website: https://df.eu/
---
