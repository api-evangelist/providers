---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.revv.so/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revvsales
- group: commercial
  title: ''
  type: Plans
  url: plans/revv-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revv-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revv-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/revv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.revv.so/trust/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.revv.so/trust/security.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revv-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revv.so/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.revv.so/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revv.so/termsofuse.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revv.so/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.revv.so/blog/
coverage:
  checked: '2026-08-14'
  detail: Revv's API is still advertised and priced on a frozen 2021 Webflow marketing site, but every surface behind it is dead after the LegalZoom acquisition — build.revv.so, the API reference named in Revv's own API-pricing FAQ, returns a Postman "Not found" 404, all ~200 www.revv.so/docs/* articles still in the sitemap return nginx 502, and api./apidocs./docs./help./app.revv.so all serve the LegalZoom single-page-app shell.
  evidence:
  - status: 404
    url: https://build.revv.so/
  - status: 502
    url: https://www.revv.so/docs/authenticate-your-revv-api
  - status: 200
    url: https://apidocs.revv.so/
  - status: 200
    url: https://www.revv.so/developers/api-pricing.html
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Revv (formerly RevvSales) is a document automation and electronic-signature platform that helps businesses prepare, automate, and execute business paperwork such as sales contracts, proposals, and agreements. The product offers 1,000+ customizable document templates, drag-and-drop editing, rule-based approval workflows, eSignatures with audit trails, real-time collaboration, and analytics, plus integrations with Salesforce, HubSpot, Google Sheets, and Zapier alongside a native REST API. Founded in India and backed by Lightspeed Venture Partners, Revv was acquired by LegalZoom (announced 2022-10-17). The marketing site still sells the API and publishes a per-document price list ($4.00 / $2.00 / $1.50 by annual volume, OAuth 2.0, webhooks, API logs, free sandbox accounts), but every developer surface behind it is gone: the API reference host build.revv.so returns 404 from a Postman-hosted "Not found" page, all ~200 www.revv.so/docs/* help articles still listed in the sitemap
  return nginx 502, and the api., apidocs., docs., help. and app. subdomains all serve the LegalZoom application shell. No Revv OpenAPI, AsyncAPI, GraphQL SDL, Postman collection, MCP server or agent card is published anywhere.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revv.png
layout: provider
modified: '2026-08-14'
name: Revv
nav: Providers
network: true
overview: 'Revv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Document Automation, Electronic Signature, Contract Management, and Sales Enablement.


  Revv''s developer surface includes authentication, pricing, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Revv Plans Pricing
  plan_count: 3
  slug: revv-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Revv Rate Limits
  slug: revv-rate-limits
score:
  band: thin
  composite: 28.5
  delta: -0.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Revv Authentication
  slug: revv-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Revv Domain Security
  slug: revv-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Revv Vulnerability Disclosure
  slug: revv-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Revv Trust Center
  slug: revv-trust-center
  summary_line: ISO 27001:2013, SAS 70 / SOC 2, ISO 27001:2013, SAS 70 / SSAE 16, PCI DSS, GDPR
slug: revv
tags:
- Company
- Document Automation
- Electronic Signature
- Contract Management
- Sales Enablement
- Workflow Automation
- SaaS
website: https://www.revv.so/
---
