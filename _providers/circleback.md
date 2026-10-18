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
- description: Organize contacts on iPhone - In this handy guide, you’ll discover everything you need to know about using CircleBack, whether it’s effortlessly updating outdated contacts, discovering new contacts, d
  name: CircleBack API
  slug: circleback-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/circleback/refs/heads/main/conformance/circleback-conformance.yml
  title: ''
  type: Conformance
  url: conformance/circleback-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circleback/refs/heads/main/hosts/circleback-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circleback-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circleback/refs/heads/main/vendors/circleback-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circleback-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/circleback/refs/heads/main/packages/circleback-packages.yml
  title: ''
  type: SDKs
  url: packages/circleback-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/circleback/refs/heads/main/packages/circleback-packages.yml
  title: ''
  type: Packages
  url: packages/circleback-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circleback.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circleback.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://circleback.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://circleback.com/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/circleback
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/circleback/refs/heads/main/security/circleback-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circleback-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circleback.com/
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI or other machine-readable contract found at standard endpoints on api.circleback.com.
  evidence:
  - status: 404
    url: https://api.circleback.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: 'CircleBack is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://circleback.com/wp-content/uploads/2016/08/cb_1000.png
layout: provider
modified: '2026-10-08'
name: CircleBack
nav: Providers
network: true
overview: 'CircleBack is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  CircleBack''s developer surface includes engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circleback Domain Security
  slug: circleback-domain-security
  summary_line: TLSv1.3 · DMARC
slug: circleback
tags:
- Company
website: https://circleback.com/
---
