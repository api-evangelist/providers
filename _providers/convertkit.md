---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Convertkit Agentic Access
  operation_count: 72
  slug: convertkit-agentic-access
  summary_line: 72 operations · 39 acting
api_count: 2
apis:
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Accounts API from Kit — 5 operation(s) for accounts.
  name: Kit Accounts API
  phrasing_intents:
  - id: getV4Account
    intent: View the current account and user
    question: Which Kit account is my API key or OAuth token connected to?
  - id: getV4AccountColors
    intent: List the account's saved brand colors
    question: What brand colors are saved on my newsletter account?
  - id: putV4AccountColors
    intent: Replace the account's brand colors
    question: How do I change the saved brand colors on my account?
  - id: getV4AccountCreatorProfile
    intent: Get the account's public creator profile
    question: What does my public creator profile look like through the API?
  - id: getV4AccountEmailStats
    intent: Get account-wide email performance stats
    question: What are my overall open and click rates across the emails I've sent?
  - id: getV4AccountGrowthStats
    intent: Get subscriber growth stats for a date range
    question: How many subscribers did I gain and lose over the last 90 days?
  phrasing_ops: 6
  slug: convertkit-accounts-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Broadcasts API from Kit — 5 operation(s) for broadcasts.
  name: Kit Broadcasts API
  phrasing_intents:
  - id: getV4Broadcasts
    intent: List broadcasts
    question: Which broadcasts have I sent or drafted in my newsletter account?
  - id: postV4Broadcasts
    intent: Create, draft or schedule a broadcast
    question: How do I schedule a new email broadcast to go out at a specific time?
  - id: getV4BroadcastsStats
    intent: Get stats across many broadcasts
    question: How did all my recent broadcasts perform side by side?
  - id: getV4BroadcastsByBroadcastIdClicks
    intent: Get link clicks for one broadcast
    question: Which links in a broadcast got the most clicks?
  - id: getV4BroadcastsByBroadcastIdStats
    intent: Get stats for one broadcast
    question: What was the open rate and click rate for a specific broadcast?
  - id: deleteV4BroadcastsById
    intent: Delete a broadcast
    question: How do I get rid of a broadcast draft I no longer need?
  - id: getV4BroadcastsById
    intent: Get a broadcast's details
    question: Can I fetch the subject, content and schedule of one existing broadcast?
  - id: putV4BroadcastsById
    intent: Update an existing broadcast
    question: How do I change the subject or content of a broadcast I already drafted?
  phrasing_ops: 8
  slug: convertkit-broadcasts-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Custom Fields API from Kit — 4 operation(s) for custom fields.
  name: Kit Custom Fields API
  phrasing_intents:
  - id: postV4BulkCustomFields
    intent: Create many custom fields at once
    question: Can I create a batch of new custom fields in one request?
  - id: postV4BulkCustomFieldsSubscribers
    intent: Set custom field values for many subscribers
    question: How do I update custom field values for thousands of subscribers at once?
  - id: getV4CustomFields
    intent: List custom fields
    question: What custom fields have I defined for collecting subscriber data?
  - id: postV4CustomFields
    intent: Create a custom field
    question: How do I add a new custom field like Last Name to my subscriber records?
  - id: deleteV4CustomFieldsById
    intent: Delete a custom field and its data
    question: What happens to subscriber data when I delete a custom field?
  - id: putV4CustomFieldsById
    intent: Rename a custom field's label
    question: Can I rename an existing custom field without losing subscriber data?
  phrasing_ops: 6
  slug: convertkit-custom-fields-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Email Templates API from Kit — 1 operation(s) for email templates.
  name: Kit Email Templates API
  phrasing_intents:
  - id: getV4EmailTemplates
    intent: List email templates
    question: Which email templates are available on my account?
  phrasing_ops: 1
  slug: convertkit-email-templates-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Forms API from Kit — 4 operation(s) for forms.
  name: Kit Forms API
  phrasing_intents:
  - id: postV4BulkFormsSubscribers
    intent: Add many subscribers to forms at once
    question: Can I add a large batch of subscribers to forms in one request?
  - id: getV4Forms
    intent: List forms and landing pages
    question: What signup forms and landing pages do I have?
  - id: getV4FormsByFormIdSubscribers
    intent: List subscribers who joined via a form
    question: Who signed up through a particular form?
  - id: postV4FormsByFormIdSubscribers
    intent: Add an existing subscriber to a form by email
    question: How do I add someone to a form using just their email address?
  - id: postV4FormsByFormIdSubscribersById
    intent: Add an existing subscriber to a form by id
    question: Can I add a subscriber to a form when I only have their subscriber id?
  phrasing_ops: 5
  slug: convertkit-forms-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Posts API from Kit — 2 operation(s) for posts.
  name: Kit Posts API
  phrasing_intents:
  - id: getV4Posts
    intent: List published newsletter posts
    question: Which posts are published on my newsletter's web archive?
  - id: getV4PostsById
    intent: Get a single post
    question: How do I fetch one specific newsletter post by its id?
  phrasing_ops: 2
  slug: convertkit-posts-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Purchases API from Kit — 2 operation(s) for purchases.
  name: Kit Purchases API
  phrasing_intents:
  - id: getV4Purchases
    intent: List purchases
    question: What purchases have been recorded against my subscribers?
  - id: postV4Purchases
    intent: Record a purchase
    question: How do I log a sale from my own store against a subscriber?
  - id: getV4PurchasesById
    intent: Get a single purchase
    question: Can I look up the details of one specific purchase?
  phrasing_ops: 3
  slug: convertkit-purchases-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Segments API from Kit — 1 operation(s) for segments.
  name: Kit Segments API
  phrasing_intents:
  - id: getV4Segments
    intent: List subscriber segments
    question: Which subscriber segments have I set up?
  phrasing_ops: 1
  slug: convertkit-segments-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Sequence Emails API from Kit — 2 operation(s) for sequence emails.
  name: Kit Sequence Emails API
  phrasing_intents:
  - id: getV4SequencesBySequenceIdEmails
    intent: List the emails in a sequence
    question: What emails are in my welcome sequence and in what order?
  - id: postV4SequencesBySequenceIdEmails
    intent: Add an email to a sequence
    question: How do I add a new email step to an automated sequence?
  - id: deleteV4SequencesBySequenceIdEmailsById
    intent: Delete an email from a sequence
    question: What happens to queued subscribers if I delete one email from a sequence?
  - id: getV4SequencesBySequenceIdEmailsById
    intent: Get one sequence email with its content
    question: Can I fetch the full HTML of a single email inside a sequence?
  - id: putV4SequencesBySequenceIdEmailsById
    intent: Update a sequence email
    question: How do I publish a draft email inside a sequence?
  phrasing_ops: 5
  slug: convertkit-sequence-emails-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Sequences API from Kit — 4 operation(s) for sequences.
  name: Kit Sequences API
  phrasing_intents:
  - id: getV4Sequences
    intent: List sequences
    question: What automated email sequences do I have?
  - id: postV4Sequences
    intent: Create an empty sequence
    question: How do I start a new automated email sequence?
  - id: deleteV4SequencesById
    intent: Delete a sequence
    question: What happens to active subscribers if I delete a whole sequence?
  - id: getV4SequencesById
    intent: Get a sequence's settings
    question: What schedule and sending address is a specific sequence using?
  - id: putV4SequencesById
    intent: Update a sequence's settings
    question: How do I pause or reactivate an existing sequence?
  - id: getV4SequencesBySequenceIdSubscribers
    intent: List subscribers in a sequence
    question: Who is currently enrolled in a given sequence?
  - id: postV4SequencesBySequenceIdSubscribers
    intent: Add a subscriber to a sequence by email
    question: How do I enroll someone in a sequence using their email address?
  - id: postV4SequencesBySequenceIdSubscribersById
    intent: Add a subscriber to a sequence by id
    question: Can I enroll a subscriber in a sequence using their subscriber id instead of email?
  phrasing_ops: 8
  slug: convertkit-sequences-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Snippets API from Kit — 2 operation(s) for snippets.
  name: Kit Snippets API
  phrasing_intents:
  - id: getV4Snippets
    intent: List reusable email snippets
    question: What reusable content snippets can I drop into my emails?
  - id: postV4Snippets
    intent: Create a reusable email snippet
    question: How do I create a snippet I can reuse across broadcasts and sequence emails?
  - id: getV4SnippetsById
    intent: Get one snippet with its content
    question: Can I fetch the full content of a single snippet?
  - id: putV4SnippetsById
    intent: Update, rename or archive a snippet
    question: How do I change the text of an existing snippet?
  phrasing_ops: 4
  slug: convertkit-snippets-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Subscribers API from Kit — 7 operation(s) for subscribers.
  name: Kit Subscribers API
  phrasing_intents:
  - id: postV4BulkSubscribers
    intent: Create many subscribers at once
    question: Can I import thousands of subscribers in one request?
  - id: getV4Subscribers
    intent: List and filter subscribers
    question: Which subscribers joined my list in the last month?
  - id: postV4Subscribers
    intent: Create or upsert a subscriber
    question: How do I add a new subscriber to my email list?
  - id: postV4SubscribersFilter
    intent: Filter subscribers by engagement
    question: Which subscribers opened or clicked my emails recently?
  - id: getV4SubscribersById
    intent: Get a subscriber
    question: Can I look up one subscriber's details by their id?
  - id: putV4SubscribersById
    intent: Update a subscriber's details
    question: How do I change an existing subscriber's email address or first name?
  - id: postV4SubscribersByIdUnsubscribe
    intent: Unsubscribe a subscriber
    question: How do I unsubscribe someone from all my emails?
  - id: getV4SubscribersBySubscriberIdStats
    intent: Get email stats for one subscriber
    question: How engaged is a specific subscriber with my emails?
  phrasing_ops: 9
  slug: convertkit-subscribers-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Tags API from Kit — 6 operation(s) for tags.
  name: Kit Tags API
  phrasing_intents:
  - id: postV4BulkTags
    intent: Create many tags at once
    question: Can I create a whole batch of new tags in one request?
  - id: deleteV4BulkTagsSubscribers
    intent: Remove tags from many subscribers at once
    question: Can I strip tags from a large batch of subscribers in one request?
  - id: postV4BulkTagsSubscribers
    intent: Tag many subscribers at once
    question: How do I apply tags to thousands of subscribers in one go?
  - id: getV4Tags
    intent: List tags
    question: What tags have I created for organizing subscribers?
  - id: postV4Tags
    intent: Create a tag
    question: How do I create a new tag for segmenting subscribers?
  - id: putV4TagsById
    intent: Rename a tag
    question: Can I rename an existing tag without re-tagging everyone?
  - id: deleteV4TagsByTagIdSubscribers
    intent: Remove a tag from a subscriber by email
    question: How do I untag a subscriber using their email address rather than their id?
  - id: getV4TagsByTagIdSubscribers
    intent: List subscribers with a tag
    question: Who has a particular tag applied?
  phrasing_ops: 11
  slug: convertkit-tags-api
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: The Webhooks API from Kit — 2 operation(s) for webhooks.
  name: Kit Webhooks API
  phrasing_intents:
  - id: getV4Webhooks
    intent: List webhooks
    question: Which webhooks are currently set up on my account?
  - id: postV4Webhooks
    intent: Create a webhook for a subscriber event
    question: How do I get notified at my server when someone unsubscribes?
  - id: deleteV4WebhooksById
    intent: Delete a webhook
    question: How do I stop a webhook from sending events to my server?
  phrasing_ops: 3
  slug: convertkit-webhooks-api
