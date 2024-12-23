---
aid: bunq
url: https://raw.githubusercontent.com/api-search/banking/main/_apis/bunq/apis.md
apis:
  - aid: bunq:bunq-activity-map-place-api
    name: Bunq Activity Map Place API
    tags: []
    score: 85
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/activity-map-place-public
    overlays:
      - url: overlays/bunq-activity-map-place-public-itemid-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-activity-map-place-public-itemid-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-activity-map-place-public-itemid-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing activity map for a user account.
  - aid: bunq:bunq-transaction-categories-api
    name: Bunq Transaction Categories API
    tags:
      - Additional
      - Categories
      - Information
      - Transactions
      - Users
      - Defined
    score: 156
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/additional-transaction-information-category
    overlays:
      - url: >-
          overlays/bunq-user-userid-additional-transaction-information-category-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-additional-transaction-information-category-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-additional-transaction-information-category-openapi-original.yml
        type: OpenAPI
    description: Manage additional information transactional categories.
  - aid: bunq:bunq-monetary-account-api
    name: Bunq Monetary Account API
    tags:
      - Accounts
      - Actions
      - Adyen
      - Allocate
      - Attachments
      - Auto
      - Bank
      - Batches
      - Cards
      - Cloud
      - Content
      - Conversions
      - Currencies
      - Customers
      - Definitions
      - Draft
      - Eal
      - Events
      - Exports
      - External
      - Filter
      - Fundraiser
      - Ideal
      - Inquiries
      - Instances
      - Invite
      - Invoices
      - Items
      - Joint
      - Mastercard
      - Merchants
      - Monetary
      - Notes
      - Notifications
      - Payments
      - Quotes
      - Responses
      - Results
      - Savings
      - Schedules
      - Services
      - Share
      - Statements
      - Switch
      - Tabs
      - Text
      - Transactions
      - URL
      - Users
      - Whitelist
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/monetary-account
    overlays:
      - url: overlays/bunq-user-userid-monetary-account-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-monetary-account-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing different types of monetary accounts.
  - aid: bunq:bunq-attachments-api
    name: Bunq Attachments API
    tags:
      - Attachments
      - Items
      - Users
      - Content
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/attachment
    overlays:
      - url: overlays/bunq-user-userid-attachment-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-attachment-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: An API for managing attachments associated with a Bunq account.
  - aid: bunq:bunq-avatar-api
    name: Bunq Avatar API
    tags:
      - Avatars
      - Items
    score: 86
    humanURL: https://doc.bunq.com/#/avatar
    overlays:
      - url: overlays/bunq-avatar--openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-avatar--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-avatar--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Avatars are public images used to represent you or your company. Avatars
      are used to represent users, monetary accounts and cash registers. Avatars
      cannot be deleted, only replaced. Avatars can be updated after uploading
      the image you would like to use through AttachmentPublic. Using the
      attachment_public_uuid which is returned you can update your Avatar.
      Avatars used for cash registers and company accounts will be reviewed by
      bunq.
  - aid: bunq:bunq-billing-contract-subscription-api
    name: Bunq Billing Contract Subscription API
    tags:
      - Billing
      - Contracts
      - Subscriptions
      - Users
    humanURL: >-
      https://doc.bunq.com/#/billing-contract-subscription/List_all_BillingContractSubscription_for_User
    overlays:
      - url: >-
          overlays/bunq-user-userid-billing-contract-subscription-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-billing-contract-subscription-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Manage all subscription billing contract for the authenticated user.
  - aid: bunq:bunq-fundraiser-profile-api
    name: Bunq Fundraiser Profile API
    tags:
      - Fundraiser
      - Items
      - Profiles
      - Users
    humanURL: >-
      https://doc.bunq.com/#/bunqme-fundraiser-profile/READ_BunqmeFundraiserProfile_for_User
    overlays:
      - url: overlays/bunq-user-userid-bunqme-fundraiser-profile-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-bunqme-fundraiser-profile-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: The /me profile for the Bunq user.
  - aid: bunq:bunq-oauth-client-api
    name: Bunq Oauth Client API
    tags:
      - Callback
      - Clients
      - Items
      - OAuth
      - URL
      - Users
    score: 696
    humanURL: https://doc.bunq.com/#/
    overlays:
      - url: overlays/bunq-user-userid-oauth-client-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-oauth-client-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-oauth-client-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: For managing OAuth clients through an API.
  - aid: bunq:bunq-card-api
    name: Bunq Card API
    tags:
      - Cards
      - Items
      - Users
      - Batches
      - Replace
      - Credit
      - Debit
      - Names
      - Content
      - Exports
      - Statements
      - CSV
      - PDF
      - Generated
    humanURL: https://doc.bunq.com/#/card
    overlays:
      - url: overlays/bunq-user-userid-card-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-card-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing cards and transactions made via cards.
  - aid: bunq:bunq-certificate-pinning-api
    name: Bunq Certificate Pinning API
    tags:
      - Certificates
      - Pinned
      - Users
      - Items
    score: 292
    humanURL: https://doc.bunq.com/#/certificate-pinned
    overlays:
      - url: overlays/bunq-user-userid-certificate-pinned-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-certificate-pinned-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-certificate-pinned-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing the pinned certificates for a user.
  - aid: bunq:bunq-challenge-request-api
    name: Bunq Challenge Request API
    tags:
      - Challenges
      - Items
      - Users
    score: 168
    humanURL: https://doc.bunq.com/#/challenge-request
    overlays:
      - url: overlays/bunq-user-userid-challenge-request-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-challenge-request-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-challenge-request-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing the challenge requests for a user.
  - aid: bunq:bunq-company-api
    name: Bunq Company API
    tags:
      - Companies
      - Users
      - Items
    score: 299
    humanURL: https://doc.bunq.com/#/company
    overlays:
      - url: overlays/bunq-user-userid-company-openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-user-userid-company-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-company-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing details of an accounts company information.
  - aid: bunq:bunq-confirmation-of-funds-api
    name: Bunq Confirmation Of Funds API
    tags:
      - Confirmation
      - Funds
      - Users
    score: 85
    humanURL: >-
      https://doc.bunq.com/#/confirmation-of-funds/CREATE_ConfirmationOfFunds_for_User
    overlays:
      - url: overlays/bunq-user-userid-confirmation-of-funds-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-confirmation-of-funds-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-confirmation-of-funds-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Used to confirm availability of funds on an account.
  - aid: bunq:bunq-chat-conversation-api
    name: Bunq Chat Conversation API
    tags:
      - Attachments
      - Chat
      - Content
      - Conversations
      - Users
    score: 106
    humanURL: >-
      https://doc.bunq.com/#/content/List_all_Content_for_User_ChatConversation_Attachment
    overlays:
      - url: overlays/bunq-user-userid-chat-conversation-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-chat-conversation-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-chat-conversation-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Managing the chat conversations for a user account.
  - aid: bunq:bunq-attachment-content-api
    name: Bunq Attachment Content API
    tags:
      - Attachments
      - Content
      - Public
    score: 87
    humanURL: https://doc.bunq.com/#/content
    overlays:
      - url: >-
          overlays/bunq-attachment-public-attachment-publicuuid-content-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-attachment-public-attachment-publicuuid-content-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-attachment-public-attachment-publicuuid-content-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Used to manage the attachment content for an A/PI.
  - aid: bunq:bunq-export-annual-overview-api
    name: Bunq Export Annual Overview API
    tags:
      - Annual
      - Content
      - Exports
      - Overview
      - Users
      - Items
    score: 370
    humanURL: >-
      https://doc.bunq.com/#/content/List_all_Content_for_User_ExportAnnualOverview
    overlays:
      - url: overlays/bunq-user-userid-export-annual-overview-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-export-annual-overview-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-export-annual-overview-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: Used to retrieve the raw content of an annual overview.
  - aid: bunq:bunq-user-credential-password-ip-api
    name: Bunq User Credential Password Ip API
    tags:
      - Credentials
      - IP
      - Items
      - Password
      - Users
    score: 484
    overlays:
      - url: overlays/bunq-user-userid-credential-password-ip-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-credential-password-ip-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-credential-password-ip-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-currency-cloud-beneficiary-api
    name: Bunq User Currency Cloud Beneficiary API
    tags: []
    score: 294
    overlays:
      - url: >-
          overlays/bunq-user-userid-currency-cloud-beneficiary-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-currency-cloud-beneficiary-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-currency-cloud-beneficiary-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-device-api
    name: Bunq Device API
    tags:
      - Device
      - Items
    score: 85
    overlays:
      - url: overlays/bunq-device--openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-device--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-device--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-device-server-api
    name: Bunq Device Server API
    tags:
      - Device
      - Items
      - Servers
    score: 85
    overlays:
      - url: overlays/bunq-device-server--openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-device-server--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-device-server--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-event-api
    name: Bunq User Event API
    tags:
      - Events
      - Items
      - Users
    score: 164
    overlays:
      - url: overlays/bunq-user-userid-event-openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-user-userid-event-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-event-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-feature-announcement-api
    name: Bunq User Feature Announcement API
    tags:
      - Announcement
      - Feature
      - Items
      - Users
    score: 95
    overlays:
      - url: overlays/bunq-user-userid-feature-announcement-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-feature-announcement-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-feature-announcement-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-insight-preference-date-api
    name: Bunq User Insight Preference Date API
    tags:
      - Dates
      - Insights
      - Preferences
      - Users
    score: 86
    overlays:
      - url: overlays/bunq-user-userid-insight-preference-date-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-insight-preference-date-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-insight-preference-date-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-insights-api
    name: Bunq User Insights API
    tags:
      - Insights
      - Users
      - Search
    score: 154
    overlays:
      - url: overlays/bunq-user-userid-insights-openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-user-userid-insights-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-insights-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-installation-api
    name: Bunq Installation API
    tags:
      - Installations
      - Items
      - Keys
      - Public
      - Servers
    score: 153
    overlays:
      - url: overlays/bunq-installation--openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-installation--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-installation--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-invoice-api
    name: Bunq User Invoice API
    tags:
      - Invoices
      - Users
      - Items
      - Content
      - PDF
    score: 241
    overlays:
      - url: overlays/bunq-user-userid-invoice-openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-user-userid-invoice-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-invoice-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-legal-name-api
    name: Bunq User Legal Name API
    tags:
      - Legal
      - Names
      - Users
    score: 86
    overlays:
      - url: overlays/bunq-user-userid-legal-name-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-legal-name-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-legal-name-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-limit-api
    name: Bunq User Limit API
    tags:
      - Limits
      - Users
    score: 86
    overlays:
      - url: overlays/bunq-user-userid-limit-openapi-search.yml
        type: OpenAPI
      - url: overlays/bunq-user-userid-limit-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-limit-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-monetary-account-bank-api
    name: Bunq User Monetary Account Bank API
    tags:
      - Accounts
      - Bank
      - Monetary
      - Users
      - Items
    score: 299
    overlays:
      - url: overlays/bunq-user-userid-monetary-account-bank-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-monetary-account-bank-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-monetary-account-bank-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-monetary-account-card-api
    name: Bunq User Monetary Account Card API
    tags:
      - Accounts
      - Cards
      - Items
      - Monetary
      - Users
    score: 236
    overlays:
      - url: overlays/bunq-user-userid-monetary-account-card-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-monetary-account-card-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/bunq-user-userid-monetary-account-card-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-monetary-account-external-api
    name: Bunq User Monetary Account External API
    tags:
      - Accounts
      - External
      - Monetary
      - Users
      - Items
      - Savings
    score: 580
    humanURL: https://doc.bunq.com/#/monetary-account-external
    overlays:
      - url: overlays/bunq-user-userid-monetary-account-external-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-monetary-account-external-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-monetary-account-external-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-monetary-account-joint-api
    name: Bunq User Monetary Account Joint API
    tags:
      - Accounts
      - Joint
      - Monetary
      - Users
      - Items
    score: 300
    overlays:
      - url: overlays/bunq-user-userid-monetary-account-joint-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-monetary-account-joint-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-monetary-account-joint-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-monetary-account-savings-api
    name: Bunq User Monetary Account Savings API
    tags:
      - Accounts
      - Monetary
      - Savings
      - Users
      - Items
    score: 301
    overlays:
      - url: overlays/bunq-user-userid-monetary-account-savings-openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/bunq-user-userid-monetary-account-savings-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-
          properties/bunq-user-userid-monetary-account-savings-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-company-user-company-name-api
    name: Bunq User Company User Company Name API
    tags:
      - Companies
      - Names
      - Users
    overlays:
      - url: overlays/bunq-user-company-user-companyid-name-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-company-user-companyid-name-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-notification-filter-email-api
    name: Bunq User Notification Filter Email API
    tags:
      - Emails
      - Filter
      - Notifications
      - Users
    overlays:
      - url: overlays/bunq-user-userid-notification-filter-email-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-notification-filter-email-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-notification-filter-failure-api
    name: Bunq User Notification Filter Failure API
    tags:
      - Failure
      - Filter
      - Notifications
      - Users
    overlays:
      - url: >-
          overlays/bunq-user-userid-notification-filter-failure-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-notification-filter-failure-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-notification-filter-push-api
    name: Bunq User Notification Filter Push API
    tags:
      - Filter
      - Notifications
      - Users
    overlays:
      - url: overlays/bunq-user-userid-notification-filter-push-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-notification-filter-push-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-notification-filter-url-api
    name: Bunq User Notification Filter Url API
    tags:
      - Filter
      - Notifications
      - URL
      - Users
    overlays:
      - url: overlays/bunq-user-userid-notification-filter-url-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-notification-filter-url-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-payment-auto-allocate-api
    name: Bunq User Payment Auto Allocate API
    tags:
      - Allocate
      - Auto
      - Payments
      - Users
    overlays:
      - url: overlays/bunq-user-userid-payment-auto-allocate-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-payment-auto-allocate-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-payment-service-provider-credential-api
    name: Bunq Payment Service Provider Credential API
    tags:
      - Credentials
      - Er
      - Items
      - Payments
      - Prov
      - Providers
      - Services
    overlays:
      - url: overlays/bunq-payment-service-provider-credential--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-payment-service-provider-credential--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-payment-service-provider-draft-payment-api
    name: Bunq User Payment Service Provider Draft Payment API
    tags:
      - Draft
      - Er
      - Payments
      - Prov
      - Providers
      - Services
      - Users
      - Items
    overlays:
      - url: >-
          overlays/bunq-user-userid-payment-service-provider-draft-payment-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-payment-service-provider-draft-payment-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-payment-service-provider-issuer-transaction-api
    name: Bunq User Payment Service Provider Issuer Transaction API
    tags:
      - Er
      - Issuer
      - Payments
      - Prov
      - Providers
      - Services
      - Transactions
      - Users
      - Items
    overlays:
      - url: >-
          overlays/bunq-user-userid-payment-service-provider-issuer-transaction-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-payment-service-provider-issuer-transaction-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-registry-import-splitwise-csv-api
    name: Bunq Registry Import Splitwise Csv API
    tags: []
    overlays:
      - url: overlays/bunq-registry-import-splitwise-csv--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-registry-import-splitwise-csv--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-registry-api
    name: Bunq User Registry API
    tags:
      - Registries
      - Settlements
      - Users
      - Items
    overlays:
      - url: overlays/bunq-user-userid-registry-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-registry-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-sandbox-user-company-api
    name: Bunq Sandbox User Company API
    tags: []
    overlays:
      - url: overlays/bunq-sandbox-user-company--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-sandbox-user-company--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-sandbox-user-person-api
    name: Bunq Sandbox User Person API
    tags: []
    overlays:
      - url: overlays/bunq-sandbox-user-person--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-sandbox-user-person--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-schedule-api
    name: Bunq User Schedule API
    tags:
      - Schedules
      - Users
    overlays:
      - url: overlays/bunq-user-userid-schedule-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-schedule-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-server-error-api
    name: Bunq Server Error API
    tags: []
    overlays:
      - url: overlays/bunq-server-error--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-server-error--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-installation-installation-server-public-key-api
    name: Bunq Installation Installation Server Public Key API
    tags:
      - Installations
      - Keys
      - Public
      - Servers
    overlays:
      - url: >-
          overlays/bunq-installation-installationid-server-public-key-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-installation-installationid-server-public-key-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-session-item-api
    name: Bunq Session Item API
    tags: []
    overlays:
      - url: overlays/bunq-session-itemid--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-session-itemid--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-session-server-api
    name: Bunq Session Server API
    tags: []
    overlays:
      - url: overlays/bunq-session-server--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-session-server--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-share-invite-monetary-account-response-api
    name: Bunq User Share Invite Monetary Account Response API
    tags:
      - Accounts
      - Invite
      - Items
      - Monetary
      - Share
      - Users
    overlays:
      - url: >-
          overlays/bunq-user-userid-share-invite-monetary-account-response-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-share-invite-monetary-account-response-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-token-qr-request-eal-api
    name: Bunq User Token Qr Request Eal API
    tags:
      - Ideal
      - Tokens
      - Users
    overlays:
      - url: overlays/bunq-user-userid-token-qr-request-ideal-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-token-qr-request-ideal-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-token-qr-request-sofort-api
    name: Bunq User Token Qr Request Sofort API
    tags:
      - Tokens
      - Users
    overlays:
      - url: overlays/bunq-user-userid-token-qr-request-sofort-openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-userid-token-qr-request-sofort-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-transferwise-currency-api
    name: Bunq User Transferwise Currency API
    tags:
      - Currencies
      - Transferwise
      - Users
    overlays:
      - url: overlays/bunq-user-userid-transferwise-currency-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-transferwise-currency-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-transferwise-quote-api
    name: Bunq User Transferwise Quote API
    tags:
      - Quotes
      - Transferwise
      - Users
      - Items
      - Temporary
      - Recipient
      - Requirements
      - Transfers
    overlays:
      - url: overlays/bunq-user-userid-transferwise-quote-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-transferwise-quote-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-transferwise-user-api
    name: Bunq User Transferwise User API
    tags:
      - Transferwise
      - Users
    overlays:
      - url: overlays/bunq-user-userid-transferwise-user-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-transferwise-user-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-tree-progress-api
    name: Bunq User Tree Progress API
    tags:
      - Progress
      - Trees
      - Users
    overlays:
      - url: overlays/bunq-user-userid-tree-progress-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-tree-progress-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-item-api
    name: Bunq User Item API
    tags: []
    overlays:
      - url: overlays/bunq-user-itemid--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-itemid--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-company-item-api
    name: Bunq User Company Item API
    tags: []
    overlays:
      - url: overlays/bunq-user-company-itemid--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-company-itemid--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-payment-service-provider-item-api
    name: Bunq User Payment Service Provider Item API
    tags: []
    overlays:
      - url: overlays/bunq-user-payment-service-provider-itemid--openapi-search.yml
        type: OpenAPI
    properties:
      - url: >-
          properties/bunq-user-payment-service-provider-itemid--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-person-item-api
    name: Bunq User Person Item API
    tags: []
    overlays:
      - url: overlays/bunq-user-person-itemid--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-person-itemid--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: bunq:bunq-user-whitelist-sdd-api
    name: Bunq User Whitelist Sdd API
    tags:
      - Items
      - Users
      - Whitelist
      - Recurring
    overlays:
      - url: overlays/bunq-user-userid-whitelist-sdd-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/bunq-user-userid-whitelist-sdd-openapi-original.yml
        type: OpenAPI
    description: Needs description.
