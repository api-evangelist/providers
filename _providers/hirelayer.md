---
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: The HireLayer API API from HireLayer — 1 operation(s) for hirelayer api.
  name: HireLayer HireLayer API
  slug: hirelayer-hirelayer-api-api
- description: The Jobs API from HireLayer — 1 operation(s) for jobs.
  name: HireLayer Jobs API
  slug: hirelayer-jobs-api
- description: The Matching API from HireLayer — 2 operation(s) for matching.
  name: HireLayer Matching API
  slug: hirelayer-matching-api
- description: The Parser API from HireLayer — 2 operation(s) for parser.
  name: HireLayer Parser API
  slug: hirelayer-parser-api
- description: The Skills API from HireLayer — 1 operation(s) for skills.
  name: HireLayer Skills API
  slug: hirelayer-skills-api
artifact_total: 16
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/plans/hirelayer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hirelayer-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/rules/hirelayer-rules.yml
  title: ''
  type: Spectral
  url: rules/hirelayer-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/json-ld/hirelayer-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hirelayer-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/vocabulary/hirelayer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hirelayer-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/data-model/hirelayer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hirelayer-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/authentication/hirelayer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hirelayer-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/conformance/hirelayer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hirelayer-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/llms/hirelayer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hirelayer-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/well-known/hirelayer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hirelayer-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/hosts/hirelayer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hirelayer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/vendors/hirelayer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hirelayer-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/packages/hirelayer-packages.yml
  title: ''
  type: SDKs
  url: packages/hirelayer-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/packages/hirelayer-packages.yml
  title: ''
  type: Packages
  url: packages/hirelayer-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hirelayer.co/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hirelayer.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://hirelayer.co/pricing
- group: start
  title: ''
  type: Login
  url: https://hirelayer.co/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HireLayer
- group: company
  title: ''
  type: Blog
  url: https://hirelayer.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://hirelayer.co/api-docs/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hirelayer/refs/heads/main/security/hirelayer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hirelayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hirelayer.co
- group: docs
  title: ''
  type: Documentation
  url: https://hirelayer.co/api-docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://hirelayer.co/openapi.json
  - status: 401
    url: https://hirelayer.co/mcp
  - status: 200
    url: https://hirelayer.co
  reason: partner-login
  state: gated
created: '2026-10-12'
description: HireLayer provides a suite of recruiting APIs that enable developers to parse resumes, extract structured data, and match candidates to job descriptions. Their platform offers five core APIs covering resume parsing, job parsing, candidate‑job matching, candidate ranking, and skills matching. Users can access these services via a single API key and credit‑based billing, with documentation, pricing, and a free trial available online. The company targets ATS integrations, HR tech solutions, and staffing agencies, positioning itself as a flexible, cloud‑based recruiting API provider.
image: https://hirelayer.co/images/blog/og-image.png
json_schemas:
- name: PostApiV1JobsExtractCriteriaResponse
  property_count: 1
  slug: hirelayer-post-api-v1-jobs-extract-criteria-response
- name: PostApiV1MatchingJobCandidateRequest
  property_count: 3
  slug: hirelayer-post-api-v1-matching-job-candidate-request
- name: PostApiV1MatchingJobCandidateResponse
  property_count: 3
  slug: hirelayer-post-api-v1-matching-job-candidate-response
- name: PostApiV1SkillsResolveResponse
  property_count: 4
  slug: hirelayer-post-api-v1-skills-resolve-response
- name: PostApiV2ParserRequest
  property_count: 2
  slug: hirelayer-post-api-v2-parser-request
- name: PostApiV3ParserResponse
  property_count: 6
  slug: hirelayer-post-api-v3-parser-response
jsonld:
- class_count: 12
  name: Hirelayer Context
  property_count: 20
  slug: hirelayer-context
layout: provider
modified: '2026-10-12'
name: HireLayer
nav: Providers
network: true
overview: 'HireLayer is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including HireLayer API, Jobs API, Matching API, and 2 more. Tagged areas include Company, Recruiting, ResumeParsing, and CandidateMatching.


  The HireLayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HireLayer''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
plans:
- name: Hirelayer Plans Pricing
  plan_count: 7
  slug: hirelayer-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: HireLayer API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: hirelayer-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.6
    developer_ergonomics: 42.9
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hirelayer Authentication
  slug: hirelayer-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hirelayer Domain Security
  slug: hirelayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hirelayer
tags:
- Company
- Recruiting
- ResumeParsing
- CandidateMatching
website: https://hirelayer.co
---
