---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'First Digital''s RESTful API suite for programmatic access to its trust and custody data and services. The provider''s product page describes seven capability areas: client onboarding (business and indi'
  name: Open Trust APIs
  slug: first-digital-trust-open-trust-apis
artifact_total: 7
asyncapis:
- description: ''
  name: First Digital Trust Webhooks
  slug: first-digital-trust-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://1stdigital.com/
- group: docs
  title: ''
  type: Documentation
  url: https://1stdigital.com/open-trust-apis/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.1stdigital.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.1stdigital.com/kb
- group: start
  title: ''
  type: Login
  url: https://portal.1stdigital.com/
- group: company
  title: ''
  type: Blog
  url: https://1stdigital.com/news-and-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://1stdigital.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1stdigital.com/legal-and-regulatory/acceptable-use-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1stdigital.com/legal-and-regulatory/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://1stdigital.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://1stdigital.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://1stdigital.com/legal-and-regulatory/
- group: auth
  title: ''
  type: TrustCenter
  url: security/first-digital-trust-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/first-digital-trust-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-digital-trust-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/first-digital-trust-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-digital-trust-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-digital-trust-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/first-digital-trust-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/first-digital-trust-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/first-digital-trust-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-digital-trust-llms.txt
coverage:
  checked: '2026-08-12'
  detail: First Digital markets "Open Trust APIs" with seven named capability areas (onboarding, KYC/AML, account information, instruction initiation, reporting, webhooks, SSO) but the product page carries no reference, no base URL, no signup and no spec — its only call to action is "Become a Client"; the client portal is Microsoft Entra sign-in and the public help center holds only end-user Client Portal articles.
  evidence:
  - status: 403
    url: https://1stdigital.com/open-trust-apis/
  - status: 200
    url: https://helpdesk.1stdigital.com/kb
  - status: 403
    url: https://portal.1stdigital.com/openapi.json
  - status: 404
    url: https://helpdesk.1stdigital.com/openapi.json
  - status: 200
    url: https://1stdigital.com/.well-known/security.txt
  reason: sales-gate
  state: gated
created: '2026-08-12'
description: First Digital Trust Limited (trading as First Digital) is a Hong Kong-headquartered, technology-driven trust and custody institution serving the digital asset industry — blockchain startups, money service businesses, exchanges and token issuers. It provides multi-asset trust and custody across major fiat currencies, digital assets and securities, plus fiat gateways, settlement and clearing, payments rails, accounting and compliance infrastructure. It markets a developer-facing product, "Open Trust APIs" — an industry-standard RESTful API suite covering client onboarding, KYC/AML data access, account information, instruction initiation, reporting, webhooks and an SSO authentication service — but publishes no public developer portal, API reference or machine-readable specification; API access is reached through a client relationship. The firm is licensed as a Trust or Company Service Provider in Hong Kong (TC006771) and registered under section 78(1) of the Trustee Ordinance (Cap.
  29), and is SOC 1 Type 2, SOC 2 Type 2 and ISO 27001 certified.
image: https://cdn.1stdigital.com/brand/favicon.png
layout: provider
modified: '2026-08-12'
name: First Digital Trust
nav: Providers
network: true
overview: 'First Digital Trust publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Assets, Custody, Trust Services, and Financial Services.


  The First Digital Trust catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  First Digital Trust''s developer surface includes documentation, support, engineering blog, and 19 more developer resources.'
plans:
- name: First Digital Trust Plans Pricing
  plan_count: 0
  slug: first-digital-trust-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: First Digital Trust Rate Limits
  slug: first-digital-trust-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 15.2
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: First Digital Trust Domain Security
  slug: first-digital-trust-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: First Digital Trust Vulnerability Disclosure
  slug: first-digital-trust-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: First Digital Trust Trust Center
  slug: first-digital-trust-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001, CSA STAR Level 1 (Self-Assessment)
slug: first-digital-trust
tags:
- Company
- Digital Assets
- Custody
- Trust Services
- Financial Services
- Banking
- Payments
- Compliance
- Cryptocurrency
- Hong Kong
website: https://1stdigital.com/
---