name: Bunq
tags:
  - Banking
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
score: 1805
access: 3rd-Party
common:
  - url: https://developer.bunq.com/en/
    type: Portal
  - url: https://doc.bunq.com/#/authentication
    type: Authentication
  - url: https://doc.bunq.com/#/errors
    type: Errors
  - url: https://doc.bunq.com/#/headers
    type: Headers
  - url: https://example.com
    type: Type
  - url: https://doc.bunq.com/#/callbacks
    type: Callbacks
  - url: https://doc.bunq.com/#/pagination
    type: Pagination
  - url: https://beta.doc.bunq.com/basics/changelog
    type: Change Log
  - url: https://status.bunq.com/
    type: Status
  - url: https://github.com/bunq
    type: GitHub Organization
  - url: https://github.com/bunq/postman/
    type: Postman Collections
  - url: https://beta.doc.bunq.com/basics/sandbox
    type: Sandbox
  - url: https://medium.com/bunq-developers-corner
    type: Blog
  - url: https://beta.doc.bunq.com/other/faq
    type: FAQ
  - url: >-
      https://assets-global.website-files.com/63b43f001c7774d38d5f3a2d/63b43f001c7774ee815f41aa_20200805_terms_bunq_API_EN.pdf
    type: Terms of Service
created: 2023/11/13
modified: '2024-12-15'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
position: Consuming
description: >-
  We offer mobile banking that makes life easy-wherever, whenever. Join us and
  discover a simple, sustainable, and user-centered way of banking that makes
  everyday finances 100% hassle-free.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---