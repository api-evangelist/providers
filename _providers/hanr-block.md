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
  scored_at: '2026-09-16'
api_count: 2
apis:
- description: 'The partner-facing H&R Block integration surface — tax-data import from financial institutions, payroll providers and employer solutions. No public contract, reference or portal is reachable: api.hrbl'
  name: H&R Block API
  slug: hanr-block-api
- description: H&R Block's customer identity platform, a PingFederate authorization server at https://login.hrblock.com serving OpenID Connect discovery and RFC 8414 OAuth 2.0 authorization-server metadata anonymous
  name: H&R Block Identity (OAuth 2.0 / OpenID Connect)
  slug: hanr-block-identity
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.hrblock.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hrblock-dsa
- group: operate
  title: ''
  type: Support
  url: https://www.hrblock.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.hrblock.com/tax-center/newsroom/
- group: start
  title: ''
  type: Login
  url: https://account.hrblock.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hrblock.com/universal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hrblock.com/universal/digital-online-mobile-privacy-principles/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/authentication/hanr-block-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hanr-block-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/scopes/hanr-block-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hanr-block-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/well-known/hanr-block-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/hanr-block-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/well-known/hanr-block-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hanr-block-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/conformance/hanr-block-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hanr-block-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hrblock.com/responsible-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/security/hanr-block-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hanr-block-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/security/hanr-block-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hanr-block-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/lifecycle/hanr-block-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hanr-block-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/llms/hanr-block-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hanr-block-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/plans/hanr-block-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hanr-block-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/rate-limits/hanr-block-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hanr-block-rate-limits.yml
created: '2026-04-19'
description: 'H&R Block (NYSE: HRB) is a US tax-preparation company and Fortune 1000 constituent, operating retail tax offices, consumer and small-business tax software, and the MyBlock digital platform. It runs no public developer program: the hosts that make up its API estate — api.hrblock.com, developer.hrblock.com, the apiportal.hrblock.com Apigee portal, apigw, mcp, edge, services and connect — either do not resolve or refuse connections from the public internet, and integration is arranged bilaterally through the tax-import partner program. The one machine-readable contract H&R Block does serve publicly is the OAuth 2.0 / OpenID Connect discovery metadata for its customer identity platform at login.hrblock.com.'
finops:
- name: Hanr Block Finops
  service_category: Tax Preparation / Financial Services Partner API
  slug: hanr-block-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hanr-block.png
layout: provider
modified: '2026-09-14'
name: H&R Block
nav: Providers
network: true
overview: 'H&R Block publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Tax Preparation, Financial-Services, Fortune 1000, Identity, and Authentication.


  H&R Block''s developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Hanr Block Plans Pricing
  plan_count: 1
  slug: hanr-block-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Hanr Block Rate Limits
  slug: hanr-block-rate-limits
scopes:
- name: Hanr Block Scopes
  scope_count: 0
  slug: hanr-block-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    operational_transparency: 18.4
  previous_composite: 24.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hanr-block/refs/heads/main/screenshots/hanr-block-2026-06-20T182508.png
security:
- kind: authentication
  name: Hanr Block Authentication
  slug: hanr-block-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hanr Block Domain Security
  slug: hanr-block-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hanr Block Vulnerability Disclosure
  slug: hanr-block-vulnerability-disclosure
  summary_line: Hackerone
slug: hanr-block
tags:
- Tax Preparation
- Financial-Services
- Fortune 1000
- Identity
- Authentication
- OpenID Connect
- Consumer Software
website: https://www.hrblock.com
---
