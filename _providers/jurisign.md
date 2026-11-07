---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Credit balance and plan
  name: JuriSign Account API
  slug: jurisign-account-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Obtain and revoke API tokens
  name: JuriSign Authentication API
  slug: jurisign-authentication-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Merge templates and bulk campaigns (one individualised request per recipient)
  name: JuriSign Bulk API
  slug: jurisign-bulk-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Upload and manage PDF documents
  name: JuriSign Documents API
  slug: jurisign-documents-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: 'Shareable links: each respondent signs their own generated request, no account needed'
  name: JuriSign Public Forms API
  slug: jurisign-public-forms-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Create, send, and track signature requests
  name: JuriSign Sign Requests API
  slug: jurisign-sign-requests-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Reusable sign request templates
  name: JuriSign Templates API
  slug: jurisign-templates-api
- baseURL: https://www.jurisign.fr/api/v1
  baseurl_source: declared
  description: Manage webhook endpoints for event notifications
  name: JuriSign Webhooks API
  slug: jurisign-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Jurisign Webhooks
  slug: jurisign-webhooks
common:
- group: other
  href: https://artifacts.apis.io/jurisign/capabilities/jurisign-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jurisign-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.jurisign.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.jurisign.fr/developpeurs
- group: docs
  title: ''
  type: Documentation
  url: https://www.jurisign.fr/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.jurisign.fr/api/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jurisign.fr/api/guide
- group: operate
  title: ''
  type: Support
  url: https://www.jurisign.fr/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.jurisign.fr/aide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jurisign.fr/tarifs
- group: start
  title: ''
  type: SignUp
  url: https://www.jurisign.fr/register
- group: start
  title: ''
  type: Login
  url: https://www.jurisign.fr/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jurisign.fr/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jurisign.fr/confidentialite
- group: auth
  href: https://artifacts.apis.io/jurisign/authentication/jurisign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jurisign-authentication.yml
- group: auth
  href: https://artifacts.apis.io/jurisign/scopes/jurisign-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/jurisign-scopes.yml
- group: design
  href: https://artifacts.apis.io/jurisign/conventions/jurisign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jurisign-conventions.yml
- group: design
  href: https://artifacts.apis.io/jurisign/conventions/jurisign-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jurisign-conventions.yml
- group: design
  href: https://artifacts.apis.io/jurisign/errors/jurisign-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jurisign-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/jurisign/rate-limits/jurisign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jurisign-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jurisign/plans/jurisign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jurisign-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/jurisign/sandbox/jurisign-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jurisign-sandbox.yml
- group: design
  href: https://artifacts.apis.io/jurisign/asyncapi/jurisign-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jurisign-webhooks.yml
- group: design
  href: https://artifacts.apis.io/jurisign/lifecycle/jurisign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jurisign-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jurisign/conformance/jurisign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jurisign-conformance.yml
- group: auth
  href: https://artifacts.apis.io/jurisign/conformance/jurisign-conformance.yml
  title: ''
  type: Compliance
  url: conformance/jurisign-conformance.yml
- group: design
  href: https://artifacts.apis.io/jurisign/data-model/jurisign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jurisign-data-model.yml
- group: build
  href: https://artifacts.apis.io/jurisign/examples/jurisign-examples.yml
  title: ''
  type: Examples
  url: examples/jurisign-examples.yml
- group: other
  href: https://artifacts.apis.io/jurisign/overlays/jurisign-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jurisign-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/jurisign/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/jurisign/llms/jurisign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jurisign-llms.txt
- group: build
  href: https://artifacts.apis.io/jurisign/packages/jurisign-packages.yml
  title: ''
  type: Packages
  url: packages/jurisign-packages.yml
- group: agent
  href: https://artifacts.apis.io/jurisign/well-known/jurisign-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jurisign-well-known.yml
- group: auth
  href: https://artifacts.apis.io/jurisign/well-known/jurisign-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jurisign-security.txt
- group: auth
  href: https://artifacts.apis.io/jurisign/security/jurisign-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jurisign-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jurisign/security/jurisign-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jurisign-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jurisign/security/jurisign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jurisign-domain-security.yml
created: '2026-08-31'
description: eIDAS electronic signature API developed in France by PCFrance and hosted in Europe. JuriSign issues Simple Electronic Signatures (SES) under eIDAS Regulation (EU) No 910/2014 only -- not advanced (AdES) and not qualified (QES). The 46-operation REST contract covers PDF upload with multi-file merge, multi-signer signature requests with email or SMS OTP verification, pixel-placed signature zones, reusable templates, bulk campaigns, shareable public self-signing forms, pay-at-signature collection through Stripe Connect, HMAC-signed webhooks across twelve events, and download of both the signed PDF and its SHA-256 chained audit proof. Signature level is Simple Electronic Signature (SES) under eIDAS Regulation (EU) 910/2014; the provider states in its own GDPR Article 28 annex that it is not a qualified trust service provider and issues neither advanced nor qualified signatures. Bearer tokens carry one of five restrictable scopes, an Idempotency-Key makes the billable write safely
  repeatable, and a free sandbox needs no credit card. All data stays in the European Union.
finops:
- has_sources: true
  method: derived
  name: Jurisign Finops
  primary_unit: organisation
  service_category: ''
  slug: jurisign-finops
  template: false
image: https://www.jurisign.fr/images/icons/icon-192x192.png
layout: provider
modified: '2026-08-31'
name: JuriSign
nav: Providers
network: true
overview: 'JuriSign publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Bulk API, and 5 more. Tagged areas include E-Signature, eIDAS, PDF, Webhook, and OTP.


  The JuriSign catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  JuriSign''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 29 more developer resources.'
plans:
- name: Jurisign Plans Pricing
  plan_count: 14
  slug: jurisign-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Jurisign Rate Limits
  slug: jurisign-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: JuriSign API Rules
  rule_count: 63
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 10
  slug: jurisign-rules
scopes:
- name: Jurisign Scopes
  scope_count: 5
  slug: jurisign-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 69.4
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 68.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jurisign/jurisign-2026-09-02T150005.png
security:
- kind: authentication
  name: Jurisign Authentication
  slug: jurisign-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jurisign Domain Security
  slug: jurisign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jurisign Vulnerability Disclosure
  slug: jurisign-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: jurisign-bulk-and-public-forms
  slug: jurisign-bulk-and-public-forms
- name: jurisign-receive-signature-webhooks
  slug: jurisign-receive-signature-webhooks
- name: jurisign-send-document-for-signature
  slug: jurisign-send-document-for-signature
slug: jurisign
tags:
- E-Signature
- eIDAS
- PDF
- Webhook
- OTP
- GDPR
- France
- Legal Tech
- Identity Verification
- Audit Trail
- data-residency-eu
website: https://www.jurisign.fr/
---
