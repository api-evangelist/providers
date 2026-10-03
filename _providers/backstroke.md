---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 10.1
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.backstroke.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/backstroke/refs/heads/main/well-known/backstroke-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backstroke-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/backstroke/refs/heads/main/hosts/backstroke-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backstroke-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backstroke.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.backstroke.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backstroke.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.backstroke.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.backstroke.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backstroke/refs/heads/main/security/backstroke-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/backstroke-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backstroke/refs/heads/main/security/backstroke-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backstroke-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.backstroke.com/
coverage:
  checked: 2026-09-27
  detail: OpenAPI endpoints on api.backstroke.com return 403, no machine‑readable spec found.
  evidence:
  - status: 403
    url: https://api.backstroke.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Backstroke is a company identified through the API Evangelist secondary-market harvest. It currently exists as a stub entry awaiting comprehensive profiling. No public website or API documentation has been located, and the company’s online presence appears minimal or undisclosed. Further investigation may be required to determine its services, target market, and technical offerings.
image: https://framerusercontent.com/assets/QjRrFjVeYl2KqPFPNZOMvouYk.png
layout: provider
modified: '2026-09-27'
name: Backstroke
nav: Providers
network: true
overview: 'Backstroke is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Data, and Services.


  Backstroke''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Backstroke Domain Security
  slug: backstroke-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Backstroke Trust Center
  slug: backstroke-trust-center
  summary_line: SOC 2
slug: backstroke
tags:
- Company
- Technology
- Data
- Services
website: https://www.backstroke.com/
---
