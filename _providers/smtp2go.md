---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 68
  human_in_the_loop: 0
  name: Smtp2Go Agentic Access
  operation_count: 73
  slug: smtp2go-agentic-access
  summary_line: 73 operations · 68 acting
api_count: 1
apis:
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Email activity search
  name: SMTP2GO Activity API
  phrasing_intents:
  - id: search-activity
    intent: Search email activity events
    question: Which recipients opened or unsubscribed from my emails this week?
  phrasing_ops: 1
  slug: smtp2go-activity-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: API key management
  name: SMTP2GO API Keys API
  phrasing_intents:
  - id: add-api-key
    intent: Create a new API key
    question: How do I create a new SMTP2GO API key?
  - id: edit-api-key
    intent: Replace an API key's settings
    question: How do I update all the settings of an existing API key at once?
  - id: patch-api-key
    intent: Partially update an API key
    question: Can I change just one setting on an API key without resending everything?
  - id: view-api-key-permissions
    intent: List endpoints the current key can call
    question: Which endpoints is the API key I'm using allowed to call?
  - id: remove-api-key
    intent: Delete an API key
    question: How do I revoke an API key I no longer need?
  - id: view-api-keys
    intent: List API keys on the account
    question: What API keys exist on my account?
  phrasing_ops: 6
  slug: smtp2go-api-keys-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Send and receive SMS messages
  name: SMTP2GO SMS API
  phrasing_intents:
  - id: send-sms
    intent: Send an SMS message
    question: How do I send a text message to a group of phone numbers?
  - id: sms-summary
    intent: Summarize SMS activity for a period
    question: How many SMS messages did we send last month?
  - id: view-received-sms
    intent: View received SMS messages
    question: What inbound text messages have we received?
  - id: view-sent-sms
    intent: View sent SMS messages
    question: Which outbound SMS messages have gone out recently?
  phrasing_ops: 4
  slug: smtp2go-sms-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: SMTP user account management
  name: SMTP2GO SMTP Users API
  phrasing_intents:
  - id: add-an-smtp-user
    intent: Create an SMTP user
    question: How do I create new SMTP credentials for an application?
  - id: edit-an-smtp-user
    intent: Replace an SMTP user's settings
    question: How do I do a full update of an SMTP user's settings?
  - id: patch-smtp-user
    intent: Partially update an SMTP user
    question: Can I change only one field on an SMTP user and leave the rest alone?
  - id: remove-an-smtp-user
    intent: Delete an SMTP user
    question: How do I delete SMTP credentials that are no longer used?
  - id: view-smtp-users
    intent: List SMTP users
    question: Which SMTP users exist on my account?
  phrasing_ops: 5
  slug: smtp2go-smtp-users-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Subaccount management
  name: SMTP2GO Subaccounts API
  phrasing_intents:
  - id: add-subaccount
    intent: Create a subaccount
    question: How do I create a subaccount for a client under my master account?
  - id: close-a-subaccount
    intent: Close a subaccount
    question: How do I shut down a client's subaccount?
  - id: update-a-subaccount
    intent: Update a subaccount's details
    question: How do I raise the sending limit on a subaccount?
  - id: reopen-a-closed-subaccount
    intent: Reopen a closed subaccount
    question: Can I reactivate a subaccount I closed earlier?
  - id: search-subaccounts
    intent: Search subaccounts
    question: Which subaccounts do I have, and which are closed?
  phrasing_ops: 5
  slug: smtp2go-subaccounts-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Suppression list management
  name: SMTP2GO Suppressions API
  phrasing_intents:
  - id: add-a-suppression
    intent: Suppress an email address or domain
    question: How do I stop all email going to a specific address?
  - id: remove-a-suppression
    intent: Lift a suppression
    question: How do I unblock an address that got suppressed after a bounce?
  - id: view-suppressions
    intent: List suppressed addresses and domains
    question: Which email addresses are on my suppression list?
  phrasing_ops: 3
  slug: smtp2go-suppressions-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Email template management
  name: SMTP2GO Templates API
  phrasing_intents:
  - id: add-an-email-template
    intent: Create an email template
    question: How do I create a reusable email template with variables?
  - id: remove-an-email-template
    intent: Delete an email template
    question: How do I delete an email template I don't use anymore?
  - id: update-an-email-template
    intent: Update an email template
    question: How do I change the subject line of an existing template?
  - id: search-email-templates
    intent: Search email templates
    question: Which email templates do I have?
  - id: view-template-details
    intent: Get one email template's details
    question: What does a specific template contain, including its HTML and variables?
  phrasing_ops: 5
  slug: smtp2go-templates-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Webhook configuration
  name: SMTP2GO Webhooks API
  phrasing_intents:
  - id: add-webhook
    intent: Create a webhook
    question: How do I get notified at my URL when emails bounce or are opened?
  - id: edit-webhook
    intent: Update a webhook
    question: How do I change the URL an existing webhook posts to?
  - id: remove-webhook
    intent: Delete a webhook
    question: How do I stop a webhook from sending events?
  - id: view-webhook
    intent: List configured webhooks
    question: Which webhooks are configured on my account?
  phrasing_ops: 4
  slug: smtp2go-webhooks-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage the allowed recipients list
  name: SMTP2GO ALLOWED RECIPIENTS API
  phrasing_intents:
  - id: add-allowed-recipients
    intent: Add addresses to the Allowed Recipients List
    question: How do I add a domain to my allowed recipients list?
  - id: remove-allowed-recipients
    intent: Remove addresses from the Allowed Recipients List
    question: How can I take a domain off my allowed recipients list?
  - id: update-allowed-recipients
    intent: Replace the Allowed Recipients List
    question: Can I overwrite my whole allowed recipients list with a new set of addresses?
  - id: view-allowed-recipients
    intent: View the Allowed Recipients List
    question: Which addresses and domains are currently on my allowed recipients list?
  phrasing_ops: 4
  slug: smtp2go-allowed-recipients-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage the allowed/restricted senders list
  name: SMTP2GO ALLOWED SENDERS API
  phrasing_intents:
  - id: add-allowed-senders
    intent: Add addresses to the allowed senders list
    question: How do I add a sender domain to my allowed or restricted senders list?
  - id: remove-allowed-senders
    intent: Remove addresses from the allowed senders list
    question: How can I take a sender address off my allowed senders list?
  - id: update-allowed-senders
    intent: Replace the senders list and its mode
    question: Can I switch my senders list between whitelist, blacklist and disabled mode?
  - id: view-allowed-senders
    intent: View the allowed senders list and mode
    question: Which senders are on my allowed senders list and what mode is it in?
  phrasing_ops: 4
  slug: smtp2go-allowed-senders-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: View dedicated IP addresses on the account
  name: SMTP2GO DEDICATED IPS API
  phrasing_intents:
  - id: view-dedicated-ips
    intent: List dedicated IP addresses
    question: Which dedicated IP addresses does my SMTP2GO account have?
  phrasing_ops: 1
  slug: smtp2go-dedicated-ips-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Search and retrieve archived email content
  name: SMTP2GO EMAIL ARCHIVE API
  phrasing_intents:
  - id: view-an-archived-email
    intent: Retrieve one archived email
    question: How do I pull up the full archived copy of a specific email?
  - id: search-archived-pages
    intent: Search the email archive
    question: Which archived emails did we send to a particular recipient last month?
  phrasing_ops: 2
  slug: smtp2go-email-archive-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Send standard, MIME and batch email; manage scheduled sends
  name: SMTP2GO EMAILS API
  phrasing_intents:
  - id: send-email-batch
    intent: Send a batch of emails
    question: Can I send many different emails in a single request?
  - id: send-mime-email
    intent: Send a pre-encoded MIME email
    question: How do I send an email I've already built as a raw MIME string?
  - id: remove-scheduled-email
    intent: Cancel a scheduled email
    question: How do I cancel an email that's scheduled but not yet sent?
  - id: search-scheduled-emails
    intent: Search scheduled emails
    question: Which emails do I have scheduled to go out later?
  - id: send-standard-email
    intent: Send an email
    question: How do I send a transactional email with SMTP2GO using JSON?
  phrasing_ops: 5
  slug: smtp2go-emails-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage IP-authenticated sending entries
  name: SMTP2GO IP AUTH API
  phrasing_intents:
  - id: patch-ip-auth
    intent: Partially update an IP Auth entry
    question: Can I change settings on an IP-authenticated sender without resending them all?
  - id: remove-ip-auth
    intent: Remove an IP Auth entry
    question: How do I stop an IP address from authenticating to send mail?
  - id: view-ip-auth
    intent: View IP Auth entries
    question: Which IP addresses are set up for IP authentication on my account?
  phrasing_ops: 3
  slug: smtp2go-ip-auth-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Add, verify and manage sender domains, tracking and return-path subdomains
  name: SMTP2GO SENDER DOMAINS API
  phrasing_intents:
  - id: add-sender-domain
    intent: Add a sender domain
    question: How do I add my domain so I can send email from it?
  - id: remove-sender-domain
    intent: Remove a sender domain
    question: How do I delete a sender domain I no longer use?
  - id: edit-return-path-domain
    intent: Change a domain's return-path subdomain
    question: How do I change where bounces are returned for my sender domain?
  - id: edit-subaccount-access
    intent: Share a sender domain with subaccounts
    question: Can my subaccounts send from a domain verified on the master account?
  - id: edit-tracking-domain
    intent: Change a domain's tracking subdomain
    question: How do I change the subdomain used to track opens and clicks?
  - id: verify-a-sender-domain
    intent: Verify a sender domain now
    question: How do I verify my sender domain without waiting for the periodic check?
  - id: view-sender-domains
    intent: List sender domains
    question: Which sender domains are on my account and are they verified?
  phrasing_ops: 7
  slug: smtp2go-sender-domains-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Verify individual From addresses
  name: SMTP2GO SINGLE SENDER EMAILS API
  phrasing_intents:
  - id: add-a-single-sender-email
    intent: Add a single sender email address
    question: How do I send from one email address without verifying a whole domain?
  - id: remove-a-single-sender-email
    intent: Remove a single sender email address
    question: How do I delete a single sender address from my account?
  - id: view-all-single-sender-emails
    intent: List single sender emails and status
    question: Which single sender addresses do I have and are they verified?
  phrasing_ops: 3
  slug: smtp2go-single-sender-emails-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Delivery, bounce, spam, unsubscribe and cycle statistics
  name: SMTP2GO STATISTICS API
  phrasing_intents:
  - id: email-bounces
    intent: Summarize bounces over the last 30 days
    question: How many of my emails bounced in the last 30 days?
  - id: email-cycle
    intent: View usage for the current billing cycle
    question: How many emails have I sent so far this billing cycle?
  - id: email-history
    intent: Report email activity by sender or domain
    question: Which sender addresses sent the most email last month?
  - id: email-spam
    intent: Summarize spam complaints
    question: How many spam complaints did we get in the last 30 days?
  - id: email-summary
    intent: Get a combined email statistics report
    question: Can I get bounces, spam, unsubscribes and cycle usage in one report?
  - id: email-unsubscribes
    intent: Summarize unsubscribes
    question: How many people unsubscribed in the last 30 days?
  phrasing_ops: 6
  slug: smtp2go-statistics-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage the account IP allow list for SMTP and API access
  name: SMTP2GO IP Allowlist API
  phrasing_intents:
  - id: ip-allowlist
    intent: Enable or disable an IP allow list
    question: How do I turn on IP allow listing for API access?
  - id: add-ip-allowlist
    intent: Add an IP to an allow list
    question: How do I add a new IP address to my allow list?
  - id: edit-ip-allowlist
    intent: Change an allow-listed IP address
    question: How do I change an IP address that's already on my allow list?
  - id: remove-ip-allowlist
    intent: Remove an IP from an allow list
    question: How do I remove an IP address from my allow list?
  - id: view-ip-allowlist
    intent: View an IP allow list and its status
    question: Which IP addresses are on my allow list, and is it enabled?
  phrasing_ops: 5
  slug: smtp2go-ip-allowlist-api