- description: The legacy ConvertKit V3 API is deprecated and slated for discontinuation; new integrations should target V4.
  name: Kit API V3 (Deprecated)
  slug: kit-api-v3
- baseURL: https://api.kit.com/v4
  baseurl_source: declared
  description: Account, creator profile, and account-level statistics
  name: Kit Account API
  phrasing_intents:
  - id: getAccount
    intent: View my Kit account and user details
    question: Which Kit account and user does my API key belong to?
  - id: getAccountColors
    intent: List the account's saved brand colors
    question: What color preferences are saved on my email marketing account?
  - id: updateAccountColors
    intent: Update the account's brand colors
    question: How do I change the saved brand colors on my account?
  - id: getAccountEmailStats
    intent: Get email performance stats for the last 90 days
    question: How have my emails performed over the last 90 days?
  - id: getAccountGrowthStats
    intent: Get subscriber growth for a date range
    question: How many subscribers did I gain or lose over a given period?
  phrasing_ops: 5
  slug: convertkit-account-api
artifact_total: 227
asyncapis:
- description: ''
  name: Convertkit Webhooks
  slug: convertkit-webhooks
- description: AsyncAPI 2.6 description of the Kit (formerly ConvertKit) webhook surface. Kit delivers webhook notifications via HTTP `POST` requests with a JSON body to a `target_url` registered through the Kit API
  name: Kit Webhooks
  slug: kit-webhooks-asyncapi
