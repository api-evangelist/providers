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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/joinupkid-com/hosts/joinupkid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinupkid-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinupkid-com/vendors/joinupkid-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinupkid-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upkid.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upkid.com/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.upkid.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.upkid.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.upkid.com/reference/changelog
- group: auth
  href: https://artifacts.apis.io/joinupkid-com/security/joinupkid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinupkid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upkid.com/
coverage:
  checked: '2026-10-29'
  detail: The provider's website offers documentation pages but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.upkid.com/get-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Upkid is a platform that connects early childhood education programs with qualified teachers, offering both full‑time and flexible job opportunities. It provides an applicant tracking system for childcare providers, enables teachers to find on‑demand positions, and supports hiring hubs across multiple US locations. The service aims to streamline recruitment, improve candidate matching, and enhance early‑education staffing efficiency.
image: https://cdn.prod.website-files.com/61157274e97e06297f461117/6160bcd1f1eb5612716b2045_ogupkid.jpg
layout: provider
modified: '2026-10-29'
name: Upkid
nav: Providers
network: true
overview: 'Upkid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Childcare, Recruitment, SaaS, and Marketplace.


  Upkid''s developer surface includes getting-started guide, engineering blog, API reference, and 6 more developer resources.'
plans:
- name: Joinupkid Com Plans Pricing
  plan_count: 0
  slug: joinupkid-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Joinupkid Com Rate Limits
  slug: joinupkid-com-rate-limits
scopes:
- name: Joinupkid Com Scopes
  scope_count: 0
  slug: joinupkid-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Joinupkid Com Authentication
  slug: joinupkid-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Joinupkid Com Domain Security
  slug: joinupkid-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: joinupkid-com
tags:
- Education
- Childcare
- Recruitment
- SaaS
- Marketplace
website: https://www.upkid.com/
---
