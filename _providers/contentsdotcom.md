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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/contentsdotcom/refs/heads/main/plans/contentsdotcom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contentsdotcom-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentsdotcom/refs/heads/main/hosts/contentsdotcom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentsdotcom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentsdotcom/refs/heads/main/vendors/contentsdotcom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentsdotcom-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contentsdotcom/refs/heads/main/security/contentsdotcom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentsdotcom-domain-security.yml
created: '2026-10-10'
description: Contentsdotcom provides an enterprise AI-powered content platform that enables creation, localization, and governance of copy, blogs, SEO, translations, images, video, and campaigns at scale. The service offers tools for content ideation, automated writing, multilingual translation, and brand voice management, targeting digital agencies and enterprises seeking to automate and optimize their content workflows.
layout: provider
modified: '2026-10-10'
name: Contentsdotcom
nav: Providers
network: true
overview: Contentsdotcom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Contentsdotcom Plans Pricing
  plan_count: 0
  slug: contentsdotcom-plans-pricing
random_paper: 6
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contentsdotcom Domain Security
  slug: contentsdotcom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contentsdotcom
tags:
- Company
---
