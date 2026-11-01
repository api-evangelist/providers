---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 64
  human_in_the_loop: 1
  name: Notarize Com Agentic Access
  operation_count: 111
  slug: notarize-com-agentic-access
  summary_line: 111 operations · 64 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Cost Centers API from Notarize — 2 operation(s) for cost centers.
  name: Notarize Cost Centers API
  slug: notarize-com-cost-centers-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Documents API from Notarize — 7 operation(s) for documents.
  name: Notarize Documents API
  slug: notarize-com-documents-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Eligibilities API from Notarize — 3 operation(s) for eligibilities.
  name: Notarize Eligibilities API
  slug: notarize-com-eligibilities-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The eNote API from Notarize — 1 operation(s) for enote.
  name: Notarize E Note API
  slug: notarize-com-enote-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Integrations API from Notarize — 1 operation(s) for integrations.
  name: Notarize Integrations API
  slug: notarize-com-integrations-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Notaries API from Notarize — 4 operation(s) for notaries.
  name: Notarize Notaries API
  slug: notarize-com-notaries-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Notarization Records API from Notarize — 3 operation(s) for notarization records.
  name: Notarize Notarization Records API
  slug: notarize-com-notarization-records-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The OAuth 2.0 API from Notarize — 7 operation(s) for oauth 2.0.
  name: Notarize OAuth 2.0 API
  slug: notarize-com-oauth-2-0-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The OID4VP API from Notarize — 4 operation(s) for oid4vp.
  name: Notarize OID4VP API
  slug: notarize-com-oid4vp-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Organizations API from Notarize — 5 operation(s) for organizations.
  name: Notarize Organizations API
  slug: notarize-com-organizations-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Referrals API from Notarize — 2 operation(s) for referrals.
  name: Notarize Referrals API
  slug: notarize-com-referrals-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The SCIM API from Notarize — 6 operation(s) for scim.
  name: Notarize SCIM API
  slug: notarize-com-scim-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Security Events API from Notarize — 1 operation(s) for security events.
  name: Notarize Security Events API
  slug: notarize-com-security-events-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Templates API from Notarize — 2 operation(s) for templates.
  name: Notarize Templates API
  slug: notarize-com-templates-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Title Agencies API from Notarize — 1 operation(s) for title agencies.
  name: Notarize Title Agencies API
  slug: notarize-com-title-agencies-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Transactions API from Notarize — 21 operation(s) for transactions.
  name: Notarize Transactions API
  slug: notarize-com-transactions-api
- baseURL: https://api.proof.com
  baseurl_source: declared
  description: The Webhooks API from Notarize — 12 operation(s) for webhooks.
  name: Notarize Webhooks API
  slug: notarize-com-webhooks-api
artifact_total: 28
asyncapis:
- description: ''
  name: Notarize Com Webhooks
  slug: notarize-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/notarize-com/agentic-access/notarize-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/notarize-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/notarize-com/rules/notarize-com-rules.yml
  title: ''
  type: Spectral
  url: rules/notarize-com-rules.yml
- group: design
  href: https://artifacts.apis.io/notarize-com/json-ld/notarize-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/notarize-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/notarize-com/vocabulary/notarize-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/notarize-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/notarize-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/notarize-com/asyncapi/notarize-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/notarize-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/notarize-com/data-model/notarize-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/notarize-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/notarize-com/authentication/notarize-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/notarize-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/notarize-com/errors/notarize-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/notarize-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/notarize-com/conformance/notarize-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/notarize-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/notarize-com/llms/notarize-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/notarize-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/notarize-com/well-known/notarize-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/notarize-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/notarize-com/hosts/notarize-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/notarize-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/notarize-com/vendors/notarize-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/notarize-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.proof.com/docs/in-house-notary-ihn-testing-setup
- group: docs
  title: ''
  type: Documentation
  url: https://dev.notarize.com/
- group: auth
  href: https://artifacts.apis.io/notarize-com/security/notarize-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/notarize-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://notarize.com/
- group: company
  title: ''
  type: Blog
  url: https://www.notarize.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.notarize.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.notarize.com/hc/en-us
created: '2026-10-25'
description: Notarize provides an online notarization platform that enables individuals, businesses, and notaries to complete notarizations digitally. Users can upload documents, verify identity, and connect with a licensed notary 24/7, eliminating the need for in‑person visits. The service supports a wide range of use cases including real‑estate closings, power‑of‑attorney forms, and personal documents, and is trusted by millions across all 50 U.S. states. Notarize aims to simplify legal processes with secure, fast, and compliant electronic notarizations.
jsonld:
- class_count: 81
  name: Notarize Com Context
  property_count: 319
  slug: notarize-com-context
layout: provider
modified: '2026-10-25'
name: Notarize
nav: Providers
network: true
overview: 'Notarize publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cost Centers API, Documents API, Eligibilities API, and 14 more. Tagged areas include Company, Notarization, LegalTech, SaaS, and DigitalSignature.


  The Notarize catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Notarize''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, support, and 15 more developer resources.'
random_paper: 16
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
  slug: notarize-com-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 62.5
    developer_ergonomics: 42.3
    discoverability: 58.9
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Notarize Com Authentication
  slug: notarize-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Notarize Com Domain Security
  slug: notarize-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: notarize-com-add-and-get-document
  slug: notarize-com-add-and-get-document
- name: notarize-com-create-and-activate-transaction
  slug: notarize-com-create-and-activate-transaction
- name: notarize-com-create-and-update-partner-organization
  slug: notarize-com-create-and-update-partner-organization
- name: notarize-com-manage-webhook-url
  slug: notarize-com-manage-webhook-url
- name: notarize-com-notary-lifecycle
  slug: notarize-com-notary-lifecycle
slug: notarize-com
tags:
- Company
- Notarization
- LegalTech
- SaaS
- DigitalSignature
website: https://notarize.com/
---
