---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 84
  human_in_the_loop: 1
  name: Algovoi Co Uk Agentic Access
  operation_count: 151
  slug: algovoi-co-uk-agentic-access
  summary_line: 151 operations · 84 acting · 1 human-in-the-loop
api_count: 10
apis:
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The A2a API from AlgoVoi — 12 operation(s) for a2a.
  name: AlgoVoi A2a API
  phrasing_intents:
  - id: a2a_hint_a2a_get
    intent: Get a pointer to the A2A POST transport
    question: What does a GET on the A2A endpoint return if the real transport is POST?
  - id: a2a_a2a_post
    intent: Post a request to the A2A endpoint
    question: Can I POST an agent-to-agent request directly to the base A2A path?
  - id: _scoped_auth_receipts_profile_ext_scoped_authorization_receipts_v1_head
    intent: Read the scoped authorization receipts profile
    question: What is the scoped authorization receipts extension profile for A2A?
  - id: headExtScopedAuthorizationReceiptsV1
    intent: Check the receipts profile exists (HEAD)
    question: Can I check the scoped receipts profile is published without downloading the body?
  - id: extended_agent_card_extendedAgentCard_get
    intent: Get the authenticated extended agent card
    question: How do I see my tenant-specific endpoints in the AlgoVoi agent card?
  - id: send_message_message_send_post
    intent: Send a message to the payment agent
    question: How do I ask the payment agent to create a checkout or verify a payment over A2A?
  - id: message_stream_message_stream_post
    intent: Request a streamed agent reply (unsupported)
    question: Does the AlgoVoi agent support streaming message responses?
  - id: push_notification_config_tasks__task_id__pushNotificationConfigs__config_id__get
    intent: Get one push notification config for a task
    question: Can I read a specific push notification configuration on a task?
  phrasing_ops: 16
  slug: algovoi-co-uk-a2a-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The agent-auth API from AlgoVoi — 2 operation(s) for agent-auth.
  name: AlgoVoi Agent Auth API
  phrasing_intents:
  - id: exchange_atb_cert_auth_token_post
    intent: Exchange an ATB certificate for an agent session
    question: How does my agent swap an ATB zero-knowledge certificate for a session token?
  - id: session_status_auth_token_status_get
    intent: Check an agent session's spend against its cap
    question: How much of its spend cap has my agent session used?
  phrasing_ops: 2
  slug: algovoi-co-uk-agent-auth-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The AlgoVoi Audit Verifier API from AlgoVoi — 1 operation(s) for algovoi audit verifier.
  name: AlgoVoi AlgoVoi Audit Verifier API
  phrasing_intents:
  - id: root__get
    intent: Open the audit verifier home page
    question: What is on the AlgoVoi audit verifier's root page?
  phrasing_ops: 1
  slug: algovoi-co-uk-algovoi-audit-verifier-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The AlgoVoi Verifiable Comms Agent API from AlgoVoi — 1 operation(s) for algovoi verifiable comms agent.
  name: AlgoVoi AlgoVoi Verifiable Comms Agent API
  phrasing_intents:
  - id: landing__get
    intent: Open the verifiable comms agent landing page
    question: What does the verifiable comms agent's landing page describe?
  phrasing_ops: 1
  slug: algovoi-co-uk-algovoi-verifiable-comms-agent-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Ap2 API from AlgoVoi — 7 operation(s) for ap2.
  name: AlgoVoi Ap2 API
  phrasing_intents:
  - id: ap2_verify_v1_ap2_verify_post
    intent: Verify a payer's AP2 mandate credential
    question: How do I check that an AP2 mandate a payer submitted carries a valid signed JWT?
  - id: submit_intent_ap2_intent_post
    intent: Open an AP2 shopping session with an IntentMandate
    question: How does an agent start an AP2 shopping session?
  - id: submit_cart_ap2_cart_post
    intent: Submit a merchant-signed CartMandate
    question: How do I attach a merchant-signed cart to an accepted AP2 intent?
  - id: initiate_payment_ap2_pay_post
    intent: Submit a PaymentMandate and get a crypto challenge
    question: How do I pay for an AP2 cart once it is accepted?
  - id: confirm_payment_ap2_confirm_post
    intent: Confirm an AP2 on-chain payment and get a JWT
    question: After the on-chain transfer, how do I get the AP2 access token?
  - id: get_status_ap2_status__cart_id__get
    intent: Inspect an AP2 mandate chain by cart
    question: Where is my AP2 cart in the intent, cart, payment and confirm chain?
  - id: list_extensions_ap2_extensions_get
    intent: List the AP2 extensions this gateway supports
    question: Which AP2 extensions and crypto payment methods does the gateway support?
  phrasing_ops: 7
  slug: algovoi-co-uk-ap2-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The atb-license API from AlgoVoi — 1 operation(s) for atb-license.
  name: AlgoVoi Atb License API
  phrasing_intents:
  - id: activate_atb_license_activate_post
    intent: Activate an atb-zkp-service operator licence
    question: How does an operator get the signed activation token needed to start the atb-zkp-service container?
  phrasing_ops: 1
  slug: algovoi-co-uk-atb-license-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The bazaar API from AlgoVoi — 1 operation(s) for bazaar.
  name: AlgoVoi Bazaar API
  phrasing_intents:
  - id: discovery_resources_discovery_resources_get
    intent: List x402-payable resources on the facilitator
    question: Which x402-payable resources does this facilitator offer?
  phrasing_ops: 1
  slug: algovoi-co-uk-bazaar-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The checkout API from AlgoVoi — 17 operation(s) for checkout.
  name: AlgoVoi Checkout API
  phrasing_intents:
  - id: verify_checkout_checkout__token__verify_post
    intent: Verify a payer's on-chain transaction for a checkout
    question: How do I confirm a shopper's crypto transaction and mark the payment link as paid?
  - id: checkout_qr_checkout__token__qr_get
    intent: Render a QR code image for a checkout
    question: Can I get a PNG QR code for a WalletConnect pairing URI on a checkout page?
  - id: checkout_build_txn_checkout__token__build_txn_get
    intent: Build an unsigned Algorand or VOI checkout transaction
    question: How can a wallet get an unsigned Algorand transaction to sign for a checkout via WalletConnect?
  - id: checkout_submit_txn_checkout__token__submit_txn_post
    intent: Submit a signed Algorand or VOI checkout transaction
    question: Once the customer signs the Algorand transaction, how do I broadcast it to algod for this checkout?
  - id: detect_payment_checkout__token__detect_get
    intent: Detect an inbound payment for a checkout
    question: Can the checkout find the customer's payment on-chain without them pasting a transaction id?
  - id: submit_sponsored_checkout__token__submit_sponsored_post
    intent: Submit a fee-sponsored checkout transaction
    question: Can the merchant's sponsor wallet pay the network fee so the customer sends a zero-fee transaction?
  - id: abandon_checkout_checkout__token__abandon_post
    intent: Mark a checkout as abandoned by the customer
    question: How does a shopper walk away from a checkout so the merchant order doesn't stay pending forever?
  - id: cancel_checkout_checkout__token__cancel_post
    intent: Cancel an active checkout link as the merchant
    question: How does a merchant cancel a payment link they created?
  phrasing_ops: 17
  slug: algovoi-co-uk-checkout-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The compliance API from AlgoVoi — 5 operation(s) for compliance.
  name: AlgoVoi Compliance API
  phrasing_intents:
  - id: attestation_compliance_attestation_get
    intent: Get the gateway's compliance attestation
    question: What is the payment gateway's full compliance posture?
  - id: screen_compliance_screen_post
    intent: Screen a recipient wallet before paying
    question: How do I screen a wallet address for sanctions before sending it money?
  - id: trust_query_compliance_trust_query_post
    intent: Get a composite trust verdict over receipts
    question: Can I get one trust verdict over a chain of compliance, settlement, refund and cancellation receipts?
  - id: verify_receipt_v1_receipt_verify_post
    intent: Verify a JWS compliance receipt
    question: How do I cryptographically verify a compliance receipt or settlement attestation?
  - id: get_settlement_evidence_v1_receipt_settlement_evidence__settled_payment_ref__get
    intent: Fetch on-chain settlement evidence for a payment
    question: Has the chain evidence for one of my settled payments been captured yet?
  phrasing_ops: 5
  slug: algovoi-co-uk-compliance-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Customers API from AlgoVoi — 1 operation(s) for customers.
  name: AlgoVoi Customers API
  phrasing_intents:
  - id: create_customer_endpoint_v1_customers_post
    intent: Create a customer
    question: How do I add a new customer with an email and wallet address?
  - id: list_customers_endpoint_v1_customers_get
    intent: List customers
    question: Which customers do I have on file?
  phrasing_ops: 2
  slug: algovoi-co-uk-customers-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: Resource discovery and manifest endpoints
  name: AlgoVoi Discovery API
  phrasing_intents:
  - id: list_resources
    intent: List all bench profiles in Bazaar format
    question: Which bench profiles can an x402 crawler enumerate on the Agent Trust Bench?
  - id: well_known_x402
    intent: Get the x402 discovery manifest
    question: Where is the bench's x402 well-known discovery document?
  phrasing_ops: 2
  slug: algovoi-co-uk-discovery-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Health API from AlgoVoi — 1 operation(s) for health.
  name: AlgoVoi Health API
  phrasing_intents:
  - id: health_health_get
    intent: Check service health
    question: Is the AlgoVoi gateway up?
  phrasing_ops: 1
  slug: algovoi-co-uk-health-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The mandate API from AlgoVoi — 1 operation(s) for mandate.
  name: AlgoVoi Mandate API
  phrasing_intents:
  - id: mandate_pay_mandate_pay_post
    intent: Pay for a resource with a mandate token
    question: How do I pay for a resource using a prepaid mandate JWT?
  phrasing_ops: 1
  slug: algovoi-co-uk-mandate-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The mandate-portal API from AlgoVoi — 3 operation(s) for mandate-portal.
  name: AlgoVoi Mandate Portal API
  phrasing_intents:
  - id: get_mandate_portal_mandate_portal__mandate_id__get
    intent: View a mandate's balance and recent charges
    question: What is my mandate's balance and its last few charges?
  - id: portal_topup_initiate_mandate_portal__mandate_id__topup_initiate_post
    intent: Start a PayPal top-up for a mandate
    question: How do I add funds to my mandate with PayPal?
  - id: portal_topup_capture_mandate_portal__mandate_id__topup_capture_post
    intent: Capture an approved PayPal mandate top-up
    question: After the buyer approves in PayPal, how do I capture the top-up?
  phrasing_ops: 3
  slug: algovoi-co-uk-mandate-portal-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The mesh-federation API from AlgoVoi — 2 operation(s) for mesh-federation.
  name: AlgoVoi Mesh Federation API
  phrasing_intents:
  - id: provision_suite_store_mesh_fed_provision_post
    intent: Provision a mesh federation certificate
    question: How do I get a mesh federation certificate for my customer licence?
  - id: info_suite_store_mesh_fed_info_get
    intent: Check the mesh federation service is live
    question: Is the mesh federation provisioning service reachable before I install?
  phrasing_ops: 2
  slug: algovoi-co-uk-mesh-federation-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: Service metadata and health
  name: AlgoVoi Meta API
  phrasing_intents:
  - id: get_stats
    intent: Get aggregate bench statistics
    question: How many bench challenges have been issued and payments verified?
  - id: openapi_schema
    intent: Download the bench OpenAPI schema
    question: Where is the OpenAPI description for the bench?
  - id: health
    intent: Check the bench health
    question: Is the Agent Trust Bench up right now?
  phrasing_ops: 3
  slug: algovoi-co-uk-meta-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The mpp API from AlgoVoi — 6 operation(s) for mpp.
  name: AlgoVoi Mpp API
  phrasing_intents:
  - id: mpp_challenge_mpp_challenge_post
    intent: Pre-fetch an MPP payment challenge
    question: Can my agent get the payment challenge before building its transaction instead of hitting the resource first?
  - id: mpp_probe_mpp_probe_delete
    intent: Probe the paid MPP resource with GET
    question: What does a plain GET to the MPP probe return without payment?
  - id: putMppProbe
    intent: Probe the paid MPP resource with PUT
    question: Does the MPP probe accept a PUT request with a payment proof?
  - id: postMppProbe
    intent: Probe the paid MPP resource with POST
    question: Can I POST a Payment authorization to the MPP probe and get a receipt?
  - id: deleteMppProbe
    intent: Probe the paid MPP resource with DELETE
    question: Is the DELETE method on the MPP probe also gated by a payment challenge?
  - id: optionsMppProbe
    intent: Probe the paid MPP resource with OPTIONS
    question: Which methods does the MPP probe allow when asked with OPTIONS?
  - id: headMppProbe
    intent: Probe the paid MPP resource with HEAD
    question: Can I read the MPP probe's payment challenge headers with HEAD only?
  - id: patchMppProbe
    intent: Probe the paid MPP resource with PATCH
    question: Does a PATCH to the MPP probe behave like the other paid methods?
  phrasing_ops: 13
  slug: algovoi-co-uk-mpp-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The payable-a2a API from AlgoVoi — 1 operation(s) for payable-a2a.
  name: AlgoVoi Payable A2a API
  phrasing_intents:
  - id: a2a_jsonrpc_a2a_post
    intent: Call the payable agent over A2A JSON-RPC
    question: Can I reach the payable services agent with an A2A JSON-RPC call?
  phrasing_ops: 1
  slug: algovoi-co-uk-payable-a2a-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The payable API from AlgoVoi — 6 operation(s) for payable.
  name: AlgoVoi Payable API
  phrasing_intents:
  - id: payable_index_pay_v1_index_get
    intent: List the pay-per-call services
    question: Which pay-per-call verification services are available?
  - id: negotiate_capabilities_pay_v1_negotiate_get
    intent: See which chains and protocols can be negotiated
    question: Which payment chains and protocols can I negotiate for payable services?
  - id: negotiate_pay_v1_negotiate_post
    intent: Negotiate payment terms for a service
    question: How do I agree a chain and protocol before paying for a service?
  - id: probe_receipt_pay_v1_verify_receipt_get
    intent: Probe the paid receipt verifier
    question: What does the paid receipt-verification service charge before I call it?
  - id: pay_verify_receipt_pay_v1_verify_receipt_post
    intent: Pay to verify a JWS receipt
    question: How do I pay per call to verify a JWS receipt?
  - id: probe_rfc9421_pay_v1_verify_rfc9421_get
    intent: Probe the paid RFC 9421 verifier
    question: What payment does the RFC 9421 signature verifier ask for?
  - id: pay_verify_rfc9421_pay_v1_verify_rfc9421_post
    intent: Pay to verify an RFC 9421 signed request
    question: How do I pay to have an HTTP message signature verified?
  - id: probe_url_screen_pay_v1_screen_url_get
    intent: Probe the paid URL screening service
    question: How much does it cost to screen a URL?
  phrasing_ops: 11
  slug: algovoi-co-uk-payable-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The payable-identity API from AlgoVoi — 1 operation(s) for payable-identity.
  name: AlgoVoi Payable Identity API
  phrasing_intents:
  - id: verify_receipt_post_v1_receipt_verify_post
    intent: Verify a JWS receipt on the identity service
    question: Can the payable identity service verify a signed receipt for me?
  phrasing_ops: 1
  slug: algovoi-co-uk-payable-identity-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Payment Links API from AlgoVoi — 1 operation(s) for payment links.
  name: AlgoVoi Payment Links API
  phrasing_intents:
  - id: create_dynamic_payment_link_v1_payment_links_post
    intent: Create a hosted checkout link for a fiat amount
    question: How do I create a crypto payment link for a price in pounds or dollars?
  phrasing_ops: 1
  slug: algovoi-co-uk-payment-links-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Payouts API from AlgoVoi — 1 operation(s) for payouts.
  name: AlgoVoi Payouts API
  phrasing_intents:
  - id: create_payout_v1_payouts_post
    intent: Send an on-chain payout from my balance
    question: How do I pay out funds from my custodial balance to a wallet?
  phrasing_ops: 1
  slug: algovoi-co-uk-payouts-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: Payable and free bench profiles
  name: AlgoVoi Profiles API
  phrasing_intents:
  - id: get_profile
    intent: Request a trust bench profile
    question: What does a bench profile return to an agent that hasn't paid, a 402 x402 challenge?
  - id: get_freebie
    intent: Call the always-free control endpoint
    question: Is there a free endpoint to check my agent tells free and paid resources apart?
  phrasing_ops: 2
  slug: algovoi-co-uk-profiles-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The public API from AlgoVoi — 1 operation(s) for public.
  name: AlgoVoi Public API
  phrasing_intents:
  - id: public_cancel_page_subscription__cancel_secret__cancel_get
    intent: Show a subscription's cancel confirmation page
    question: What does a customer see when they open their subscription cancel link?
  - id: public_cancel_commit_subscription__cancel_secret__cancel_post
    intent: Commit a subscription cancellation via its link
    question: How does a customer confirm cancelling a subscription from the single-use link?
  phrasing_ops: 2
  slug: algovoi-co-uk-public-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The public-resource API from AlgoVoi — 1 operation(s) for public-resource.
  name: AlgoVoi Public Resource API
  phrasing_intents:
  - id: public_resource_r__tenant_short_id___resource_id__get
    intent: Access a merchant's public x402 resource
    question: How does an agent pay for a merchant's public x402 resource by short link?
  phrasing_ops: 1
  slug: algovoi-co-uk-public-resource-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The recurr API from AlgoVoi — 6 operation(s) for recurr.
  name: AlgoVoi Recurr API
  phrasing_intents:
  - id: challenge_endpoint_v1_recurr_auth_challenge_post
    intent: Get a wallet sign-in challenge for the portal
    question: How does a subscriber sign in to the customer portal with their wallet?
  - id: verify_endpoint_v1_recurr_auth_verify_post
    intent: Verify a wallet signature to sign in
    question: After signing the nonce, how do I finish wallet login to the portal?
  - id: my_subscriptions_v1_recurr_me_subscriptions_get
    intent: List my subscriptions across all merchants
    question: Which subscriptions is my wallet paying for across every merchant?
  - id: my_subscription_detail_v1_recurr_me_subscriptions__subscription_id__get
    intent: View one of my subscriptions
    question: What are the details of one subscription my wallet pays for?
  - id: my_subscription_cancel_v1_recurr_me_subscriptions__subscription_id__cancel_post
    intent: Cancel one of my subscriptions as a subscriber
    question: How do I cancel a subscription I'm paying for from the portal?
  - id: my_invoices_v1_recurr_me_invoices_get
    intent: List my invoices as a subscriber
    question: Which invoices has my wallet been charged?
  phrasing_ops: 6
  slug: algovoi-co-uk-recurr-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The recurr-public API from AlgoVoi — 2 operation(s) for recurr-public.
  name: AlgoVoi Recurr Public API
  phrasing_intents:
  - id: portal_page_recurr_portal_get
    intent: Open the subscriber customer portal
    question: Where can a customer connect a wallet and see every subscription billing it?
  - id: public_cancel_page_recurr_cancel__cancel_secret__get
    intent: Show the portal cancel page for a subscription
    question: What does the recurr portal cancel link show before I confirm?
  - id: public_cancel_commit_recurr_cancel__cancel_secret__post
    intent: Confirm cancellation from the portal link
    question: How do I confirm a cancellation from the recurr portal link?
  phrasing_ops: 3
  slug: algovoi-co-uk-recurr-public-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The recurring API from AlgoVoi — 7 operation(s) for recurring.
  name: AlgoVoi Recurring API
  phrasing_intents:
  - id: create_authority_endpoint_v1_recurring_authorities_post
    intent: Create a standing authority for a subscription
    question: How do I set up an on-chain spending authority so a subscription can pull payments?
  - id: list_authorities_endpoint_v1_recurring_authorities_get
    intent: List standing payment authorities
    question: Which standing payment authorities exist for my subscriptions?
  - id: get_authority_endpoint_v1_recurring_authorities__authority_id__get
    intent: Get a standing authority
    question: What is the status of a standing payment authority?
  - id: confirm_authority_endpoint_v1_recurring_authorities__authority_id__confirm_post
    intent: Activate an authority after it lands on-chain
    question: How do I mark a pending authority active once the customer's transaction lands?
  - id: revoke_authority_endpoint_v1_recurring_authorities__authority_id__revoke_post
    intent: Revoke a standing authority
    question: How do I permanently revoke a customer's standing payment authority?
  - id: pause_authority_endpoint_v1_recurring_authorities__authority_id__pause_post
    intent: Pause a standing authority
    question: Can I temporarily stop pulls on a standing authority without revoking it?
  - id: resume_authority_endpoint_v1_recurring_authorities__authority_id__resume_post
    intent: Resume a paused standing authority
    question: How do I restart pulls on a paused authority?
  - id: manual_pull_endpoint_v1_recurring_pulls_post
    intent: Request a manual pull on an authority
    question: Can I trigger a payment pull now instead of waiting for the next cycle?
  phrasing_ops: 8
  slug: algovoi-co-uk-recurring-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The recurring-contracts API from AlgoVoi — 1 operation(s) for recurring-contracts.
  name: AlgoVoi Recurring Contracts API
  phrasing_intents:
  - id: get_algorand_spending_cap_vault_v1_v1_recurring_contracts_algorand_spending_cap_vault_v1_get
    intent: Get the compiled SpendingCapVault contract
    question: Where do I get the compiled TEAL for the Algorand spending-cap vault?
  phrasing_ops: 1
  slug: algovoi-co-uk-recurring-contracts-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The recurring-hosted-auth API from AlgoVoi — 2 operation(s) for recurring-hosted-auth.
  name: AlgoVoi Recurring Hosted Auth API
  phrasing_intents:
  - id: resolve_token_v1_recurring_auth__token__get
    intent: Resolve a hosted-auth signing token
    question: What authority summary does a hosted-auth signing link show the customer?
  - id: confirm_token_v1_recurring_auth__token__confirm_post
    intent: Confirm a hosted-auth token and activate authority
    question: How does the hosted-auth page activate an authority once the wallet transaction lands?
  phrasing_ops: 2
  slug: algovoi-co-uk-recurring-hosted-auth-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The resources API from AlgoVoi — 1 operation(s) for resources.
  name: AlgoVoi Resources API
  phrasing_intents:
  - id: get_resource_resources__resource_id__get
    intent: Get a paid resource definition
    question: What price and network is configured for one of my paid resources?
  phrasing_ops: 1
  slug: algovoi-co-uk-resources-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The signup API from AlgoVoi — 2 operation(s) for signup.
  name: AlgoVoi Signup API
  phrasing_intents:
  - id: signup_proxy_signup_create_post
    intent: Sign up a merchant with a wallet
    question: How do I create a merchant account by connecting a wallet?
  - id: cloud_signup_proxy_cloud_signup_create_post
    intent: Sign up a merchant with email
    question: Can I sign up for the cloud service with an email instead of a wallet?
  phrasing_ops: 2
  slug: algovoi-co-uk-signup-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Subscriptions API from AlgoVoi — 6 operation(s) for subscriptions.
  name: AlgoVoi Subscriptions API
  phrasing_intents:
  - id: create_subscription_endpoint_v1_subscriptions_post
    intent: Create a recurring subscription
    question: How do I bill a customer a fixed crypto amount every month?
  - id: list_subscriptions_endpoint_v1_subscriptions_get
    intent: List merchant subscriptions
    question: Which subscriptions are my customers on as a merchant?
  - id: get_subscription_endpoint_v1_subscriptions__subscription_id__get
    intent: Get a subscription
    question: What are the billing terms and status of one subscription?
  - id: update_subscription_endpoint_v1_subscriptions__subscription_id__patch
    intent: Update a subscription's notices and policies
    question: Can I change how far ahead customers are notified of a charge on an existing subscription?
  - id: cancel_subscription_endpoint_v1_subscriptions__subscription_id__cancel_post
    intent: Cancel a subscription as the merchant
    question: How does a merchant cancel a customer's subscription?
  - id: pause_subscription_endpoint_v1_subscriptions__subscription_id__pause_post
    intent: Pause a subscription
    question: Can I pause billing on a subscription without cancelling it?
  - id: resume_subscription_endpoint_v1_subscriptions__subscription_id__resume_post
    intent: Resume a paused subscription
    question: How do I restart billing on a paused subscription?
  - id: list_subscription_invoices_endpoint_v1_subscriptions__subscription_id__invoices_get
    intent: List a subscription's invoices
    question: Which invoices has a subscription generated so far?
  phrasing_ops: 8
  slug: algovoi-co-uk-subscriptions-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The suite-store API from AlgoVoi — 4 operation(s) for suite-store.
  name: AlgoVoi Suite Store API
  phrasing_intents:
  - id: suite_store_checkout_suite_store_checkout_post
    intent: Buy a suite package via hosted checkout
    question: How do I buy an AlgoVoi suite package?
  - id: suite_store_settled_suite_store_settled_post
    intent: Receive a suite store settlement webhook
    question: What happens when a suite store order settles?
  - id: suite_store_activate_suite_store_order__token__activate_post
    intent: Bind a paid suite order to agent DIDs
    question: How do I mint my Agent Mesh licence after paying?
  - id: suite_store_order_status_suite_store_order__token__status_get
    intent: Check a suite store order's status
    question: Has my suite store order been paid and fulfilled?
  phrasing_ops: 4
  slug: algovoi-co-uk-suite-store-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The Verify API from AlgoVoi — 6 operation(s) for verify.
  name: AlgoVoi Verify API
  phrasing_intents:
  - id: verify_verify_post
    intent: Verify an audit bundle
    question: How do I check an audit bundle's integrity without storing it anywhere?
  - id: verify_verify_rfc9421_post
    intent: Verify a signed HTTP message offline
    question: Can I verify an HTTP message signature against the key I expect the signer to hold?
  - id: rfc9421_info_verify_rfc9421_get
    intent: Get the RFC 9421 verifier's input schema
    question: What input does the free RFC 9421 verifier expect?
  - id: explain_verify_rfc9421_explain_post
    intent: Explain why an HTTP signature passes or fails
    question: Why is my RFC 9421 signature failing, and how do I fix it?
  - id: sign_demo_verify_rfc9421_sign_post
    intent: Sign a sample request with a demo key
    question: Is there a reference signer I can diff my own RFC 9421 signer against?
  - id: mpp_verify_v1_verify_post
    intent: Verify an MPP on-chain payment transaction
    question: How does the MPP adapter confirm a payer's on-chain transaction?
  - id: action_ref_info_verify_action_ref_get
    intent: Get the action_ref verifier's input schema
    question: What fields does the action_ref verifier take?
  - id: verify_action_ref_verify_action_ref_post
    intent: Compute the canonical action_ref hash
    question: How do I check my implementation computes the same action_ref hash as production?
  phrasing_ops: 8
  slug: algovoi-co-uk-verify-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The .well Known API from AlgoVoi — 2 operation(s) for .well known.
  name: AlgoVoi .well Known API
  phrasing_intents:
  - id: agent_card__well_known_agent_card_json_get
    intent: Get the agent card
    question: Where is the AlgoVoi A2A agent card published?
  - id: agent_card_legacy__well_known_agent_json_get
    intent: Get the agent card at the legacy path
    question: Is the agent card still served at the older agent.json path?
  phrasing_ops: 2
  slug: algovoi-co-uk-well-known-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The x402 API from AlgoVoi — 2 operation(s) for x402.
  name: AlgoVoi X402 API
  phrasing_intents:
  - id: challenge_x402_challenge_post
    intent: Get x402 payment instructions for a resource
    question: How much and where do I pay for an x402 resource?
  - id: verify_x402_verify_post
    intent: Verify an x402 payment transaction
    question: How do I prove I paid for an x402 resource?
  phrasing_ops: 2
  slug: algovoi-co-uk-x402-api
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: The x402-protected API from AlgoVoi — 1 operation(s) for x402-protected.
  name: AlgoVoi X402 Protected API
  phrasing_intents:
  - id: get_protected_resource_protected__resource_id__get
    intent: Access an x402-protected resource
    question: How do I fetch a resource that is behind an x402 paywall?
  phrasing_ops: 1
  slug: algovoi-co-uk-x402-protected-api
