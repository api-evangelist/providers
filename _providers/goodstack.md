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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 79.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Goodstack Agentic Access
  operation_count: 62
  slug: goodstack-agentic-access
  summary_line: 62 operations · 28 acting
api_count: 21
apis:
- description: The Activities API from Goodstack — 2 operation(s) for activities.
  name: Goodstack Activities API
  slug: goodstack-activities-api
- description: 'Agent verification is a one-off check. It is used to confirm that: 1. The person applying is who they say they are. 2. They represent the nonprofit. They are not editable once created.'
  name: Goodstack Agent Verifications API
  slug: goodstack-agent-verifications-api
- description: Categories represent collections of Organisations, which can be used to group and filter Organisations.
  name: Goodstack Categories API
  slug: goodstack-categories-api
- description: The Countries API from Goodstack — 1 operation(s) for countries.
  name: Goodstack Countries API
  slug: goodstack-countries-api
- description: The Donation Sessions API from Goodstack — 2 operation(s) for donation sessions.
  name: Goodstack Donation Sessions API
  slug: goodstack-donation-sessions-api
- description: A Donation object tracks the lifecycle of a Donation from creation and payment to disbursement to the nonprofit. Donations can be created during a Donation Session by the Hosted Donation Gateway or cr
  name: Goodstack Donations API
  slug: goodstack-donations-api
- description: The Eligibility Subscriptions API from Goodstack — 3 operation(s) for eligibility subscriptions.
  name: Goodstack Eligibility Subscriptions API
  slug: goodstack-eligibility-subscriptions-api
- description: The Gift Aid API from Goodstack — 2 operation(s) for gift aid.
  name: Goodstack Gift Aid API
  slug: goodstack-gift-aid-api
- description: The Monitoring Subscriptions API from Goodstack — 3 operation(s) for monitoring subscriptions.
  name: Goodstack Monitoring Subscriptions API
  slug: goodstack-monitoring-subscriptions-api
- description: The Org name search API from Goodstack — 1 operation(s) for org name search.
  name: Goodstack Org name search API
  slug: goodstack-org-name-search-api
- description: The Organisation API from Goodstack — 1 operation(s) for organisation.
  name: Goodstack Organisation API
  slug: goodstack-organisation-api
- description: Nonprofits are represented by the Organisation object. You can retrieve and query for Organisations.
  name: Goodstack Organisations API
  slug: goodstack-organisations-api
- description: The Registries API from Goodstack — 2 operation(s) for registries.
  name: Goodstack Registries API
  slug: goodstack-registries-api
- description: The User object represents a user of your application. It can be used to track Donations that belong to that user.
  name: Goodstack Users API
  slug: goodstack-users-api
- description: The Validation Invites API from Goodstack — 1 operation(s) for validation invites.
  name: Goodstack Validation Invites API
  slug: goodstack-validation-invites-api
- description: The Validation Request Documents API from Goodstack — 1 operation(s) for validation request documents.
  name: Goodstack Validation Request Documents API
  slug: goodstack-validation-request-documents-api
- description: If you want to know if a nonprofit exists in an official registry, create a Validation Request and we will check it for you. Documentary evidence can be attached to a Validation Request. When a Valida
  name: Goodstack Validation Requests API
  slug: goodstack-validation-requests-api
- description: The Validation Submission Configuration API from Goodstack — 2 operation(s) for validation submission configuration.
  name: Goodstack Validation Submission Configuration API
  slug: goodstack-validation-submission-configuration-api
- description: The Validation Submission Documents API from Goodstack — 2 operation(s) for validation submission documents.
  name: Goodstack Validation Submission Documents API
  slug: goodstack-validation-submission-documents-api
- description: The Validation Submissions API from Goodstack — 2 operation(s) for validation submissions.
  name: Goodstack Validation Submissions API
  slug: goodstack-validation-submissions-api
- description: The Webhook Subscriptions API from Goodstack — 2 operation(s) for webhook subscriptions.
  name: Goodstack Webhook Subscriptions API
  slug: goodstack-webhook-subscriptions-api
artifact_total: 26
asyncapis:
- description: ''
  name: Goodstack Webhooks
  slug: goodstack-webhooks
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goodstack-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goodstack-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/goodstack-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goodstack-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/goodstack-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goodstack-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goodstack-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/goodstack-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goodstack-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goodstack-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goodstack-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/goodstack-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goodstack-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goodstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodstack-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.goodstack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goodstack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.goodstack.io/docs/api/goodstack-services
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.goodstack.io/docs/guides
- group: operate
  title: ''
  type: Support
  url: https://goodstack.io/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://goodstack.org/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://goodstack.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://goodstack.io/demo-request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goodstack.io/legal/standard-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goodstack.io/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://goodstack.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.goodstack.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.goodstack.io/
created: '2026-07-17'
description: Goodstack (formerly Percent) is an impact platform whose REST API lets businesses build charitable giving, nonprofit verification, and fund disbursement into their own products. The Goodstack Services API covers monetary donations (direct and via a hosted donation gateway), a global registry of verified nonprofit and educational organisations, organisation name search, eligibility and monitoring subscriptions, agent verifications, validation requests and submissions, Gift Aid declarations, categories, and webhook subscriptions. Goodstack handles the vetting, validation, and timely disbursement of donations to good causes across multiple countries and currencies. The API is organised around REST, uses API-key authentication (publishable pk_ and secret sk_ keys), returns JSON with standard HTTP status codes, and offers a sandbox environment.
image: https://goodstack.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: goodstack-mcp.yml
  slug: goodstack-mcpyml
modified: '2026-07-19'
name: Goodstack
nav: Providers
network: true
overview: 'Goodstack publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Agent Verifications API, Categories API, and 18 more. Tagged areas include Company, Nonprofits, Donations, Charitable Giving, and Fundraising.


  The Goodstack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goodstack''s developer surface includes sandbox, changelog, authentication, documentation, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 57.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.5
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 57.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goodstack/refs/heads/main/screenshots/goodstack-2026-07-25T220057.png
security:
- kind: authentication
  name: Goodstack Authentication
  slug: goodstack-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Goodstack Domain Security
  slug: goodstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: goodstack
tags:
- Company
- Nonprofits
- Donations
- Charitable Giving
- Fundraising
- Verification
- Compliance
- Payments
- Disbursements
- Social Impact
website: https://docs.goodstack.io/
---
