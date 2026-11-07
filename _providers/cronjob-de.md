---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Cronjob De Agentic Access
  operation_count: 28
  slug: cronjob-de-agentic-access
  summary_line: 28 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.cronjob.de/api/v1
  baseurl_source: declared
  description: The Benachrichtigungen API from Cronjob.de — 2 operation(s) for benachrichtigungen.
  name: Cronjob.de Benachrichtigungen API
  slug: cronjob-de-benachrichtigungen-api
- baseURL: https://www.cronjob.de/api/v1
  baseurl_source: declared
  description: The Cronjobs und Heartbeats API from Cronjob.de — 10 operation(s) for cronjobs und heartbeats.
  name: Cronjob.de Cronjobs und Heartbeats API
  slug: cronjob-de-cronjobs-und-heartbeats-api
- baseURL: https://www.cronjob.de/api/v1
  baseurl_source: declared
  description: The Serverüberwachung und SSL API from Cronjob.de — 4 operation(s) for serverüberwachung und ssl.
  name: Cronjob.de Serverüberwachung und SSL API
  slug: cronjob-de-server-berwachung-und-ssl-api
- baseURL: https://www.cronjob.de/api/v1
  baseurl_source: declared
  description: The Statusseiten API from Cronjob.de — 2 operation(s) for statusseiten.
  name: Cronjob.de Statusseiten API
  slug: cronjob-de-statusseiten-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/cronjob-de/agentic-access/cronjob-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cronjob-de-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cronjob-de/rules/cronjob-de-rules.yml
  title: ''
  type: Spectral
  url: rules/cronjob-de-rules.yml
- group: design
  href: https://artifacts.apis.io/cronjob-de/vocabulary/cronjob-de-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cronjob-de-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cronjob-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cronjob-de/errors/cronjob-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cronjob-de-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cronjob-de/conformance/cronjob-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cronjob-de-conformance.yml
- group: other
  href: https://artifacts.apis.io/cronjob-de/hosts/cronjob-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cronjob-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/cronjob-de/vendors/cronjob-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cronjob-de-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cronjob.de/en/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cronjob.de/
- group: start
  title: ''
  type: SignUp
  url: https://www.cronjob.de/en/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cronjob.de/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cronjob.de/en/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.cronjob.de/en/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cronjob.de/en/whats-new
- group: docs
  title: ''
  type: APIReference
  url: https://www.cronjob.de/llms.txt
- group: auth
  href: https://artifacts.apis.io/cronjob-de/authentication/cronjob-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cronjob-de-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cronjob-de/security/cronjob-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cronjob-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cronjob.de/
created: '2026-11-04'
description: Cronjob.de offers a free online cron job scheduling service without requiring a server. Operated by a German company since 2003, it runs on EU-based servers, provides invoicing with VAT, GDPR‑compliant data processing agreements, team accounts, and AI‑assisted setup. Users can create cron jobs via a web UI or API, with monitoring and alerts, all hosted on renewable‑energy powered infrastructure.
image: https://www.cronjob.de/assets/img/og-cronjob-en.jpg
layout: provider
modified: '2026-11-04'
name: Cronjob.de
nav: Providers
network: true
overview: 'Cronjob.de publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Benachrichtigungen API, Cronjobs und Heartbeats API, Serverüberwachung und SSL API, and 1 more. Tagged areas include Cronjob, Scheduling, Automation, and EU-hosted.


  The Cronjob.de catalog on APIs.io includes 1 Spectral governance ruleset.


  Cronjob.de''s developer surface includes signup flow, pricing, documentation, changelog, API reference, authentication, and 13 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Cronjob.de API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: cronjob-de-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 49.0
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cronjob De Authentication
  slug: cronjob-de-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cronjob De Domain Security
  slug: cronjob-de-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: cronjob-de-manage-notifications
  slug: cronjob-de-manage-notifications
- name: cronjob-de-server-berwachung-und-ssl-create-and-activate
  slug: cronjob-de-server-berwachung-und-ssl-create-and-activate
slug: cronjob-de
tags:
- Cronjob
- Scheduling
- Automation
- EU-hosted
website: https://cronjob.de/
---
