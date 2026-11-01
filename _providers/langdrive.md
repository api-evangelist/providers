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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/langdrive/llms/langdrive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/langdrive-llms.txt
- group: other
  href: https://artifacts.apis.io/langdrive/hosts/langdrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/langdrive-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://addy.com/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addy.com/privacypolicy
- group: company
  title: ''
  type: Blog
  url: https://addy.com/blog
- group: auth
  href: https://artifacts.apis.io/langdrive/security/langdrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/langdrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.addyai.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.addyai.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Addy AI provides AI‑powered automation for mortgage professionals, enabling faster loan closings through intelligent borrower communication, document review, and loan preparation. The platform streamlines the mortgage workflow, reduces manual effort, and improves accuracy, helping lenders close loans up to 90% faster.
image: https://framerusercontent.com/images/vHdxUtZscMbozEqEfqDgVodq3E.png
layout: provider
modified: '2026-10-21'
name: Addy AI
nav: Providers
network: true
overview: 'Addy AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Mortgage, Automation, and FinTech.


  Addy AI''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Langdrive Domain Security
  slug: langdrive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: langdrive
tags:
- Company
- AI
- Mortgage
- Automation
- FinTech
website: https://www.addyai.com/
---
