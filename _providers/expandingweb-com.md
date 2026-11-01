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
api_count: 1
apis:
- description: ExpandingWeb provides agentic commerce suite APIs documented at https://expandingweb.com/docs.
  name: ExpandingWeb API
  slug: expandingweb-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/expandingweb-com/hosts/expandingweb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/expandingweb-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://expandingweb.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.expandingweb.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://expandingweb.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marcinsdance
- group: docs
  title: ''
  type: Documentation
  url: https://expandingweb.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://expandingweb.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/expandingweb-com/security/expandingweb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/expandingweb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://expandingweb.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation is HTML without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://expandingweb.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: 'expandingweb-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://expandingweb.com/img/og-agentic.png
layout: provider
modified: '2026-10-30'
name: expandingweb-com
nav: Providers
network: true
overview: 'expandingweb-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  expandingweb-com''s developer surface includes support, documentation, getting-started guide, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Expandingweb Com Domain Security
  slug: expandingweb-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: expandingweb-com
tags:
- Company
website: https://expandingweb.com/
---
