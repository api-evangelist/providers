---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/security/aiflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiflow.solutions/
- group: company
  title: ''
  type: Website
  url: https://www.veratainsight.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.veratainsight.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.veratainsight.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.veratainsight.com/resources/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veratainsight.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veratainsight.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/well-known/aiflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiflow-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/authentication/aiflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiflow-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/scopes/aiflow-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aiflow-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/conformance/aiflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiflow-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/plans/aiflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiflow-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/rate-limits/aiflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiflow-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiflow/refs/heads/main/llms/aiflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiflow-llms.txt
coverage:
  checked: '2026-09-14'
  detail: aiFlow ships only an end-user web application — the word "API" does not appear anywhere on the aiflow.solutions or veratainsight.com sites, and the company's own security page states the platform is "self-contained by design" with "no integration credentials to manage", so data leaves it by Excel and CSV export rather than through any interface.
  evidence:
  - status: 200
    url: https://www.veratainsight.com/
  - status: 200
    url: https://www.veratainsight.com/pricing
  - status: 200
    url: https://www.veratainsight.com/security
  - status: 404
    url: https://aiflow.solutions/llms.txt
  - status: 404
    url: https://aiflow.solutions/.well-known/api-catalog
  - status: 200
    url: https://auth.aiflow.solutions/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: aiFlow (AiFlow, Inc., Y Combinator W23) is a San Francisco company building AI-powered executive intelligence for private equity talent teams and executive search firms, founded in 2022 by Nick Manske and Josh Gardner. Its platform reads public sources — company sites, press, deal announcements and professional profiles — to generate data-driven evaluations of C-level and board candidates, revenue estimates with published comparable-company methodology, transaction and funding history, backchannel and reference discovery, and search management. In 2025 the founders relaunched the product as Verata, Inc. at veratainsight.com; the aiFlow brand site and the company's Auth0 identity tenant at auth.aiflow.solutions both remain live and the Verata application authenticates against them. aiFlow publishes no developer program, no API documentation and no machine-readable API contract — its security page states the platform is self-contained by design with no third-party ATS or CRM integrations
  — so the only machine-readable documents it serves are the OpenID Connect and OAuth 2.0 authorization-server discovery documents that gate its own application.
image: https://res.cloudinary.com/verdiq/image/upload/v1769805304/verata/verata_private_equity_firm_network_paths.png
layout: provider
modified: '2026-09-14'
name: aiFlow
nav: Providers
network: true
overview: 'aiFlow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Executive Search, Private Equity, Talent Intelligence, and People Data.


  aiFlow''s developer surface includes pricing, support, engineering blog, authentication, and 11 more developer resources.'
plans:
- name: Aiflow Plans Pricing
  plan_count: 3
  slug: aiflow-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aiflow Rate Limits
  slug: aiflow-rate-limits
scopes:
- name: Aiflow Scopes
  scope_count: 0
  slug: aiflow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    operational_transparency: 0.0
  previous_composite: 22.2
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiflow Authentication
  slug: aiflow-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aiflow Domain Security
  slug: aiflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiflow
tags:
- Company
- Executive Search
- Private Equity
- Talent Intelligence
- People Data
- Company Data
- Market Intelligence
- Artificial Intelligence
- Y Combinator
- No Public API
website: https://aiflow.solutions/
---
