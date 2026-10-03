---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Stannp Agentic Access
  operation_count: 32
  slug: stannp-agentic-access
  summary_line: 32 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Account balance and user information
  name: Stannp Account API
  phrasing_intents:
  - id: getAccountBalance
    intent: Check the account balance
    question: How much credit is left on my Stannp account?
  - id: topUpBalance
    intent: Add funds to the account balance
    question: Can I prepay credit onto my account so mailings draw from a balance?
  - id: getCurrentUser
    intent: Look up the signed-in user
    question: Which user is my API key authenticated as?
  phrasing_ops: 3
  slug: stannp-account-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Manage batch direct mail campaigns
  name: Stannp Campaigns API
  phrasing_intents:
  - id: listCampaigns
    intent: List direct mail campaigns
    question: What mail campaigns have I created so far?
  - id: getCampaign
    intent: Look up a campaign
    question: What are the settings and status of one particular campaign?
  - id: createCampaign
    intent: Create a direct mail campaign for a group
    question: How do I set up a bulk mailing to everyone in one of my recipient groups?
  - id: getCampaignSample
    intent: Generate a sample PDF of a campaign
    question: Can I see a proof of what a campaign's mailpiece will look like before approving it?
  - id: approveCampaign
    intent: Approve a campaign for booking
    question: What do I need to do before a campaign can be scheduled?
  - id: getCampaignCost
    intent: Calculate what a campaign will cost
    question: How much will it cost to send a campaign, including VAT?
  - id: getCampaignAvailableDates
    intent: Find available campaign dispatch dates
    question: Which dates can my campaign be sent out on?
  - id: bookCampaign
    intent: Schedule a campaign for dispatch
    question: How do I schedule an approved campaign to go out on a specific day?
  phrasing_ops: 9
  slug: stannp-campaigns-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Record recipient engagement and conversion events
  name: Stannp Events API
  phrasing_intents:
  - id: createRecipientEvent
    intent: Record an engagement event for a recipient
    question: How do I log that a mail recipient made a purchase after receiving a mailpiece?
  phrasing_ops: 1
  slug: stannp-events-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Manage recipient groups
  name: Stannp Groups API
  phrasing_intents:
  - id: listGroups
    intent: List recipient groups
    question: What mailing groups have I set up?
  - id: createGroup
    intent: Create a recipient group
    question: How do I set up a new mailing list group to hold recipients?
  - id: addRecipientsToGroup
    intent: Add existing recipients to a group
    question: Can I put recipients I've already created into another mailing group?
  - id: removeRecipientsFromGroup
    intent: Remove specific recipients from a group
    question: How can I take a few people out of a mailing group without deleting them?
  - id: purgeGroup
    intent: Empty all recipients out of a group
    question: How do I clear every recipient out of a group but keep the group itself?
  - id: recalculateGroup
    intent: Recalculate a group's counts and validity
    question: Why does my group's recipient count look out of date, and can I refresh it?
  - id: deleteGroup
    intent: Delete a recipient group
    question: How do I delete a mailing group I no longer need?
  phrasing_ops: 7
  slug: stannp-groups-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Create, post, retrieve, and cancel letter mailpieces
  name: Stannp Letters API
  phrasing_intents:
  - id: createLetter
    intent: Send a letter from a template or HTML
    question: How do I mail a single letter built from one of my saved templates?
  - id: postLetter
    intent: Mail a pre-merged PDF letter
    question: Can I upload a finished PDF with the address already on it and have it posted?
  - id: getLetter
    intent: Look up a letter mailpiece
    question: What's the current status of a letter I sent?
  - id: cancelLetter
    intent: Cancel a letter before dispatch
    question: Can I stop a letter from going out if it hasn't been dispatched yet?
  phrasing_ops: 4
  slug: stannp-letters-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Create, retrieve, and cancel postcard mailpieces
  name: Stannp Postcards API
  phrasing_intents:
  - id: createPostcard
    intent: Send a postcard
    question: How do I mail a single postcard with my own front and back artwork?
  - id: getPostcard
    intent: Look up a postcard mailpiece
    question: What's the status of a postcard I already sent?
  - id: cancelPostcard
    intent: Cancel a postcard before dispatch
    question: Can I cancel a postcard that hasn't been dispatched yet?
  phrasing_ops: 3
  slug: stannp-postcards-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Manage individual recipients and bulk imports
  name: Stannp Recipients API
  phrasing_intents:
  - id: listRecipients
    intent: List recipients
    question: Who is on my mailing list?
  - id: getRecipient
    intent: Look up a single recipient
    question: What address do I have on file for a specific recipient?
  - id: createRecipient
    intent: Add a recipient address
    question: How do I add one new person's postal address to my mailing list?
  - id: deleteRecipient
    intent: Delete a recipient
    question: How do I permanently remove someone's address record?
  - id: importRecipients
    intent: Bulk import recipients from a spreadsheet
    question: Can I upload a CSV or Excel file of addresses instead of adding them one by one?
  phrasing_ops: 5
  slug: stannp-recipients-api
artifact_total: 32
asyncapis:
- description: ''
  name: Stannp Webhooks
  slug: stannp-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stannp Direct Mail Account API
  slug: open-stannp-account-api