artifact_total: 48
asyncapis:
- description: ''
  name: Smtp2Go Webhooks
  slug: smtp2go-webhooks
collections:
- collection_type: open
  name: SMTP2GO Email Activity API
  slug: open-smtp2go-activity-api
- collection_type: open
  name: SMTP2GO Email Activity API Keys API
  slug: open-smtp2go-api-keys-api
- collection_type: open
  name: SMTP2GO Email Activity Domains API
  slug: open-smtp2go-domains-api
- collection_type: open
  name: SMTP2GO Activity Email API
  slug: open-smtp2go-email-api
- collection_type: open
  name: SMTP2GO Email Activity SMS API
  slug: open-smtp2go-sms-api
- collection_type: open
  name: SMTP2GO Email Activity SMTP Users API
  slug: open-smtp2go-smtp-users-api
- collection_type: open
  name: SMTP2GO Email Activity Stats API
  slug: open-smtp2go-stats-api
- collection_type: open
  name: SMTP2GO Email Activity Subaccounts API
  slug: open-smtp2go-subaccounts-api
- collection_type: open
  name: SMTP2GO Email Activity Suppressions API
  slug: open-smtp2go-suppressions-api
- collection_type: open
  name: SMTP2GO Email Activity Templates API
  slug: open-smtp2go-templates-api
