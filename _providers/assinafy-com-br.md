---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 67
  human_in_the_loop: 5
  name: Assinafy Com Br Agentic Access
  operation_count: 118
  slug: assinafy-com-br-agentic-access
  summary_line: 118 operations · 67 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: 'Workspace accounts: profile, logo and theme.'
  name: Assinafy Accounts API
  slug: assinafy-com-br-accounts-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: Request signatures on a document and estimate their cost.
  name: Assinafy Assignments API
  slug: assinafy-com-br-assignments-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: 'Authentication can be done in three ways: - API key in the `X-Api-Key` header: `X-Api-Key: {api-key}` - Access token in the `Authorization` header: `Authorization: Bearer {access-token}` - Access toke'
  name: Assinafy Authentication API
  slug: assinafy-com-br-authentication-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: 'Contract terms tracked on documents: counterparty, value, dates and renewal terms. A contract always belongs to a document of the workspace, and tracking it never changes how that document is uploaded'
  name: Assinafy Contracts API
  slug: assinafy-com-br-contracts-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: Create, list, download, tag and delete documents.
  name: Assinafy Documents API
  slug: assinafy-com-br-documents-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: Reusable field definitions used on templates and assignments.
  name: Assinafy Fields API
  slug: assinafy-com-br-fields-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: The token, revocation and userinfo endpoints an OAuth application calls, and this API's protected-resource metadata. New to OAuth with Assinafy? Read **OAuth Integration Guide** first. The authorizati
  name: Assinafy OAuth API
  slug: assinafy-com-br-oauth-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: Manage the signing parties of a workspace.
  name: Assinafy Signers API
  slug: assinafy-com-br-signers-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: 'Signer-facing endpoints: view, sign and decline documents using a signer access code.'
  name: Assinafy Signing API
  slug: assinafy-com-br-signing-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: Workspace-scoped labels attachable to documents and templates.
  name: Assinafy Tags API
  slug: assinafy-com-br-tags-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: Reusable document templates, their roles, fields and tags.
  name: Assinafy Templates API
  slug: assinafy-com-br-templates-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: User account endpoints.
  name: Assinafy Users API
  slug: assinafy-com-br-users-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: 'This section documents the HTTP request your endpoint receives whenever a subscribed event is triggered, and the shape of the JSON body sent for each event type. ### Delivery contract When an event oc'
  name: Assinafy Webhook Payloads API
  slug: assinafy-com-br-webhook-payloads-api
- baseURL: https://api.assinafy.com.br
  baseurl_source: declared
  description: 'Outbound webhook endpoints and delivery history. An account can register **1 webhook endpoint**, or **up to 3** on paid plans. Each endpoint has its own URL, event list and signing setting, and every '
  name: Assinafy Webhooks API
  slug: assinafy-com-br-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Assinafy Com Br Webhooks
  slug: assinafy-com-br-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/assinafy-com-br/agentic-access/assinafy-com-br-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/assinafy-com-br-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/assinafy-com-br/rate-limits/assinafy-com-br-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/assinafy-com-br-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/assinafy-com-br/plans/assinafy-com-br-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assinafy-com-br-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/rules/assinafy-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/assinafy-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/json-ld/assinafy-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/assinafy-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/vocabulary/assinafy-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/assinafy-com-br-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/assinafy-com-br/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/asyncapi/assinafy-com-br-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/assinafy-com-br-webhooks.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/data-model/assinafy-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/assinafy-com-br-data-model.yml
- group: build
  href: https://artifacts.apis.io/assinafy-com-br/cli/assinafy-com-br-cli.yml
  title: ''
  type: CLI
  url: cli/assinafy-com-br-cli.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/conventions/assinafy-com-br-conventions.yml
  title: ''
  type: Conventions
  url: conventions/assinafy-com-br-conventions.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/errors/assinafy-com-br-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/assinafy-com-br-problem-types.yml
