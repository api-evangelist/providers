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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/scientist-com/well-known/scientist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scientist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/scientist-com/hosts/scientist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scientist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/scientist-com/vendors/scientist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scientist-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.scientist.com/legal-notices
- group: start
  title: ''
  type: Login
  url: https://backoffice.scientist.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scientist-hq
- group: auth
  href: https://artifacts.apis.io/scientist-com/security/scientist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scientist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scientist.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.scientist.com/platform
- group: company
  title: ''
  type: Blog
  url: https://www.scientist.com/innovation-hub-search?2_type_equal=%5B%22Blog%22%5D
- group: operate
  title: ''
  type: Support
  url: https://www.scientist.com/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://www.scientist.com/demo
coverage:
  checked: '2026-10-12'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 404
    url: https://api.scientist.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Scientist.com provides a digital backbone for life science research, offering a unified platform that supports the full drug development lifecycle—from discovery and preclinical studies through clinical trials, manufacturing, and commercial operations. The platform integrates vendor networks, guided buying, workflow automation, regulatory compliance, and AI-driven insights, enabling organizations to source, manage, and scale external research efficiently.
layout: provider
modified: '2026-10-12'
name: Scientist.com
nav: Providers
network: true
overview: 'Scientist.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Platform, Artificial Intelligence, and Research.


  Scientist.com''s developer surface includes documentation, engineering blog, support, getting-started guide, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 5.3
  previous_composite: 15.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scientist Com Domain Security
  slug: scientist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scientist-com
tags:
- Company
- Life Sciences
- Platform
- Artificial Intelligence
- Research
website: https://www.scientist.com
---
