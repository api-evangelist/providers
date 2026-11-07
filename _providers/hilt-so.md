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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Hosted MCP server at https://api.hilt.so/mcp (streamable HTTP, protocol 2025-06-18, server Hilt Pay Agent Gateway 1.1.0) exposing nine tools: free offer/catalog/pricing/quote/sandbox-bootstrap tools a'
  name: Hilt Pay Agent Gateway (MCP + A2A)
  slug: agent-gateway
- description: 'OAuth-gated remote MCP resource at https://api.hilt.so/mcp/pay-me for compatible AI clients: resolve a verified PayMe handle, start a wallet-approved SOL or Solana USDC payment (the client prepares te'
  name: Hilt PayMe MCP Connector
  slug: payme-mcp
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The account API from Hilt — 7 operation(s) for account.
  name: Hilt Account API
  phrasing_intents:
  - id: get_me_v1_account_me_get
    intent: Get my full merchant profile
    question: Where can I load everything about my signed-in Hilt profile at once?
  - id: update_me_v1_account_me_patch
    intent: Update my profile settings
    question: Can I change my display name or timezone on my merchant profile?
  - id: get_account_summary_v1_account_summary_get
    intent: Get my merchant dashboard summary
    question: What are my totals so far, split by USDC and SOL?
  - id: get_account_analytics_v1_account_analytics_get
    intent: View account analytics over a date range
    question: Can I see my account analytics between two dates?
  - id: update_account_security_v1_account_me_security_patch
    intent: Change my sign-in email or password
    question: How do I change the password I use to sign in to hilt.so?
  - id: get_delivery_readiness_v1_account_delivery_readiness_get
    intent: Check delivery setup readiness
    question: Is my account ready to deliver access to buyers after they pay?
  - id: run_delivery_test_v1_account_delivery_test_post
    intent: Run a delivery test for a provider
    question: Can I test that access delivery works before a real customer buys?
  - id: delete_account_v1_account_account_delete
    intent: Delete my merchant account
    question: How do I close and delete my Hilt account?
  phrasing_ops: 8
  slug: hilt-so-account-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The Agent Commerce API from Hilt — 4 operation(s) for agent commerce.
  name: Hilt Agent Commerce API
  phrasing_intents:
  - id: callHiltAgentGatewayMcp
    intent: Call the agent gateway over MCP
    question: Is there an MCP endpoint my agent can use for the catalog, quotes and plan activation?
  - id: getHiltA2aAgentCard
    intent: Get the A2A agent card
    question: Where is the A2A Agent Card for the Hilt Pay agent published?
  - id: getHiltA2aAgentCardLegacy
    intent: Get the A2A agent card from the legacy path
    question: My registry still looks for agent.json - is the card served there?
  - id: callHiltA2aAgent
    intent: Send a JSON-RPC message to the A2A agent
    question: How do I talk to the Hilt Pay agent over A2A JSON-RPC?
  phrasing_ops: 4
  slug: hilt-so-agent-commerce-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The api-keys API from Hilt — 2 operation(s) for api-keys.
  name: Hilt API Keys API
  phrasing_intents:
  - id: list_keys_v1_keys_get
    intent: List my API keys
    question: Which API keys have I created?
  - id: create_key_v1_keys_post
    intent: Create an API key
    question: How do I generate a new API key?
  - id: revoke_key_v1_keys__key_id__delete
    intent: Revoke an API key
    question: How do I permanently revoke a leaked API key?
  phrasing_ops: 3
  slug: hilt-so-api-keys-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The auth API from Hilt — 8 operation(s) for auth.
  name: Hilt Auth API
  phrasing_intents:
  - id: register_v1_auth_register_post
    intent: Register a new merchant account
    question: How do I sign up for a free Hilt merchant account?
  - id: login_v1_auth_login_post
    intent: Log in with email and password
    question: How do I get a JWT by logging in with my email and password?
  - id: wallet_auth_v1_auth_wallet_post
    intent: Sign in with a Phantom wallet
    question: Can I sign in with my Phantom wallet instead of an email?
  - id: oauth_provider_status_v1_auth_oauth_providers_get
    intent: List available OAuth sign-in providers
    question: Which social OAuth providers can I sign in with?
  - id: oauth_start_v1_auth_oauth__provider__start_get
    intent: Start an OAuth sign-in flow
    question: How do I begin signing in through an OAuth provider?
  - id: oauth_callback_v1_auth_oauth__provider__callback_get
    intent: Handle an OAuth provider callback
    question: What endpoint receives the authorization code when the OAuth provider redirects back?
  - id: logout_v1_auth_logout_post
    intent: Log out of the current session
    question: How do I log out of my session?
  - id: refresh_token_v1_auth_refresh_post
    intent: Refresh a session token
    question: Can I renew my JWT before it expires?
  phrasing_ops: 8
  slug: hilt-so-auth-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The billing API from Hilt — 5 operation(s) for billing.
  name: Hilt Billing API
  phrasing_intents:
  - id: get_billing_summary_v1_billing_summary_get
    intent: View my billing summary
    question: What plan am I on and what's my current billing status?
  - id: create_stripe_checkout_v1_billing_checkout_stripe_post
    intent: Start a Stripe checkout to upgrade my plan
    question: How do I pay for a paid Hilt plan by card through Stripe?
  - id: create_stripe_portal_v1_billing_portal_stripe_post
    intent: Open the Stripe billing portal
    question: Where do I update my card or cancel my subscription?
  - id: refresh_stripe_billing_v1_billing_refresh_stripe_post
    intent: Resync my billing from Stripe
    question: My plan change isn't showing - can I force a resync from Stripe?
  - id: stripe_webhook_v1_billing_webhooks_stripe_post
    intent: Receive Stripe billing webhook events
    question: Which endpoint should Stripe send subscription webhooks to?
  phrasing_ops: 5
  slug: hilt-so-billing-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The checkout API from Hilt — 12 operation(s) for checkout.
  name: Hilt Checkout API
  phrasing_intents:
  - id: record_payment_broadcast_v1_pay_broadcast_post
    intent: Record a broadcast checkout transaction
    question: How do I tell the checkout that the buyer's transaction was broadcast on-chain?
  - id: automatic_renew_setup_v1_pay_automatic_renew_setup_post
    intent: Set up automatic renewal for a payment
    question: Can a buyer turn on automatic renewal during checkout?
  - id: start_checkout_identity_handshake_v1_pay_identity_start_post
    intent: Start a buyer identity handshake at checkout
    question: How does a buyer link their wallet to their customer identity before paying?
  - id: complete_checkout_identity_handshake_v1_pay_identity_complete_post
    intent: Complete a buyer identity handshake
    question: What do I submit to finish the checkout identity handshake?
  - id: phantom_connect_callback_v1_pay_phantom_connect_callback_post
    intent: Handle the Phantom mobile connect callback
    question: Where does Phantom mobile send its encrypted connect response during checkout?
  - id: phantom_message_url_v1_pay_phantom_message_url_post
    intent: Build a Phantom sign-message deeplink for identity
    question: Can I get a Phantom mobile link that asks the buyer to sign the identity message?
  - id: phantom_renewal_message_url_v1_pay_phantom_renewal_message_url_post
    intent: Build a Phantom deeplink to sign auto-renew consent
    question: How does a mobile buyer sign the automatic renewal consent in Phantom?
  - id: phantom_message_callback_v1_pay_phantom_message_callback_post
    intent: Handle Phantom's signed identity message callback
    question: Where does Phantom return the signed identity message after the buyer approves?
  phrasing_ops: 12
  slug: hilt-so-checkout-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The checkout-domains API from Hilt — 1 operation(s) for checkout-domains.
  name: Hilt Checkout Domains API
  phrasing_intents:
  - id: list_merchant_checkout_domains_v1_checkout_domains_get
    intent: List my checkout domain requests
    question: Which custom checkout domains have I requested?
  - id: request_merchant_checkout_domain_v1_checkout_domains_post
    intent: Request a custom checkout domain
    question: Can I host checkout on my own domain?
  phrasing_ops: 2
  slug: hilt-so-checkout-domains-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The Hilt Pay API API from Hilt — 39 operation(s) for hilt pay api.
  name: Hilt Hilt Pay API
  phrasing_intents:
  - id: getHiltPayApiMarketplaceOffer
    intent: Get the Hilt Pay API marketplace offer
    question: What plans does the Hilt Pay API marketplace offer and how can I buy them?
  - id: getHiltAgentCommerceCatalog
    intent: Get the agent-commerce catalog
    question: What products and tools are in the canonical agent-commerce catalog?
  - id: getHiltAgentCommercePricing
    intent: Get agent-commerce pricing
    question: How much do the Starter, Growth and Scale plans cost?
  - id: activateHiltPayApiStarterWithX402
    intent: Buy the Starter plan with x402
    question: Can my agent pay 79 USDC over x402 to activate the Starter plan?
  - id: activateHiltPayApiGrowthWithX402
    intent: Buy the Growth plan with x402
    question: Can an agent pay 349 USDC through x402 to activate the Growth plan?
  - id: activateHiltPayApiScaleWithX402
    intent: Buy the Scale plan with x402
    question: Can I pay 1250 USDC with x402 to unlock the Scale plan?
  - id: claimHiltPayApiMarketplaceKey
    intent: Recover a live key after a marketplace purchase
    question: I paid for a plan but never got the key - can I claim it again?
  - id: create_agent_bootstrap_v1_access_agent_bootstrap_post
    intent: Create a sandbox setup intent for an agent
    question: How does an agent get started with a free sandbox setup intent?
  phrasing_ops: 39
  slug: hilt-so-hilt-pay-api-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The Hilt PayMe Connector API from Hilt — 6 operation(s) for hilt payme connector.
  name: Hilt Hilt PayMe Connector API
  phrasing_intents:
  - id: read_grok_authorization_v1_connectors_grok_authorization_get
    intent: Review a pending Grok connector authorization
    question: What is the Grok connector asking permission to do on my PayMe account?
  - id: approve_grok_authorization_v1_connectors_grok_authorization_post
    intent: Approve or deny a Grok connector authorization
    question: How do I let Grok connect to my PayMe account?
  - id: read_pay_me_connector_connections_v1_pay_me_connector_connections_get
    intent: List my PayMe connector connections
    question: Which AI connectors are currently linked to my PayMe account?
  - id: disconnect_pay_me_connector_v1_pay_me_connector_connections__connection_id__delete
    intent: Disconnect a PayMe connector
    question: How do I remove a connector's access to my PayMe account?
  - id: create_pay_me_payment_request_v1_pay_me_payment_requests_post
    intent: Request a payment through PayMe
    question: Can I ask someone on X to pay me a specific amount?
  - id: read_pay_me_payment_request_v1_pay_me_payment_requests__public_id__get
    intent: Read a PayMe payment request
    question: Has my PayMe payment request been paid yet?
  - id: read_pay_me_payment_intent_v1_pay_me_payment_intents__public_id__get
    intent: Read a PayMe payment intent
    question: What's the state of a PayMe payment intent?
  phrasing_ops: 7
  slug: hilt-so-hilt-payme-connector-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The integrations API from Hilt — 4 operation(s) for integrations.
  name: Hilt Integrations API
  phrasing_intents:
  - id: integration_health_v1_integrations_health_get
    intent: Check integration connection health
    question: Are my integrations connected and healthy?
  - id: list_integration_events_v1_integrations_events_get
    intent: List events emitted to integrations
    question: Which events have been sent out to my integrations recently?
  - id: subscribe_zapier_hook_v1_integrations_zapier_hooks_post
    intent: Subscribe a Zapier REST hook
    question: How do I send Hilt payment events to a Zap?
  - id: unsubscribe_zapier_hook_v1_integrations_zapier_hooks__endpoint_id__delete
    intent: Unsubscribe a Zapier REST hook
    question: How do I stop a Zap from receiving Hilt events?
  phrasing_ops: 4
  slug: hilt-so-integrations-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The memberships API from Hilt — 11 operation(s) for memberships.
  name: Hilt Memberships API
  phrasing_intents:
  - id: api_list_memberships_v1_memberships_get
    intent: List memberships
    question: Which members currently have access to my products?
  - id: api_lookup_memberships_v1_memberships_lookup_get
    intent: Look up memberships by wallet or transaction
    question: Which membership belongs to this wallet address?
  - id: api_membership_renewal_intelligence_v1_memberships_renewal_intelligence_get
    intent: Get renewal cohorts and reminders
    question: Which members are coming up for renewal soon?
  - id: api_get_membership_v1_memberships__membership_id__get
    intent: Get a membership
    question: What are the details of a specific membership?
  - id: api_update_membership_notes_v1_memberships__membership_id__notes_patch
    intent: Save notes on a membership
    question: Can I keep private merchant notes on a member?
  - id: api_update_membership_profile_v1_memberships__membership_id__profile_patch
    intent: Update a member's display details
    question: Can I change how a member's platform name is displayed?
  - id: api_gift_membership_extension_v1_memberships__membership_id__gift_post
    intent: Gift extra access days to a member
    question: Can I give a member free extra days of access?
  - id: api_retry_membership_delivery_v1_memberships__membership_id__retry_delivery_post
    intent: Retry access delivery for a member
    question: A member paid but never got into the group - can I retry delivery?
  phrasing_ops: 11
  slug: hilt-so-memberships-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The pay-me API from Hilt — 21 operation(s) for pay-me.
  name: Hilt Pay Me API
  phrasing_intents:
  - id: read_pay_me_session_v1_pay_me_session_get
    intent: Read my X identity and PayMe profile
    question: Which X account am I signed into PayMe with?
  - id: read_pay_me_security_v1_pay_me_security_get
    intent: Check my receiving-wallet security
    question: Is an authenticator protecting my PayMe receiving wallet?
  - id: start_pay_me_authenticator_setup_v1_pay_me_security_authenticator_setup_post
    intent: Start authenticator enrollment
    question: How do I add an authenticator app to PayMe?
  - id: read_pay_me_authenticator_enrollment_v1_pay_me_security_authenticator_enrollments__enrollment_id__get
    intent: Read an authenticator enrollment's wallet approval
    question: What wallet approval is pending for my authenticator enrollment?
  - id: approve_pay_me_authenticator_wallet_v1_pay_me_security_authenticator_enrollments__enrollment_id__signature_post
    intent: Approve authenticator setup with my wallet
    question: How do I sign with my current wallet to approve authenticator setup?
  - id: read_pay_me_authenticator_enrollment_status_v1_pay_me_security_authenticator_enrollments__enrollment_id__status_get
    intent: Check wallet approval status for an enrollment
    question: Has my wallet approved the authenticator enrollment yet?
  - id: confirm_pay_me_authenticator_setup_v1_pay_me_security_authenticator_confirm_post
    intent: Confirm authenticator enrollment with a code
    question: How do I finish authenticator setup with the code from my app?
  - id: create_verified_pay_me_profile_v1_pay_me_profile_post
    intent: Create or update my verified PayMe profile
    question: Can I publish a verified PayMe profile tied to my receiving wallet?
  phrasing_ops: 21
  slug: hilt-so-pay-me-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The products API from Hilt — 9 operation(s) for products.
  name: Hilt Products API
  phrasing_intents:
  - id: api_create_product_v1_products_post
    intent: Create a payment product
    question: How do I create a product buyers can pay for in crypto?
  - id: api_list_products_v1_products_get
    intent: List my products
    question: Which products have I created?
  - id: api_view_product_public_v1_products_p__slug__get
    intent: View a product's public page
    question: What does a buyer see on my product's public page?
  - id: api_connect_payment_v1_products_p__slug__connect_post
    intent: Start a checkout session for a product
    question: How does a buyer start paying for a product?
  - id: api_resolve_checkout_handoff_v1_products_p__slug__resolve_handoff_post
    intent: Resolve a signed buyer handoff link
    question: What buyer identity is encoded in a signed checkout handoff?
  - id: api_list_payments_v1_products__product_id__payments_get
    intent: List payments for a product
    question: Who has paid for this product?
  - id: api_product_analytics_v1_products__product_id__analytics_get
    intent: View payment analytics for a product
    question: How much has a single product earned?
  - id: api_get_product_v1_products__product_id__get
    intent: Get a product by ID
    question: What are the full settings of one of my products?
  phrasing_ops: 12
  slug: hilt-so-products-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The Receipt API from Hilt — 10 operation(s) for receipt.
  name: Hilt Receipt API
  phrasing_intents:
  - id: post_receipt_v1_receipt_post
    intent: Generate a signed receipt for a transaction
    question: How do I get a signed receipt for a Solana transaction?
  - id: get_receipt_v1_receipt__receipt_id__get
    intent: Get a full signed receipt
    question: Can I retrieve the full signed receipt JSON?
  - id: get_public_receipt_v1_receipt__receipt_id__public_get
    intent: View a receipt's public proof
    question: What does the public proof page of a receipt show?
  - id: verify_receipt_v1_receipt__receipt_id__verify_get
    intent: Verify a receipt's signature
    question: Is this receipt's signature genuine?
  - id: get_receipt_pdf_v1_receipt__receipt_id__pdf_get
    intent: Download a public receipt PDF
    question: Can I download a receipt as a public PDF?
  - id: get_authenticated_receipt_pdf_v1_receipt__receipt_id__pdf_private_get
    intent: Export a private receipt PDF
    question: Can I export a receipt PDF that includes my private invoice details?
  - id: list_receipts_v1_receipts_get
    intent: List my receipts
    question: Which receipts have I generated?
  - id: export_receipts_csv_v1_receipts_export_csv_get
    intent: Export my receipt ledger to CSV
    question: How do I download my receipts as a CSV for accounting?
  phrasing_ops: 10
  slug: hilt-so-receipt-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The Solana API from Hilt — 1 operation(s) for solana.
  name: Hilt Solana API
  phrasing_intents:
  - id: getSolanaTransactionEvidence
    intent: Get evidence for a finalized Solana transaction
    question: Who signed a Solana transaction and what tokens moved in it?
  phrasing_ops: 1
  slug: hilt-so-solana-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The Support API from Hilt — 3 operation(s) for support.
  name: Hilt Support API
  phrasing_intents:
  - id: create_ticket_v1_support_tickets_post
    intent: Open a support ticket
    question: How do I contact Hilt support about a problem?
  - id: list_tickets_v1_support_tickets_get
    intent: List my support tickets
    question: Which support tickets have I opened?
  - id: get_ticket_v1_support_tickets__ticket_id__get
    intent: View a support ticket thread
    question: Has support replied to my ticket?
  - id: add_message_v1_support_tickets__ticket_id__message_post
    intent: Reply to a support ticket
    question: Can I add more details to a ticket I already opened?
  phrasing_ops: 4
  slug: hilt-so-support-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The system API from Hilt — 2 operation(s) for system.
  name: Hilt System API
  phrasing_intents:
  - id: health_health_get
    intent: Check service health at the root path
    question: Is the Hilt service up at the root /health check?
  - id: health_v1_v1_health_get
    intent: Check v1 API health
    question: Is the v1 API responding right now?
  phrasing_ops: 2
  slug: hilt-so-system-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The testing API from Hilt — 3 operation(s) for testing.
  name: Hilt Testing API
  slug: hilt-so-testing-api
