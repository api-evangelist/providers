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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aistech/refs/heads/main/security/aistech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aistech-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aistech/refs/heads/main/llms/aistech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aistech-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aistechspace.com
- group: company
  title: ''
  type: Blog
  url: https://aistechspace.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aistechspace.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aistechspace.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://aistechspace.com/cookie-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://aistechspace.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://aistechspace.com/careers/
coverage:
  checked: 2026-09-21
  detail: The provider's website does not expose any machine‑readable API specification such as OpenAPI, GraphQL SDL, or AsyncAPI.
  evidence:
  - status: 200
    url: https://aistechspace.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: Aistech Space is a European leader providing proprietary high‑resolution thermal imagery and geospatial intelligence from its own satellite constellation. The company captures the human activity layer of Earth, delivering on‑demand thermal data for security, defense, infrastructure monitoring, maritime, natural hazards, and agriculture, enabling decisive action across industries.
layout: provider
modified: '2026-09-21'
name: Aistech
nav: Providers
network: true
overview: 'Aistech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Thermal Imagery, and Geospatial Intelligence.


  Aistech''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.7
    operational_transparency: 0.0
  previous_composite: 10.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aistech Domain Security
  slug: aistech-domain-security
  summary_line: TLSv1.3
slug: aistech
tags:
- Company
- Space
- Satellite
- Thermal Imagery
- Geospatial Intelligence
website: https://aistechspace.com
---
