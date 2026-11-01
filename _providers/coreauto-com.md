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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/coreauto-com/hosts/coreauto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coreauto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coreauto-com/vendors/coreauto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coreauto-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/coreauto-com/security/coreauto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coreauto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coreauto.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coreauto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coreautom
coverage:
  checked: '2026-10-29'
  detail: No developer documentation or API reference pages are publicly available on the company's website.
  evidence:
  - status: 200
    url: https://www.coreauto.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Core Automation builds AI-driven systems that optimize and automate work across enterprises. Their mission is to create the world’s most automated AI lab, enabling researchers and organizations to streamline processes, reduce manual effort, and accelerate innovation. By integrating advanced automation, machine learning, and cloud-native technologies, Core delivers scalable solutions that transform how work is performed.
image: https://www.coreauto.com/assets/ca_logo.svg
layout: provider
modified: '2026-10-29'
name: Core
nav: Providers
network: true
overview: 'Core is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, AI, Workflow, and Technology.


  Core''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Coreauto Com Plans Pricing
  plan_count: 0
  slug: coreauto-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Coreauto Com Rate Limits
  slug: coreauto-com-rate-limits
scopes:
- name: Coreauto Com Scopes
  scope_count: 0
  slug: coreauto-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
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
  name: Coreauto Com Authentication
  slug: coreauto-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Coreauto Com Domain Security
  slug: coreauto-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coreauto-com
tags:
- Company
- Automation
- AI
- Workflow
- Technology
- Platform
website: https://www.coreauto.com/
---
