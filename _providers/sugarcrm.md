---
access_model:
  confidence: high
  label: Published seat pricing, 15-user minimum, annual billing
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.sugarai.com/pricing
  - plans/sugarcrm-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Sugar REST API is hosted on each Sugar deployment at https://<site_url>/rest/v{version}/ (v10 through v11.27). SugarCloud instances are hosted on Sugar's own sugarondemand.com domain, so a cloud t
  name: Sugar REST API
  slug: sugar-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Sugarcrm Webhooks
  slug: sugarcrm-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.sugarai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.sugarai.com/documentation/sugar_developer/
- group: docs
  title: ''
  type: Documentation
  url: https://support.sugarai.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://support.sugarai.com/documentation/sugar_developer/sugar_developer_guide_26.1/integration/web_services/rest_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sugarai.com/documentation/sugar_developer/sugar_developer_guide_26.1/
- group: operate
  title: ''
  type: Support
  url: https://sugarclub.sugarai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sugarai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sugarcrm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sugarai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.sugarondemand.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sugarai.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sugarai.com/legal/privacy-policy
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
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sugarcrm-changelog.yml
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
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sugarcrm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/sugarcrm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sugarcrm-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/sugarcrm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sugarcrm-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sugarcrm-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sugarcrm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sugarcrm-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sugarcrm-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sugarcrm-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sugarcrm-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sugarcrm-llms.txt
created: '2026-07-17'
description: SugarCRM — rebranded as SugarAI in April 2026, with www.sugarcrm.com now redirecting to www.sugarai.com — is a B2B sales CRM platform serving 4,000+ customers and over one million users across 120+ countries. Its product suite spans Sugar Sell (sales automation), Sugar Serve (customer service), Sugar Market (marketing automation), and sales-i (sales intelligence from ERP data), with an emphasis on domain-specific AI that surfaces opportunities and recommends next actions and native integration with 180+ ERP systems. Sugar exposes a REST API on every deployment at https://<site_url>/rest/v{version}/ (v10 through v11.27 as of the 26.1 Developer Guide), authenticated with two-legged OAuth 2.0 and returning JSON. The API covers CRM modules (Accounts, Contacts, Leads, Opportunities, Cases and more) with offset pagination, a /{module}/filter query surface, and role-based access control. Outbound events are delivered as Web Logic Hooks through the instance job queue. Official client
  libraries include the JavaScript Ventana connector and the PHP REST SDK. There is no public OpenAPI — the endpoint reference is served per instance at /rest/v{version}/help.
image: https://www.sugarcrm.com/wp-content/uploads/2021/05/sugarcrm-facebook-card.png
layout: provider
modified: '2026-08-13'
name: SugarCRM
nav: Providers
network: true
overview: 'SugarCRM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, CRM, Sales, and Marketing.


  The SugarCRM catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SugarCRM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Sugarcrm Plans Pricing
  plan_count: 3
  slug: sugarcrm-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Sugarcrm Rate Limits
  slug: sugarcrm-rate-limits
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 62.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sugarcrm/refs/heads/main/screenshots/sugarcrm-2026-08-17T080426.png
security:
- kind: authentication
  name: Sugarcrm Authentication
  slug: sugarcrm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sugarcrm Domain Security
  slug: sugarcrm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sugarcrm Vulnerability Disclosure
  slug: sugarcrm-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
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
- Webhook
- Sales Intelligence
website: https://www.sugarai.com/
---
