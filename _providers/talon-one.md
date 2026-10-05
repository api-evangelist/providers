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
  band: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: templated
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 142
  human_in_the_loop: 3
  name: Talon One Agentic Access
  operation_count: 271
  slug: talon-one-agentic-access
  summary_line: 271 operations · 142 acting · 3 human-in-the-loop
api_count: 5
apis:
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents account and user management, including billing email addresses and user invitations.
  name: Talon.One Accounts and users API
  phrasing_intents:
  - id: getUsers
    intent: List the users in my account
    question: Who has a login to our Talon.One account?
  - id: getUser
    intent: Get one user's details
    question: What details, including the invitation code, are stored for a specific account user?
  - id: updateUser
    intent: Update a user's name, role or admin status
    question: How do I make an existing account user an admin?
  - id: deleteUser
    intent: Delete a user by ID
    question: What happens when I remove a user from the account using their user ID?
  - id: oktaEventHandlerChallenge
    intent: Answer Okta's ownership verification challenge
    question: How does Okta verify it is talking to the right endpoint before provisioning users?
  - id: scimGetGroups
    intent: List groups provisioned through SCIM
    question: Which role groups has our identity provider created over SCIM?
  - id: scimCreateGroup
    intent: Create a role group over SCIM
    question: How do I create a role from Entra ID using SCIM group provisioning?
  - id: scimGetGroup
    intent: Get one SCIM group
    question: Who are the members of a particular SCIM-provisioned group?
  phrasing_ops: 30
  slug: talon-one-accounts-and-users-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: 'Represents achievements that reward a customer profile for performing a number of specific actions or reaching a transactional milestone within a defined period. For example, you can use achievements '
  name: Talon.One Achievements API
  phrasing_intents:
  - id: getCustomerAchievements
    intent: List achievements available to a customer
    question: Which achievements can a given customer work toward, and how far along are they?
  - id: getCustomerAchievementHistory
    intent: Get a customer's progress history in one achievement
    question: How has a customer progressed through one achievement over time?
  - id: createAchievement
    intent: Create an achievement inside a campaign
    question: How do I add a campaign-level achievement like spend 100 in 30 days?
  - id: listAchievements
    intent: List a campaign's achievements
    question: Which achievements are set up inside a specific campaign?
  - id: getAchievement
    intent: Get one achievement in a campaign
    question: What target and period does a particular campaign achievement use?
  - id: updateAchievement
    intent: Update an achievement inside a campaign
    question: Can I change the target of an achievement that belongs to a campaign?
  - id: deleteAchievement
    intent: Delete an achievement from a campaign
    question: How do I remove an achievement from a campaign?
  - id: exportAchievements
    intent: Export participants of a campaign achievement to CSV
    question: Can I download a CSV of every customer participating in a campaign's achievement?
  phrasing_ops: 15
  slug: talon-one-achievements-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents an extra fee applied to the cart, for example, shipping fees or processing fees. See the [docs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).
  name: Talon.One Additional costs API
  phrasing_intents:
  - id: createAdditionalCost
    intent: Create an additional cost
    question: How do I define a shipping fee so campaigns can discount it?
  - id: getAdditionalCosts
    intent: List additional costs
    question: What additional costs like shipping or gift wrap are defined in my account?
  - id: getAdditionalCost
    intent: Get an additional cost
    question: What are the details of one additional cost definition?
  - id: updateAdditionalCost
    intent: Update an additional cost
    question: Can I change an additional cost's API name after creating it?
  phrasing_ops: 4
  slug: talon-one-additional-costs-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents analytics used to retrieve statistical data about the performance of campaigns within an Application.
  name: Talon.One Analytics API
  phrasing_intents:
  - id: exportEffects
    intent: Export triggered effects to CSV
    question: Can I download every discount and effect my rules triggered last month?
  - id: exportCustomerSessions
    intent: Export customer sessions to CSV
    question: How do I download all closed sessions for analysis?
  phrasing_ops: 2
  slug: talon-one-analytics-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents an Application in the Campaign Manager. An Application is the target of every Integration API request to Talon.One. One Application can hold various API keys used for Integration API reques
  name: Talon.One Applications API
  phrasing_intents:
  - id: getApplications
    intent: List Applications in the account
    question: What Applications exist in my Talon.One account?
  - id: getApplication
    intent: Get an Application
    question: What currency, timezone and settings does a given Application use?
  - id: getApplicationApiHealth
    intent: Check an Application's integration health
    question: Is my integration still talking to this Application, and when was it last used?
  - id: listApplicationCartItemFilters
    intent: List an Application's cart item filters
    question: Which cart item filters are defined in an Application?
  - id: getApplicationCartItemFilterExpression
    intent: Get a cart item filter expression
    question: What logic does a specific cart item filter expression contain?
  phrasing_ops: 5
  slug: talon-one-applications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a piece of information related to one of the entities available in the Campaign Manager. Use them to create highly customized rules. See the [docs](https://docs.talon.one/docs/product/accou
  name: Talon.One Attributes API
  phrasing_intents:
  - id: createAttribute
    intent: Create a custom attribute
    question: How do I add a new field like 'membership level' to customer profiles?
  - id: getAttributes
    intent: List custom attributes
    question: What custom attributes have been defined for customers, sessions and campaigns in my account?
  - id: getAttribute
    intent: Get a custom attribute
    question: What type and entity does a specific custom attribute belong to?
  - id: updateAttribute
    intent: Update a custom attribute's description
    question: Can I change the type or name of a custom attribute after it's created?
  - id: importAllowedList
    intent: Import picklist values for an attribute
    question: How do I upload the list of allowed values for a picklist attribute?
  phrasing_ops: 5
  slug: talon-one-attributes-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents lists of customer profiles that allow you to target specific groups of customers in your campaigns. Audiences can be synced from customer data platforms or created directly in Talon.One. Se
  name: Talon.One Audiences API
  phrasing_intents:
  - id: createAudienceV2
    intent: Create an audience
    question: How do I create a customer audience I can target in promotion rules?
  - id: deleteAudienceV2
    intent: Delete an audience
    question: What happens to customer associations when I delete an audience?
  - id: updateAudienceV2
    intent: Rename an audience
    question: Can I rename an audience that a third-party integration created?
  - id: deleteAudienceMembershipsV2
    intent: Remove every member from an audience
    question: Can I empty an audience without deleting the audience itself?
  - id: updateCustomerProfileAudiences
    intent: Add or remove customers from audiences in bulk
    question: How many add or remove audience actions can I send in one request?
  - id: updateAudienceCustomersAttributes
    intent: Set profile attributes for everyone in an audience
    question: Can I set the same profile attribute value for every customer in an audience?
  - id: getAudiences
    intent: List the account's audiences
    question: Which audiences have been created in my account?
  - id: getAudiencesAnalytics
    intent: Get member counts for audiences
    question: How many members does each of my audiences have?
  phrasing_ops: 11
  slug: talon-one-audiences-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[Braze](https://www.braze.com/) is a customer engagement platform to manage customer-centric interactions between consumers and brands in real-time. Use these endpoints to automate the creation of cou'
  name: Talon.One Braze API
  phrasing_intents:
  - id: braze/createReferral
    intent: Create a referral code for a Braze campaign
    question: How do I generate a referral code for an advocate from a Braze message?
  - id: braze/createCoupon
    intent: Create a coupon code for a Braze message
    question: How do I insert a unique coupon code into a Braze email?
  - id: braze/createCouponReservation
    intent: Reserve a coupon for a customer from Braze
    question: Can a Braze campaign reserve a coupon code for the recipient?
  - id: braze/trackEvent
    intent: Track a custom event from Braze
    question: How do I send a Braze event so it triggers promotion rules?
  phrasing_ops: 4
  slug: talon-one-braze-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the campaign access groups you can create in your Applications to organize your campaigns based on the type of campaign or the team in charge. See the [docs](https://docs.talon.one/docs/pro
  name: Talon.One Campaign access groups API
  phrasing_intents:
  - id: getCampaignGroups
    intent: List campaign access groups
    question: Which campaign access groups exist in my account?
  - id: getCampaignGroup
    intent: Get one campaign access group
    question: Which campaigns belong to a particular access group?
  phrasing_ops: 2
  slug: talon-one-campaign-access-groups-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/applications/application-notifications/overview) about campaign-related changes. > [!note] The value of the `NotificationType` property indicates the campa
  name: Talon.One Campaign notifications API
  slug: talon-one-campaign-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents templates used to generate campaigns from.
  name: Talon.One Campaign templates API
  phrasing_intents:
  - id: getCampaignTemplates
    intent: List campaign templates
    question: What campaign templates are available to start a new promotion from?
  - id: createCampaignFromTemplate
    intent: Create a campaign from a template
    question: How do I launch a new campaign based on one of my templates?
  phrasing_ops: 2
  slug: talon-one-campaign-templates-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the primary resource used to control the behavior of the Talon.One Rule Engine. They combine rulesets, coupons, and limits into a single unit. See the [docs](https://docs.talon.one/docs/pro
  name: Talon.One Campaigns API
  phrasing_intents:
  - id: integrationGetAllCampaigns
    intent: List running campaigns for an integration
    question: Which promotions are live right now that my storefront should know about?
  - id: getCampaigns
    intent: List campaigns in an Application
    question: What campaigns does my Application have, including disabled and expired ones?
  - id: getCampaign
    intent: Get a campaign
    question: What are the settings, dates and limits of a particular campaign?
  - id: updateCampaign
    intent: Update a campaign
    question: How do I change a campaign's end date or disable it?
  - id: deleteCampaign
    intent: Delete a campaign
    question: How do I permanently delete a campaign I no longer need?
  - id: copyCampaignToApplications
    intent: Copy a campaign into other Applications
    question: How do I reuse the same campaign in another Application or region?
  - id: getCampaignByAttributes
    intent: Search campaigns by custom attributes
    question: Which campaigns have a specific custom attribute value, like a region or budget owner?
  - id: getRulesets
    intent: List a campaign's ruleset revisions
    question: What revisions have a campaign's rules gone through?
  phrasing_ops: 12
  slug: talon-one-campaigns-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a catalog of cart items with unique SKUs. Cart item catalogs allow you to synchronize your entire inventory with Talon.One. See the [docs](https://docs.talon.one/docs/product/account/dev-to
  name: Talon.One Catalogs API
  phrasing_intents:
  - id: bestPriorPrice
    intent: Get the best prior price for SKUs
    question: What was the lowest price of a product over the last 30 days before a discount?
  - id: syncCatalog
    intent: Add, update or remove items in a cart item catalog
    question: How do I keep my product catalog in sync with my item attributes?
  - id: priceHistory
    intent: Get a SKU's price history
    question: How has the price of one SKU changed between two dates?
  - id: excludePriceHistory
    intent: Exclude price records from best prior price
    question: Can I ignore a wrong historical price when calculating the best prior price?
  - id: listCatalogItems
    intent: List items in a catalog
    question: What products are in my cart item catalog?
  phrasing_ops: 5
  slug: talon-one-catalogs-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a collection of arbitrary values that you can use inside rules. For example, a list of SKUs. See the [docs](https://docs.talon.one/docs/product/campaigns/managing-collections).
  name: Talon.One Collections API
  phrasing_intents:
  - id: listAccountCollections
    intent: List account-level collections
    question: What account-wide collections have I set up for use across Applications?
  - id: createAccountCollection
    intent: Create an account-level collection
    question: How do I create a shared list of SKUs that every Application can use in its rules?
  - id: getAccountCollection
    intent: Get an account-level collection
    question: Which Applications is an account-level collection enabled in?
  - id: updateAccountCollection
    intent: Update an account-level collection
    question: How do I turn an account-wide collection on or off for specific Applications?
  - id: deleteAccountCollection
    intent: Delete an account-level collection
    question: How do I remove a shared collection from my whole account?
  - id: getCollectionItems
    intent: Get the items in a collection
    question: What values are stored in a given collection?
  - id: listCollectionsInApplication
    intent: List campaign collections across an Application
    question: Which campaign-level collections exist across all campaigns in one Application?
  - id: listCollections
    intent: List collections in a campaign
    question: What collections does one specific campaign have?
  phrasing_ops: 16
  slug: talon-one-collections-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/applications/application-notifications/overview) about coupons.
  name: Talon.One Coupon notifications API
  slug: talon-one-coupon-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents unique codes belonging to a particular campaign. Coupons don't define any behavior on their own. Instead the campaign ruleset can include rules that validate coupons and carry out particula
  name: Talon.One Coupons API
  phrasing_intents:
  - id: createCouponReservation
    intent: Reserve a coupon code for specific customers
    question: How do I reserve a coupon code so only certain customers can use it?
  - id: deleteCouponReservation
    intent: Remove coupon reservations from customers
    question: Can I take back a coupon I reserved for a customer?
  - id: getReservedCustomers
    intent: List customers who have a coupon reserved
    question: Which customers currently hold a reservation on a given coupon code?
  - id: createCoupons
    intent: Generate coupon codes from a pattern
    question: How many coupons can I generate in one go, with and without a unique prefix?
  - id: updateCouponBatch
    intent: Bulk update all or a batch of a campaign's coupons
    question: Can I extend the expiry date of every coupon in a campaign at once?
  - id: deleteCoupons
    intent: Delete all coupons matching filters
    question: Can I delete every expired coupon in a campaign right away?
  - id: createCouponsForMultipleRecipients
    intent: Create coupons for a list of recipients
    question: Can I issue a personal coupon to each of up to 1000 customers in one call?
  - id: createCouponsAsync
    intent: Create millions of coupons as a background job
    question: What should I use when I need more than 20,000 coupons?
  phrasing_ops: 17
  slug: talon-one-coupons-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the data of a customer, including sessions and events used for reporting and debugging in the Campaign Manager.
  name: Talon.One Customer data API
  phrasing_intents:
  - id: getApplicationCustomers
    intent: List an Application's customers
    question: Who are the customers that have interacted with one of my Applications?
  - id: getApplicationCustomersByAttributes
    intent: Search an Application's customers by attributes
    question: Which customers in one Application have a given attribute value, like a certain city?
  - id: getCustomersByAttributes
    intent: Search all customer profiles by attributes
    question: Which customer profiles across my whole account match a set of attributes?
  - id: getCustomerProfile
    intent: Get a customer profile
    question: What attributes and loyalty data are stored on a specific customer profile?
  - id: getCustomerProfiles
    intent: List all customer profiles
    question: How many customer profiles exist across my account, page by page?
  - id: getApplicationCustomer
    intent: Get a customer within an Application
    question: What does a specific customer look like in the context of one Application?
  - id: getCustomerActivityReportsWithoutTotalCount
    intent: List activity reports for an Application's customers
    question: What did all my customers do in an Application over the last quarter?
  - id: getCustomerActivityReport
    intent: Get one customer's activity report
    question: What has one particular customer done in my Application during a date range?
  phrasing_ops: 14
  slug: talon-one-customer-data-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: You can integrate with any customer data platform, or CDP, using the following endpoints designed for third-party tools, rather than your own integration layer. Use these endpoints to automate the cre
  name: Talon.One Customer data platforms API
  phrasing_intents:
  - id: cdp/updateCustomerProfile
    intent: Update or create a customer profile from a CDP
    question: How does my customer data platform push profile attributes into Talon.One?
  - id: cdp/updateCustomerProfileAudiences
    intent: Change one profile's audiences from a CDP
    question: How does my CDP add a single customer to an audience or take them out of one?
  - id: cdp/updateCustomerProfilesAudiences
    intent: Update audiences for many profiles from a CDP
    question: Can my CDP update audience membership for lots of customers in one call using Talon.One audience IDs?
  - id: cdp/v2/updateCustomerProfilesAudiences
    intent: Update audiences for many profiles by external ID
    question: Can my CDP bulk-update audiences using its own external audience IDs?
  - id: cdp/createAudience
    intent: Create an audience from a CDP
    question: How do I bring an audience segment from my CDP into Talon.One?
  - id: cdp/updateAudience
    intent: Rename an audience created by a CDP
    question: How do I update the name of an audience my CDP created?
  - id: cdp/deleteAudience
    intent: Delete an audience created by a CDP
    question: How do I remove an audience that came from my CDP?
  phrasing_ops: 7
  slug: talon-one-customer-data-platforms-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: You can integrate with any customer engagement platform, or CEP, using the following endpoints designed for third-party tools, rather than your own integration layer. Use these endpoints to automate t
  name: Talon.One Customer engagement platforms API
  phrasing_intents:
  - id: cep/createCoupon
    intent: Create a coupon from an engagement platform
    question: How can my email or messaging platform generate a coupon code for a recipient?
  - id: cep/createReferral
    intent: Create a referral from an engagement platform
    question: Can my messaging platform generate a referral code for an advocate inside a campaign message?
  - id: cep/loyalty
    intent: Get a customer's loyalty ledger for an engagement platform
    question: How can my email platform show a customer's points balance in a message?
  - id: cep/addLoyaltyPoints
    intent: Add loyalty points from an engagement platform
    question: Can my engagement platform reward a customer with points when they open a campaign email?
  phrasing_ops: 4
  slug: talon-one-customer-engagement-platforms-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the customer's information. For instance, their contact information.
  name: Talon.One Customer profiles API
  phrasing_intents:
  - id: updateCustomerProfileV2
    intent: Update or create a customer profile
    question: How do I set custom attributes on a customer profile and get the triggered effects back?
  - id: updateCustomerProfilesV2
    intent: Update or create up to 1000 customer profiles
    question: Can I sync a batch of customer profiles in one request?
  - id: deleteCustomerData
    intent: Erase a customer's personal data
    question: How do I handle a GDPR erasure request for a customer?
  - id: getCustomerInventory
    intent: Get everything tied to a customer profile
    question: What coupons, referrals and loyalty points does a customer have?
  - id: getCustomerHeadless
    intent: Fetch a Shopify customer's profile for a headless store
    question: How does a headless Shopify storefront load the shopper's promotion profile?
  - id: getCustomerThemeBased
    intent: Fetch a Shopify customer's profile for a theme store
    question: How does a theme-based Shopify store read the customer's loyalty and coupon data?
  phrasing_ops: 6
  slug: talon-one-customer-profiles-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the data related to a customer session. Typically, a customer session is the value and content of the customer's cart. Sessions can be anonymous or linked to a customer profile and they hav
  name: Talon.One Customer sessions API
  phrasing_intents:
  - id: updateCustomerSessionV2
    intent: Update a cart session and get promotion effects
    question: How do I send a shopper's cart and get back the discounts that apply?
  - id: getCustomerSession
    intent: Get a customer session
    question: What's currently in a shopper's session, without changing it?
  - id: returnCartItems
    intent: Return items from a closed session
    question: How do I process a return and roll back the discounts on those items?
  - id: reopenCustomerSession
    intent: Reopen a closed customer session
    question: Can I edit an order after its session was closed?
  phrasing_ops: 4
  slug: talon-one-customer-sessions-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Emarsys is a customer engagement platform that enables marketers to build, launch, and scale personalized cross-channel promotional campaigns that have measurable impact. Use these endpoints to integr
  name: Talon.One Emarsys API
  phrasing_intents:
  - id: emarsys/getCoupon
    intent: Fetch a coupon code for an Emarsys message
    question: How can an Emarsys campaign pull a Talon.One coupon code to include in an email?
  - id: emarsys/getLoyaltyProgramBalance
    intent: Fetch a loyalty balance for an Emarsys message
    question: How can Emarsys show a customer's points balance inside a personalized email?
  - id: emarsys/v2/updateCustomerProfilesAudiences
    intent: Sync audiences from Emarsys to customer profiles
    question: How do I push Emarsys segment membership into Talon.One audiences?
  phrasing_ops: 3
  slug: talon-one-emarsys-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: 'Represents a single occurrence of a specific customer action, for example, updating the cart or signing up for a newsletter. There are 2 types of events: - **Built-in events:** They are triggered by v'
  name: Talon.One Events API
  phrasing_intents:
  - id: trackEventV2
    intent: Track a custom event
    question: How do I send a custom event like 'newsletter signup' so a rule can reward it?
  - id: trackEventV3
    intent: Track an advanced, idempotent event
    question: How do I send an idempotent event that can reference a session that's already closed?
  - id: getEventV3
    intent: Get an advanced event
    question: Can I look up an advanced event I already sent by its identifier?
  - id: getEventTypes
    intent: List event type definitions
    question: What custom event types have been defined in my account?
  phrasing_ops: 4
  slug: talon-one-events-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents an A/B testing configuration within a campaign that splits customer sessions across multiple variants to compare rule effects against each other.
  name: Talon.One Experiments API
  phrasing_intents:
  - id: listExperiments
    intent: List an Application's experiments
    question: What A/B experiments are running in an Application?
  - id: getExperiment
    intent: Get one experiment
    question: How is a particular experiment configured?
  phrasing_ops: 2
  slug: talon-one-experiments-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a program that rewards customers with giveaways, such as free gift cards. See the [docs](https://docs.talon.one/docs/product/giveaways/overview).
  name: Talon.One Giveaways API
  phrasing_intents:
  - id: importPoolGiveaways
    intent: Import giveaway codes into a pool
    question: How do I load a batch of gift card codes into a giveaway pool?
  - id: exportPoolGiveaways
    intent: Export a giveaway pool's codes to CSV
    question: Can I download all the giveaway codes in a pool, including which were awarded?
  phrasing_ops: 2
  slug: talon-one-giveaways-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[Iterable](https://iterable.com/) is a cross-channel marketing platform that powers unified customer experiences and empowers you to create, optimize and measure every interaction across the entire cu'
  name: Talon.One Iterable API
  phrasing_intents:
  - id: iterable/createCoupon
    intent: Create a coupon code for an Iterable campaign
    question: How do I drop a freshly generated coupon code into an Iterable message?
  - id: iterable/createReferral
    intent: Create a referral code for an Iterable campaign
    question: How can an Iterable message give an advocate their own referral code?
  - id: iterable/loyalty
    intent: Get a customer's loyalty ledger for Iterable
    question: How do I show a customer's loyalty points balance in an Iterable email?
  phrasing_ops: 3
  slug: talon-one-iterable-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the Talon.One logs, which contain all incoming and outgoing requests.
  name: Talon.One Logs API
  phrasing_intents:
  - id: getAccessLogsWithoutTotalCount
    intent: Get API access logs for an Application
    question: Which API calls hit my Application during a time window?
  - id: getMessageLogs
    intent: List webhook and notification message logs
    question: Did my webhook deliveries succeed, and what response codes came back?
  - id: getChanges
    intent: Get the account's audit log
    question: Who changed what in our account, and when?
  - id: getExports
    intent: List past data exports
    question: What exports have been run in the account before?
  phrasing_ops: 4
  slug: talon-one-logs-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents loyalty programs or concepts related to them. Loyalty programs can be _profile-based_ or _card-based_, depending on whether loyalty points are linked to [customer profiles](https://docs.tal
  name: Talon.One Loyalty API
  phrasing_intents:
  - id: getLoyaltyBalances
    intent: Get a customer's loyalty balances in real time
    question: How many active and pending points does this shopper have right now, from my storefront integration?
  - id: getLoyaltyProgramProfileTransactions
    intent: List a customer's loyalty transactions in real time
    question: Where can my app show a shopper their recent points earned and spent, straight from the Integration API?
  - id: deleteLoyaltyTransactionsFromLedgers
    intent: Delete a customer's loyalty transactions
    question: How do I wipe a customer's loyalty transaction history across every ledger in a program?
  - id: joinLoyaltyProgram
    intent: Enroll a customer in a loyalty program
    question: How do I sign a customer up for my profile-based loyalty program?
  - id: getLoyaltyProgramProfilePoints
    intent: List a customer's unused loyalty points
    question: Which of a customer's unused points are active, pending or expiring soon?
  - id: activateLoyaltyPoints
    intent: Activate pending loyalty points
    question: How do I turn pending points into spendable points once an order ships?
  - id: getLoyaltyLedgerBalances
    intent: Get a customer's loyalty balances for back-office use
    question: Is there a Management API version of the customer points balance lookup for back-office tools?
  - id: getLoyaltyProgramProfileLedgerTransactions
    intent: List a customer's loyalty transactions for back-office use
    question: Can an admin tool list a customer's points transactions through the Management API instead of the Integration API?
  phrasing_ops: 24
  slug: talon-one-loyalty-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/loyalty-programs/loyalty-notifications/overview) about changes to loyalty points in card-based loyalty programs.
  name: Talon.One Loyalty card notifications API
  slug: talon-one-loyalty-card-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents loyalty cards. [Loyalty cards](https://docs.talon.one/docs/product/loyalty-programs/card-based/card-based-overview) allow your customers to collect and spend loyalty points within a card-ba
  name: Talon.One Loyalty cards API
  phrasing_intents:
  - id: linkLoyaltyCardToProfile
    intent: Link a customer profile to a loyalty card
    question: How do I register a physical loyalty card to a customer's account?
  - id: unlinkLoyaltyCardFromProfile
    intent: Unlink a customer profile from a loyalty card
    question: How do I detach a customer from a loyalty card they no longer use?
  - id: getLoyaltyCardBalances
    intent: Get a loyalty card's point balances
    question: How many points are on a customer's loyalty card right now?
  - id: getLoyaltyCardTransactions
    intent: List a loyalty card's transactions in real time
    question: Where can my checkout app show the latest points earned and spent on a card, via the Integration API?
  - id: getLoyaltyCardPoints
    intent: List a loyalty card's unused points
    question: Which point batches on a loyalty card are still unspent, and when do they expire?
  - id: generateLoyaltyCard
    intent: Generate a single loyalty card
    question: How do I issue one new loyalty card on demand when a customer signs up in store?
  - id: getLoyaltyCards
    intent: List loyalty cards in a program
    question: Which loyalty cards have been issued in my card-based program?
  - id: importLoyaltyCards
    intent: Import loyalty cards from a CSV file
    question: How do I bring my existing physical card numbers into a card-based program?
  phrasing_ops: 19
  slug: talon-one-loyalty-cards-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/loyalty-programs/loyalty-notifications/overview) about changes to loyalty points in profile-based loyalty programs.
  name: Talon.One Loyalty notifications API
  slug: talon-one-loyalty-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[mParticle](https://www.mparticle.com/) is the customer data platform that helps unify data and simplify partner integrations with enterprise-class security and reliability. For more information, see '
  name: Talon.One M Particle API
  phrasing_intents:
  - id: mparticle/sendevent
    intent: Receive an event from mParticle
    question: Which mParticle events can be forwarded, such as audience membership changes?
  phrasing_ops: 1
  slug: talon-one-mparticle-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: 'Represents a referral code shared between a customer (advocate) and a prospect (friend). A referral is defined by: - an advocate: person who invited their friend via referral program. - a friend: pers'
  name: Talon.One Referrals API
  phrasing_intents:
  - id: createReferral
    intent: Create a referral code for an advocate
    question: How do I give one customer a referral code they can share with friends?
  - id: createReferralsForMultipleAdvocates
    intent: Create referral codes for many advocates at once
    question: Can I generate unique referral codes for a whole list of customers in one request?
  - id: deleteReferral
    intent: Delete a referral
    question: How do I revoke a referral code that's being abused?
  - id: updateReferral
    intent: Update a referral
    question: How do I extend the expiry date of an existing referral code?
  - id: getReferralsWithoutTotalCount
    intent: List a campaign's referrals
    question: Which referral codes exist in a campaign, and which are still usable?
  - id: getApplicationCustomerFriends
    intent: List friends a customer has referred
    question: Who has a particular customer successfully referred?
  - id: exportReferrals
    intent: Export referrals to CSV
    question: Can I download all referral codes in an Application as a spreadsheet?
  - id: importReferrals
    intent: Import referral codes from a CSV file
    question: How do I bring existing referral codes from another system into a campaign?
  phrasing_ops: 8
  slug: talon-one-referrals-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a set of permissions assigned to a user. See the [docs](https://docs.talon.one/docs/product/account/account-settings/managing-roles).
  name: Talon.One Roles API
  phrasing_intents:
  - id: listAllRolesV2
    intent: List user roles
    question: What roles exist in my Talon.One account?
  - id: getRoleV2
    intent: Get a role's permissions and members
    question: Which permissions and users does a particular role have?
  - id: updateRoleV2
    intent: Update a role
    question: How do I add a colleague to an existing role?
  phrasing_ops: 3
  slug: talon-one-roles-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[Segment](https://segment.com/) is a customer data platform that collects events from your web & mobile apps. Use these endpoints to integrate with Talon.One.'
  name: Talon.One Segment API
  phrasing_intents:
  - id: segment/updateCustomerProfile
    intent: Upsert a customer profile via Segment (deprecated v1)
    question: Is the original v1 Segment customer profile upsert still supported?
  - id: segment/updateCustomerProfileV2
    intent: Upsert a customer profile via Segment (deprecated v2)
    question: What was the deprecated customer_profile_v2 Segment endpoint used for?
  - id: segment/v2/updateCustomerProfile
    intent: Update or create a customer profile from Segment
    question: What is the current way to sync a Segment identify call into a customer profile?
  - id: segment/updateCustomerProfileAudiences
    intent: Change one profile's audiences from Segment
    question: Can I add a single customer to Segment audiences using the Segment audience ID?
  - id: segment/updateCustomerProfilesAudiences
    intent: Update audiences for many profiles from Segment
    question: Can I update audience membership for a batch of customers coming from Segment?
  - id: segment/v2/updateCustomerProfilesAudiences
    intent: Update audiences for many profiles by external ID
    question: Can I bulk update audiences using the audience ID from the third-party integration?
  - id: segment/trackEvent
    intent: Track a custom event from Segment (deprecated v1)
    question: How did the deprecated v1 Segment track event endpoint work?
  - id: segment/trackEventV2
    intent: Track a custom event from Segment
    question: How do I trigger promotion rules from a Segment track call?
  phrasing_ops: 13
  slug: talon-one-segment-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Use the following endpoints to manage customer sessions.
  name: Talon.One Session API
  phrasing_intents:
  - id: upsertSession
    intent: Create or update a session from a Shopify cart
    question: How do I send a Shopify cart to Talon.One so promotions are evaluated?
  phrasing_ops: 1
  slug: talon-one-session-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a session used for authentication purposes. Create one with the [Create session](#tag/Sessions/operation/createSession) endpoint.
  name: Talon.One Sessions API
  phrasing_intents:
  - id: createSession
    intent: Log in and get a Management API token
    question: How do I get a bearer token for the Management API with my email and password?
  - id: destroySession
    intent: Log out and end the session
    question: Can I invalidate my current management session token?
  phrasing_ops: 2
  slug: talon-one-sessions-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents store budgets. You can set a store budget to limit the total amount an individual store can spend in a campaign.
  name: Talon.One Store budgets API
  phrasing_intents:
  - id: createCampaignStoreBudget
    intent: Set per-store budgets for a campaign
    question: How do I cap how many redemptions each store can give in a campaign?
  - id: listCampaignStoreBudgetLimits
    intent: List a campaign's per-store budget limits
    question: What budget limit does each store have in a campaign?
  - id: deleteCampaignStoreBudgets
    intent: Delete a campaign's store budgets
    question: How do I remove all per-store limits from a campaign?
  - id: summarizeCampaignStoreBudget
    intent: Summarize a campaign's store budgets
    question: What's the overall picture of store budget usage in a campaign?
  - id: importCampaignStoreBudget
    intent: Import store budgets from a CSV
    question: How do I upload store budget limits for hundreds of stores at once?
  - id: exportCampaignStoreBudgets
    intent: Export a campaign's store budgets to CSV
    question: Can I download each store's budget limit for a campaign as a spreadsheet?
  phrasing_ops: 6
  slug: talon-one-store-budgets-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents physical or digital stores, branches, and franchises.
  name: Talon.One Stores API
  phrasing_intents:
  - id: listStores
    intent: List an Application's stores
    question: Which physical or online stores are registered in an Application?
  - id: createStore
    intent: Create a store
    question: How do I register a new store in an Application?
  - id: getStore
    intent: Get a store's details
    question: What attributes are saved for a particular store?
  - id: updateStore
    intent: Update a store's details
    question: Can I change a store's name or description after creating it?
  - id: deleteStore
    intent: Delete a store
    question: How do I remove a closed store from an Application?
  - id: exportCampaignStores
    intent: Export the stores linked to a campaign
    question: Can I download the list of stores a campaign runs in?
  - id: disconnectCampaignStores
    intent: Unlink all stores from a campaign
    question: How do I stop a campaign from being limited to specific stores?
  - id: importCampaignStores
    intent: Link stores to a campaign from a CSV
    question: How do I restrict a campaign to a list of stores using a CSV?
  phrasing_ops: 8
  slug: talon-one-stores-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/applications/application-notifications/overview) about strikethrough pricing updates.
  name: Talon.One Strikethrough pricing notifications API
  slug: talon-one-strikethrough-pricing-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the value maps that the user can create within a campaign ruleset.
  name: Talon.One Value maps API
  phrasing_intents:
  - id: exportCampaignValueMap
    intent: Export a campaign value map to CSV
    question: Can I download all the items in a campaign's value map?
  phrasing_ops: 1
  slug: talon-one-value-maps-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents webhooks, which send information from Talon.One to the URI of your choice. See the [docs](https://docs.talon.one/docs/dev/getting-started/webhooks).
  name: Talon.One Webhooks API
  phrasing_intents:
  - id: getWebhooks
    intent: List webhooks
    question: What webhooks are configured in my account?
  - id: getWebhook
    intent: Get a webhook
    question: What URL and payload does a specific webhook send?
  phrasing_ops: 2
  slug: talon-one-webhooks-api
artifact_total: 57
asyncapis:
- description: ''
  name: Talon One Webhooks
  slug: talon-one-webhooks
collections:
- collection_type: open
  name: Integration API
  slug: open-talon-one-integration-api
- collection_type: open
  name: Management API
  slug: open-talon-one-management-api
- collection_type: open
  name: Notification schemas
  slug: open-talon-one-outbound-notifications
- collection_type: open
  name: Shopify Integration API
  slug: open-talon-one-shopify-integration-api
- collection_type: open
  name: Third-party API
  slug: open-talon-one-third-party-api
- collection_type: open
  name: Talon.One API
  slug: open-talon-one
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/capabilities/talon-one-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/talon-one-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/overlays/talon-one-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/talon-one-management-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/overlays/talon-one-third-party-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/talon-one-third-party-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/overlays/talon-one-shopify-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/talon-one-shopify-integration-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/agentic-access/talon-one-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/talon-one-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/security/talon-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/talon-one-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/authentication/talon-one-authentication.yml
  title: ''
  type: Authentication
  url: authentication/talon-one-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/talon-one
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talon-one
- group: company
  title: ''
  type: Website
  url: https://www.talon.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talon.one
- group: start
  title: ''
  type: SignUp
  url: https://www.talon.one/book-a-demo
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/plans/talon-one-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/talon-one-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/rate-limits/talon-one-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/talon-one-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/finops/talon-one-finops.yml
  title: ''
  type: FinOps
  url: finops/talon-one-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.talon.one/blog
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/packages/talon-one-packages.yml
  title: ''
  type: Packages
  url: packages/talon-one-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/packages/talon-one-packages.yml
  title: ''
  type: SDKs
  url: packages/talon-one-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/mcp/talon-one-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/talon-one-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/mcp/talon-one-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/talon-one-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/llms/talon-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/talon-one-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/conformance/talon-one-conformance.yml
  title: ''
  type: Conformance
  url: conformance/talon-one-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/security/talon-one-trust-center.yml
  title: ''
  type: Compliance
  url: security/talon-one-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/security/talon-one-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/talon-one-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/errors/talon-one-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/talon-one-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/lifecycle/talon-one-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/talon-one-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.talon.one/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/lifecycle/talon-one-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/talon-one-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/conventions/talon-one-conventions.yml
  title: ''
  type: Conventions
  url: conventions/talon-one-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/conventions/talon-one-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/talon-one-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/changelog/talon-one-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/talon-one-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.talon.one/whats-new
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/sandbox/talon-one-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/talon-one-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/data-model/talon-one-data-model.yml
  title: ''
  type: DataModel
  url: data-model/talon-one-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/asyncapi/talon-one-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/talon-one-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/overlays/talon-one-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/talon-one-integration-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.talon.one/docs/dev/get-started/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.talon.one/integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.talon.one/docs/dev/quickstart
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/talonone-rnd/workspace/talon-one/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talon.one/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talon.one/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talon.one/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.talon.one/contact-us
created: '2026-07-10'
description: Talon.One is an enterprise promotion, loyalty, and incentives engine that lets teams build and run coupons, discounts, referrals, bundles, giveaways, and multi-tier loyalty programs from a single rules-based platform. It exposes two primary REST APIs. The Integration API pushes real-time customer sessions, profiles, and events into the rules engine and returns the effects (discounts, awarded loyalty points, accepted coupons) to apply in the calling application. The Management API programmatically administers applications, campaigns, rulesets, coupons, loyalty programs, audiences, custom attributes, collections, and analytics exports that back the Campaign Manager. Talon.One is delivered as a managed, per-customer deployment; each account calls its own base URL (https://yourbaseurl.talon.one) and authenticates with an API key whose prefix distinguishes the Integration key (ApiKey-v1) from the Management key (ManagementKey-v1).
finops:
- name: Talon One Finops
  service_category: Marketing and Promotions
  slug: talon-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talon-one.png
layout: provider
mcp_servers:
- description: Talon.One ships an official MCP server that gives agents secure, read-only access to the campaigns, customers, coupons and loyalty data in a Talon.One environment. Because Talon.One runs as a per-cust
  name: Talon.One MCP server
  slug: talon-one-mcp-server
modified: '2026-08-13'
name: Talon.One
nav: Providers
network: true
overview: 'Talon.One publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Accounts and users API, Achievements API, Additional costs API, and 39 more. Tagged areas include Promotions, Loyalty, Coupons, Incentives, and Campaigns.


  The Talon.One catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Talon.One''s developer surface includes authentication, documentation, signup flow, engineering blog, changelog, sandbox, API reference, and 38 more developer resources.'
plans:
- name: Talon One Plans Pricing
  plan_count: 3
  slug: talon-one-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Talon One Rate Limits
  slug: talon-one-rate-limits
score:
  band: exemplar
  composite: 74.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 61.8
    developer_ergonomics: 81.0
    discoverability: 73.3
    operational_transparency: 81.6
  previous_composite: 74.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: first-party
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
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/screenshots/talon-one-2026-08-17T080429.png
security:
- kind: authentication
  name: Talon One Authentication
  slug: talon-one-authentication
  summary_line: apiKey/http · 8 schemes
- kind: domain-security
  name: Talon One Domain Security
  slug: talon-one-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Talon One Trust Center
  slug: talon-one-trust-center
  summary_line: ISO 27001, SOC 2, GDPR
slug: talon-one
tags:
- Promotions
- Loyalty
- Coupons
- Incentives
- Campaigns
- Personalization
- MarTech
- Rules Engine
- Referrals
- Discounts
- E-Commerce
- Retail
- Loyalty & Incentives
website: https://www.talon.one
---
