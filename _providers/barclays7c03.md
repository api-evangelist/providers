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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/security/barclays7c03-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/barclays7c03-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/well-known/barclays7c03-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barclays7c03-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/well-known/barclays7c03-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barclays7c03-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/hosts/barclays7c03-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barclays7c03-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/vendors/barclays7c03-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barclays7c03-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.barclays/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://home.barclays/archive-barclays/collections/featured-items/register-of-new-clerks-union-bank-of-manchester/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.barclays/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://home.barclays/news/
- group: other
  title: ''
  type: Leadership
  url: https://home.barclays/who-we-are/structure-and-leadership/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/security/barclays7c03-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/barclays7c03-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barclays7c03/refs/heads/main/security/barclays7c03-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barclays7c03-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.barclays/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.barclays.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.barclays.com
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://developer.barclays.com/mcp
  - status: 403
    url: https://home.barclays/mcp
  - status: 403
    url: https://equityzen.com/company/barclays7c03
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Barclays7c03 is a stub entry for Barclays Group, a global financial services company offering banking, credit cards, wealth management, and investment services. The company operates worldwide with a corporate website at home.barclays, providing extensive information about its strategy, sustainability, and corporate governance. While the specific API offerings are not yet documented, the organization maintains a developer portal at developer.barclays.com for API exchange and integration resources.
layout: provider
modified: '2026-09-27'
name: Barclays7c03
nav: Providers
network: true
overview: 'Barclays7c03 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Finance, Global, and Corporate.


  Barclays7c03''s developer surface includes signup flow, documentation, API reference, and 12 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 0
  name: Barclays7C03 Rate Limits
  slug: barclays7c03-rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 39.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barclays7C03 Domain Security
  slug: barclays7c03-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Barclays7C03 Vulnerability Disclosure
  slug: barclays7c03-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: barclays7c03
tags:
- Banking
- Finance
- Global
- Corporate
website: https://home.barclays/
---
