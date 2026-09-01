---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/trust-will-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trust-will-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trust-will-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trustandwill.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/trust-will_stock/
- group: operate
  title: ''
  type: Support
  url: https://help.trustandwill.com/hc/en-us/
- group: company
  title: ''
  type: Blog
  url: https://trustandwill.com/learn/
- group: commercial
  title: ''
  type: Pricing
  url: https://trustandwill.com/compare
- group: start
  title: ''
  type: SignUp
  url: https://trustandwill.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.trustandwill.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trustandwill.com/security/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trustandwill.com/security/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://trustandwill.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://trustandwill.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/trust-will-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trust-will-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Trust & Will's own EstateOS launch announcement promises an "open API, MCP, and SDKs for enterprise integration" and api.trustandwill.com is a live first-party API host, but every documentation and discovery path on it 404s and the only route to it is the partnerships contact-sales form — there is no public developer portal, reference, or specification anywhere on the domain.
  evidence:
  - status: 200
    url: https://trustandwill.com/learn/estateos-launch-announcement
  - status: 404
    url: https://api.trustandwill.com/openapi.json
  - status: 404
    url: https://api.trustandwill.com/.well-known/oauth-authorization-server
  - status: 404
    url: https://trustandwill.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: Trust & Will is a San Diego-based digital estate planning and probate company that lets individuals and families create legally valid wills, revocable living trusts, guardianship documents and probate filings online, with attorney-drafted state-specific documents and notarization support. Alongside its direct-to-consumer product it runs an enterprise and professional channel — EstateOS, plus programs for financial advisors, estate attorneys, nonprofits, banks and credit unions — that embeds estate planning into partner client experiences. The company reports more than one million members and 200+ enterprise partners including AARP, Fifth Third Bank, LPL Financial, UBS and USAA. Its EstateOS launch announcement states that an open API, MCP server and SDKs for enterprise integration are planned, but as of this profile no public developer portal, API reference or machine-readable specification is published — partner integration runs through a sales and partnership conversation.
image: https://trustandwill.com/images/trust-and-will-logo.png
layout: provider
modified: '2026-08-05'
name: Trust & Will
nav: Providers
network: true
overview: 'Trust & Will is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Estate Planning, Wills And Trusts, Probate, and Legal.


  Trust & Will''s developer surface includes support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 22.8
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Trust Will Domain Security
  slug: trust-will-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trust Will Vulnerability Disclosure
  slug: trust-will-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Trust Will Trust Center
  slug: trust-will-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: trust-will
tags:
- Company
- Estate Planning
- Wills And Trusts
- Probate
- Legal
- Financial-Services
- Wealth Management
- Fintech
website: https://trustandwill.com/
---
