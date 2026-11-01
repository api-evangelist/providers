---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/xwiki/well-known/xwiki-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xwiki-well-known.yml
- group: other
  href: https://artifacts.apis.io/xwiki/hosts/xwiki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xwiki-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xwiki.com/en/company/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://help.xwiki.com/en
- group: commercial
  title: ''
  type: Pricing
  url: https://xwiki.com/en/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://xwiki.com/en/company/Newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://xwiki.com/en/company/team/
- group: company
  title: ''
  type: Blog
  url: https://xwiki.com/en/Blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.xwiki.com/
- group: auth
  href: https://artifacts.apis.io/xwiki/security/xwiki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xwiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xwiki.com/
coverage:
  checked: '2026-10-27'
  detail: XWiki provides REST documentation but no machine‑readable OpenAPI/AsyncAPI spec was found.
  evidence:
  - status: 404
    url: https://www.xwiki.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: XWiki provides an open-source enterprise wiki and knowledge management platform that enables teams to create, collaborate on, and share structured content. The platform offers customizable applications, integrations, and extensions for use cases such as documentation, intranets, knowledge bases, and digital workplaces. XWiki is available as self‑hosted software, cloud services, and enterprise editions, supporting open standards and extensibility through APIs and plugins.
image: https://xwiki.com/en/download/Main/WebHome/XWiki-create-update-share-collaborate.jpg
layout: provider
modified: '2026-10-26'
name: XWiki
nav: Providers
network: true
overview: 'XWiki is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open-Source, Enterprise, Wiki, and Knowledge-Management.


  XWiki''s developer surface includes support, pricing, engineering blog, documentation, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Xwiki Domain Security
  slug: xwiki-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: xwiki
tags:
- Company
- Open-Source
- Enterprise
- Wiki
- Knowledge-Management
- Collaboration
website: https://xwiki.com/
---