collections:
- collection_type: open
  name: Kit Accounts API
  slug: open-convertkit-accounts-api
- collection_type: open
  name: Kit Accounts Broadcasts API
  slug: open-convertkit-broadcasts-api
- collection_type: open
  name: Kit Accounts Custom Fields API
  slug: open-convertkit-custom-fields-api
- collection_type: open
  name: Kit Accounts Email Templates API
  slug: open-convertkit-email-templates-api
- collection_type: open
  name: Kit Accounts Forms API
  slug: open-convertkit-forms-api
- collection_type: open
  name: Kit Accounts Posts API
  slug: open-convertkit-posts-api
- collection_type: open
  name: Kit Accounts Purchases API
  slug: open-convertkit-purchases-api
- collection_type: open
  name: Kit Accounts Segments API
  slug: open-convertkit-segments-api
- collection_type: open
  name: Kit Accounts Sequence Emails API
  slug: open-convertkit-sequence-emails-api
- collection_type: open
  name: Kit Accounts Sequences API
  slug: open-convertkit-sequences-api
- collection_type: open
  name: Kit Accounts Snippets API
  slug: open-convertkit-snippets-api
- collection_type: open
  name: Kit Accounts Subscribers API
  slug: open-convertkit-subscribers-api
- collection_type: open
  name: Kit Accounts Tags API
  slug: open-convertkit-tags-api
- collection_type: open
  name: Kit Accounts Webhooks API
  slug: open-convertkit-webhooks-api
common:
- group: design
  href: https://artifacts.apis.io/convertkit/rules/convertkit-rules.yml
  title: ''
  type: Spectral
  url: rules/convertkit-rules.yml
- group: design
  href: https://artifacts.apis.io/convertkit/rules/convertkit-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/convertkit-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/convertkit/json-ld/convertkit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/convertkit-context.jsonld
- group: design
  href: https://artifacts.apis.io/convertkit/vocabulary/convertkit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/convertkit-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/convertkit/asyncapi/kit-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/kit-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/convertkit/conventions/convertkit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/convertkit-conventions.yml
- group: other
  href: https://artifacts.apis.io/convertkit/hosts/convertkit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/convertkit-hosts.yml
- group: build
  href: https://artifacts.apis.io/convertkit/integrations/convertkit-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/convertkit-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/convertkit/vendors/convertkit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/convertkit-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://kit.com/news
- group: other
  href: https://artifacts.apis.io/convertkit/capabilities/convertkit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/convertkit-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/convertkit/agentic-access/convertkit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/convertkit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/convertkit/security/convertkit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/convertkit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/convertkit/security/convertkit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/convertkit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/convertkit/security/convertkit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convertkit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/convertkit/authentication/convertkit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/convertkit-authentication.yml
- group: auth
  href: https://artifacts.apis.io/convertkit/scopes/convertkit-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/convertkit-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://kit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kit.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kit.com
- group: company
  title: ''
  type: Blog
  url: https://kit.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://kit.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kit.com
- group: other
  title: ''
  type: X
  url: https://x.com/kit
- group: commercial
  href: https://artifacts.apis.io/convertkit/plans/convertkit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/convertkit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/convertkit/rate-limits/convertkit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/convertkit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/convertkit/finops/convertkit-finops.yml
  title: ''
  type: FinOps
  url: finops/convertkit-finops.yml
- group: other
  href: https://artifacts.apis.io/convertkit/a2a/convertkit-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/convertkit-a2a.yml
- group: agent
  href: https://artifacts.apis.io/convertkit/well-known/convertkit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/convertkit-well-known.yml
- group: agent
  href: https://artifacts.apis.io/convertkit/mcp/convertkit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/convertkit-mcp.yml
- group: build
  href: https://artifacts.apis.io/convertkit/mcp/convertkit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/convertkit-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/convertkit/llms/convertkit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/convertkit-llms.txt
- group: build
  href: https://artifacts.apis.io/convertkit/packages/convertkit-packages.yml
  title: ''
  type: Packages
  url: packages/convertkit-packages.yml
