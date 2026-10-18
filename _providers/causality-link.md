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
  href: https://raw.githubusercontent.com/api-evangelist/causality-link/refs/heads/main/hosts/causality-link-hosts.yml
  title: ''
  type: Hosts
  url: hosts/causality-link-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/causality-link/refs/heads/main/vendors/causality-link-vendors.yml
  title: ''
  type: Vendors
  url: vendors/causality-link-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://causalitylink.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/causality-link/refs/heads/main/security/causality-link-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causality-link-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://causalitylink.com/
- group: operate
  title: ''
  type: Support
  url: https://causalitylink.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://causalitylink.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://causalitylink.com/privacy-policy
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discoverable at the API host or documentation pages.
  evidence:
  - status: 0
    url: https://api.causalitylink.com/openapi.json
  - status: 0
    url: https://api.causalitylink.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Causality Link is a cloud‑based platform that reads and understands millions of words each day from thousands of sources worldwide. It surfaces the knowledge of millions of authors as causal links, explaining not just what is happening but why. The platform offers automated causation identification and analysis for finance, corporate strategy, and government policy, delivering transparent attributions and insights across industries.
image: https://causalitylink.com/wp-content/uploads/2023/04/favicon.png
layout: provider
modified: '2026-10-07'
name: Causality Link
nav: Providers
network: true
overview: 'Causality Link is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Causality, Analytics, and Finance.


  Causality Link''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.6
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
    discoverability: 50.0
    operational_transparency: 0.0
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
  name: Causality Link Domain Security
  slug: causality-link-domain-security
  summary_line: TLSv1.3 · DMARC
slug: causality-link
tags:
- Company
- Artificial Intelligence
- Causality
- Analytics
- Finance
website: https://causalitylink.com/
---
