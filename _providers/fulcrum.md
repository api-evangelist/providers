---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Fulcrum Agentic Access
  operation_count: 55
  slug: fulcrum-agentic-access
  summary_line: 55 operations · 29 acting
api_count: 15
apis:
- description: Audio media attached to records
  name: Fulcrum Audio API
  slug: fulcrum-audio-api
- description: Grouped record changes for sync and audit
  name: Fulcrum Changesets API
  slug: fulcrum-changesets-api
- description: Reusable choice lists referenced by form fields
  name: Fulcrum Choice Lists API
  slug: fulcrum-choice-lists-api
- description: Hierarchical classifications referenced by form fields
  name: Fulcrum Classification Sets API
  slug: fulcrum-classification-sets-api
- description: App and form definitions
  name: Fulcrum Forms API
  slug: fulcrum-forms-api
- description: Layers and tile sources used by forms
  name: Fulcrum Layers API
  slug: fulcrum-layers-api
- description: Account memberships and assignments
  name: Fulcrum Memberships API
  slug: fulcrum-memberships-api
- description: Photo media attached to records
  name: Fulcrum Photos API
  slug: fulcrum-photos-api
- description: Project containers used to scope records
  name: Fulcrum Projects API
  slug: fulcrum-projects-api
- description: Ad hoc query and SQL execution against Fulcrum data
  name: Fulcrum Query API
  slug: fulcrum-query-api
- description: Records collected against a form
  name: Fulcrum Records API
  slug: fulcrum-records-api
- description: Permission roles for memberships
  name: Fulcrum Roles API
  slug: fulcrum-roles-api
- description: Signature media attached to records
  name: Fulcrum Signatures API
  slug: fulcrum-signatures-api
- description: Video media attached to records
  name: Fulcrum Videos API
  slug: fulcrum-videos-api
- description: Outbound webhooks for record and form events
  name: Fulcrum Webhooks API
  slug: fulcrum-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: Fulcrum API
  slug: open-fulcrum-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fulcrum-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fulcrum-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fulcrum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fulcrum-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fulcrumapp
- group: company
  title: ''
  type: Website
  url: https://www.fulcrumapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fulcrumapp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fulcrumapp.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fulcrumapp.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://web.fulcrumapp.com/users/sign_in
- group: start
  title: ''
  type: Signup
  url: https://web.fulcrumapp.com/users/sign_up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fulcrumapp.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fulcrumapp.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.fulcrumapp.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.fulcrumapp.com/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.fulcrumapp.com/llms.txt
created: '2024-11-13'
description: Fulcrum is a field data collection and inspection platform used by teams to build mobile forms, capture geospatial records, attach photos, videos, audio, and signatures, and synchronize the resulting data with back-office systems. The Fulcrum REST API exposes programmatic access to forms, records, media, choice lists, classification sets, projects, layers, memberships, roles, webhooks, ad hoc SQL queries, and changesets.
finops:
- name: Fulcrum Finops
  service_category: API
  slug: fulcrum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fulcrum.png
layout: provider
modified: '2026-05-19'
name: Fulcrum
nav: Providers
network: true
overview: 'Fulcrum publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Changesets API, Choice Lists API, and 12 more. Tagged areas include Data Collection, Field Data, Geospatial, Process Management, and Mobile.


  Fulcrum''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, support, engineering blog, and 9 more developer resources.'
plans:
- name: Fulcrum Plans Pricing
  plan_count: 3
  slug: fulcrum-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Fulcrum Rate Limits
  slug: fulcrum-rate-limits
score:
  band: developing
  composite: 52.4
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 57.7
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fulcrum/refs/heads/main/screenshots/fulcrum-2026-06-20T181606.png
security:
- kind: authentication
  name: Fulcrum Authentication
  slug: fulcrum-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fulcrum Domain Security
  slug: fulcrum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fulcrum Trust Center
  slug: fulcrum-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: fulcrum
tags:
- Data Collection
- Field Data
- Geospatial
- Process Management
- Mobile
website: https://www.fulcrumapp.com/
---
