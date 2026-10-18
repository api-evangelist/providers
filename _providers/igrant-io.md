---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Config API from iGrant.io — 8 operation(s) for config.
  name: iGrant.io Config API
  slug: igrant-io-config-api
artifact_total: 12
asyncapis:
- description: ''
  name: Igrant Io Webhooks
  slug: igrant-io-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/rules/igrant-io-rules.yml
  title: ''
  type: Spectral
  url: rules/igrant-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/json-ld/igrant-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/igrant-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/vocabulary/igrant-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/igrant-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/asyncapi/igrant-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/igrant-io-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/data-model/igrant-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/igrant-io-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/changelog/igrant-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/igrant-io-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/conventions/igrant-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/igrant-io-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/sandbox/igrant-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/igrant-io-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/authentication/igrant-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/igrant-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/conformance/igrant-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/igrant-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/llms/igrant-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/igrant-io-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/hosts/igrant-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/igrant-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/vendors/igrant-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/igrant-io-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://igrant.io/sdk/usecase_sdk/demo-app.html
- group: company
  title: ''
  type: Newsroom
  url: https://igrant.io/news/2.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/L3-iGrant
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.igrant.io/docs/changelog/2026-q3/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/igrant-io/refs/heads/main/security/igrant-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/igrant-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://igrant.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.igrant.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.igrant.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.igrant.io/docs/developer-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.igrant.io/docs/get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.igrant.io/
- group: company
  title: ''
  type: Blog
  url: https://igrant.io/news.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://igrant.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://igrant.io/privacy.html
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://igrant.io/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: iGrant.io provides EU Digital Identity and Business Wallet software, offering a suite of data wallet, data verifier, data pod, and consent management solutions. Built to be eIDAS 2.0‑ready and ISO27001 certified, the platform enables secure, user‑centric authentication and cross‑border data exchange for regulated industries. It supplies APIs for issuers, holders, verifiers, webhooks, and key management, supporting developers with sandbox environments and comprehensive documentation.
image: https://igrant.io/assets/images/favicons/preview.png
json_schemas:
- name: GetV2ConfigWebhooksWebhookidDeliveriesResponse
  property_count: 15
  slug: igrant-io-get-v2-config-webhooks-webhookid-deliveries-response
- name: GetV2ConfigWebhooksWebhookidDeliveryDeliveryidResponse
  property_count: 7
  slug: igrant-io-get-v2-config-webhooks-webhookid-delivery-deliveryid-response
- name: PostV2ConfigWebhookRequest
  property_count: 9
  slug: igrant-io-post-v2-config-webhook-request
- name: PostV2ConfigWebhookResponse
  property_count: 10
  slug: igrant-io-post-v2-config-webhook-response
- name: PutV2ConfigWebhookWebhookidRequest
  property_count: 6
  slug: igrant-io-put-v2-config-webhook-webhookid-request
- name: PutV2ConfigWebhookWebhookidResponse
  property_count: 10
  slug: igrant-io-put-v2-config-webhook-webhookid-response
jsonld:
- class_count: 12
  name: Igrant Io Context
  property_count: 33
  slug: igrant-io-context
layout: provider
modified: '2026-10-15'
name: iGrant.io
nav: Providers
network: true
overview: 'iGrant.io is listed with 1 API on the [APIs.io](https://apis.io/) network: Config API. Tagged areas include Company, Identity, Wallets, and eIDAS.


  The iGrant.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  iGrant.io''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: iGrant.io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: igrant-io-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 35.7
    developer_ergonomics: 71.4
    discoverability: 57.1
    operational_transparency: 28.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Igrant Io Authentication
  slug: igrant-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Igrant Io Domain Security
  slug: igrant-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: igrant-io
tags:
- Company
- Identity
- Wallets
- eIDAS
website: https://igrant.io/
---
