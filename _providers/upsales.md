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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.upsales.com/no/pricing
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upsales/refs/heads/main/llms/upsales-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upsales-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upsales/refs/heads/main/well-known/upsales-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upsales-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upsales/refs/heads/main/well-known/upsales-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upsales-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/upsales/refs/heads/main/hosts/upsales-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upsales-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/upsales/refs/heads/main/vendors/upsales-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upsales-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upsales.com/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.upsales.com
- group: operate
  title: ''
  type: StatusPage
  url: http://status.upsales.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upsales.com/legal/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.upsales.com/about-upsales/team
- group: company
  title: ''
  type: Blog
  url: https://www.upsales.com/about-upsales/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upsales/refs/heads/main/security/upsales-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upsales-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upsales.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.upsales.com/hc/en-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.upsales.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.upsales.com (404 responses).
  evidence:
  - status: 404
    url: https://api.upsales.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Upsales provides a comprehensive AI‑driven sales platform that helps businesses identify new opportunities, expand existing accounts, and prioritize deals. The solution offers end‑to‑end tools for lead recommendation, pipeline management, and performance analytics, empowering sales teams to close more deals efficiently. Founded in Sweden, Upsales serves customers across Europe and integrates with major CRMs and marketing tools.
image: https://www.upsales.com/api/media/file/og-home-2.png
layout: provider
modified: '2026-10-15'
name: Upsales
nav: Providers
network: true
overview: 'Upsales is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Artificial Intelligence, CRM, and Software-as-a-Service.


  Upsales'' developer surface includes pricing, support, engineering blog, documentation, and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Upsales Domain Security
  slug: upsales-domain-security
  summary_line: TLSv1.3 · DMARC
slug: upsales
tags:
- Company
- Sales
- Artificial Intelligence
- CRM
- Software-as-a-Service
website: https://upsales.com/
---
