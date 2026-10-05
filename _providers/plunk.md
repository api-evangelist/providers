---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Plunk Agentic Access
  operation_count: 14
  slug: plunk-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 2
apis:
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Create and send marketing campaigns.
  name: Plunk Campaigns API
  phrasing_intents:
  - id: listCampaigns
    intent: List email campaigns
    question: Which email campaigns do I have in Plunk right now?
  - id: createCampaign
    intent: Create a new email campaign draft
    question: How do I set up a new marketing email campaign?
  - id: updateCampaign
    intent: Edit a draft campaign
    question: Can I change the subject line of a campaign that's still a draft?
  - id: deleteCampaign
    intent: Delete a campaign
    question: Can I permanently remove a campaign I no longer need?
  - id: sendCampaign
    intent: Send or schedule a campaign now or later
    question: How do I schedule a campaign to go out at a specific date and time?
  - id: postCampaignsSend
    intent: Send a campaign live or as a test, with delay
    question: Can I do a test send of a campaign before sending it for real?
  phrasing_ops: 6
  slug: plunk-campaigns-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Manage contacts and their subscription state.
  name: Plunk Contacts API
  phrasing_intents:
  - id: listContacts
    intent: List contacts
    question: Which contacts are on my Plunk mailing list?
  - id: createContact
    intent: Create or upsert a contact by email
    question: How do I add a new contact to my list?
  - id: updateContact
    intent: Update a contact by id in the request body
    question: Is there an update endpoint where the contact id goes in the body rather than the URL?
  - id: deleteContact
    intent: Delete a contact by id in the request body
    question: Can I delete a contact by sending its id in the request body?
  - id: getContact
    intent: Get a single contact
    question: How do I look up one contact's details by their id?
  - id: patchContactsById
    intent: Patch a contact's email, subscription or data
    question: Can I change a contact's email address?
  - id: deleteContactsById
    intent: Permanently delete a contact by URL id
    question: How do I permanently remove a contact when I have its id for the URL path?
  - id: getContactCount
    intent: Count all contacts
    question: How many contacts are in my project in total?
  phrasing_ops: 10
  slug: plunk-contacts-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Track contact events that drive automations.
  name: Plunk Events API
  phrasing_intents:
  - id: trackEvent
    intent: Track a named event for a contact
    question: How do I record that a user signed up so my Plunk automations fire?
  phrasing_ops: 1
  slug: plunk-events-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Send transactional email.
  name: Plunk Transactional API
  phrasing_intents:
  - id: sendEmail
    intent: Send a transactional email
    question: How do I send a one-off transactional email with Plunk?
  phrasing_ops: 1
  slug: plunk-transactional-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Public API endpoints for sending emails and tracking events
  name: Plunk Public API
  phrasing_intents:
  - id: sendEmail
    intent: Send a transactional email
    question: How do I send a password reset email through Plunk?
  - id: trackEvent
    intent: Track an event for a contact
    question: How do I log a custom event like a purchase against a contact?
  - id: verifyEmail
    intent: Verify an email address
    question: Can I check whether an email address is valid before I add it?
  phrasing_ops: 3
  slug: plunk-public-api-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Audience segmentation
  name: Plunk Segments API
  phrasing_intents:
  - id: listSegments
    intent: List audience segments
    question: Which audience segments have I set up in Plunk?
  - id: createSegment
    intent: Create an audience segment
    question: How do I create a segment that updates automatically as contact data changes?
  phrasing_ops: 2
  slug: plunk-segments-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Email template management
  name: Plunk Templates API
  phrasing_intents:
  - id: listTemplates
    intent: List email templates
    question: Which email templates do I have in Plunk?
  - id: createTemplate
    intent: Create an email template
    question: How do I save a reusable email template with variable placeholders?
  phrasing_ops: 2
  slug: plunk-templates-api
artifact_total: 20
asyncapis:
- description: ''
  name: Plunk Webhooks
  slug: plunk-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plunk Campaigns API
  slug: open-plunk-campaigns-api
