---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Fulcrum Agentic Access
  operation_count: 55
  slug: fulcrum-agentic-access
  summary_line: 55 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Audio media attached to records
  name: Fulcrum Audio API
  slug: fulcrum-audio-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Grouped record changes for sync and audit
  name: Fulcrum Changesets API
  slug: fulcrum-changesets-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Reusable choice lists referenced by form fields
  name: Fulcrum Choice Lists API
  slug: fulcrum-choice-lists-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Hierarchical classifications referenced by form fields
  name: Fulcrum Classification Sets API
  slug: fulcrum-classification-sets-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: App and form definitions
  name: Fulcrum Forms API
  slug: fulcrum-forms-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Layers and tile sources used by forms
  name: Fulcrum Layers API
  slug: fulcrum-layers-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Account memberships and assignments
  name: Fulcrum Memberships API
  slug: fulcrum-memberships-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Photo media attached to records
  name: Fulcrum Photos API
  slug: fulcrum-photos-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Project containers used to scope records
  name: Fulcrum Projects API
  slug: fulcrum-projects-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Ad hoc query and SQL execution against Fulcrum data
  name: Fulcrum Query API
  slug: fulcrum-query-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Records collected against a form
  name: Fulcrum Records API
  slug: fulcrum-records-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Permission roles for memberships
  name: Fulcrum Roles API
  slug: fulcrum-roles-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Signature media attached to records
  name: Fulcrum Signatures API
  slug: fulcrum-signatures-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Video media attached to records
  name: Fulcrum Videos API
  slug: fulcrum-videos-api
- baseURL: https://api.fulcrumapp.com/api/v2
  baseurl_source: declared
  description: Outbound webhooks for record and form events
  name: Fulcrum Webhooks API
  slug: fulcrum-webhooks-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fulcrum API
  slug: open-fulcrum-api
- collection_type: open
  name: Fulcrum Audio API
  slug: open-fulcrum-audio-api
- collection_type: open
  name: Fulcrum Audio Changesets API
  slug: open-fulcrum-changesets-api
- collection_type: open
  name: Fulcrum Audio Choice Lists API
  slug: open-fulcrum-choice-lists-api
- collection_type: open
  name: Fulcrum Audio Classification Sets API
  slug: open-fulcrum-classification-sets-api
- collection_type: open
  name: Fulcrum Audio Forms API
  slug: open-fulcrum-forms-api
- collection_type: open
  name: Fulcrum Audio Layers API
  slug: open-fulcrum-layers-api
- collection_type: open
  name: Fulcrum Audio Memberships API
  slug: open-fulcrum-memberships-api
- collection_type: open
  name: Fulcrum Audio Photos API
  slug: open-fulcrum-photos-api
- collection_type: open
  name: Fulcrum Audio Projects API
  slug: open-fulcrum-projects-api
- collection_type: open
  name: Fulcrum Audio Query API
  slug: open-fulcrum-query-api
- collection_type: open
  name: Fulcrum Audio Records API
  slug: open-fulcrum-records-api
- collection_type: open
  name: Fulcrum Audio Roles API
  slug: open-fulcrum-roles-api
- collection_type: open
  name: Fulcrum Audio Signatures API
  slug: open-fulcrum-signatures-api
- collection_type: open
  name: Fulcrum Audio Videos API
  slug: open-fulcrum-videos-api
- collection_type: open
  name: Fulcrum Audio Webhooks API
  slug: open-fulcrum-webhooks-api
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
random_paper: 10
rate_limits:
- limit_count: 5
  name: Fulcrum Rate Limits
  slug: fulcrum-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 54.0
    developer_ergonomics: 29.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