- baseURL: https://api.hilt.so
  baseurl_source: declared
  description: The webhooks API from Hilt — 7 operation(s) for webhooks.
  name: Hilt Webhooks API
  phrasing_intents:
  - id: list_webhook_endpoints_v1_webhooks_endpoints_get
    intent: List webhook endpoints
    question: Which webhook endpoints have I set up?
  - id: create_webhook_endpoint_v1_webhooks_endpoints_post
    intent: Create a webhook endpoint
    question: How do I get notified when someone pays?
  - id: update_webhook_endpoint_v1_webhooks_endpoints__endpoint_id__patch
    intent: Update a webhook endpoint
    question: Can I change the URL of an existing webhook?
  - id: disable_webhook_endpoint_v1_webhooks_endpoints__endpoint_id__delete
    intent: Disable a webhook endpoint
    question: How do I turn off a webhook endpoint?
  - id: test_webhook_endpoint_v1_webhooks_endpoints__endpoint_id__test_post
    intent: Send a test webhook event
    question: Can I send a signed test event to check my webhook works?
  - id: list_webhook_deliveries_v1_webhooks_deliveries_get
    intent: List webhook deliveries
    question: Which webhook deliveries failed?
  - id: replay_owned_webhook_delivery_v1_webhooks_deliveries__delivery_id__replay_post
    intent: Replay a webhook delivery
    question: Can I resend a webhook delivery my server missed?
  - id: webhook_timeline_v1_webhooks_timeline_get
    intent: View the webhook timeline for a payment or membership
    question: Which webhooks fired for a specific payment?
  phrasing_ops: 9
  slug: hilt-so-webhooks-api
