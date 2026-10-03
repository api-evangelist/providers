---
access_model:
  confidence: high
  label: Enterprise · Partner certification required
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://developers.partech.com/engagement-tools/par-punchh/
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 191
  human_in_the_loop: 3
  name: Punchh Agentic Access
  operation_count: 288
  slug: punchh-agentic-access
  summary_line: 288 operations · 191 acting · 3 human-in-the-loop
api_count: 15
apis:
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: Punchh provides robust APIs for integrating POS (Point-of-Sale) terminals with its back end. The integration helps businesses to offer their customers loyalty programs directly from their POS systems.
  name: Punchh POS API
  phrasing_intents:
  - id: pos_redemption_possible
    intent: Check if a redemption can apply to a check
    question: Can the POS verify a reward will work on a check before redeeming it?
  - id: pos_create_redemption
    intent: Redeem a reward or discount on a receipt
    question: How does the POS redeem a guest's reward against a receipt in Redemptions 1.0?
  - id: pos_void_redemption
    intent: Void one processed redemption
    question: How do I undo a single redemption and give the offer back to the guest?
  - id: pos_void_multiple_redemptions
    intent: Void several redemptions at once
    question: Can the POS void multiple redemptions in one request?
  - id: pos_applicable_offers
    intent: List offers that apply to a check
    question: Which of a guest's offers apply to the items on their current check?
  - id: pos_get_active_redemptions
    intent: List a guest's active redemptions at the POS
    question: Which redemptions does a guest currently have open?
  - id: get-api-pos-users-find
    intent: Identify a guest at the POS
    question: How does the POS find a loyalty guest before applying Redemptions 2.0 discounts?
  - id: post-api-auth-discounts-auto_select
    intent: Auto-fill a guest's discount basket
    question: Can discounts be queued into a guest's basket automatically at checkout?
  phrasing_ops: 15
  slug: punchh-pos-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Api2 API from Punchh — 26 operation(s) for api2.
  name: Punchh Api2 API
  phrasing_intents:
  - id: delete-api2-mobile-redemptions
    intent: Cancel an unprocessed redemption from the app
    question: Can a guest cancel a redemption code in the mobile app before it has been used at the store?
  - id: mobile_create_redemption_using_banked_currency
    intent: Redeem banked currency for a redemption code
    question: How can a guest turn part of their banked currency balance into a redemption code?
  - id: mobile_create_redemption_using_visits
    intent: Redeem a completed visit card
    question: In a visit-based loyalty program, how does a guest redeem a completed punch card from the app?
  - id: mobile_create_redemption_using_redeemable
    intent: Redeem loyalty points for a redeemable
    question: How does a guest spend loyalty points on a specific redeemable item from the catalog?
  - id: mobile_create_redemption_using_reward_id
    intent: Redeem a reward a guest was given
    question: How do I generate a redemption code for a reward the guest received from a campaign?
  - id: mobile_list_applicable_offers
    intent: List offers that apply to a cart in the app
    question: Which offers can a guest apply to the items currently in their mobile order?
  - id: sso_create_online_redemption
    intent: Add discounts to the guest's discount basket
    question: How does the mobile app add a reward to the guest's discount basket?
  - id: delete-api-auth-discounts-unselect
    intent: Remove discounts from the discount basket
    question: Can a guest take a discount back out of their basket in the app?
  phrasing_ops: 33
  slug: punchh-api2-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Auth API from Punchh — 14 operation(s) for auth.
  name: Punchh Auth API
  phrasing_intents:
  - id: sso_create_online_redemption
    intent: Redeem a reward against an online order receipt
    question: How does an online ordering site apply a guest's reward or redemption code to a checkout under the older Redemptions 1.0 flow?
  - id: sso_fetch_redemption_code
    intent: Generate a redemption code to use at the POS
    question: How do I get a tracking code a guest can show at the register to redeem a reward?
  - id: sso_void_processed_redemption
    intent: Void a processed Redemptions 1.0 redemption
    question: Can I reverse a redemption that has already been processed and give the offer back to the guest?
  - id: sso_applicable_offers
    intent: List rewards that apply to an online check
    question: Which of the guest's rewards can be used on the items in this online order?
  - id: post-api-auth-discounts-auto_select
    intent: Auto-fill the discount basket for an order
    question: Can the best discount be queued in the guest's basket automatically when auto-redemption is on?
  - id: postApiAuthDiscountsSelect
    intent: Add chosen discounts to the guest's basket
    question: How does an online ordering site add a guest's chosen reward to their discount basket?
  - id: delete-api-auth-discounts-unselect
    intent: Remove discounts from the online discount basket
    question: Can a guest drop a reward from their discount basket before checking out online?
  - id: get-api-auth-discounts-active
    intent: View the guest's current discount basket
    question: What rewards has the guest already put in their discount basket?
  phrasing_ops: 16
  slug: punchh-auth-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Badges API from Punchh — 1 operation(s) for badges.
  name: Punchh Badges API
  phrasing_intents:
  - id: mobile_update_badge
    intent: Link a badge to a Facebook story
    question: How do I attach the Facebook post a guest shared to the badge they earned?
  phrasing_ops: 1
  slug: punchh-badges-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Beacons API from Punchh — 2 operation(s) for beacons.
  name: Punchh Beacons API
  phrasing_intents:
  - id: mobile_record_beacon_entry
    intent: Record a guest entering a beacon's range
    question: What happens when a loyalty member walks into range of a store beacon?
  - id: mobile_record_beacon_exit
    intent: Record a guest leaving a beacon's range
    question: What gets triggered when a guest leaves a store beacon's range?
  phrasing_ops: 2
  slug: punchh-beacons-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Business Admin Users API from Punchh — 3 operation(s) for business admin users.
  name: Punchh Business Admin Users API
  phrasing_intents:
  - id: dashboard_get_admin_roles_list
    intent: List admin roles in the business
    question: Which admin roles have been set up for our business?
  - id: dashboard_create_business_admin
    intent: Create a business admin
    question: Can I add a new dashboard admin directly without sending an invite?
  - id: dashboard_update_business_admin
    intent: Update a business admin
    question: Can I change a business admin's role or details?
  - id: dashboard_show_business_admin
    intent: Get a business admin's details
    question: How can I see the details of one business admin?
  - id: dashboard_delete_business_admin
    intent: Delete a business admin
    question: How do I remove an admin who left the company?
  - id: dashboard_invite_business_admin
    intent: Invite someone to be a business admin
    question: How do I invite a new manager to use the loyalty dashboard?
  phrasing_ops: 6
  slug: punchh-business-admin-users-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Business Migration Users API from Punchh — 3 operation(s) for business migration users.
  name: Punchh Business Migration Users API
  phrasing_intents:
  - id: dashboard_create_business_migration_user
    intent: Add a guest to migrate from an old program
    question: How do I bring a member over from our previous loyalty program with their points?
  - id: dashboard_update_business_migration_user
    intent: Update a business migration user
    question: How do I correct the points or contact details on a migration record?
  - id: dashboard_delete_business_migration_user
    intent: Delete a business migration user
    question: Can I remove a guest from the migration list before they're imported?
  - id: post-api2-dashboard-migration_users-bulk_bmu_upload
    intent: Bulk upload migration users from a CSV
    question: Can I upload a whole CSV of members from our previous loyalty program at once?
  phrasing_ops: 4
  slug: punchh-business-migration-users-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Challenges API from Punchh — 5 operation(s) for challenges.
  name: Punchh Challenges API
  phrasing_intents:
  - id: mobile_list_challenges
    intent: List the business's challenges
    question: What challenges is the brand running for loyalty members right now?
  - id: mobile_Fetch_challenge_details
    intent: Get details of one challenge
    question: What are the rules and rewards of a specific challenge?
  - id: mobile_list_user_challenges
    intent: List a guest's available, active and past challenges
    question: Which challenges has this guest joined and how far along are they?
  - id: put-api2-mobile-challenge_opt_in
    intent: Opt a guest into a challenge
    question: How does a guest explicitly join a challenge campaign?
  - id: put-api2-mobile-challenge_opt_out
    intent: Opt a guest out of a challenge
    question: Can a guest leave a challenge they already joined?
  phrasing_ops: 5
  slug: punchh-challenges-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Check-in API from Punchh — 3 operation(s) for check-in.
  name: Punchh Check In API
  phrasing_intents:
  - id: sso_loyalty_checkin
    intent: Award loyalty for an online order
    question: How does a signed-in guest earn points for an online order?
  - id: sso_update_loyalty_checkin
    intent: Update a pending online order check-in
    question: How do I change the details of an online order check-in that's still pending?
  - id: sso_void_loyalty_checkin
    intent: Void a pending loyalty check-in
    question: How do I cancel a pending check-in when an online order is abandoned?
  - id: sso_create_loyalty_checkin
    intent: Check a guest in by store number (legacy)
    question: Is there an older endpoint that checks a guest in using only a store number?
  - id: sso_Fetch_a_Checkin_by_external_uid
    intent: Look up a check-in by its external ID
    question: How do I retrieve a loyalty check-in using the ID my ordering system assigned?
  - id: post-api2-dashboard-checkins
    intent: Create a check-in without the guest's token
    question: How can I award points for a future-dated order when I don't have the guest's access token?
  phrasing_ops: 6
  slug: punchh-check-in-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Check-ins API from Punchh — 6 operation(s) for check-ins.
  name: Punchh Check Ins API
  phrasing_intents:
  - id: mobile_create_loyalty_checkin_by_barcode
    intent: Earn points by scanning a receipt barcode
    question: How does a guest get points by scanning the barcode on their receipt?
  - id: mobile_create_loyalty_checkin_by_qr_code
    intent: Earn points by scanning a QR code
    question: Can guests earn loyalty points by scanning a QR code in the app?
  - id: mobile_create_loyalty_checkin_by_receipt_image
    intent: Earn points by uploading a receipt photo
    question: Can a guest snap a photo of a receipt to get loyalty credit?
  - id: mobile_Fetch_checins
    intent: List a guest's check-ins
    question: Where can a guest see all of their past check-ins?
  - id: mobile_account_balance
    intent: Get a guest's rewards and banked balance
    question: What membership level and banked currency does a guest have?
  - id: mobile_transaction_details
    intent: Get details of one transaction
    question: How can a guest see what happened on a specific transaction?
  phrasing_ops: 6
  slug: punchh-check-ins-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Check User Balance API from Punchh — 4 operation(s) for check user balance.
  name: Punchh Check User Balance API
  phrasing_intents:
  - id: sso_account_balance
    intent: Get a guest's points and credit totals
    question: What is a guest's points balance and membership level?
  - id: sso_list_available_rewards
    intent: List rewards available to a guest
    question: Which rewards or offers can a guest use right now?
  - id: sso_fetch_user_balance
    intent: Get balance with redemptions, badges and notices
    question: Can I get a guest's active redemptions and badges with their balance?
  - id: sso_balance_timelines
    intent: Show a guest's balance over time
    question: How has a signed-in guest's balance changed over time?
  phrasing_ops: 4
  slug: punchh-check-user-balance-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Collectibles API from Punchh — 3 operation(s) for collectibles.
  name: Punchh Collectibles API
  phrasing_intents:
  - id: get-api2-mobile-collectibles
    intent: List the business's digital collectibles
    question: What digital collectibles can guests earn from this brand?
  - id: get-api2-mobile-collectibles-collectible_id
    intent: Get details of one collectible
    question: Which active campaigns award a particular collectible?
  - id: get-api2-mobile-users_collectibles
    intent: List collectibles a guest has earned
    question: Which collectibles has this guest earned so far?
  phrasing_ops: 3
  slug: punchh-collectibles-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Coupons API from Punchh — 1 operation(s) for coupons.
  name: Punchh Coupons API
  phrasing_intents:
  - id: mobile_apply_coupons
    intent: Apply a coupon or promo code
    question: How does a guest enter a promo code in the app to get a reward?
  phrasing_ops: 1
  slug: punchh-coupons-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Custom Segments API from Punchh — 5 operation(s) for custom segments.
  name: Punchh Custom Segments API
  phrasing_intents:
  - id: dashboard_list_all_custom_segments
    intent: List all custom segments
    question: What custom segments has my business created?
  - id: dashboard_create_custom_segment
    intent: Create an empty custom segment
    question: How do I create a new custom segment to hold a hand-picked list of guests?
  - id: dashboard_update_custom_segment
    intent: Rename or redescribe a custom segment
    question: Can I change the name or description of an existing custom segment?
  - id: dashboard_delete_custom_segment
    intent: Delete a custom segment
    question: How do I permanently remove a custom segment we no longer use?
  - id: dashboard_search_user_in_custom_segment
    intent: Check whether a guest is in a custom segment
    question: Is a particular guest already a member of this custom segment?
  - id: dashboard_add_user_to_custom_segment
    intent: Add one guest to a custom segment
    question: How do I add a single guest to a custom segment?
  - id: dashboard_remove_user_from_custom_segment
    intent: Remove one guest from a custom segment
    question: How do I take a single guest out of a custom segment?
  - id: post-api2-dashboard-custom_segments-members-bulk_add
    intent: Bulk add guests to a segment from a CSV
    question: Can I upload a CSV of user IDs and emails to fill a custom segment?
  phrasing_ops: 10
  slug: punchh-custom-segments-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Deals API from Punchh — 2 operation(s) for deals.
  name: Punchh Deals API
  phrasing_intents:
  - id: sso_list_all_deals
    intent: List deals available to a guest
    question: Which deals can a signed-in web guest choose from?
  - id: sso_save_selected_deals
    intent: Save a deal to a guest's account
    question: How does a web guest add a deal to their account?
  - id: sso_get_the_deal_detail
    intent: Get the details of a deal
    question: What does a particular deal include before a guest saves it?
  phrasing_ops: 3
  slug: punchh-deals-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Drive-Thru API from Punchh — 1 operation(s) for drive-thru.
  name: Punchh Drive Thru API
  phrasing_intents:
  - id: post-api2-mobile-drivethru_code
    intent: Generate a drive-thru loyalty short code
    question: How can a guest identify themselves at the drive-thru window by saying a short code?
  phrasing_ops: 1
  slug: punchh-drive-thru-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The eClub API from Punchh — 1 operation(s) for eclub.
  name: Punchh E Club API
  phrasing_intents:
  - id: dashboard_eclub_guest_upload
    intent: Upload or update eClub guests
    question: How do I bulk add email club guests collected at a store?
  phrasing_ops: 1
  slug: punchh-eclub-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Feedback API from Punchh — 4 operation(s) for feedback.
  name: Punchh Feedback API
  phrasing_intents:
  - id: mobile_create_feedback
    intent: Submit guest feedback from the app
    question: How does a guest leave a rating and comment about a visit in the app?
  - id: mobile_update_feedback
    intent: Attach media to feedback from the app
    question: Can a guest add a photo or video to feedback they already sent from the app?
  - id: post-api2-dashboard-feedbacks
    intent: Record feedback for a guest from the back end
    question: How can our support system log feedback for a guest without their access token?
  - id: patch-api2-dashboard-feedbacks-feedback_id
    intent: Update a guest's feedback from the back end
    question: Can an admin edit the message on feedback that was already recorded?
  phrasing_ops: 4
  slug: punchh-feedback-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The File Upload API from Punchh — 1 operation(s) for file upload.
  name: Punchh File Upload API
  phrasing_intents:
  - id: mobile_file_upload
    intent: Get a signed URL to upload a file
    question: How does the app get a signed URL to upload a photo?
  phrasing_ops: 1
  slug: punchh-file-upload-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Franchisee API from Punchh — 1 operation(s) for franchisee.
  name: Punchh Franchisee API
  phrasing_intents:
  - id: dashboard_create_franchisee
    intent: Create a franchisee for locations
    question: How does a business admin set up a new franchisee for their locations?
  - id: dashboard_update_franchisee
    intent: Update a franchisee's details
    question: Can I change the details of an existing franchisee?
  - id: dashboard_delete_franchisee
    intent: Delete a franchisee
    question: How do I remove a franchisee that no longer operates our stores?
  phrasing_ops: 3
  slug: punchh-franchisee-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Game API from Punchh — 1 operation(s) for game.
  name: Punchh Game API
  phrasing_intents:
  - id: get-api2-mobile-par_games
    intent: List active game URLs for the app
    question: Which games has the brand set up for guests to play in the app?
  phrasing_ops: 1
  slug: punchh-game-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Gift Cards API from Punchh — 14 operation(s) for gift cards.
  name: Punchh Gift Cards API
  phrasing_intents:
  - id: mobile_purchase_gift_card
    intent: Buy a new gift card in the app
    question: How does a guest buy a brand-new gift card for themselves in the app?
  - id: mobile_reload_gift_card
    intent: Add funds to an existing gift card
    question: Can a guest top up the balance on a gift card they already have?
  - id: mobile_import_physical_gift_card
    intent: Add a physical gift card to the app
    question: How can a guest load a plastic gift card into their app wallet?
  - id: mobile_udpate_gift_card
    intent: Rename a gift card or set auto-reload
    question: Can a guest turn on auto-reload when their gift card balance gets low?
  - id: mobile_delete_gift_card
    intent: Remove a gift card from the guest's app
    question: Can a guest hide a gift card from their app without deleting it from the system?
  - id: mobile_fetch_gift_cards
    intent: List a guest's active gift cards
    question: Which gift cards does the guest currently have in their app?
  - id: mobile_fetch_gift_card_balance
    intent: Check a gift card's balance
    question: How much money is left on a particular gift card?
  - id: mobile_fetch_gift_card_transaction_history
    intent: View a gift card's transaction history
    question: Where can a guest see past purchases and reloads on a gift card?
  phrasing_ops: 15
  slug: punchh-gift-cards-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Invitations API from Punchh — 4 operation(s) for invitations.
  name: Punchh Invitations API
  phrasing_intents:
  - id: mobile_get_invitations
    intent: List a guest's pending invitations
    question: Which gift card invitations are still waiting for this guest?
  - id: Mobile_Create_Gift_Card_Claim_Token
    intent: Create a claim token to hand off a gift card
    question: How do I generate a claim link or token so someone else can take my gift card?
  - id: mobile_Check_Status_of_the_claim_token
    intent: Check whether a gift card claim token is valid
    question: Is this gift card claim token still valid?
  - id: Mobile_delete_an_invitation_claim_token
    intent: Delete a gift card invitation
    question: How do I cancel a gift card invitation I sent by mistake?
  - id: mobile_transfer_a_gift_card_using_invitation_claim_token
    intent: Claim a gift card with an invitation token
    question: How does the recipient accept a gift card that was sent with a claim token?
  phrasing_ops: 5
  slug: punchh-invitations-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Locations API from Punchh — 9 operation(s) for locations.
  name: Punchh Locations API
  phrasing_intents:
  - id: mobile_location_configuration
    intent: Get a store location's configuration
    question: What configuration does a store location expose to the app or POS?
  - id: mobile_diagnostic_logs
    intent: Send POS diagnostic logs for a location
    question: How do I report POS terminal diagnostics for a store to the loyalty platform?
  - id: mobile_search_locations
    intent: Find nearby store locations
    question: Which restaurant locations are closest to a guest's GPS position?
  - id: dashboard_get_location_list
    intent: List a business's locations
    question: How do I get all store locations and their details for a business?
  - id: dashboard_create_location
    intent: Create a store location
    question: What admin permission do I need to add a new store location?
  - id: dashboard_update_location
    intent: Edit a store location
    question: Can I change a store location's details after it was created?
  - id: dashboard_delete_location
    intent: Delete a store location immediately
    question: How do I remove a closed store location from the business right away?
  - id: dashboard_get_location_group_list
    intent: List location groups and their stores
    question: Which location groups exist and which stores are in each?
  phrasing_ops: 16
  slug: punchh-locations-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Loyalty Transfers API from Punchh — 3 operation(s) for loyalty transfers.
  name: Punchh Loyalty Transfers API
  phrasing_intents:
  - id: mobile_loyalty_transfer_points
    intent: Send loyalty points to another member
    question: Can a guest give some of their loyalty points to a friend?
  - id: mobile_loyalty_transfer_currency
    intent: Send banked reward currency to another member
    question: Can a guest share their banked reward dollars with a family member?
  - id: mobile_loyalty_transfer_reward
    intent: Give a loyalty reward to another member
    question: Can a guest gift one of their earned rewards to someone else?
  phrasing_ops: 3
  slug: punchh-loyalty-transfers-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Meta API from Punchh — 1 operation(s) for meta.
  name: Punchh Meta API
  phrasing_intents:
  - id: dashboard_meta_api
    intent: List the business's redeemables for admins
    question: Which redeemables has our business created?
  phrasing_ops: 1
  slug: punchh-meta-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Meta & Version API from Punchh — 3 operation(s) for meta & version.
  name: Punchh Meta & Version API
  phrasing_intents:
  - id: mobile_program_meta_API
    intent: Get loyalty program details for the app
    question: How does the mobile app learn the program type, locations and redeemables for a business?
  - id: mobile_version_note
    intent: Get release notes for an app version
    question: What changed in a specific version of the brand's app?
  - id: mobile_making_batch_requests
    intent: Send several mobile API calls in one request
    question: Can the app bundle several API calls into a single HTTP request?
  phrasing_ops: 3
  slug: punchh-meta-version-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Migration API from Punchh — 2 operation(s) for migration.
  name: Punchh Migration API
  phrasing_intents:
  - id: mobile_generate_otp_token
    intent: Send a migration one-time password
    question: Can I email a guest a one-time password to move their old loyalty account?
  - id: mobile_verify_token
    intent: Verify a migration one-time password
    question: How do I confirm the OTP a guest received during account migration?
  - id: mobile_migration_lookup
    intent: Get a guest's migrated account details
    question: What details were imported for a guest from the old loyalty program?
  - id: mobile_basic_migration_lookup
    intent: Check if a guest is in migration data
    question: Is a guest present in the business's imported migration data?
  phrasing_ops: 4
  slug: punchh-migration-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Notifications API from Punchh — 5 operation(s) for notifications.
  name: Punchh Notifications API
  phrasing_intents:
  - id: mobile_fetch_user_notifications
    intent: List a guest's push notifications
    question: Which push notifications has a guest received in the app?
  - id: mobile_delete_user_notification
    intent: Delete a guest's notification
    question: How does a guest clear a notification from their inbox?
  - id: mobile_messages
    intent: List rich messages for a guest
    question: What rich messages are available for a guest to view in the app?
  - id: mobile_mark_messages_read
    intent: Mark rich messages as read
    question: Can I mark a guest's user-specific rich messages as read?
  - id: mobile_delete_messages
    intent: Delete a rich message
    question: How does a guest dismiss a user-specific rich message for good?
  phrasing_ops: 5
  slug: punchh-notifications-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Offers API from Punchh — 2 operation(s) for offers.
  name: Punchh Offers API
  phrasing_intents:
  - id: mobile_list_user_offers
    intent: List a guest's offers in the app
    question: Which offers does a guest currently have in the app?
  - id: mobile_mark_read
    intent: Mark offers as read
    question: Can I record that a guest opened an offer from a push notification?
  phrasing_ops: 2
  slug: punchh-offers-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Passcodes API from Punchh — 2 operation(s) for passcodes.
  name: Punchh Passcodes API
  phrasing_intents:
  - id: mobile_forgot_passcode
    intent: Email a guest a passcode reset link
    question: What happens when a guest taps reset passcode in the app?
  - id: mobile_create_passcode
    intent: Set a secondary passcode for a guest
    question: How does a guest set up a PIN to protect gift cards and payments in the app?
  phrasing_ops: 2
  slug: punchh-passcodes-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Payment Cards API from Punchh — 2 operation(s) for payment cards.
  name: Punchh Payment Cards API
  phrasing_intents:
  - id: create_api2-mobile-payment_cards
    intent: Save a payment card to the guest's app
    question: How does the app save a guest's credit card for future purchases?
  - id: get-api2-mobile-payment_cards
    intent: List a guest's saved payment cards
    question: Which credit cards has the guest saved in the app?
  - id: put-api2-mobile-payment_cards
    intent: Rename or set a saved card as default
    question: Can a guest change the nickname on a saved card?
  - id: delete-api2-mobile-payment_cards
    intent: Delete a saved payment card
    question: How does a guest remove a credit card they no longer use from the app?
  phrasing_ops: 4
  slug: punchh-payment-cards-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Payments API from Punchh — 7 operation(s) for payments.
  name: Punchh Payments API
  phrasing_intents:
  - id: mobile_fetch_client_token
    intent: Get a secure client token for a service
    question: How does the app get a secure token for gift card or online ordering services?
  - id: mobile_get_client_token
    intent: Get a payment gateway client token
    question: Where does the app get a client token to start a card payment?
  - id: mobile_record_payment
    intent: Record an in-app payment
    question: How does the app record a payment after the guest enters their card?
  - id: get-api2-mobile-iframe_payments-new
    intent: Get a PAR Pay card entry page for a token
    question: How does a guest save a payment card to buy or reload gift cards?
  - id: pos_create_payment_ssf
    intent: Charge a payment at the POS via single scan
    question: How does the POS charge a guest who scanned a single scan code?
  - id: pos_update_payments
    intent: Mark a POS payment's status
    question: How does the POS tell the loyalty platform a payment is complete?
  - id: pos_void_payments
    intent: Void or cancel a POS payment
    question: How do I cancel a payment request that hasn't settled yet?
  - id: pos_get_payments_status
    intent: Check a POS payment's status
    question: Did the guest's payment succeed, or was it cancelled?
  phrasing_ops: 9
  slug: punchh-payments-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Point Of Sale API from Punchh — 8 operation(s) for point of sale.
  name: Punchh Point Of Sale API
  phrasing_intents:
  - id: pos_location_config
    intent: Get a store location's POS configuration
    question: How does a POS terminal pull the loyalty settings for its own store location?
  - id: pos_program_meta
    intent: Get loyalty program details for the POS
    question: What program type and redeemables does the register need to know about this loyalty program?
  - id: pos_create_user
    intent: Enroll a new loyalty member at the register
    question: Can a cashier sign a guest up for loyalty right at the POS with just a phone number?
  - id: pos_user_search
    intent: Look up a loyalty guest and their balance at the POS
    question: How does the register find a guest's loyalty account by phone, email or QR code?
  - id: pos_checkin
    intent: Award loyalty for an in-store check
    question: How does the POS credit a guest with points for a purchase they just made in store?
  - id: receipt_details
    intent: Send receipt details from the POS
    question: How do I push every receipt from my POS so guests can scan it later for points?
  - id: pos_create_transaction
    intent: Record a visit without earning loyalty
    question: Can I log a guest's store visit without giving them any points?
  - id: get-api-pos-users-balance
    intent: Fetch a guest's account balance and subscriptions
    question: What points, rewards and subscription benefits does a guest have available at the register?
  phrasing_ops: 8
  slug: punchh-point-of-sale-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Redemptions API from Punchh — 2 operation(s) for redemptions.
  name: Punchh Redemptions API
  phrasing_intents:
  - id: dashboard_search_redemption_code
    intent: Look up a redemption code
    question: Is a guest's redemption code valid, and what does it unlock?
  - id: dashboard_process_redemption
    intent: Mark a redemption code as processed
    question: How do I mark a redemption as used once the guest has received the item?
  - id: dashboard_force_redeem
    intent: Force-redeem an offer for a guest
    question: Can a manager override the normal flow and redeem an offer for a guest?
  phrasing_ops: 3
  slug: punchh-redemptions-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Referrals API from Punchh — 1 operation(s) for referrals.
  name: Punchh Referrals API
  phrasing_intents:
  - id: mobile_fetch_possible_referrers
    intent: List who may have referred a guest
    question: Which members might have referred a new guest to the loyalty program?
  - id: mobile_select_referrer
    intent: Choose the member who referred a guest
    question: How does a guest credit the friend who referred them?
  phrasing_ops: 2
  slug: punchh-referrals-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Rewards API from Punchh — 5 operation(s) for rewards.
  name: Punchh Rewards API
  phrasing_intents:
  - id: sso_estimate_loyalty_points_earning
    intent: Estimate points from an order subtotal
    question: How many points would a guest earn on a $25 subtotal before they check out?
  - id: sso_points_conversion_api
    intent: Convert points to cash, fuel or charity
    question: Can a guest turn loyalty points into cash credit or a fuel discount?
  - id: sso_estimate_points_earning
    intent: Estimate points for a cart with menu items
    question: What would the items in this cart earn in points before the order is placed?
  - id: sso_ordering_meta
    intent: Get the base redeemable for ordering
    question: What is the base redeemable configured for online ordering?
  - id: sso_auth_fetchavailableoffers
    intent: List offers available to a guest
    question: How many offers does this guest have available right now?
  phrasing_ops: 5
  slug: punchh-rewards-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Single Scan Code API from Punchh — 1 operation(s) for single scan code.
  name: Punchh Single Scan Code API
  phrasing_intents:
  - id: mobile_gen_ssc
    intent: Generate a single scan code for checkout
    question: Can a guest pay, redeem a reward and tip with one scan at the register?
  phrasing_ops: 1
  slug: punchh-single-scan-code-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Social Cause Campaign API from Punchh — 2 operation(s) for social cause campaign.
  name: Punchh Social Cause Campaign API
  phrasing_intents:
  - id: mobile_get_social_cause_campaigns
    intent: Search active charity campaigns
    question: Which charities can guests donate to through the loyalty app?
  - id: Mobile_Create_donation
    intent: Donate to a social cause campaign
    question: How does a guest donate points or money to a charity campaign?
  - id: mobile_social_cause_campaign_details
    intent: View a guest's donations to a cause
    question: How much has this guest donated to a particular charity campaign?
  phrasing_ops: 3
  slug: punchh-social-cause-campaign-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Social Cause Campaigns API from Punchh — 3 operation(s) for social cause campaigns.
  name: Punchh Social Cause Campaigns API
  phrasing_intents:
  - id: dashboard_create_social_cause_campaigns
    intent: Create a social cause campaign
    question: How do I set up a charity campaign that loyalty guests can support?
  - id: dashboard_social_cause_activate
    intent: Activate a social cause campaign
    question: How do I make a social cause campaign live for guests?
  - id: dashboard_social_cause_deactivate
    intent: Deactivate a social cause campaign
    question: How do I end a charity campaign once the fundraising period is over?
  phrasing_ops: 3
  slug: punchh-social-cause-campaigns-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Surveys API from Punchh — 1 operation(s) for surveys.
  name: Punchh Surveys API
  phrasing_intents:
  - id: mobile_fetch_user_survey
    intent: Get the link to a guest's survey
    question: Where can a guest find the survey they've been asked to complete?
  phrasing_ops: 1
  slug: punchh-surveys-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Swag API from Punchh — 4 operation(s) for swag.
  name: Punchh Swag API
  phrasing_intents:
  - id: mobile_update_user_banking_preferences
    intent: Opt a guest in or out of saving points for swag
    question: Can a guest stop points from auto-converting so they can save for merch?
  - id: mobile_get_user_banking_preferences
    intent: Get a guest's Save Points for Swag settings
    question: Has a guest opted in to saving points for swag?
  - id: mobile_create_swag_redemption
    intent: Redeem saved points for a swag item
    question: How does a guest trade saved points for branded merchandise?
  - id: mobile_fetch_available_user_merch
    intent: List swag items a guest can redeem
    question: What branded merch can a guest get with their points?
  - id: dashboard_get_swag_shipping_details
    intent: Export shipping details for swag deliveries
    question: Which swag redemptions need to be shipped this week?
  phrasing_ops: 5
  slug: punchh-swag-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The User Management API from Punchh — 5 operation(s) for user management.
  name: Punchh User Management API
  phrasing_intents:
  - id: sso_forgot_password
    intent: Send a guest a password reset email
    question: How does a guest on the web ordering site reset a forgotten password?
  - id: sso_fetch_user_informaton
    intent: Get a signed-in guest's profile details
    question: Can I read a guest's birthday, anniversary and zip code after SSO login?
  - id: sso_update_user_information
    intent: Update a guest's profile or password
    question: Can a guest change their name or anniversary from the website?
  - id: sso_account_history
    intent: Get a guest's account history
    question: Where can a web guest see their check-ins and other loyalty events?
  - id: sso_change_password
    intent: Change a guest's password without the old one
    question: Can a guest set a new password without entering their current one?
  - id: sso_user_enrollment
    intent: Enroll a guest in a social cause campaign
    question: Can a guest join a charity campaign from the web ordering site?
  - id: sso_user_disenrollment
    intent: Disenroll a guest from a campaign
    question: How does a web guest leave a social cause campaign?
  phrasing_ops: 7
  slug: punchh-user-management-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The User Sign-up and SSO API from Punchh — 8 operation(s) for user sign-up and sso.
  name: Punchh User Sign-up and SSO API
  phrasing_intents:
  - id: sso_signup
    intent: Register a new guest account online
    question: How does an online ordering site register a new loyalty guest with email and password?
  - id: sso_login
    intent: Log a guest in with email and password
    question: How do I sign an existing guest in with their email and password?
  - id: sso_create_acces_token_for_sso
    intent: Exchange a security token for an auth token
    question: How does a partner site turn its SSO security token into a guest authentication token?
  - id: sso_Get_reset_password_token_of_the_user
    intent: Get a password reset token for a guest
    question: How can a guest who forgot their password get a reset token?
  - id: oauth_token
    intent: Exchange an OAuth code for an SSO token
    question: After a guest logs in on the hosted sign-in form, how do I get an access token from the authorization code?
  - id: sso_connect_with_facebook
    intent: Sign a guest in or up with Facebook
    question: Can guests register for loyalty using their Facebook account?
  - id: Sign_in_with_apple
    intent: Sign a guest in with Apple
    question: Can guests use Sign in with Apple on the web ordering site?
  - id: post-api-auth-users-connect_with_google
    intent: Sign a guest in with Google
    question: How do I let guests log in with their Google account on the web?
  phrasing_ops: 8
  slug: punchh-user-sign-up-and-sso-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The Users API from Punchh — 35 operation(s) for users.
  name: Punchh Users API
  phrasing_intents:
  - id: mobile_signin
    intent: Sign a guest in to the loyalty app
    question: How do I log a guest into a restaurant's loyalty app with their email and password?
  - id: mobile_connect_with_facebook
    intent: Register or log in a guest with Facebook
    question: Can guests register on the loyalty app using their Facebook account?
  - id: mobile_login_with_apple
    intent: Sign a guest in with Apple
    question: Does the loyalty app support Sign in with Apple using Apple's private relay email?
  - id: mobile_logout
    intent: Log a guest out of the mobile app
    question: How do I end a guest's session in the mobile loyalty app?
  - id: mobile_fetch_user_information
    intent: Get the signed-in guest's profile
    question: What profile details can the app show for the guest who is signed in?
  - id: mobile_update_user_profile
    intent: Update the signed-in guest's profile
    question: Can a guest change their own name or phone number from the mobile app?
  - id: mobile_sign_up
    intent: Register a new guest in the mobile app
    question: How do I sign up a new guest on a business's loyalty app?
  - id: delete-api2-mobile-users
    intent: Request deletion of the guest's own account
    question: Can a guest ask to have their loyalty account deleted from inside the app?
  phrasing_ops: 43
  slug: punchh-users-api
