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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API information not publicly documented.
  name: ASPRS API
  slug: asprs-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/american-society-for-photogrammetry-remote-sensing-asprs/hosts/american-society-for-photogrammetry-remote-sensing-asprs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/american-society-for-photogrammetry-remote-sensing-asprs-hosts.yml
- group: other
  href: https://artifacts.apis.io/american-society-for-photogrammetry-remote-sensing-asprs/vendors/american-society-for-photogrammetry-remote-sensing-asprs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/american-society-for-photogrammetry-remote-sensing-asprs-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://community.asprs.org/HigherLogic/Security/ImisRestLoginBounce.aspx?ReturnURL=https%3a%2f%2fcommunity.asprs.org%2fhome
- group: auth
  href: https://artifacts.apis.io/american-society-for-photogrammetry-remote-sensing-asprs/security/american-society-for-photogrammetry-remote-sensing-asprs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/american-society-for-photogrammetry-remote-sensing-asprs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.asprs.org
coverage:
  checked: '2026-10-26'
  detail: The provider's documentation pages are JavaScript‑rendered and no machine‑readable OpenAPI, GraphQL, AsyncAPI or WSDL files were found.
  evidence:
  - status: 200
    url: http://www.asprs.org
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: The American Society for Photogrammetry & Remote Sensing (ASPRS) is a professional association dedicated to advancing the science and technology of photogrammetry, remote sensing, and geospatial information. Founded in 1955, ASPRS provides standards, education, certification, and a community for professionals in surveying, mapping, and imaging. The organization hosts conferences, publishes research, and offers resources such as guidelines, best practices, and training programs to support the geospatial industry worldwide.
layout: provider
modified: '2026-10-26'
name: American Society for Photogrammetry & Remote Sensing (ASPRS)
nav: Providers
network: true
overview: American Society for Photogrammetry & Remote Sensing (ASPRS) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, Photogrammetry, Remote Sensing, Standards, and Education.
random_paper: 11
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/american-society-for-photogrammetry-remote-sensing-asprs/american-society-for-photogrammetry-remote-sensing-asprs-2026-11-03T120817.png
security:
- kind: domain-security
  name: American Society For Photogrammetry Remote Sensing Asprs Domain Security
  slug: american-society-for-photogrammetry-remote-sensing-asprs-domain-security
  summary_line: TLSv1.3
slug: american-society-for-photogrammetry-remote-sensing-asprs
tags:
- Geospatial
- Photogrammetry
- Remote Sensing
- Standards
- Education
website: http://www.asprs.org
---
