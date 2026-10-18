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
- description: Swvl provides on‑demand bus transportation APIs accessible via their developer portal.
  name: Swvl API
  slug: swvl-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/swvl/refs/heads/main/llms/swvl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swvl-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/swvl/refs/heads/main/hosts/swvl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swvl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/swvl/refs/heads/main/vendors/swvl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swvl-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/swvl/refs/heads/main/packages/swvl-packages.yml
  title: ''
  type: SDKs
  url: packages/swvl-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/swvl/refs/heads/main/packages/swvl-packages.yml
  title: ''
  type: Packages
  url: packages/swvl-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swvl.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swvl.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.swvl.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swvl
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swvl/refs/heads/main/security/swvl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swvl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swvl.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.swvl.com/partner-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://www.swvl.com/request-demo
- group: company
  title: ''
  type: Blog
  url: https://www.swvl.com/blog
coverage:
  checked: '2026-10-13'
  detail: Swvl's developer portal and API reference pages provide only HTML docs with no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files discovered.
  evidence:
  - status: 0
    url: https://api.swvl.com/openapi.json
  - status: 0
    url: https://api.swvl.com/openapi.yaml
  - status: 0
    url: https://api.swvl.com/swagger.json
  - status: 0
    url: https://api.swvl.com/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Swvl provides on‑demand bus transportation solutions for commuters, students, and enterprises across multiple countries. The platform offers a rider app for booking and tracking rides, a partner portal for fleet operators, and an admin dashboard for managing operations. Swvl’s services include Mobility‑as‑a‑Service, software solutions for fleet dispatch, and customizable transit options for businesses, schools, and events.
image: https://cdn.prod.website-files.com/6874bcb26cc8479274177d70/68a8a269b7ef7da9ace5c93c_Media_kit-3.png
layout: provider
modified: '2026-10-13'
name: Swvl
nav: Providers
network: true
overview: 'Swvl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobility, Transportation, On‑Demand, Fleet Management, and B2B Solutions.


  Swvl''s developer surface includes getting-started guide, engineering blog, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.5
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
    developer_ergonomics: 31.0
    discoverability: 66.1
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
  name: Swvl Domain Security
  slug: swvl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: swvl
tags:
- Mobility
- Transportation
- On‑Demand
- Fleet Management
- B2B Solutions
website: https://www.swvl.com
---
