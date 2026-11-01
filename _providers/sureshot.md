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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/sureshot/llms/sureshot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sureshot-llms.txt
- group: agent
  href: https://artifacts.apis.io/sureshot/well-known/sureshot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sureshot-well-known.yml
- group: other
  href: https://artifacts.apis.io/sureshot/hosts/sureshot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sureshot-hosts.yml
- group: other
  href: https://artifacts.apis.io/sureshot/vendors/sureshot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sureshot-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.sureshot.io/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sure-shot
- group: auth
  href: https://artifacts.apis.io/sureshot/security/sureshot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sureshot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sureshot.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.sureshot.io/mcp
  - status: 200
    url: https://sureshot.io/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Sureshot provides a comprehensive platform for managing and automating security testing workflows. It offers tools for vulnerability scanning, penetration testing orchestration, and continuous security validation across cloud, on‑premise, and hybrid environments. The service integrates with CI/CD pipelines, supports multi‑tenant reporting, and delivers actionable insights to help organizations improve their security posture while reducing manual effort and time to remediation. Sureshot aims to streamline security operations for enterprises of all sizes, enabling faster detection and response to threats.
layout: provider
modified: '2026-10-21'
name: Sureshot
nav: Providers
network: true
overview: 'Sureshot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Automation, Vulnerability Management, and DevOps.


  Sureshot''s developer surface includes support and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sureshot Domain Security
  slug: sureshot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sureshot
tags:
- Company
- Security
- Automation
- Vulnerability Management
- DevOps
website: https://sureshot.io/
---
