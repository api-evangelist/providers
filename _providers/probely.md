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
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://snyk.io/product/dast-api-web/
- group: agent
  href: https://artifacts.apis.io/probely/llms/probely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/probely-llms.txt
- group: auth
  href: https://artifacts.apis.io/probely/well-known/probely-snyk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/probely-snyk-security.txt
- group: auth
  href: https://artifacts.apis.io/probely/well-known/probely-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/probely-security.txt
- group: auth
  href: https://artifacts.apis.io/probely/well-known/probely-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/probely-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/probely/well-known/probely-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/probely-well-known.yml
- group: other
  href: https://artifacts.apis.io/probely/hosts/probely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/probely-hosts.yml
- group: other
  href: https://artifacts.apis.io/probely/vendors/probely-vendors.yml
  title: ''
  type: Vendors
  url: vendors/probely-vendors.yml
- group: build
  href: https://artifacts.apis.io/probely/packages/probely-packages.yml
  title: ''
  type: SDKs
  url: packages/probely-packages.yml
- group: build
  href: https://artifacts.apis.io/probely/packages/probely-packages.yml
  title: ''
  type: Packages
  url: packages/probely-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.probely.com/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://probely.com/sign-up/
- group: auth
  title: ''
  type: Security
  url: https://probely.com/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://probely.com/pricing/
- group: other
  title: ''
  type: Leadership
  url: https://probely.com/web-vulnerability-scanner/management/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snyk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.probely.com/?_gl=1*10r1o7h*_gcl_au*MTYxMzA3MDk4MS4xNzA3ODA1MDA3
- group: company
  title: ''
  type: Blog
  url: https://probely.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snyk.io/getting-started-guides/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.probely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.probely.com/api/reference/
- group: auth
  href: https://artifacts.apis.io/probely/security/probely-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/probely-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/probely/security/probely-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/probely-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/probely/security/probely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/probely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://probely.com/
created: '2026-10-26'
description: 'Probely is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://probely.com/api/og?title=Web%20application%20and%20API%20vulnerability%20scanner
layout: provider
modified: '2026-10-26'
name: Probely
nav: Providers
network: true
overview: 'Probely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Probely''s developer surface includes signup flow, pricing, engineering blog, getting-started guide, documentation, API reference, and 19 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 32.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Probely Domain Security
  slug: probely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Probely Vulnerability Disclosure
  slug: probely-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Probely Trust Center
  slug: probely-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: probely
tags:
- Company
website: https://probely.com/
---