artifact_total: 48
asyncapis:
- description: ''
  name: Algovoi Co Uk Webhooks
  slug: algovoi-co-uk-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/overlays/algovoi-co-uk-pay-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algovoi-co-uk-pay-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/skills/algovoi-co-uk-pay-per-call-verification.md
  title: ''
  type: AgentSkill
  url: skills/algovoi-co-uk-pay-per-call-verification.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/skills/algovoi-co-uk-algovoi.md
  title: ''
  type: AgentSkill
  url: skills/algovoi-co-uk-algovoi.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/skills/algovoi-co-uk-hosted-checkout.md
  title: ''
  type: AgentSkill
  url: skills/algovoi-co-uk-hosted-checkout.md
- group: agent
  title: ''
  type: MCPServer
  url: https://agents.algovoi.co.uk/mcp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/overlays/algovoi-co-uk-clinic-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algovoi-co-uk-clinic-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/skills/algovoi-co-uk-rfc9421-clinic.md
  title: ''
  type: AgentSkill
  url: skills/algovoi-co-uk-rfc9421-clinic.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/overlays/algovoi-co-uk-agent-trust-bench-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algovoi-co-uk-agent-trust-bench-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/overlays/algovoi-co-uk-audit-verifier-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algovoi-co-uk-audit-verifier-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.algovoi.co.uk/mcp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/security/algovoi-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algovoi-co-uk-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/agentic-access/algovoi-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/algovoi-co-uk-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://algovoi.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.algovoi.co.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.algovoi.co.uk/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.algovoi.co.uk/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.algovoi.co.uk/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.algovoi.co.uk/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chopmob-cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://algovoi.co.uk/pricing.html
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.algovoi.co.uk/trial-and-pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.algovoi.co.uk/signup
- group: start
  title: ''
  type: Login
  url: https://dash.algovoi.co.uk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algovoi.co.uk/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algovoi.co.uk/privacy-policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://algovoi.co.uk/compliance.html
