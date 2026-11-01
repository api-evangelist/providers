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
api_count: 1
apis:
- description: Security product APIs referenced in the security documentation.
  name: DugganUSA Security API
  slug: dugganusa-security-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dugganusa-com/llms/dugganusa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dugganusa-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-dugganusa-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-dugganusa-security.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-aipmsec-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-aipmsec-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.dugganusa.com/post/dugganusa-vulnerability-disclosure-policy-and-hall-of-fame
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-security.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-security-security.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-finops-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-finops-security.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-epstein-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-epstein-security.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-analytics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dugganusa-com-analytics-security.txt
- group: agent
  href: https://artifacts.apis.io/dugganusa-com/well-known/dugganusa-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dugganusa-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dugganusa-com/hosts/dugganusa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dugganusa-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dugganusa-com/vendors/dugganusa-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dugganusa-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://analytics.dugganusa.com/stix/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dugganusa.com/post/privacy-first-security-what-tim-cook-would-build-if-he-started-a-security-company
- group: commercial
  title: ''
  type: Pricing
  url: https://analytics.dugganusa.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pduggusa
- group: company
  title: ''
  type: Blog
  url: https://www.dugganusa.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dugganusa.com/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dugganusa.com/
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/security/dugganusa-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dugganusa-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dugganusa-com/security/dugganusa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dugganusa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dugganusa.com/
coverage:
  checked: '2026-10-30'
  detail: Cloudflare bot challenge blocks access to the security docs, preventing retrieval of a machine-readable spec.
  evidence:
  - status: 403
    url: https://security.dugganusa.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Duggan USA is listed as a stub company in the API Evangelist harvest backlog. No public website or documentation could be retrieved despite attempts using standard and rendered fetch methods, indicating the company may not have an active online presence or may restrict access. Further investigation is required to confirm its identity and any available API offerings.
image: https://static.wixstatic.com/media/fd5e2b_253df397e0a04da3b551842db6fbb2fc%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/fd5e2b_253df397e0a04da3b551842db6fbb2fc%7Emv2.jpg
layout: provider
modified: '2026-10-30'
name: dugganusa-com
nav: Providers
network: true
overview: 'dugganusa-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Technology, Services, and USA.


  dugganusa-com''s developer surface includes signup flow, pricing, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dugganusa Com Domain Security
  slug: dugganusa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dugganusa Com Vulnerability Disclosure
  slug: dugganusa-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dugganusa-com
tags:
- Company
- API
- Technology
- Services
- USA
website: https://dugganusa.com/
---
