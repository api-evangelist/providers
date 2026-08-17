---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigfoot-biomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigfootbiomedical.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bigfootbiomedical.com/blog.html
- group: operate
  title: ''
  type: Support
  url: https://www.bigfootbiomedical.com/contact.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigfootbiomedical.com/help/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigfootbiomedical.com/help/terms_of_use.html
- group: auth
  title: ''
  type: Security
  url: https://www.bigfootbiomedical.com/security.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BigfootBiomedical
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bigfoot-biomedical_stock/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bigfoot-biomedical-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bigfoot-biomedical-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigfoot-biomedical-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bigfoot-biomedical-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bigfoot-biomedical-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bigfoot-biomedical-llms.txt
coverage:
  checked: '2026-08-07'
  detail: Bigfoot Biomedical was acquired by Abbott in September 2023 and no longer exists as an independent company; bigfootbiomedical.com now CNAMEs to Abbott's platform (www-bigfootbiomedical-com.abbottapps.net), is headed "Bigfoot is Now Abbott", carries a 2024 copyright, and its 161-URL sitemap contains no developer, API or documentation page of any kind — the only live machine-readable document on any Bigfoot host is Salesforce Experience Cloud's own OIDC discovery file behind the login-gated Clinic Hub HCP portal.
  evidence:
  - status: 200
    url: https://www.bigfootbiomedical.com/sitemap.xml
  - status: 404
    url: https://www.bigfootbiomedical.com/openapi.json
  - status: 404
    url: https://www.bigfootbiomedical.com/.well-known/agent-card.json
  - status: 301
    url: https://www.bigfootbiomedical.com/developers
  - status: 401
    url: https://clinichub.bigfootbiomedical.com/openapi.json
  reason: defunct
  state: none
created: '2026-08-07'
description: Bigfoot Biomedical was a Milpitas, California medical-device company building connected insulin-management technology for people with insulin-requiring diabetes. Its flagship product, the FDA-cleared Bigfoot Unity Diabetes Management System, paired reusable smart insulin pen caps with Abbott FreeStyle Libre 2 iCGM data and a clinician-set dosing program, displaying real-time glucose values, trends and recommended correction doses on the pen cap itself, alongside a patient mobile app and a Salesforce-hosted Bigfoot Clinic Hub portal for healthcare professionals. Abbott announced its acquisition of Bigfoot in September 2023 and closed it the same month; the company is now fully absorbed into Abbott and its website is an Abbott-hosted archive headed "Bigfoot is Now Abbott." Bigfoot never operated a public developer program, and no OpenAPI, AsyncAPI, GraphQL SDL, SDK, webhook catalog or developer portal has ever been published on its own surface.
image: https://www.bigfootbiomedical.com/content/dam/corp/bigfoot-biomedical/press-releases/bigfoot-logo.png
layout: provider
modified: '2026-08-07'
name: Bigfoot Biomedical
nav: Providers
network: true
overview: 'Bigfoot Biomedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Medical Devices, and Diabetes.


  Bigfoot Biomedical''s developer surface includes engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 36
scopes:
- name: Bigfoot Biomedical Scopes
  scope_count: 36
  slug: bigfoot-biomedical-scopes
  summary_line: 36 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 23.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 23.4
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigfoot-biomedical/refs/heads/main/screenshots/bigfoot-biomedical-2026-08-07T162422.png
security:
- kind: authentication
  name: Bigfoot Biomedical Authentication
  slug: bigfoot-biomedical-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Bigfoot Biomedical Domain Security
  slug: bigfoot-biomedical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bigfoot Biomedical Vulnerability Disclosure
  slug: bigfoot-biomedical-vulnerability-disclosure
  summary_line: contact published
slug: bigfoot-biomedical
tags:
- Company
- Health
- Digital Health
- Medical Devices
- Diabetes
- Insulin Management
- Continuous Glucose Monitoring
- Connected Devices
- Acquired
website: https://www.bigfootbiomedical.com/
---