- group: auth
  title: ''
  type: Compliance
  url: https://api.algovoi.co.uk/compliance/attestation
- group: auth
  title: ''
  type: Security
  url: https://docs.algovoi.co.uk/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/well-known/algovoi-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/algovoi-co-uk-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://algovoi.co.uk/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/security/algovoi-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/algovoi-co-uk-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/changelog/algovoi-co-uk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/algovoi-co-uk-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.algovoi.co.uk/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/lifecycle/algovoi-co-uk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/algovoi-co-uk-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/llms/algovoi-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algovoi-co-uk-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://algovoi.co.uk/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/llms/algovoi-co-uk-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algovoi-co-uk-docs-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.algovoi.co.uk/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/a2a/algovoi-co-uk-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/algovoi-co-uk-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/mcp/algovoi-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algovoi-co-uk-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/mcp/algovoi-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/algovoi-co-uk-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/well-known/algovoi-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algovoi-co-uk-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://docs.algovoi.co.uk/.well-known/agent-skills/algovoi/skill.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/conformance/algovoi-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algovoi-co-uk-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/errors/algovoi-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algovoi-co-uk-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/authentication/algovoi-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algovoi-co-uk-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/conventions/algovoi-co-uk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/algovoi-co-uk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/conventions/algovoi-co-uk-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/algovoi-co-uk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/asyncapi/algovoi-co-uk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/algovoi-co-uk-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/rate-limits/algovoi-co-uk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/algovoi-co-uk-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/plans/algovoi-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algovoi-co-uk-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/sandbox/algovoi-co-uk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/algovoi-co-uk-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/packages/algovoi-co-uk-packages.yml
  title: ''
  type: Packages
  url: packages/algovoi-co-uk-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/packages/algovoi-co-uk-packages.yml
  title: ''
  type: SDKs
  url: packages/algovoi-co-uk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://docs.algovoi.co.uk/integrations/native-sdks
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/components/algovoi-co-uk-components.yml
  title: ''
  type: Components
  url: components/algovoi-co-uk-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/data-model/algovoi-co-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algovoi-co-uk-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/overlays/algovoi-co-uk-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algovoi-co-uk-gateway-overlay.yaml
