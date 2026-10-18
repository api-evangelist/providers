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
- description: API for Crimson Education services (admissions consulting).
  name: Crimson Education API
  slug: crimson-education-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crimson/refs/heads/main/hosts/crimson-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crimson-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crimson/refs/heads/main/vendors/crimson-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crimson-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crimsoneducation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crimson/refs/heads/main/security/crimson-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crimson-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crimsoneducation.org
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.crimsoneducation.org/openapi.json
  - status: 200
    url: https://app.crimsoneducation.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Crimson Education is a global education consultancy that helps students gain admission to top universities worldwide. It offers services including college admissions counseling, test preparation, athletic recruitment, and graduate school consulting. The company operates a network of former admissions officers and Ivy League graduates, providing personalized guidance and resources to improve applicants’ chances at elite institutions.
image: https://a.storyblok.com/f/64062/1200x630/261c719537/crimson-website-share-image.jpg
layout: provider
modified: '2026-10-11'
name: Crimson
nav: Providers
network: true
overview: Crimson is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, College Admissions, Test Preparation, Consulting, and Global.
random_paper: 15
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crimson Domain Security
  slug: crimson-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crimson
tags:
- Education
- College Admissions
- Test Preparation
- Consulting
- Global
website: https://www.crimsoneducation.org
---
