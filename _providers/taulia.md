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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.8
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The buyer-side integration API described in the SAP Taulia Description of Software Services. It carries the accounts-payable object set — supplier master, business unit, purchase orders, invoices, pay
  name: Taulia Buyer API
  slug: taulia-buyer-api
- description: 'The supplier-side integration API described in the SAP Taulia Description of Software Services. It exchanges information between the Taulia Platform and a supplier''s accounts-receivable data: submitti'
  name: Taulia Supplier API
  slug: taulia-supplier-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://taulia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.taulia.com/technical-resources
- group: start
  title: ''
  type: GettingStarted
  url: https://support.taulia.com/article/Easy-Guide-to-Activating-SAP-Taulia-with-S-4HANA-Cloud-Public-Edition
- group: operate
  title: ''
  type: Support
  url: https://support.taulia.com/contactsupport
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.taulia.com/
- group: company
  title: ''
  type: Blog
  url: https://taulia.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://taulia.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taulia
- group: start
  title: ''
  type: Login
  url: https://login.na1prd.taulia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taulia.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taulia.com/privacy-statement/
- group: auth
  title: ''
  type: Compliance
  url: https://taulia.com/sap-taulia-agreements/
- group: other
  title: ''
  type: Glossary
  url: https://taulia.com/glossary/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taulia.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taulia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taulia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/taulia-security.txt
- group: auth
  title: ''
  type: Security
  url: security/taulia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/taulia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taulia-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taulia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taulia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/taulia-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taulia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taulia-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/taulia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taulia-rate-limits.yml
created: '2026-08-29'
description: 'SAP Taulia is a working-capital and cash-flow acceleration platform for enterprises, their suppliers and their funding partners. Acquired by SAP in 2022 and now operated as SAP Taulia, it runs supply chain finance, dynamic discounting, ERP-embedded virtual cards, receivables finance, inventory finance, supplier self-service and supplier information management across SAP and non-SAP ERP estates. Its programmatic surface is an enterprise integration estate rather than a public developer platform: a Taulia Buyer API and Taulia Supplier API described in the Description of Software Services, an XMLRPC interface monitored per region on the public status page, a Taulia Connector supporting SFTP, AS2 and HTTP with EDI, cXML and XML payloads, and ERP add-ons for SAP, SAP Integration Suite managed gateway and Oracle EBS. No OpenAPI, AsyncAPI, GraphQL SDL, WSDL, Postman collection or SDK is published anywhere, and API credentials are provisioned during onboarding rather than through self-service.'
image: https://taulia.com/wp-content/uploads/2025/04/android-chrome-512x512-1-300x300.png
layout: provider
modified: '2026-08-29'
name: Taulia
nav: Providers
network: true
overview: 'Taulia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Working Capital, Supply Chain Finance, Dynamic Discounting, and Accounts Payable.


  Taulia''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, authentication, and 21 more developer resources.'
plans:
- name: Taulia Plans Pricing
  plan_count: 0
  slug: taulia-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Taulia Rate Limits
  slug: taulia-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 33.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Taulia Authentication
  slug: taulia-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Taulia Domain Security
  slug: taulia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taulia Vulnerability Disclosure
  slug: taulia-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Taulia Trust Center
  slug: taulia-trust-center
  summary_line: SSAE SOC 1 Type 2, PCI DSS (website scanning), GDPR / data protection, Export control and sanctions compliance
slug: taulia
tags:
- Company
- Working Capital
- Supply Chain Finance
- Dynamic Discounting
- Accounts Payable
- Accounts Receivable
- Invoicing
- Payments
- Procurement
- Financial-Services
- ERP Integration
- SAP
website: https://taulia.com/
---
