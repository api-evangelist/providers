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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Postmark Agentic Access
  operation_count: 108
  slug: postmark-agentic-access
  summary_line: 108 operations · 42 acting
api_count: 3
apis:
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Activate API from Postmark — 1 operation(s) for activate.
  name: Postmark Activate API
  phrasing_intents:
  - id: putBouncesByBounceidActivate
    intent: Reactivate a bounced address
    question: How do I start sending again to an address that was deactivated after a bounce?
  phrasing_ops: 1
  slug: postmark-activate-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Alias API from Postmark — 1 operation(s) for alias.
  name: Postmark Alias API
  phrasing_intents:
  - id: deleteTemplatesByTemplateIdOrAlias
    intent: Delete a template
    question: How do I remove a template I no longer use?
  phrasing_ops: 1
  slug: postmark-alias-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Batch API from Postmark — 2 operation(s) for batch.
  name: Postmark Batch API
  phrasing_intents:
  - id: postEmailBatch
    intent: Send a batch of emails in one call
    question: Can I send many different emails in a single API request?
  - id: postEmailBatchWithTemplates
    intent: Send a batch of templated emails
    question: Can I send lots of personalized template emails in one request?
  phrasing_ops: 2
  slug: postmark-batch-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Bounceid API from Postmark — 3 operation(s) for bounceid.
  name: Postmark Bounceid API
  phrasing_intents:
  - id: getBouncesByBounceid
    intent: Get details of one bounce
    question: What exactly caused a particular bounce I'm looking at?
  - id: getBouncesByBounceidDump
    intent: Get the raw dump of a bounce
    question: Can I see the raw SMTP source of a bounced message?
  phrasing_ops: 2
  slug: postmark-bounceid-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Bounces API API from Postmark — 5 operation(s) for bounces api.
  name: Postmark Bounces API
  phrasing_intents:
  - id: getDeliveryStats
    intent: Summarize bounces and inactive addresses
    question: How many of my recipient addresses are currently inactive because of bounces?
  - id: getBounces
    intent: List bounced emails
    question: Which emails bounced on my server last week?
  - id: getSingleBounce
    intent: Get details of one bounce
    question: What exactly caused a particular bounce I'm looking at?
  - id: getBouncesByBounceidDump
    intent: Get the raw dump of a bounce
    question: Can I see the raw SMTP source of a bounced message?
  - id: activateBounce
    intent: Reactivate a bounced address
    question: How do I start sending again to an address that was deactivated after a bounce?
  phrasing_ops: 5
  slug: postmark-bounces-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Bounces API from Postmark — 2 operation(s) for bounces.
  name: Postmark Bounces API
  phrasing_intents:
  - id: getBounces
    intent: List bounced emails
    question: Which emails bounced on my server last week?
  - id: getBouncesTags
    intent: List tags that have bounces
    question: Which of my message tags have bounced emails?
  phrasing_ops: 2
  slug: postmark-bounces-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Browser Families API from Postmark — 1 operation(s) for browser families.
  name: Postmark Browser Families API
  phrasing_intents:
  - id: getStatsOutboundClicksBrowserfamilies
    intent: Break down link clicks by browser
    question: Which browsers do recipients use when they click my email links?
  phrasing_ops: 1
  slug: postmark-browser-families-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Bypass API from Postmark — 1 operation(s) for bypass.
  name: Postmark Bypass API
  phrasing_intents:
  - id: putMessagesInboundByMessageidBypass
    intent: Let a blocked inbound email through
    question: An inbound email got blocked by my rules — how do I let it through?
  phrasing_ops: 1
  slug: postmark-bypass-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Deliverystats API from Postmark — 1 operation(s) for deliverystats.
  name: Postmark Deliverystats API
  phrasing_intents:
  - id: getDeliverystats
    intent: Summarize bounces and inactive addresses
    question: How many of my recipient addresses are currently inactive because of bounces?
  phrasing_ops: 1
  slug: postmark-deliverystats-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Domains API API from Postmark — 6 operation(s) for domains api.
  name: Postmark Domains API
  phrasing_intents:
  - id: listDomains
    intent: List sending domains
    question: Which domains have I added to my Postmark account?
  - id: createDomain
    intent: Add a sending domain
    question: How do I add a new domain so I can send email from it?
  - id: getDomain
    intent: Get a domain's DNS and verification status
    question: What DKIM and Return-Path records does one of my domains need?
  - id: editDomain
    intent: Change a domain's Return-Path
    question: How do I change the Return-Path on a domain I already added?
  - id: deleteDomain
    intent: Remove a sending domain
    question: How do I remove a domain I no longer send from?
  - id: requestDkimVerificationForDomain
    intent: Verify a domain's DKIM record
    question: I added the DKIM TXT record — how do I get it checked?
  - id: requestReturnPathVerificationForDomain
    intent: Verify a domain's Return-Path CNAME
    question: How do I confirm my Return-Path CNAME is set up correctly?
  - id: requestSPFVerificationForDomain
    intent: Verify a domain's SPF record
    question: How do I get the SPF record on my domain verified?
  phrasing_ops: 9
  slug: postmark-domains-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Dump API from Postmark — 2 operation(s) for dump.
  name: Postmark Dump API
  phrasing_intents:
  - id: getMessagesOutboundByMessageidDump
    intent: Get the raw source of a sent email
    question: How do I see the raw SMTP source of an email I sent?
  phrasing_ops: 1
  slug: postmark-dump-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Email API from Postmark — 4 operation(s) for email.
  name: Postmark Email API
  phrasing_intents:
  - id: postEmail
    intent: Send a single email
    question: How do I send one transactional email with Postmark?
  - id: postEmailWithTemplate
    intent: Send an email from a template
    question: How do I send an email using one of my saved templates?
  phrasing_ops: 2
  slug: postmark-email-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Inbound API from Postmark — 4 operation(s) for inbound.
  name: Postmark Inbound API
  phrasing_intents:
  - id: getMessagesInboundByMessageidDetails
    intent: Get details of a received email
    question: What did a specific inbound email contain and how was it processed?
  - id: putMessagesInboundByMessageidRetry
    intent: Retry a failed inbound email
    question: My inbound webhook was down — how do I reprocess a failed message?
  - id: getMessagesInbound
    intent: Search received inbound emails
    question: Which inbound emails failed processing or got blocked this week?
  phrasing_ops: 3
  slug: postmark-inbound-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Inbound Rules API API from Postmark — 2 operation(s) for inbound rules api.
  name: Postmark Inbound Rules API
  phrasing_intents:
  - id: createInboundRule
    intent: Block an inbound sender or domain
    question: How do I stop inbound mail from a specific sender reaching my webhook?
  - id: listInboundRules
    intent: List inbound blocking rules
    question: Which senders or domains am I currently blocking from my inbound stream?
  - id: deleteInboundRule
    intent: Remove an inbound blocking rule
    question: How do I unblock a sender I added an inbound rule for?
  phrasing_ops: 3
  slug: postmark-inbound-rules-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Locations API from Postmark — 1 operation(s) for locations.
  name: Postmark Locations API
  phrasing_intents:
  - id: getStatsOutboundClicksLocation
    intent: Compare clicks in HTML versus text parts
    question: Are recipients clicking links in the HTML part or the plain text part of my emails?
  phrasing_ops: 1
  slug: postmark-locations-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Message Identifier API from Postmark — 2 operation(s) for message identifier.
  name: Postmark Message Identifier API
  phrasing_intents:
  - id: getMessagesOutboundClicksByMessageid
    intent: Get link clicks for one sent email
    question: Did anyone click the links in one particular email I sent?
  - id: getMessagesOutboundOpensByMessageid
    intent: Get opens for one sent email
    question: Has a specific email I sent been opened, and how many times?
  phrasing_ops: 2
  slug: postmark-message-identifier-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Messages API API from Postmark — 11 operation(s) for messages api.
  name: Postmark Messages API
  phrasing_intents:
  - id: searchOutboundMessages
    intent: Search sent emails
    question: Did my password reset email actually go out to a particular customer?
  - id: getOutboundMessageDetails
    intent: Get details of a sent email
    question: What happened to one specific email I sent — was it delivered?
  - id: getOutboundMessageDump
    intent: Get the raw source of a sent email
    question: How do I see the raw SMTP source of an email I sent?
  - id: searchInboundMessages
    intent: Search received inbound emails
    question: Which inbound emails failed processing or got blocked this week?
  - id: getInboundMessageDetails
    intent: Get details of a received email
    question: What did a specific inbound email contain and how was it processed?
  - id: bypassRulesForInboundMessage
    intent: Let a blocked inbound email through
    question: An inbound email got blocked by my rules — how do I let it through?
  - id: retryInboundMessageProcessing
    intent: Retry a failed inbound email
    question: My inbound webhook was down — how do I reprocess a failed message?
  - id: searchOpensForOutboundMessages
    intent: Search email open events
    question: Who opened my emails, and from which email clients?
  phrasing_ops: 11
  slug: postmark-messages-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Messages API from Postmark — 11 operation(s) for messages.
  name: Postmark Messages API
  phrasing_intents:
  - id: getMessagesOutboundClicks
    intent: Search link click events
    question: Which links in my emails are recipients clicking, and from where?
  - id: getMessagesOutboundOpens
    intent: Search email open events
    question: Who opened my emails, and from which email clients?
  - id: getMessagesOutboundByMessageidDetails
    intent: Get details of a sent email
    question: What happened to one specific email I sent — was it delivered?
  - id: getMessagesOutbound
    intent: Search sent emails
    question: Did my password reset email actually go out to a particular customer?
  phrasing_ops: 4
  slug: postmark-messages-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Outbound API from Postmark — 20 operation(s) for outbound.
  name: Postmark Outbound API
  phrasing_intents:
  - id: getStatsOutboundClicks
    intent: Count link clicks per day
    question: How many link clicks did my emails get each day?
  - id: getStatsOutboundClicksPlatforms
    intent: Break down link clicks by device platform
    question: Do people click my email links more from phones or desktops?
  - id: getStatsOutboundOpens
    intent: Count email opens per day
    question: How many opens and unique opens did my emails get each day?
  - id: getStatsOutboundOpensPlatforms
    intent: Break down opens by device platform
    question: Are my emails opened more on mobile, desktop or webmail?
  - id: getStatsOutboundOpensReadtimes
    intent: See how long recipients spend reading emails
    question: How long do recipients spend reading my emails after opening them?
  - id: getStatsOutbound
    intent: Get an overview of outbound email stats
    question: How is my outbound email performing overall this month?
  - id: getStatsOutboundBounces
    intent: Count bounces per day by type
    question: How many hard and soft bounces did I get each day?
  - id: getStatsOutboundSends
    intent: Count emails sent per day
    question: How many emails did I send each day last week?
  phrasing_ops: 10
  slug: postmark-outbound-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Sender Signatures API API from Postmark — 5 operation(s) for sender signatures api.
  name: Postmark Sender Signatures API
  phrasing_intents:
  - id: listSenderSignatures
    intent: List sender signatures
    question: Which from addresses are registered as sender signatures on my account?
  - id: createSenderSignature
    intent: Register a new from address
    question: How do I add a new from address so I can send email as it?
  - id: getSenderSignature
    intent: Get a sender signature
    question: Is my sender signature confirmed, and what DNS does it still need?
  - id: editSenderSignature
    intent: Update a sender signature
    question: How do I change the display name on an existing sender signature?
  - id: deleteSenderSignature
    intent: Delete a sender signature
    question: How do I remove a from address I no longer use?
  - id: resendSenderSignatureConfirmationEmail
    intent: Resend a sender confirmation email
    question: The confirmation email for my new sender never arrived — can I get it resent?
  - id: requestSPFVerificationForSenderSignature
    intent: Verify SPF for a sender signature
    question: How do I get SPF checked for a sender signature's domain?
  - id: requestNewDKIMKeyForSenderSignature
    intent: Request a new DKIM key for a sender
    question: How do I get a fresh DKIM key for a sender signature?
  phrasing_ops: 8
  slug: postmark-sender-signatures-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Sending API API from Postmark — 4 operation(s) for sending api.
  name: Postmark Sending API
  phrasing_intents:
  - id: sendEmail
    intent: Send a single email
    question: How do I send one transactional email with Postmark?
  - id: sendEmailBatch
    intent: Send a batch of emails in one call
    question: Can I send many different emails in a single API request?
  - id: sendEmailWithTemplate
    intent: Send an email from a template
    question: How do I send an email using one of my saved templates?
  - id: sendEmailBatchWithTemplates
    intent: Send a batch of templated emails
    question: Can I send lots of personalized template emails in one request?
  phrasing_ops: 4
  slug: postmark-sending-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Server Configuration API API from Postmark — 1 operation(s) for server configuration api.
  name: Postmark Server Configuration API
  phrasing_intents:
  - id: getCurrentServerConfiguration
    intent: View this server's settings
    question: What webhook URLs and tracking settings is my current server using?
  - id: editCurrentServerConfiguration
    intent: Change this server's settings
    question: How do I point bounce webhooks for my current server at a new URL?
  phrasing_ops: 2
  slug: postmark-server-configuration-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Server Management API API from Postmark — 2 operation(s) for server management api.
  name: Postmark Server Management API
  phrasing_intents:
  - id: getServerInformation
    intent: Get a server on the account
    question: What are the settings of one of the servers on my account?
  - id: editServerInformation
    intent: Edit a server by ID
    question: How do I rename another server on my account?
  - id: deleteServer
    intent: Delete a server
    question: How do I permanently remove a server I no longer need?
  - id: listServers
    intent: List servers on the account
    question: Which servers exist on my account?
  - id: createServer
    intent: Create a server
    question: How do I set up a new server to separate staging mail from production?
  phrasing_ops: 5
  slug: postmark-server-management-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Servers API from Postmark — 1 operation(s) for servers.
  name: Postmark Servers API
  phrasing_intents:
  - id: getServer
    intent: View this server's settings
    question: What webhook URLs and tracking settings is my current server using?
  phrasing_ops: 1
  slug: postmark-servers-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Stats API API from Postmark — 12 operation(s) for stats api.
  name: Postmark Stats API
  phrasing_intents:
  - id: getOutboundOverviewStatistics
    intent: Get an overview of outbound email stats
    question: How is my outbound email performing overall this month?
  - id: getSentCounts
    intent: Count emails sent per day
    question: How many emails did I send each day last week?
  - id: getBounceCounts
    intent: Count bounces per day by type
    question: How many hard and soft bounces did I get each day?
  - id: getSpamComplaints
    intent: Count spam complaints per day
    question: How many recipients marked my emails as spam?
  - id: getTrackedEmailCounts
    intent: Count emails sent with tracking enabled
    question: How many of my emails went out with open or link tracking turned on?
  - id: getOutboundOpenCounts
    intent: Count email opens per day
    question: How many opens and unique opens did my emails get each day?
  - id: getOutboundOpenCountsByPlatform
    intent: Break down opens by device platform
    question: Are my emails opened more on mobile, desktop or webmail?
  - id: getOutboundOpenCountsByEmailClient
    intent: Break down opens by email client
    question: Which email clients do my recipients open messages in?
  phrasing_ops: 12
  slug: postmark-stats-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Templates API API from Postmark — 6 operation(s) for templates api.
  name: Postmark Templates API
  phrasing_intents:
  - id: pushTemplates
    intent: Copy templates from one server to another
    question: How do I copy my templates from staging to production?
  - id: sendEmailWithTemplate
    intent: Send one email from a saved template
    question: How do I send a single message based on a template I've stored?
  - id: sendEmailBatchWithTemplates
    intent: Send many templated emails at once
    question: Can I send a whole list of template-based emails in one request?
  - id: listTemplates
    intent: List the server's templates
    question: Which email templates exist on this server?
  - id: postTemplates
    intent: Create a template
    question: How do I create a new email template on my server?
  - id: getSingleTemplate
    intent: Get a template
    question: What does the HTML and subject of one of my templates look like?
  - id: updateTemplate
    intent: Edit a template
    question: How do I change the subject line of an existing template?
  - id: deleteTemplate
    intent: Delete a template
    question: How do I remove a template I no longer use?
  phrasing_ops: 9
  slug: postmark-templates-api-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Templates API from Postmark — 4 operation(s) for templates.
  name: Postmark Templates API
  phrasing_intents:
  - id: getTemplates
    intent: List the server's templates
    question: Which email templates exist on this server?
  - id: postTemplatesValidate
    intent: Validate and preview template content
    question: Will my template syntax render correctly before I save it?
  phrasing_ops: 2
  slug: postmark-templates-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Triggerid API from Postmark — 1 operation(s) for triggerid.
  name: Postmark Triggerid API
  phrasing_intents:
  - id: deleteTriggersInboundrulesByTriggerid
    intent: Remove an inbound blocking rule
    question: How do I unblock a sender I added an inbound rule for?
  phrasing_ops: 1
  slug: postmark-triggerid-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Triggers API from Postmark — 4 operation(s) for triggers.
  name: Postmark Triggers API
  phrasing_intents:
  - id: getTriggersInboundrules
    intent: List inbound blocking rules
    question: Which senders or domains am I currently blocking from my inbound stream?
  - id: getTriggersTags
    intent: Search tag triggers
    question: Which tag triggers are set up on my server?
  - id: deleteTriggersTagsByTriggerid
    intent: Delete a tag trigger
    question: How do I remove a tag trigger I no longer need?
  phrasing_ops: 3
  slug: postmark-triggers-api