- baseURL: https://{server_name}.punchh.com
  baseurl_source: declared
  description: The WiFi Acquisition API from Punchh — 2 operation(s) for wifi acquisition.
  name: Punchh WiFi Acquisition API
  phrasing_intents:
  - id: mobile_wifi_enrollment
    intent: Check a WiFi guest's email from the captive portal
    question: Can the WiFi login page check whether a guest's email is already a member?
  - id: mobile_enroll_guest_for_wifi
    intent: Enroll a guest from the WiFi captive portal
    question: How does a guest who logs into store WiFi join the eClub from the portal?
  - id: dashboard_guest_lookup_for_wifi_enrollment
    intent: Check a WiFi guest by email or phone as an admin
    question: Using an admin key, can I check if a phone number already belongs to a member?
  - id: dashboard_enroll_guests_for_wifi
    intent: Enroll WiFi guests into eClub as an admin
    question: Can a WiFi vendor enroll guests into the eClub with a business admin key?
  phrasing_ops: 4
  slug: punchh-wifi-acquisition-api
artifact_total: 132
asyncapis:
- description: ''
  name: Punchh Webhooks
  slug: punchh-webhooks
collections:
- collection_type: postman
  name: PAR Punchh Mobile Check-In API
  slug: postman-punchh-check-in-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Check-Ins API
  slug: postman-punchh-check-ins-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Configuration API
  slug: postman-punchh-configuration-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Offers API
  slug: postman-punchh-offers-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Receipts API
  slug: postman-punchh-receipts-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Redemptions API
  slug: postman-punchh-redemptions-api
