---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GetKlo provides AI‑enhanced video editing tools and a cloud MCP platform.
  name: getklo
  slug: getklo
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/getklo-com/changelog/getklo-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getklo-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/getklo-com/authentication/getklo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getklo-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/getklo-com/llms/getklo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getklo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/getklo-com/hosts/getklo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getklo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getklo-com/vendors/getklo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getklo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://klo.mov/terms
- group: operate
  title: ''
  type: Support
  url: https://getklo.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klo.mov/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://klo.mov/changelog
- group: company
  title: ''
  type: Blog
  url: https://klo.mov/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://getklo.com/mcp
- group: auth
  href: https://artifacts.apis.io/getklo-com/security/getklo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getklo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://klo.mov/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec found on any discovered host.
  evidence:
  - status: 404
    url: https://api.getklo.com/openapi.json
  - status: 404
    url: https://api.klo.mov/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Klo (getklo.com) offers an AI‑powered video editing platform that lets users edit footage through conversational prompts. The service provides cloud‑based rendering, collaborative tools, and integrations for downloading edited videos via its API. It targets creators, marketers, and enterprises seeking fast, automated video production without traditional editing software.
image: https://getklo.com/og.jpg?v=3
layout: provider
modified: '2026-10-30'
name: getklo-com
nav: Providers
network: true
overview: 'getklo-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Editing, AI, Cloud Rendering, Collaboration, and Marketing.


  getklo-com''s developer surface includes changelog, authentication, support, engineering blog, getting-started guide, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 10
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
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getklo Com Authentication
  slug: getklo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Getklo Com Domain Security
  slug: getklo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getklo-com
tags:
- Video Editing
- AI
- Cloud Rendering
- Collaboration
- Marketing
website: https://klo.mov/
---