- baseURL: https://api.postmarkapp.com
  baseurl_source: declared
  description: The Email Clients API from Postmark — 1 operation(s) for email clients.
  name: Postmark Email Clients API
  phrasing_intents:
  - id: getStatsOutboundOpensEmailclients
    intent: Break down opens by email client
    question: Which email clients do my recipients open messages in?
  phrasing_ops: 1
  slug: postmark-email-clients-api
artifact_total: 132
asyncapis:
- description: AsyncAPI description of Postmark's outbound webhook surface. Postmark delivers event notifications by issuing HTTP POST requests with a JSON body to a URL the customer configures per server (and per s
  name: Postmark Webhooks
  slug: postmark-webhooks-asyncapi
collections:
- collection_type: open
  name: Postmark Account Activate API
  slug: open-postmark-activate-api
- collection_type: open
  name: Postmark Account Activate Alias API
  slug: open-postmark-alias-api
- collection_type: open
  name: Postmark API
  slug: open-postmark-api
- collection_type: open
  name: Postmark Account Activate Batch API
  slug: open-postmark-batch-api
- collection_type: open
  name: Postmark Account Activate Bounceid API
  slug: open-postmark-bounceid-api
- collection_type: open
  name: Postmark Account Activate Bounces API API
  slug: open-postmark-bounces-api-api