- collection_type: postman
  name: PAR Punchh Mobile Check-In Users API
  slug: postman-punchh-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mobile API
  slug: open-punchh-mobile-api
- collection_type: open
  name: Redemptions 1.0 (Legacy) API - Mobile
  slug: open-punchh-mobile-redemptions-legacy
- collection_type: open
  name: Redemptions 2.0 (New) API - Mobile
  slug: open-punchh-mobile-redemptions-v2
- collection_type: open
  name: Subscription API - Mobile
  slug: open-punchh-mobile-subscription
- collection_type: open
  name: PAR Punchh Mobile API
  slug: open-punchh-mobile
- collection_type: open
  name: Redemptions 1.0 (Legacy) API - Online Ordering
  slug: open-punchh-online-ordering-redemptions-legacy
- collection_type: open
  name: Redemptions 2.0 (New) API - Online Ordering
  slug: open-punchh-online-ordering-redemptions-v2
- collection_type: open
  name: Online Ordering and SSO API
  slug: open-punchh-online-ordering-sso-api
- collection_type: open
  name: Subscription API - Online Ordering
  slug: open-punchh-online-ordering-subscription
- collection_type: open
  name: PAR Punchh Online Ordering and SSO API
  slug: open-punchh-online-ordering
- collection_type: open
  name: Platform Functions API
  slug: open-punchh-platform-functions-api
