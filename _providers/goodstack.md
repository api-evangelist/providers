---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Goodstack Agentic Access
  operation_count: 62
  slug: goodstack-agentic-access
  summary_line: 62 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Activities API from Goodstack — 2 operation(s) for activities.
  name: Goodstack Activities API
  slug: goodstack-activities-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: 'Agent verification is a one-off check. It is used to confirm that: 1. The person applying is who they say they are. 2. They represent the nonprofit. They are not editable once created.'
  name: Goodstack Agent Verifications API
  slug: goodstack-agent-verifications-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: Categories represent collections of Organisations, which can be used to group and filter Organisations.
  name: Goodstack Categories API
  slug: goodstack-categories-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Countries API from Goodstack — 1 operation(s) for countries.
  name: Goodstack Countries API
  slug: goodstack-countries-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Donation Sessions API from Goodstack — 2 operation(s) for donation sessions.
  name: Goodstack Donation Sessions API
  slug: goodstack-donation-sessions-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: A Donation object tracks the lifecycle of a Donation from creation and payment to disbursement to the nonprofit. Donations can be created during a Donation Session by the Hosted Donation Gateway or cr
  name: Goodstack Donations API
  slug: goodstack-donations-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Eligibility Subscriptions API from Goodstack — 3 operation(s) for eligibility subscriptions.
  name: Goodstack Eligibility Subscriptions API
  slug: goodstack-eligibility-subscriptions-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Gift Aid API from Goodstack — 2 operation(s) for gift aid.
  name: Goodstack Gift Aid API
  slug: goodstack-gift-aid-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Monitoring Subscriptions API from Goodstack — 3 operation(s) for monitoring subscriptions.
  name: Goodstack Monitoring Subscriptions API
  slug: goodstack-monitoring-subscriptions-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Org name search API from Goodstack — 1 operation(s) for org name search.
  name: Goodstack Org name search API
  slug: goodstack-org-name-search-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Organisation API from Goodstack — 1 operation(s) for organisation.
  name: Goodstack Organisation API
  slug: goodstack-organisation-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: Nonprofits are represented by the Organisation object. You can retrieve and query for Organisations.
  name: Goodstack Organisations API
  slug: goodstack-organisations-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Registries API from Goodstack — 2 operation(s) for registries.
  name: Goodstack Registries API
  slug: goodstack-registries-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The User object represents a user of your application. It can be used to track Donations that belong to that user.
  name: Goodstack Users API
  slug: goodstack-users-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Validation Invites API from Goodstack — 1 operation(s) for validation invites.
  name: Goodstack Validation Invites API
  slug: goodstack-validation-invites-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Validation Request Documents API from Goodstack — 1 operation(s) for validation request documents.
  name: Goodstack Validation Request Documents API
  slug: goodstack-validation-request-documents-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: If you want to know if a nonprofit exists in an official registry, create a Validation Request and we will check it for you. Documentary evidence can be attached to a Validation Request. When a Valida
  name: Goodstack Validation Requests API
  slug: goodstack-validation-requests-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Validation Submission Configuration API from Goodstack — 2 operation(s) for validation submission configuration.
  name: Goodstack Validation Submission Configuration API
  slug: goodstack-validation-submission-configuration-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Validation Submission Documents API from Goodstack — 2 operation(s) for validation submission documents.
  name: Goodstack Validation Submission Documents API
  slug: goodstack-validation-submission-documents-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Validation Submissions API from Goodstack — 2 operation(s) for validation submissions.
  name: Goodstack Validation Submissions API
  slug: goodstack-validation-submissions-api
- baseURL: https://api.goodstack.io/v1
  baseurl_source: declared
  description: The Webhook Subscriptions API from Goodstack — 2 operation(s) for webhook subscriptions.
  name: Goodstack Webhook Subscriptions API
  slug: goodstack-webhook-subscriptions-api
artifact_total: 47
asyncapis:
- description: ''
  name: Goodstack Webhooks
  slug: goodstack-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Goodstack Services Activities API
  slug: open-goodstack-activities-api
- collection_type: open
  name: Goodstack Services Activities Agent Verifications API
  slug: open-goodstack-agent-verifications-api
- collection_type: open
  name: Goodstack Services Activities Categories API
  slug: open-goodstack-categories-api
- collection_type: open
  name: Goodstack Services Activities Countries API
  slug: open-goodstack-countries-api
- collection_type: open
  name: Goodstack Services Activities Donation Sessions API
  slug: open-goodstack-donation-sessions-api
- collection_type: open
  name: Goodstack Services Activities Donations API
  slug: open-goodstack-donations-api
- collection_type: open
  name: Goodstack Services Activities Eligibility Subscriptions API
  slug: open-goodstack-eligibility-subscriptions-api
- collection_type: open
  name: Goodstack Services Activities Gift Aid API
  slug: open-goodstack-gift-aid-api
- collection_type: open
  name: Goodstack Services Activities Monitoring Subscriptions API
  slug: open-goodstack-monitoring-subscriptions-api
- collection_type: open
  name: Goodstack Services Activities Org name search API
  slug: open-goodstack-org-name-search-api
- collection_type: open
  name: Goodstack Services Activities Organisation API
  slug: open-goodstack-organisation-api
- collection_type: open
  name: Goodstack Services Activities Organisations API
  slug: open-goodstack-organisations-api
- collection_type: open
  name: Goodstack Services Activities Registries API
  slug: open-goodstack-registries-api
- collection_type: open
  name: Goodstack Services Activities Users API
  slug: open-goodstack-users-api
- collection_type: open
  name: Goodstack Services Activities Validation Invites API
  slug: open-goodstack-validation-invites-api
- collection_type: open
  name: Goodstack Services Activities Validation Request Documents API
  slug: open-goodstack-validation-request-documents-api
- collection_type: open
  name: Goodstack Services Activities Validation Requests API
  slug: open-goodstack-validation-requests-api
- collection_type: open
  name: Goodstack Services Activities Validation Submission Configuration API
  slug: open-goodstack-validation-submission-configuration-api
- collection_type: open
  name: Goodstack Services Activities Validation Submission Documents API
  slug: open-goodstack-validation-submission-documents-api
- collection_type: open
  name: Goodstack Services Activities Validation Submissions API
  slug: open-goodstack-validation-submissions-api
- collection_type: open
  name: Goodstack Services Activities Webhook Subscriptions API
  slug: open-goodstack-webhook-subscriptions-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Goodstack
nav: Providers
network: true
overview: 'Goodstack publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Agent Verifications API, Categories API, and 18 more. Tagged areas include Company, Non-Profit, Donations, Charitable Giving, and Fundraising.


  The Goodstack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goodstack''s developer surface includes sandbox, changelog, authentication, documentation, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 61.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Non-Profit
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
