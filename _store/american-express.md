---
aid: american-express
url: >-
  https://raw.githubusercontent.com/api-search/american-express/refs/heads/main/apis.yml
apis:
  - aid: american-express:american-express-token-service-aets-api
    name: American Express Token Service (AETS) API
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/amex-token-service/resources#readme
    properties: []
    description: >-
      The American Express Token Service (AETS) API provides a suite of
      endpoints with the following capabilities:
  - aid: american-express:american-express-enhanced-authorization-ea-
    name: American Express Enhanced Authorization (EA)
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/enhanced-authorization-v2/resources#readme
    properties: []
    description: >-
      Enhanced Authorization (EA) provides a mechanism to increase the level of
      fraud detection during the authorization process. You simply submit the
      available information before processing the authorization. The information
      provided is automatically connected to the authorization request and used
      during the formal authorization process.
  - aid: american-express:american-express-account-and-transaction-api
    name: American Express Account and Transaction API
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/account-and-transaction-api-public/overview
    properties: []
    description: >-
      The Account and Transaction API enables access to Customer-authorized,
      account-specific data for certain American Express® proprietary Card
      products including Personal, Small Business and Corporate Cards.
  - aid: american-express:american-express-confirmation-of-funds-psd2-api
    name: American Express Confirmation of Funds PSD2 API
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/confirmation-of-funds/overview
    properties: []
    description: >-
      The Confirmation of Funds PSD2 API provides Customer-authorized,
      confirmation of available funds for certain American Express® proprietary
      Card products including Personal, Small Business, and Corporate Cards.
  - aid: american-express:american-express-work-b2b-api
    name: American Express @ Work B2B API
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/at-work-apis-public/overview
    properties: []
    description: >-
      The @ Work B2B APIs provide a suite of REST APIs that enables
      system-to-system communication between a corporate Clients Enterprise
      Resource Platform (ERP) and American Express to automate common American
      Express @ Work functions. The communication between these systems,
      automates the changes made in the Clients ERP, which triggers changes to
      the American Express Commercial Card program.
  - aid: american-express:american-express-card-on-demand
    name: American Express Card On-demand
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/nextgen-card-on-demand/resources
    properties: []
    description: >-
      Card on-demand is a collection of the following API resources (required:
      buyers, accounts, cards, authorizations, transactions
  - aid: american-express:american-express-pay-with-points
    name: American Express Pay with Points
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/global-pay-with-points/resources#readme
    properties: []
    description: >-
      Pay with Points functions as a two-part API requiring:Call inquiry POST
      /paywithpoints?pricing=true to retrieve the Card Members Point
      balance.Complete the transaction if the Card Member chose to Pay with
      Points by calling redemption POST /paywithpoints.
  - aid: american-express:american-express-api-based-payment-platform
    name: American Express API-based Payment Platform
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/pay-with-bank-transfer-public/overview
    properties: []
    description: >-
      The American Express API-based Payment Platform allows eCommerce Sellers
      and Merchants to scale their business by integrating with the Open Banking
      enabled Payment Gateways. The information in this guide is designed to
      help you implement Pay with Bank transfer, an American Express Payment
      Initiation Service (PIS). We have outlined the integration steps to give
      you a sense of what to expect. We are here to help, feel free to contact
      us at any stage of the process.,Pay with Bank transfer enables Customers
      to check out easily and securely by using their existing online bank
      account for direct bank payments. It is cost effective and easy to
      incorporate, with an intuitive integration that works within your existing
      payment journeys.
  - aid: american-express:american-express-payment-account-reference-par-
    name: American Express Payment Account Reference (PAR)
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/payment-account-reference-public/overview
    properties: []
    description: >-
      Payment Account Reference (PAR) provides an aggregated view of a Card
      Members account activity across different payment formats. Developed by
      EMV Co, it is a non-financial reference generated by American Express
      Network Services that is associated with a Primary Account Number (PAN).
      PAR links the PAN and associated tokens to allow acquirers and Merchants
      to comply with their obligations and provide value-added services to Card
      Members.
  - aid: american-express:american-express-smart-offer-partnership
    name: American Express Smart Offer Partnership
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/smart-offer-partnerships-public/overview
    properties: []
    description: >-
      The American Express Smart Offer Partnership product provides registered
      Partners with access to certain American Express data, required to run
      their card-linked offer and loyalty programs, via API and SFTP. Through
      this product, Partners are able to access the transaction data of enrolled
      Card Members from specific participating Merchants.
  - aid: american-express:american-express-amex-account-connect
    name: American Express AMEX Account Connect
    tags: []
    humanURL: >-
      https://developer.americanexpress.com/products/nextgen-amex-account-connect/overview
    properties: []
    description: >-
      AMEX Account Connect is a suite of APIs that enables eligible American
      Express® Card Members to add their Cards on file with participating
      Partners, using their American Express login credentials, instead of
      manually entering the Card information. There are two journeys available
      where the Card Member can begin the journey. A User can start from AMEX
      channels, or from the Partner’s channel to link their eligible American
      Express Card without needing the Card on-hand.
  - aid: american-express:american-express-network-loyalty-platform
    name: American Express Network Loyalty Platform
    tags: []
    humanURL: https://developer.americanexpress.com/products/network-loyalty/overview
    properties: []
    description: >-
      The American Express® Network Loyalty Platform (the R42 Platform) is a
      suite of APIs that offer real-time Application Programming Interfaces
      (APIs) to Issuers and their Concierge Service Providers (a.k.a., Concierge
      Providers). The R42 Platform allows an Issuers Card Members to enroll in
      Elite - Tier Benefits and transfer points into a benefit providers loyalty
      programs.
name: American Express
tags:
  - Credit Cards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://americanexpress.io/
    name: Blog
    type: Blog
  - url: https://github.com/americanexpress
    name: GitHub
    type: GitHubOrganization
  - url: https://developer.americanexpress.com/
    name: American Express Developers
    type: Portal
    description: 'null'
  - url: https://developer.americanexpress.com/support
    name: American Express Developers
    type: Support
    description: 'null'
  - url: >-
      https://www.americanexpress.com/en-us/account/light/login?target=https://developer.americanexpress.com/login?redirect%3Dfalse
    name: Log In to My Account | American Express US
    type: Login
    description: 'null'
  - url: https://developer.americanexpress.com/signup
    name: American Express Developers
    type: SignUp
    description: 'null'
  - url: https://developer.americanexpress.com/documentation/getting-started
    name: American Express Developers
    type: GettingStarted
    description: 'null'
  - url: https://developer.americanexpress.com/documentation/whats-new
    name: American Express Developers
    type: WhatsNew
    description: 'null'
  - url: >-
      https://developer.americanexpress.com/documentation/api-security/certificates
    name: American Express Developers
    type: ' Certificates'
    description: 'null'
  - url: https://developer.americanexpress.com/documentation/api-security/hmac
    name: American Express Developers
    type: ' Certificates'
    description: 'null'
  - url: https://developer.americanexpress.com/documentation/api-security/oauth-2
    name: American Express Developers
    type: ' OAuth20'
    description: 'null'
  - url: https://developer.americanexpress.com/faq
    name: American Express Developers
    type: FAQ
    description: 'null'
  - url: >-
      https://www.americanexpress.com/us/legal-disclosures/website-rules-and-regulations.html?inav=footer_Terms_of_Use
    name: Terms of Service - American Express US
    type: TermsOfService
    description: 'null'
  - url: https://developer.americanexpress.com/terms
    name: American Express Developers
    type: TermsOfService
    description: 'null'
  - url: https://developer.americanexpress.com/products
    name: American Express Developers
    type: Products
    description: 'null'
created: '2024-11-15'
modified: '2024-12-22'
position: Consumer
description: >-
  Get Started. Our products are backed by a team of passionate American Express
  software developers who are adding new code regularly. With a robust set of
  tools and resources at your fingertips, this platform can help you create new
  experiences and services for your customers. 
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---