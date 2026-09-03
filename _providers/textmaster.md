---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: true
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Abilities API from TextMaster — 1 operation(s) for abilities.
  name: TextMaster Abilities API
  slug: textmaster-abilities-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The API Templates API from TextMaster — 2 operation(s) for api templates.
  name: TextMaster API Templates API
  slug: textmaster-api-templates-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Authors API from TextMaster — 1 operation(s) for authors.
  name: TextMaster Authors API
  slug: textmaster-authors-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Categories API from TextMaster — 1 operation(s) for categories.
  name: TextMaster Categories API
  slug: textmaster-categories-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Countries API from TextMaster — 1 operation(s) for countries.
  name: TextMaster Countries API
  slug: textmaster-countries-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Documents API from TextMaster — 7 operation(s) for documents.
  name: TextMaster Documents API
  slug: textmaster-documents-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Expertises API from TextMaster — 3 operation(s) for expertises.
  name: TextMaster Expertises API
  slug: textmaster-expertises-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Glossaries API from TextMaster — 1 operation(s) for glossaries.
  name: TextMaster Glossaries API
  slug: textmaster-glossaries-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Invoices API from TextMaster — 1 operation(s) for invoices.
  name: TextMaster Invoices API
  slug: textmaster-invoices-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Languages API from TextMaster — 1 operation(s) for languages.
  name: TextMaster Languages API
  slug: textmaster-languages-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Locales API from TextMaster — 1 operation(s) for locales.
  name: TextMaster Locales API
  slug: textmaster-locales-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The My Authors API from TextMaster — 3 operation(s) for my authors.
  name: TextMaster My Authors API
  slug: textmaster-my-authors-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Negotiated Contracts API from TextMaster — 1 operation(s) for negotiated contracts.
  name: TextMaster Negotiated Contracts API
  slug: textmaster-negotiated-contracts-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Projects API from TextMaster — 14 operation(s) for projects.
  name: TextMaster Projects API
  slug: textmaster-projects-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Receipts API from TextMaster — 1 operation(s) for receipts.
  name: TextMaster Receipts API
  slug: textmaster-receipts-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Support Messages API from TextMaster — 1 operation(s) for support messages.
  name: TextMaster Support Messages API
  slug: textmaster-support-messages-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Transactions API from TextMaster — 1 operation(s) for transactions.
  name: TextMaster Transactions API
  slug: textmaster-transactions-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The UploadProperties API from TextMaster — 1 operation(s) for uploadproperties.
  name: TextMaster Upload Properties API
  slug: textmaster-uploadproperties-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Users API from TextMaster — 2 operation(s) for users.
  name: TextMaster Users API
  slug: textmaster-users-api
- baseURL: https://api.textmaster.com
  baseurl_source: declared
  description: The Work Templates API from TextMaster — 2 operation(s) for work templates.
  name: TextMaster Work Templates API
  slug: textmaster-work-templates-api
artifact_total: 27
asyncapis:
- description: ''
  name: Textmaster Event Surface
  slug: textmaster-event-surface
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/textmaster-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/textmaster-api-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.textmaster.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.textmaster.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.textmaster.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.textmaster.com/reference/abilities
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.textmaster.com/quick-start
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.textmaster.com/client
- group: operate
  title: ''
  type: Support
  url: mailto:support@textmaster.com
- group: start
  title: ''
  type: SignUp
  url: https://app.textmaster.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.textmaster.com/sign_in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/textmaster
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acolad.com/en/legal-notices/website-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textmaster.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/textmaster-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/textmaster/bugbounty/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/textmaster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textmaster-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.textmaster.com/client/policies/subprocessors
- group: design
  title: ''
  type: Conformance
  url: conformance/textmaster-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/textmaster-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/textmaster-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/textmaster-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: https://developer.textmaster.com/robots.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/textmaster-plans-pricing.yml
created: '2026-08-17'
description: TextMaster is a French professional translation, proofreading and copywriting platform that sells human-and-machine language work as an API-first service in 50+ languages. Clients create Projects, attach Documents (plain text or file URLs), request a quotation, launch against a prepaid credit wallet, and receive finished content back through status-change webhooks. The platform exposes a documented OpenAPI 3.0.3 REST API at api.textmaster.com covering projects, documents, glossaries, expertises, preferred authors, work/API templates, transactions, invoices and receipts, secured by OAuth 2.0 authorization-code apps with 22 granular scopes plus a legacy signature strategy. It ships first-party Akeneo, Magento 2, Salesforce Commerce Cloud and Hybris connectors and a PHP API client. TextMaster is now part of Acolad Group; the marketing site is a transition landing page pointing at Acolad's Lia platform, while the application, the API and the developer portal remain live and in service.
image: https://www.textmaster.com/assets/textmaster-logo.svg
layout: provider
modified: '2026-08-17'
name: TextMaster
nav: Providers
network: true
overview: 'TextMaster publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Abilities API, API Templates API, Authors API, and 17 more. Tagged areas include Company, Translation, Localization, Language Services, and Copywriting.


  The TextMaster catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TextMaster''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, and 21 more developer resources.'
plans:
- name: Textmaster Plans Pricing
  plan_count: 0
  slug: textmaster-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Textmaster Rate Limits
  slug: textmaster-rate-limits
scopes:
- name: Textmaster Scopes
  scope_count: 22
  slug: textmaster-scopes
  summary_line: 22 scopes · authorizationCode
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 46.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/textmaster/refs/heads/main/screenshots/textmaster-2026-09-02T163300.png
security:
- kind: authentication
  name: Textmaster Authentication
  slug: textmaster-authentication
  summary_line: oauth2/custom-signature · 2 schemes
- kind: domain-security
  name: Textmaster Domain Security
  slug: textmaster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Textmaster Vulnerability Disclosure
  slug: textmaster-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: textmaster
tags:
- Company
- Translation
- Localization
- Language Services
- Copywriting
- Proofreading
- Machine Translation
- Content Production
- Translation Memory
- Glossary
- Ecommerce Localization
- Product Information Management
- Webhook
- Authentication
- Software-as-a-Service
website: https://www.textmaster.com/
---
