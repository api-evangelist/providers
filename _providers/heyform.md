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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Heyform Agentic Access
  operation_count: 9
  slug: heyform-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: Authentication and social login (OAuth)
  name: HeyForm Auth API
  slug: heyform-auth-api
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: Runtime configuration
  name: HeyForm Config API
  slug: heyform-config-api
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: Form rendering (public endpoint)
  name: HeyForm Forms API
  slug: heyform-forms-api
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: Image proxy and resizing
  name: HeyForm Images API
  slug: heyform-images-api
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: Export form submission data
  name: HeyForm Submissions API
  slug: heyform-submissions-api
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: File upload
  name: HeyForm Upload API
  slug: heyform-upload-api
- baseURL: https://api.heyform.net
  baseurl_source: declared
  description: Primary data API (GraphQL over HTTP)
  name: HeyForm Graph QL API
  slug: heyform-graph-ql-api
artifact_total: 26
collections:
- collection_type: open
  name: HeyForm Auth API
  slug: open-heyform-auth-api
- collection_type: open
  name: HeyForm Auth Config API
  slug: open-heyform-config-api
- collection_type: open
  name: HeyForm Auth Forms API
  slug: open-heyform-forms-api
- collection_type: open
  name: HeyForm Auth GraphQL API
  slug: open-heyform-graphql-api
- collection_type: open
  name: HeyForm Auth Images API
  slug: open-heyform-images-api
- collection_type: open
  name: HeyForm Auth Submissions API
  slug: open-heyform-submissions-api
- collection_type: open
  name: HeyForm Auth Upload API
  slug: open-heyform-upload-api
common:
- group: agent
  href: https://artifacts.apis.io/heyform/agentic-access/heyform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/heyform-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/heyform/security/heyform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heyform-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/heyform/authentication/heyform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/heyform-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://heyform.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.heyform.net
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/heyform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heyform
- group: company
  title: ''
  type: Blog
  url: https://heyform.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://heyform.net/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://heyform.net
- group: other
  title: ''
  type: X
  url: https://x.com/heyform_net
- group: commercial
  href: https://artifacts.apis.io/heyform/plans/heyform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heyform-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/heyform/rate-limits/heyform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/heyform-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/heyform/finops/heyform-finops.yml
  title: ''
  type: FinOps
  url: finops/heyform-finops.yml
created: '2026-06-13'
description: HeyForm is an open-source conversational form builder that enables anyone to create engaging forms, surveys, quizzes, and polls without coding. It provides a REST API and webhook integrations for creating and managing forms, collecting responses, configuring conditional logic, and embedding forms in any web application. With 30+ integrations including Zapier, Slack, Google Sheets, Airtable, HubSpot, and Stripe, HeyForm suits small businesses and developers who want full data ownership. Licensed under AGPL-3.0, it can be self-hosted or used via the managed cloud service.
examples:
- key_count: 3
  name: Heyform Graphql Complete Submission Example
  slug: heyform-graphql-complete-submission-example
- key_count: 7
  name: Heyform Webhook Payload Example
  slug: heyform-webhook-payload-example
finops:
- has_sources: false
  method: generated
  name: Heyform Finops
  primary_unit: ''
  service_category: ''
  slug: heyform-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heyform.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: HeyForm Form
  property_count: 16
  slug: heyform-form
- name: HeyForm Submission
  property_count: 15
  slug: heyform-submission
jsonld:
- class_count: 16
  name: Heyform Context
  property_count: 55
  slug: heyform-context
layout: provider
modified: '2026-06-13'
name: HeyForm
nav: Providers
network: true
overview: 'HeyForm publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Config API, Forms API, and 4 more. Tagged areas include Forms, Surveys, Quizzes, Polls, and Conversational Forms.


  The HeyForm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HeyForm''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Heyform Plans Pricing
  plan_count: 6
  slug: heyform-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 10
  name: Heyform Rate Limits
  slug: heyform-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: HeyForm — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: heyform-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 9.8
    contract_quality: 51.8
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/heyform/heyform-2026-06-20T182715.png
security:
- kind: authentication
  name: Heyform Authentication
  slug: heyform-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Heyform Domain Security
  slug: heyform-domain-security
  summary_line: TLSv1.3 · DMARC
slug: heyform
tags:
- Forms
- Surveys
- Quizzes
- Polls
- Conversational Forms
- Open Source
- Webhook
- No-Code
- Form Builder
- Self-Hosted
website: https://heyform.net
---