- group: other
  title: ''
  type: Subprocessors
  url: https://docs.algovoi.co.uk/compliance#subprocessors
- group: operate
  title: ''
  type: IncidentNotification
  url: https://docs.algovoi.co.uk/security#incident-response
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://algovoi.co.uk/privacy-policy.html#your-rights
- group: other
  title: ''
  type: AITransparency
  url: https://algovoi.co.uk/run-by-a-secure-agent-workforce.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/regulatory/algovoi-co-uk-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/algovoi-co-uk-regulatory-posture.yml
- group: other
  title: ''
  type: Store
  url: https://api.algovoi.co.uk/suite-store
created: '2026-09-19'
description: 'AlgoVoi (AlgoVoi Ltd, UK; founder Christopher Hopley) builds compliance-aware, offline-verifiable payment and evidence infrastructure for AI agents across twelve mainnet chains, answering all four agent-payment protocols — x402, A2A, MPP and AP2 — from one settlement core. It runs two hosted doors: AlgoVoi Pay at pay.algovoi.co.uk, a tenant-free rail that charges 0.01 USDC per call with no account or API key (payment is the credential) and returns an Ed25519 receipt anyone can verify offline, and the multi-tenant Gateway at api.algovoi.co.uk (Bearer key + X-Tenant-Id, hosted checkout, recurring authorities, sanctions screening, hash-chained audit trail, Stripe-shaped signed webhooks). Around them sit an anonymous RFC 9421 signing clinic reachable over REST, A2A and a hosted MCP server, the Agent Trust Bench (187 adversarial x402 research profiles), an audit-bundle verifier, five OpenAPI 3.1 contracts, A2A agent cards on five hosts, a published Agent Skill, llms.txt on four
  hosts, did:web identities, and a large Apache-2.0 reference layer on npm and PyPI (RFC 9421 signer/verifier, JCS substrate, receipt formats, an MCP server). Self-hosted products (Payment Rails, Verifiable Compliance Suite, post-quantum Reseal and Evidence Auditor) sell on perpetual licences paid in USDC.'