- group: build
  href: https://artifacts.apis.io/convertkit/packages/convertkit-packages.yml
  title: ''
  type: SDKs
  url: packages/convertkit-packages.yml
- group: design
  href: https://artifacts.apis.io/convertkit/conventions/convertkit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/convertkit-conventions.yml
- group: design
  href: https://artifacts.apis.io/convertkit/errors/convertkit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/convertkit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/convertkit/lifecycle/convertkit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/convertkit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.kit.com/api-reference/upgrading-to-v4
- group: operate
  href: https://artifacts.apis.io/convertkit/changelog/convertkit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/convertkit-changelog.yml
- group: design
  href: https://artifacts.apis.io/convertkit/conformance/convertkit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/convertkit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kit.com/security
- group: auth
  title: ''
  type: Security
  url: https://kit.com/security
- group: design
  href: https://artifacts.apis.io/convertkit/asyncapi/convertkit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/convertkit-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/convertkit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/convertkit/components/convertkit-components.yml
  title: ''
  type: Components
  url: components/convertkit-components.yml
- group: design
  href: https://artifacts.apis.io/convertkit/data-model/convertkit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/convertkit-data-model.yml
- group: design
  href: https://artifacts.apis.io/convertkit/vocabulary/vocabulary.json
  title: ''
  type: Vocabulary
  url: vocabulary/vocabulary.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kit.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kit.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.kit.com/kit-app-store/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://kit.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.kit.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kit.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.kit.com/users/signup
- group: design
  href: https://artifacts.apis.io/convertkit/rules/convertkit-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/convertkit-jsonschema-spectral-rules.yml
- group: build
  href: https://artifacts.apis.io/convertkit/examples/add-subscriber-to-form-by-email-address.json
  title: ''
  type: Examples
  url: examples/add-subscriber-to-form-by-email-address.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/add-subscriber-to-form.json
  title: ''
  type: Examples
  url: examples/add-subscriber-to-form.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/add-subscriber-to-sequence-by-email-address.json
  title: ''
  type: Examples
  url: examples/add-subscriber-to-sequence-by-email-address.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/add-subscriber-to-sequence.json
  title: ''
  type: Examples
  url: examples/add-subscriber-to-sequence.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-add-subscribers-to-forms.json
  title: ''
  type: Examples
  url: examples/bulk-add-subscribers-to-forms.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-create-custom-fields.json
  title: ''
  type: Examples
  url: examples/bulk-create-custom-fields.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-create-subscribers.json
  title: ''
  type: Examples
  url: examples/bulk-create-subscribers.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-create-tags.json
  title: ''
  type: Examples
  url: examples/bulk-create-tags.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-remove-tags-from-subscribers.json
  title: ''
  type: Examples
  url: examples/bulk-remove-tags-from-subscribers.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-tag-subscribers.json
  title: ''
  type: Examples
  url: examples/bulk-tag-subscribers.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/bulk-update-subscriber-custom-field-values.json
  title: ''
  type: Examples
  url: examples/bulk-update-subscriber-custom-field-values.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-broadcast.json
  title: ''
  type: Examples
  url: examples/create-a-broadcast.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-custom-field.json
  title: ''
  type: Examples
  url: examples/create-a-custom-field.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-purchase.json
  title: ''
  type: Examples
  url: examples/create-a-purchase.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-sequence-email.json
  title: ''
  type: Examples
  url: examples/create-a-sequence-email.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-sequence.json
  title: ''
  type: Examples
  url: examples/create-a-sequence.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-snippet.json
  title: ''
  type: Examples
  url: examples/create-a-snippet.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-subscriber.json
  title: ''
  type: Examples
  url: examples/create-a-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-tag.json
  title: ''
  type: Examples
  url: examples/create-a-tag.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/create-a-webhook.json
  title: ''
  type: Examples
  url: examples/create-a-webhook.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/delete-a-broadcast.json
  title: ''
  type: Examples
  url: examples/delete-a-broadcast.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/delete-a-sequence-email.json
  title: ''
  type: Examples
  url: examples/delete-a-sequence-email.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/delete-a-sequence.json
  title: ''
  type: Examples
  url: examples/delete-a-sequence.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/delete-a-webhook.json
  title: ''
  type: Examples
  url: examples/delete-a-webhook.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/delete-custom-field.json
  title: ''
  type: Examples
  url: examples/delete-custom-field.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/filter-subscribers-based-on-engagement.json
  title: ''
  type: Examples
  url: examples/filter-subscribers-based-on-engagement.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-broadcast.json
  title: ''
  type: Examples
  url: examples/get-a-broadcast.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-post.json
  title: ''
  type: Examples
  url: examples/get-a-post.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-purchase.json
  title: ''
  type: Examples
  url: examples/get-a-purchase.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-sequence-email.json
  title: ''
  type: Examples
  url: examples/get-a-sequence-email.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-sequence.json
  title: ''
  type: Examples
  url: examples/get-a-sequence.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-snippet.json
  title: ''
  type: Examples
  url: examples/get-a-snippet.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-a-subscriber.json
  title: ''
  type: Examples
  url: examples/get-a-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-creator-profile.json
  title: ''
  type: Examples
  url: examples/get-creator-profile.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-current-account.json
  title: ''
  type: Examples
  url: examples/get-current-account.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-email-stats.json
  title: ''
  type: Examples
  url: examples/get-email-stats.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-growth-stats.json
  title: ''
  type: Examples
  url: examples/get-growth-stats.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-link-clicks-for-a-broadcast.json
  title: ''
  type: Examples
  url: examples/get-link-clicks-for-a-broadcast.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-stats-for-a-broadcast.json
  title: ''
  type: Examples
  url: examples/get-stats-for-a-broadcast.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/get-stats-for-a-list-of-broadcasts.json
  title: ''
  type: Examples
  url: examples/get-stats-for-a-list-of-broadcasts.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-broadcasts.json
  title: ''
  type: Examples
  url: examples/list-broadcasts.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-colors.json
  title: ''
  type: Examples
  url: examples/list-colors.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-custom-fields.json
  title: ''
  type: Examples
  url: examples/list-custom-fields.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-email-templates.json
  title: ''
  type: Examples
  url: examples/list-email-templates.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-forms.json
  title: ''
  type: Examples
  url: examples/list-forms.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-posts.json
  title: ''
  type: Examples
  url: examples/list-posts.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-purchases.json
  title: ''
  type: Examples
  url: examples/list-purchases.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-segments.json
  title: ''
  type: Examples
  url: examples/list-segments.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-sequence-emails.json
  title: ''
  type: Examples
  url: examples/list-sequence-emails.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-sequences.json
  title: ''
  type: Examples
  url: examples/list-sequences.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-snippets.json
  title: ''
  type: Examples
  url: examples/list-snippets.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-stats-for-a-subscriber.json
  title: ''
  type: Examples
  url: examples/list-stats-for-a-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-subscribers-for-a-form.json
  title: ''
  type: Examples
  url: examples/list-subscribers-for-a-form.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-subscribers-for-a-sequence.json
  title: ''
  type: Examples
  url: examples/list-subscribers-for-a-sequence.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-subscribers-for-a-tag.json
  title: ''
  type: Examples
  url: examples/list-subscribers-for-a-tag.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-subscribers.json
  title: ''
  type: Examples
  url: examples/list-subscribers.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-tags-for-a-subscriber.json
  title: ''
  type: Examples
  url: examples/list-tags-for-a-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-tags.json
  title: ''
  type: Examples
  url: examples/list-tags.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/list-webhooks.json
  title: ''
  type: Examples
  url: examples/list-webhooks.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/remove-tag-from-subscriber-by-email-address.json
  title: ''
  type: Examples
  url: examples/remove-tag-from-subscriber-by-email-address.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/remove-tag-from-subscriber.json
  title: ''
  type: Examples
  url: examples/remove-tag-from-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/tag-a-subscriber-by-email-address.json
  title: ''
  type: Examples
  url: examples/tag-a-subscriber-by-email-address.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/tag-a-subscriber.json
  title: ''
  type: Examples
  url: examples/tag-a-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/unsubscribe-subscriber.json
  title: ''
  type: Examples
  url: examples/unsubscribe-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-a-broadcast.json
  title: ''
  type: Examples
  url: examples/update-a-broadcast.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-a-custom-field.json
  title: ''
  type: Examples
  url: examples/update-a-custom-field.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-a-sequence-email.json
  title: ''
  type: Examples
  url: examples/update-a-sequence-email.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-a-sequence.json
  title: ''
  type: Examples
  url: examples/update-a-sequence.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-a-snippet.json
  title: ''
  type: Examples
  url: examples/update-a-snippet.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-a-subscriber.json
  title: ''
  type: Examples
  url: examples/update-a-subscriber.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-colors.json
  title: ''
  type: Examples
  url: examples/update-colors.json
