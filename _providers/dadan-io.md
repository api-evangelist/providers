---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://app.dadan.io
  baseurl_source: declared
  description: REST API for creating video recording requests and retrieving their status and video links; authenticated with an X-Dadan-API-Key header, with optional webhook notifications when a recording is submit
  name: Dadan Recording Request API
  slug: recording-request-api
- description: 'Remote MCP server (Streamable HTTP, OAuth 2.1, scopes dadan:full and dadan:read) that lets AI agents search, edit, publish, caption and analyze videos in a Dadan library; tools/list returns 401 until '
  name: Dadan MCP
  slug: dadan-mcp
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/dadan-io/plans/dadan-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dadan-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/rules/dadan-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dadan-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/json-ld/dadan-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dadan-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dadan-io/vocabulary/dadan-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dadan-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dadan-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/data-model/dadan-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dadan-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/components/dadan-io-components.yml
  title: ''
  type: Components
  url: components/dadan-io-components.yml
- group: operate
  href: https://artifacts.apis.io/dadan-io/changelog/dadan-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dadan-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/conventions/dadan-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dadan-io-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dadan.io/privacy-policy
- group: auth
  href: https://artifacts.apis.io/dadan-io/authentication/dadan-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dadan-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dadan-io/scopes/dadan-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dadan-io-scopes.yml
- group: operate
  href: https://artifacts.apis.io/dadan-io/lifecycle/dadan-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dadan-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/lifecycle/dadan-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dadan-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/errors/dadan-io-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dadan-io-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/errors/dadan-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dadan-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dadan-io/conformance/dadan-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dadan-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/dadan-io/overlays/dadan-io-recording-request-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dadan-io-recording-request-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dadan-io/llms/dadan-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dadan-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/dadan-io/well-known/dadan-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dadan-io-security.txt
- group: auth
  href: https://artifacts.apis.io/dadan-io/well-known/dadan-io-dadan-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dadan-io-dadan-security.txt
- group: agent
  href: https://artifacts.apis.io/dadan-io/well-known/dadan-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dadan-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dadan-io/hosts/dadan-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dadan-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/dadan-io/integrations/dadan-io-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dadan-io-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dadan-io/vendors/dadan-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dadan-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/dadan-io/packages/dadan-io-packages.yml
  title: ''
  type: SDKs
  url: packages/dadan-io-packages.yml
- group: build
  href: https://artifacts.apis.io/dadan-io/packages/dadan-io-packages.yml
  title: ''
  type: Packages
  url: packages/dadan-io-packages.yml
- group: auth
  href: https://artifacts.apis.io/dadan-io/security/dadan-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dadan-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dadan-io/security/dadan-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dadan-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dadan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.dadan.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://kb.dadan.io/docs-category/getting-started
- group: operate
  title: ''
  type: Support
  url: https://kb.dadan.io/
- group: company
  title: ''
  type: Blog
  url: https://www.dadan.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.dadan.io/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dadan.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dadan.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dadan.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dadan.io/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: https://www.dadan.io/dadan-mcp
- group: operate
  title: ''
  type: ContactSales
  url: https://www.dadan.io/contact-sales
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/dadan_ltd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dadan/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC93eE9Ruvr5vDQ6lPdsi9XQ
created: '2026-11-05'
description: Dadan (dadan, Inc.) is a video communication platform for recording, editing, hosting and sharing screen and camera videos. It offers interactive videos, engagement analytics, meeting recaps, clipping, caption translation and lead capture, plus desktop apps and business integrations. Dadan MCP connects the platform to AI agents such as Claude and ChatGPT so users can work with their videos and analytics in plain language.
image: https://www.dadan.io/wp-content/uploads/dadan-og-3.png
json_schemas:
- name: PostApiV1UsedadanRequestrecordingRequest
  property_count: 3
  slug: dadan-io-post-api-v1-usedadan-requestrecording-request
jsonld:
- class_count: 1
  name: Dadan Io Context
  property_count: 3
  slug: dadan-io-context
layout: provider
mcp_servers:
- description: ''
  name: Dadan MCP (product page)
  slug: dadan-mcp-product-page
modified: '2026-11-05'
name: Dadan
nav: Providers
network: true
overview: 'Dadan is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Recording Request API, and 1 more. Tagged areas include Company, Video, Screen Recording, Video Hosting, and Video Analytics.


  The Dadan catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dadan''s developer surface includes changelog, authentication, documentation, getting-started guide, support, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Dadan Io Plans Pricing
  plan_count: 4
  slug: dadan-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Dadan Io Rate Limits
  slug: dadan-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Dadan API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: dadan-io-rules
scopes:
- name: Dadan Io Scopes
  scope_count: 2
  slug: dadan-io-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.2
    catalog_earned_first_party: 12.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 19.0
    developer_ergonomics: 49.4
    discoverability: 65.0
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dadan Io Authentication
  slug: dadan-io-authentication
  summary_line: apiKey/oauth2/publicAppId · 3 schemes
- kind: domain-security
  name: Dadan Io Domain Security
  slug: dadan-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dadan Io Vulnerability Disclosure
  slug: dadan-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dadan-request-recording
  slug: dadan-io-request-recording
slug: dadan-io
tags:
- Company
- Video
- Screen Recording
- Video Hosting
- Video Analytics
- MCP
- AI Agents
website: https://www.dadan.io/
---
