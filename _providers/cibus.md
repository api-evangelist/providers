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
- description: Cibus provides an API for agricultural biotechnology data and services. Documentation is not publicly machine‑readable.
  name: Cibus API
  slug: cibus-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cibus/refs/heads/main/hosts/cibus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cibus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cibus/refs/heads/main/vendors/cibus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cibus-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cibus.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cibus.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cibus/refs/heads/main/security/cibus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cibus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cibus.com/
coverage:
  checked: '2026-10-08'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract was found despite probing known hosts.
  evidence:
  - status: 200
    url: https://www.cibus.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Cibus is an agricultural biotechnology company focused on precision breeding to develop more resilient, sustainable, and vigorous crops. By leveraging nature‑identical traits and advanced gene‑editing technologies, Cibus accelerates the creation of seeds with improved yield, stress tolerance, and reduced chemical inputs, helping farmers meet the challenges of a changing climate and growing global food demand.
image: https://cdn.prod.website-files.com/6878b7b8057f5d7e488ae4bf/68b82e1f995e0b9d14bc6a9a_og_image.jpg
layout: provider
modified: '2026-10-08'
name: Cibus
nav: Providers
network: true
overview: Cibus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Biotechnology, PrecisionBreeding, and Sustainable Food.
random_paper: 6
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cibus Domain Security
  slug: cibus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cibus
tags:
- Company
- Agriculture
- Biotechnology
- PrecisionBreeding
- Sustainable Food
website: https://www.cibus.com/
---