- collection_type: open
  name: SMTP2GO Email Activity Webhooks API
  slug: open-smtp2go-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/smtp2go/capabilities/smtp2go-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smtp2go-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/smtp2go/agentic-access/smtp2go-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smtp2go-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/smtp2go/security/smtp2go-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smtp2go-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/smtp2go/authentication/smtp2go-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smtp2go-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smtp2go.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smtp2go.com/docs/introduction-guide
- group: docs
  title: ''
  type: APIReference
  url: https://developers.smtp2go.com/reference/general-api-resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/smtp2go-oss
- group: company
  title: ''
  type: Blog
  url: https://www.smtp2go.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smtp2go.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://smtp2gostatus.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smtp2go
- group: other
  title: ''
  type: X
  url: https://x.com/smtp2go
- group: operate
  title: ''
  type: Support
  url: https://support.smtp2go.com/
- group: commercial
  href: https://artifacts.apis.io/smtp2go/plans/smtp2go-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smtp2go-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smtp2go/rate-limits/smtp2go-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smtp2go-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/smtp2go/finops/smtp2go-finops.yml
  title: ''
  type: FinOps
  url: finops/smtp2go-finops.yml
- group: build
  href: https://artifacts.apis.io/smtp2go/packages/smtp2go-packages.yml
  title: ''
  type: Packages
  url: packages/smtp2go-packages.yml
