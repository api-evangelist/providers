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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Vault Radar integration provided by BluBracket, documented on HashiCorp developer portal.
  name: Vault Radar
  slug: vault-radar
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/blubracket/changelog/blubracket-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blubracket-changelog.yml
- group: other
  href: https://artifacts.apis.io/blubracket/grpc/blubracket.proto
  title: ''
  type: Protobuf
  url: grpc/blubracket.proto
- group: other
  href: https://artifacts.apis.io/blubracket/hosts/blubracket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blubracket-hosts.yml
- group: other
  href: https://artifacts.apis.io/blubracket/vendors/blubracket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blubracket-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hashicorp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hashicorp.com/vault/docs/get-started/developer-qs
- group: auth
  href: https://artifacts.apis.io/blubracket/security/blubracket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blubracket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.hashicorp.com/hcp/docs/vault-radar
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/hcp/docs/vault-radar
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hashicorp.com/hcp/docs/vault-radar
- group: operate
  title: ''
  type: Support
  url: https://developer.hashicorp.com/hcp/docs/vault-radar#support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hashicorp.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BluBracket
coverage:
  checked: '2026-10-29'
  detail: Documentation is available but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://developer.hashicorp.com/hcp/docs/vault-radar
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: BluBracket is a venture‑backed startup focused on providing security and compliance tooling for cloud‑native applications. The company appears in the API Evangelist harvest backlog and is associated with unusual‑ventures. Public information is limited, but references point to a product called Vault Radar hosted on HashiCorp’s developer portal, suggesting integration with secret management solutions.
image: https://developer.hashicorp.com/og-image/vault-radar.jpg
layout: provider
modified: '2026-10-29'
name: BluBracket
nav: Providers
network: true
overview: 'BluBracket is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  BluBracket''s developer surface includes changelog, getting-started guide, documentation, API reference, support, and 8 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blubracket/blubracket-2026-11-03T122036.png
security:
- kind: domain-security
  name: Blubracket Domain Security
  slug: blubracket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blubracket
tags:
- Company
website: https://developer.hashicorp.com/hcp/docs/vault-radar
---
