---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ceremonia/refs/heads/main/llms/ceremonia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ceremonia-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ceremonia/refs/heads/main/well-known/ceremonia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ceremonia-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceremonia/refs/heads/main/hosts/ceremonia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceremonia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceremonia/refs/heads/main/vendors/ceremonia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceremonia-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ceremonia.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceremonia/refs/heads/main/security/ceremonia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceremonia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ceremonia.com
- group: company
  title: ''
  type: Blog
  url: https://ceremonia.com/blogs/all
- group: commercial
  title: ''
  type: Policies/TermsOfService
  url: https://ceremonia.com/policies/terms-of-service
- group: commercial
  title: ''
  type: Policies/PrivacyPolicy
  url: https://ceremonia.com/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://ceremonia.com/pages/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://ceremonia.com/pages/about-us
- group: start
  title: ''
  type: GettingStarted
  url: https://ceremonia.com/pages/about-us
coverage:
  checked: '2026-10-08'
  detail: Homepage loads JavaScript and provides no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://ceremonia.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Ceremonia is a clean hair care brand rooted in Latinx heritage, offering sustainable, silicone‑free, sulfate‑free hair products. Founded by Babba Rivera, the company focuses on natural ingredients and clinically‑backed formulas, aiming to empower confident, healthy hair while celebrating cultural rituals.
image: http://ceremonia.com/cdn/shop/files/Ceremonia-social-logo_71764e31-bd3e-4f2d-bb5f-6f51403f833b.jpg?v=1611087594
layout: provider
modified: '2026-10-07'
name: Ceremonia
nav: Providers
network: true
overview: 'Ceremonia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hair Care, Sustainable, Latinx, and Beauty.


  Ceremonia''s developer surface includes engineering blog, support, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
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
  name: Ceremonia Domain Security
  slug: ceremonia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ceremonia
tags:
- Company
- Hair Care
- Sustainable
- Latinx
- Beauty
website: https://ceremonia.com
---
