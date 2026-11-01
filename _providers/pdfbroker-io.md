---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Pdfbroker Io Agentic Access
  operation_count: 16
  slug: pdfbroker-io-agentic-access
  summary_line: 16 operations · 14 acting
api_count: 1
apis:
- description: PdfBroker.io provides PDF generation services via a REST API.
  name: PdfBroker.io API
  slug: pdfbroker-io-api
- baseURL: https://api.pdfbroker.io
  baseurl_source: declared
  description: The Pdf API from pdfbroker-io — 16 operation(s) for pdf.
  name: pdfbroker-io PDF API
  slug: pdfbroker-io-pdf-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/pdfbroker-io/agentic-access/pdfbroker-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfbroker-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/pdfbroker-io/plans/pdfbroker-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pdfbroker-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pdfbroker-io/rules/pdfbroker-io-rules.yml
  title: ''
  type: Spectral
  url: rules/pdfbroker-io-rules.yml
- group: design
  href: https://artifacts.apis.io/pdfbroker-io/json-ld/pdfbroker-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pdfbroker-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/pdfbroker-io/vocabulary/pdfbroker-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pdfbroker-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pdfbroker-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pdfbroker-io/data-model/pdfbroker-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pdfbroker-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/pdfbroker-io/authentication/pdfbroker-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pdfbroker-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/pdfbroker-io/errors/pdfbroker-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pdfbroker-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pdfbroker-io/conformance/pdfbroker-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pdfbroker-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pdfbroker-io/llms/pdfbroker-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pdfbroker-io-llms.txt
- group: other
  href: https://artifacts.apis.io/pdfbroker-io/hosts/pdfbroker-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pdfbroker-io-hosts.yml
- group: auth
  href: https://artifacts.apis.io/pdfbroker-io/scopes/pdfbroker-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/pdfbroker-io-scopes.yml
- group: auth
  href: https://artifacts.apis.io/pdfbroker-io/security/pdfbroker-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pdfbroker-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pdfbroker.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pdfbroker.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pdfbroker.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.pdfbroker.io/docs/openapi-swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pdfbroker.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.pdfbroker.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.pdfbroker.io/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pdfbroker.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pdfbroker.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pdfbroker.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.pdfbroker.io/signup
- group: start
  title: ''
  type: Login
  url: https://www.pdfbroker.io/login
created: '2026-10-30'
description: PdfBroker.io provides a cloud-based PDF generation REST API that converts HTML, CSS, and XSL-FO into PDF/A and PDF/UA compliant documents. It supports OAuth2/OIDC authentication, EU-hosted data residency, and offers multiple service tiers including free, premium, and enterprise plans. The platform includes AI integration, .NET client libraries, and extensive documentation for developers.
image: https://www.pdfbroker.io/assets/images/og-default.png
jsonld:
- class_count: 18
  name: Pdfbroker Io Context
  property_count: 48
  slug: pdfbroker-io-context
layout: provider
modified: '2026-10-30'
name: pdfbroker-io
nav: Providers
network: true
overview: 'pdfbroker-io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including PDF API, and 1 more. Tagged areas include PDF Generation, REST API, HTML to PDF, PDF/A, and PDF/UA.


  The pdfbroker-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pdfbroker-io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Pdfbroker Io Plans Pricing
  plan_count: 4
  slug: pdfbroker-io-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: pdfbroker-io API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: pdfbroker-io-rules
scopes:
- name: Pdfbroker Io Scopes
  scope_count: 1
  slug: pdfbroker-io-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 79.5
    catalog_earned_first_party: 0.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 50.3
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 34.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pdfbroker Io Authentication
  slug: pdfbroker-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pdfbroker Io Domain Security
  slug: pdfbroker-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: getting-started
  slug: pdfbroker-io-getting-started
slug: pdfbroker-io
tags:
- PDF Generation
- REST API
- HTML to PDF
- PDF/A
- PDF/UA
- PDF Utilities
- XSL-FO
website: https://pdfbroker.io/
---
