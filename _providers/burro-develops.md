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
- description: Burro develops provides a robotics API documented at https://docs.burro.ai. The API details autonomous workhorse platform capabilities for agriculture and industrial tasks.
  name: Burro API
  slug: burro-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/burro-develops/refs/heads/main/changelog/burro-develops-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/burro-develops-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/burro-develops/refs/heads/main/llms/burro-develops-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burro-develops-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/burro-develops/refs/heads/main/hosts/burro-develops-hosts.yml
  title: ''
  type: Hosts
  url: hosts/burro-develops-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/burro-develops/refs/heads/main/vendors/burro-develops-vendors.yml
  title: ''
  type: Vendors
  url: vendors/burro-develops-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.burro.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://burro.ai/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.burro.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.burro.ai/platforms/burro-grande/assembly-and-setup/assembly
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/burro-develops/refs/heads/main/security/burro-develops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burro-develops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://burro.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.burro.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.burro.ai
- group: company
  title: ''
  type: Blog
  url: https://burro.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/burro-robotics
- group: commercial
  title: ''
  type: Pricing
  url: https://burro.ai/pricing
- group: operate
  title: ''
  type: Contact
  url: https://burro.ai/contact
coverage:
  checked: '2026-10-06'
  detail: Docs site https://docs.burro.ai returns JavaScript shells and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.burro.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Burro develops is a robotics company building autonomous, electric workhorse platforms for agriculture and industrial tasks. Founded in 2017, Burro creates collaborative robots that automate repetitive labor, improving productivity in farms, nurseries, vineyards, and warehouses. The company offers modular, plug‑and‑play robots capable of towing, load‑carrying, mowing, spraying, and monitoring, targeting specialty crop operations and heavy‑duty material handling.
image: https://burro.ai/wp-content/uploads/2026/05/burro-logo-feature.png
layout: provider
modified: '2026-10-06'
name: Burro develops
nav: Providers
network: true
overview: 'Burro develops is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Agriculture, Automation, and Industrial.


  Burro develops'' developer surface includes changelog, support, getting-started guide, documentation, engineering blog, pricing, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 64.3
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Burro Develops Domain Security
  slug: burro-develops-domain-security
  summary_line: TLSv1.3 · DMARC
slug: burro-develops
tags:
- Company
- Robotics
- Agriculture
- Automation
- Industrial
- Artificial Intelligence
website: https://burro.ai
---
