---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Documented, versioned REST API (OpenAPI 3.0.3, 46 operations across 8 tags) for eIDAS SES electronic signatures: documents, sign requests, templates, bulk campaigns, public forms, account credits, web'
  name: JuriSign REST API
  slug: jurisign-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Jurisign Webhooks
  slug: jurisign-webhooks
common:
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
  title: ''
  type: Authentication
  url: authentication/jurisign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jurisign-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jurisign-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/jurisign-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jurisign-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jurisign-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jurisign-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jurisign-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jurisign-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jurisign-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jurisign-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/jurisign-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jurisign-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/jurisign-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jurisign-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jurisign-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/jurisign-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jurisign-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jurisign-security.txt
- group: auth
  title: ''
  type: Security
  url: security/jurisign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jurisign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jurisign-domain-security.yml
created: '2026-08-31'
description: eIDAS-compliant electronic signature API built, operated and hosted in France by PCFRANCE. The 46-operation REST contract covers PDF upload with multi-file merge, multi-signer signature requests with email or SMS OTP verification, pixel-placed signature zones, reusable templates, bulk campaigns, shareable public self-signing forms, pay-at-signature collection through Stripe Connect, HMAC-signed webhooks across twelve events, and download of both the signed PDF and its SHA-256 chained audit proof. Signature level is Simple Electronic Signature (SES) under eIDAS Regulation (EU) 910/2014; the provider states in its own GDPR Article 28 annex that it is not a qualified trust service provider and issues neither advanced nor qualified signatures. Bearer tokens carry one of five restrictable scopes, an Idempotency-Key makes the billable write safely repeatable, and a free sandbox needs no credit card. All data stays in the European Union.
image: https://www.jurisign.fr/images/icons/icon-192x192.png
layout: provider
modified: '2026-08-31'
name: JuriSign
nav: Providers
network: true
overview: 'JuriSign publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Electronic Signature, E-Signature, eIDAS, Document Signing, and PDF.


  The JuriSign catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  JuriSign''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Jurisign Plans Pricing
  plan_count: 8
  slug: jurisign-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Jurisign Rate Limits
  slug: jurisign-rate-limits
scopes:
- name: Jurisign Scopes
  scope_count: 0
  slug: jurisign-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 66.0
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 62.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
slug: jurisign
tags:
- Electronic Signature
- E-Signature
- eIDAS
- Document Signing
- PDF
- Webhook
- OTP
- GDPR
- France
- Legal Tech
- Identity Verification
- Audit Trail
- data-residency-eu
website: https://www.jurisign.fr/developpeurs
---