- collection_type: open
  name: Headless Offers API - Platform Functions
  slug: open-punchh-platform-functions-headless-offers
- collection_type: open
  name: Offers Ingestion API - Platform Functions
  slug: open-punchh-platform-functions-offers-ingestion
- collection_type: open
  name: Subscription API - Platform Functions
  slug: open-punchh-platform-functions-subscription
- collection_type: open
  name: PAR Punchh Platform Functions API
  slug: open-punchh-platform-functions
- collection_type: open
  name: POS API
  slug: open-punchh-pos-api
- collection_type: open
  name: Redemptions 1.0 (Legacy) API - POS
  slug: open-punchh-pos-redemptions-legacy
- collection_type: open
  name: Redemptions 2.0 (New) API - POS
  slug: open-punchh-pos-redemptions-v2
- collection_type: open
  name: PAR Punchh POS and Kiosk API
  slug: open-punchh-pos
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-mobile-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-mobile-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-mobile-redemptions-legacy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-mobile-redemptions-legacy-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-mobile-redemptions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-mobile-redemptions-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-mobile-subscription-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-mobile-subscription-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-online-ordering-redemptions-legacy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-online-ordering-redemptions-legacy-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-online-ordering-redemptions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-online-ordering-redemptions-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-online-ordering-sso-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-online-ordering-sso-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-online-ordering-subscription-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-online-ordering-subscription-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-platform-functions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-platform-functions-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-platform-functions-headless-offers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-platform-functions-headless-offers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-platform-functions-offers-ingestion-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-platform-functions-offers-ingestion-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-platform-functions-subscription-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-platform-functions-subscription-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-pos-redemptions-legacy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-pos-redemptions-legacy-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/overlays/punchh-pos-redemptions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/punchh-pos-redemptions-v2-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/punchh/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/agentic-access/punchh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/punchh-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/security/punchh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/punchh-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/security/punchh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/punchh-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/authentication/punchh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/punchh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://punchh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.partech.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.partech.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.partech.com/docs/dev-portal-developer-resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/punchh
- group: company
  title: ''
  type: Blog
  url: https://punchh.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/partechnology
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/rules/punchh-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/punchh-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/vocabulary/punchh-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/punchh-vocabulary.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/plans/punchh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/punchh-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/rate-limits/punchh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/punchh-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/finops/punchh-finops.yml
  title: ''
  type: FinOps
  url: finops/punchh-finops.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.partech.com/docs/dev-portal-webhooks-manager/8c18e3660f73f-event-guest
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/conventions/punchh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/punchh-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/conventions/punchh-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/punchh-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/errors/punchh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/punchh-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/lifecycle/punchh-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/punchh-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.punchh.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/lifecycle/punchh-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/punchh-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/conformance/punchh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/punchh-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/data-model/punchh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/punchh-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/asyncapi/punchh-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/punchh-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/sandbox/punchh-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/punchh-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/changelog/punchh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/punchh-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/packages/punchh-packages.yml
  title: ''
  type: Packages
  url: packages/punchh-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/llms/punchh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/punchh-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/mcp/punchh-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/punchh-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/security/punchh-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/punchh-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partech.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://punchh.com/contact/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.partech.com/docs/dev-portal-developer-resources
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://punchh.com/security/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/par-tech/workspace/par-tech-apis-official
created: '2026-06-02'
description: Punchh, now part of PAR Technology and offered under the PAR Engagement brand, is an enterprise loyalty, offers, and customer engagement platform for restaurants. It unifies guest data from online ordering, mobile apps, POS, and kiosks into a single view so brands can run personalized loyalty and marketing programs. PAR exposes well-documented Punchh APIs through its developer portal covering platform functions, mobile, online ordering, POS and kiosk integration, and a webhooks manager, with sample collections published to Postman. Most integration surfaces require partner certification. Over 275 restaurant brands rely on Punchh to grow customer lifetime value.
examples:
- key_count: 4
  name: Mobile Access Token Example
  slug: mobile-access-token-example
