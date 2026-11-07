---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Dregs Com Agentic Access
  operation_count: 59
  slug: dregs-com-agentic-access
  summary_line: 59 operations · 25 acting
api_count: 1
apis:
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Badge rule management
  name: Dregs Badge Rules API
  slug: dregs-com-badge-rules-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Notification channel management
  name: Dregs Channels API
  slug: dregs-com-channels-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Dashboard summary data
  name: Dregs Dashboard API
  slug: dregs-com-dashboard-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Dataset management for analyzers
  name: Dregs Datasets API
  slug: dregs-com-datasets-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Devices tracked by Dregs
  name: Dregs Devices API
  slug: dregs-com-devices-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Escalation rule management
  name: Dregs Escalation Rules API
  slug: dregs-com-escalation-rules-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Escalation management
  name: Dregs Escalations API
  slug: dregs-com-escalations-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Event tracking and management endpoints
  name: Dregs Events API
  slug: dregs-com-events-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Groups (organizations, teams, workspaces, or whatever your app calls them) that identities belong to
  name: Dregs Groups API
  slug: dregs-com-groups-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Identities known to Dregs
  name: Dregs Identities API
  slug: dregs-com-identities-api
- baseURL: https://dregs.com
  baseurl_source: declared
  description: Manage mappings from customer-supplied names to canonical fields and event types
  name: Dregs Mappings API
  slug: dregs-com-mappings-api
artifact_total: 27
asyncapis:
- description: ''
  name: Dregs Com Webhooks
  slug: dregs-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/dregs-com/agentic-access/dregs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dregs-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dregs-com/plans/dregs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dregs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dregs-com/rules/dregs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dregs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dregs-com/json-ld/dregs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dregs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dregs-com/vocabulary/dregs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dregs-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dregs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dregs-com/asyncapi/dregs-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dregs-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dregs-com/data-model/dregs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dregs-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dregs-com/changelog/dregs-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dregs-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dregs-com/authentication/dregs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dregs-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dregs-com/errors/dregs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dregs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dregs-com/conformance/dregs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dregs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dregs-com/llms/dregs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dregs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dregs-com/well-known/dregs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dregs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dregs-com/hosts/dregs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dregs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dregs-com/vendors/dregs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dregs-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://dregs.com/manual/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dregs.com/legal/terms/
- group: start
  title: ''
  type: SignUp
  url: https://dregs.com/dashboard/register
- group: auth
  title: ''
  type: Security
  url: https://dregs.com/legal/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dregs.com/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dregs.com/pricing/
- group: other
  title: ''
  type: Leadership
  url: https://dregs.com/manual/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dregs-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://dregs.com/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://dregs.com/manual/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://dregs.com/changelog/
- group: auth
  href: https://artifacts.apis.io/dregs-com/security/dregs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dregs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dregs.com/
created: '2026-11-05'
description: Dregs provides fraud detection and abuse prevention services for SaaS applications. It scores user identities on humanity, authenticity, uniqueness, and behavior to identify bots, duplicate accounts, and malicious activity. The platform offers SDKs, a REST API, notifications, escalations, and autonomous remediation to protect free trials, payment sign‑ups, and overall platform integrity.
image: https://dregs.com/images/og/home.png
json_schemas:
- name: V1Escalation
  property_count: 20
  slug: dregs-com-v1-escalation
- name: V1PageV1DatasetEntry
  property_count: 8
  slug: dregs-com-v1-page-v1-dataset-entry
- name: V1PageV1Escalation
  property_count: 8
  slug: dregs-com-v1-page-v1-escalation
- name: V1PageV1TrackedEvent
  property_count: 8
  slug: dregs-com-v1-page-v1-tracked-event
- name: V1TrackRequest
  property_count: 9
  slug: dregs-com-v1-track-request
- name: V1TrackedEvent
  property_count: 12
  slug: dregs-com-v1-tracked-event
jsonld:
- class_count: 78
  name: Dregs Com Context
  property_count: 202
  slug: dregs-com-context
layout: provider
modified: '2026-11-05'
name: Dregs
nav: Providers
network: true
overview: 'Dregs publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Badge Rules API, Channels API, Dashboard API, and 8 more. Tagged areas include Fraud Prevention, Abuse Prevention, Identity Scoring, Bot Detection, and Account Verification.


  The Dregs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Dregs'' developer surface includes changelog, authentication, signup flow, pricing, documentation, getting-started guide, API reference, and 22 more developer resources.'
plans:
- name: Dregs Com Plans Pricing
  plan_count: 3
  slug: dregs-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Dregs API Rules
  rule_count: 59
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 4
  slug: dregs-com-rules
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 70.9
    developer_ergonomics: 42.3
    discoverability: 67.9
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
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
  name: Dregs Com Authentication
  slug: dregs-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dregs Com Domain Security
  slug: dregs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: dregs-com-add-dataset-entries
  slug: dregs-com-add-dataset-entries
- name: dregs-com-manage-group-identities
  slug: dregs-com-manage-group-identities
- name: dregs-com-review-identity
  slug: dregs-com-review-identity
slug: dregs-com
tags:
- Fraud Prevention
- Abuse Prevention
- Identity Scoring
- Bot Detection
- Account Verification
website: https://dregs.com/
---
