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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudpay.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudpay/refs/heads/main/well-known/cloudpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudpay-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudpay/refs/heads/main/hosts/cloudpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudpay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudpay/refs/heads/main/vendors/cloudpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudpay-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudpay.com/terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.cloudpay.com/resources/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudpay/refs/heads/main/security/cloudpay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudpay-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudpay/refs/heads/main/security/cloudpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudpay.com/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was discovered on any host.
  evidence:
  - status: 0
    url: https://api.cloudpay.com/openapi.json
  - status: 404
    url: https://trust.cloudpay.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: CloudPay provides a global payroll and payments platform that automates payroll processing, global payments, and on‑demand pay solutions for midsize businesses. Their SaaS offering includes API‑driven integrations with major HCM systems, advanced AI‑powered pay automation, and compliance tools, enabling companies to manage worldwide payroll, tax, and benefits efficiently.
image: https://www.cloudpay.com/app/uploads/2024/01/home-page-feature-image1.webp
layout: provider
modified: '2026-10-09'
name: CloudPay
nav: Providers
network: true
overview: 'CloudPay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Global Payroll, Payments, Pay On-Demand, Managed Service, and HCM Integrations.


  CloudPay''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudpay Domain Security
  slug: cloudpay-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cloudpay Trust Center
  slug: cloudpay-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018
slug: cloudpay
tags:
- Global Payroll
- Payments
- Pay On-Demand
- Managed Service
- HCM Integrations
- Cloud-based Payroll
website: https://www.cloudpay.com/
---