artifact_total: 38
asyncapis:
- description: 'Hilt webhook events delivered by HTTPS POST to merchant endpoints. GENERATED by API Evangelist (method: generated) from the provider''s documented webhook catalogue at https://docs.hilt.so/developers/w'
  name: Hilt Webhooks
  slug: hilt-so-webhooks-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/hilt-so/capabilities/hilt-so-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hilt-so-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.hilt.so/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hilt.so/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hilt.so/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.hilt.so/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hilt.so/developers/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.hilt.so/merchant/support
- group: operate
  title: ''
  type: Contact
  url: https://www.hilt.so/contact
- group: company
  title: ''
  type: Blog
  url: https://www.hilt.so/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hiltpay
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hilt.so/developers/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.hilt.so/register
- group: start
  title: ''
  type: Login
  url: https://app.hilt.so/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hilt.so/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hilt.so/legal/privacy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.hilt.so/legal/refund
- group: operate
  title: ''
  type: StatusPage
  url: https://www.hilt.so/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.hilt.so/updates
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.hilt.so/release-notes/changelog
- group: operate
  href: https://artifacts.apis.io/hilt-so/changelog/hilt-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hilt-so-changelog.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hiltpay
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@hiltpay
- group: build
  title: ''
  type: Postman
  url: https://www.hilt.so/downloads/hilt-postman-collection-latest.json
