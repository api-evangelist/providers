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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Documenso Agentic Access
  operation_count: 18
  slug: documenso-agentic-access
  summary_line: 18 operations · 13 acting
api_count: 1
apis:
- description: 'Outbound webhook events covering the full document lifecycle - created, sent, opened, signed, completed, rejected, cancelled - plus template events. Payloads are verified with a shared secret sent in '
  name: Documenso Webhooks
  slug: webhooks
- baseURL: https://app.documenso.com/api/v1
  baseurl_source: declared
  description: Create, upload, send, retrieve, download, and delete documents.
  name: Documenso Documents API
  slug: documenso-documents-api
- baseURL: https://app.documenso.com/api/v1
  baseurl_source: declared
  description: Add and configure signature and form fields on a document.
  name: Documenso Fields API
  slug: documenso-fields-api
- baseURL: https://app.documenso.com/api/v1
  baseurl_source: declared
  description: Manage the recipients (signers, approvers, viewers) of a document.
  name: Documenso Recipients API
  slug: documenso-recipients-api
- baseURL: https://app.documenso.com/api/v1
  baseurl_source: declared
  description: Manage reusable templates and generate documents from them.
  name: Documenso Templates API
  slug: documenso-templates-api
artifact_total: 18
collections:
- collection_type: open
  name: Documenso Public Documents API
  slug: open-documenso-documents-api
- collection_type: open
  name: Documenso Public Documents Fields API
  slug: open-documenso-fields-api
- collection_type: open
  name: Documenso Public Documents Recipients API
  slug: open-documenso-recipients-api
- collection_type: open
  name: Documenso Public Documents Templates API
  slug: open-documenso-templates-api
- collection_type: open
  name: Documenso Public API
  slug: open-documenso
common:
- group: agent
  href: https://artifacts.apis.io/documenso/agentic-access/documenso-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/documenso-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/documenso/security/documenso-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/documenso-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/documenso/security/documenso-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/documenso-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/documenso/authentication/documenso-authentication.yml
  title: ''
  type: Authentication
  url: authentication/documenso-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/documenso
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/documenso
- group: company
  title: ''
  type: Website
  url: https://documenso.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.documenso.com
- group: commercial
  href: https://artifacts.apis.io/documenso/plans/documenso-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/documenso-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/documenso/rate-limits/documenso-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/documenso-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/documenso/finops/documenso-finops.yml
  title: ''
  type: FinOps
  url: finops/documenso-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://documenso.com/blog
created: '2026-06-20'
description: Documenso is the open-source DocuSign alternative, a developer-friendly e-signature platform for sending, signing, and managing documents. Its public REST API lets you create and upload documents, add recipients and signature fields, send documents for signing, work with reusable templates, and receive webhook events across the document lifecycle. Self-hostable under AGPL.
finops:
- has_sources: true
  method: generated
  name: Documenso Finops
  primary_unit: ''
  service_category: Productivity and Business Applications
  slug: documenso-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/documenso.png
layout: provider
modified: '2026-06-20'
name: Documenso
nav: Providers
network: true
overview: 'Documenso publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documents API, Fields API, Recipients API, and 2 more. Tagged areas include E-Signature, Documents, Signing, Open Source, and DocuSign Alternative.


  The Documenso catalog on APIs.io includes 1 Spectral governance ruleset.


  Documenso''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Documenso Plans Pricing
  plan_count: 6
  slug: documenso-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Documenso Rate Limits
  slug: documenso-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Documenso API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: documenso-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.0
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/documenso/documenso-2026-06-20T180120.png
security:
- kind: authentication
  name: Documenso Authentication
  slug: documenso-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Documenso Domain Security
  slug: documenso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Documenso Vulnerability Disclosure
  slug: documenso-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: documenso
tags:
- E-Signature
- Documents
- Signing
- Open Source
- DocuSign Alternative
website: https://documenso.com
---