- group: build
  href: https://artifacts.apis.io/convertkit/examples/update-tag-name.json
  title: ''
  type: Examples
  url: examples/update-tag-name.json
- group: design
  href: https://artifacts.apis.io/convertkit/json-ld/api.json
  title: ''
  type: JSONLD
  url: json-ld/api.json
- group: design
  href: https://artifacts.apis.io/convertkit/json-ld/context.json
  title: ''
  type: JSONLDContext
  url: json-ld/context.json
- group: operate
  title: ''
  type: Contact
  url: mailto:help@kit.com
created: '2026-06-13'
description: Kit (formerly ConvertKit) is a creator email marketing platform whose REST API v4 covers subscribers, tags, custom fields, forms and landing pages, sequences, broadcasts, snippets, posts, purchases, segments and webhooks across 72 operations on https://api.kit.com/v4. It authenticates with an X-Kit-Api-Key header for personal automation or OAuth 2.0 (PKCE, dynamic client registration, rotating single-use refresh tokens) for apps published to the Kit App Store, and uses cursor-based pagination, an OAuth-only bulk namespace with async callbacks, and eventually-consistent list reads. Kit also runs two remote MCP servers - an OAuth-gated one that acts on a creator's account and an anonymous read-only documentation server - publishes an A2A agent card and an Agent Skill from its developer docs host, and ships llms.txt. Its only first-party API client is a PHP SDK.
examples:
- key_count: 6
  name: Add Subscriber To Form By Email Address
  slug: add-subscriber-to-form-by-email-address
- key_count: 6
  name: Add Subscriber To Form
  slug: add-subscriber-to-form
- key_count: 6
  name: Add Subscriber To Sequence By Email Address
  slug: add-subscriber-to-sequence-by-email-address
- key_count: 5
  name: Add Subscriber To Sequence
  slug: add-subscriber-to-sequence
- key_count: 6
  name: Bulk Add Subscribers To Forms
  slug: bulk-add-subscribers-to-forms
- key_count: 6
  name: Bulk Create Custom Fields
  slug: bulk-create-custom-fields
- key_count: 6
  name: Bulk Create Subscribers
  slug: bulk-create-subscribers
- key_count: 6
  name: Bulk Create Tags
  slug: bulk-create-tags
- key_count: 5
  name: Bulk Remove Tags From Subscribers
  slug: bulk-remove-tags-from-subscribers
- key_count: 6
  name: Bulk Tag Subscribers
  slug: bulk-tag-subscribers
- key_count: 6
  name: Bulk Update Subscriber Custom Field Values
  slug: bulk-update-subscriber-custom-field-values
- key_count: 6
  name: Create A Broadcast
  slug: create-a-broadcast