- collection_type: open
  name: Postmark Account Activate Bounces API
  slug: open-postmark-bounces-api
- collection_type: open
  name: Postmark Account Activate Browser Families API
  slug: open-postmark-browser-families-api
- collection_type: open
  name: Postmark Account Activate Bypass API
  slug: open-postmark-bypass-api
- collection_type: open
  name: Postmark Account Activate Deliverystats API
  slug: open-postmark-deliverystats-api
- collection_type: open
  name: Postmark Account Activate Domains API API
  slug: open-postmark-domains-api-api
- collection_type: open
  name: Postmark Account Activate Dump API
  slug: open-postmark-dump-api
- collection_type: open
  name: Postmark Account Activate Email API
  slug: open-postmark-email-api
- collection_type: open
  name: Postmark Account Activate Emailclients API
  slug: open-postmark-emailclients-api
- collection_type: open
  name: Postmark Account Activate Inbound API
  slug: open-postmark-inbound-api
- collection_type: open
  name: Postmark Account Activate Inbound Rules API API
  slug: open-postmark-inbound-rules-api-api
- collection_type: open
  name: Postmark Account Activate Locations API
  slug: open-postmark-locations-api
- collection_type: open
  name: Postmark Account Activate Message Identifier API
  slug: open-postmark-message-identifier-api
