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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/office-of-the-surveyor-general-of-the-federation-osgof/hosts/office-of-the-surveyor-general-of-the-federation-osgof-hosts.yml
  title: ''
  type: Hosts
  url: hosts/office-of-the-surveyor-general-of-the-federation-osgof-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://osgof.gov.ng/privacy-policy-2/
- group: other
  title: ''
  type: Leadership
  url: https://osgof.gov.ng/leadership/
- group: auth
  href: https://artifacts.apis.io/office-of-the-surveyor-general-of-the-federation-osgof/security/office-of-the-surveyor-general-of-the-federation-osgof-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/office-of-the-surveyor-general-of-the-federation-osgof-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osgof.gov.ng/
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were discoverable on the provider's website.
  evidence:
  - status: 404
    url: https://osgof.gov.ng/openapi.json
  - status: 404
    url: https://osgof.gov.ng/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: The Office of the Surveyor General of the Federation (OSGOF) is a governmental agency responsible for overseeing land surveying, mapping, and geospatial data management across the Federation. It provides authoritative geographic information, maintains cadastral records, and supports infrastructure planning, environmental monitoring, and public policy with accurate spatial data. The agency offers APIs for accessing land parcel data, survey results, and geospatial services to developers, researchers, and other government bodies, fostering transparency and innovation in the public sector.
image: https://osgof.gov.ng/wp-content/uploads/2025/01/LOGO-3.png
layout: provider
modified: '2026-10-23'
name: Office of the Surveyor General of the Federation (OSGOF)
nav: Providers
network: true
overview: Office of the Surveyor General of the Federation (OSGOF) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Geospatial, Mapping, LandSurvey, and Data.
random_paper: 12
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/office-of-the-surveyor-general-of-the-federation-osgof/office-of-the-surveyor-general-of-the-federation-osgof-2026-11-03T140529.png
security:
- kind: domain-security
  name: Office Of The Surveyor General Of The Federation Osgof Domain Security
  slug: office-of-the-surveyor-general-of-the-federation-osgof-domain-security
  summary_line: TLSv1.3
slug: office-of-the-surveyor-general-of-the-federation-osgof
tags:
- Government
- Geospatial
- Mapping
- LandSurvey
- Data
website: https://osgof.gov.ng/
---