- key_count: 6
  name: Create A Custom Field
  slug: create-a-custom-field
- key_count: 6
  name: Create A Purchase
  slug: create-a-purchase
- key_count: 6
  name: Create A Sequence Email
  slug: create-a-sequence-email
- key_count: 6
  name: Create A Sequence
  slug: create-a-sequence
- key_count: 5
  name: Create A Snippet
  slug: create-a-snippet
- key_count: 6
  name: Create A Subscriber
  slug: create-a-subscriber
- key_count: 6
  name: Create A Tag
  slug: create-a-tag
- key_count: 6
  name: Create A Webhook
  slug: create-a-webhook
- key_count: 4
  name: Delete A Broadcast
  slug: delete-a-broadcast
- key_count: 4
  name: Delete A Sequence Email
  slug: delete-a-sequence-email
- key_count: 4
  name: Delete A Sequence
  slug: delete-a-sequence
- key_count: 4
  name: Delete A Webhook
  slug: delete-a-webhook
- key_count: 4
  name: Delete Custom Field
  slug: delete-custom-field
- key_count: 5
  name: Filter Subscribers Based On Engagement
  slug: filter-subscribers-based-on-engagement
- key_count: 5
  name: Get A Broadcast
  slug: get-a-broadcast
- key_count: 5
  name: Get A Post
  slug: get-a-post
- key_count: 5
  name: Get A Purchase
  slug: get-a-purchase
- key_count: 5
  name: Get A Sequence Email
  slug: get-a-sequence-email
- key_count: 5
  name: Get A Sequence
  slug: get-a-sequence
- key_count: 5
  name: Get A Snippet
  slug: get-a-snippet
- key_count: 5
  name: Get A Subscriber
  slug: get-a-subscriber
- key_count: 5
  name: Get Creator Profile
  slug: get-creator-profile
- key_count: 5
  name: Get Current Account
  slug: get-current-account
- key_count: 5
  name: Get Email Stats
  slug: get-email-stats
- key_count: 5
  name: Get Growth Stats
  slug: get-growth-stats
- key_count: 5
  name: Get Link Clicks For A Broadcast
  slug: get-link-clicks-for-a-broadcast
- key_count: 5
  name: Get Stats For A Broadcast
  slug: get-stats-for-a-broadcast
- key_count: 5
  name: Get Stats For A List Of Broadcasts
  slug: get-stats-for-a-list-of-broadcasts
- key_count: 5
  name: List Broadcasts
  slug: list-broadcasts
- key_count: 5
  name: List Colors
  slug: list-colors
- key_count: 5
  name: List Custom Fields
  slug: list-custom-fields
- key_count: 5
  name: List Email Templates
  slug: list-email-templates
- key_count: 5
  name: List Forms
  slug: list-forms
- key_count: 5
  name: List Posts
  slug: list-posts
- key_count: 5
  name: List Purchases
  slug: list-purchases
- key_count: 5
  name: List Segments
  slug: list-segments
- key_count: 5
  name: List Sequence Emails
  slug: list-sequence-emails
- key_count: 5
  name: List Sequences
  slug: list-sequences
- key_count: 5
  name: List Snippets
  slug: list-snippets
- key_count: 5
  name: List Stats For A Subscriber
  slug: list-stats-for-a-subscriber
- key_count: 5
  name: List Subscribers For A Form
  slug: list-subscribers-for-a-form
- key_count: 5
  name: List Subscribers For A Sequence
  slug: list-subscribers-for-a-sequence
- key_count: 5
  name: List Subscribers For A Tag
  slug: list-subscribers-for-a-tag
- key_count: 5
  name: List Subscribers
  slug: list-subscribers
- key_count: 5
  name: List Tags For A Subscriber
  slug: list-tags-for-a-subscriber
- key_count: 5
  name: List Tags
  slug: list-tags
- key_count: 5
  name: List Webhooks
  slug: list-webhooks
- key_count: 4
  name: Remove Tag From Subscriber By Email Address
  slug: remove-tag-from-subscriber-by-email-address
- key_count: 4
  name: Remove Tag From Subscriber
  slug: remove-tag-from-subscriber
- key_count: 6
  name: Tag A Subscriber By Email Address
  slug: tag-a-subscriber-by-email-address
- key_count: 5
  name: Tag A Subscriber
  slug: tag-a-subscriber
- key_count: 4
  name: Unsubscribe Subscriber
  slug: unsubscribe-subscriber
- key_count: 6
  name: Update A Broadcast
  slug: update-a-broadcast
- key_count: 6
  name: Update A Custom Field
  slug: update-a-custom-field
- key_count: 6
  name: Update A Sequence Email
  slug: update-a-sequence-email
- key_count: 6
  name: Update A Sequence
  slug: update-a-sequence
- key_count: 5
  name: Update A Snippet
  slug: update-a-snippet
- key_count: 6
  name: Update A Subscriber
  slug: update-a-subscriber
- key_count: 6
  name: Update Colors
  slug: update-colors
- key_count: 6
  name: Update Tag Name
  slug: update-tag-name
finops:
- has_sources: true
  method: derived
  name: Convertkit Finops
  primary_unit: ''
  service_category: ''
  slug: convertkit-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convertkit.png
json_schemas:
- name: BroadcastAnyCondition
  property_count: 2
  slug: BroadcastAnyCondition
- name: FilterCondition
  property_count: 9
  slug: FilterCondition
- name: FormsAnyCondition
  property_count: 2
  slug: FormsAnyCondition
- name: IdsAnyCondition
  property_count: 2
  slug: IdsAnyCondition
- name: SubscriberFilterRequest
  property_count: 2
  slug: SubscriberFilterRequest
- name: UrlAnyCondition
  property_count: 4
  slug: UrlAnyCondition
