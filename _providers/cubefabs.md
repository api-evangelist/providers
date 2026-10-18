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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cubefabs/refs/heads/main/well-known/cubefabs-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cubefabs-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cubefabs/refs/heads/main/well-known/cubefabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cubefabs-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cubefabs/refs/heads/main/hosts/cubefabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cubefabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cubefabs/refs/heads/main/vendors/cubefabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cubefabs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cubefabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cubefabs.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cubefabs.com/press
- group: other
  title: ''
  type: Leadership
  url: https://cubefabs.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cubefabs/refs/heads/main/security/cubefabs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cubefabs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cubefabs/refs/heads/main/security/cubefabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubefabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cubefabs.com
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.cubefabs.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CubeFabs is an industrial AI company building modular, AI‑driven micro‑fabrication factories for semiconductor and advanced material production. Based in Brooklyn, the firm leverages real‑time AI, computer vision, and robotics to create scalable, low‑cost chip fabs and next‑generation material manufacturing. The platform offers a cloud‑connected factory model, enabling rapid deployment of fab units worldwide, accelerating innovation in semiconductors, data‑center chips, automotive and aerospace components. CubeFabs aims to democratize advanced manufacturing through AI‑powered process optimization and modular hardware.
image: https://cdn.sanity.io/images/vpe6kkg1/production/db7570ba7224680ad8d289f7adefd605778d00de-1200x630.png?rect=40,0,1120,630&w=1600&h=900&fit=max&auto=format
layout: provider
modified: '2026-10-11'
name: Cubefabs
nav: Providers
network: true
overview: Cubefabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Manufacturing, Semiconductors, and Modular.
random_paper: 13
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Cubefabs Domain Security
  slug: cubefabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cubefabs Vulnerability Disclosure
  slug: cubefabs-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cubefabs
tags:
- Company
- Artificial Intelligence
- Manufacturing
- Semiconductors
- Modular
website: https://cubefabs.com
---
