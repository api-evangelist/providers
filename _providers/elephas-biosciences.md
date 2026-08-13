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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The private backend API behind the Elephas Portal, the secure cloud-based web application through which clinicians, laboratories and research partners receive elive test reports and manage specimen re
  name: Elephas Portal API
  slug: elephas-biosciences-portal-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://elephas.com/
- group: start
  title: ''
  type: Login
  url: https://portal.elephas.com/
- group: operate
  title: ''
  type: Support
  url: https://elephas.com/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://elephas.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://elephas.com/news/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elephas.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elephas.com/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://elephas.com/faqs
- group: other
  title: ''
  type: Documents
  url: https://elephas.com/resources/documents
- group: other
  title: ''
  type: Publications
  url: https://elephas.com/resources/publications
- group: company
  title: ''
  type: Careers
  url: https://elephas.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elephasbiosciences
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/elephas-biosciences
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elephas-biosciences-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elephas-biosciences-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elephas-biosciences-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elephas-biosciences-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elephas-biosciences-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elephas-biosciences-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elephas-biosciences-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elephas-biosciences-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elephas-biosciences-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elephas-biosciences-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Elephas runs a real ASP.NET Core API at portal.elephasapis.com behind the Elephas Portal, but every path on it — including /swagger and /swagger/v1/swagger.json — answers HTTP 401 with a WWW-Authenticate: Bearer challenge, and tokens are only issuable to an existing Elephas tenant through Azure AD B2C, so the Swagger contract the service already generates is readable only by active customers.'
  evidence:
  - status: 401
    url: https://portal.elephasapis.com/swagger/v1/swagger.json
  - status: 401
    url: https://portal.elephasapis.com/swagger
  - status: 404
    url: https://elephas.com/developers
  - status: 404
    url: https://elephas.com/llms.txt
  - status: 200
    url: https://na.login.elephas.com/bf865bf1-740f-49ec-922c-9b2c233faa13/B2C_1A_SMART_HRD_SUSI/v2.0/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-12'
description: Elephas Biosciences Corporation is a Madison, Wisconsin precision-oncology company that builds elive, a first-in-class functional immune-profiling platform that measures how a patient's own live tumor tissue responds to immunotherapy. The platform combines elive Edge (an automated instrument that cuts core-needle biopsies into uniform 300-micron viable fragments), elive Gel (a proprietary hydrogel that preserves the native tumor microenvironment) and the elive Method (a sequential treatment and cytokine-analysis strategy) to return a functional response readout within roughly 72 hours of biopsy. Clinicians receive elive test reports through a secure, cloud-based web application; researchers and drug developers receive custom reports plus raw data for in-house analysis. The company raised a $40M Series B-2 in November 2025 to commercialize elive as a laboratory developed test. Its digital surface is the Elephas Portal (portal.elephas.com), an Angular single-page application backed
  by an ASP.NET Core API at portal.elephasapis.com that is authenticated with Azure AD B2C on the company-controlled na.login.elephas.com identity host. No public developer program, API reference or machine-readable contract is published.
image: https://elephas.com/hubfs/raw_assets/public/ele_2026/images/ele-logo-tagline.svg
layout: provider
modified: '2026-08-12'
name: Elephas Biosciences
nav: Providers
network: true
overview: 'Elephas Biosciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Life Sciences, Biotechnology, and Precision Oncology.


  Elephas Biosciences'' developer surface includes support, engineering blog, FAQ, authentication, and 19 more developer resources.'
plans:
- name: Elephas Biosciences Plans Pricing
  plan_count: 0
  slug: elephas-biosciences-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Elephas Biosciences Rate Limits
  slug: elephas-biosciences-rate-limits
scopes:
- name: Elephas Biosciences Scopes
  scope_count: 2
  slug: elephas-biosciences-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 25.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Elephas Biosciences Authentication
  slug: elephas-biosciences-authentication
  summary_line: oauth2/openIdConnect/http · 2 schemes
- kind: domain-security
  name: Elephas Biosciences Domain Security
  slug: elephas-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elephas-biosciences
tags:
- Company
- Healthcare
- Life Sciences
- Biotechnology
- Precision Oncology
- Diagnostics
- Immunotherapy
- Clinical Research
- Laboratory
- Medical Devices
website: https://elephas.com/
---
