---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Kameleoon Agentic Access
  operation_count: 5
  slug: kameleoon-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 6
apis:
- description: Kameleoon Automation API (REST) for programmatically managing experiments, feature flags, and configuration. Limited to roughly a dozen calls per minute per account.
  name: Kameleoon Automation API
  slug: kameleoon-automation-api
- description: Kameleoon Data API (REST) for high-volume server-to-server data exchange — visitor data, custom data, and offline conversions. Designed for millions of calls per minute.
  name: Kameleoon Data API
  slug: kameleoon-data-api
- description: Kameleoon Product Recommendation API (REST) for managing product catalogs and serving AI-driven recommendations.
  name: Kameleoon Product Recommendation API
  slug: kameleoon-recommendation-api
- description: Manage Kameleoon experiments.
  name: Kameleoon Experiments API
  slug: kameleoon-experiments-api
- description: OAuth 2.0 authorization and token endpoints.
  name: Kameleoon OAuth API
  slug: kameleoon-oauth-api
- description: Manage Kameleoon personalizations.
  name: Kameleoon Personalizations API
  slug: kameleoon-personalizations-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kameleoon Automation Experiments API
  slug: open-kameleoon-experiments-api
- collection_type: open
  name: Kameleoon Automation Experiments OAuth API
  slug: open-kameleoon-oauth-api
- collection_type: open
  name: Kameleoon Automation Experiments Personalizations API
  slug: open-kameleoon-personalizations-api
- collection_type: open
  name: Kameleoon Automation API
  slug: open-kameleoon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kameleoon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kameleoon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kameleoon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kameleoon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kameleoon-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kameleoon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kameleoon
- group: company
  title: ''
  type: Website
  url: https://www.kameleoon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kameleoon.com/apis/automation-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/kameleoon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kameleoon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kameleoon-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.kameleoon.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.kameleoon.com/blog
created: '2026-05-08'
description: Kameleoon is an experimentation, personalization, feature flag, and AI-driven optimization platform for product and marketing teams.
finops:
- name: Kameleoon Finops
  service_category: A/B Testing
  slug: kameleoon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kameleoon.png
layout: provider
modified: '2026-05-08'
name: Kameleoon
nav: Providers
network: true
overview: 'Kameleoon publishes 3 APIs on the [APIs.io](https://apis.io/) network: Experiments API, OAuth API, and Personalizations API. Tagged areas include Experimentation, A/B Testing, Personalization, Feature Flags, and Artificial Intelligence.


  Kameleoon''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Kameleoon Plans Pricing
  plan_count: 1
  slug: kameleoon-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Kameleoon Rate Limits
  slug: kameleoon-rate-limits
scopes:
- name: Kameleoon Scopes
  scope_count: 0
  slug: kameleoon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 51.3
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kameleoon/refs/heads/main/screenshots/kameleoon-2026-06-20T183912.png
security:
- kind: authentication
  name: Kameleoon Authentication
  slug: kameleoon-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Kameleoon Domain Security
  slug: kameleoon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kameleoon Trust Center
  slug: kameleoon-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: kameleoon
tags:
- Experimentation
- A/B Testing
- Personalization
- Feature Flags
- Artificial Intelligence
website: https://www.kameleoon.com/
---
