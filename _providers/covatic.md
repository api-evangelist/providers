---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://covatic.com/contact/
  - https://covatic.com/page-sitemap.xml
  - https://platform.covatic.io/sign-in
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'REST API behind the Covatic client platform (platform.covatic.io) for building and operating privacy-preserving audiences and campaigns: audience profiles, traits (behavioural, event and retargeting),'
  name: Covatic Audience Builder API
  slug: covatic-audience-builder-api
artifact_total: 7
collections:
- collection_type: open
  name: Audience builder
  slug: open-covatic-audience-builder
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covatic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/covatic-llms.txt
- group: company
  title: ''
  type: Website
  url: https://covatic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://covatic.com/technical/
- group: docs
  title: ''
  type: APIReference
  url: https://prodaudiencebuilderapi.covatic.io/docs
- group: start
  title: ''
  type: Login
  url: https://platform.covatic.io/sign-in
- group: operate
  title: ''
  type: Support
  url: https://covatic.com/help-faq/
- group: company
  title: ''
  type: Blog
  url: https://covatic.com/insights/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://covatic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://covatic.com/terms-and-conditions/
- group: company
  title: ''
  type: About
  url: https://covatic.com/about/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/covatic/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Covatic
- group: auth
  title: ''
  type: Authentication
  url: authentication/covatic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/covatic-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/covatic-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/covatic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/covatic-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/covatic-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/covatic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/covatic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/covatic-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/covatic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/covatic-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/covatic-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/covatic-audience-builder-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://covatic.com/dpa/
created: '2026-07-17'
description: Covatic is a UK-based, B Corp certified advertising technology company providing privacy-preserving audience intelligence and addressability for media owners, broadcasters, publishers, and advertisers. Its platform uses on-device (edge) processing to build audience segments and demographic cohorts without third-party cookies, shared user IDs, or personal data leaving the device. Products include Covatic Sense for individual-level connected TV (CTV) addressability and attribution, a next-generation audience DMP for enrichment, clean-room data sharing, retargeting and attribution, plus audio, podcast, and smart-speaker targeting. Covatic integrates via the Covatic Tag (no-code tag manager), the Covatic SDK (on-device processing), and a server-to-server Covatic API, with a Google Ad Manager publishing path and client data stored in EU, AU, or US regions to meet local requirements.
image: https://covatic.com/wp-content/uploads/2025/07/covatic_favicon-1-300x300.png
layout: provider
modified: '2026-08-12'
name: Covatic
nav: Providers
network: true
overview: 'Covatic publishes 1 API on the [APIs.io](https://apis.io/) network: Audience Builder API. Tagged areas include Company, Advertising Technology, AdTech, Audience Intelligence, and Data Management Platform.


  Covatic''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Covatic Plans Pricing
  plan_count: 0
  slug: covatic-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Covatic Rate Limits
  slug: covatic-rate-limits
scopes:
- name: Covatic Scopes
  scope_count: 0
  slug: covatic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 58.7
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 40.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covatic/refs/heads/main/screenshots/covatic-2026-07-25T210538.png
security:
- kind: authentication
  name: Covatic Authentication
  slug: covatic-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Covatic Domain Security
  slug: covatic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: covatic
tags:
- Company
- Advertising Technology
- AdTech
- Audience Intelligence
- Data Management Platform
- Connected TV
- Privacy
- On-Device Processing
- Attribution
- Audio
- Campaigns
- Retargeting
- Publishing
- Broadcasting
- Media
- B Corp
- United Kingdom
website: https://covatic.com/
---
