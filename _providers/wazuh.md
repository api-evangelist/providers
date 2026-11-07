---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: build
  href: https://artifacts.apis.io/wazuh/cli/wazuh-cli.yml
  title: ''
  type: CLI
  url: cli/wazuh-cli.yml
- group: operate
  href: https://artifacts.apis.io/wazuh/changelog/wazuh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wazuh-changelog.yml
- group: design
  href: https://artifacts.apis.io/wazuh/conformance/wazuh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wazuh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wazuh/llms/wazuh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wazuh-llms.txt
- group: other
  href: https://artifacts.apis.io/wazuh/hosts/wazuh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wazuh-hosts.yml
- group: other
  href: https://artifacts.apis.io/wazuh/vendors/wazuh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wazuh-vendors.yml
- group: build
  href: https://artifacts.apis.io/wazuh/packages/wazuh-packages.yml
  title: ''
  type: SDKs
  url: packages/wazuh-packages.yml
- group: build
  href: https://artifacts.apis.io/wazuh/packages/wazuh-packages.yml
  title: ''
  type: Packages
  url: packages/wazuh-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://wazuh.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wazuh
- group: company
  title: ''
  type: Blog
  url: https://wazuh.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.wazuh.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.wazuh.com/current/user-manual/api/reference.html
- group: auth
  href: https://artifacts.apis.io/wazuh/security/wazuh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wazuh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wazuh.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation provides HTML API reference but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://documentation.wazuh.com/current/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Wazuh provides an open source security platform for threat detection, integrity monitoring, incident response, and compliance. It offers a unified XDR solution that combines SIEM, log analysis, and endpoint security, enabling organizations to monitor and protect their infrastructure across cloud, on‑premise, and hybrid environments. The platform includes real‑time alerting, file integrity checking, vulnerability detection, and powerful dashboards for security operations.
image: https://wazuh.com/uploads/2024/01/wazuh-cover.png
layout: provider
modified: '2026-10-28'
name: Wazuh
nav: Providers
network: true
overview: 'Wazuh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Open Source, XDR, and SIEM.


  Wazuh''s developer surface includes CLI, changelog, engineering blog, documentation, API reference, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 56.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.7
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wazuh/wazuh-2026-11-03T150016.png
security:
- kind: domain-security
  name: Wazuh Domain Security
  slug: wazuh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wazuh
tags:
- Company
- Security
- Open Source
- XDR
- SIEM
website: https://wazuh.com/
---