- collection_type: open
  name: Postmark Account Activate Messages API API
  slug: open-postmark-messages-api-api
- collection_type: open
  name: Postmark Account Activate Messages API
  slug: open-postmark-messages-api
- collection_type: open
  name: Postmark Account Activate Messages > Inbound > {Messageid} API
  slug: open-postmark-messages-inbound-messageid-api
- collection_type: open
  name: Postmark Account Activate Messages > Outbound > Clicks API
  slug: open-postmark-messages-outbound-clicks-api
- collection_type: open
  name: Postmark Account Activate Messages > Outbound > {Messageid} API
  slug: open-postmark-messages-outbound-messageid-api
- collection_type: open
  name: Postmark Account Activate Messages > Outbound > Opens API
  slug: open-postmark-messages-outbound-opens-api
- collection_type: open
  name: Postmark Account Activate Outbound API
  slug: open-postmark-outbound-api
- collection_type: open
  name: Postmark Account Activate Platforms API
  slug: open-postmark-platforms-api
- collection_type: open
  name: Postmark Account Activate Readtimes API
  slug: open-postmark-readtimes-api
- collection_type: open
  name: Postmark Account Activate Retry API
  slug: open-postmark-retry-api
- collection_type: open
  name: Postmark Account Activate Sender Signatures API API
  slug: open-postmark-sender-signatures-api-api