- collection_type: open
  name: Stannp Direct Mail Account Campaigns API
  slug: open-stannp-campaigns-api
- collection_type: open
  name: Stannp Direct Mail Account Events API
  slug: open-stannp-events-api
- collection_type: open
  name: Stannp Direct Mail Account Groups API
  slug: open-stannp-groups-api
- collection_type: open
  name: Stannp Direct Mail Account Letters API
  slug: open-stannp-letters-api
- collection_type: open
  name: Stannp Direct Mail Account Postcards API
  slug: open-stannp-postcards-api
- collection_type: open
  name: Stannp Direct Mail Account Recipients API
  slug: open-stannp-recipients-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/capabilities/stannp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stannp-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/agentic-access/stannp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stannp-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/security/stannp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stannp-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.stannp.com/us/accreditations
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/security/stannp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stannp-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/security/stannp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stannp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.stannp.com/us/trust
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/authentication/stannp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stannp-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/conventions/stannp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stannp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/conventions/stannp-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/stannp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/errors/stannp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stannp-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/data-model/stannp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stannp-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/conformance/stannp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stannp-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/lifecycle/stannp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stannp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stannp.com/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/sandbox/stannp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stannp-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/asyncapi/stannp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/stannp-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/packages/stannp-packages.yml
  title: ''
  type: Packages
  url: packages/stannp-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/packages/stannp-packages.yml
  title: ''
  type: SDKs
  url: packages/stannp-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/mcp/stannp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/stannp-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/llms/stannp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stannp-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.stannp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.stannp.com/us/developer-tools
- group: docs
  title: ''
  type: Documentation
  url: https://www.stannp.com/us/direct-mail-api/guide
- group: docs
  title: ''
  type: APIReference
  url: https://www.stannp.com/us/direct-mail-api/postcards
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stannp.com/us/direct-mail-api/guide#introduction
- group: operate
  title: ''
  type: Support
  url: https://www.stannp.com/us/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.stannp.com/us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stannp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stannp-com-postcard-bulk-mailer
- group: other
  title: ''
  type: X
  url: https://twitter.com/stannpdm
- group: company
  title: ''
  type: Blog
  url: https://go.stannp.com/en-us/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stannp.com/us/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/plans/stannp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stannp-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app-us1.stannp.com/register
- group: start
  title: ''
  type: Login
  url: https://app-us1.stannp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stannp.com/us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stannp.com/us/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/rate-limits/stannp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stannp-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/finops/stannp-finops.yml
  title: ''
  type: FinOps
  url: finops/stannp-finops.yml
created: '2026-06-12'
description: Stannp is a direct mail platform that enables businesses to send physical postcards and letters programmatically via a REST API. The platform lets developers create campaigns, upload recipient lists, trigger individual mail pieces in real time, and track print and delivery status through webhooks and event endpoints. Authentication uses API key-based HTTP Basic Auth over HTTPS, and the API follows a simple JSON response envelope with success/data or success/error fields. Stannp serves businesses across the UK, US, and Canada with per-item pricing for letters and postcards at scale, and supports no-code integrations through Zapier and Make as well as official SDKs for PHP, Go, and C#.
examples:
- key_count: 8
  name: Create Postcard Request
  slug: create-postcard-request
- key_count: 2
  name: Create Postcard Response
  slug: create-postcard-response
- key_count: 5
  name: Webhook Payload
  slug: webhook-payload
finops:
- name: Stannp Finops
  service_category: ''
  slug: stannp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stannp.png
json_schemas:
- name: Campaign
  property_count: 8
  slug: campaign
- name: Mailpiece
  property_count: 8
  slug: mailpiece
- name: Recipient
  property_count: 22
  slug: recipient
jsonld:
- class_count: 45
  name: Stannp Context
  property_count: 9
  slug: stannp-context
layout: provider
modified: '2026-08-13'
name: Stannp
nav: Providers
network: true
overview: 'Stannp publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Campaigns API, Events API, and 4 more. Tagged areas include Direct Mail, Postcards, Letters, Print, and Physical Mail.


  The Stannp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Stannp''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 34 more developer resources.'
plans:
- name: Stannp Plans Pricing
  plan_count: 5
  slug: stannp-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Stannp Rate Limits
  slug: stannp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stannp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stannp-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 76.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 88.8
    catalog_earned_first_party: 24.0
    catalog_gap: 26.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 41.7
    contract_quality: 69.5
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 68.4
  previous_composite: 76.1
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
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/screenshots/stannp-2026-06-20T194506.png
security:
- kind: authentication
  name: Stannp Authentication
  slug: stannp-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Stannp Domain Security
  slug: stannp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stannp Vulnerability Disclosure
  slug: stannp-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Stannp Trust Center
  slug: stannp-trust-center
  summary_line: HIPAA, ISO 27001, ISO 9001, GDPR, ICO registration ZA134992 (UK Data Processor), USPS CASS certification, Royal Mail PAF accreditation, Royal Mail Mail Made Easy partner, SecurityScorecard A rating
slug: stannp
tags:
- Direct Mail
- Postcards
- Letters
- Print
- Physical Mail
- Marketing Automation
- Campaigns
- Address Verification
- SMS
- Webhook
- Mailing Lists
- Fulfillment
website: https://www.stannp.com
---
