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
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://vdp.gaig.com
- group: auth
  href: https://artifacts.apis.io/great-american-insurance-group/well-known/great-american-insurance-group-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/great-american-insurance-group-www-security.txt
- group: agent
  href: https://artifacts.apis.io/great-american-insurance-group/well-known/great-american-insurance-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/great-american-insurance-group-well-known.yml
- group: other
  href: https://artifacts.apis.io/great-american-insurance-group/hosts/great-american-insurance-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/great-american-insurance-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/great-american-insurance-group/vendors/great-american-insurance-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/great-american-insurance-group-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.greatamericaninsurancegroup.com/about-us/business-operations/division/fidelity-crime/news
- group: start
  title: ''
  type: Login
  url: https://www.greatamericaninsurancegroup.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.greatamericaninsurancegroup.com/content-hub/loss-control/details/hiring-onboarding-and-engaging
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gaig.com/
- group: auth
  href: https://artifacts.apis.io/great-american-insurance-group/security/great-american-insurance-group-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/great-american-insurance-group-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/great-american-insurance-group/security/great-american-insurance-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/great-american-insurance-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gaig.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greatamericaninsurancegroup.com/contact/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greatamericaninsurancegroup.com/contact/legal-disclosures
- group: operate
  title: ''
  type: Support
  url: https://www.greatamericaninsurancegroup.com/contact
coverage:
  checked: '2026-10-28'
  detail: Great American Insurance Group does not provide a public API or developer program.
  evidence:
  - status: 200
    url: https://www.greatamericaninsurancegroup.com/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Great American Insurance Group (GAIG) is a specialty property and casualty insurance carrier operating in the United States. It provides a range of insurance solutions for niche industries, including commercial property, casualty, and specialty lines. GAIG is a member of American Financial Group, Inc., a publicly traded holding company. The website offers information about its services, corporate structure, legal disclosures, privacy policy, and contact options for customers and agents.
image: https://www.greatamericaninsurancegroup.com/images/default-source/menu-icons/ga-tower.png
layout: provider
modified: '2026-10-28'
name: Great American Insurance Group
nav: Providers
network: true
overview: 'Great American Insurance Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Property, Casualty, Specialty, and Financial-Services.


  Great American Insurance Group''s developer surface includes getting-started guide, documentation, support, and 12 more developer resources.'
random_paper: 23
scopes:
- name: Great American Insurance Group Scopes
  scope_count: 0
  slug: great-american-insurance-group-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 32.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Great American Insurance Group Authentication
  slug: great-american-insurance-group-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Great American Insurance Group Domain Security
  slug: great-american-insurance-group-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Great American Insurance Group Vulnerability Disclosure
  slug: great-american-insurance-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: great-american-insurance-group
tags:
- Insurance
- Property
- Casualty
- Specialty
- Financial-Services
- Company
website: https://gaig.com/
---
