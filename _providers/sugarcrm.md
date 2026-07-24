---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 21.2
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Sugar REST API is hosted on each Sugar deployment at https://<site_url>/rest/v{version}/ (v10 through v11_20). It authenticates with two-legged OAuth 2.0 (password + refresh_token grants, OAuth-To
  name: Sugar REST API
  slug: sugar-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.sugarcrm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.sugarcrm.com/documentation/sugar_developer/
- group: docs
  title: ''
  type: Documentation
  url: https://support.sugarcrm.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://support.sugarcrm.com/documentation/sugar_developer/sugar_developer_guide_13.0/integration/web_services/rest_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sugarcrm.com/documentation/sugar_developer/
- group: operate
  title: ''
  type: Support
  url: https://sugarclub.sugarcrm.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sugarcrm.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sugarcrm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sugarcrm.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://portal.sugarondemand.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sugarcrm.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sugarcrm.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.sugarai.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sugarcrm-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sugarcrm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sugarcrm-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sugarcrm-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sugarcrm-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sugarcrm-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sugarai.com/legal/security-trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/sugarcrm-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sugarcrm-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/sugarcrm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sugarcrm-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sugarcrm-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sugarcrm-llms.txt
created: '2026-07-17'
description: SugarCRM (rebranding as Sugar AI) is a B2B sales CRM platform serving 4,000+ customers and over one million users across 120+ countries. Its product suite spans Sugar Sell (sales automation), Sugar Serve (customer service), Sugar Market (marketing automation), and sales-i (sales intelligence from ERP data), with an emphasis on domain-specific AI that surfaces opportunities and recommends next actions. Sugar exposes a REST API on every deployment at https://<site_url>/rest/v{version}/ (v10 through v11_20), authenticated with two-legged OAuth 2.0 and returning JSON. The API covers CRM modules (Accounts, Contacts, Leads, Opportunities, Cases and more) with offset pagination, a /{module}/filter query surface, and role-based access control. Official client libraries include the JavaScript Ventana connector and a PHP REST SDK.
image: https://www.sugarcrm.com/wp-content/uploads/2021/05/sugarcrm-facebook-card.png
layout: provider
modified: '2026-07-21'
name: SugarCRM
nav: Providers
network: true
overview: 'SugarCRM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, CRM, Sales, and Marketing.


  SugarCRM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 35.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sugarcrm Authentication
  slug: sugarcrm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sugarcrm Domain Security
  slug: sugarcrm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sugarcrm Trust Center
  slug: sugarcrm-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type II, CSA STAR, EcoVadis
slug: sugarcrm
tags:
- Company
- Saas
- CRM
- Sales
- Marketing
- Customer Service
- Sales Automation
- REST API
website: https://www.sugarcrm.com/
---
