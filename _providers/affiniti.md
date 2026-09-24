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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/security/affiniti-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affiniti-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://extu.com/
- group: other
  title: ''
  type: Product
  url: https://extu.com/platform/
- group: company
  title: ''
  type: About
  url: https://extu.com/about/
- group: company
  title: ''
  type: Blog
  url: https://extu.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://extu.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://partners.extu.com/knowledge-base/
- group: operate
  title: ''
  type: ContactUs
  url: https://extu.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://extu.com/about/careers/
- group: start
  title: ''
  type: Login
  url: https://app.extu.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://extu.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://extu.com/legal/general-terms-of-service/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/security/affiniti-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/affiniti-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://extu.com/legal/gdpr-trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://extu.com/resource/extu-soc-2-type-2-compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneAffiniti
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extu/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ExtuHq
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/affiniti
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/well-known/affiniti-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affiniti-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/authentication/affiniti-authentication.yml
  title: ''
  type: Authentication
  url: authentication/affiniti-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/scopes/affiniti-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/affiniti-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/conformance/affiniti-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affiniti-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/llms/affiniti-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affiniti-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/affiniti/refs/heads/main/plans/affiniti-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affiniti-plans-pricing.yml
coverage:
  checked: '2026-09-12'
  detail: 'Affiniti — trading today as Extu after the OneAffiniti / Incentive Solutions merger — sells a through-channel marketing and incentive SaaS platform as an end-user product and a managed service, and publishes no developer program of any kind: its own llms.txt indexes 661 pages and its three XML sitemaps every public URL, and neither names a developer portal, API reference, SDK, webhook or specification, while every OpenAPI/GraphQL/MCP/agent-card path probed on extu.com, oneaffiniti.com, app.extu.com and the cms-api.extu.com backend the Partner Experience app actually calls returns 404 (a Laravel "route could not be found" JSON body on cms-api, including for a random control path). The only machine-readable documents any Extu host serves are the OpenID Connect discovery documents for the two Auth0 tenants behind its CMS and partner logins, which are sign-in metadata for humans, not an API contract.'
  evidence:
  - status: 200
    url: https://extu.com/llms.txt
  - status: 200
    url: https://extu.com/sitemap_index.xml
  - status: 200
    url: https://extu.com/robots.txt
  - status: 404
    url: https://cms-api.extu.com/openapi.json
  - status: 404
    url: https://cms-api.extu.com/swagger.json
  - status: 404
    url: https://cms-api.extu.com/api-docs
  - status: 404
    url: https://cms-api.extu.com/api/v1
  - status: 404
    url: https://extu.com/.well-known/agent-card.json
  - status: 404
    url: https://extu.com/.well-known/agent.json
  - status: 404
    url: https://extu.com/.well-known/api-catalog
  - status: 404
    url: https://extu.com/.well-known/security.txt
  - status: 404
    url: https://oneaffiniti.com/apis.json
  - status: 200
    url: https://cms-login.extu.com/.well-known/openid-configuration
  - status: 200
    url: https://pexp-login.extu.com/.well-known/openid-configuration
  - status: 404
    url: https://extu.com/.well-known/affiniti-negative-control-7f3ab91c.json
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Affiniti is the channel-marketing software company founded in Sydney, Australia by Joel Montgomery and listed under that name on the EquityZen secondary market; it traded for most of its life as OneAffiniti and, after Capstreet-backed Incentive Solutions acquired it in April 2021, the combined business rebranded to Extu in September 2023, the brand its product and every live web property carry today. It sells a through-channel marketing automation and channel incentive platform that suppliers and distributors use to run co-branded campaigns, content syndication, rewards, rebates, SPIFFs and attribution for their reseller partners in technology, building, automotive, energy, insurance and medical channels. It is a SaaS product and managed service: its own llms.txt and full XML sitemap list no developer portal, API reference, SDK or machine-readable contract of any kind.'
image: https://extu.com/wp-content/uploads/2023/05/Extu_Logo_FullColor.png
layout: provider
modified: '2026-09-12'
name: Affiniti
nav: Providers
network: true
overview: 'Affiniti is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Channel Marketing, Marketing Automation, Through-Channel Marketing, and Partner Marketing.


  Affiniti''s developer surface includes engineering blog, support, YouTube channel, authentication, and 21 more developer resources.'
plans:
- name: Affiniti Plans Pricing
  plan_count: 0
  slug: affiniti-plans-pricing
random_paper: 6
scopes:
- name: Affiniti Scopes
  scope_count: 14
  slug: affiniti-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    operational_transparency: 2.6
  previous_composite: 20.7
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Affiniti Authentication
  slug: affiniti-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Affiniti Domain Security
  slug: affiniti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Affiniti Trust Center
  slug: affiniti-trust-center
  summary_line: SOC 2 Type 2, GDPR
slug: affiniti
tags:
- Company
- Channel Marketing
- Marketing Automation
- Through-Channel Marketing
- Partner Marketing
- Incentives
- Loyalty
- Rebates
- Rewards
- B2B SaaS
website: https://extu.com/
---
