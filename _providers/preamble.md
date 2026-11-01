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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/preamble/plans/preamble-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/preamble-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/preamble/llms/preamble-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/preamble-llms.txt
- group: agent
  href: https://artifacts.apis.io/preamble/well-known/preamble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/preamble-well-known.yml
- group: other
  href: https://artifacts.apis.io/preamble/hosts/preamble-hosts.yml
  title: ''
  type: Hosts
  url: hosts/preamble-hosts.yml
- group: other
  href: https://artifacts.apis.io/preamble/vendors/preamble-vendors.yml
  title: ''
  type: Vendors
  url: vendors/preamble-vendors.yml
- group: build
  href: https://artifacts.apis.io/preamble/packages/preamble-packages.yml
  title: ''
  type: SDKs
  url: packages/preamble-packages.yml
- group: build
  href: https://artifacts.apis.io/preamble/packages/preamble-packages.yml
  title: ''
  type: Packages
  url: packages/preamble-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.preamble.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.preamble.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.preamble.com/media
- group: start
  title: ''
  type: GettingStarted
  url: https://help.preamble.com/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.preamble.com/template-info/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://help.preamble.com/
- group: auth
  href: https://artifacts.apis.io/preamble/security/preamble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/preamble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://preamble.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.preamble.com/pricing
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://preamble.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Preamble provides cybersecurity and compliance solutions for generative AI, protecting against prompt injections, data leakage, and regulatory risks. Their platform offers policy enforcement, monitoring, and risk assessment tools tailored for AI developers and enterprises, ensuring safe and trustworthy AI deployments across various industries.
image: https://cdn.prod.website-files.com/67d5e6f8c0c32c5ff1c7f21d/67d5e7bb25c4c8e65404778f_Open%20Graph%20Preview.png
layout: provider
modified: '2026-10-21'
name: Preamble
nav: Providers
network: true
overview: 'Preamble is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, AI, Compliance, and Risk Management.


  Preamble''s developer surface includes getting-started guide, changelog, documentation, pricing, and 12 more developer resources.'
plans:
- name: Preamble Plans Pricing
  plan_count: 3
  slug: preamble-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Preamble Domain Security
  slug: preamble-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: preamble
tags:
- Company
- Cybersecurity
- AI
- Compliance
- Risk Management
website: https://preamble.com/
---
