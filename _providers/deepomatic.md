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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Deepomatic platform API (documentation restricted)
  name: Deepomatic API
  slug: deepomatic-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/deepomatic/llms/deepomatic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepomatic-llms.txt
- group: agent
  href: https://artifacts.apis.io/deepomatic/well-known/deepomatic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deepomatic-well-known.yml
- group: other
  href: https://artifacts.apis.io/deepomatic/hosts/deepomatic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepomatic-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepomatic/vendors/deepomatic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepomatic-vendors.yml
- group: build
  href: https://artifacts.apis.io/deepomatic/packages/deepomatic-packages.yml
  title: ''
  type: SDKs
  url: packages/deepomatic-packages.yml
- group: build
  href: https://artifacts.apis.io/deepomatic/packages/deepomatic-packages.yml
  title: ''
  type: Packages
  url: packages/deepomatic-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepomatic.com/legal/legal-notice
- group: start
  title: ''
  type: Login
  url: https://api.deepomatic.com/accounts/login/
- group: company
  title: ''
  type: Blog
  url: https://deepomatic.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deepomatic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Deepomatic
- group: auth
  href: https://artifacts.apis.io/deepomatic/security/deepomatic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepomatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepomatic.com
coverage:
  checked: '2026-10-22'
  detail: Documentation is restricted and provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.deepomatic.com/restricted
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Deepomatic provides computer‑vision AI solutions that enable enterprises to automate visual quality inspection and field operations. Their platform offers real‑time image analysis, defect detection, and workflow integration, helping customers reduce errors, improve efficiency, and scale visual intelligence across industries. Deepomatic was acquired by IQGeo, extending its capabilities into network intelligence.
layout: provider
modified: '2026-10-22'
name: Deepomatic
nav: Providers
network: true
overview: 'Deepomatic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Computer Vision, Artificial Intelligence, Automation, Enterprise, and Imaging.


  Deepomatic''s developer surface includes engineering blog, documentation, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepomatic Domain Security
  slug: deepomatic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deepomatic
tags:
- Computer Vision
- Artificial Intelligence
- Automation
- Enterprise
- Imaging
website: https://deepomatic.com
---
