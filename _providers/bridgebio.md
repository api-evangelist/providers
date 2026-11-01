---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/bridgebio/llms/bridgebio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bridgebio-llms.txt
- group: other
  href: https://artifacts.apis.io/bridgebio/hosts/bridgebio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgebio-hosts.yml
- group: other
  href: https://artifacts.apis.io/bridgebio/vendors/bridgebio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridgebio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bridgebio.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://bridgebio.com/patients/support
- group: company
  title: ''
  type: Newsroom
  url: https://investor.bridgebio.com/news/default.aspx
- group: auth
  href: https://artifacts.apis.io/bridgebio/security/bridgebio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgebio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgebio.com/
coverage:
  checked: '2026-10-29'
  detail: BridgeBio's website and sitemap contain no API documentation or machine-readable contract endpoints.
  evidence:
  - status: 404
    url: https://bridgebio.com/openapi.json
  - status: 404
    url: https://bridgebio.com/asyncapi.yaml
  - status: 404
    url: https://investor.bridgebio.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Discover BridgeBio, a unique biotechnology company advancing genetic medicines via a decentralized model linking expert teams and shared infrastructure. Learn how BridgeBio advances precision medicines for genetic diseases through innovative science, strong leadership, and a patient‑first approach.
image: https://bridgebio.com/static/img/og-fallback.png?w=1200&h=628&fit=crop&q=60&fm=jpg
layout: provider
modified: '2026-10-28'
name: BridgeBio
nav: Providers
network: true
overview: 'BridgeBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Genetics, Precision Medicine, Drug Development, and Healthcare.


  BridgeBio''s developer surface includes support and 7 more developer resources.'
plans:
- name: Bridgebio Plans Pricing
  plan_count: 0
  slug: bridgebio-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Bridgebio Rate Limits
  slug: bridgebio-rate-limits
scopes:
- name: Bridgebio Scopes
  scope_count: 0
  slug: bridgebio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bridgebio Authentication
  slug: bridgebio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bridgebio Domain Security
  slug: bridgebio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridgebio
tags:
- Biotechnology
- Genetics
- Precision Medicine
- Drug Development
- Healthcare
website: https://bridgebio.com/
---
