---
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/inherentlaboratories-com/authentication/inherentlaboratories-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inherentlaboratories-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/inherentlaboratories-com/hosts/inherentlaboratories-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inherentlaboratories-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/inherentlaboratories-com/vendors/inherentlaboratories-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inherentlaboratories-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inherentlabs.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/github-cli/github-cli/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inherentlaboratories.com/
- group: auth
  href: https://artifacts.apis.io/inherentlaboratories-com/security/inherentlaboratories-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inherentlaboratories-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.inherentlaboratories.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.inherentlaboratories.com/mcp
  - status: 200
    url: http://www.inherentlaboratories.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Inherent Labs provides a recursively self‑improving AI platform that discovers new knowledge. The site describes itself as a system that continuously improves to uncover information, positioning itself in the AI research and knowledge discovery space.
image: https://inherentlabs.ai/og-image.png
layout: provider
modified: '2026-10-25'
name: Inherent
nav: Providers
network: true
overview: 'Inherent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, KnowledgeDiscovery, Platform, and SelfImproving.


  Inherent''s developer surface includes authentication, getting-started guide, documentation, and 5 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Inherentlaboratories Com Authentication
  slug: inherentlaboratories-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Inherentlaboratories Com Domain Security
  slug: inherentlaboratories-com-domain-security
  summary_line: TLSv1.3
slug: inherentlaboratories-com
tags:
- Company
- AI
- KnowledgeDiscovery
- Platform
- SelfImproving
website: http://www.inherentlaboratories.com
---