- name: Add subscriber to form by email address Request
  property_count: 2
  slug: add_subscriber_to_form_by_email_address_request
- name: Add subscriber to form by email address Response
  property_count: 1
  slug: add_subscriber_to_form_by_email_address_response
- name: Add subscriber to form Request
  property_count: 1
  slug: add_subscriber_to_form_request
- name: Add subscriber to form Response
  property_count: 1
  slug: add_subscriber_to_form_response
- name: Add subscriber to sequence by email address Request
  property_count: 1
  slug: add_subscriber_to_sequence_by_email_address_request
- name: Add subscriber to sequence by email address Response
  property_count: 1
  slug: add_subscriber_to_sequence_by_email_address_response
- name: Add subscriber to sequence Request
  property_count: 0
  slug: add_subscriber_to_sequence_request
- name: Add subscriber to sequence Response
  property_count: 1
  slug: add_subscriber_to_sequence_response
- name: Bulk add subscribers to forms Request
  property_count: 2
  slug: bulk_add_subscribers_to_forms_request
- name: Bulk add subscribers to forms Response
  property_count: 2
  slug: bulk_add_subscribers_to_forms_response
- name: Bulk create custom fields Request
  property_count: 2
  slug: bulk_create_custom_fields_request
- name: Bulk create custom fields Response
  property_count: 2
  slug: bulk_create_custom_fields_response
- name: Bulk create subscribers Request
  property_count: 2
  slug: bulk_create_subscribers_request
- name: Bulk create subscribers Response
  property_count: 2
  slug: bulk_create_subscribers_response
- name: Bulk create tags Request
  property_count: 2
  slug: bulk_create_tags_request
- name: Bulk create tags Response
  property_count: 2
  slug: bulk_create_tags_response
- name: Bulk remove tags from subscribers Response
  property_count: 1
  slug: bulk_remove_tags_from_subscribers_response
- name: Bulk tag subscribers Request
  property_count: 2
  slug: bulk_tag_subscribers_request
- name: Bulk tag subscribers Response
  property_count: 2
  slug: bulk_tag_subscribers_response
- name: Bulk update subscriber custom field values Request
  property_count: 2
  slug: bulk_update_subscriber_custom_field_values_request
- name: Bulk update subscriber custom field values Response
  property_count: 2
  slug: bulk_update_subscriber_custom_field_values_response
- name: AccountResponse
  property_count: 1
  slug: convertkit-account-response
- name: ColorsRequest
  property_count: 1
  slug: convertkit-colors-request
- name: ColorsResponse
  property_count: 1
  slug: convertkit-colors-response
- name: StatsResponse
  property_count: 1
  slug: convertkit-stats-response
- name: SubscriberFilterRequest
  property_count: 2
  slug: convertkit-subscriber-filter-request
- name: Create a broadcast Request
  property_count: 12
  slug: create_a_broadcast_request
- name: Create a broadcast Response
  property_count: 1
  slug: create_a_broadcast_response
- name: Create a custom field Request
  property_count: 1
  slug: create_a_custom_field_request
- name: Create a custom field Response
  property_count: 1
  slug: create_a_custom_field_response
- name: Create a purchase Request
  property_count: 1
  slug: create_a_purchase_request
- name: Create a purchase Response
  property_count: 1
  slug: create_a_purchase_response
- name: Create a sequence email Request
  property_count: 9
  slug: create_a_sequence_email_request
- name: Create a sequence email Response
  property_count: 1
  slug: create_a_sequence_email_response
- name: Create a sequence Request
  property_count: 10
  slug: create_a_sequence_request
- name: Create a sequence Response
  property_count: 1
  slug: create_a_sequence_response
- name: Create a snippet Request
  property_count: 0
  slug: create_a_snippet_request
- name: Create a snippet Response
  property_count: 1
  slug: create_a_snippet_response
- name: Create a subscriber Request
  property_count: 4
  slug: create_a_subscriber_request
- name: Create a subscriber Response
  property_count: 2
  slug: create_a_subscriber_response
- name: Create a tag Request
  property_count: 1
  slug: create_a_tag_request
- name: Create a tag Response
  property_count: 1
  slug: create_a_tag_response
- name: Create a webhook Request
  property_count: 2
  slug: create_a_webhook_request
- name: Create a webhook Response
  property_count: 1
  slug: create_a_webhook_response
- name: Filter subscribers based on engagement Response
  property_count: 2
  slug: filter_subscribers_based_on_engagement_response
- name: Get a broadcast Response
  property_count: 1
  slug: get_a_broadcast_response
- name: Get a post Response
  property_count: 1
  slug: get_a_post_response
- name: Get a purchase Response
  property_count: 1
  slug: get_a_purchase_response
- name: Get a sequence email Response
  property_count: 1
  slug: get_a_sequence_email_response
- name: Get a sequence Response
  property_count: 1
  slug: get_a_sequence_response
- name: Get a snippet Response
  property_count: 1
  slug: get_a_snippet_response
- name: Get a subscriber Response
  property_count: 1
  slug: get_a_subscriber_response
- name: Get Creator Profile Response
  property_count: 1
  slug: get_creator_profile_response
- name: Get current account Response
  property_count: 2
  slug: get_current_account_response
- name: Get email stats Response
  property_count: 1
  slug: get_email_stats_response
- name: Get growth stats Response
  property_count: 1
  slug: get_growth_stats_response
- name: Get link clicks for a broadcast Response
  property_count: 2
  slug: get_link_clicks_for_a_broadcast_response
- name: Get stats for a broadcast Response
  property_count: 1
  slug: get_stats_for_a_broadcast_response
- name: Get stats for a list of broadcasts Response
  property_count: 2
  slug: get_stats_for_a_list_of_broadcasts_response
