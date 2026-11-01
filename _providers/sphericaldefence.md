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
- description: API reference for Spherical Defence services.
  name: Spherical Defence API
  slug: spherical-defence-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/sphericaldefence/llms/sphericaldefence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sphericaldefence-llms.txt
- group: agent
  href: https://artifacts.apis.io/sphericaldefence/well-known/sphericaldefence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sphericaldefence-well-known.yml
- group: other
  href: https://artifacts.apis.io/sphericaldefence/hosts/sphericaldefence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sphericaldefence-hosts.yml
- group: other
  href: https://artifacts.apis.io/sphericaldefence/vendors/sphericaldefence-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sphericaldefence-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://sphericaldefence.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SphericalDefence
- group: auth
  href: https://artifacts.apis.io/sphericaldefence/security/sphericaldefence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sphericaldefence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sphericaldefence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://guide.sphericaldefence.com/
- group: company
  title: ''
  type: Blog
  url: https://sphericaldefence.com/blog/
coverage:
  checked: '2026-10-21'
  detail: Docs site returns HTML shells with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.sphericaldefence.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Spherical Defense provides advanced cybersecurity solutions focused on protecting critical infrastructure and enterprise networks. Their platform offers real‑time threat detection, automated response, and comprehensive security analytics, leveraging AI and machine learning to identify sophisticated attacks. Founded to address the growing complexity of modern cyber threats, Spherical Defense serves government agencies, financial institutions, and large corporations worldwide, delivering scalable, cloud‑native defenses and compliance support across multiple regulatory frameworks.
layout: provider
modified: '2026-10-21'
name: Spherical Defense
nav: Providers
network: true
overview: 'Spherical Defense is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Artificial Intelligence, Threat Detection, and Cloud-Native.


  Spherical Defense''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sphericaldefence Domain Security
  slug: sphericaldefence-domain-security
  summary_line: TLSv1.2
slug: sphericaldefence
tags:
- Company
- Cybersecurity
- Artificial Intelligence
- Threat Detection
- Cloud-Native
website: https://sphericaldefence.com/
---