- collection_type: open
  name: Postmark Account Activate Sending API API
  slug: open-postmark-sending-api-api
- collection_type: open
  name: Postmark Account Activate Sends API
  slug: open-postmark-sends-api
- collection_type: open
  name: Postmark Account Activate Server Configuration API API
  slug: open-postmark-server-configuration-api-api
- collection_type: open
  name: Postmark Account Activate Server Management API API
  slug: open-postmark-server-management-api-api
- collection_type: open
  name: Postmark Account Activate Servers API
  slug: open-postmark-servers-api
- collection_type: open
  name: Postmark Account Activate Spam API
  slug: open-postmark-spam-api
- collection_type: open
  name: Postmark Account Activate Statistics API
  slug: open-postmark-statistics-api
- collection_type: open
  name: Postmark Account Activate Stats API API
  slug: open-postmark-stats-api-api
- collection_type: open
  name: Postmark Account Activate Stats/Outbound API
  slug: open-postmark-stats-outbound-api
- collection_type: open
  name: Postmark Account Activate Stats/Outbound > Clicks API
  slug: open-postmark-stats-outbound-clicks-api
- collection_type: open
  name: Postmark Account Activate Stats/Outbound > Opens API
  slug: open-postmark-stats-outbound-opens-api
- collection_type: open
  name: Postmark Account Activate Template API
  slug: open-postmark-template-api