- name: List broadcasts Response
  property_count: 2
  slug: list_broadcasts_response
- name: List colors Response
  property_count: 1
  slug: list_colors_response
- name: List custom fields Response
  property_count: 2
  slug: list_custom_fields_response
- name: List email templates Response
  property_count: 2
  slug: list_email_templates_response
- name: List forms Response
  property_count: 2
  slug: list_forms_response
- name: List posts Response
  property_count: 2
  slug: list_posts_response
- name: List purchases Response
  property_count: 2
  slug: list_purchases_response
- name: List segments Response
  property_count: 2
  slug: list_segments_response
- name: List sequence emails Response
  property_count: 2
  slug: list_sequence_emails_response
- name: List sequences Response
  property_count: 2
  slug: list_sequences_response
- name: List snippets Response
  property_count: 2
  slug: list_snippets_response
- name: List stats for a subscriber Response
  property_count: 1
  slug: list_stats_for_a_subscriber_response
- name: List subscribers for a form Response
  property_count: 2
  slug: list_subscribers_for_a_form_response
- name: List subscribers for a sequence Response
  property_count: 2
  slug: list_subscribers_for_a_sequence_response
- name: List subscribers for a tag Response
  property_count: 2
  slug: list_subscribers_for_a_tag_response
- name: List subscribers Response
  property_count: 2
  slug: list_subscribers_response
- name: List tags for a subscriber Response
  property_count: 2
  slug: list_tags_for_a_subscriber_response
- name: List tags Response
  property_count: 2
  slug: list_tags_response
- name: List webhooks Response
  property_count: 2
  slug: list_webhooks_response
- name: Tag a subscriber by email address Request
  property_count: 1
  slug: tag_a_subscriber_by_email_address_request
- name: Tag a subscriber by email address Response
  property_count: 1
  slug: tag_a_subscriber_by_email_address_response
- name: Tag a subscriber Request
  property_count: 0
  slug: tag_a_subscriber_request
- name: Tag a subscriber Response
  property_count: 1
  slug: tag_a_subscriber_response
- name: Unsubscribe subscriber Request
  property_count: 0
  slug: unsubscribe_subscriber_request
- name: Update a broadcast Request
  property_count: 12
  slug: update_a_broadcast_request
- name: Update a broadcast Response
  property_count: 1
  slug: update_a_broadcast_response
- name: Update a custom field Request
  property_count: 1
  slug: update_a_custom_field_request
- name: Update a custom field Response
  property_count: 1
  slug: update_a_custom_field_response
- name: Update a sequence email Request
  property_count: 9
  slug: update_a_sequence_email_request
- name: Update a sequence email Response
  property_count: 1
  slug: update_a_sequence_email_response
- name: Update a sequence Request
  property_count: 10
  slug: update_a_sequence_request
- name: Update a sequence Response
  property_count: 1
  slug: update_a_sequence_response
- name: Update a snippet Request
  property_count: 0
  slug: update_a_snippet_request
- name: Update a snippet Response
  property_count: 1
  slug: update_a_snippet_response
- name: Update a subscriber Request
  property_count: 3
  slug: update_a_subscriber_request
- name: Update a subscriber Response
  property_count: 2
  slug: update_a_subscriber_response
- name: Update colors Request
  property_count: 1
  slug: update_colors_request
- name: Update colors Response
  property_count: 1
  slug: update_colors_response
- name: Update tag name Request
  property_count: 1
  slug: update_tag_name_request
- name: Update tag name Response
  property_count: 1
  slug: update_tag_name_response
jsonld:
- class_count: 12
  name: Convertkit Context
  property_count: 21
  slug: convertkit-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.kit.com requiring OAuth; 3 tools listed.
  name: Kit MCP Server
  slug: convertkit-mcp-yml
modified: '2026-08-13'
name: Kit
nav: Providers
network: true
overview: 'Kit publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Custom Fields API, and 13 more. Tagged areas include Email Marketing, Creator Economy, Subscribers, Automation, and Newsletters.


  The Kit catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Kit''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 125 more developer resources.'
plans:
- name: Convertkit Plans Pricing
  plan_count: 3
  slug: convertkit-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Convertkit Rate Limits
  slug: convertkit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Kit — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: convertkit-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Kit API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: convertkit-rules
scopes:
- name: Convertkit Scopes
  scope_count: 3
  slug: convertkit-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 79.6
  coverage:
    artifact_dirs: 38
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 76.4
    developer_ergonomics: 71.4
    discoverability: 75.8
    operational_transparency: 92.1
  previous_composite: 79.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/convertkit/convertkit-2026-06-20T175000.png
security:
- kind: authentication
  name: Convertkit Authentication
  slug: convertkit-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Convertkit Domain Security
  slug: convertkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Convertkit Vulnerability Disclosure
  slug: convertkit-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Convertkit Trust Center
  slug: convertkit-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
skill_count: 5
skills:
- name: draft-target-and-send-a-kit-broadcast
  slug: convertkit-broadcast-send
- name: bulk-import-subscribers-and-tags-into-kit
  slug: convertkit-bulk-import
- name: kit-provider
  slug: convertkit-kit-provider-skill
- name: onboard-a-subscriber-into-kit
  slug: convertkit-subscriber-onboarding
- name: subscribe-to-kit-events-with-webhooks
  slug: convertkit-webhook-subscriptions
slug: convertkit
tags:
- Email Marketing
- Creator Economy
- Subscribers
- Automation
- Newsletters
- Sequences
- Forms
- Broadcast
- Webhook
- MCP
- Agents
- Authentication
- Marketing Automation
- Landing Pages
- Segmentation
- Email Campaigns
- Software-as-a-Service
- Commerce
- A2A
- Email
website: https://kit.com
---