- group: build
  href: https://artifacts.apis.io/smtp2go/packages/smtp2go-packages.yml
  title: ''
  type: SDKs
  url: packages/smtp2go-packages.yml
- group: agent
  href: https://artifacts.apis.io/smtp2go/mcp/smtp2go-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smtp2go-mcp.yml
- group: build
  href: https://artifacts.apis.io/smtp2go/mcp/smtp2go-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/smtp2go-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/smtp2go/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/smtp2go/llms/smtp2go-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smtp2go-llms.txt
- group: other
  href: https://artifacts.apis.io/smtp2go/overlays/smtp2go-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/smtp2go-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/smtp2go/conventions/smtp2go-conventions.yml
  title: ''
  type: Conventions
  url: conventions/smtp2go-conventions.yml
- group: design
  href: https://artifacts.apis.io/smtp2go/errors/smtp2go-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/smtp2go-problem-types.yml
- group: design
  href: https://artifacts.apis.io/smtp2go/lifecycle/smtp2go-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/smtp2go-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/smtp2go/changelog/smtp2go-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/smtp2go-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.smtp2go.com/reference/changelog
- group: design
  href: https://artifacts.apis.io/smtp2go/conformance/smtp2go-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smtp2go-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.smtp2go.com/blog/security-and-privacy-at-smtp2go/
