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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/constrafor/refs/heads/main/plans/constrafor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/constrafor-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/constrafor/refs/heads/main/hosts/constrafor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constrafor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/constrafor/refs/heads/main/vendors/constrafor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constrafor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.constrafor.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.constrafor.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.constrafor.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.constrafor.com/knowledge/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/constrafor/refs/heads/main/security/constrafor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constrafor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.constrafor.com/
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered despite probing known hosts and documentation pages.
  evidence:
  - status: 404
    url: https://api.constrafor.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Constrafor provides a construction‑focused platform that streamlines payments, risk management, and back‑office operations for general contractors and subcontractors. Their SaaS suite includes early‑pay financing, contract management, invoicing, and compliance tools, helping firms accelerate cash flow and reduce administrative overhead while ensuring regulatory adherence.
layout: provider
modified: '2026-10-10'
name: Constrafor
nav: Providers
network: true
overview: 'Constrafor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Fintech, Software-as-a-Service, Payments, and Risk Management.


  Constrafor''s developer surface includes pricing, getting-started guide, and 7 more developer resources.'
plans:
- name: Constrafor Plans Pricing
  plan_count: 7
  slug: constrafor-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constrafor Domain Security
  slug: constrafor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: constrafor
tags:
- Construction
- Fintech
- Software-as-a-Service
- Payments
- Risk Management
- Company
website: https://www.constrafor.com/
---
