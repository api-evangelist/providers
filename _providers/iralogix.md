---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The publicly reachable OpenID Connect / OAuth 2.0 authorization server that fronts the IRALOGIX partner platform. It publishes a full OIDC discovery document at /.well-known/openid-configuration and a
  name: IRALOGIX Partner Authorization Server
  slug: iralogix-partner-authorization-server
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iralogix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iralogix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partner.iralogix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iralogix.com/
- group: company
  title: ''
  type: Blog
  url: https://iralogix.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://iralogix.com/feed/
- group: start
  title: ''
  type: Login
  url: https://partner.iralogix.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iralogix.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://iralogix.com/contact/
- group: auth
  title: ''
  type: Compliance
  url: https://iralogix.com/platform/
- group: auth
  title: ''
  type: Authentication
  url: authentication/iralogix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/iralogix-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iralogix-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iralogix-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iralogix-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iralogix
created: '2026-08-04'
description: 'IRALOGIX is a Pittsburgh, Pennsylvania fintech that operates a cloud-native, white-label IRA (Individual Retirement Account) recordkeeping and administration platform for financial institutions — banks, wealth managers, brokerages, recordkeepers and advisors — who use it to offer digital IRA programs under their own brand. The platform covers onboarding, contributions, trading, distributions, rollovers, compliance monitoring and administration end to end, and the company markets "API-driven connectivity and real-time data flows" that integrate with existing custodial and recordkeeping infrastructure rather than replacing it. The developer surface is partner-gated: documentation at docs.iralogix.com sits behind Okta visitor authentication and the partner console at partner.iralogix.com behind an Auth0 tenant, so no public OpenAPI, AsyncAPI or SDK is published. The company states SSAE SOC 2 Type 1 and SSAE SOC 1 Type 2 attestation.'
image: https://iralogix.com/wp-content/uploads/2025/11/Iralogix-logo.svg
layout: provider
modified: '2026-08-04'
name: IRALOGIX
nav: Providers
network: true
overview: 'IRALOGIX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Retirement, IRA, and Recordkeeping.


  IRALOGIX''s developer surface includes documentation, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 2
scopes:
- name: Iralogix Scopes
  scope_count: 14
  slug: iralogix-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iralogix/refs/heads/main/screenshots/iralogix-2026-08-07T170914.png
security:
- kind: authentication
  name: Iralogix Authentication
  slug: iralogix-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Iralogix Domain Security
  slug: iralogix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iralogix
tags:
- Company
- Financial-Services
- Retirement
- IRA
- Recordkeeping
- Wealth Management
- Fintech
- Compliance
- White Label
- Retirement Technology
website: https://iralogix.com/
---
