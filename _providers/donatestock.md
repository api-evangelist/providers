---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DonateStock provides a platform for donors to contribute publicly traded stock, cryptocurrency, and other assets to charitable organizations. The Help Center describes the service but no machine‑reada
  name: DonateStock API
  slug: donatestock-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/donatestock/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://donatestock.com/security
- group: other
  href: https://artifacts.apis.io/donatestock/hosts/donatestock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donatestock-hosts.yml
- group: other
  href: https://artifacts.apis.io/donatestock/vendors/donatestock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donatestock-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.donatestock.com/en-US
- group: auth
  title: ''
  type: Security
  url: https://donatestock.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://donatestock.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://donatestock.com/press
- group: company
  title: ''
  type: Blog
  url: https://donatestock.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.donatestock.com/
- group: auth
  href: https://artifacts.apis.io/donatestock/security/donatestock-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/donatestock-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/donatestock/security/donatestock-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/donatestock-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/donatestock/security/donatestock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donatestock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donatestock.com/
coverage:
  checked: '2026-10-27'
  detail: The provider's Help Center contains only HTML documentation and no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://help.donatestock.com/en-US
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: DonateStock is a platform that enables donors to contribute publicly traded stock, cryptocurrency, and other assets to charitable organizations quickly and tax-efficiently. By allowing donors to avoid capital gains tax and receive larger deductions, it benefits both donors and nonprofits. The service also offers tools for financial advisors and donors to manage charitable giving, featuring a marketplace of causes, educational resources, and a secure transaction process.
image: https://donatestock.com/themes/custom/donstob/share-image.png
layout: provider
modified: '2026-10-27'
name: DonateStock
nav: Providers
network: true
overview: 'DonateStock is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Charity, Stock, and Donations.


  DonateStock''s developer surface includes support, engineering blog, documentation, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Donatestock Domain Security
  slug: donatestock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Donatestock Vulnerability Disclosure
  slug: donatestock-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Donatestock Trust Center
  slug: donatestock-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: donatestock
tags:
- Company
- Finance
- Charity
- Stock
- Donations
- Platform
website: https://donatestock.com/
---