image: https://algovoi.co.uk/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: AlgoVoi MCP Server
  slug: algovoi-mcp-server
- description: ''
  name: AlgoVoi MCP Server
  slug: algovoi-mcp-server-2
- description: ''
  name: AlgoVoi MCP Server
  slug: algovoi-mcp-server-3
modified: '2026-09-19'
name: AlgoVoi
nav: Providers
network: true
overview: 'AlgoVoi publishes 38 APIs on the [APIs.io](https://apis.io/) network, including A2a API, Agent Auth API, AlgoVoi Audit Verifier API, and 35 more. Tagged areas include Payments, Agentic Commerce, x402, A2A, and MCP.


  The AlgoVoi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AlgoVoi''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 58 more developer resources.'
plans:
- name: Algovoi Co Uk Plans Pricing
  plan_count: 11
  slug: algovoi-co-uk-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 7
  name: Algovoi Co Uk Rate Limits
  slug: algovoi-co-uk-rate-limits
score:
  band: exemplar
  composite: 67.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 46.5
    developer_ergonomics: 76.2
    discoverability: 90.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 7.9
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Algovoi Co Uk Authentication
  slug: algovoi-co-uk-authentication
  summary_line: http-bearer/apiKey(header)/payment-as-auth(x402)/payment-as-auth(mpp)/hmac-webhook-signature/session-token/none · 9 schemes
- kind: domain-security
  name: Algovoi Co Uk Domain Security
  slug: algovoi-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Algovoi Co Uk Vulnerability Disclosure
  slug: algovoi-co-uk-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: algovoi-co-uk
tags:
- Payments
- Agentic Commerce
- x402
- A2A
- MCP
- Stablecoins
- Cryptocurrency
- Blockchain
- Compliance
- Digital Signature
- Post-Quantum Cryptography
- Verification
- Fintech
- Agent-Native
- Algorand
- United Kingdom
website: https://algovoi.co.uk/
---
