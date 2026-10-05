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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: BorderX Lab API (no public documentation found)
  name: BorderX Lab API
  slug: borderx-lab-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/borderx-lab/refs/heads/main/llms/borderx-lab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/borderx-lab-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/borderx-lab/refs/heads/main/hosts/borderx-lab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/borderx-lab-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/borderx-lab/refs/heads/main/vendors/borderx-lab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/borderx-lab-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.borderxlab.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/borderx-lab/refs/heads/main/security/borderx-lab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/borderx-lab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.borderxlab.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.borderxlab.com/our-story
- group: company
  title: ''
  type: Blog
  url: https://www.borderxlab.com/blog
coverage:
  checked: '2026-10-02'
  detail: Home page renders via Wix with no machine‑readable API spec discovered
  evidence:
  - status: 200
    url: https://www.borderxlab.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: BorderX Lab, founded in 2014 by three former Google PhDs, is a Silicon Valley‑based leader in AI‑driven cross‑border e‑commerce. It offers a suite of products—including CloudStore AI, BeyondStyle, and the Bieyang app—to empower brands and merchants worldwide to deliver autonomous shopping experiences. With over 200 employees across the US and China, BorderX Lab combines advanced personalization, logistics, and agentic commerce technology to create a seamless global trade platform.
layout: provider
modified: '2026-10-02'
name: BorderX Lab
nav: Providers
network: true
overview: 'BorderX Lab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, E-Commerce, Cross-Border, and Platform.


  BorderX Lab''s developer surface includes getting-started guide, engineering blog, and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Borderx Lab Domain Security
  slug: borderx-lab-domain-security
  summary_line: TLSv1.3 · DMARC
slug: borderx-lab
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Cross-Border
- Platform
website: https://www.borderxlab.com/
---
