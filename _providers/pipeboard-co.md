---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Pipeboard MCP (Multi‑Channel Platform) API provides programmatic access to advertising campaign management across Meta, Google, TikTok, and other ad networks.
  name: Pipeboard MCP API
  slug: pipeboard-mcp-api
- baseURL: https://api.statuspage.io
  baseurl_source: declared
  description: 'pipeboard-co API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: pipeboard-co API
  slug: pipeboard-co-api
artifact_total: 14
common:
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-pipeboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-pipeboard-security.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-dev-security.txt
- group: commercial
  href: https://artifacts.apis.io/pipeboard-co/plans/pipeboard-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pipeboard-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pipeboard-co/rules/pipeboard-co-rules.yml
  title: ''
  type: Spectral
  url: rules/pipeboard-co-rules.yml
- group: design
  href: https://artifacts.apis.io/pipeboard-co/json-ld/pipeboard-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pipeboard-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/pipeboard-co/vocabulary/pipeboard-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pipeboard-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pipeboard-co/data-model/pipeboard-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pipeboard-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/pipeboard-co/conformance/pipeboard-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pipeboard-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pipeboard-co/llms/pipeboard-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pipeboard-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-developers-security.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-datahub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-datahub-security.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-data-security.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-apis-security.txt
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeboard-co-api-security.txt
- group: agent
  href: https://artifacts.apis.io/pipeboard-co/well-known/pipeboard-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pipeboard-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/pipeboard-co/hosts/pipeboard-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pipeboard-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/pipeboard-co/vendors/pipeboard-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pipeboard-co-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://pipeboard.co/blog
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/security/pipeboard-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pipeboard-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pipeboard-co/security/pipeboard-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pipeboard-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pipeboard.co/
- group: docs
  title: ''
  type: Documentation
  url: https://pipeboard.co/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://pipeboard.co/auth/signup
- group: start
  title: ''
  type: Login
  url: https://pipeboard.co/auth/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://pipeboard.co/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pipeboard.co/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://pipeboard.co/security
- group: operate
  title: ''
  type: Support
  url: https://pipeboard.co/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pipeboard.co/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://pipeboard.statuspage.io
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.pipeboard.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nictuku
coverage:
  checked: '2026-10-29'
  detail: API access requires authentication; the MCP endpoint https://pipeboard.co/api/mcp returns 401 Unauthorized.
  evidence:
  - status: 401
    url: https://pipeboard.co/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Pipeboard provides an AI‑powered marketing collaboration platform that automates ad agency workflows, integrates with major ad networks (Google, Meta, Amazon), and offers a Multi‑Channel Platform (MCP) for unified campaign management. The service includes token‑based API access, detailed guides, pricing tiers, and a public status page, enabling developers to programmatically manage advertising assets and analytics.
image: https://pipeboard.co/opengraph-image?07123b6d8088653c
json_schemas:
- name: GetLoginResponse
  property_count: 2
  slug: pipeboard-co-get-login-response
- name: GetPagesGytm4Qzbx9T6JsonResponse
  property_count: 45
  slug: pipeboard-co-get-pages-gytm4-qzbx9-t6-json-response
- name: GetV1PagesGytm4Qzbx9T6JsonResponse
  property_count: 2
  slug: pipeboard-co-get-v1-pages-gytm4-qzbx9-t6-json-response
- name: PostRequest
  property_count: 4
  slug: pipeboard-co-post-request
jsonld:
- class_count: 4
  name: Pipeboard Co Context
  property_count: 50
  slug: pipeboard-co-context
layout: provider
modified: '2026-10-29'
name: pipeboard-co
nav: Providers
network: true
overview: 'pipeboard-co is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Artificial Intelligence, Automation, and MCP.


  The pipeboard-co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pipeboard-co''s developer surface includes engineering blog, documentation, getting-started guide, pricing, support, and 28 more developer resources.'
plans:
- name: Pipeboard Co Plans Pricing
  plan_count: 4
  slug: pipeboard-co-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Pipeboard Co Rate Limits
  slug: pipeboard-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: pipeboard-co API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: pipeboard-co-rules
scopes:
- name: Pipeboard Co Scopes
  scope_count: 0
  slug: pipeboard-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 23.8
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pipeboard-co/pipeboard-co-2026-11-03T141233.png
security:
- kind: authentication
  name: Pipeboard Co Authentication
  slug: pipeboard-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pipeboard Co Domain Security
  slug: pipeboard-co-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pipeboard Co Vulnerability Disclosure
  slug: pipeboard-co-vulnerability-disclosure
  summary_line: no policy recorded
slug: pipeboard-co
tags:
- Advertising
- Marketing
- Artificial Intelligence
- Automation
- MCP
website: https://pipeboard.co/
---
