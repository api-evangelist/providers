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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Majr App Agentic Access
  operation_count: 15
  slug: majr-app-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://seo.majr.app
  baseurl_source: declared
  description: Fetch one URL (SSRF-guarded) and score its technical SEO + AI-readiness signals.
  name: majr-app Audit API
  slug: majr-app-audit-api
- baseURL: https://dispatch.majr.app
  baseurl_source: declared
  description: Who this service is and where its contracts live.
  name: majr-app Discovery API
  slug: majr-app-discovery-api
- baseURL: https://dispatch.majr.app
  baseurl_source: declared
  description: 'The capability: dev log in, release-notes Markdown out.'
  name: majr-app Drafting API
  slug: majr-app-drafting-api
- baseURL: https://encoding.majr.app
  baseurl_source: declared
  description: The Encode API from majr-app — 1 operation(s) for encode.
  name: majr-app Encode API
  slug: majr-app-encode-api
- baseURL: https://seo.majr.app
  baseurl_source: declared
  description: Pure artifact generation — JSON in, artifact out, no fetches, no state.
  name: majr-app Generation API
  slug: majr-app-generation-api
- baseURL: https://encoding.majr.app
  baseurl_source: declared
  description: The Healthz API from majr-app — 1 operation(s) for healthz.
  name: majr-app Healthz API
  slug: majr-app-healthz-api
- baseURL: https://encoding.majr.app
  baseurl_source: declared
  description: The Jobs API from majr-app — 1 operation(s) for jobs.
  name: majr-app Jobs API
  slug: majr-app-jobs-api
- baseURL: https://encoding.majr.app
  baseurl_source: declared
  description: The Uploads API from majr-app — 1 operation(s) for uploads.
  name: majr-app Uploads API
  slug: majr-app-uploads-api
- baseURL: https://dispatch.majr.app
  baseurl_source: declared
  description: Your metered usage (drafts + token counts).
  name: majr-app Usage API
  slug: majr-app-usage-api
- baseURL: https://dispatch.majr.app
  baseurl_source: declared
  description: Your account's brand-voice floor (composed beneath every draft).
  name: majr-app Voice API
  slug: majr-app-voice-api
artifact_total: 34
asyncapis:
- description: ''
  name: Majr App Webhooks
  slug: majr-app-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/majr-app/agentic-access/majr-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/majr-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/majr-app/rules/majr-app-rules.yml
  title: ''
  type: Spectral
  url: rules/majr-app-rules.yml
- group: design
  href: https://artifacts.apis.io/majr-app/json-ld/majr-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/majr-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/majr-app/vocabulary/majr-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/majr-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/majr-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/majr-app/asyncapi/majr-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/majr-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/majr-app/data-model/majr-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/majr-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/majr-app/changelog/majr-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/majr-app-changelog.yml
- group: design
  href: https://artifacts.apis.io/majr-app/errors/majr-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/majr-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/majr-app/conformance/majr-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/majr-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/majr-app/llms/majr-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/majr-app-llms.txt
- group: other
  href: https://artifacts.apis.io/majr-app/hosts/majr-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/majr-app-hosts.yml
- group: auth
  href: https://artifacts.apis.io/majr-app/authentication/majr-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/majr-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/majr-app/security/majr-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/majr-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://majr.app/
- group: docs
  title: ''
  type: Documentation
  url: https://dispatch.majr.app/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dispatch.majr.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://majr.app/quickstart/seo
- group: operate
  title: ''
  type: ChangeLog
  url: https://majr.app/whats-new
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://majr.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://majr.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://majr.app/keys/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dispatch.majr.app/openapi.json
  - status: null
    url: https://encoding.majr.app/openapi.json
  - status: null
    url: https://seo.majr.app/openapi.json
  - status: 401
    url: https://dispatch.majr.app/mcp
  - status: 401
    url: https://encoding.majr.app/mcp
  - status: 401
    url: https://seo.majr.app/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: MAJR provides agent services that expose shared, product‑neutral capabilities such as Dispatch (release‑note generation), AI SEO (search‑engine and AI answer‑engine optimization), and Media Encoding (video, audio, and image processing). These services are offered via a simple MCP‑based HTTP interface with a single bearer‑auth key, enabling developers to integrate powerful media and marketing functions without building them from scratch. The platform is hosted at majr.app and documented across sub‑domains for each service.
image: https://majr.app/og.jpg?v=1
json_schemas:
- name: AuditRequest
  property_count: 2
  slug: majr-app-audit-request
- name: AuditResponse
  property_count: 6
  slug: majr-app-audit-response
- name: DraftRequest
  property_count: 5
  slug: majr-app-draft-request
- name: DraftResponse
  property_count: 2
  slug: majr-app-draft-response
- name: EncodeRequest
  property_count: 8
  slug: majr-app-encode-request
- name: EncodeStatus
  property_count: 2
  slug: majr-app-encode-status
- name: HeadRequest
  property_count: 9
  slug: majr-app-head-request
- name: JobState
  property_count: 8
  slug: majr-app-job-state
- name: LlmsTxtRequest
  property_count: 6
  slug: majr-app-llms-txt-request
- name: RobotsRequest
  property_count: 5
  slug: majr-app-robots-request
- name: SitemapRequest
  property_count: 3
  slug: majr-app-sitemap-request
- name: UploadContract
  property_count: 4
  slug: majr-app-upload-contract
- name: UploadRequest
  property_count: 1
  slug: majr-app-upload-request
- name: UsageResponse
  property_count: 6
  slug: majr-app-usage-response
- name: VoiceResponse
  property_count: 3
  slug: majr-app-voice-response
jsonld:
- class_count: 33
  name: Majr App Context
  property_count: 82
  slug: majr-app-context
layout: provider
modified: '2026-10-29'
name: majr-app
nav: Providers
network: true
overview: 'majr-app publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Discovery API, Drafting API, and 7 more. Tagged areas include Company, Artificial Intelligence, Media, SEO, and Encoding.


  The majr-app catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  majr-app''s developer surface includes changelog, authentication, documentation, getting-started guide, signup flow, and 17 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: majr-app API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: majr-app-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 37.4
    discoverability: 78.6
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/majr-app/majr-app-2026-11-03T135257.png
security:
- kind: authentication
  name: Majr App Authentication
  slug: majr-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Majr App Domain Security
  slug: majr-app-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: dispatch
  slug: majr-app-dispatch
- name: encoding
  slug: majr-app-encoding
- name: seo
  slug: majr-app-seo
slug: majr-app
tags:
- Company
- Artificial Intelligence
- Media
- SEO
- Encoding
- Agent Services
website: https://majr.app/
---
