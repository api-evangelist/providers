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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/common-trust/refs/heads/main/well-known/common-trust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/common-trust-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/common-trust/refs/heads/main/hosts/common-trust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/common-trust-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/common-trust/refs/heads/main/vendors/common-trust-vendors.yml
  title: ''
  type: Vendors
  url: vendors/common-trust-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.common-trust.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.common-trust.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/common-trust/refs/heads/main/security/common-trust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/common-trust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.common-trust.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.common-trust.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Common Trust provides guidance and resources for employee ownership trusts (EOTs), helping companies transition to employee ownership models. The platform offers educational content, playbooks, case studies, webinars, and tools such as an EOT fit analyzer. It serves business owners, advisors, and stakeholders interested in exploring EOT structures as alternatives to traditional ownership, aiming to promote inclusive and sustainable business ownership.
layout: provider
modified: '2026-10-09'
name: Common Trust
nav: Providers
network: true
overview: 'Common Trust is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Ownership, Trust, EOT, and Advisory.


  Common Trust''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Common Trust Domain Security
  slug: common-trust-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: common-trust
tags:
- Company
- Employee Ownership
- Trust
- EOT
- Advisory
website: https://www.common-trust.com/
---
