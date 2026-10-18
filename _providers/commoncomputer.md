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
  href: https://raw.githubusercontent.com/api-evangelist/commoncomputer/refs/heads/main/hosts/commoncomputer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commoncomputer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commoncomputer/refs/heads/main/vendors/commoncomputer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commoncomputer-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.commoncomputer.net/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commoncomputer/refs/heads/main/security/commoncomputer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commoncomputer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commoncomputer.net
coverage:
  checked: '2026-10-09'
  detail: No public developer documentation or API endpoints were found on the company's website.
  evidence:
  - status: 200
    url: https://www.commoncomputer.net
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Common Computer provides reliable IT support services for homes and businesses, offering solutions ranging from network setup and cybersecurity to cloud migration and on‑site troubleshooting. Founded to deliver trustworthy technology assistance, the company emphasizes rapid response, skilled technicians, and personalized service, ensuring clients can focus on their core activities without IT disruptions.
image: http://static1.squarespace.com/static/69efd24d2f94c0404a032657/t/69efd2960944be1386ccd169/1777324694890/CC_Logo_Black.png?format=1500w
layout: provider
modified: '2026-10-09'
name: Commoncomputer
nav: Providers
network: true
overview: 'Commoncomputer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IT Services, Managed Service, Cybersecurity, Cloud Migration, and Small Business.


  Commoncomputer''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Commoncomputer Domain Security
  slug: commoncomputer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commoncomputer
tags:
- IT Services
- Managed Service
- Cybersecurity
- Cloud Migration
- Small Business
website: https://www.commoncomputer.net
---
