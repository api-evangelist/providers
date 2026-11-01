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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Koofr provides cloud storage services.
  name: Koofr API
  slug: koofr-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/koofr/plans/koofr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/koofr-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/koofr/hosts/koofr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/koofr-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://koofr.eu/security/two-factor-authentication/
- group: start
  title: ''
  type: Login
  url: https://koofr.eu/login
- group: other
  title: ''
  type: Leadership
  url: https://koofr.eu/team/
- group: auth
  href: https://artifacts.apis.io/koofr/security/koofr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/koofr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koofr.eu/
- group: company
  title: ''
  type: Blog
  url: https://koofr.eu/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://koofr.eu/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://koofr.eu/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://koofr.eu/privacy
- group: operate
  title: ''
  type: Support
  url: https://koofr.eu/help
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: could-not-resolve
    url: https://api.koofr.eu/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Koofr provides a secure, privacy‑focused cloud storage service based in the European Union. It offers unified access to files across multiple devices and integrates with popular services like Instagram, Facebook, and Microsoft Office. Users get 10 GB of free storage forever, with client‑side encryption, two‑factor authentication, and GDPR‑compliant data handling. The platform includes features such as secure sharing links, a vault for sensitive files, and desktop and mobile apps for Windows, macOS, Linux, iOS, Android, and Huawei devices.
image: https://koofr.eu/static/images/koofr_home_preview.jpg
layout: provider
modified: '2026-10-28'
name: Koofr
nav: Providers
network: true
overview: 'Koofr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, Privacy, GDPR, File Sync, and European Union.


  Koofr''s developer surface includes engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Koofr Plans Pricing
  plan_count: 9
  slug: koofr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Koofr Rate Limits
  slug: koofr-rate-limits
scopes:
- name: Koofr Scopes
  scope_count: 0
  slug: koofr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Koofr Authentication
  slug: koofr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Koofr Domain Security
  slug: koofr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: koofr
tags:
- Cloud Storage
- Privacy
- GDPR
- File Sync
- European Union
- Company
website: https://koofr.eu/
---
