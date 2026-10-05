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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: AuditFile provides API access to its audit software platform. Documentation is available at the pricing page, but no machine‑readable contract was found.
  name: AuditFile API
  slug: auditfile-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/auditfile/refs/heads/main/plans/auditfile-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auditfile-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://auditfile.com/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auditfile/refs/heads/main/hosts/auditfile-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auditfile-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auditfile/refs/heads/main/vendors/auditfile-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auditfile-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://auditfile.com/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AuditFile
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auditfile/refs/heads/main/security/auditfile-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/auditfile-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auditfile/refs/heads/main/security/auditfile-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auditfile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auditfile.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://auditfile.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auditfile.com/
- group: start
  title: ''
  type: Login
  url: https://auditfile.com/signin
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was discovered at any host.
  evidence:
  - status: failed
    url: https://api.auditfile.com/openapi.json
  - status: 404
    url: https://auditfile.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: AuditFile provides secure, cloud‑based audit software for CPA firms, combining AI‑enabled workflows, risk assessment, workpapers, reporting, and client portal features. Founded in 2011, AuditFile pioneered cloud audit and continues to innovate with patented AI tools, offering integrations with popular accounting platforms and a suite of products for modern audit practices.
layout: provider
modified: '2026-09-26'
name: AuditFile
nav: Providers
network: true
overview: 'AuditFile publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Audit, Cloud, Artificial Intelligence, and CPA.


  AuditFile''s developer surface includes support, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Auditfile Plans Pricing
  plan_count: 1
  slug: auditfile-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auditfile Domain Security
  slug: auditfile-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Auditfile Trust Center
  slug: auditfile-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: auditfile
tags:
- Accounting
- Audit
- Cloud
- Artificial Intelligence
- CPA
website: https://auditfile.com/
---
