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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Beszel provides monitoring and management of servers and services, offering agents, dashboards, and integrations as described in its Getting Started guide.
  name: Beszel API
  slug: beszel-api-2
- baseURL: https://get.beszel.dev
  baseurl_source: declared
  description: 'Beszel API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Beszel API
  slug: beszel-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/beszel/rules/beszel-rules.yml
  title: ''
  type: Spectral
  url: rules/beszel-rules.yml
- group: design
  href: https://artifacts.apis.io/beszel/vocabulary/beszel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beszel-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/beszel/conformance/beszel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beszel-conformance.yml
- group: other
  href: https://artifacts.apis.io/beszel/hosts/beszel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beszel-hosts.yml
- group: other
  href: https://artifacts.apis.io/beszel/vendors/beszel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beszel-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/henrygd/beszel/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://beszel.dev/guide/getting-started
- group: auth
  href: https://artifacts.apis.io/beszel/security/beszel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beszel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beszel.dev/
coverage:
  checked: '2026-10-28'
  detail: Beszel's documentation is public HTML markdown but provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://beszel.dev/guide/getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Beszel provides a lightweight server monitoring solution that tracks CPU, memory, and network usage for Docker and Podman containers. It offers configurable alerts, multi‑user management with shared systems, OAuth/OIDC authentication, automatic backups to disk or S3‑compatible storage, and a REST API for integration. The software is released under the MIT License.
image: https://beszel.dev/image/social.png
layout: provider
modified: '2026-10-28'
name: Beszel
nav: Providers
network: true
overview: 'Beszel is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Server Monitoring, Docker, Podman, Alerts, and Multi-User.


  The Beszel catalog on APIs.io includes 1 Spectral governance ruleset.


  Beszel''s developer surface includes changelog, getting-started guide, and 7 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Beszel API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: beszel-rules
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/beszel/beszel-2026-11-03T121652.png
security:
- kind: domain-security
  name: Beszel Domain Security
  slug: beszel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beszel
tags:
- Server Monitoring
- Docker
- Podman
- Alerts
- Multi-User
- OAuth
- Backup
- REST API
website: https://beszel.dev/
---