- collection_type: open
  name: Postmark Account Activate Templates API API
  slug: open-postmark-templates-api-api
- collection_type: open
  name: Postmark Account Activate Templates API
  slug: open-postmark-templates-api
- collection_type: open
  name: Postmark Account Activate Triggerid API
  slug: open-postmark-triggerid-api
- collection_type: open
  name: Postmark Account Activate Triggers API
  slug: open-postmark-triggers-api
- collection_type: open
  name: Postmark Account Activate Triggers > Inboundrules API
  slug: open-postmark-triggers-inboundrules-api
- collection_type: open
  name: Postmark Account Activate Triggers > Tags API
  slug: open-postmark-triggers-tags-api
- collection_type: open
  name: Postmark Account Activate Validate API
  slug: open-postmark-validate-api
common:
- group: other
  href: https://artifacts.apis.io/postmark/capabilities/postmark-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/postmark-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-emailclients-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-emailclients-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-messages-inbound-messageid-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-messages-inbound-messageid-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-messages-outbound-clicks-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-messages-outbound-clicks-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-messages-outbound-messageid-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-messages-outbound-messageid-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-messages-outbound-opens-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-messages-outbound-opens-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-platforms-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-platforms-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-readtimes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-readtimes-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-retry-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-retry-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-sends-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-sends-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-spam-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-spam-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-statistics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-statistics-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-stats-outbound-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-stats-outbound-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-stats-outbound-clicks-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-stats-outbound-clicks-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-stats-outbound-opens-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-stats-outbound-opens-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-template-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-template-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-triggers-inboundrules-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-triggers-inboundrules-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-triggers-tags-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-triggers-tags-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postmark/overlays/postmark-validate-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postmark-validate-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/postmark/agentic-access/postmark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postmark-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/postmark/security/postmark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postmark-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/ActiveCampaign/postmark-skills
- group: company
  title: ''
  type: Website
  url: https://postmarkapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://postmarkapp.com/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://postmarkapp.com/developer/api/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://postmarkapp.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://account.postmarkapp.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://account.postmarkapp.com/login
- group: company
  title: ''
  type: Blog
  url: https://postmarkapp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://postmarkapp.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postmarkapp.com
- group: other
  title: ''
  type: Templates
  url: https://postmarkapp.com/transactional-email-templates
