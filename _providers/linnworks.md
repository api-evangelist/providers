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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.linnworks.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/llms/linnworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linnworks-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/well-known/linnworks-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/linnworks-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/well-known/linnworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linnworks-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/hosts/linnworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linnworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/vendors/linnworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linnworks-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.linnworks.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.linnworks.com/support/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.linnworks.com/
- group: auth
  title: ''
  type: Security
  url: https://www.linnworks.com/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.linnworks.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.linnworks.com/news/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.linnworks.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/security/linnworks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/linnworks-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/security/linnworks-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linnworks-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linnworks/refs/heads/main/security/linnworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linnworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.linnworks.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at common spec endpoints on api.linnworks.com.
  evidence:
  - status: 404
    url: https://api.linnworks.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Linnworks provides a multichannel inventory and order management platform for small and medium-sized e‑commerce businesses. Their SaaS solution centralises inventory, automates order processing, integrates with multiple marketplaces and shipping carriers, and offers AI‑driven forecasting and reporting tools. The platform aims to help retailers scale operations across channels while reducing manual effort and errors.
image: https://www.linnworks.com/wp-content/uploads/2025/02/hero-visual-dtv2.png
layout: provider
modified: '2026-10-14'
name: Linnworks
nav: Providers
network: true
overview: 'Linnworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Software-as-a-Service, Inventory, and Order Management.


  Linnworks'' developer surface includes support, pricing, documentation, and 14 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Linnworks Domain Security
  slug: linnworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linnworks Vulnerability Disclosure
  slug: linnworks-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Linnworks Trust Center
  slug: linnworks-trust-center
  summary_line: ISO 27001, GDPR
slug: linnworks
tags:
- Company
- E-Commerce
- Software-as-a-Service
- Inventory
- Order Management
website: https://www.linnworks.com
---
