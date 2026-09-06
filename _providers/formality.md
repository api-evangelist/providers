---
access_model:
  confidence: medium
  label: Customer-only API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://help.formality.com/integrations/api
  - https://www.formality.com/en/index.html
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Formality REST API exposes the workspace contract repository so external tools and AI agents can retrieve documents and the AI-extracted metadata layer. Every path is namespaced to a workspace — /
  name: Formality API
  slug: formality-api
artifact_total: 8
asyncapis:
- description: ''
  name: Formality Webhooks
  slug: formality-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.formality.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.formality.com/en/privacy-policy.html
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.formality.com/en/cookie-policy.html
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.formality.com/en/legal-notice.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.formality.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.formality.com/en/index.html#security
- group: auth
  title: ''
  type: TrustCenter
  url: security/formality-trust-center.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.formality.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.formality.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.formality.com/integrations/api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.formality.com/start/first-steps
- group: operate
  title: ''
  type: Support
  url: https://help.formality.com/faq/feedback
- group: start
  title: ''
  type: Login
  url: https://auth.eu1.formality.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formality-group/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/formality-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/formality-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/formality-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.formality.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/formality-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formality-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/formality-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/formality-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/formality-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/formality-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/formality-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/formality-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/formality-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formality-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/formality-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formality-domain-security.yml
created: '2026-07-17'
description: 'Formality is a Paris-based AI platform for end-to-end asset and contract intelligence, aimed at businesses that need to centralize, understand, and track their legal, administrative, and asset-related documents. The product covers the full contract lifecycle: AI-assisted creation and collaborative negotiation, electronic signature, then post-signature data extraction, deadline and obligation alerts, and natural-language analysis of the resulting document estate. Its AI is trained on corporate legal documents, works across multiple languages, and runs inside a secure perimeter with full auditability and no use of customer data for model training. Formality integrates with tools including Google Drive, SharePoint, DocuWare, Docusign, Universign, Yousign, HubSpot, Salesforce, Outlook, Teams, Slack, and Gmail, and runs on compliant hosting with ISO 27001 and SOC 2 Type II certifications and GDPR compliance. It was founded in 2023 and is backed by Partech, Serena, and Bpifrance.'
image: https://framerusercontent.com/images/hEwKjnYt6aQ2PnIpW5a9LjGDmG4.svg
layout: provider
modified: '2026-08-17'
name: Formality
nav: Providers
network: true
overview: 'Formality publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Legal, Contract Management, and Document-Management.


  The Formality catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Formality''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 25 more developer resources.'
plans:
- name: Formality Plans Pricing
  plan_count: 0
  slug: formality-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Formality Rate Limits
  slug: formality-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 39.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formality/refs/heads/main/screenshots/formality-2026-07-25T214945.png
security:
- kind: authentication
  name: Formality Authentication
  slug: formality-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Formality Domain Security
  slug: formality-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Formality Vulnerability Disclosure
  slug: formality-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Formality Trust Center
  slug: formality-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: formality
tags:
- Company
- Ai Ml
- Legal
- Contract Management
- Document-Management
- Asset Intelligence
- Compliance
- Software-as-a-Service
website: https://www.formality.com/
---