- group: operate
  title: ''
  type: ChangeLog
  url: https://postmarkapp.com/updates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postmarkapp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wildbit.com/privacy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ActiveCampaign
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/postmarkapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postmarkapp
- group: build
  href: https://artifacts.apis.io/postmark/packages/postmark-packages.yml
  title: ''
  type: Packages
  url: packages/postmark-packages.yml
- group: build
  href: https://artifacts.apis.io/postmark/packages/postmark-packages.yml
  title: ''
  type: SDKs
  url: packages/postmark-packages.yml
- group: agent
  href: https://artifacts.apis.io/postmark/mcp/postmark-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/postmark-mcp.yml
- group: build
  href: https://artifacts.apis.io/postmark/mcp/postmark-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/postmark-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/postmark/llms/postmark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postmark-llms.txt
- group: design
  href: https://artifacts.apis.io/postmark/conformance/postmark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postmark-conformance.yml
- group: auth
  href: https://artifacts.apis.io/postmark/security/postmark-trust-center.yml
  title: ''
  type: Compliance
  url: security/postmark-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/postmark/security/postmark-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/postmark-trust-center.yml
- group: design
  href: https://artifacts.apis.io/postmark/errors/postmark-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postmark-problem-types.yml
- group: design
  href: https://artifacts.apis.io/postmark/lifecycle/postmark-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/postmark-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/postmark/lifecycle/postmark-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/postmark-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/postmark/authentication/postmark-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postmark-authentication.yml
- group: design
  href: https://artifacts.apis.io/postmark/conventions/postmark-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postmark-conventions.yml
- group: operate
  href: https://artifacts.apis.io/postmark/changelog/postmark-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/postmark-changelog.yml
- group: build
  href: https://artifacts.apis.io/postmark/cli/postmark-cli.yml
  title: ''
  type: CLI
  url: cli/postmark-cli.yml
- group: design
  href: https://artifacts.apis.io/postmark/data-model/postmark-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postmark-data-model.yml
- group: start
  href: https://artifacts.apis.io/postmark/sandbox/postmark-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/postmark-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/postmark/plans/postmark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postmark-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/postmark/rate-limits/postmark-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postmark-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/postmark/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/postmark/asyncapi/postmark-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/postmark-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/postmark/asyncapi/postmark-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/postmark-webhooks-asyncapi.yml
- group: commercial
  href: https://artifacts.apis.io/postmark/finops/postmark-finops.yml
  title: ''
  type: FinOps
  url: finops/postmark-finops.yml
- group: design
  href: https://artifacts.apis.io/postmark/vocabulary/postmark-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postmark-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://postmarkapp.com/developer
- group: docs
  title: ''
  type: APIReference
  url: https://postmarkapp.com/developer/api/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActiveCampaign
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/15802082-f50b3ffc-9eee-4ab1-bdc5-8b423d19d535?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D15802082-f50b3ffc-9eee-4ab1-bdc5-8b423d19d535%26entityType%3Dcollection%26workspaceId%3D55e9c6f2-5d69-40a5-b00b-caec1640454c
created: '2024-04-14'
description: Postmark is an email delivery service that helps businesses send and track transactional and broadcast email reliably, replacing SMTP with a scalable service that surfaces detailed delivery analytics, bounce tracking, open and click tracking, and dedicated IP addresses.
features:
- 'Free: 100 emails/month'
- 'Basic: $15/mo for 10K emails'
- 'Pro: $16.50/mo for 10K emails with templates and webhooks'
- 'Platform: $18/mo for 10K emails with multiple servers and dedicated IPs'
- Email API and SMTP server
- Templates with versioning (Pro+)
- Webhooks for delivery, bounce, open, click, spam, subscription events
- Bounce and spam complaint handling
- Server tokens for per-environment isolation
- Send up to 500 emails per batch request
- Inbound email parsing
- Message Streams (broadcast vs transactional)
- OpenTracker beacon for opens/clicks
- Suppression management
- Dedicated IPs (Platform)
- Best-in-class deliverability
finops:
- has_sources: true
  method: derived
  name: Postmark Finops
  primary_unit: emails
  service_category: ''
  slug: postmark-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postmark.png
json_schemas:
- name: CreateServerPayload
  property_count: 14
  slug: postmark-createserverpayload
