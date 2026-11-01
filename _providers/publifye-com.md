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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Publifye provides various subdomain APIs but no public machine-readable contract was found.
  name: Publifye API
  slug: publifye-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/publifye-com/llms/publifye-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/publifye-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/publifye-com/well-known/publifye-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/publifye-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/publifye-com/hosts/publifye-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/publifye-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://publifye.com/news
- group: auth
  href: https://artifacts.apis.io/publifye-com/security/publifye-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/publifye-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://publifye.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.publifye.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Publifye
- group: operate
  title: ''
  type: Support
  url: https://publifye.com/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://publifye.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://publifye.com/privacy.html
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://publifye.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Publifye AS is a Norwegian Bible publishing company based in Oslo, offering over 4,200 Bible editions and a suite of AI‑enhanced tools for Scripture study, publishing, document management, and Norwegian data integration. Their platform provides APIs that enable developers to access biblical texts, leverage AI for content generation, and integrate publishing workflows into applications. Publifye focuses on combining traditional publishing expertise with modern AI capabilities to serve churches, scholars, and developers worldwide.
image: https://publifye.com/og-image.png
layout: provider
modified: '2026-10-29'
name: publifye-com
nav: Providers
network: true
overview: 'publifye-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bible, Publishing, AI, and Norway.


  publifye-com''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Publifye Com Plans Pricing
  plan_count: 0
  slug: publifye-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Publifye Com Rate Limits
  slug: publifye-com-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Publifye Com Authentication
  slug: publifye-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Publifye Com Domain Security
  slug: publifye-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: publifye-com
tags:
- Company
- Bible
- Publishing
- AI
- Norway
- Data
website: https://publifye.com/
---
