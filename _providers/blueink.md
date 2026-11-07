---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.blueink.com
  baseurl_source: declared
  description: 'BlueInk Technologies API as documented publicly: 42 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: BlueInk Technologies API
  slug: blueink-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/blueink/rules/blueink-rules.yml
  title: ''
  type: Spectral
  url: rules/blueink-rules.yml
- group: design
  href: https://artifacts.apis.io/blueink/json-ld/blueink-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blueink-context.jsonld
- group: design
  href: https://artifacts.apis.io/blueink/vocabulary/blueink-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blueink-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blueink/data-model/blueink-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blueink-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blueink.com/compliance
- group: design
  href: https://artifacts.apis.io/blueink/conformance/blueink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blueink-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blueink/llms/blueink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blueink-llms.txt
- group: auth
  href: https://artifacts.apis.io/blueink/well-known/blueink-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blueink-help-security.txt
- group: agent
  href: https://artifacts.apis.io/blueink/well-known/blueink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blueink-well-known.yml
- group: other
  href: https://artifacts.apis.io/blueink/hosts/blueink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blueink-hosts.yml
- group: other
  href: https://artifacts.apis.io/blueink/vendors/blueink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blueink-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueink.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.blueink.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blueink.com/
- group: auth
  title: ''
  type: Security
  url: https://www.blueink.com/product-release-topics/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueink.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blueink.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.blueink.com/topics/news
- group: start
  title: ''
  type: Login
  url: https://secure.blueink.com/auth/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blueinkhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.blueink.com/docs/esignature-api/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.blueink.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.blueink.com/docs/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://developer.blueink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.blueink.com`
- group: docs
  title: ''
  type: APIReference
  url: https://developer.blueink.com/docs/api/
- group: auth
  href: https://artifacts.apis.io/blueink/security/blueink-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blueink-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/blueink/security/blueink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blueink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blueink.com/
created: '2026-10-20'
description: BlueInk Technologies provides electronic signature software that enables businesses to automate document signing, manage contracts, and integrate eSignature capabilities into their workflows. Their platform offers features such as auto‑detect fields, bulk sending, blueink payments, certificate of evidence, SMS delivery, custom branding, team collaboration, in‑person signing, smart link forms, and real‑time dashboards. BlueInk serves a wide range of industries including education, enterprise, government, insurance, retail, and senior living, positioning itself as a leading DocuSign alternative.
image: https://cdn.prod.website-files.com/64c7b08696f4c7099539f94b/6acd3d265f600cf0b90d7819_blueink-homepage-og-1200x630.png
json_schemas:
- name: GetApiV2BundlesBundleslugFilesResponse
  property_count: 3
  slug: blueink-get-api-v2-bundles-bundleslug-files-response
- name: GetApiV2BundlesF9K2Mq7XlpValidateResponse
  property_count: 3
  slug: blueink-get-api-v2-bundles-f9-k2-mq7-xlp-validate-response
- name: GetApiV2WebhooksHeadersHdrAbc123Response
  property_count: 3
  slug: blueink-get-api-v2-webhooks-headers-hdr-abc123-response
- name: PostBundlesPreparationSessionRequest
  property_count: 4
  slug: blueink-post-bundles-preparation-session-request
- name: PostBundlesRequest
  property_count: 3
  slug: blueink-post-bundles-request
- name: PostTemplatesPreparationSessionRequest
  property_count: 4
  slug: blueink-post-templates-preparation-session-request
jsonld:
- class_count: 39
  name: Blueink Context
  property_count: 30
  slug: blueink-context
layout: provider
modified: '2026-10-20'
name: BlueInk Technologies
nav: Providers
network: true
overview: 'BlueInk Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Signature, Government, Education, Enterprise, and Compliance.


  The BlueInk Technologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlueInk Technologies'' developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, API reference, and 22 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: BlueInk Technologies API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: blueink-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.9
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 22.6
    discoverability: 74.1
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/blueink/blueink-2026-11-03T122049.png
security:
- kind: domain-security
  name: Blueink Domain Security
  slug: blueink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blueink Trust Center
  slug: blueink-trust-center
  summary_line: HIPAA, GDPR
slug: blueink
tags:
- E-Signature
- Government
- Education
- Enterprise
- Compliance
- Workflows
- Integration
website: https://blueink.com/
---
