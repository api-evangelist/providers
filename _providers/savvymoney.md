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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: JWT-based Single Sign-On REST API that lets a partner's online or mobile banking platform transfer an authenticated member into SavvyMoney without a second set of credentials. Publicly documented oper
  name: SavvyMoney SSO REST API
  slug: savvymoney-sso-rest-api
- description: Partner-facing REST API that returns select credit data for an SSO-identified member so the partner can render it inside its own experience. SavvyMoney's published Mobile Integration Guide names two o
  name: SavvyMoney External Credit API
  slug: savvymoney-external-credit-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.savvymoney.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.savvymoney.com/why-savvymoney/integration-partners/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.savvymoney.com
- group: operate
  title: ''
  type: Support
  url: https://www.savvymoney.com/book-a-demo/
- group: company
  title: ''
  type: Blog
  url: https://www.savvymoney.com/category/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.savvymoney.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://www.savvymoney.com/book-a-demo/
- group: start
  title: ''
  type: Login
  url: https://hub.savvymoney.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.savvymoney.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.savvymoney.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.savvymoney.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/savvymoney-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.savvymoney.com/
- group: auth
  title: ''
  type: Compliance
  url: security/savvymoney-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/savvymoney-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/savvymoney-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/savvymoney-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/savvymoney-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/savvymoney-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/savvymoney-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/savvymoney-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/savvymoney-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/savvymoney-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/savvymoney-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/savvymoney-rate-limits.yml
created: '2026-08-26'
description: 'SavvyMoney is a Dublin, California based financial technology company that supplies credit score, credit monitoring, financial wellness, pre-qualified offer and digital account-opening software to banks and credit unions. Its platform is delivered embedded inside a financial institution''s existing online and mobile banking rather than as a standalone destination, and SavvyMoney states it is live across 70+ pre-built integrations spanning 40+ digital banking platforms including Alkami, Fiserv, Q2, Lumin and Candescent. The technical surface partners integrate against is a partner-scoped REST API on creditscore.savvymoney.com: a JWT-based Single Sign-On API (authenticate, sign-on, optional browser fingerprint, prolong, log off, and a RelayPost form endpoint) that hands a partner''s authenticated member into SavvyMoney without a second credential, plus an External Credit API that returns User Status and User Credit Score data so the partner can render score, score change and
  monitoring alerts in its own UI. Embeddable iFrame widgets (score widget, offer widget, desktop and mobile dashboards) are published alongside the API, and a documented beta environment runs at creditscoretest.savvymoney.com. Credentials, the full API document and the partner hub are gated behind a partner agreement; no OpenAPI, AsyncAPI, SDK, MCP server or agent card is published publicly.'
image: https://www.savvymoney.com/wp-content/uploads/2022/12/cropped-SM_favicon-180x180-1-180x180.png
layout: provider
modified: '2026-08-26'
name: SavvyMoney
nav: Providers
network: true
overview: 'SavvyMoney publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Credit Scores, Credit Monitoring, and Financial Wellness.


  SavvyMoney''s developer surface includes documentation, support, engineering blog, signup flow, changelog, and 20 more developer resources.'
plans:
- name: Savvymoney Plans Pricing
  plan_count: 0
  slug: savvymoney-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Savvymoney Rate Limits
  slug: savvymoney-rate-limits
scopes:
- name: Savvymoney Scopes
  scope_count: 0
  slug: savvymoney-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 40.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 74.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Savvymoney Authentication
  slug: savvymoney-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Savvymoney Domain Security
  slug: savvymoney-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Savvymoney Vulnerability Disclosure
  slug: savvymoney-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Savvymoney Trust Center
  slug: savvymoney-trust-center
  summary_line: SOC 2 Type 2, CSA STAR Level 1, CSA STAR Level 2, CSA Trusted Cloud Provider, TRUSTe
slug: savvymoney
tags:
- Company
- Financial-Services
- Credit Scores
- Credit Monitoring
- Financial Wellness
- Banking
- Credit Unions
- Fintech
- Single Sign-On
- Embedded Finance
- Lending
- Account Opening
website: https://www.savvymoney.com/
---