- key_count: 4
  name: Mobile Create User Request Example
  slug: mobile-create-user-request-example
- key_count: 2
  name: Mobile Login Request Example
  slug: mobile-login-request-example
- key_count: 4
  name: Mobile Mark Offers Read Request Example
  slug: mobile-mark-offers-read-request-example
- key_count: 2
  name: Mobile Transaction Details Example
  slug: mobile-transaction-details-example
- key_count: 2
  name: Mobile Transaction Details Request Example
  slug: mobile-transaction-details-request-example
- key_count: 2
  name: Mobile Update User Profile Request Example
  slug: mobile-update-user-profile-request-example
- key_count: 2
  name: Mobile User Session Example
  slug: mobile-user-session-example
- key_count: 12
  name: Online Ordering Online Order Checkin Request Example
  slug: online-ordering-online-order-checkin-request-example
- key_count: 5
  name: Online Ordering Online Order Checkin Response Example
  slug: online-ordering-online-order-checkin-response-example
- key_count: 7
  name: Online Ordering Online Order Redemption Request Example
  slug: online-ordering-online-order-redemption-request-example
- key_count: 7
  name: Online Ordering Online Order Redemption Response Example
  slug: online-ordering-online-order-redemption-response-example
- key_count: 5
  name: Platform Functions Redeemable Example
  slug: platform-functions-redeemable-example
