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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation for Avarobotics robots and platform
  name: Avarobotics API
  slug: avarobotics-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avarobotics/refs/heads/main/llms/avarobotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avarobotics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avarobotics/refs/heads/main/hosts/avarobotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avarobotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avarobotics/refs/heads/main/vendors/avarobotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avarobotics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avarobotics.com/terms-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.avarobotics.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avarobotics.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.avarobotics.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.avarobotics.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.avarobotics.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avarobotics/refs/heads/main/security/avarobotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avarobotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avarobotics.com
coverage:
  checked: 2026-09-26
  detail: Documentation pages are HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files.
  evidence:
  - status: 200
    url: https://www.avarobotics.com/documents
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Ava Robotics develops telepresence and mobile base robots for workplace and healthcare environments. Their technology enables remote experts to interact with on‑site personnel, improving safety, efficiency, and collaboration across industries such as hospitals, clean rooms, and hybrid workspaces. The company offers a suite of robotic solutions, including the Ava Telepresence robot, mobile base platforms, and integrated software for remote operation and monitoring.
image: https://static.wixstatic.com/media/90f1de_c6f2b8bde1c54d9bbec1e088dd64ddae%7Emv2.png/v1/fit/w_2500,h_1330,al_c/90f1de_c6f2b8bde1c54d9bbec1e088dd64ddae%7Emv2.png
layout: provider
modified: '2026-09-26'
name: Avarobotics
nav: Providers
network: true
overview: 'Avarobotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Telepresence, Healthcare, Automation, and Company.


  Avarobotics'' developer surface includes changelog, engineering blog, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avarobotics Domain Security
  slug: avarobotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avarobotics
tags:
- Robotics
- Telepresence
- Healthcare
- Automation
- Company
website: https://www.avarobotics.com
---
