---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for Contentrain Studio providing content generation and management features.
  name: Contentrain Studio API
  slug: contentrain-studio-api
- description: 'Contentrain API as documented publicly: 51 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Contentrain API
  slug: contentrain-io-api
artifact_total: 13
asyncapis:
- description: ''
  name: Contentrain Io Webhooks
  slug: contentrain-io-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/contentrain-io/plans/contentrain-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contentrain-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contentrain-io/rules/contentrain-io-rules.yml
  title: ''
  type: Spectral
  url: rules/contentrain-io-rules.yml
- group: design
  href: https://artifacts.apis.io/contentrain-io/json-ld/contentrain-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contentrain-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/contentrain-io/vocabulary/contentrain-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contentrain-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contentrain-io/asyncapi/contentrain-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contentrain-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/contentrain-io/data-model/contentrain-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contentrain-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/contentrain-io/changelog/contentrain-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contentrain-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/contentrain-io/conformance/contentrain-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contentrain-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contentrain-io/llms/contentrain-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contentrain-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/contentrain-io/well-known/contentrain-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contentrain-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/contentrain-io/hosts/contentrain-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentrain-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/contentrain-io/vendors/contentrain-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentrain-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contentrain.io/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://contentrain.io/support
- group: auth
  title: ''
  type: Security
  url: https://contentrain.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contentrain.io/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://contentrain.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Contentrain
- group: start
  title: ''
  type: DeveloperPortal
  url: https://contentrain.io/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.contentrain.io/developer/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.contentrain.io/developer/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.contentrain.io/guide/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contentrain.io/
- group: auth
  href: https://artifacts.apis.io/contentrain-io/security/contentrain-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentrain-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contentrain.io/
coverage:
  checked: '2026-11-04'
  detail: API reference page renders via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.contentrain.io/developer/api-reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Contentrain provides open‑source developer tools and a Studio workflow that enable teams to govern AI‑generated UI copy, documentation and locale strings within Git repositories. It lets developers create, review and approve content changes through Git‑native models, and allows non‑developers to edit content in Studio while preserving branch, diff and validation controls.
image: https://contentrain.io/og-contentrain-1200x630.png
json_schemas:
- name: GetApiMediaV1ProjectidAssetsAssetidResponse
  property_count: 13
  slug: contentrain-io-get-api-media-v1-projectid-assets-assetid-response
- name: GetApiWorkspacesWorkspaceidProjectsProjectidCdnBuildsRespons
  property_count: 12
  slug: contentrain-io-get-api-workspaces-workspaceid-projects-projectid-cdn-builds-respons
- name: GetApiWorkspacesWorkspaceidProjectsProjectidMediaAssetidResp
  property_count: 13
  slug: contentrain-io-get-api-workspaces-workspaceid-projects-projectid-media-assetid-resp
- name: PatchApiWorkspacesWorkspaceidProjectsProjectidMediaAssetidRe2
  property_count: 13
  slug: contentrain-io-patch-api-workspaces-workspaceid-projects-projectid-media-assetid-re2
- name: PostApiMediaV1ProjectidAssetsRequest
  property_count: 5
  slug: contentrain-io-post-api-media-v1-projectid-assets-request
- name: PostApiMediaV1ProjectidAssetsResponse
  property_count: 15
  slug: contentrain-io-post-api-media-v1-projectid-assets-response
jsonld:
- class_count: 49
  name: Contentrain Io Context
  property_count: 74
  slug: contentrain-io-context
layout: provider
modified: '2026-11-04'
name: Contentrain
nav: Providers
network: true
overview: 'Contentrain is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Content Governance, Developer Tools, AI content, Studio Workflow, and Localization.


  The Contentrain catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Contentrain''s developer surface includes changelog, support, pricing, API reference, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Contentrain Io Plans Pricing
  plan_count: 4
  slug: contentrain-io-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Contentrain API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 1
  slug: contentrain-io-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 35.0
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contentrain Io Domain Security
  slug: contentrain-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contentrain-io
tags:
- Content Governance
- Developer Tools
- AI content
- Studio Workflow
- Localization
website: https://contentrain.io/
---
