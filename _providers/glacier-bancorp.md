---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 5.0
  scored_at: '2026-09-14'
api_count: 1
apis:
- description: The OpenID Connect issuer Glacier Bank serves at connect.glacierbank.com for its Jack Henry Banno Digital Toolkit tenant. Issuer https://connect.glacierbank.com/a/consumer/api/v0/oidc; the base URL fo
  name: Glacier Bank Digital Banking OIDC (Banno tenant)
  slug: glacier-bancorp-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/security/glacier-bancorp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glacier-bancorp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glacier-bancorp-inc
- group: company
  title: ''
  type: Website
  url: https://www.glacierbancorp.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/authentication/glacier-bancorp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/glacier-bancorp-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/scopes/glacier-bancorp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/glacier-bancorp-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/conformance/glacier-bancorp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/glacier-bancorp-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/well-known/glacier-bancorp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/glacier-bancorp-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/llms/glacier-bancorp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/glacier-bancorp-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/plans/glacier-bancorp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glacier-bancorp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/glacier-bancorp/refs/heads/main/rate-limits/glacier-bancorp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/glacier-bancorp-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://connect.glacierbank.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.glacierbank.com/personal/open-an-account
- group: operate
  title: ''
  type: Support
  url: https://www.glacierbank.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glacierbank.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glacierbank.com/terms-and-conditions
created: '2026-04-19'
description: 'Glacier Bancorp, Inc. (NYSE: GBCI) is a Kalispell, Montana bank holding company operating Glacier Bank and its division banks across the western United States. It runs no developer program and publishes no OpenAPI: the only machine-readable API surface it serves from its own hosts is the OpenID Connect issuer for Glacier Bank''s Jack Henry Banno digital-banking tenant at connect.glacierbank.com, which advertises 116 OAuth scopes covering accounts, transfers, bill pay, ACH batches, wire transfers, positive pay and Zelle. Client credentials for that issuer are provisioned out of band, not self-service.'
finops:
- name: Glacier Bancorp Finops
  service_category: Banking
  slug: glacier-bancorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glacier-bancorp.png
layout: provider
modified: '2026-09-14'
name: Glacier Bancorp
nav: Providers
network: true
overview: 'Glacier Bancorp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial-Services, Digital Banking, OpenID Connect, and Authentication.


  Glacier Bancorp''s developer surface includes authentication, signup flow, support, and 12 more developer resources.'
plans:
- name: Glacier Bancorp Plans Pricing
  plan_count: 1
  slug: glacier-bancorp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Glacier Bancorp Rate Limits
  slug: glacier-bancorp-rate-limits
scopes:
- name: Glacier Bancorp Scopes
  scope_count: 116
  slug: glacier-bancorp-scopes
  summary_line: 116 scopes
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.4
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    operational_transparency: 5.3
  previous_composite: 7.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Glacier Bancorp Authentication
  slug: glacier-bancorp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Glacier Bancorp Domain Security
  slug: glacier-bancorp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glacier-bancorp
tags:
- Banking
- Financial-Services
- Digital Banking
- OpenID Connect
- Authentication
- Treasury Management
website: https://www.glacierbancorp.com
---
