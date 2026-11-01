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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/signaturit/plans/signaturit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/signaturit-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/signaturit/llms/signaturit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signaturit-llms.txt
- group: agent
  href: https://artifacts.apis.io/signaturit/well-known/signaturit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signaturit-well-known.yml
- group: other
  href: https://artifacts.apis.io/signaturit/hosts/signaturit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signaturit-hosts.yml
- group: other
  href: https://artifacts.apis.io/signaturit/vendors/signaturit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signaturit-vendors.yml
- group: build
  href: https://artifacts.apis.io/signaturit/packages/signaturit-packages.yml
  title: ''
  type: SDKs
  url: packages/signaturit-packages.yml
- group: build
  href: https://artifacts.apis.io/signaturit/packages/signaturit-packages.yml
  title: ''
  type: Packages
  url: packages/signaturit-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signaturit.com/legal-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signaturit.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signaturit.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.signaturit.com/press/
- group: start
  title: ''
  type: Login
  url: https://app.sandbox.signaturit.com/en/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signaturit
- group: auth
  href: https://artifacts.apis.io/signaturit/security/signaturit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signaturit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signaturit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.signaturit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.signaturit.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.signaturit.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://servicedesk-spain-latam.namirial.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.signaturit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signaturit.com/pricing
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://signaturit.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Signaturit Group, a Namirial Company, provides a trusted European digital transaction platform offering services such as electronic signatures, certified communications (SMS, email), digital identity verification, and e‑government solutions. The platform enables businesses to securely send, sign, and manage documents and communications, complying with European regulations and supporting a wide range of industries.
layout: provider
modified: '2026-10-21'
name: Signaturit Group, a Namirial Company
nav: Providers
network: true
overview: 'Signaturit Group, a Namirial Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Transactions, Electronic Signature, Identity Verification, and eGovernment.


  Signaturit Group, a Namirial Company''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Signaturit Plans Pricing
  plan_count: 4
  slug: signaturit-plans-pricing
random_paper: 18
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 46.4
    operational_transparency: 21.1
  provenance:
    mcp: unknown
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
  name: Signaturit Domain Security
  slug: signaturit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: signaturit
tags:
- Company
- Digital Transactions
- Electronic Signature
- Identity Verification
- eGovernment
website: https://signaturit.com/
---
