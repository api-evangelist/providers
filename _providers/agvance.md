---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/agvance/llms/agvance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agvance-llms.txt
- group: other
  href: https://artifacts.apis.io/agvance/hosts/agvance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agvance-hosts.yml
- group: other
  href: https://artifacts.apis.io/agvance/vendors/agvance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agvance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meriplex.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://meriplex.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meriplex.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://meriplex.com/blog/
- group: auth
  href: https://artifacts.apis.io/agvance/security/agvance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agvance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ssi-net.com/
coverage:
  checked: '2026-10-28'
  detail: The provider's website and API hosts return 404 for all standard OpenAPI and GraphQL spec URLs, and no documentation host is identified.
  evidence:
  - status: 404
    url: https://meriplex.com/openapi.json
  - status: 404
    url: https://api.meriplex.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: 'Agvance (SSI) is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://meriplex.com/wp-content/uploads/2024/11/cropped-Favicon-1.png
layout: provider
modified: '2026-10-28'
name: Agvance (SSI)
nav: Providers
network: true
overview: 'Agvance (SSI) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Agvance (SSI)''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Agvance Plans Pricing
  plan_count: 0
  slug: agvance-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Agvance Rate Limits
  slug: agvance-rate-limits
scopes:
- name: Agvance Scopes
  scope_count: 0
  slug: agvance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agvance Authentication
  slug: agvance-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agvance Domain Security
  slug: agvance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agvance
tags:
- Company
website: https://ssi-net.com/
---
