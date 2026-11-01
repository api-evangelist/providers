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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/larksuite/hosts/larksuite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/larksuite-hosts.yml
- group: other
  href: https://artifacts.apis.io/larksuite/vendors/larksuite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/larksuite-vendors.yml
- group: build
  href: https://artifacts.apis.io/larksuite/packages/larksuite-packages.yml
  title: ''
  type: SDKs
  url: packages/larksuite-packages.yml
- group: build
  href: https://artifacts.apis.io/larksuite/packages/larksuite-packages.yml
  title: ''
  type: Packages
  url: packages/larksuite-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.larksuite.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/larksuite
- group: auth
  href: https://artifacts.apis.io/larksuite/security/larksuite-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/larksuite-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/larksuite/security/larksuite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/larksuite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.larksuite.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.larksuite.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Lark offers a productivity superapp that combines team chat, video meetings, document editing, workflow automation, and knowledge bases into a single platform. It is designed for organizations of all sizes that need integrated collaboration tools for internal teams, frontline operations, and global work across regions and languages.
image: https://p16-hera-sg.larksuitecdn.com/tos-alisg-i-hn4qzgxq2n-sg/589f47191ffc4b69976865b0d3df6906.jpeg~tplv-hn4qzgxq2n-image-v1:0:0.image
layout: provider
modified: '2026-10-27'
name: Lark
nav: Providers
network: true
overview: 'Lark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Team Collaboration, Productivity, No-code Workflow, Global Collaboration, and Enterprise Software.


  Lark''s developer surface includes documentation and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Larksuite Domain Security
  slug: larksuite-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Larksuite Trust Center
  slug: larksuite-trust-center
  summary_line: trust center published
slug: larksuite
tags:
- Team Collaboration
- Productivity
- No-code Workflow
- Global Collaboration
- Enterprise Software
website: https://www.larksuite.com/
---
