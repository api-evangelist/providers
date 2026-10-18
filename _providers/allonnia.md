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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allonnia/refs/heads/main/llms/allonnia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allonnia-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allonnia/refs/heads/main/hosts/allonnia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allonnia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allonnia/refs/heads/main/vendors/allonnia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allonnia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allonnia.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allonnia.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://allonnia.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://allonnia.com/newsroom/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Allonnia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allonnia/refs/heads/main/security/allonnia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allonnia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allonnia.com/
coverage:
  checked: '2026-10-05'
  detail: No OpenAPI or other machine-readable contract found at https://api.allonnia.com/openapi.json (HTTP 000).
  evidence:
  - status: 0
    url: https://api.allonnia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Allonnia is a biotechnology and critical materials technology company focused on accelerating the deployment of innovative solutions for the life sciences and sustainable mining sectors. It provides data-driven platforms, advanced materials, and consulting services to help organizations navigate complex regulatory landscapes, improve operational efficiency, and drive sustainable growth. Founded to bridge the gap between scientific research and commercial application, Allonnia leverages AI-driven analytics and a global network of partners to deliver impactful results across the biotech and mining industries.
image: https://allonnia.com/wp-content/uploads/2026/07/allonnia-opengraph-compressed.png
layout: provider
modified: '2026-09-24'
name: Allonnia
nav: Providers
network: true
overview: 'Allonnia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Materials, Sustainability, and Artificial Intelligence.


  Allonnia''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 0.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Allonnia Domain Security
  slug: allonnia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allonnia
tags:
- Company
- Biotechnology
- Materials
- Sustainability
- Artificial Intelligence
- Mining
website: https://allonnia.com/
---
