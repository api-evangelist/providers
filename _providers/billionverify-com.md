---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Billionverify Com Agentic Access
  operation_count: 13
  slug: billionverify-com-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.billionverify.com
  baseurl_source: declared
  description: Account and credits management
  name: BillionVerify Account API
  slug: billionverify-com-account-api
- baseURL: https://api.billionverify.com
  baseurl_source: declared
  description: Batch file upload and processing endpoints
  name: BillionVerify File Processing API
  slug: billionverify-com-file-processing-api
- baseURL: https://api.billionverify.com
  baseurl_source: declared
  description: Health check endpoints
  name: BillionVerify Health API
  slug: billionverify-com-health-api
- baseURL: https://api.billionverify.com
  baseurl_source: declared
  description: Email verification endpoints
  name: BillionVerify Verification API
  slug: billionverify-com-verification-api
- baseURL: https://api.billionverify.com
  baseurl_source: declared
  description: Webhook management endpoints
  name: BillionVerify Webhooks API
  slug: billionverify-com-webhooks-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/billionverify-com/agentic-access/billionverify-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/billionverify-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/billionverify-com/plans/billionverify-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billionverify-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/billionverify-com/rules/billionverify-com-rules.yml
  title: ''
  type: Spectral
  url: rules/billionverify-com-rules.yml
- group: design
  href: https://artifacts.apis.io/billionverify-com/json-ld/billionverify-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billionverify-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/billionverify-com/vocabulary/billionverify-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billionverify-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/billionverify-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/billionverify-com/data-model/billionverify-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billionverify-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://billionverify.com/trust
- group: auth
  href: https://artifacts.apis.io/billionverify-com/authentication/billionverify-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billionverify-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/billionverify-com/errors/billionverify-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/billionverify-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/billionverify-com/conformance/billionverify-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billionverify-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/billionverify-com/llms/billionverify-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billionverify-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/billionverify-com/well-known/billionverify-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billionverify-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/billionverify-com/hosts/billionverify-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billionverify-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/billionverify-com/vendors/billionverify-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billionverify-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://billionverify.com/integrations/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billionverify.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.billionverify.com/
- group: auth
  title: ''
  type: Security
  url: https://billionverify.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billionverify.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BillionVerify
- group: start
  title: ''
  type: SignUp
  url: https://billionverify.com/auth/sign-up.md
- group: start
  title: ''
  type: GettingStarted
  url: https://billionverify.com/docs/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.billionverify.com`
- group: docs
  title: ''
  type: APIReference
  url: https://billionverify.com/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/billionverify-com/security/billionverify-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/billionverify-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/billionverify-com/security/billionverify-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billionverify-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billionverify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://billionverify.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://billionverify.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://billionverify.com/blog
- group: company
  title: ''
  type: About
  url: https://billionverify.com/about
created: '2026-11-02'
description: BillionVerify provides an email verification service with real‑time SMTP checks, bulk list cleaning, and a robust API for developers and AI agents. Users can validate single emails or upload large lists, receiving detailed deliverability status, risk scores, and actionable insights. The platform offers free daily credits, tiered pricing, and comprehensive documentation, supporting multiple languages and integrations.
image: https://billionverify.com/og/email-verification-tool.webp
json_schemas:
- name: ApiResponse
  property_count: 4
  slug: billionverify-com-api-response
- name: BatchVerifyRequest
  property_count: 4
  slug: billionverify-com-batch-verify-request
- name: FileUploadRequest
  property_count: 4
  slug: billionverify-com-file-upload-request
- name: SingleVerifyApiResponse
  property_count: 5
  slug: billionverify-com-single-verify-api-response
- name: SingleVerifyRequest
  property_count: 4
  slug: billionverify-com-single-verify-request
- name: WebhookCreateRequest
  property_count: 2
  slug: billionverify-com-webhook-create-request
jsonld:
- class_count: 19
  name: Billionverify Com Context
  property_count: 114
  slug: billionverify-com-context
layout: provider
modified: '2026-11-02'
name: BillionVerify
nav: Providers
network: true
overview: 'BillionVerify publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, File Processing API, Health API, and 2 more. Tagged areas include Email Verification, Software-as-a-Service, Data Quality, and B2B.


  The BillionVerify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BillionVerify''s developer surface includes authentication, support, signup flow, getting-started guide, API reference, documentation, pricing, and 25 more developer resources.'
plans:
- name: Billionverify Com Plans Pricing
  plan_count: 18
  slug: billionverify-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: BillionVerify API Rules
  rule_count: 70
  severity_counts:
    error: 63
    hint: 0
    info: 2
    warn: 5
  slug: billionverify-com-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 36.3
    discoverability: 57.1
    operational_transparency: 11.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Billionverify Com Authentication
  slug: billionverify-com-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Billionverify Com Domain Security
  slug: billionverify-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Billionverify Com Trust Center
  slug: billionverify-com-trust-center
  summary_line: SOC 2, GDPR
skill_count: 2
skills:
- name: billionverify-com-file-verification
  slug: billionverify-com-file-verification
- name: billionverify-com-manage-webhooks
  slug: billionverify-com-manage-webhooks
slug: billionverify-com
tags:
- Email Verification
- Software-as-a-Service
- Data Quality
- B2B
website: https://billionverify.com/
---
