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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boltsolutions/refs/heads/main/hosts/boltsolutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boltsolutions-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boltsolutions/refs/heads/main/vendors/boltsolutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boltsolutions-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boltsolutions/refs/heads/main/security/boltsolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boltsolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boltsolutions.org
- group: docs
  title: ''
  type: Documentation
  url: https://boltsolutions.org/about
- group: start
  title: ''
  type: GettingStarted
  url: https://boltsolutions.org/start-a-project
- group: commercial
  title: ''
  type: Pricing
  url: https://boltsolutions.org/pay
coverage:
  checked: '2026-10-02'
  detail: The provider's website offers HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://boltsolutions.org/packages
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bolt Solutions is a digital agency founded in 2025 that builds fast websites and drives growth for brands. It offers packages, client case studies, and a focus on SEO, conversion gains, and rapid development, positioning itself as a small‑agency with big‑agency results for founders seeking fast, scalable digital experiences.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/ebd29c1b-4648-4a77-9c5e-ab3096d9538a/id-preview-8bbe6f58--41a506bf-c8e4-4409-ab1c-8ab99ab04d63.lovable.app-1779167833677.png
layout: provider
modified: '2026-10-02'
name: Boltsolutions
nav: Providers
network: true
overview: 'Boltsolutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Agency, Web Development, SEO, and Growth.


  Boltsolutions'' developer surface includes documentation, getting-started guide, pricing, and 4 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boltsolutions Domain Security
  slug: boltsolutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boltsolutions
tags:
- Company
- Digital Agency
- Web Development
- SEO
- Growth
website: https://boltsolutions.org
---
