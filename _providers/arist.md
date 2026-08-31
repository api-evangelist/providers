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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Arist runs its customer-facing authentication on an Auth0 tenant at auth.arist.app. The tenant publishes an RFC 8414 / OpenID Connect Discovery document anonymously, describing the authorization, toke
  name: Arist Identity (OIDC)
  slug: identity
- description: The Arist platform API host at api.arist.app fronts an Amazon API Gateway deployment and answers every anonymous request with a 403 MissingAuthenticationToken, so the surface is real but entirely cred
  name: Arist Platform API
  slug: platform
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://arist.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/arist_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://help.arist.co/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.arist.co/
- group: operate
  title: ''
  type: Support
  url: https://help.arist.co/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://help.arist.co/article/1117-new-user-onboarding
- group: company
  title: ''
  type: Blog
  url: https://arist.com/resources/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aristco
- group: start
  title: ''
  type: Login
  url: https://arist.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arist.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arist.com/legal/privacy-policy
- group: other
  title: ''
  type: SubProcessors
  url: https://arist.com/legal/sub-processors
- group: auth
  title: ''
  type: Compliance
  url: https://trust.arist.co/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arist.app/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arist-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arist-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arist-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arist-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/arist-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arist-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arist-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/arist-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arist-conventions.yml
created: '2026-08-02'
description: Arist is an AI-native enterprise enablement platform, founded in 2019 and headquartered in New York City, that delivers training, communications, nudges and surveys in the flow of work over SMS, WhatsApp, Slack, Microsoft Teams, email and its own web and mobile apps rather than through a traditional LMS portal. The product is packaged as an agent suite — a Needs Analysis agent that interviews employees and syncs HRIS/CRM/LMS data, a Creator agent that generates and translates courses into 50+ languages, a Core Platform and Routing agent that decides who receives what and where, and an Analytics agent that ties delivery back to business goals. Customer systems (Workday, Salesforce, SAP SuccessFactors, Cornerstone, ServiceNow, Oracle) are connected through Workato-hosted connectors rather than a publicly documented REST API; the platform API host at api.arist.app is credential-gated and no public OpenAPI, SDK or developer portal is published. Identity is handled by an Auth0 tenant
  at auth.arist.app supporting SAML and OIDC single sign-on plus one-time email passcodes.
image: https://framerusercontent.com/images/MVcgY55O8cBGMijaJPKzShyOgk.png
layout: provider
modified: '2026-08-02'
name: Arist
nav: Providers
network: true
overview: 'Arist publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Learning, Training, Enablement, and Microlearning.


  Arist''s developer surface includes documentation, support, getting-started guide, engineering blog, authentication, changelog, and 18 more developer resources.'
random_paper: 1
scopes:
- name: Arist Scopes
  scope_count: 14
  slug: arist-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 29.4
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arist/refs/heads/main/screenshots/arist-2026-08-07T161713.png
security:
- kind: authentication
  name: Arist Authentication
  slug: arist-authentication
  summary_line: openIdConnect/oauth2/saml · 3 schemes
- kind: domain-security
  name: Arist Domain Security
  slug: arist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Arist Trust Center
  slug: arist-trust-center
  summary_line: ISO 27001, ISO 27701, ISO 42001, SOC 2 Type 2
slug: arist
tags:
- Company
- Learning
- Training
- Enablement
- Microlearning
- Human Resources
- Messaging
- Artificial Intelligence
- Employee Communications
- Software-as-a-Service
website: https://arist.com/
---
