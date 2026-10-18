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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canoesoftware/refs/heads/main/llms/canoesoftware-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canoesoftware-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canoesoftware/refs/heads/main/well-known/canoesoftware-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canoesoftware-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canoesoftware/refs/heads/main/hosts/canoesoftware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canoesoftware-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canoesoftware/refs/heads/main/vendors/canoesoftware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canoesoftware-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canoeintelligence.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canoesoftware/refs/heads/main/security/canoesoftware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canoesoftware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canoeintelligence.com
coverage:
  checked: '2026-10-06'
  detail: The provider's documentation site https://canoesoftware.github.io returns a JavaScript shell and no machine‑readable spec.
  evidence:
  - status: 200
    url: https://canoesoftware.github.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Canoesoftware is a technology company that provides software solutions for managing and optimizing canoe rental operations. The company focuses on delivering APIs that enable integration with booking systems, inventory management, and customer relationship tools. While detailed public information is limited, Canoesoftware aims to streamline the workflow for businesses in the recreational watercraft industry, offering developers programmatic access to core functionalities such as reservation handling, pricing, and reporting. The organization appears to be associated with Canoe Intelligence, as the domain canoeesoftware.com redirects to canoeintelligence.com, suggesting a possible rebranding or acquisition, though the exact relationship remains unclear.
image: https://canoeintelligence.com/wp-content/uploads/2024/07/canoe-OG.jpg
layout: provider
modified: '2026-10-06'
name: Canoesoftware
nav: Providers
network: true
overview: Canoesoftware is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Canoe Rental, and Technology.
random_paper: 7
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canoesoftware Domain Security
  slug: canoesoftware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canoesoftware
tags:
- Company
- Software
- Canoe Rental
- Technology
website: https://canoeintelligence.com
---
