---
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Plumma Agentic Access
  operation_count: 1
  slug: plumma-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://connect.plumma.it/services
  baseurl_source: declared
  description: 'A single-operation aggregation API over mobile network operator intelligence. One POST /api call carries a phone number in E.164 form plus a `commands` array, and returns the requested signals in one '
  name: Plumma CONNECT API
  slug: plumma-connect-api
artifact_total: 10
common:
- group: design
  title: ''
  type: Conventions
  url: conventions/plumma-conventions.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/plumma-commands-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plumma-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plumma-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/plumma-status-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plumma-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plumma-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://connect.plumma.it/plumma-connect-docs/#security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/plumma-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/plumma-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plumma-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/plumma-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/plumma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plumma-llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://connect.ploomma.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connect.plumma.it/plumma-connect-docs/#terms-and-conditions
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plumma-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plumma-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plumma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plumma.it
- group: company
  title: ''
  type: Website
  url: https://connect.plumma.it
- group: start
  title: ''
  type: DeveloperPortal
  url: https://connect.plumma.it
- group: docs
  title: ''
  type: Documentation
  url: https://connect.plumma.it/plumma-connect-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://connect.plumma.it/plumma-connect-docs/
- group: operate
  title: ''
  type: StatusPage
  url: https://oneuptime.com/status-page/5c4b010b-1753-4d8f-8689-226d6e86d72a
- group: operate
  title: ''
  type: Support
  url: https://connect.plumma.it/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plumma.it/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://connect.plumma.it/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.plumma.it/company.html
- group: other
  title: ''
  type: Standards
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
- group: other
  title: ''
  type: Standards
  url: https://camaraproject.org/
- group: other
  title: ''
  type: Standards
  url: https://www.rfc-editor.org/rfc/rfc9457
- group: other
  title: ''
  type: Standards
  url: https://spec.openapis.org/oas/v3.1.0
created: '2026-09-07'
description: 'Plumma SRL is an Italian software house (VAT IT04209450362, REA MO-451932) with its registered office at Via Corsini 21, Fellicarolo, Fanano (Modena) and an operational office at Via Provinciale 175/B, Crespellano, Valsamoggia (Bologna). Its own product, Plumma Connect, is an aggregation gateway in front of mobile network operators: it sells enterprises a single integration point for the operator-held identity, SIM and network-state signals that the GSMA Open Gateway programme exposes, instead of requiring the buyer to onboard operator-by-operator and country-by-country. Plumma states it is a GSMA Open Gateway channel partner and names GSMA, TIM, AWS and WaveMaker among its partners. Its architectural position is the notable part, and it is deliberate. Rather than mirroring the CAMARA one-endpoint-per-capability shape, Plumma Connect publishes a SINGLE OpenAPI 3.1 operation — POST /api on https://connect.plumma.it/services — that takes a phone number in E.164 form plus a list
  of named commands (sim_swap, kyc_match, age_verification, current_carrier, porting_logs, roaming_intel, churn_tracker, digital_footprint and others), so the CAMARA surface is an implementation detail behind an abstraction layer rather than the developer contract. The company is not, however, standard-averse underneath: its KYC request schema carries the CAMARA KnowYourCustomer Match attribute vocabulary verbatim (in snake_case), and every 4xx/5xx returns an RFC 7807 problem document with a correlation_id. The divergence is at the endpoint shape, not the data model. The product is positioned for fraud prevention and identity verification, with company-stated coverage of 17 live countries across Europe, the Americas, APAC and Africa and 75+ network connections. Documentation, the OpenAPI and a draft-07 request schema are public and ungated, and the JavaScript documentation portal is backed by an unauthenticated JSON content API at connect.ploomma.com that serves 72 documents including the
  billing guide, SLA, terms and full command reference. Billing is EUR 200/month plus a prepaid wallet charged per served command; published rate limits are 2/5 RPS and 180 commands/day. There is no MCP server, no agent card, no SDKs and no /.well-known documents — the provider marks SDKs and webhooks ''under construction''.'
examples:
- key_count: 6
  name: Plumma Connect Api Examples
  slug: plumma-connect-api-examples
image: https://connect.plumma.it/wp-content/uploads/2026/03/PLUMMA-logo-bianco-inline-90x304-1.png
json_schemas:
- name: PlmRequest
  property_count: 4
  slug: plumma-plmrequest.schema
layout: provider
modified: '2026-09-07'
name: Plumma
nav: Providers
network: true
overview: 'Plumma publishes 1 API on the [APIs.io](https://apis.io/) network: CONNECT API. Tagged areas include Telecommunications, Network APIs, Italy, Europe, and GSMA Open Gateway.


  Plumma''s developer surface includes sandbox, signup flow, authentication, documentation, API reference, support, engineering blog, and 27 more developer resources.'
plans:
- name: Plumma Plans Pricing
  plan_count: 2
  slug: plumma-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Plumma Rate Limits
  slug: plumma-rate-limits
security:
- kind: authentication
  name: Plumma Authentication
  slug: plumma-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Plumma Domain Security
  slug: plumma-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Plumma Vulnerability Disclosure
  slug: plumma-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Plumma Trust Center
  slug: plumma-trust-center
  summary_line: trust center published
slug: plumma
tags:
- Telecommunications
- Network APIs
- Italy
- Europe
- GSMA Open Gateway
- CAMARA
- API Aggregator
- Fraud Prevention
- Identity Verification
- SIM Swap
- KYC
- Age Verification
- Number Verification
- Telco Intelligence
- Software Development
website: https://www.plumma.it
---