- group: agent
  href: https://artifacts.apis.io/hilt-so/llms/hilt-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hilt-so-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.hilt.so/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.hilt.so/llms.txt
- group: agent
  href: https://artifacts.apis.io/hilt-so/well-known/hilt-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hilt-so-well-known.yml
- group: agent
  href: https://artifacts.apis.io/hilt-so/mcp/hilt-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hilt-so-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hilt-so/mcp/hilt-so-pay-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hilt-so-pay-me-mcp.yml
- group: build
  href: https://artifacts.apis.io/hilt-so/mcp/hilt-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hilt-so-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/hilt-so/a2a/hilt-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hilt-so-a2a.yml
- group: build
  href: https://artifacts.apis.io/hilt-so/packages/hilt-so-packages.yml
  title: ''
  type: Packages
  url: packages/hilt-so-packages.yml
- group: build
  href: https://artifacts.apis.io/hilt-so/packages/hilt-so-packages.yml
  title: ''
  type: SDKs
  url: packages/hilt-so-packages.yml
- group: build
  href: https://artifacts.apis.io/hilt-so/cli/hilt-so-cli.yml
  title: ''
  type: CLI
  url: cli/hilt-so-cli.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/components/hilt-so-components.yml
  title: ''
  type: Components
  url: components/hilt-so-components.yml
