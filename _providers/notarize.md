---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 64
  human_in_the_loop: 1
  name: Notarize Agentic Access
  operation_count: 111
  slug: notarize-agentic-access
  summary_line: 111 operations · 64 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: REST API for creating and managing notarization, eSign, Identify, and real-estate transactions, documents, signers, notaries, templates, and Webhooks V2 subscriptions.
  name: Proof API (formerly Notarize)
  slug: proof-api-formerly-notarize
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Cost Centers API from Notarize — 2 operation(s) for cost centers.
  name: Notarize Cost Centers API
  slug: notarize-cost-centers-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Documents API from Notarize — 7 operation(s) for documents.
  name: Notarize Documents API
  slug: notarize-documents-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Eligibilities API from Notarize — 3 operation(s) for eligibilities.
  name: Notarize Eligibilities API
  slug: notarize-eligibilities-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The eNote API from Notarize — 1 operation(s) for enote.
  name: Notarize E Note API
  slug: notarize-enote-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Integrations API from Notarize — 1 operation(s) for integrations.
  name: Notarize Integrations API
  slug: notarize-integrations-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Notaries API from Notarize — 4 operation(s) for notaries.
  name: Notarize Notaries API
  slug: notarize-notaries-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Notarization Records API from Notarize — 3 operation(s) for notarization records.
  name: Notarize Notarization Records API
  slug: notarize-notarization-records-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The OAuth 2.0 API from Notarize — 7 operation(s) for oauth 2.0.
  name: Notarize OAuth 2.0 API
  slug: notarize-oauth-2-0-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The OID4VP API from Notarize — 4 operation(s) for oid4vp.
  name: Notarize OID4VP API
  slug: notarize-oid4vp-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Organizations API from Notarize — 5 operation(s) for organizations.
  name: Notarize Organizations API
  slug: notarize-organizations-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Referrals API from Notarize — 2 operation(s) for referrals.
  name: Notarize Referrals API
  slug: notarize-referrals-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The SCIM API from Notarize — 6 operation(s) for scim.
  name: Notarize SCIM API
  slug: notarize-scim-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Security Events API from Notarize — 1 operation(s) for security events.
  name: Notarize Security Events API
  slug: notarize-security-events-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Templates API from Notarize — 2 operation(s) for templates.
  name: Notarize Templates API
  slug: notarize-templates-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Title Agencies API from Notarize — 1 operation(s) for title agencies.
  name: Notarize Title Agencies API
  slug: notarize-title-agencies-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Transactions API from Notarize — 21 operation(s) for transactions.
  name: Notarize Transactions API
  slug: notarize-transactions-api
- baseURL: https://api.proof.com/v1
  baseurl_source: declared
  description: The Webhooks API from Notarize — 12 operation(s) for webhooks.
  name: Notarize Webhooks API
  slug: notarize-webhooks-api
artifact_total: 45
asyncapis:
- description: ''
  name: Notarize Webhooks
  slug: notarize-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/agentic-access/notarize-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/notarize-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/rules/notarize-rules.yml
  title: ''
  type: Spectral
  url: rules/notarize-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/json-ld/notarize-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/notarize-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/vocabulary/notarize-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/notarize-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/lifecycle/notarize-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/notarize-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/errors/notarize-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/notarize-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/hosts/notarize-hosts.yml
  title: ''
  type: Hosts
  url: hosts/notarize-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/vendors/notarize-vendors.yml
  title: ''
  type: Vendors
  url: vendors/notarize-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.proof.com/about/press
- group: company
  title: ''
  type: BlogRSS
  url: https://www.proof.com/blog/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/security/notarize-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/notarize-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/security/notarize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/notarize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.proof.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.proof.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.proof.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.proof.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.proof.com/docs/business-quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.proof.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.proof.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.proof.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proof.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@proof.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/notarize
- group: operate
  title: ''
  type: StatusPage
  url: https://status.proof.com