- key_count: 4
  name: Pos Pos Checkin Request Example
  slug: pos-pos-checkin-request-example
- key_count: 6
  name: Pos Pos User Example
  slug: pos-pos-user-example
finops:
- name: Punchh Finops
  service_category: Loyalty + Guest Engagement
  slug: punchh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/punchh.png
json_schemas:
- name: AccessToken
  property_count: 4
  slug: mobile-access-token
- name: CreateUserRequest
  property_count: 4
  slug: mobile-create-user-request
- name: LoginRequest
  property_count: 2
  slug: mobile-login-request
- name: MarkOffersReadRequest
  property_count: 4
  slug: mobile-mark-offers-read-request
- name: TransactionDetailsRequest
  property_count: 2
  slug: mobile-transaction-details-request
- name: TransactionDetails
  property_count: 2
  slug: mobile-transaction-details
- name: UpdateUserProfileRequest
  property_count: 2
  slug: mobile-update-user-profile-request
- name: UserSession
  property_count: 2
  slug: mobile-user-session
- name: OnlineOrderCheckinRequest
  property_count: 12
  slug: online-ordering-online-order-checkin-request
- name: OnlineOrderCheckinResponse
  property_count: 5
  slug: online-ordering-online-order-checkin-response
- name: OnlineOrderRedemptionRequest
  property_count: 7
  slug: online-ordering-online-order-redemption-request