- collection_type: open
  name: Plunk Campaigns Contacts API
  slug: open-plunk-contacts-api
- collection_type: open
  name: Plunk Campaigns Events API
  slug: open-plunk-events-api
- collection_type: open
  name: Plunk Campaigns Transactional API
  slug: open-plunk-transactional-api
- collection_type: open
  name: Plunk API
  slug: open-plunk
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/capabilities/plunk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/plunk-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/useplunk/plunk/blob/next/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/agentic-access/plunk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plunk-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/security/plunk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plunk-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/authentication/plunk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plunk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useplunk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useplunk
- group: company
  title: ''
  type: Website
  url: https://www.useplunk.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useplunk.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/plans/plunk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plunk-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/rate-limits/plunk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plunk-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/finops/plunk-finops.yml
  title: ''
  type: FinOps
  url: finops/plunk-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/packages/plunk-packages.yml
  title: ''
  type: Packages
  url: packages/plunk-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/packages/plunk-packages.yml
  title: ''
  type: SDKs
  url: packages/plunk-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/llms/plunk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plunk-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/overlays/plunk-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/plunk-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/conventions/plunk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plunk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/conventions/plunk-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/plunk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/errors/plunk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plunk-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/lifecycle/plunk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plunk-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useplunk.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/changelog/plunk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plunk-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/data-model/plunk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plunk-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/asyncapi/plunk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/plunk-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/conformance/plunk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plunk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.useplunk.com/dpa
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.useplunk.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useplunk.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useplunk.com
- group: operate
  title: ''
  type: Support
  url: https://www.useplunk.com/discord
- group: commercial
  title: ''
  type: Pricing
  url: https://www.useplunk.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://next-app.useplunk.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://next-app.useplunk.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.useplunk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.useplunk.com/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/useplunk/plunk
created: '2026-06-20'
description: Plunk is an open-source (AGPL-3.0) email platform for developers that unifies transactional email, marketing campaigns, contact segmentation and event-driven workflow automation behind a single REST API. It publishes its own OpenAPI 3.1.0 at docs.useplunk.com/openapi.json, declaring next-api.useplunk.com as the production base URL, and authenticates with a two-class Bearer API key where the prefix decides capability — sk_ for every endpoint and pk_ for the client-safe /v1/track tracking call. The API supports Idempotency-Key on both public write endpoints, cursor pagination, a structured error envelope carrying machine codes plus remediation hints, and a documented webhook event catalogue delivered as workflow steps. Every documentation page is also served as Markdown. The entire stack self-hosts with Docker Compose for full data ownership and no per-email costs.
finops:
- name: Plunk Finops
  service_category: Email and Messaging
  slug: plunk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plunk.png
layout: provider
modified: '2026-08-13'
name: Plunk
nav: Providers
network: true
overview: 'Plunk publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, Events API, and 4 more. Tagged areas include Email, Transactional Email, Marketing, Automation, and Open Source.


  The Plunk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plunk''s developer surface includes authentication, documentation, changelog, API reference, getting-started guide, support, pricing, and 30 more developer resources.'
plans:
- name: Plunk Plans Pricing
  plan_count: 3
  slug: plunk-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Plunk Rate Limits
  slug: plunk-rate-limits
score:
  band: exemplar
  composite: 75.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 64.2
    developer_ergonomics: 64.9
    discoverability: 73.2
    operational_transparency: 73.7
  previous_composite: 74.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 72.2
screenshot: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/screenshots/plunk-2026-06-20T191814.png
security:
- kind: authentication
  name: Plunk Authentication
  slug: plunk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plunk Domain Security
  slug: plunk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plunk
tags:
- Email
- Transactional Email
- Marketing
- Automation
- Open Source
- Software-as-a-Service
- Email API
- Webhook
- Segmentation
- Workflow Automation
- Self-Hosted
- Developer Tools
website: https://www.useplunk.com
---
