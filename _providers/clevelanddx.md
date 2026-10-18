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
- description: Cleveland Diagnostics provides the IsoClear platform for cancer diagnostic testing, described on their platform page.
  name: IsoClear Platform API
  slug: isoclear-platform-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clevelanddx/refs/heads/main/hosts/clevelanddx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clevelanddx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clevelanddx/refs/heads/main/vendors/clevelanddx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clevelanddx-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.clevelanddx.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clevelanddx/refs/heads/main/security/clevelanddx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clevelanddx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clevelanddx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clevelanddx.com/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://www.clevelanddx.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.clevelanddx.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.clevelanddx.com/news-media-center
coverage:
  detail: Platform page renders via Squarespace JavaScript, no machine‑readable API spec found.
  evidence:
  - status: 200
    url: https://www.clevelanddx.com/platform
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: ClevelandDx, operating as Cleveland Diagnostics, provides innovative cancer diagnostic testing, including the IsoPSA test and the IsoClear platform. The company focuses on early detection of cancer through advanced protein biomarker analysis, offering services to clinicians and patients worldwide. Their mission is to improve cancer decision-making with more accurate and rapid diagnostic tools, supported by a leadership team and extensive research collaborations.
image: http://static1.squarespace.com/static/6206bdb5ff4ac21c6a8eda7f/t/6264b349aec8746813dc740e/1650766665846/social-logo.png?format=1500w
layout: provider
modified: '2026-10-08'
name: ClevelandDx
nav: Providers
network: true
overview: 'ClevelandDx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Cancer, Healthcare, and Biotechnology.


  ClevelandDx''s developer surface includes documentation, getting-started guide, support, engineering blog, and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clevelanddx Domain Security
  slug: clevelanddx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clevelanddx
tags:
- Company
- Diagnostics
- Cancer
- Healthcare
- Biotechnology
website: https://www.clevelanddx.com/
---