- group: design
  href: https://artifacts.apis.io/smtp2go/asyncapi/smtp2go-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/smtp2go-webhooks.yml
- group: start
  href: https://artifacts.apis.io/smtp2go/sandbox/smtp2go-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/smtp2go-sandbox.yml
- group: design
  href: https://artifacts.apis.io/smtp2go/data-model/smtp2go-data-model.yml
  title: ''
  type: DataModel
  url: data-model/smtp2go-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smtp2go.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.smtp2go.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.smtp2go.com/pricing/signup/
- group: start
  title: ''
  type: Login
  url: https://app.smtp2go.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smtp2go.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smtp2go.com/privacy/
created: '2026-06-13'
description: SMTP2GO is a New Zealand-founded email and SMS delivery platform, running since 2006, that sends and tracks transactional and marketing messages over SMTP relay or a JSON REST API from data centres in the United States, the European Union and Australia. The v3 API covers sending standard, MIME, batch and scheduled email, sending and receiving SMS, verifying sender domains and single sender addresses, managing SMTP users, API keys, IP allow lists and IP authentication, templates, webhooks, suppressions, subaccounts, dedicated IPs and the email archive, plus activity search and delivery statistics. It also ships a remote MCP server and a published Agent Skill for AI agents.
examples:
- key_count: 4
  name: Add Suppression Example
  slug: add-suppression-example
- key_count: 4
  name: Send Email Example
  slug: send-email-example
- key_count: 4
  name: Send Sms Example
  slug: send-sms-example
finops:
- has_sources: true
  method: derived
  name: Smtp2Go Finops
  primary_unit: emails/mo
  service_category: ''
  slug: smtp2go-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smtp2go.png
json_schemas:
- name: SMTP2GO Send Email Request
  property_count: 15
  slug: smtp2go-send-email
- name: SMTP2GO Suppression
  property_count: 6
  slug: smtp2go-suppression
jsonld:
- class_count: 9
  name: Smtp2Go Context
  property_count: 66
  slug: smtp2go-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.smtp2go.com over streamable HTTP requiring an API key; 5 tools listed.
  name: SMTP2GO remote MCP server
  slug: smtp2go-api-docs
modified: '2026-08-13'
name: SMTP2GO
nav: Providers
network: true
overview: 'SMTP2GO publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, API Keys API, SMS API, and 15 more. Tagged areas include Email, Email Delivery, Transactional Email, SMTP, and SMS.


  The SMTP2GO catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SMTP2GO''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, support, changelog, and 33 more developer resources.'
plans:
- name: Smtp2Go Plans Pricing
  plan_count: 4
  slug: smtp2go-plans-pricing
- name: Smtp2Go Price Estimates
  plan_count: 0
  slug: smtp2go-price-estimates
random_paper: 20
rate_limits:
- limit_count: 9
  name: Smtp2Go Rate Limits
  slug: smtp2go-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SMTP2GO — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smtp2go-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 73.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 78.3
    catalog_earned_first_party: 24.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.3
  facets:
    access_clarity: 92.1
    contract_governance: 28.0
    contract_quality: 73.7
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 76.3
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 85.7
      total: 21
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smtp2go/smtp2go-2026-06-20T194102.png
security:
- kind: authentication
  name: Smtp2Go Authentication
  slug: smtp2go-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Smtp2Go Domain Security
  slug: smtp2go-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: smtp2go-send-email
  slug: smtp2go-send-email
- name: smtp2go-verify-sender-domain
  slug: smtp2go-verify-sender-domain
- name: smtp2go-webhook-and-reconcile
  slug: smtp2go-webhook-and-reconcile
slug: smtp2go
tags:
- Email
- Email Delivery
- Transactional Email
- SMTP
- SMS
- Email API
- Deliverability
- Webhook
- Messaging
- Communications
- MCP
- Agent Skills
website: https://www.smtp2go.com/
---
