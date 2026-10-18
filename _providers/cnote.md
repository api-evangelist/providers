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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cnote/refs/heads/main/hosts/cnote-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cnote-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cnote/refs/heads/main/vendors/cnote-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cnote-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mycnote.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mycnote.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://secure.mycnote.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.mycnote.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cnote/refs/heads/main/security/cnote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cnote-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mycnote.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.mycnote.com
  - status: 403
    url: https://equityzen.com/company/cnote
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CNote is a cash and fixed‑income platform that helps institutions and individuals achieve competitive returns while preserving capital and strengthening communities nationwide. It connects investors with mission‑driven financial institutions such as CDFIs, MDIs, and LIDs, offering insured cash‑management products and impact‑focused fixed‑income solutions.
image: https://www.mycnote.com/wp-content/uploads/2024/12/CNote-Impact-Investing-made-easy.png
layout: provider
modified: '2026-10-09'
name: Cnote
nav: Providers
network: true
overview: 'Cnote is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Impact Investing, Cash Management, Fixed Income, and Community Development.


  Cnote''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cnote Domain Security
  slug: cnote-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cnote
tags:
- Finance
- Impact Investing
- Cash Management
- Fixed Income
- Community Development
website: https://www.mycnote.com
---
