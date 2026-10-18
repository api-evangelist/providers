---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Audiostack API providing audio generation and management endpoints.
  name: Audiostack API
  slug: audiostack-api-2
- baseURL: https://v2.api.audio
  baseurl_source: declared
  description: The Content API from AudioStack — 2 operation(s) for content.
  name: AudioStack Content API
  slug: audiostack-content-api
- baseURL: https://v2.api.audio
  baseurl_source: declared
  description: The Creator API from AudioStack — 2 operation(s) for creator.
  name: AudioStack Creator API
  slug: audiostack-creator-api
artifact_total: 11
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://help.audiostack.ai/en/articles/14323269-instantcreative-sales-quick-start
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/rules/audiostack-rules.yml
  title: ''
  type: Spectral
  url: rules/audiostack-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/json-ld/audiostack-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audiostack-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/vocabulary/audiostack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audiostack-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/data-model/audiostack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audiostack-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/changelog/audiostack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/audiostack-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://audiostack.ai/trust-security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/authentication/audiostack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audiostack-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/conformance/audiostack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audiostack-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/llms/audiostack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audiostack-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/well-known/audiostack-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audiostack-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/well-known/audiostack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audiostack-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/hosts/audiostack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audiostack-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/vendors/audiostack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audiostack-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/packages/audiostack-packages.yml
  title: ''
  type: SDKs
  url: packages/audiostack-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/packages/audiostack-packages.yml
  title: ''
  type: Packages
  url: packages/audiostack-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.audiostack.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.audiostack.ai/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/security/audiostack-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/audiostack-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audiostack/refs/heads/main/security/audiostack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audiostack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audiostack.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://audiostack.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.audiostack.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.audiostack.ai/reference/quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.audiostack.ai/en/
- group: company
  title: ''
  type: Blog
  url: https://audiostack.ai/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audiostack.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audiostack.ai/legal/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docs.audiostack.ai/mcp
  - status: 403
    url: https://help.audiostack.ai/mcp
  - status: 200
    url: https://audiostack.ai
  reason: partner-login
  state: gated
created: '2026-10-13'
description: AudioStack provides an AI-driven audio production platform that automates creation of broadcast‑ready audio for agencies, brands, ad‑tech platforms, radio, and video producers. Leveraging a library of 2,600+ voices and over 1,000 sonic assets, it can generate hyper‑local ads at scale, delivering thousands of ads in days with up to 90% faster turnaround. The platform offers embeddable APIs for dynamic creative, story engine, and instant creative solutions, supporting personalized audio content across multiple channels.
json_schemas:
- name: GetCreatorStoryStoryidResponse
  property_count: 2
  slug: audiostack-get-creator-story-storyid-response
- name: PostContentScriptRequest
  property_count: 4
  slug: audiostack-post-content-script-request
- name: PostCreatorStoryResponse
  property_count: 3
  slug: audiostack-post-creator-story-response
jsonld:
- class_count: 3
  name: Audiostack Context
  property_count: 4
  slug: audiostack-context
layout: provider
modified: '2026-10-13'
name: AudioStack
nav: Providers
network: true
overview: 'AudioStack is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Content API, Creator API, and 1 more. Tagged areas include Company, Artificial Intelligence, Audio, Advertising, and Platform.


  The AudioStack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AudioStack''s developer surface includes getting-started guide, changelog, authentication, documentation, API reference, support, engineering blog, and 21 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AudioStack API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: audiostack-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 21.9
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Audiostack Authentication
  slug: audiostack-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Audiostack Domain Security
  slug: audiostack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Audiostack Trust Center
  slug: audiostack-trust-center
  summary_line: SOC 2, GDPR
slug: audiostack
tags:
- Company
- Artificial Intelligence
- Audio
- Advertising
- Platform
website: https://audiostack.ai
---
