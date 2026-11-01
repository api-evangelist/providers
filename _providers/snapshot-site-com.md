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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Screenshot API providing capture, visual diff, and AI analysis.
  name: Snapshot Site API
  slug: snapshot-site-api
- baseURL: https://api.prod.ss.snapshot-site.com
  baseurl_source: declared
  description: 'snapshot-site-com API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: snapshot-site-com API
  slug: snapshot-site-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/snapshot-site-com/plans/snapshot-site-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snapshot-site-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/snapshot-site-com/rules/snapshot-site-com-rules.yml
  title: ''
  type: Spectral
  url: rules/snapshot-site-com-rules.yml
- group: design
  href: https://artifacts.apis.io/snapshot-site-com/json-ld/snapshot-site-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snapshot-site-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/snapshot-site-com/vocabulary/snapshot-site-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snapshot-site-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/snapshot-site-com/data-model/snapshot-site-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snapshot-site-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/snapshot-site-com/cli/snapshot-site-com-cli.yml
  title: ''
  type: CLI
  url: cli/snapshot-site-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/snapshot-site-com/authentication/snapshot-site-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snapshot-site-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/snapshot-site-com/conformance/snapshot-site-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snapshot-site-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/snapshot-site-com/llms/snapshot-site-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snapshot-site-com-llms.txt
- group: other
  href: https://artifacts.apis.io/snapshot-site-com/hosts/snapshot-site-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snapshot-site-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/snapshot-site-com/packages/snapshot-site-com-packages.yml
  title: ''
  type: Packages
  url: packages/snapshot-site-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snapshot-site.com/
- group: build
  title: ''
  type: SDKs
  url: https://snapshot-site.com/integrations/sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snapshot-site
- group: start
  title: ''
  type: GettingStarted
  url: https://snapshot-site.com/posts/a-recipe-for-clean-onboarding-tour-screenshots
- group: auth
  href: https://artifacts.apis.io/snapshot-site-com/security/snapshot-site-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snapshot-site-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snapshot-site.com/
- group: docs
  title: ''
  type: Documentation
  url: https://snapshot-site.com/api-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.snapshot-site.com
- group: commercial
  title: ''
  type: Pricing
  url: https://snapshot-site.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://snapshot-site.com/posts
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snapshot-site.com/terms-policy-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snapshot-site.com/terms-policy
created: '2026-10-31'
description: Snapshot Site provides a Screenshot API that captures, compares, and analyzes any web page. It offers pixel‑perfect full‑page screenshots with real browser rendering, visual diff, and AI‑powered page analysis. Users can integrate the API to automate website monitoring, SEO checks, ecommerce tracking, and more, with SDKs for TypeScript, Python, PHP and others. The service includes a console, pricing plans, and extensive documentation for quick integration.
image: https://cdn.snapshot-site.fr/images/banner.jpg
json_schemas:
- name: PostApiV1Request
  property_count: 7
  slug: snapshot-site-com-post-api-v1-request
- name: PostApiV2ScreenshotRequest
  property_count: 7
  slug: snapshot-site-com-post-api-v2-screenshot-request
- name: PostApiV3CompareRequest
  property_count: 11
  slug: snapshot-site-com-post-api-v3-compare-request
- name: PostApiV3CompareResponse
  property_count: 22
  slug: snapshot-site-com-post-api-v3-compare-response
- name: PostV1ScreenshotRequest
  property_count: 7
  slug: snapshot-site-com-post-v1-screenshot-request
- name: PostV3AnalyzeRequest
  property_count: 7
  slug: snapshot-site-com-post-v3-analyze-request
jsonld:
- class_count: 10
  name: Snapshot Site Com Context
  property_count: 41
  slug: snapshot-site-com-context
layout: provider
modified: '2026-10-31'
name: snapshot-site-com
nav: Providers
network: true
overview: 'snapshot-site-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Screenshot, API, AI, and Monitoring.


  The snapshot-site-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  snapshot-site-com''s developer surface includes CLI, authentication, getting-started guide, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Snapshot Site Com Plans Pricing
  plan_count: 4
  slug: snapshot-site-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: snapshot-site-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: snapshot-site-com-rules
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 83.5
    catalog_earned_first_party: 0.0
    catalog_gap: 31.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 55.2
    developer_ergonomics: 59.5
    discoverability: 57.1
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Snapshot Site Com Authentication
  slug: snapshot-site-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Snapshot Site Com Domain Security
  slug: snapshot-site-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: snapshot-site-com
tags:
- Company
- Screenshot
- API
- AI
- Monitoring
website: https://snapshot-site.com/
---
