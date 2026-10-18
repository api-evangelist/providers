---
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-10-17'
api_count: 8
apis:
- description: API for Copyleaks plagiarism detection and content authenticity services.
  name: Copyleaks API
  slug: copyleaks-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The Ai Image Detector Async API from Copyleaksplagiarismchecker — 1 operation(s) for ai image detector async.
  name: Copyleaksplagiarismchecker Ai Image Detector Async API
  slug: copyleaksplagiarismchecker-ai-image-detector-async-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The Ai Video Detector API from Copyleaksplagiarismchecker — 1 operation(s) for ai video detector.
  name: Copyleaksplagiarismchecker Ai Video Detector API
  slug: copyleaksplagiarismchecker-ai-video-detector-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The Downloads API from Copyleaksplagiarismchecker — 1 operation(s) for downloads.
  name: Copyleaksplagiarismchecker Downloads API
  slug: copyleaksplagiarismchecker-downloads-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The My Scan 123 API from Copyleaksplagiarismchecker — 1 operation(s) for my scan 123.
  name: Copyleaksplagiarismchecker My Scan 123 API
  slug: copyleaksplagiarismchecker-my-scan-123-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The Repositories API from Copyleaksplagiarismchecker — 1 operation(s) for repositories.
  name: Copyleaksplagiarismchecker Repositories API
  slug: copyleaksplagiarismchecker-repositories-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The Scans API from Copyleaksplagiarismchecker — 5 operation(s) for scans.
  name: Copyleaksplagiarismchecker Scans API
  slug: copyleaksplagiarismchecker-scans-api
- baseURL: https://api.copyleaks.com
  baseurl_source: declared
  description: The Writer Detector API from Copyleaksplagiarismchecker — 2 operation(s) for writer detector.
  name: Copyleaksplagiarismchecker Writer Detector API
  slug: copyleaksplagiarismchecker-writer-detector-api
artifact_total: 21
asyncapis:
- description: ''
  name: Copyleaksplagiarismchecker Webhooks
  slug: copyleaksplagiarismchecker-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/rate-limits/copyleaksplagiarismchecker-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/copyleaksplagiarismchecker-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/plans/copyleaksplagiarismchecker-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/copyleaksplagiarismchecker-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/rules/copyleaksplagiarismchecker-rules.yml
  title: ''
  type: Spectral
  url: rules/copyleaksplagiarismchecker-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/json-ld/copyleaksplagiarismchecker-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/copyleaksplagiarismchecker-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/vocabulary/copyleaksplagiarismchecker-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/copyleaksplagiarismchecker-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/asyncapi/copyleaksplagiarismchecker-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/copyleaksplagiarismchecker-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/data-model/copyleaksplagiarismchecker-data-model.yml
  title: ''
  type: DataModel
  url: data-model/copyleaksplagiarismchecker-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/changelog/copyleaksplagiarismchecker-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/copyleaksplagiarismchecker-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/authentication/copyleaksplagiarismchecker-authentication.yml
  title: ''
  type: Authentication
  url: authentication/copyleaksplagiarismchecker-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/conformance/copyleaksplagiarismchecker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/copyleaksplagiarismchecker-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/llms/copyleaksplagiarismchecker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/copyleaksplagiarismchecker-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/well-known/copyleaksplagiarismchecker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/copyleaksplagiarismchecker-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/hosts/copyleaksplagiarismchecker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copyleaksplagiarismchecker-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/vendors/copyleaksplagiarismchecker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/copyleaksplagiarismchecker-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://copyleaks.com/termsofuse
- group: operate
  title: ''
  type: Support
  url: https://help.copyleaks.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://copyleaks.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://copyleaks.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://copyleaks.com/about-us/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://copyleaks.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://copyleaks.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.copyleaks.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.copyleaks.com/get-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.copyleaks.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Copyleaks
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copyleaksplagiarismchecker/refs/heads/main/security/copyleaksplagiarismchecker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copyleaksplagiarismchecker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://copyleaks.com
coverage:
  checked: '2026-10-11'
  detail: Documentation provides endpoint details but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.copyleaks.com/reference/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Copyleaks provides AI-powered plagiarism detection and content authenticity solutions for businesses, educators, and developers. Their platform offers text, image, and video plagiarism checking, deepfake detection, and content moderation tools, with API access for integration into LMS, CMS, and custom applications. Copyleaks serves a global customer base across education, media, and enterprise sectors, emphasizing AI-driven accuracy and compliance.
image: https://copyleaks.com/wp-content/uploads/2023/02/Feature_Image-01.png?_t=1782892736
json_schemas:
- name: GetV3RepositoriesRepositoryMyRepo123InfoResponse
  property_count: 9
  slug: copyleaksplagiarismchecker-get-v3-repositories-repository-my-repo123-info-response
- name: PostV1V1IdMyScan123CheckResponse
  property_count: 7
  slug: copyleaksplagiarismchecker-post-v1-v1-id-my-scan123-check-response
- name: PostV2WriterDetectorMyScan123CheckResponse
  property_count: 1
  slug: copyleaksplagiarismchecker-post-v2-writer-detector-my-scan123-check-response
- name: PostV3DownloadsMyScan123ExportMyExport1Request
  property_count: 5
  slug: copyleaksplagiarismchecker-post-v3-downloads-my-scan123-export-my-export1-request
- name: PutV3ScansSubmitSubmitidMyScan123Request
  property_count: 4
  slug: copyleaksplagiarismchecker-put-v3-scans-submit-submitid-my-scan123-request
- name: PutV3ScansSubmitSubmitidMyScan123Response
  property_count: 4
  slug: copyleaksplagiarismchecker-put-v3-scans-submit-submitid-my-scan123-response
jsonld:
- class_count: 17
  name: Copyleaksplagiarismchecker Context
  property_count: 45
  slug: copyleaksplagiarismchecker-context
layout: provider
modified: '2026-10-10'
name: Copyleaksplagiarismchecker
nav: Providers
network: true
overview: 'Copyleaksplagiarismchecker is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Ai Image Detector Async API, Ai Video Detector API, Downloads API, and 5 more. Tagged areas include AI Detection, Plagiarism Checker, Content Integrity, Education, and Enterprise.


  The Copyleaksplagiarismchecker catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Copyleaksplagiarismchecker''s developer surface includes changelog, authentication, support, pricing, engineering blog, API reference, getting-started guide, and 20 more developer resources.'
plans:
- name: Copyleaksplagiarismchecker Plans Pricing
  plan_count: 6
  slug: copyleaksplagiarismchecker-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Copyleaksplagiarismchecker Rate Limits
  slug: copyleaksplagiarismchecker-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Copyleaksplagiarismchecker API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: copyleaksplagiarismchecker-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 84.0
    catalog_earned_first_party: 24.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 33.8
    developer_ergonomics: 47.6
    discoverability: 71.4
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Copyleaksplagiarismchecker Authentication
  slug: copyleaksplagiarismchecker-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Copyleaksplagiarismchecker Domain Security
  slug: copyleaksplagiarismchecker-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: copyleaksplagiarismchecker
tags:
- AI Detection
- Plagiarism Checker
- Content Integrity
- Education
- Enterprise
- Media Publishing
- API Integration
website: https://copyleaks.com
---