- name: OnlineOrderRedemptionResponse
  property_count: 7
  slug: online-ordering-online-order-redemption-response
- name: Redeemable
  property_count: 5
  slug: platform-functions-redeemable
- name: PosCheckinRequest
  property_count: 4
  slug: pos-pos-checkin-request
- name: PosUser
  property_count: 6
  slug: pos-pos-user
json_structures:
- name: Mobile Access Token Structure
  property_count: 4
  slug: mobile-access-token-structure
- name: Mobile Create User Request Structure
  property_count: 4
  slug: mobile-create-user-request-structure
- name: Mobile Login Request Structure
  property_count: 2
  slug: mobile-login-request-structure
- name: Mobile Mark Offers Read Request Structure
  property_count: 4
  slug: mobile-mark-offers-read-request-structure
- name: Mobile Transaction Details Request Structure
  property_count: 2
  slug: mobile-transaction-details-request-structure
- name: Mobile Transaction Details Structure
  property_count: 2
  slug: mobile-transaction-details-structure
- name: Mobile Update User Profile Request Structure
  property_count: 2
  slug: mobile-update-user-profile-request-structure
- name: Mobile User Session Structure
  property_count: 2
  slug: mobile-user-session-structure
- name: Online Ordering Online Order Checkin Request Structure
  property_count: 12
  slug: online-ordering-online-order-checkin-request-structure
