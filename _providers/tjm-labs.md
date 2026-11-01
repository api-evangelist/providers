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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tjm-labs/hosts/tjm-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tjm-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/tjm-labs/vendors/tjm-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tjm-labs-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://tjmlabs.com/leadership/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tjmlabs
- group: auth
  href: https://artifacts.apis.io/tjm-labs/security/tjm-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tjm-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tjmlabs.com
- group: company
  title: ''
  type: Blog
  url: https://tjmlabs.com/blog
- group: company
  title: ''
  type: About
  url: https://tjmlabs.com/about-us/
- group: company
  title: ''
  type: Careers
  url: https://tjmlabs.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://tjmlabs.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tjmlabs.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tjmlabs.com/privacy-policy/
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://tjmlabs.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: TJM Labs is a pharmacy AI platform built by pharmacists, offering voice automation, vaccine intake bots, and custom data entry solutions for compounding, specialty, long‑term care, and community pharmacies. Their services include the TJM Custom Bot, Data Entry Bot, Provider Portal, Voice AI, and Vaccine Bot, aiming to scale pharmacy operations and improve efficiency across North America.
image: https://tjmlabs.com/images/og-default.png
layout: provider
modified: '2026-10-25'
name: TJM Labs
nav: Providers
network: true
overview: 'TJM Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmacy, AI, Automation, Healthcare, and Voice.


  TJM Labs'' developer surface includes engineering blog and 11 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tjm Labs Domain Security
  slug: tjm-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tjm-labs
tags:
- Pharmacy
- AI
- Automation
- Healthcare
- Voice
website: https://tjmlabs.com
---
