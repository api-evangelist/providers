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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: VoiceDock API provides endpoints for managing AI voice assistants and related telephony features.
  name: VoiceDock API
  slug: voicedock-api
- description: 'VoiceDock api API as documented publicly: 39 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: VoiceDock api API
  slug: api-api
- description: 'VoiceDock reference API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: VoiceDock reference API
  slug: reference-api
artifact_total: 18
common:
- group: commercial
  href: https://artifacts.apis.io/voicedock/plans/voicedock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voicedock-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/voicedock/rules/voicedock-rules.yml
  title: ''
  type: Spectral
  url: rules/voicedock-rules.yml
- group: design
  href: https://artifacts.apis.io/voicedock/json-ld/voicedock-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/voicedock-context.jsonld
- group: design
  href: https://artifacts.apis.io/voicedock/vocabulary/voicedock-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/voicedock-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/voicedock/data-model/voicedock-data-model.yml
  title: ''
  type: DataModel
  url: data-model/voicedock-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.voicedock.ai/
- group: auth
  href: https://artifacts.apis.io/voicedock/authentication/voicedock-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voicedock-authentication.yml
- group: design
  href: https://artifacts.apis.io/voicedock/conformance/voicedock-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voicedock-conformance.yml
- group: agent
  href: https://artifacts.apis.io/voicedock/llms/voicedock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voicedock-llms.txt
- group: auth
  href: https://artifacts.apis.io/voicedock/well-known/voicedock-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voicedock-trust-security.txt
- group: auth
  href: https://artifacts.apis.io/voicedock/well-known/voicedock-resend-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voicedock-resend-security.txt
- group: auth
  href: https://artifacts.apis.io/voicedock/well-known/voicedock-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voicedock-platform-security.txt
- group: auth
  href: https://artifacts.apis.io/voicedock/well-known/voicedock-elevenlabs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voicedock-elevenlabs-security.txt
- group: agent
  href: https://artifacts.apis.io/voicedock/well-known/voicedock-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voicedock-well-known.yml
- group: other
  href: https://artifacts.apis.io/voicedock/hosts/voicedock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voicedock-hosts.yml
- group: other
  href: https://artifacts.apis.io/voicedock/vendors/voicedock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/voicedock-vendors.yml
- group: build
  href: https://artifacts.apis.io/voicedock/packages/voicedock-packages.yml
  title: ''
  type: SDKs
  url: packages/voicedock-packages.yml
- group: build
  href: https://artifacts.apis.io/voicedock/packages/voicedock-packages.yml
  title: ''
  type: Packages
  url: packages/voicedock-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.voicedock.ai/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://dashboard.voicedock.ai/en/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://voicedock.ai/en/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.voicedock.ai/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.voicedock.ai/docs/get-started/quickstart
- group: auth
  href: https://artifacts.apis.io/voicedock/security/voicedock-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/voicedock-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/voicedock/security/voicedock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voicedock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voicedock.ai/en
- group: docs
  title: ''
  type: Documentation
  url: https://doc.voicedock.ai/docs/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://voicedock.ai/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://voicedock.ai/en/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.voicedock.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flireo-bv-org
coverage:
  checked: '2026-11-02'
  detail: Human‑readable documentation is available but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://doc.voicedock.ai/docs/introduction
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: VoiceDock provides a Voice AI platform that runs on real phone lines, offering a Vapi‑alternative with on‑premise, private‑cloud and EU‑sovereign deployment options. The service includes real‑time transcription, call control, webhooks and post‑call analysis, all accessible via a transparent REST API and dashboard. Pricing is €0.07 per minute plus model usage at cost, with no per‑seat licences or hidden markup. VoiceDock also supports white‑labeling, reseller setups, and compliance documentation through its Trust Center.
image: https://voicedock.ai/voice-dock-logo.png
json_schemas:
- name: GetArenaCases497F6Eca62764993Bfeb53Cbbbba6F08Response
  property_count: 22
  slug: voicedock-get-arena-cases497-f6-eca62764993-bfeb53-cbbbba6-f08-response
- name: GetArenaRuns497F6Eca62764993Bfeb53Cbbbba6F08Response
  property_count: 13
  slug: voicedock-get-arena-runs497-f6-eca62764993-bfeb53-cbbbba6-f08-response
- name: GetArenaSuites497F6Eca62764993Bfeb53Cbbbba6F08RunsResponse
  property_count: 13
  slug: voicedock-get-arena-suites497-f6-eca62764993-bfeb53-cbbbba6-f08-runs-response
- name: GetCallsResponse
  property_count: 2
  slug: voicedock-get-calls-response
- name: PostApiV1ByokRequest
  property_count: 2
  slug: voicedock-post-api-v1-byok-request
- name: PostArenaSuites497F6Eca62764993Bfeb53Cbbbba6F08CasesResponse
  property_count: 22
  slug: voicedock-post-arena-suites497-f6-eca62764993-bfeb53-cbbbba6-f08-cases-response
- name: PostArenaSuites497F6Eca62764993Bfeb53Cbbbba6F08RunsResponse
  property_count: 13
  slug: voicedock-post-arena-suites497-f6-eca62764993-bfeb53-cbbbba6-f08-runs-response
- name: PostWebhookRequest
  property_count: 1
  slug: voicedock-post-webhook-request
jsonld:
- class_count: 40
  name: Voicedock Context
  property_count: 77
  slug: voicedock-context
layout: provider
modified: '2026-11-02'
name: VoiceDock
nav: Providers
network: true
overview: 'VoiceDock is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including api API, reference API, and 1 more. Tagged areas include Voice AI, Telephony, Communications, Platform, and EU-Sovereign.


  The VoiceDock catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VoiceDock''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, support, and 25 more developer resources.'
plans:
- name: Voicedock Plans Pricing
  plan_count: 1
  slug: voicedock-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Voicedock Rate Limits
  slug: voicedock-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: VoiceDock API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: voicedock-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 23.8
    developer_ergonomics: 36.9
    discoverability: 62.5
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Voicedock Authentication
  slug: voicedock-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Voicedock Domain Security
  slug: voicedock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Voicedock Trust Center
  slug: voicedock-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, PCI DSS, GDPR
slug: voicedock
tags:
- Voice AI
- Telephony
- Communications
- Platform
- EU-Sovereign
- On-Premises
website: https://voicedock.ai/en
---
