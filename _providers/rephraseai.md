---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rephraseai Agentic Access
  operation_count: 6
  slug: rephraseai-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://auth.rephrase.ai
  baseurl_source: declared
  description: The Actor API from Rephrase.ai — 1 operation(s) for actor.
  name: Rephrase.ai Actor API
  slug: rephraseai-actor-api
- baseURL: https://auth.rephrase.ai
  baseurl_source: declared
  description: The Authentication API from Rephrase.ai — 1 operation(s) for authentication.
  name: Rephrase.ai Authentication API
  slug: rephraseai-authentication-api
- baseURL: https://auth.rephrase.ai
  baseurl_source: declared
  description: The Video API from Rephrase.ai — 3 operation(s) for video.
  name: Rephrase.ai Video API
  slug: rephraseai-video-api
- baseURL: https://auth.rephrase.ai
  baseurl_source: declared
  description: The Voice API from Rephrase.ai — 1 operation(s) for voice.
  name: Rephrase.ai Voice API
  slug: rephraseai-voice-api
artifact_total: 16
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/agentic-access/rephraseai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rephraseai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/rules/rephraseai-rules.yml
  title: ''
  type: Spectral
  url: rules/rephraseai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/json-ld/rephraseai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rephraseai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/vocabulary/rephraseai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rephraseai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/data-model/rephraseai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rephraseai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/conformance/rephraseai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rephraseai-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/hosts/rephraseai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rephraseai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/vendors/rephraseai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rephraseai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/security/rephraseai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rephraseai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rephrase.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://studio-rephrase-api.readme.io/reference/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://studio-rephrase-api.readme.io/reference/documentation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/authentication/rephraseai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rephraseai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/scopes/rephraseai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/rephraseai-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/conventions/rephraseai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rephraseai-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/mcp/rephraseai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rephraseai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/well-known/rephraseai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rephraseai-well-known.yml
created: '2026-07-17'
description: Rephrase.ai is a Bengaluru-based generative-AI startup whose text-to-video platform, Rephrase Studio, turns plain text scripts into videos of digital human avatars ("actors") that speak the script with lip-synced, natural voices. It exposed a Rephrase Studio API for programmatic video generation (list actors and voices, create and export videos, poll video status) secured with OAuth2 bearer tokens. Backed by Techstars, Rephrase.ai was acquired by Adobe in November 2023 and its technology folded into Adobe's video and generative-AI offerings; the standalone product hosts have since been decommissioned, though the legacy API reference remains hosted on ReadMe. This profile is maintained by API Evangelist for historical and enrichment purposes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rephraseai.png
json_schemas:
- name: AuthRequest
  property_count: 4
  slug: rephraseai-auth-request
- name: AuthResponse
  property_count: 4
  slug: rephraseai-auth-response
- name: CreateCampaignResponse
  property_count: 2
  slug: rephraseai-create-campaign-response
- name: ExportCampaignResponse
  property_count: 2
  slug: rephraseai-export-campaign-response
- name: GetCampaignResponse
  property_count: 8
  slug: rephraseai-get-campaign-response
- name: SimplifiedCreateCampaignRequest
  property_count: 11
  slug: rephraseai-simplified-create-campaign-request
jsonld:
- class_count: 56
  name: Rephraseai Context
  property_count: 100
  slug: rephraseai-context
layout: provider
modified: '2026-07-20'
name: Rephrase.ai
nav: Providers
network: true
overview: 'Rephrase.ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actor API, Authentication API, Video API, and 1 more. Tagged areas include Company, Artificial Intelligence, Generative AI, Video, and Video Generation.


  The Rephrase.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rephrase.ai''s developer surface includes documentation, API reference, authentication, and 14 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Rephrase.ai API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: rephraseai-rules
scopes:
- name: Rephraseai Scopes
  scope_count: 1
  slug: rephraseai-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.7
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 11.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/rephraseai/refs/heads/main/screenshots/rephraseai-2026-09-02T153504.png
security:
- kind: authentication
  name: Rephraseai Authentication
  slug: rephraseai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Rephraseai Domain Security
  slug: rephraseai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rephraseai
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video
- Video Generation
- Avatars
- Media
- Content Creation
website: https://rephrase.ai/
---
