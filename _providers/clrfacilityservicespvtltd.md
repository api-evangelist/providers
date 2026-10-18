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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clrfacilityservicespvtltd/refs/heads/main/hosts/clrfacilityservicespvtltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clrfacilityservicespvtltd-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clrservices.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clrservices.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clrfacilityservicespvtltd/refs/heads/main/security/clrfacilityservicespvtltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clrfacilityservicespvtltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clrservices.com
coverage:
  checked: '2026-10-09'
  detail: The company provides facility management services and does not expose a developer program or API.
  evidence:
  - status: 200
    url: https://clrservices.com
  reason: not-a-software-company
  state: none
created: '2026-10-09'
description: CLR Facility Services Private Limited provides integrated facility management solutions across multiple industries including healthcare, aviation, manufacturing, and retail. Their services span IFM, technical services, business support, aviation services, production support, and sustainable impact initiatives such as circular economy and renewable energy. The company emphasizes ESG pledges, corporate governance, and smart building technologies, offering comprehensive facility management and consulting.
image: https://clrservices.com/wp-content/uploads/2024/08/experience.png
layout: provider
modified: '2026-10-09'
name: Clrfacilityservicespvtltd
nav: Providers
network: true
overview: Clrfacilityservicespvtltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Facility Management, Integrated Services, ESG, Smart Buildings, and India.
random_paper: 6
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
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
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Clrfacilityservicespvtltd Domain Security
  slug: clrfacilityservicespvtltd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clrfacilityservicespvtltd
tags:
- Facility Management
- Integrated Services
- ESG
- Smart Buildings
- India
website: https://clrservices.com
---