- group: design
  href: https://artifacts.apis.io/assinafy-com-br/conformance/assinafy-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/assinafy-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/assinafy-com-br/llms/assinafy-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assinafy-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/assinafy-com-br/well-known/assinafy-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assinafy-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/assinafy-com-br/hosts/assinafy-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assinafy-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/assinafy-com-br/vendors/assinafy-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assinafy-com-br-vendors.yml
- group: build
  href: https://artifacts.apis.io/assinafy-com-br/packages/assinafy-com-br-packages.yml
  title: ''
  type: SDKs
  url: packages/assinafy-com-br-packages.yml
- group: build
  href: https://artifacts.apis.io/assinafy-com-br/packages/assinafy-com-br-packages.yml
  title: ''
  type: Packages
  url: packages/assinafy-com-br-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assinafy
- group: auth
  href: https://artifacts.apis.io/assinafy-com-br/scopes/assinafy-com-br-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/assinafy-com-br-scopes.yml
- group: auth
  href: https://artifacts.apis.io/assinafy-com-br/authentication/assinafy-com-br-authentication.yml
  title: ''
  type: Authentication
  url: authentication/assinafy-com-br-authentication.yml
- group: auth
  href: https://artifacts.apis.io/assinafy-com-br/security/assinafy-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assinafy-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assinafy.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.assinafy.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://www.assinafy.com.br/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.assinafy.com.br/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.assinafy.com.br/cadastro
- group: operate
  title: ''
  type: Support
  url: https://www.assinafy.com.br/contato
- group: company
  title: ''
  type: Blog
  url: https://www.assinafy.com.br/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.assinafy.com.br/planos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.assinafy.com.br/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.assinafy.com.br/politica-de-privacidade
- group: start
  title: ''
  type: SignUp
  url: https://www.assinafy.com.br/cadastro
created: '2026-11-01'
description: Assinafy provides a free electronic signature platform for Brazilian users, allowing online signing of documents with legal validity under ICP‑Brasil standards. The service offers a public, fully documented API for developers to integrate signature workflows into their applications, supports unlimited users per document, customizable branding, and a range of plans for businesses such as software houses, law firms, accountants, SaaS platforms, marketplaces, fintechs, and more.
image: https://www.assinafy.com.br/images/favicon-assetfy/favicon-32x32.png
json_schemas:
- name: DocumentContractAmendment
  property_count: 15
  slug: assinafy-com-br-document-contract-amendment
- name: DocumentContractInput
  property_count: 16
  slug: assinafy-com-br-document-contract-input
- name: DocumentContract
  property_count: 20
  slug: assinafy-com-br-document-contract
- name: Document
  property_count: 19
  slug: assinafy-com-br-document
- name: SignerIdentityReview
  property_count: 17
  slug: assinafy-com-br-signer-identity-review
- name: WebhookDispatch
  property_count: 17
  slug: assinafy-com-br-webhook-dispatch
jsonld:
- class_count: 47
  name: Assinafy Com Br Context
  property_count: 211
  slug: assinafy-com-br-context
layout: provider
modified: '2026-11-02'
name: Assinafy
nav: Providers
network: true
overview: 'Assinafy publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Assignments API, Authentication API, and 11 more. Tagged areas include E-Signature, Document Management, Brazil, and Free.


  The Assinafy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Assinafy''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Assinafy Com Br Plans Pricing
  plan_count: 4
  slug: assinafy-com-br-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Assinafy Com Br Rate Limits
  slug: assinafy-com-br-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Assinafy API Rules
  rule_count: 65
  severity_counts:
    error: 49
    hint: 0
    info: 4
    warn: 12
  slug: assinafy-com-br-rules
scopes:
- name: Assinafy Com Br Scopes
  scope_count: 10
  slug: assinafy-com-br-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 70.5
    developer_ergonomics: 55.2
    discoverability: 57.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assinafy Com Br Authentication
  slug: assinafy-com-br-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Assinafy Com Br Domain Security
  slug: assinafy-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: accounts
  slug: assinafy-com-br-accounts
slug: assinafy-com-br
tags:
- E-Signature
- Document Management
- Brazil
- Free
website: https://assinafy.com.br/
---
