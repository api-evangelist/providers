---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Runlocal provides a tunneling service; the API is documented in the Getting Started page but no machine‑readable spec is published.
  name: Runlocal API
  slug: runlocal-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/runlocal-eu/rate-limits/runlocal-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/runlocal-eu-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/rules/runlocal-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/runlocal-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/json-ld/runlocal-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/runlocal-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/runlocal-eu/vocabulary/runlocal-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/runlocal-eu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/runlocal-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/data-model/runlocal-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/runlocal-eu-data-model.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/conventions/runlocal-eu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/runlocal-eu-conventions.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/conventions/runlocal-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/runlocal-eu-conventions.yml
- group: auth
  href: https://artifacts.apis.io/runlocal-eu/authentication/runlocal-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/runlocal-eu-authentication.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/errors/runlocal-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/runlocal-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/runlocal-eu/conformance/runlocal-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/runlocal-eu-conformance.yml
- group: other
  href: https://artifacts.apis.io/runlocal-eu/hosts/runlocal-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runlocal-eu-hosts.yml
- group: build
  href: https://artifacts.apis.io/runlocal-eu/packages/runlocal-eu-packages.yml
  title: ''
  type: SDKs
  url: packages/runlocal-eu-packages.yml
- group: build
  href: https://artifacts.apis.io/runlocal-eu/packages/runlocal-eu-packages.yml
  title: ''
  type: Packages
  url: packages/runlocal-eu-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runlocal.eu/legal/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://runlocal.eu/getting-started
- group: auth
  href: https://artifacts.apis.io/runlocal-eu/security/runlocal-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runlocal-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runlocal.eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runlocal.eu/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runlater-eu
coverage:
  checked: '2026-10-30'
  detail: The provider’s documentation pages are public HTML but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://runlocal.eu/getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Runlocal provides a simple, no‑signup, no‑config service that exposes a local development server to the public internet via a single command. It is European‑owned, GDPR‑compliant, and focuses on privacy‑first tunneling without tracking. Users can quickly share localhost applications for demos, testing, or collaboration, leveraging a secure tunnel that respects EU data protection standards.
jsonld:
- class_count: 25
  name: Runlocal Eu Context
  property_count: 60
  slug: runlocal-eu-context
layout: provider
modified: '2026-10-30'
name: runlocal-eu
nav: Providers
network: true
overview: 'runlocal-eu publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Networking, Security, Privacy, and EU.


  The runlocal-eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  runlocal-eu''s developer surface includes authentication, getting-started guide, and 18 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 5
  name: Runlocal Eu Rate Limits
  slug: runlocal-eu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: runlocal-eu API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: runlocal-eu-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 72.5
    catalog_earned_first_party: 0.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 80.9
    contract_quality: 14.7
    developer_ergonomics: 37.4
    discoverability: 53.6
    operational_transparency: 33.7
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Runlocal Eu Authentication
  slug: runlocal-eu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Runlocal Eu Domain Security
  slug: runlocal-eu-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: runlocal-eu-getting-started
  slug: runlocal-eu-getting-started
slug: runlocal-eu
tags:
- Developer Tools
- Networking
- Security
- Privacy
- EU
website: https://runlocal.eu/
---
