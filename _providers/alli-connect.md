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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Alli Connect provides a platform for employee engagement and communication.
  name: Alli Connect API
  slug: alli-connect-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alli-connect/refs/heads/main/conformance/alli-connect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alli-connect-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alli-connect/refs/heads/main/hosts/alli-connect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alli-connect-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alli-connect/refs/heads/main/vendors/alli-connect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alli-connect-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.alliconnect.com/company/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alli-connect/refs/heads/main/security/alli-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alli-connect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alliconnect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alliconnect.com/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alliconnect.com/book-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alliconnect.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.alliconnect.com/customer-success
coverage:
  checked: '2026-10-05'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 200
    url: https://www.alliconnect.com/platform
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Alli Connect provides peer support and wellness software for public safety agencies, including law enforcement, fire, EMS, and military. Their platform enables internal peer connections, therapist matching with AI, digital resource centers, wellness check‑ins across six domains, and 24/7 clinical support for critical incidents. The solution aims to improve mental health outcomes and resilience for first‑responders and related personnel.
image: https://cdn.prod.website-files.com/66b511e3db4a142cd99222a8/66be5aa721a788a55c77db0d_AC-OG.jpg
layout: provider
modified: '2026-09-24'
name: Alli Connect
nav: Providers
network: true
overview: 'Alli Connect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Peer Support, Wellness Software, Public Safety, Law Enforcement, and Fire Rescue.


  Alli Connect''s developer surface includes documentation, getting-started guide, support, and 7 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.1
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alli Connect Domain Security
  slug: alli-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alli-connect
tags:
- Peer Support
- Wellness Software
- Public Safety
- Law Enforcement
- Fire Rescue
- Military
- Mental Health
- Clinical Support
website: https://www.alliconnect.com/
---
