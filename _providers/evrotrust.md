---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 100
  human_in_the_loop: 0
  name: Evrotrust Agentic Access
  operation_count: 104
  slug: evrotrust-agentic-access
  summary_line: 104 operations · 100 acting
api_count: 1
apis:
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The All Signing API from Evrotrust — 32 operation(s) for all signing.
  name: Evrotrust All Signing API
  slug: evrotrust-all-signing-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The e-Authentication API from Evrotrust — 1 operation(s) for e-authentication.
  name: Evrotrust E Authentication API
  slug: evrotrust-e-authentication-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The e-Delivery API from Evrotrust — 3 operation(s) for e-delivery.
  name: Evrotrust E Delivery API
  slug: evrotrust-e-delivery-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The e-Signatures API from Evrotrust — 6 operation(s) for e-signatures.
  name: Evrotrust E Signatures API
  slug: evrotrust-e-signatures-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The Evrotrust eID (Registered Users) API from Evrotrust — 4 operation(s) for evrotrust eid (registered users).
  name: Evrotrust Evrotrust eID (Registered Users) API
  slug: evrotrust-evrotrust-eid-registered-users-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The Ident Lite (Advanced, Basic) API from Evrotrust — 5 operation(s) for ident lite (advanced, basic).
  name: Evrotrust Ident Lite (Advanced, Basic) API
  slug: evrotrust-ident-lite-advanced-basic-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The One-time Signatures (Documents) API from Evrotrust — 20 operation(s) for one-time signatures (documents).
  name: Evrotrust One-time Signatures (Documents) API
  slug: evrotrust-one-time-signatures-documents-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The One-time Signatures (Hash) API from Evrotrust — 28 operation(s) for one-time signatures (hash).
  name: Evrotrust One-time Signatures (Hash) API
  slug: evrotrust-one-time-signatures-hash-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The Signing via App/SDK (Documents) API from Evrotrust — 3 operation(s) for signing via app/sdk (documents).
  name: Evrotrust Signing via App/SDK (Documents) API
  slug: evrotrust-signing-via-app-sdk-documents-api
- baseURL: https://v.evrotrust.com/vendor
  baseurl_source: declared
  description: The Signing via App/SDK (Hash) API from Evrotrust — 2 operation(s) for signing via app/sdk (hash).
  name: Evrotrust Signing via App/SDK (Hash) API
  slug: evrotrust-signing-via-app-sdk-hash-api
artifact_total: 30
common:
- group: other
  href: https://artifacts.apis.io/evrotrust/capabilities/evrotrust-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/evrotrust-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/evrotrust/agentic-access/evrotrust-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evrotrust-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/evrotrust/plans/evrotrust-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/evrotrust-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/rules/evrotrust-rules.yml
  title: ''
  type: Spectral
  url: rules/evrotrust-rules.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/json-ld/evrotrust-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/evrotrust-context.jsonld
- group: design
  href: https://artifacts.apis.io/evrotrust/vocabulary/evrotrust-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/evrotrust-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/evrotrust/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/data-model/evrotrust-data-model.yml
  title: ''
  type: DataModel
  url: data-model/evrotrust-data-model.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/components/evrotrust-components.yml
  title: ''
  type: Components
  url: components/evrotrust-components.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/conventions/evrotrust-conventions.yml
  title: ''
  type: Conventions
  url: conventions/evrotrust-conventions.yml
- group: start
  href: https://artifacts.apis.io/evrotrust/sandbox/evrotrust-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/evrotrust-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/evrotrust/authentication/evrotrust-authentication.yml
  title: ''
  type: Authentication
  url: authentication/evrotrust-authentication.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/lifecycle/evrotrust-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/evrotrust-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/errors/evrotrust-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/evrotrust-problem-types.yml
- group: design
  href: https://artifacts.apis.io/evrotrust/conformance/evrotrust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evrotrust-conformance.yml
- group: other
  href: https://artifacts.apis.io/evrotrust/overlays/evrotrust-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/evrotrust-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/evrotrust/llms/evrotrust-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evrotrust-llms.txt
- group: auth
  href: https://artifacts.apis.io/evrotrust/well-known/evrotrust-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/evrotrust-status-security.txt
- group: agent
  href: https://artifacts.apis.io/evrotrust/well-known/evrotrust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evrotrust-well-known.yml
- group: other
  href: https://artifacts.apis.io/evrotrust/hosts/evrotrust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evrotrust-hosts.yml
