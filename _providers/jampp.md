---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'GraphQL reporting API for Jampp advertisers. The pivot query returns funnel metrics — impressions, clicks, spend, installs, events, CPC/CPM/CTR/CPI/CPA/ROAS — grouped by any combination of documented '
  name: Jampp Reporting API
  slug: jampp-reporting-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://jampp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jampp.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jampp.com/docs/reporting-api/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jampp.com/docs/reporting-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.jampp.com/docs/reporting-api-client/usage.html
- group: operate
  title: ''
  type: Support
  url: https://www.jampp.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.jampp.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jampp
- group: start
  title: ''
  type: SignUp
  url: https://auth.jampp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jampp.com/advertisers-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jampp.com/privacy-policy-terms-and-conditions
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jampp-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/jampp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jampp-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jampp-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jampp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jampp-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jampp-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jampp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jampp-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jampp-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jampp-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jampp-reporting-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jampp-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jampp-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jampp-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jampp-llms.txt
created: '2026-08-12'
description: Jampp is a programmatic demand-side platform for mobile app growth, founded in 2013 and now an Affle company, with hubs in San Francisco, Buenos Aires, Sao Paulo and Singapore. It buys user acquisition, app retargeting and CTV inventory on behalf of app advertisers in commerce, fintech, gaming and delivery, and reports the resulting funnel — impressions, clicks, installs and in-app events — back to customers. Its one public developer surface is the Jampp Reporting API, a GraphQL endpoint that serves synchronous and asynchronous "pivot" reports across roughly seventy campaign, creative, geo, publisher and SKAdNetwork dimensions, authenticated with OAuth 2.0 client credentials issued from the Silver dashboard.
image: https://cdn.prod.website-files.com/60a2dbe1d34866625cde6145/60a3205afb51116f7b844c73_jampp-featured-image.png
layout: provider
modified: '2026-08-12'
name: Jampp
nav: Providers
network: true
overview: 'Jampp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Mobile, and Analytics.


  Jampp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 21 more developer resources.'
plans:
- name: Jampp Plans Pricing
  plan_count: 0
  slug: jampp-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Jampp Rate Limits
  slug: jampp-rate-limits
scopes:
- name: Jampp Scopes
  scope_count: 1
  slug: jampp-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: thin
  composite: 33.8
  delta: -0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 22.0
    operational_transparency: 18.4
  previous_composite: 34.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Jampp Authentication
  slug: jampp-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Jampp Domain Security
  slug: jampp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jampp
tags:
- Company
- Advertising
- Marketing
- Mobile
- Analytics
- Reporting
- GraphQL
- Demand-Side Platform
- App Marketing
- Attribution
website: https://jampp.com/
---
