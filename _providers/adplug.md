---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Adplug Agentic Access
  operation_count: 35
  slug: adplug-agentic-access
  summary_line: 35 operations · 15 acting
api_count: 1
apis:
- description: MCP Ads Platform API providing OAuth endpoints for Google, LinkedIn, Microsoft, and Meta Ads.
  name: AdPlug API
  slug: adplug-api
- baseURL: https://api.adplug.app
  baseurl_source: declared
  description: The Health API from AdPlug — 1 operation(s) for health.
  name: AdPlug Health API
  slug: adplug-health-api
- baseURL: https://api.adplug.app
  baseurl_source: declared
  description: The Mcp API from AdPlug — 1 operation(s) for mcp.
  name: AdPlug MCP API
  slug: adplug-mcp-api
- baseURL: https://api.adplug.app
  baseurl_source: declared
  description: The oauth API from AdPlug — 13 operation(s) for oauth.
  name: AdPlug OAuth API
  slug: adplug-oauth-api
- baseURL: https://api.adplug.app
  baseurl_source: declared
  description: The oauth-legacy-compat API from AdPlug — 3 operation(s) for oauth-legacy-compat.
  name: AdPlug OAUTH Legacy Compat API
  slug: adplug-oauth-legacy-compat-api
- baseURL: https://api.adplug.app
  baseurl_source: declared
  description: The Users API from AdPlug — 14 operation(s) for users.
  name: AdPlug Users API
  slug: adplug-users-api
- baseURL: https://api.adplug.app
  baseurl_source: declared
  description: The Webhooks API from AdPlug — 2 operation(s) for webhooks.
  name: AdPlug Webhooks API
  slug: adplug-webhooks-api
artifact_total: 18
common:
- group: docs
  title: ''
  type: Documentation
  url: https://adplug.app/guides/google-ads
- group: agent
  href: https://artifacts.apis.io/adplug/agentic-access/adplug-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adplug-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/adplug/plans/adplug-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adplug-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adplug/rules/adplug-rules.yml
  title: ''
  type: Spectral
  url: rules/adplug-rules.yml
- group: design
  href: https://artifacts.apis.io/adplug/json-ld/adplug-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adplug-context.jsonld
- group: design
  href: https://artifacts.apis.io/adplug/vocabulary/adplug-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adplug-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adplug/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adplug/data-model/adplug-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adplug-data-model.yml
- group: design
  href: https://artifacts.apis.io/adplug/errors/adplug-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adplug-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adplug/conformance/adplug-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adplug-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adplug/llms/adplug-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adplug-llms.txt
- group: agent
  href: https://artifacts.apis.io/adplug/well-known/adplug-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adplug-well-known.yml
- group: other
  href: https://artifacts.apis.io/adplug/hosts/adplug-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adplug-hosts.yml
- group: other
  href: https://artifacts.apis.io/adplug/vendors/adplug-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adplug-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adplug/authentication/adplug-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adplug-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adplug/security/adplug-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adplug-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adplug.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://adplug.app/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adplug
- group: commercial
  title: ''
  type: Pricing
  url: https://adplug.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://adplug.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adplug.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adplug.app/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/adplug/workspace
created: '2026-10-15'
description: AdPlug provides AI‑powered Marketing Cloud Platforms (MCP) that integrate with Google Ads, LinkedIn Ads, Microsoft Ads, and Google Search Console. It enables agencies and PPC specialists to audit, safely edit, and automate campaign data across multiple accounts using large language models like Claude and ChatGPT. The platform offers multi‑account management, audit logs, team seats, and a suite of guides and resources for performance optimization.
finops:
- has_sources: true
  method: derived
  name: Adplug Finops
  primary_unit: seat
  service_category: ''
  slug: adplug-finops
  template: false
image: https://adplug.app/opengraph-image?2e27cb39d30c0e91
jsonld:
- class_count: 3
  name: Adplug Context
  property_count: 5
  slug: adplug-context
layout: provider
modified: '2026-10-15'
name: AdPlug
nav: Providers
network: true
overview: 'AdPlug publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, MCP API, OAuth API, and 4 more. Tagged areas include PPC, AI Integration, Agency Tools, and Search Console.


  The AdPlug catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AdPlug''s developer surface includes documentation, authentication, getting-started guide, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Adplug Plans Pricing
  plan_count: 4
  slug: adplug-plans-pricing
- name: Adplug Price Estimates
  plan_count: 0
  slug: adplug-price-estimates
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AdPlug API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: adplug-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 61.8
    contract_governance: 35.6
    contract_quality: 43.5
    developer_ergonomics: 26.8
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adplug/adplug-2026-11-03T120320.png
security:
- kind: authentication
  name: Adplug Authentication
  slug: adplug-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adplug Domain Security
  slug: adplug-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: adplug-manage-paddle-subscription
  slug: adplug-manage-paddle-subscription
- name: adplug-oauth-authorization
  slug: adplug-oauth-authorization
- name: adplug-oauth-legacy-compat-flow
  slug: adplug-oauth-legacy-compat-flow
slug: adplug
tags:
- PPC
- AI Integration
- Agency Tools
- Search Console
website: https://adplug.app/
---
