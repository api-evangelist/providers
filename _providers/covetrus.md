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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/covetrus/llms/covetrus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/covetrus-llms.txt
- group: agent
  href: https://artifacts.apis.io/covetrus/well-known/covetrus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/covetrus-well-known.yml
- group: other
  href: https://artifacts.apis.io/covetrus/hosts/covetrus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/covetrus-hosts.yml
- group: other
  href: https://artifacts.apis.io/covetrus/vendors/covetrus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/covetrus-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://covetrus.com/legal/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://covetrus.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://covetrus.com/legal/privacy-notices/
- group: company
  title: ''
  type: Newsroom
  url: https://covetrus.com/about/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://covetrus.com/about/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://covetrus.com/insights/webinar-your-rxassist-setup-step-by-step/
- group: auth
  href: https://artifacts.apis.io/covetrus/security/covetrus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/covetrus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://covetrus.com/
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API hosts.
  evidence:
  - status: 404
    url: https://api.covetrus.com/openapi.json
  - status: 404
    url: https://api.covetrus.com/openapi.yaml
  - status: 404
    url: https://api.covetrus.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Covetrus provides veterinary software, online pharmacy, and client communication solutions that simplify every touchpoint from pre‑visit to post‑appointment. Their platform offers practice management, workflow productivity tools, prescription management, and a suite of services for animal health professionals, aiming to deliver a frictionless, connected experience across the veterinary ecosystem.
image: https://covetrus.com/wp-content/uploads/hero-background-scaled.webp
layout: provider
modified: '2026-10-28'
name: Covetrus
nav: Providers
network: true
overview: 'Covetrus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Veterinary, Software, Pharmacy, and Client-Communication.


  Covetrus'' developer surface includes support, getting-started guide, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
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
  name: Covetrus Domain Security
  slug: covetrus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: covetrus
tags:
- Company
- Veterinary
- Software
- Pharmacy
- Client-Communication
website: https://covetrus.com/
---
