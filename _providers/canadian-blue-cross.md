---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canadian-blue-cross-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluecross.ca/
- group: company
  title: ''
  type: About
  url: https://www.bluecross.ca/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.bluecross.ca/contact/
- group: company
  title: ''
  type: News
  url: https://www.bluecross.ca/news/
- group: company
  title: ''
  type: Blog
  url: https://www.bluecross.ca/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bluecross.ca/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.bluecross.ca/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluecross.ca/terms-of-use-privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluecross.ca/terms-of-use-privacy/
- group: other
  title: ''
  type: Accessibility
  url: https://www.bluecross.ca/accessibility/
- group: company
  title: ''
  type: Careers
  url: https://www.bluecross.ca/careers/
- group: other
  title: ''
  type: Sitemap
  url: https://www.bluecross.ca/sitemap_index.xml
- group: start
  title: ''
  type: Login
  url: https://www.bluecross.ca/memberweb/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canadian-blue-cross-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canadian-blue-cross-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canadian-blue-cross-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canadian-blue-cross-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canadian-blue-cross-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canadian-blue-cross-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canadian-blue-cross-llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'Blue Cross Canada (bluecross.ca) is the national consumer-facing brand of the Canadian Association of Blue Cross Plans, the association that owns the Blue Cross trademark in Canada and coordinates a federation of independent, largely not-for-profit regional Blue Cross plans — Alberta Blue Cross, Pacific Blue Cross, Manitoba Blue Cross, Saskatchewan Blue Cross, Ontario and Quebec Blue Cross (Canassurance), and Medavie Blue Cross. Operating in Canada since 1938, the federation covers roughly eight million Canadians a year across supplementary health and dental benefits, group and employee benefits, retiree plans, travel medical insurance, and term life and critical illness cover, and several member plans also administer public health programs on behalf of provincial and federal governments. Its API posture is partner-gated and effectively non-existent as a public surface: bluecross.ca is a WordPress marketing and region-routing site with no developer portal, no API reference,
  and no published OpenAPI, and the developer/developers/docs/api subdomains do not resolve at all. Members, plan sponsors, brokers, and health-care providers integrate through authenticated member portals, mobile apps, group-benefit employer portals, and third-party health-claim rails rather than through any self-serve API. Canada offers no forcing function that would change this — OSFI supervises prudentially, the provinces (FSRA, AMF) regulate market conduct, there is no open-insurance mandate, and Consumer-Driven Banking explicitly excludes insurance.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Blue Cross Canada
nav: Providers
network: true
overview: 'Blue Cross Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Health Insurance, Dental Benefits, and Travel Insurance.


  Blue Cross Canada''s developer surface includes product news, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 20
scopes:
- name: Canadian Blue Cross Scopes
  scope_count: 2
  slug: canadian-blue-cross-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 25.4
  delta: -0.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 25.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Canadian Blue Cross Authentication
  slug: canadian-blue-cross-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Canadian Blue Cross Domain Security
  slug: canadian-blue-cross-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canadian-blue-cross
tags:
- Insurance
- Canada
- Health Insurance
- Dental Benefits
- Travel Insurance
- Life Insurance
- Employee Benefits
- Group Benefits
- Claims
- Carrier
- Association
- No Public API
website: https://www.bluecross.ca/
---