- group: other
  href: https://artifacts.apis.io/evrotrust/vendors/evrotrust-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evrotrust-vendors.yml
- group: build
  href: https://artifacts.apis.io/evrotrust/packages/evrotrust-packages.yml
  title: ''
  type: SDKs
  url: packages/evrotrust-packages.yml
- group: build
  href: https://artifacts.apis.io/evrotrust/packages/evrotrust-packages.yml
  title: ''
  type: Packages
  url: packages/evrotrust-packages.yml
- group: company
  title: ''
  type: Website
  url: https://evrotrust.com
- group: auth
  href: https://artifacts.apis.io/evrotrust/security/evrotrust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evrotrust-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.evrotrust.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evrotrust.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evrotrust.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evrotrust.com/docs/get-started
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evrotrust.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.evrotrust.com/
- group: operate
  title: ''
  type: Support
  url: https://evrotrust.com/support/
- group: company
  title: ''
  type: Blog
  url: https://evrotrust.com/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://evrotrust.com/release-notes/
- group: auth
  title: ''
  type: Compliance
  url: https://evrotrust.com/compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evrotrust
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evrotrust/
- group: start
  title: ''
  type: Login
  url: https://portal.evrotrust.com/
- group: operate
  title: ''
  type: ContactSales
  url: https://evrotrust.com/contact-sales/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evrotrust.com/website-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evrotrust.com/privacy-policy/
created: '2026-10-18'
description: Evrotrust is a European qualified trust service provider (QTSP) under eIDAS offering remote qualified electronic signatures (QES), an EU-notified electronic identification (eID) scheme for KYC/AML-compliant customer verification, electronic timestamps, electronic registered delivery and free validation of electronic signatures and seals. It serves financial services, public sector, telecom, insurance, healthcare, education and iGaming, and publishes developer documentation, an API reference and a Web SDK at docs.evrotrust.com.
image: https://files.readme.io/554d7570aaad6a49e760e45fd3cfccc325344adc4616c9fa0d3e36edfd34439b-evrotrust-logo.svg
json_schemas:
- name: DataDocumentGroupOfflineReady
  property_count: 3
  slug: evrotrust-data-document-group-offline-ready
- name: DataDocumentGroupReady
  property_count: 5
  slug: evrotrust-data-document-group-ready
- name: DataDocumentOfflineReady
  property_count: 3
  slug: evrotrust-data-document-offline-ready
- name: DataDocumentReady
  property_count: 4
  slug: evrotrust-data-document-ready
- name: DataHashOfflineCertificateReady
  property_count: 2
  slug: evrotrust-data-hash-offline-certificate-ready
jsonld:
- class_count: 5
  name: Evrotrust Context
  property_count: 5
  slug: evrotrust-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.evrotrust.com.
  name: Evrotrust documentation MCP endpoint
  slug: evrotrust-documentation-mcp-endpoint
modified: '2026-10-18'
name: Evrotrust
nav: Providers
network: true
overview: 'Evrotrust publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including All Signing API, E Authentication API, E Delivery API, and 7 more. Tagged areas include Company, Trust Services, Electronic Signatures, Digital Identity, and eIDAS.


  The Evrotrust catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Evrotrust''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 34 more developer resources.'
plans:
- name: Evrotrust Plans Pricing
  plan_count: 4
  slug: evrotrust-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Evrotrust Rate Limits
  slug: evrotrust-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Evrotrust API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: evrotrust-rules
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 55.9
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Evrotrust Authentication
  slug: evrotrust-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Evrotrust Domain Security
  slug: evrotrust-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 7
skills:
- name: evrotrust-deliver-document
  slug: evrotrust-deliver-document
- name: evrotrust-one-time-identification
  slug: evrotrust-one-time-identification
- name: evrotrust-one-time-sign-document
  slug: evrotrust-one-time-sign-document
- name: evrotrust-one-time-signatures-documents
  slug: evrotrust-one-time-signatures-documents
- name: evrotrust-registered-delivery
  slug: evrotrust-registered-delivery
- name: evrotrust-sign-document-in-app
  slug: evrotrust-sign-document-in-app
- name: evrotrust-sign-document-via-hash
  slug: evrotrust-sign-document-via-hash
slug: evrotrust
tags:
- Company
- Trust Services
- Electronic Signatures
- Digital Identity
- eIDAS
- KYC
- Identity Verification
- Timestamping
- Compliance
website: https://evrotrust.com
---
