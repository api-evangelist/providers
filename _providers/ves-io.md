---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Volterra (F5 Distributed Cloud Services)
  name: Volterra API
  slug: volterra-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/ves-io/well-known/ves-io-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ves-io-www-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.f5.com/products/distributed-cloud-services
- group: agent
  href: https://artifacts.apis.io/ves-io/well-known/ves-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ves-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/ves-io/hosts/ves-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ves-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/ves-io/vendors/ves-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ves-io-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.f5.com/support
- group: auth
  title: ''
  type: Security
  url: https://www.f5.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.f5.com/company/policies/privacy-compliance-and-practices
- group: company
  title: ''
  type: Newsroom
  url: https://www.f5.com/company/news
- group: other
  title: ''
  type: Leadership
  url: https://www.f5.com/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.f5.com/company/blog
- group: auth
  href: https://artifacts.apis.io/ves-io/security/ves-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ves-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ves-io/security/ves-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ves-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ves.io/
coverage:
  checked: '2026-10-28'
  detail: Documentation provides HTML API reference but no OpenAPI/AsyncAPI/GraphQL spec is available.
  evidence:
  - status: 200
    url: https://clouddocs.f5.com/api/irules-lx/APIReference.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Volterra (brand of F5 Distributed Cloud Services) provides an edge cloud platform that enables developers and enterprises to deploy, secure, and manage applications and services at the network edge. It offers capabilities such as edge compute, networking, security, and observability, integrating with multi‑cloud environments to deliver low‑latency, high‑performance experiences for users worldwide. The platform supports APIs for automation, policy enforcement, and service orchestration across distributed edge locations.
image: https://cdn.studio.f5.com/images/k6fem79d/translations-production/f09892d813aa6e963305be4ddb37e72c6286e7be-1200x675.png
layout: provider
modified: '2026-10-28'
name: Volterra
nav: Providers
network: true
overview: 'Volterra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edge Computing, Cloud Platform, Security, and API Management.


  Volterra''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.9
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ves-io/ves-io-2026-11-03T145748.png
security:
- kind: domain-security
  name: Ves Io Domain Security
  slug: ves-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ves Io Trust Center
  slug: ves-io-trust-center
  summary_line: FedRAMP
slug: ves-io
tags:
- Company
- Edge Computing
- Cloud Platform
- Security
- API Management
website: https://www.ves.io/
---
