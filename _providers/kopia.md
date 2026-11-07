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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Kopia API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Kopia API
  slug: kopia-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/kopia/rules/kopia-rules.yml
  title: ''
  type: Spectral
  url: rules/kopia-rules.yml
- group: design
  href: https://artifacts.apis.io/kopia/vocabulary/kopia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kopia-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kopia/conformance/kopia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kopia-conformance.yml
- group: other
  href: https://artifacts.apis.io/kopia/hosts/kopia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kopia-hosts.yml
- group: other
  href: https://artifacts.apis.io/kopia/vendors/kopia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kopia-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kopia.io/docs/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://kopia.io/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://kopia.io/docs/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://kopia.io/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://kopia.io/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/kopia/security/kopia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kopia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kopia.io/
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation site lists reference pages but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are publicly available.
  evidence:
  - status: 200
    url: https://kopia.io/docs/reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Kopia provides fast, secure, open-source backup software for Windows, macOS, and Linux. It offers encrypted, compressed, and deduplicated backups using cloud storage of your choice, with both GUI and CLI tools. The solution supports scalable architecture for laptops to servers, and includes policies, snapshots, and easy restoration.
image: https://kopia.io/featured-background.jpg
layout: provider
modified: '2026-10-28'
name: Kopia
nav: Providers
network: true
overview: 'Kopia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Backup, Open Source, Cloud, Security, and Cross-Platform.


  The Kopia catalog on APIs.io includes 1 Spectral governance ruleset.


  Kopia''s developer surface includes documentation, changelog, API reference, getting-started guide, and 8 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Kopia API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: kopia-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 14.3
    contract_governance: 22.0
    contract_quality: 10.4
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 24.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/kopia/kopia-2026-11-03T134529.png
security:
- kind: domain-security
  name: Kopia Domain Security
  slug: kopia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kopia
tags:
- Backup
- Open Source
- Cloud
- Security
- Cross-Platform
website: https://kopia.io/
---
