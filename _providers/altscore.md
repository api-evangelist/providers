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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 31.7
  scored_at: '2026-09-21'
api_count: 3
apis:
- description: Alternative-data aggregation for credit underwriting and scoring. Aggregates over 50 data sources into on-demand data requests that feed borrower enrichment and decisioning.
  name: AltData API
  slug: altdata-api
- description: Onboarding, KYC/KYB, identities, documents, deals, forms, workflows (v1 + v2), credit decisioning, evaluators, and policy rules. The default module of the AltScore SDK and CLI.
  name: Borrower Central API
  slug: borrower-central-api
- description: The loan lifecycle system — partners, clients, credit accounts, debts, disbursements, disbursement accounts, payment accounts, payment orders, and DPAs (payment agreements). Includes the webhooks surf
  name: Credit Management System API
  slug: credit-management-system-api
artifact_total: 8
asyncapis:
- description: ''
  name: Altscore Webhooks
  slug: altscore-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/security/altscore-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/altscore-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://altscore.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.altscore.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.altscore.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.altscore.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.altscore.ai/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AltScore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altscore.ai/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altscore.ai/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.altscore.ai/en/#contacto
- group: auth
  title: ''
  type: Compliance
  url: https://www.altscore.ai/en/security
- group: build
  title: ''
  type: Postman
  url: https://docs.altscore.ai/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/packages/altscore-packages.yml
  title: ''
  type: Packages
  url: packages/altscore-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/packages/altscore-packages.yml
  title: ''
  type: SDKs
  url: packages/altscore-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/cli/altscore-cli.yml
  title: ''
  type: CLI
  url: cli/altscore-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/authentication/altscore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/altscore-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/scopes/altscore-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/altscore-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/well-known/altscore-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/altscore-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/well-known/altscore-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altscore-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/mcp/altscore-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/altscore-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/llms/altscore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altscore-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/conventions/altscore-conventions.yml
  title: ''
  type: Conventions
  url: conventions/altscore-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/conformance/altscore-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altscore-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/lifecycle/altscore-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/altscore-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/sandbox/altscore-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/altscore-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/data-model/altscore-data-model.yml
  title: ''
  type: DataModel
  url: data-model/altscore-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/asyncapi/altscore-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/altscore-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/security/altscore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altscore-domain-security.yml
created: '2026-07-17'
description: 'AltScore is a B2B credit infrastructure platform for Latin America — the "Rails of Lending" that lets any company build, embed, and deploy credit products in weeks instead of years. Its API surface spans three products: AltData, an aggregation layer over 50+ alternative and traditional data sources for underwriting and scoring; Borrower Central, an onboarding, KYC/KYB, identity, document, and workflow/decisioning engine; and a Credit Management System for the full loan lifecycle — disbursements, credit accounts, debts, payment orders, and DPAs. Access is through first-party Python and TypeScript SDKs, a Go CLI, and a Frontegg-backed OAuth/OIDC identity layer, with a dedicated sandbox environment and an in-production test mode (isTest) for UAT.'
image: https://altscore.ai/favicon.ico
layout: provider
modified: '2026-07-17'
name: AltScore
nav: Providers
network: true
overview: 'AltScore publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Credit, Lending, Fintech, and Credit Scoring.


  The AltScore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AltScore''s developer surface includes documentation, API reference, engineering blog, support, CLI, authentication, sandbox, and 22 more developer resources.'
random_paper: 3
scopes:
- name: Altscore Scopes
  scope_count: 3
  slug: altscore-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 78.6
    discoverability: 81.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 51.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/screenshots/altscore-2026-07-25T195844.png
security:
- kind: authentication
  name: Altscore Authentication
  slug: altscore-authentication
  summary_line: oauth2/apiKey/http · 5 schemes
- kind: domain-security
  name: Altscore Domain Security
  slug: altscore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Altscore Trust Center
  slug: altscore-trust-center
  summary_line: ISO 27001:2022, SOC 2
slug: altscore
tags:
- Company
- Credit
- Lending
- Fintech
- Credit Scoring
- Underwriting
- KYC
- Financial-Services
- Latin America
- Data Aggregation
- Workflows
- Decisioning
website: https://altscore.ai/
---
