---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Allscreenshots Com Agentic Access
  operation_count: 2
  slug: allscreenshots-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Capture website screenshots, PDFs, and page outputs via API.
  name: Allscreenshots API
  slug: allscreenshots-api
- baseURL: https://api.allscreenshots.com
  baseurl_source: declared
  description: The Screenshots API from allscreenshots-com — 2 operation(s) for screenshots.
  name: allscreenshots-com Screenshots API
  slug: allscreenshots-com-screenshots-api
artifact_total: 13
asyncapis:
- description: ''
  name: Allscreenshots Com Webhooks
  slug: allscreenshots-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/allscreenshots-com/agentic-access/allscreenshots-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/allscreenshots-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/allscreenshots-com/plans/allscreenshots-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allscreenshots-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/rules/allscreenshots-com-rules.yml
  title: ''
  type: Spectral
  url: rules/allscreenshots-com-rules.yml
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/json-ld/allscreenshots-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allscreenshots-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/vocabulary/allscreenshots-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allscreenshots-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/asyncapi/allscreenshots-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/allscreenshots-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/data-model/allscreenshots-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allscreenshots-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/errors/allscreenshots-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allscreenshots-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/allscreenshots-com/conformance/allscreenshots-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allscreenshots-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allscreenshots-com/llms/allscreenshots-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allscreenshots-com-llms.txt
- group: other
  href: https://artifacts.apis.io/allscreenshots-com/a2a/allscreenshots-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/allscreenshots-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/allscreenshots-com/well-known/allscreenshots-com-crates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allscreenshots-com-crates-security.txt
- group: agent
  href: https://artifacts.apis.io/allscreenshots-com/well-known/allscreenshots-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allscreenshots-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/allscreenshots-com/hosts/allscreenshots-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allscreenshots-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allscreenshots-com/vendors/allscreenshots-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allscreenshots-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allscreenshots.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allscreenshots.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allscreenshots
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.allscreenshots.com/getting-started/quickstart
- group: auth
  href: https://artifacts.apis.io/allscreenshots-com/authentication/allscreenshots-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allscreenshots-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/allscreenshots-com/security/allscreenshots-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allscreenshots-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allscreenshots.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.allscreenshots.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.allscreenshots.com/api-reference/screenshots
- group: commercial
  title: ''
  type: Pricing
  url: https://allscreenshots.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://allscreenshots.com/blog
- group: operate
  title: ''
  type: Changelog
  url: https://allscreenshots.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://allscreenshots.com/support
created: '2026-10-30'
description: Allscreenshots provides a screenshot API that enables developers, marketers, and founders to capture website screenshots programmatically. With a single API call, users can obtain pixel‑perfect images of any web page, customize output formats, handle full‑page captures, and integrate blocking of unwanted elements. The service offers a free tier with 100 screenshots, global regions, high uptime, and no infrastructure to manage, making it ideal for automating visual testing, content generation, and social media assets.
image: https://og.allscreenshots.com/?url=https%3A%2F%2Fallscreenshots.com%2F
json_schemas:
- name: ScreenshotRequest
  property_count: 11
  slug: allscreenshots-com-screenshot-request
- name: ScreenshotResponse
  property_count: 4
  slug: allscreenshots-com-screenshot-response
jsonld:
- class_count: 2
  name: Allscreenshots Com Context
  property_count: 14
  slug: allscreenshots-com-context
layout: provider
modified: '2026-10-30'
name: allscreenshots-com
nav: Providers
network: true
overview: 'allscreenshots-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Screenshots API, and 1 more. Tagged areas include Company, ScreenshotAPI, Automation, Marketing, and Developers.


  The allscreenshots-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  allscreenshots-com''s developer surface includes getting-started guide, authentication, documentation, API reference, pricing, engineering blog, changelog, and 21 more developer resources.'
plans:
- name: Allscreenshots Com Plans Pricing
  plan_count: 5
  slug: allscreenshots-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: allscreenshots-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: allscreenshots-com-rules
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 76.5
    catalog_earned_first_party: 0.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 58.7
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 23.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Allscreenshots Com Authentication
  slug: allscreenshots-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Allscreenshots Com Domain Security
  slug: allscreenshots-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: create-async-screenshot
  slug: allscreenshots-com-create-async-screenshot
- name: create-screenshot
  slug: allscreenshots-com-create-screenshot
slug: allscreenshots-com
tags:
- Company
- ScreenshotAPI
- Automation
- Marketing
- Developers
website: https://allscreenshots.com/
---
