---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Convertkit Agentic Access
  operation_count: 72
  slug: convertkit-agentic-access
  summary_line: 72 operations · 39 acting
api_count: 14
apis:
- description: The Accounts API from Kit — 5 operation(s) for accounts.
  name: Kit Accounts API
  slug: convertkit-accounts-api
- description: The Broadcasts API from Kit — 5 operation(s) for broadcasts.
  name: Kit Broadcasts API
  slug: convertkit-broadcasts-api
- description: The Custom Fields API from Kit — 4 operation(s) for custom fields.
  name: Kit Custom Fields API
  slug: convertkit-custom-fields-api
- description: The Email Templates API from Kit — 1 operation(s) for email templates.
  name: Kit Email Templates API
  slug: convertkit-email-templates-api
- description: The Forms API from Kit — 4 operation(s) for forms.
  name: Kit Forms API
  slug: convertkit-forms-api
- description: The Posts API from Kit — 2 operation(s) for posts.
  name: Kit Posts API
  slug: convertkit-posts-api
- description: The Purchases API from Kit — 2 operation(s) for purchases.
  name: Kit Purchases API
  slug: convertkit-purchases-api
- description: The Segments API from Kit — 1 operation(s) for segments.
  name: Kit Segments API
  slug: convertkit-segments-api
- description: The Sequence Emails API from Kit — 2 operation(s) for sequence emails.
  name: Kit Sequence Emails API
  slug: convertkit-sequence-emails-api
- description: The Sequences API from Kit — 4 operation(s) for sequences.
  name: Kit Sequences API
  slug: convertkit-sequences-api
- description: The Snippets API from Kit — 2 operation(s) for snippets.
  name: Kit Snippets API
  slug: convertkit-snippets-api
- description: The Subscribers API from Kit — 7 operation(s) for subscribers.
  name: Kit Subscribers API
  slug: convertkit-subscribers-api
- description: The Tags API from Kit — 6 operation(s) for tags.
  name: Kit Tags API
  slug: convertkit-tags-api
- description: The Webhooks API from Kit — 2 operation(s) for webhooks.
  name: Kit Webhooks API
  slug: convertkit-webhooks-api
artifact_total: 197
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convertkit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/convertkit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/convertkit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convertkit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convertkit-authentication.yml
- group: auth
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
  type: GitHubOrg
  url: https://github.com/convertkit
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
  title: ''
  type: Plans
  url: plans/convertkit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/convertkit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/convertkit-finops.yml
created: '2026-06-13'
description: Kit (formerly ConvertKit) is a creator email marketing platform with a REST API for managing subscribers, tags, sequences, forms, broadcasts, and automation rules. The API supports both API key and OAuth 2.0 authentication, with v4 as the current version featuring cursor-based pagination, bulk operations, and async processing.
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
- name: Convertkit Finops
  service_category: ''
  slug: convertkit-finops
graphqls:
- description: Kit (formerly ConvertKit) is a creator email marketing platform. This conceptual GraphQL schema wraps the Kit REST API v4, providing queries for subscribers, tags, sequences, forms, broadcasts, and au
  name: Kit (ConvertKit) GraphQL API
  slug: convertkit-graphql
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
layout: provider
modified: '2026-06-13'
name: Kit
nav: Providers
network: true
overview: 'Kit publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Custom Fields API, and 11 more. Tagged areas include Email Marketing, Creator Economy, Subscribers, Automation, and Newsletters.


  The Kit catalog on APIs.io includes 1 Spectral governance ruleset.


  Kit''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Convertkit Plans Pricing
  plan_count: 3
  slug: convertkit-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Convertkit Rate Limits
  slug: convertkit-rate-limits
rules:
- name: Kit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: convertkit-jsonschema-spectral-rules
scopes:
- name: Convertkit Scopes
  scope_count: 2
  slug: convertkit-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  delta: -2.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 58.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convertkit/refs/heads/main/screenshots/convertkit-2026-06-20T175000.png
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
slug: convertkit
tags:
- Email Marketing
- Creator Economy
- Subscribers
- Automation
- Newsletters
- Sequences
- Forms
- Broadcasts
website: https://kit.com
---
