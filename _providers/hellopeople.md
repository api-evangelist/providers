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
api_count: 1
apis:
- description: API documentation and integration guides for Hello People services.
  name: Hello People API
  slug: hello-people-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/hellopeople/security/hellopeople-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/hellopeople-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/hellopeople/llms/hellopeople-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hellopeople-llms.txt
- group: auth
  href: https://artifacts.apis.io/hellopeople/well-known/hellopeople-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hellopeople-security.txt
- group: agent
  href: https://artifacts.apis.io/hellopeople/well-known/hellopeople-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hellopeople-well-known.yml
- group: other
  href: https://artifacts.apis.io/hellopeople/hosts/hellopeople-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hellopeople-hosts.yml
- group: other
  href: https://artifacts.apis.io/hellopeople/vendors/hellopeople-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hellopeople-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hellopeople.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hellopeople.com.au/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://hellopeople.com.au/guides
- group: auth
  href: https://artifacts.apis.io/hellopeople/security/hellopeople-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hellopeople-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hellopeople/security/hellopeople-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hellopeople-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hellopeople.com.au/
coverage:
  checked: '2026-10-20'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://hellopeople.com.au/openapi.json
  - status: 301
    url: https://api.com.au/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: HELLO PEOPLE provides AI integration and automation services across Australia, offering custom software development, web and mobile app creation, low‑code solutions, and comprehensive system integration. Their portfolio includes AI development, workflow automation, and industry‑specific platforms for project controls, compliance, and online learning, serving clients in Perth, Melbourne, Sydney, and Brisbane.
image: https://hellopeople.com.au/images/og-default.png
layout: provider
modified: '2026-10-20'
name: HELLO PEOPLE
nav: Providers
network: true
overview: 'HELLO PEOPLE is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Integration, Automation, and Software.


  HELLO PEOPLE''s developer surface includes documentation and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hellopeople Domain Security
  slug: hellopeople-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hellopeople Vulnerability Disclosure
  slug: hellopeople-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hellopeople
tags:
- Company
- Artificial Intelligence
- Integration
- Automation
- Software
website: https://hellopeople.com.au/
---
