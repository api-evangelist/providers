---
access_model:
  confidence: high
  label: No public or partner API programme
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - well-known
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Primerica's own API gateway (Broadcom/CA Layer7 — unmatched paths return a SOAP "Policy Falsified" fault in the layer7tech policy-fault namespace). It fronts the backend-for-frontend routes used by th
  name: Primerica API Gateway
  slug: primerica-api-gateway
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.primerica.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Primerica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/primerica
- group: operate
  title: ''
  type: Support
  url: https://www.primerica.com/public/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.primerica.com/public/news-insights.html
- group: start
  title: ''
  type: Login
  url: https://my.primerica.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.primerica.com/public/terms_conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.primerica.com/public/privacy/privacy_notices.html
- group: auth
  title: ''
  type: Security
  url: https://www.primerica.com/public/privacy/primerica-responsible-disclosure-practice.html
- group: auth
  href: https://artifacts.apis.io/primerica/security/primerica-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/primerica-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/primerica/security/primerica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/primerica-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/primerica/well-known/primerica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/primerica-well-known.yml
- group: auth
  href: https://artifacts.apis.io/primerica/authentication/primerica-authentication.yml
  title: ''
  type: Authentication
  url: authentication/primerica-authentication.yml
- group: auth
  href: https://artifacts.apis.io/primerica/scopes/primerica-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/primerica-scopes.yml
- group: design
  href: https://artifacts.apis.io/primerica/conformance/primerica-conformance.yml
  title: ''
  type: Conformance
  url: conformance/primerica-conformance.yml
- group: agent
  href: https://artifacts.apis.io/primerica/llms/primerica-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/primerica-llms.txt
- group: build
  href: https://artifacts.apis.io/primerica/packages/primerica-packages.yml
  title: ''
  type: Packages
  url: packages/primerica-packages.yml
- group: commercial
  href: https://artifacts.apis.io/primerica/plans/primerica-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/primerica-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/primerica/rate-limits/primerica-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/primerica-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/primerica/finops/primerica-finops.yml
  title: ''
  type: FinOps
  url: finops/primerica-finops.yml
created: '2026-04-19'
description: 'Primerica, Inc. (NYSE: PRI) is a US and Canadian financial-services company that distributes term life insurance, mutual funds and annuities, mortgages, debt-consolidation, auto and home insurance, pre-paid legal services and identity-theft protection to middle-income households through a large independent sales force. Primerica operates no public or partner API programme: as of 2026-09-14 there is no developer portal, no published OpenAPI, AsyncAPI, GraphQL, WSDL or Protobuf contract, no SDK on any package registry, no MCP server, no status page and no API pricing. What it does publish to the open internet is machine-readable identity infrastructure — anonymous OAuth 2.0 and OpenID Connect discovery documents for the two Okta identity orgs behind the MyPrimerica client portal and the Primerica Online representative portal, and for its own Broadcom/CA Layer7 API gateway at gtw.primericaonline.com — together with a published responsible-disclosure policy.'
finops:
- has_sources: true
  method: generated
  name: Primerica Finops
  primary_unit: ''
  service_category: Financial Services
  slug: primerica-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/primerica.png
layout: provider
modified: '2026-09-14'
name: Primerica
nav: Providers
network: true
overview: 'Primerica is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial Services, Life Insurance, Identity, and Authentication.


  Primerica''s developer surface includes support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Primerica Plans Pricing
  plan_count: 0
  slug: primerica-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Primerica Rate Limits
  slug: primerica-rate-limits
scopes:
- name: Primerica Scopes
  scope_count: 8
  slug: primerica-scopes
  summary_line: 8 scopes
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 23.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 42.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/primerica/primerica-2026-06-20T192103.png
security:
- kind: authentication
  name: Primerica Authentication
  slug: primerica-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Primerica Domain Security
  slug: primerica-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Primerica Vulnerability Disclosure
  slug: primerica-vulnerability-disclosure
  summary_line: Hackerone
slug: primerica
tags:
- Insurance
- Financial Services
- Life Insurance
- Identity
- Authentication
- OAuth
- API Gateway
website: https://www.primerica.com
---