- name: DKIMRotationResponse
  property_count: 12
  slug: postmark-dkimrotationresponse
- name: DomainCreationModel
  property_count: 2
  slug: postmark-domaincreationmodel
- name: DomainEditingModel
  property_count: 1
  slug: postmark-domaineditingmodel
- name: DomainExtendedInformation
  property_count: 18
  slug: postmark-domainextendedinformation
- name: DomainInformation
  property_count: 6
  slug: postmark-domaininformation
- name: DomainListingResults
  property_count: 2
  slug: postmark-domainlistingresults
- name: DomainSPFResult
  property_count: 3
  slug: postmark-domainspfresult
- name: EditServerPayload
  property_count: 14
  slug: postmark-editserverpayload
- name: ExtendedServerInfo
  property_count: 19
  slug: postmark-extendedserverinfo
- name: SenderListingResults
  property_count: 2
  slug: postmark-senderlistingresults
- name: SenderSignatureCreationModel
  property_count: 4
  slug: postmark-sendersignaturecreationmodel
- name: SenderSignatureEditingModel
  property_count: 3
  slug: postmark-sendersignatureeditingmodel
- name: SenderSignatureExtendedInformation
  property_count: 22
  slug: postmark-sendersignatureextendedinformation
- name: SenderSignatureInformation
  property_count: 6
  slug: postmark-sendersignatureinformation
- name: ServerListingResponse
  property_count: 2
  slug: postmark-serverlistingresponse
- name: StandardPostmarkResponse
  property_count: 2
  slug: postmark-standardpostmarkresponse
- name: TemplatesPushModel
  property_count: 3
  slug: postmark-templatespushmodel
- name: TemplatesPushResponse
  property_count: 2
  slug: postmark-templatespushresponse
json_structures:
- name: Postmark Structure
  property_count: 0
  slug: postmark-structure
layout: provider
mcp_servers:
- description: Postmark ships an official, first-party MCP server. It is distributed ONLY as a local-stdio npm package — there is no hosted remote endpoint an MCP client can POST to. Postmark's own landing page (htt
  name: Postmark MCP Server
  slug: postmark-mcp-server
modified: '2026-09-16'
name: Postmark
nav: Providers
network: true
overview: 'Postmark publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activate API, Alias API, Batch API, and 27 more. Tagged areas include Email, Messaging, Transactional Email, Deliverability, and SMTP.


  The Postmark catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Postmark''s developer surface includes documentation, getting-started guide, pricing, signup flow, engineering blog, support, changelog, and 59 more developer resources.'
plans:
- name: Postmark Plans Pricing
  plan_count: 7
  slug: postmark-plans-pricing
- name: Postmark Price Estimates
  plan_count: 0
  slug: postmark-price-estimates
random_paper: 17
rate_limits:
- limit_count: 11
  name: Postmark Rate Limits
  slug: postmark-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Postmark — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: postmark-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Postmark — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: postmark-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 71.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 76.0
    catalog_earned_first_party: 24.0
    catalog_gap: 39.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 82.9
    contract_governance: 31.8
    contract_quality: 54.5
    developer_ergonomics: 90.5
    discoverability: 76.7
    operational_transparency: 81.6
  previous_composite: 70.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 86.7
      total: 30
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/postmark/postmark-2026-06-20T192003.png
security:
- kind: authentication
  name: Postmark Authentication
  slug: postmark-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Postmark Domain Security
  slug: postmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Postmark Trust Center
  slug: postmark-trust-center
  summary_line: SOC 2, SSAE 16 SOC 1 Type 2, PCI DSS Level 1, HIPAA, GDPR
skill_count: 6
skills:
- name: postmark-email-best-practices
  slug: postmark-email-best-practices
- name: postmark-inbound
  slug: postmark-inbound
- name: postmark-send-email
  slug: postmark-send-email
- name: postmark-templates
  slug: postmark-templates
- name: postmark-webhooks
  slug: postmark-webhooks
- name: postmark
  slug: postmark
slug: postmark
tags:
- Email
- Messaging
- Transactional Email
- Deliverability
- SMTP
- Email API
- Webhook
- Inbound Email
- Email Templates
- Email Analytics
website: https://postmarkapp.com
---