- name: Online Ordering Online Order Checkin Response Structure
  property_count: 5
  slug: online-ordering-online-order-checkin-response-structure
- name: Online Ordering Online Order Redemption Request Structure
  property_count: 7
  slug: online-ordering-online-order-redemption-request-structure
- name: Online Ordering Online Order Redemption Response Structure
  property_count: 7
  slug: online-ordering-online-order-redemption-response-structure
- name: Platform Functions Redeemable Structure
  property_count: 5
  slug: platform-functions-redeemable-structure
- name: Pos Pos Checkin Request Structure
  property_count: 4
  slug: pos-pos-checkin-request-structure
- name: Pos Pos User Structure
  property_count: 6
  slug: pos-pos-user-structure
jsonld:
- class_count: 8
  name: Punchh Mobile Context
  property_count: 52
  slug: punchh-mobile-context
- class_count: 4
  name: Punchh Online Ordering Context
  property_count: 27
  slug: punchh-online-ordering-context
- class_count: 1
  name: Punchh Platform Functions Context
  property_count: 5
  slug: punchh-platform-functions-context
- class_count: 2
  name: Punchh Pos Context
  property_count: 10
  slug: punchh-pos-context
layout: provider
modified: '2026-08-13'
name: Punchh
nav: Providers
network: true
overview: 'Punchh publishes 46 APIs on the [APIs.io](https://apis.io/) network, including POS API, Api2 API, Auth API, and 43 more. Tagged areas include Gift Cards, Guest Engagement, Loyalty, Marketing, and Mobile.


  The Punchh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 4 JSON-LD contexts, and 2 Spectral governance rulesets.


  Punchh''s developer surface includes authentication, documentation, developer portal, getting-started guide, engineering blog, sandbox, changelog, and 47 more developer resources.'
plans:
- name: Punchh Plans Pricing
  plan_count: 1
  slug: punchh-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Punchh Rate Limits
  slug: punchh-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Punchh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: punchh-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  name: Punchh API Rules
  rule_count: 37
  severity_counts:
    error: 3
    hint: 0
    info: 11
    warn: 23
  slug: punchh-spectral-rules
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 92.0
    catalog_earned_first_party: 20.0
    catalog_gap: 23.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 50.0
    contract_governance: 45.5
    contract_quality: 64.0
    developer_ergonomics: 68.5
    discoverability: 78.6
    operational_transparency: 92.1
  previous_composite: 68.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 19.3
      derived: 11
      marker_coverage: 19.3
      total: 57
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/punchh/refs/heads/main/screenshots/punchh-2026-06-20T192311.png
security:
- kind: authentication
  name: Punchh Authentication
  slug: punchh-authentication
  summary_line: http/apiKey/oauth2-flavoured · 7 schemes
- kind: domain-security
  name: Punchh Domain Security
  slug: punchh-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Punchh Vulnerability Disclosure
  slug: punchh-vulnerability-disclosure
  summary_line: Hackerone
slug: punchh
tags:
- Gift Cards
- Guest Engagement
- Loyalty
- Marketing
- Mobile
- Offers
- Online Ordering
- PAR Technology
- Point-of-Sale
- Restaurant
- Restaurant Technology
- Webhook
- Loyalty & Incentives
website: https://punchh.com/
---
