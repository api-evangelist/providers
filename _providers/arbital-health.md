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
    dynamic_client_registration: false
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The JSON API behind the Arbital Health adjudication platform at platform.arbitalhealth.com. Observed live and returning JSON, but every resource path answers 401 {"error":"Unauthorized"} to an anonymo
  name: Arbital Health Platform API
  slug: platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://arbitalhealth.com
- group: company
  title: ''
  type: Blog
  url: https://arbitalhealth.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://arbitalhealth.com/blog/rss.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arbitalhealth.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://platform.arbitalhealth.com/
- group: company
  title: ''
  type: Careers
  url: https://arbitalhealth.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arbital-health/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/arbitalhealth
- group: auth
  title: ''
  type: TrustCenter
  url: security/arbital-health-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.arbitalhealth.com/
- group: auth
  title: ''
  type: Security
  url: https://security.arbitalhealth.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arbital-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arbital-health-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arbital-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arbital-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arbital-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arbital-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arbital-health-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Arbital Health runs a real JSON API at platform.arbitalhealth.com/api — /api/health answers 200 — but every resource path, including /api/openapi.json, returns 401 {"error":"Unauthorized"} to an anonymous caller, and no developer portal, API reference or spec exists anywhere on the marketing site (arbitalhealth.com is a 13-page HubSpot CMS site with no /docs, /developers or /api route).
  evidence:
  - status: 200
    url: https://platform.arbitalhealth.com/api/health
  - status: 401
    url: https://platform.arbitalhealth.com/api/openapi.json
  - status: 404
    url: https://arbitalhealth.com/openapi.json
  - status: 404
    url: https://arbitalhealth.com/developers
  - status: 200
    url: https://auth.arbitalhealth.com/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Arbital Health is a healthcare technology and actuarial-services company building the neutral third-party infrastructure for adjudicating outcomes-based (value-based care) contracts between payers, providers, employers, risk-bearing entities and point-solution vendors. Its cloud platform centralizes risk contracts, ingests and validates claims and eligibility data, runs actuarial calculations (IBNR, MLR, benchmarks, attribution), predicts and monitors contract performance, and adjudicates settlement between the parties. Product lines include the Adjudication Platform, ATLAS, Merlin AI, and Arbital Flex — a self-serve actuarial AI tool for payors and providers — alongside a traditional actuarial consulting practice built on the acquired Santa Barbara Actuaries team. The company launched in 2024, raised a $10M Series A led by Transformation Capital, and holds SOC 2 Type 2 and HITRUST i1 certification.
image: https://44728686.fs1.hubspotusercontent-na1.net/hubfs/44728686/Arbital_Logo_Full_Color_KO_rgb_022124.png
layout: provider
modified: '2026-08-06'
name: Arbital Health
nav: Providers
network: true
overview: 'Arbital Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Insurance, Value-Based Care, and Actuarial.


  Arbital Health''s developer surface includes engineering blog, authentication, and 16 more developer resources.'
random_paper: 3
scopes:
- name: Arbital Health Scopes
  scope_count: 3
  slug: arbital-health-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 26.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 74.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arbital-health/refs/heads/main/screenshots/arbital-health-2026-08-07T161614.png
security:
- kind: authentication
  name: Arbital Health Authentication
  slug: arbital-health-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Arbital Health Domain Security
  slug: arbital-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Arbital Health Vulnerability Disclosure
  slug: arbital-health-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Arbital Health Trust Center
  slug: arbital-health-trust-center
  summary_line: SOC 2 Type 2, HITRUST i1
slug: arbital-health
tags:
- Company
- Healthcare
- Health Insurance
- Value-Based Care
- Actuarial
- Claims
- Payers
- Providers
- Analytics
- Artificial Intelligence
website: https://arbitalhealth.com
---
