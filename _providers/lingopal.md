---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Lingopal Agentic Access
  operation_count: 13
  slug: lingopal-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: Work with reusable registered jobs, their workflows, status, and outputs.
  name: Lingopal Jobs API
  slug: lingopal-jobs-api
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: List supported language capabilities for dubbing, text, and other workflows.
  name: Lingopal Languages API
  slug: lingopal-languages-api
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: Download transcripts, subtitles, and exported job outputs.
  name: Lingopal Job Outputs API
  slug: lingopal-job-outputs-api
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: Upload or register source files as reusable jobs.
  name: Lingopal Job Registration API
  slug: lingopal-job-registration-api
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: Start translation and subtitle workflows for registered jobs.
  name: Lingopal Job Workflows API
  slug: lingopal-job-workflows-api
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: Create and complete presigned storage uploads for source files.
  name: Lingopal Storage API
  slug: lingopal-storage-api
- baseURL: https://api.lingopal.ai
  baseurl_source: declared
  description: Translate text directly without creating a job.
  name: Lingopal Text Translation API
  slug: lingopal-text-translation-api
artifact_total: 22
collections:
- collection_type: open
  name: Lingopal API v2 Jobs API
  slug: open-lingopal-jobs-api
- collection_type: open
  name: Lingopal API v2 Jobs Languages API
  slug: open-lingopal-languages-api
- collection_type: open
  name: Lingopal API v2 Jobs Translate API
  slug: open-lingopal-translate-api
- collection_type: open
  name: Lingopal API v2 Jobs Upload API
  slug: open-lingopal-upload-api
common:
- group: commercial
  href: https://artifacts.apis.io/lingopal/plans/lingopal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lingopal-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/lingopal/capabilities/lingopal-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lingopal-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://lingopal.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lingopal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lingopal.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lingopal.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lingopal.ai/guides/getting-started
- group: docs
  href: https://artifacts.apis.io/lingopal/openapi/_original/lingopal-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/lingopal-openapi-original.json
- group: auth
  href: https://artifacts.apis.io/lingopal/authentication/lingopal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lingopal-authentication.yml
- group: design
  href: https://artifacts.apis.io/lingopal/conventions/lingopal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lingopal-conventions.yml
- group: design
  href: https://artifacts.apis.io/lingopal/errors/lingopal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lingopal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lingopal/lifecycle/lingopal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lingopal-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lingopal/data-model/lingopal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lingopal-data-model.yml
- group: design
  href: https://artifacts.apis.io/lingopal/conformance/lingopal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lingopal-conformance.yml
- group: other
  href: https://artifacts.apis.io/lingopal/overlays/lingopal-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lingopal-v2-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lingopal/mcp/lingopal-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lingopal-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lingopal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lingopal/agentic-access/lingopal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lingopal-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/lingopal/llms/lingopal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lingopal-llms.txt
- group: auth
  href: https://artifacts.apis.io/lingopal/security/lingopal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lingopal-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://lingopal.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lingopal-ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@lingopal.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://lingopal.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lingopal.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lingopal.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lingopal.ai/policy
created: '2026-07-17'
description: Lingopal is an AI translation company building a real-time language layer for live and on-demand video. Its platform delivers sub-10-second AI dubbing and captioning for livestreams across 100+ languages, preserving speaker characteristics through voice cloning, and targets sports and news broadcasters, streaming and FAST channel operators, live events, faith organizations, and contact centers. Lingopal also publishes a public v2 REST API for uploading media and documents, starting translation and dubbing workflows, generating subtitle tracks, translating text synchronously, and downloading generated transcripts and subtitles. The API is documented at docs.lingopal.ai with a machine-readable OpenAPI 3.1 specification, is authenticated with an X-API-Key header, and exposes 112 locales with per-locale text, dubbing, and voice-cloning capability flags.
finops:
- has_sources: true
  method: derived
  name: Lingopal Finops
  primary_unit: subscription
  service_category: ''
  slug: lingopal-finops
  template: false
image: https://lingopal.ai/header_image.png
layout: provider
modified: '2026-07-19'
name: Lingopal
nav: Providers
network: true
overview: 'Lingopal publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Jobs API, Languages API, Job Outputs API, and 4 more. Tagged areas include Company, Frontier Tech, Artificial Intelligence, Translation, and Localization.


  The Lingopal catalog on APIs.io includes 1 Spectral governance ruleset.


  Lingopal''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 20 more developer resources.'
plans:
- name: Lingopal Plans Pricing
  plan_count: 4
  slug: lingopal-plans-pricing
- name: Lingopal Price Estimates
  plan_count: 0
  slug: lingopal-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Lingopal API Rules
  rule_count: 59
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 2
  slug: lingopal-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.6
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 58.3
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lingopal/lingopal-2026-07-25T225250.png
security:
- kind: authentication
  name: Lingopal Authentication
  slug: lingopal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lingopal Domain Security
  slug: lingopal-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Generate subtitles with Lingopal
  slug: lingopal-generate-subtitles
- name: Translate and dub media with Lingopal
  slug: lingopal-translate-media
- name: Translate text with Lingopal
  slug: lingopal-translate-text
- name: Upload large media to Lingopal
  slug: lingopal-upload-large-media
slug: lingopal
tags:
- Company
- Frontier Tech
- Artificial Intelligence
- Translation
- Localization
- Speech
- Media
- Broadcasting
- Video
- Subtitles
- Voice Cloning
website: https://lingopal.ai/
---
