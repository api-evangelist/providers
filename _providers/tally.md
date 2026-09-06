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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Tally Agentic Access
  operation_count: 26
  slug: tally-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 1
apis:
- description: REST API for managing forms and fetching/deleting submissions. Bearer token auth using API keys created from the workspace dashboard. Free on every Tally plan including the Free tier.
  name: Tally REST API
  slug: rest
- description: JavaScript embed library exposing Tally.openPopup, Tally.closePopup, Tally.loadEmbeds and event listeners for form load, page view, submission and popup close.
  name: Tally Embed JS
  slug: embed
- baseURL: https://api.tally.so
  baseurl_source: declared
  description: The Forms API from Tally — 3 operation(s) for forms.
  name: Tally Forms API
  slug: tally-forms-api
- baseURL: https://api.tally.so
  baseurl_source: declared
  description: The Organization API from Tally — 4 operation(s) for organization.
  name: Tally Organization API
  slug: tally-organization-api
- baseURL: https://api.tally.so
  baseurl_source: declared
  description: The Submissions API from Tally — 2 operation(s) for submissions.
  name: Tally Submissions API
  slug: tally-submissions-api
- baseURL: https://api.tally.so
  baseurl_source: declared
  description: The Users API from Tally — 1 operation(s) for users.
  name: Tally Users API
  slug: tally-users-api
- baseURL: https://api.tally.so
  baseurl_source: declared
  description: The Webhooks API from Tally — 4 operation(s) for webhooks.
  name: Tally Webhooks API
  slug: tally-webhooks-api
- baseURL: https://api.tally.so
  baseurl_source: declared
  description: The Workspaces API from Tally — 2 operation(s) for workspaces.
  name: Tally Workspaces API
  slug: tally-workspaces-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tally REST Forms API
  slug: open-tally-forms-api
- collection_type: open
  name: Tally REST Forms Organization API
  slug: open-tally-organization-api
- collection_type: open
  name: Tally REST Forms Submissions API
  slug: open-tally-submissions-api
- collection_type: open
  name: Tally REST Forms Users API
  slug: open-tally-users-api
- collection_type: open
  name: Tally REST Forms Webhooks API
  slug: open-tally-webhooks-api
- collection_type: open
  name: Tally REST Forms Workspaces API
  slug: open-tally-workspaces-api
- collection_type: open
  name: Tally REST API
  slug: open-tally
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tally-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tally-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tally-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withtally
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meettally
- group: company
  title: ''
  type: Website
  url: https://tally.so/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tally.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://tally.so/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://tally.so/help
- group: commercial
  title: ''
  type: Plans
  url: plans/tally-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tally-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tally-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://tally.so/llms.txt
created: '2026-05-08'
description: Tally is a Notion-style form and survey builder offering unlimited forms and submissions on its free plan. The Tally API exposes forms, submissions and webhooks programmatically and is free to use across all plans (including Free). Tally also publishes a JS embed library and an MCP server for AI integration.
finops:
- name: Tally Finops
  service_category: Forms / Surveys
  slug: tally-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tally.png
layout: provider
modified: '2026-05-08'
name: Tally
nav: Providers
network: true
overview: 'Tally publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Forms API, Organization API, Submissions API, and 3 more. Tagged areas include Forms, Surveys, No-Code, Free, and Notion-style.


  Tally''s developer surface includes authentication, documentation, pricing, and 10 more developer resources.'
plans:
- name: Tally Plans Pricing
  plan_count: 3
  slug: tally-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Tally Rate Limits
  slug: tally-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tally/refs/heads/main/screenshots/tally-2026-06-20T194908.png
security:
- kind: authentication
  name: Tally Authentication
  slug: tally-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tally Domain Security
  slug: tally-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tally
tags:
- Forms
- Surveys
- No-Code
- Free
- Notion-style
- Webhook
- MCP
website: https://tally.so/
---
