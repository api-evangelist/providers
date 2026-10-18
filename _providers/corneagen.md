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
api_count: 1
apis:
- description: API for CorneaGen services (no public documentation found)
  name: CorneaGen API
  slug: corneagen-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corneagen/refs/heads/main/hosts/corneagen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corneagen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corneagen/refs/heads/main/vendors/corneagen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corneagen-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corneagen.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corneagen.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CorneaGen
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corneagen/refs/heads/main/security/corneagen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corneagen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corneagen.com/
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec found on api.corneagen.com or corneagen.com.
  evidence:
  - status: 404
    url: https://api.corneagen.com/openapi.json
  - status: 403
    url: https://corneagen.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CorneaGen provides a comprehensive surgeon portal offering corneal tissue services, products, and educational resources. The platform enables eye surgeons to request tissue, access product information, view reimbursement details, and engage with training materials. It also includes regulatory information, adverse reaction reporting, and a range of corneal surgical solutions such as DSAEK, DMEK, and pre‑loaded grafts, supporting ophthalmic professionals worldwide.
layout: provider
modified: '2026-10-11'
name: CorneaGen
nav: Providers
network: true
overview: CorneaGen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Ophthalmology, Surgery, and Tissue.
random_paper: 0
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corneagen Domain Security
  slug: corneagen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corneagen
tags:
- Company
- Healthcare
- Ophthalmology
- Surgery
- Tissue
website: https://corneagen.com/
---
