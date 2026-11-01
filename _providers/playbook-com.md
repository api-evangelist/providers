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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.playbook.com/v1
  baseurl_source: declared
  description: 'Playbook API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Playbook API
  slug: playbook-com-api
artifact_total: 13
asyncapis:
- description: ''
  name: Playbook Com Webhooks
  slug: playbook-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/playbook-com/plans/playbook-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/playbook-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/playbook-com/rules/playbook-com-rules.yml
  title: ''
  type: Spectral
  url: rules/playbook-com-rules.yml
- group: design
  href: https://artifacts.apis.io/playbook-com/json-ld/playbook-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/playbook-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/playbook-com/vocabulary/playbook-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/playbook-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/playbook-com/asyncapi/playbook-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/playbook-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/playbook-com/data-model/playbook-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/playbook-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/playbook-com/conventions/playbook-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/playbook-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/playbook-com/authentication/playbook-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/playbook-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/playbook-com/conformance/playbook-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/playbook-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/playbook-com/llms/playbook-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/playbook-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/playbook-com/well-known/playbook-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/playbook-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/playbook-com/well-known/playbook-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/playbook-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/playbook-com/hosts/playbook-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/playbook-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/playbook-com/vendors/playbook-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/playbook-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/playbook-com/packages/playbook-com-packages.yml
  title: ''
  type: Packages
  url: packages/playbook-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.playbook.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.playbook.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.playbook.com/sign-up/
- group: build
  title: ''
  type: SDKs
  url: https://www.playbook.com/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.playbook.com/privacy/
- group: auth
  href: https://artifacts.apis.io/playbook-com/security/playbook-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/playbook-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.playbook.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.playbook.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.playbook.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.playbook.com/docs/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.playbook.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.playbook.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.playbook.com/contact/
coverage:
  checked: '2026-10-25'
  detail: The API reference page is a JavaScript‑rendered SPA that provides interactive docs but no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dev.playbook.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Playbook provides an all‑in‑one media management platform that helps enterprises, creative agencies, game studios, and consumer brands organize, store, and collaborate on digital assets. Featuring smart workflows, brand‑centric tools, and scalable storage, Playbook enables teams to streamline creative reviews, maintain brand consistency, and accelerate production pipelines across media and entertainment projects.
image: https://www.playbook.com/og-default.jpg
json_schemas:
- name: GetV1OrgAssetsTokenResponse
  property_count: 1
  slug: playbook-com-get-v1-org-assets-token-response
- name: GetV1OrganizationsResponse
  property_count: 2
  slug: playbook-com-get-v1-organizations-response
- name: GetV1SlugAssetsTokenCommentsResponse
  property_count: 1
  slug: playbook-com-get-v1-slug-assets-token-comments-response
- name: PostV1SlugAssetsBatchShowRequest
  property_count: 1
  slug: playbook-com-post-v1-slug-assets-batch-show-request
- name: PostV1SlugAssetsBatchShowResponse
  property_count: 3
  slug: playbook-com-post-v1-slug-assets-batch-show-response
- name: PostV1SlugAssetsGroupAssetsResponse
  property_count: 6
  slug: playbook-com-post-v1-slug-assets-group-assets-response
jsonld:
- class_count: 9
  name: Playbook Com Context
  property_count: 2
  slug: playbook-com-context
layout: provider
modified: '2026-10-25'
name: Playbook
nav: Providers
network: true
overview: 'Playbook is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media Management, Creative Collaboration, Digital Asset Management, Enterprise Software, and Marketing.


  The Playbook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Playbook''s developer surface includes authentication, signup flow, API reference, getting-started guide, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Playbook Com Plans Pricing
  plan_count: 4
  slug: playbook-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Playbook API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: playbook-com-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 31.7
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: unknown
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
  name: Playbook Com Authentication
  slug: playbook-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Playbook Com Domain Security
  slug: playbook-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: playbook-com
tags:
- Media Management
- Creative Collaboration
- Digital Asset Management
- Enterprise Software
- Marketing
website: https://www.playbook.com/
---
