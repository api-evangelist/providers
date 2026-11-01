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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation redirects from silversentinel.ai to verifydial.com but no machine-readable spec was found.
  name: VerifyDial API
  slug: verifydial-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/silversentinel-ai/hosts/silversentinel-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/silversentinel-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/silversentinel-ai/vendors/silversentinel-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/silversentinel-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/silversentinel-ai/security/silversentinel-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/silversentinel-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://silversentinel.ai
coverage:
  checked: '2026-10-25'
  detail: OpenAPI spec URLs on api.silversentinel.ai redirect to verifydial.com and return no spec.
  evidence:
  - status: 301
    url: https://api.silversentinel.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Alpharank, operating under the slug silversentinel-ai, is listed in the API Evangelist harvest as a venture‑backed company. Public information about its products, services, or domain is currently unavailable. The company appears to be associated with the VerifyDial platform based on a redirect from its claimed website, but no direct evidence confirms ownership of that domain.
layout: provider
modified: '2026-10-25'
name: Alpharank
nav: Providers
network: true
overview: Alpharank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Venture-backed, API, and Startup.
random_paper: 22
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Silversentinel Ai Domain Security
  slug: silversentinel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: silversentinel-ai
tags:
- Company
- FinTech
- Venture-backed
- API
- Startup
website: https://silversentinel.ai
---
