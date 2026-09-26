---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.2
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://api.zenlytic.com
  baseurl_source: declared
  description: Generate signed URLs for embedding Zenlytic content in host apps.
  name: Zenlytic Embedding API
  slug: zenlytic-embedding-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zenlytic Signed Embedding API
  slug: open-zenlytic-embedding-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.zenlytic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenlytic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenlytic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenlytic.com/embedding/signed_embedding
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenlytic.com/getting-started/start_here
- group: operate
  title: ''
  type: Support
  url: https://support.zenlytic.com/
- group: company
  title: ''
  type: Blog
  url: https://zenlytic.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zenlytic
- group: start
  title: ''
  type: SignUp
  url: https://app.zenlytic.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.zenlytic.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenlytic.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.zenlytic.com/legal-and-support/legal/terms-of-service-agreement
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/changelog/zenlytic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zenlytic-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/llms/zenlytic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zenlytic-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/packages/zenlytic-packages.yml
  title: ''
  type: Packages
  url: packages/zenlytic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/packages/zenlytic-packages.yml
  title: ''
  type: SDKs
  url: packages/zenlytic-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/authentication/zenlytic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zenlytic-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/security/zenlytic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenlytic-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/conventions/zenlytic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zenlytic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/components/zenlytic-components.yml
  title: ''
  type: Components
  url: components/zenlytic-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Zenlytic is an AI-powered business intelligence platform built around Zoë, an autonomous AI data analyst that turns natural-language questions into verified, governed insights and business-ready artifacts (dashboards, decks, models, and reports). It connects to cloud warehouses (Snowflake, BigQuery, Redshift, Databricks, Azure Synapse), builds a semantic context layer from schemas and query history, and answers with full lineage so every result is traceable to its source tables, filters, and metrics. Developers integrate Zenlytic through its open-source metrics-layer Python library, an iframe embedding surface with a signed-URL REST endpoint for external users, SSO (Microsoft Entra, Okta), and experimental MCP connectors that let Zoë call tools in the surrounding data stack. Zenlytic is backed by Bain Capital Ventures.
image: https://zenlytic.com/assets/images/social-card.png
layout: provider
modified: '2026-07-21'
name: Zenlytic
nav: Providers
network: true
overview: 'Zenlytic publishes 1 API on the [APIs.io](https://apis.io/) network: Embedding API. Tagged areas include Company, Commerce, Business Intelligence, Analytics, and Artificial Intelligence.


  Zenlytic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 14 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 43.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/zenlytic/refs/heads/main/screenshots/zenlytic-2026-08-17T083051.png
security:
- kind: authentication
  name: Zenlytic Authentication
  slug: zenlytic-authentication
  summary_line: http-basic/sso-saml-oidc/signed-jwt · 4 schemes
- kind: domain-security
  name: Zenlytic Domain Security
  slug: zenlytic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenlytic
tags:
- Company
- Commerce
- Business Intelligence
- Analytics
- Artificial Intelligence
- Data
- Embedded Analytics
- MCP
website: https://www.zenlytic.com/
---
