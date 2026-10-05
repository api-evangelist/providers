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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.braincorp.com/trust
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/llms/braincorporation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/braincorporation-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/hosts/braincorporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/braincorporation-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/vendors/braincorporation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/braincorporation-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/packages/braincorporation-packages.yml
  title: ''
  type: SDKs
  url: packages/braincorporation-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/packages/braincorporation-packages.yml
  title: ''
  type: Packages
  url: packages/braincorporation-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.braincorp.com/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.braincorp.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.braincorp.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.braincorp.com/team/andy-ng
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braincorp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/security/braincorporation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/braincorporation-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braincorporation/refs/heads/main/security/braincorporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braincorporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.braincorp.com
coverage:
  checked: '2026-10-03'
  detail: The website provides no machine‑readable API documentation; attempts to fetch common spec URLs returned HTML or 404.
  evidence:
  - status: 404
    url: https://www.braincorp.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Braincorp (formerly Braincorporation) develops AI‑driven autonomous robotics platforms for enterprises, enabling automated floor‑care, inventory scanning, and fleet management across retail, logistics, and industrial settings. Founded in 2009, the company offers the BrainOS® autonomy platform, ShelfOptix™ scanning‑as‑a‑service, and a suite of AI solutions that integrate with existing infrastructure to improve efficiency, safety, and operational insight.
image: https://cdn.prod.website-files.com/650caff2e60146b72295e1c4/6584c47cb417f2b4cfa8a648_graph-logo.jpg
layout: provider
modified: '2026-10-03'
name: Braincorporation
nav: Providers
network: true
overview: Braincorporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Robotics, Autonomous, Enterprise, and Platform.
random_paper: 8
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Braincorporation Domain Security
  slug: braincorporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Braincorporation Trust Center
  slug: braincorporation-trust-center
  summary_line: SOC 2
slug: braincorporation
tags:
- Artificial Intelligence
- Robotics
- Autonomous
- Enterprise
- Platform
website: https://www.braincorp.com
---
