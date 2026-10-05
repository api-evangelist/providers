---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API reference for Billie payment integration
  name: Billie API
  slug: billie-api
artifact_total: 5
asyncapis:
- description: ''
  name: Billieio Webhooks
  slug: billieio-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billieio-www-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/vendors/billieio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billieio-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/asyncapi/billieio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/billieio-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: https://billie.io/coordinated-vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/authentication/billieio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billieio-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/llms/billieio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billieio-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billieio-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billieio-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billieio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/hosts/billieio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billieio-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.billie.io/s/?language=en_US
- group: operate
  title: ''
  type: StatusPage
  url: https://status.billie.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billie.io/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billie.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/security/billieio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/billieio-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/security/billieio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billieio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billie.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docs.billie.io/mcp
  - status: 401
    url: https://help.billie.io/mcp/v1
  - status: 403
    url: https://equityzen.com/company/billieio
  reason: partner-login
  state: gated
created: '2026-09-28'
description: Billie is a fintech platform that provides B2B payment solutions, enabling businesses to buy now and pay later, invoice financing, and flexible checkout options. It serves over 1.3 million buyers and 9,000 merchants across Europe, processing billions in transaction volume. The service includes integration via APIs for order creation, payment processing, and refunds, with support for multiple payment methods and partner integrations.
layout: provider
modified: '2026-09-28'
name: Billieio
nav: Providers
network: true
overview: 'Billieio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, B2B, and Europe.


  The Billieio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Billieio''s developer surface includes authentication, support, API reference, documentation, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 33.3
    discoverability: 51.8
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 16.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Billieio Authentication
  slug: billieio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Billieio Domain Security
  slug: billieio-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Billieio Vulnerability Disclosure
  slug: billieio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: billieio
tags:
- Fintech
- Payments
- B2B
- Europe
website: https://www.billie.io
---