- group: start
  href: https://artifacts.apis.io/hilt-so/sandbox/hilt-so-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hilt-so-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/hilt-so/authentication/hilt-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hilt-so-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hilt-so/scopes/hilt-so-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hilt-so-scopes.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/conventions/hilt-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hilt-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/conventions/hilt-so-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hilt-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/lifecycle/hilt-so-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hilt-so-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/conformance/hilt-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hilt-so-conformance.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/errors/hilt-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hilt-so-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/hilt-so/security/hilt-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hilt-so-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/hilt-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/hilt-so/plans/hilt-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hilt-so-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hilt-so/rate-limits/hilt-so-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hilt-so-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/asyncapi/hilt-so-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/hilt-so-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/hilt-so/asyncapi/hilt-so-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/hilt-so-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/hilt-so/data-model/hilt-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hilt-so-data-model.yml
- group: other
  href: https://artifacts.apis.io/hilt-so/overlays/hilt-so-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hilt-so-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hilt-so/regulatory/hilt-so-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/hilt-so-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.hilt.so/legal/privacy
created: '2026-09-19'
description: 'Hilt is a zero-custody Solana payments company operated in the United Kingdom by Paul Wild trading as Hilt (London). It ships four connected products: PayMe (a free receiving link and QR for an OAuth-verified X handle, sender pays a flat 2% fee), Direct Checkout (a no-account SOL / USDC / single-token checkout link), Hilt Pay Workspace (the merchant dashboard for hosted checkout, embeds, WooCommerce, receipts, memberships, native Solana USDC subscriptions and signed webhooks) and Hilt Pay API, the developer and agent product under /v1/access that turns an HTTP 402 into an operating record: x402 V2 payment requirement, Solana USDC or native SOL settlement, receipt, entitlement, atomic metered usage consumption, MPP payment channels and webhook trail. Hilt publishes an OpenAPI 3.1 contract (165 operations on api.hilt.so), a hosted MCP gateway and an OAuth-gated PayMe MCP connector, an A2A agent card, llms.txt on three hosts, TypeScript and Python SDKs, a CLI, Postman assets and
  a documented sandbox. Live pricing is $0/month plus 1% per successful settlement.'