- group: auth
  title: ''
  type: Compliance
  url: https://security.proof.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/authentication/notarize-authentication.yml
  title: ''
  type: Authentication
  url: authentication/notarize-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/scopes/notarize-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/notarize-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/conventions/notarize-conventions.yml
  title: ''
  type: Conventions
  url: conventions/notarize-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/errors/notarize-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/notarize-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/lifecycle/notarize-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/notarize-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/sandbox/notarize-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/notarize-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/asyncapi/notarize-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/notarize-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/conformance/notarize-conformance.yml
  title: ''
  type: Conformance
  url: conformance/notarize-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/well-known/notarize-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/notarize-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/mcp/notarize-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/notarize-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/llms/notarize-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/notarize-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/data-model/notarize-data-model.yml
  title: ''
  type: DataModel
  url: data-model/notarize-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Notarize (rebranded as Proof) provides Remote Online Notarization (RON), eSignature, identity verification, and reusable digital credentials through the Notarize Network. Its REST API (api.proof.com) lets businesses create notarization, eSign, Identify, and real-estate/mortgage closing transactions, attach and template documents, invite signers, manage notaries, and receive V2 webhooks for every transaction and notary state change. Authentication is by API key or OAuth 2.0 client credentials, with a Fairfax test environment for end-to-end sandbox testing. Widely used across proptech, lending, title, and legal workflows.
image: https://github.com/notarize.png
json_schemas:
- name: authorization_server_metadata
  property_count: 20
  slug: notarize-authorization-server-metadata
- name: client_registration_request
  property_count: 12
  slug: notarize-client-registration-request
- name: client_registration_response
  property_count: 19
  slug: notarize-client-registration-response
- name: document_creation_params
  property_count: 19
  slug: notarize-document-creation-params
- name: document_params
  property_count: 9
  slug: notarize-document-params
- name: document
  property_count: 26
  slug: notarize-document
- name: document_update_params
  property_count: 8
  slug: notarize-document-update-params
- name: introspection_response
  property_count: 10
  slug: notarize-introspection-response
- name: revocation_request
  property_count: 6
  slug: notarize-revocation-request
- name: security_events_response
  property_count: 2
  slug: notarize-security-events-response
- name: token_info_response
  property_count: 11
  slug: notarize-token-info-response
- name: transaction_create_params
  property_count: 32
  slug: notarize-transaction-create-params
- name: transaction_object
  property_count: 43
  slug: notarize-transaction-object
- name: transaction_params
  property_count: 31
  slug: notarize-transaction-params
- name: user_creation_params
  property_count: 6
  slug: notarize-user-creation-params
- name: x401_handoff_response
  property_count: 2
  slug: notarize-x401-handoff-response
- name: x401_payload
  property_count: 2
  slug: notarize-x401-payload
- name: x401_result_response
  property_count: 2
  slug: notarize-x401-result-response
- name: x401_signature_response
  property_count: 2
  slug: notarize-x401-signature-response
jsonld:
- class_count: 81
  name: Notarize Context
  property_count: 319
  slug: notarize-context
layout: provider
modified: '2026-10-06'
name: Notarize
nav: Providers
network: true
overview: 'Notarize publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cost Centers API, Documents API, Eligibilities API, and 15 more. Tagged areas include Company, PropTech, Notarization, Remote Online Notarization, and Identity Verification.


  The Notarize catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Notarize''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 31 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Notarize API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 5
  slug: notarize-rules
scopes:
- name: Notarize Scopes
  scope_count: 2
  slug: notarize-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.9
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 70.6
    developer_ergonomics: 47.0
    discoverability: 80.4
    operational_transparency: 34.2
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: fedramp
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/notarize/refs/heads/main/screenshots/notarize-2026-08-07T185539.png
security:
- kind: authentication
  name: Notarize Authentication
  slug: notarize-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Notarize Domain Security
  slug: notarize-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Notarize Trust Center
  slug: notarize-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: notarize
tags:
- Company
- PropTech
- Notarization
- Remote Online Notarization
- Identity Verification
- E-Signature
- Digital Credentials
- Real Estate
- Mortgage
- Legal Tech
website: https://www.proof.com/
---
