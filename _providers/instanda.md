---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Instanda Webhooks
  slug: instanda-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instanda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instanda.com/
- group: company
  title: ''
  type: Blog
  url: https://instanda.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://instanda.com/blog/rss.xml
- group: company
  title: ''
  type: News
  url: https://instanda.com/news
- group: company
  title: ''
  type: Partners
  url: https://instanda.com/partners
- group: operate
  title: ''
  type: Support
  url: https://support.instanda.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instanda.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instanda-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instanda-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instanda-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://instanda.com/platform-security
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.trustero.com/trust/instanda
- group: auth
  title: ''
  type: TrustCenter
  url: security/instanda-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://instanda.com/platform-security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instanda-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instanda
- group: start
  title: ''
  type: Login
  url: https://design.instanda.com/Account/LogOn
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instanda.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instanda.com/terms-and-conditions
- group: operate
  title: ''
  type: ContactUs
  url: https://instanda.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/instanda
created: '2026-07-25'
description: 'INSTANDA is a London-headquartered no-code insurance core-systems vendor, trading as F2X Group Limited (England and Wales no. 05236974) from 70 Gracechurch Street in the City of London, a few streets from Lloyd''s. Founded in 2015 by Tim Hardcastle (CEO) and Derek Hill (Group CRO), it sells a cloud-native policy administration and digital distribution platform to insurance carriers, MGAs and brokers, letting business users configure products, rating, rules, documents, agent/broker portals and direct-to-consumer journeys without writing code. Its footprint spans property and casualty, life and health, and specialty lines across the UK, EMEA, North America and APAC, and it is architected on Microsoft Azure. INSTANDA markets itself as "API-first" and its platform does generate per-product REST/SOAP interfaces described with Swagger or WSDL definitions, plus Event Webhooks that HTTP POST customer event notifications to a subscriber-supplied URL - but none of that contract is public.
  There is no first-party developer portal: developer, developers, docs and api-docs subdomains all return 404, api.instanda.com resolves but answers anonymous requests with a bare 403, and support.instanda.com is a Freshdesk login wall. The Swagger surface has been located and it is gated - design.instanda.com/swagger/index.html is a registered route that redirects to the platform log-on page, while unknown paths on the same host hard-404. What INSTANDA does publish openly is a component-level status page at status.instanda.com covering four hosting regions, and a certification set of ISO 27001:2022, SOC 2, Cyber Essentials and PCI DSS SAQ A. Quote, bind, issue and FNOL all exist as platform capabilities - the status page names Quote Engine, Referrals, Renewals, MTAs, Endorsements and Claims as monitored services - but every one of them is reachable only through a licensed tenant or a partner integration. The honest finding is a partner-gated insurance core system with no public self-serve
  API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: INSTANDA
nav: Providers
network: true
overview: 'INSTANDA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Insurtech, Policy Administration, and Underwriting.


  The INSTANDA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  INSTANDA''s developer surface includes engineering blog, product news, support, and 19 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 36.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instanda/refs/heads/main/screenshots/instanda-2026-07-25T222607.png
security:
- kind: domain-security
  name: Instanda Domain Security
  slug: instanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Instanda Trust Center
  slug: instanda-trust-center
  summary_line: ISO 27001:2022, SOC 2, Cyber Essentials, PCI DSS SAQ A
slug: instanda
tags:
- Insurance
- United Kingdom
- Insurtech
- Policy Administration
- Underwriting
- Claims
- Property and Casualty
- Life Insurance
- Health Insurance
- Digital Distribution
- No Code
- Core Systems
- MGA
- Broker
- Webhooks
- Microsoft Azure
- Embedded Insurance
website: https://instanda.com/
---