finops:
- has_sources: true
  method: derived
  name: Hilt So Finops
  primary_unit: successful settlement
  service_category: ''
  slug: hilt-so-finops
  template: false
image: https://www.hilt.so/Logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.hilt.so over HTTP; 9 tools listed.
  name: Hilt Pay Agent Gateway
  slug: hilt-pay-agent-gateway
- description: Remote MCP server at api.hilt.so over HTTP requiring OAuth; 10 tools listed.
  name: Hilt PayMe
  slug: hilt-payme
modified: '2026-09-19'
name: Hilt
nav: Providers
network: true
overview: 'Hilt publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent Commerce API, API Keys API, and 18 more. Tagged areas include Payments, Solana, Stablecoins, USDC, and Crypto Payments.


  The Hilt catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hilt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 46 more developer resources.'
plans:
- name: Hilt So Plans Pricing
  plan_count: 3
  slug: hilt-so-plans-pricing
- name: Hilt So Price Estimates
  plan_count: 0
  slug: hilt-so-price-estimates
random_paper: 8
rate_limits:
- limit_count: 1
  name: Hilt So Rate Limits
  slug: hilt-so-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Hilt API Rules
  rule_count: 55
  severity_counts:
    error: 37
    hint: 0
    info: 4
    warn: 14
  slug: hilt-so-rules
scopes:
- name: Hilt So Scopes
  scope_count: 0
  slug: hilt-so-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 57.3
    developer_ergonomics: 65.5
    discoverability: 75.0
    operational_transparency: 43.4
  previous_composite: 75.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 94.7
      total: 19
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/hilt-so/hilt-so-2026-10-11T105307.png
security:
- kind: authentication
  name: Hilt So Authentication
  slug: hilt-so-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Hilt So Domain Security
  slug: hilt-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: hilt-agent-bootstrap-setup
  slug: hilt-so-agent-bootstrap-setup
- name: hilt-cancel-native-subscription
  slug: hilt-so-cancel-native-subscription
- name: hilt-pay-api
  slug: hilt-so-hilt-pay-api-skill
- name: hilt-mpp-metered-channel
  slug: hilt-so-mpp-metered-channel
- name: hilt-protect-metered-endpoint
  slug: hilt-so-protect-metered-endpoint
- name: hilt-verify-webhooks
  slug: hilt-so-verify-webhooks
slug: hilt-so
tags:
- Payments
- Solana
- Stablecoins
- USDC
- Crypto Payments
- Agentic Payments
- x402
- Checkout
- Subscription
- Webhook
- MCP
- Entitlements
- Micropayments
- Developer Tools
- Fintech
- A2A
website: https://www.hilt.so/
---
