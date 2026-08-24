---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Etsy Agentic Access
  operation_count: 103
  slug: etsy-agentic-access
  summary_line: 103 operations · 42 acting
api_count: 28
apis:
- description: AsyncAPI 2.6 description of Etsy's outbound webhook surface for the Open API v3. Covers the four documented event types (order.paid, order.canceled, order.shipped, order.delivered), the common webhook
  name: Etsy Open API v3 Webhooks
  slug: webhooks
- description: The BuyerTaxonomy API from Etsy — 2 operation(s) for buyertaxonomy.
  name: Etsy BuyerTaxonomy API
  slug: etsy-buyertaxonomy-api
- description: The Ledger Entry API from Etsy — 2 operation(s) for ledger entry.
  name: Etsy Ledger Entry API
  slug: etsy-ledger-entry-api
- description: The Other API from Etsy — 2 operation(s) for other.
  name: Etsy Other API
  slug: etsy-other-api
- description: The Payment API from Etsy — 3 operation(s) for payment.
  name: Etsy Payment API
  slug: etsy-payment-api
- description: The Review API from Etsy — 2 operation(s) for review.
  name: Etsy Review API
  slug: etsy-review-api
- description: The SellerTaxonomy API from Etsy — 2 operation(s) for sellertaxonomy.
  name: Etsy SellerTaxonomy API
  slug: etsy-sellertaxonomy-api
- description: The Shop API from Etsy — 3 operation(s) for shop.
  name: Etsy Shop API
  slug: etsy-shop-api
- description: The Shop HolidayPreferences API from Etsy — 2 operation(s) for shop holidaypreferences.
  name: Etsy Shop HolidayPreferences API
  slug: etsy-shop-holidaypreferences-api
- description: The Shop ProcessingProfiles API from Etsy — 2 operation(s) for shop processingprofiles.
  name: Etsy Shop ProcessingProfiles API
  slug: etsy-shop-processingprofiles-api
- description: The Shop ProductionPartner API from Etsy — 1 operation(s) for shop productionpartner.
  name: Etsy Shop ProductionPartner API
  slug: etsy-shop-productionpartner-api
- description: The Shop Receipt API from Etsy — 3 operation(s) for shop receipt.
  name: Etsy Shop Receipt API
  slug: etsy-shop-receipt-api
- description: The Shop Receipt Transactions API from Etsy — 4 operation(s) for shop receipt transactions.
  name: Etsy Shop Receipt Transactions API
  slug: etsy-shop-receipt-transactions-api
- description: The Shop Return Policy API from Etsy — 3 operation(s) for shop return policy.
  name: Etsy Shop Return Policy API
  slug: etsy-shop-return-policy-api
- description: The Shop Section API from Etsy — 2 operation(s) for shop section.
  name: Etsy Shop Section API
  slug: etsy-shop-section-api
- description: The Shop ShippingProfile API from Etsy — 7 operation(s) for shop shippingprofile.
  name: Etsy Shop ShippingProfile API
  slug: etsy-shop-shippingprofile-api
- description: The ShopListing API from Etsy — 13 operation(s) for shoplisting.
  name: Etsy ShopListing API
  slug: etsy-shoplisting-api
- description: The ShopListing File API from Etsy — 2 operation(s) for shoplisting file.
  name: Etsy ShopListing File API
  slug: etsy-shoplisting-file-api
- description: The ShopListing Image API from Etsy — 4 operation(s) for shoplisting image.
  name: Etsy ShopListing Image API
  slug: etsy-shoplisting-image-api
- description: The ShopListing Inventory API from Etsy — 1 operation(s) for shoplisting inventory.
  name: Etsy ShopListing Inventory API
  slug: etsy-shoplisting-inventory-api
- description: The ShopListing Offering API from Etsy — 1 operation(s) for shoplisting offering.
  name: Etsy ShopListing Offering API
  slug: etsy-shoplisting-offering-api
- description: The ShopListing Personalization API from Etsy — 2 operation(s) for shoplisting personalization.
  name: Etsy ShopListing Personalization API
  slug: etsy-shoplisting-personalization-api
- description: The ShopListing Product API from Etsy — 1 operation(s) for shoplisting product.
  name: Etsy ShopListing Product API
  slug: etsy-shoplisting-product-api
- description: The ShopListing Translation API from Etsy — 1 operation(s) for shoplisting translation.
  name: Etsy ShopListing Translation API
  slug: etsy-shoplisting-translation-api
- description: The ShopListing VariationImage API from Etsy — 1 operation(s) for shoplisting variationimage.
  name: Etsy ShopListing VariationImage API
  slug: etsy-shoplisting-variationimage-api
- description: The ShopListing Video API from Etsy — 4 operation(s) for shoplisting video.
  name: Etsy ShopListing Video API
  slug: etsy-shoplisting-video-api
- description: The User API from Etsy — 2 operation(s) for user.
  name: Etsy User API
  slug: etsy-user-api
- description: The UserAddress API from Etsy — 2 operation(s) for useraddress.
  name: Etsy UserAddress API
  slug: etsy-useraddress-api
arazzos:
- description: Read a source listing's images, create a new draft listing, and assign the source image.
  name: Etsy Clone an Image to a New Listing
  slug: etsy-clone-image-to-new-listing-workflow
- description: Create a shop return policy, then create a draft listing that references it.
  name: Etsy Create Return Policy and Listing
  slug: etsy-create-return-policy-and-listing-workflow
- description: Create a shop shipping profile, then create a draft listing that uses it.
  name: Etsy Create Shipping Profile and Listing
  slug: etsy-create-shipping-profile-and-listing-workflow
- description: Fetch a receipt, submit tracking to create a shipment, then mark it shipped.
  name: Etsy Fulfill a Receipt
  slug: etsy-fulfill-receipt-workflow
- description: Resolve the authenticated seller's shop and list its listings filtered by state.
  name: Etsy Get My Shop Listings
  slug: etsy-get-my-shop-listings-workflow
- description: Fetch a single listing, then retrieve the reviews left on that listing.
  name: Etsy Listing Reviews
  slug: etsy-listing-reviews-workflow
- description: Fetch a listing, then retrieve its full inventory record.
  name: Etsy Listing with Inventory
  slug: etsy-listing-with-inventory-workflow
- description: Create a shop section, then create a draft listing assigned to that section.
  name: Etsy Organize a Listing into a Section
  slug: etsy-organize-listing-into-section-workflow
- description: Resolve the seller's shop, list paid-but-unshipped receipts, and ship the first one.
  name: Etsy Process Unshipped Orders
  slug: etsy-process-unshipped-orders-workflow
- description: Create a draft physical listing, upload its image, set inventory, then publish it live.
  name: Etsy Publish a Physical Listing
  slug: etsy-publish-physical-listing-workflow
- description: Fetch a receipt, then list the listings purchased on that receipt.
  name: Etsy Receipt Listings Detail
  slug: etsy-receipt-listings-detail-workflow
- description: Fetch a receipt, then retrieve the line-item transactions on that receipt.
  name: Etsy Receipt with Transactions
  slug: etsy-receipt-with-transactions-workflow
- description: Read a listing's inventory, then rewrite its product offerings with new price and quantity.
  name: Etsy Reprice Listing Inventory
  slug: etsy-reprice-listing-inventory-workflow
- description: Resolve the authenticated seller's shop and pull its reviews.
  name: Etsy Shop Reviews Overview
  slug: etsy-shop-reviews-overview-workflow
- description: Resolve the seller's shop and list its shipping profiles.
  name: Etsy Shop Shipping Profiles
  slug: etsy-shop-shipping-profiles-workflow
- description: Resolve the seller's shop and pull all of its transactions.
  name: Etsy Shop Transactions Report
  slug: etsy-shop-transactions-report-workflow
- description: Read a shop, then update its storefront messaging fields.
  name: Etsy Update Shop Storefront
  slug: etsy-update-shop-storefront-workflow
- description: Fetch a user profile, then resolve the shop that user owns.
  name: Etsy User Shop Profile
  slug: etsy-user-shop-profile-workflow
artifact_total: 346
asyncapis:
- description: AsyncAPI description of Etsy's outbound webhook surface for the Open API v3. Etsy delivers event notifications by issuing HTTP POST requests with a JSON body to a subscriber-configured callback URL. S
  name: Etsy Open API v3 Webhooks
  slug: etsy-webhooks-asyncapi
collections:
- collection_type: postman
  name: Etsy Open API v3
  slug: postman-etsy-openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy API
  slug: open-etsy-buyertaxonomy-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Ledger Entry API
  slug: open-etsy-ledger-entry-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Other API
  slug: open-etsy-other-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Payment API
  slug: open-etsy-payment-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy SellerTaxonomy API
  slug: open-etsy-sellertaxonomy-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop API
  slug: open-etsy-shop-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop HolidayPreferences API
  slug: open-etsy-shop-holidaypreferences-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop ProcessingProfiles API
  slug: open-etsy-shop-processingprofiles-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop ProductionPartner API
  slug: open-etsy-shop-productionpartner-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop Receipt API
  slug: open-etsy-shop-receipt-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop Receipt Transactions API
  slug: open-etsy-shop-receipt-transactions-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop Return Policy API
  slug: open-etsy-shop-return-policy-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop Section API
  slug: open-etsy-shop-section-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy Shop ShippingProfile API
  slug: open-etsy-shop-shippingprofile-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing API
  slug: open-etsy-shoplisting-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing File API
  slug: open-etsy-shoplisting-file-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Image API
  slug: open-etsy-shoplisting-image-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Inventory API
  slug: open-etsy-shoplisting-inventory-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Offering API
  slug: open-etsy-shoplisting-offering-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Personalization API
  slug: open-etsy-shoplisting-personalization-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Product API
  slug: open-etsy-shoplisting-product-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Translation API
  slug: open-etsy-shoplisting-translation-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing VariationImage API
  slug: open-etsy-shoplisting-variationimage-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy ShopListing Video API
  slug: open-etsy-shoplisting-video-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy User API
  slug: open-etsy-user-api
- collection_type: open
  name: Etsy Open API v3 BuyerTaxonomy UserAddress API
  slug: open-etsy-useraddress-api
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/etsy/open-api/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/etsy/open-api/blob/main/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/etsy/.github/blob/main/CODE_OF_CONDUCT.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/etsy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/etsy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etsy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/etsy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/etsy-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/etsy/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-clone-image-to-new-listing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-create-return-policy-and-listing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-create-shipping-profile-and-listing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-fulfill-receipt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-get-my-shop-listings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-listing-reviews-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-listing-with-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-organize-listing-into-section-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-process-unshipped-orders-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-publish-physical-listing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-receipt-listings-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-receipt-with-transactions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-reprice-listing-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-shop-reviews-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-shop-shipping-profiles-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-shop-transactions-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-update-shop-storefront-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/etsy-user-shop-profile-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.etsy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.etsy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.etsy.com/documentation
- group: docs
  title: ''
  type: Reference
  url: https://developers.etsy.com/documentation/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etsy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/etsy
- group: company
  title: ''
  type: TwitterAccount
  url: https://twitter.com/etsy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.etsystatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.etsy.com/legal/api/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.etsy.com/legal/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.etsy.com/legal/api/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.etsy.com/documentation/essentials/rate-limits
- group: operate
  title: ''
  type: Support
  url: mailto:developers@etsy.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.etsy.com/changelog
- group: build
  title: ''
  type: CodeOfConduct
  url: https://etsy.github.io/codeofconduct.html
- group: commercial
  title: ''
  type: Plans
  url: plans/etsy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/etsy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/etsy-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/etsy-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/etsy-rules.yml
- group: build
  title: Pinot MCP Server (Etsy fork)
  type: Tools
  url: https://github.com/etsy/mcp-pinot
- group: build
  title: XCLogParser
  type: Tools
  url: https://github.com/etsy/XCLogParser
- group: build
  title: Cartography
  type: Tools
  url: https://github.com/etsy/cartography
created: '2026-05-05'
description: Etsy is a global marketplace for unique and creative handmade, vintage, and craft-supply goods. The Etsy Open API v3 is a REST + OAuth 2.0 surface that third-party developers, sellers, and integration partners use to manage shops, listings, inventory, receipts, transactions, payments, ledger entries, reviews, shipping profiles, processing profiles, production partners, return policies, and seller/buyer taxonomy. Webhooks deliver order lifecycle events (order.paid, order.canceled, order.shipped, order.delivered) to subscriber endpoints. This profile catalogs the public API surface, machine-readable artifacts, plans, rate limits, FinOps alignment, and Naftiko capabilities.
examples:
- key_count: 6
  name: Open Api V3 Buyer Taxonomy Node Example
  slug: open-api-v3-buyer-taxonomy-node-example
- key_count: 2
  name: Open Api V3 Buyer Taxonomy Node Properties Example
  slug: open-api-v3-buyer-taxonomy-node-properties-example
- key_count: 11
  name: Open Api V3 Buyer Taxonomy Node Property Example
  slug: open-api-v3-buyer-taxonomy-node-property-example
- key_count: 2
  name: Open Api V3 Buyer Taxonomy Nodes Example
  slug: open-api-v3-buyer-taxonomy-nodes-example
- key_count: 3
  name: Open Api V3 Buyer Taxonomy Property Scale Example
  slug: open-api-v3-buyer-taxonomy-property-scale-example
- key_count: 4
  name: Open Api V3 Buyer Taxonomy Property Value Example
  slug: open-api-v3-buyer-taxonomy-property-value-example
- key_count: 1
  name: Open Api V3 Error Schema Example
  slug: open-api-v3-error-schema-example
- key_count: 1
  name: Open Api V3 Etsy Modules Listing Personalization Api Resources Open Api Listing Personalization Example
  slug: open-api-v3-etsy-modules-listing-personalization-api-resources-open-api-listing-personalization-example
- key_count: 8
  name: Open Api V3 Etsy Modules Listing Personalization Api Resources Open Api Personalization Question Example
  slug: open-api-v3-etsy-modules-listing-personalization-api-resources-open-api-personalization-question-example
- key_count: 10
  name: Open Api V3 Listing Buyer Price Example
  slug: open-api-v3-listing-buyer-price-example
- key_count: 20
  name: Open Api V3 Listing Image Example
  slug: open-api-v3-listing-image-example
- key_count: 2
  name: Open Api V3 Listing Images Example
  slug: open-api-v3-listing-images-example
- key_count: 5
  name: Open Api V3 Listing Inventory Example
  slug: open-api-v3-listing-inventory-example
- key_count: 5
  name: Open Api V3 Listing Inventory Product Example
  slug: open-api-v3-listing-inventory-product-example
- key_count: 6
  name: Open Api V3 Listing Inventory Product Offering Example
  slug: open-api-v3-listing-inventory-product-offering-example
- key_count: 6
  name: Open Api V3 Listing Inventory With Associations Example
  slug: open-api-v3-listing-inventory-with-associations-example
- key_count: 6
  name: Open Api V3 Listing Property Value Example
  slug: open-api-v3-listing-property-value-example
- key_count: 2
  name: Open Api V3 Listing Property Values Example
  slug: open-api-v3-listing-property-values-example
- key_count: 10
  name: Open Api V3 Listing Review Example
  slug: open-api-v3-listing-review-example
- key_count: 2
  name: Open Api V3 Listing Reviews Example
  slug: open-api-v3-listing-reviews-example
- key_count: 5
  name: Open Api V3 Listing Translation Example
  slug: open-api-v3-listing-translation-example
- key_count: 13
  name: Open Api V3 Listing Translations Example
  slug: open-api-v3-listing-translations-example
- key_count: 4
  name: Open Api V3 Listing Variation Image Example
  slug: open-api-v3-listing-variation-image-example
- key_count: 2
  name: Open Api V3 Listing Variation Images Example
  slug: open-api-v3-listing-variation-images-example
- key_count: 6
  name: Open Api V3 Listing Video Example
  slug: open-api-v3-listing-video-example
- key_count: 2
  name: Open Api V3 Listing Videos Example
  slug: open-api-v3-listing-videos-example
- key_count: 3
  name: Open Api V3 Money Example
  slug: open-api-v3-money-example
- key_count: 2
  name: Open Api V3 Payment Account Ledger Entries Example
  slug: open-api-v3-payment-account-ledger-entries-example
- key_count: 14
  name: Open Api V3 Payment Account Ledger Entry Example
  slug: open-api-v3-payment-account-ledger-entry-example
- key_count: 15
  name: Open Api V3 Payment Adjustment Example
  slug: open-api-v3-payment-adjustment-example
- key_count: 9
  name: Open Api V3 Payment Adjustment Item Example
  slug: open-api-v3-payment-adjustment-item-example
- key_count: 26
  name: Open Api V3 Payment Example
  slug: open-api-v3-payment-example
- key_count: 2
  name: Open Api V3 Payments Example
  slug: open-api-v3-payments-example
- key_count: 1
  name: Open Api V3 Pong Example
  slug: open-api-v3-pong-example
- key_count: 0
  name: Open Api V3 Scopes Example
  slug: open-api-v3-scopes-example
- key_count: 2
  name: Open Api V3 Self Example
  slug: open-api-v3-self-example
- key_count: 6
  name: Open Api V3 Seller Taxonomy Node Example
  slug: open-api-v3-seller-taxonomy-node-example
- key_count: 2
  name: Open Api V3 Seller Taxonomy Nodes Example
  slug: open-api-v3-seller-taxonomy-nodes-example
- key_count: 4
  name: Open Api V3 Shipping Carrier Example
  slug: open-api-v3-shipping-carrier-example
- key_count: 2
  name: Open Api V3 Shipping Carrier Mail Class Example
  slug: open-api-v3-shipping-carrier-mail-class-example
- key_count: 2
  name: Open Api V3 Shipping Carriers Example
  slug: open-api-v3-shipping-carriers-example
- key_count: 47
  name: Open Api V3 Shop Example
  slug: open-api-v3-shop-example
- key_count: 5
  name: Open Api V3 Shop Holiday Preference Example
  slug: open-api-v3-shop-holiday-preference-example
- key_count: 49
  name: Open Api V3 Shop Listing Example
  slug: open-api-v3-shop-listing-example
- key_count: 9
  name: Open Api V3 Shop Listing File Example
  slug: open-api-v3-shop-listing-file-example
- key_count: 2
  name: Open Api V3 Shop Listing Files Example
  slug: open-api-v3-shop-listing-files-example
- key_count: 61
  name: Open Api V3 Shop Listing With Associations Example
  slug: open-api-v3-shop-listing-with-associations-example
- key_count: 2
  name: Open Api V3 Shop Listings Example
  slug: open-api-v3-shop-listings-example
- key_count: 2
  name: Open Api V3 Shop Listings With Associations Example
  slug: open-api-v3-shop-listings-with-associations-example
- key_count: 6
  name: Open Api V3 Shop Processing Profile Example
  slug: open-api-v3-shop-processing-profile-example
- key_count: 2
  name: Open Api V3 Shop Processing Profiles Example
  slug: open-api-v3-shop-processing-profiles-example
- key_count: 3
  name: Open Api V3 Shop Production Partner Example
  slug: open-api-v3-shop-production-partner-example
- key_count: 2
  name: Open Api V3 Shop Production Partners Example
  slug: open-api-v3-shop-production-partners-example
- key_count: 40
  name: Open Api V3 Shop Receipt Example
  slug: open-api-v3-shop-receipt-example
- key_count: 4
  name: Open Api V3 Shop Receipt Shipment Example
  slug: open-api-v3-shop-receipt-shipment-example
- key_count: 30
  name: Open Api V3 Shop Receipt Transaction Example
  slug: open-api-v3-shop-receipt-transaction-example
- key_count: 2
  name: Open Api V3 Shop Receipt Transactions Example
  slug: open-api-v3-shop-receipt-transactions-example
- key_count: 2
  name: Open Api V3 Shop Receipts Example
  slug: open-api-v3-shop-receipts-example
- key_count: 5
  name: Open Api V3 Shop Refund Example
  slug: open-api-v3-shop-refund-example
- key_count: 2
  name: Open Api V3 Shop Return Policies Example
  slug: open-api-v3-shop-return-policies-example
- key_count: 5
  name: Open Api V3 Shop Return Policy Example
  slug: open-api-v3-shop-return-policy-example
- key_count: 5
  name: Open Api V3 Shop Section Example
  slug: open-api-v3-shop-section-example
- key_count: 2
  name: Open Api V3 Shop Sections Example
  slug: open-api-v3-shop-sections-example
- key_count: 11
  name: Open Api V3 Shop Shipping Profile Destination Example
  slug: open-api-v3-shop-shipping-profile-destination-example
- key_count: 2
  name: Open Api V3 Shop Shipping Profile Destinations Example
  slug: open-api-v3-shop-shipping-profile-destinations-example
- key_count: 11
  name: Open Api V3 Shop Shipping Profile Example
  slug: open-api-v3-shop-shipping-profile-example
- key_count: 12
  name: Open Api V3 Shop Shipping Profile Upgrade Example
  slug: open-api-v3-shop-shipping-profile-upgrade-example
- key_count: 2
  name: Open Api V3 Shop Shipping Profile Upgrades Example
  slug: open-api-v3-shop-shipping-profile-upgrades-example
- key_count: 2
  name: Open Api V3 Shop Shipping Profiles Example
  slug: open-api-v3-shop-shipping-profiles-example
- key_count: 2
  name: Open Api V3 Shops Example
  slug: open-api-v3-shops-example
- key_count: 2
  name: Open Api V3 Taxonomy Node Properties Example
  slug: open-api-v3-taxonomy-node-properties-example
- key_count: 11
  name: Open Api V3 Taxonomy Node Property Example
  slug: open-api-v3-taxonomy-node-property-example
- key_count: 3
  name: Open Api V3 Taxonomy Property Scale Example
  slug: open-api-v3-taxonomy-property-scale-example
- key_count: 4
  name: Open Api V3 Taxonomy Property Value Example
  slug: open-api-v3-taxonomy-property-value-example
- key_count: 12
  name: Open Api V3 Transaction Review Example
  slug: open-api-v3-transaction-review-example
- key_count: 2
  name: Open Api V3 Transaction Reviews Example
  slug: open-api-v3-transaction-reviews-example
- key_count: 5
  name: Open Api V3 Transaction Variations Example
  slug: open-api-v3-transaction-variations-example
- key_count: 1
  name: Open Api V3 Type Discriminator Example
  slug: open-api-v3-type-discriminator-example
- key_count: 11
  name: Open Api V3 User Address Example
  slug: open-api-v3-user-address-example
- key_count: 2
  name: Open Api V3 User Addresses Example
  slug: open-api-v3-user-addresses-example
- key_count: 5
  name: Open Api V3 User Example
  slug: open-api-v3-user-example
- key_count: 1
  name: Webhooks Order Canceled Payload Example
  slug: webhooks-order-canceled-payload-example
- key_count: 1
  name: Webhooks Order Delivered Payload Example
  slug: webhooks-order-delivered-payload-example
- key_count: 3
  name: Webhooks Order Paid Payload Example
  slug: webhooks-order-paid-payload-example
- key_count: 1
  name: Webhooks Order Shipped Payload Example
  slug: webhooks-order-shipped-payload-example
- key_count: 3
  name: Webhooks Webhook Envelope Example
  slug: webhooks-webhook-envelope-example
finops:
- name: Etsy Finops
  service_category: Marketplace + Payments
  slug: etsy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/etsy.png
json_schemas:
- name: BuyerTaxonomyNodeProperties
  property_count: 2
  slug: open-api-v3-buyer-taxonomy-node-properties
- name: BuyerTaxonomyNodeProperty
  property_count: 11
  slug: open-api-v3-buyer-taxonomy-node-property
- name: BuyerTaxonomyNode
  property_count: 6
  slug: open-api-v3-buyer-taxonomy-node
- name: BuyerTaxonomyNodes
  property_count: 2
  slug: open-api-v3-buyer-taxonomy-nodes
- name: BuyerTaxonomyPropertyScale
  property_count: 3
  slug: open-api-v3-buyer-taxonomy-property-scale
- name: BuyerTaxonomyPropertyValue
  property_count: 4
  slug: open-api-v3-buyer-taxonomy-property-value
- name: ErrorSchema
  property_count: 1
  slug: open-api-v3-error-schema
- name: Etsy_Modules_ListingPersonalization_Api_Resources_OpenApi_ListingPersonalization
  property_count: 1
  slug: open-api-v3-etsy-modules-listing-personalization-api-resources-open-api-listing-personalization
- name: Etsy_Modules_ListingPersonalization_Api_Resources_OpenApi_PersonalizationQuestion
  property_count: 8
  slug: open-api-v3-etsy-modules-listing-personalization-api-resources-open-api-personalization-question
- name: ListingBuyerPrice
  property_count: 10
  slug: open-api-v3-listing-buyer-price
- name: ListingImage
  property_count: 20
  slug: open-api-v3-listing-image
- name: ListingImages
  property_count: 2
  slug: open-api-v3-listing-images
- name: ListingInventoryProductOffering
  property_count: 6
  slug: open-api-v3-listing-inventory-product-offering
- name: ListingInventoryProduct
  property_count: 5
  slug: open-api-v3-listing-inventory-product
- name: ListingInventory
  property_count: 5
  slug: open-api-v3-listing-inventory
- name: ListingInventoryWithAssociations
  property_count: 6
  slug: open-api-v3-listing-inventory-with-associations
- name: ListingPropertyValue
  property_count: 6
  slug: open-api-v3-listing-property-value
- name: ListingPropertyValues
  property_count: 2
  slug: open-api-v3-listing-property-values
- name: ListingReview
  property_count: 10
  slug: open-api-v3-listing-review
- name: ListingReviews
  property_count: 2
  slug: open-api-v3-listing-reviews
- name: ListingTranslation
  property_count: 5
  slug: open-api-v3-listing-translation
- name: ListingTranslations
  property_count: 13
  slug: open-api-v3-listing-translations
- name: ListingVariationImage
  property_count: 4
  slug: open-api-v3-listing-variation-image
- name: ListingVariationImages
  property_count: 2
  slug: open-api-v3-listing-variation-images
- name: ListingVideo
  property_count: 6
  slug: open-api-v3-listing-video
- name: ListingVideos
  property_count: 2
  slug: open-api-v3-listing-videos
- name: Money
  property_count: 3
  slug: open-api-v3-money
- name: PaymentAccountLedgerEntries
  property_count: 2
  slug: open-api-v3-payment-account-ledger-entries
- name: PaymentAccountLedgerEntry
  property_count: 14
  slug: open-api-v3-payment-account-ledger-entry
- name: PaymentAdjustmentItem
  property_count: 9
  slug: open-api-v3-payment-adjustment-item
- name: PaymentAdjustment
  property_count: 15
  slug: open-api-v3-payment-adjustment
- name: Payment
  property_count: 26
  slug: open-api-v3-payment
- name: Payments
  property_count: 2
  slug: open-api-v3-payments
- name: Pong
  property_count: 1
  slug: open-api-v3-pong
- name: Scopes
  property_count: 0
  slug: open-api-v3-scopes
- name: Self
  property_count: 2
  slug: open-api-v3-self
- name: SellerTaxonomyNode
  property_count: 6
  slug: open-api-v3-seller-taxonomy-node
- name: SellerTaxonomyNodes
  property_count: 2
  slug: open-api-v3-seller-taxonomy-nodes
- name: ShippingCarrierMailClass
  property_count: 2
  slug: open-api-v3-shipping-carrier-mail-class
- name: ShippingCarrier
  property_count: 4
  slug: open-api-v3-shipping-carrier
- name: ShippingCarriers
  property_count: 2
  slug: open-api-v3-shipping-carriers
- name: ShopHolidayPreference
  property_count: 5
  slug: open-api-v3-shop-holiday-preference
- name: ShopListingFile
  property_count: 9
  slug: open-api-v3-shop-listing-file
- name: ShopListingFiles
  property_count: 2
  slug: open-api-v3-shop-listing-files
- name: ShopListing
  property_count: 49
  slug: open-api-v3-shop-listing
- name: ShopListingWithAssociations
  property_count: 61
  slug: open-api-v3-shop-listing-with-associations
- name: ShopListings
  property_count: 2
  slug: open-api-v3-shop-listings
- name: ShopListingsWithAssociations
  property_count: 2
  slug: open-api-v3-shop-listings-with-associations
- name: ShopProcessingProfile
  property_count: 6
  slug: open-api-v3-shop-processing-profile
- name: ShopProcessingProfiles
  property_count: 2
  slug: open-api-v3-shop-processing-profiles
- name: ShopProductionPartner
  property_count: 3
  slug: open-api-v3-shop-production-partner
- name: ShopProductionPartners
  property_count: 2
  slug: open-api-v3-shop-production-partners
- name: ShopReceipt
  property_count: 40
  slug: open-api-v3-shop-receipt
- name: ShopReceiptShipment
  property_count: 4
  slug: open-api-v3-shop-receipt-shipment
- name: ShopReceiptTransaction
  property_count: 30
  slug: open-api-v3-shop-receipt-transaction
- name: ShopReceiptTransactions
  property_count: 2
  slug: open-api-v3-shop-receipt-transactions
- name: ShopReceipts
  property_count: 2
  slug: open-api-v3-shop-receipts
- name: ShopRefund
  property_count: 5
  slug: open-api-v3-shop-refund
- name: ShopReturnPolicies
  property_count: 2
  slug: open-api-v3-shop-return-policies
- name: ShopReturnPolicy
  property_count: 5
  slug: open-api-v3-shop-return-policy
- name: Shop
  property_count: 47
  slug: open-api-v3-shop
- name: ShopSection
  property_count: 5
  slug: open-api-v3-shop-section
- name: ShopSections
  property_count: 2
  slug: open-api-v3-shop-sections
- name: ShopShippingProfileDestination
  property_count: 11
  slug: open-api-v3-shop-shipping-profile-destination
- name: ShopShippingProfileDestinations
  property_count: 2
  slug: open-api-v3-shop-shipping-profile-destinations
- name: ShopShippingProfile
  property_count: 11
  slug: open-api-v3-shop-shipping-profile
- name: ShopShippingProfileUpgrade
  property_count: 12
  slug: open-api-v3-shop-shipping-profile-upgrade
- name: ShopShippingProfileUpgrades
  property_count: 2
  slug: open-api-v3-shop-shipping-profile-upgrades
- name: ShopShippingProfiles
  property_count: 2
  slug: open-api-v3-shop-shipping-profiles
- name: Shops
  property_count: 2
  slug: open-api-v3-shops
- name: TaxonomyNodeProperties
  property_count: 2
  slug: open-api-v3-taxonomy-node-properties
- name: TaxonomyNodeProperty
  property_count: 11
  slug: open-api-v3-taxonomy-node-property
- name: TaxonomyPropertyScale
  property_count: 3
  slug: open-api-v3-taxonomy-property-scale
- name: TaxonomyPropertyValue
  property_count: 4
  slug: open-api-v3-taxonomy-property-value
- name: TransactionReview
  property_count: 12
  slug: open-api-v3-transaction-review
- name: TransactionReviews
  property_count: 2
  slug: open-api-v3-transaction-reviews
- name: TransactionVariations
  property_count: 5
  slug: open-api-v3-transaction-variations
- name: TypeDiscriminator
  property_count: 1
  slug: open-api-v3-type-discriminator
- name: UserAddress
  property_count: 11
  slug: open-api-v3-user-address
- name: UserAddresses
  property_count: 2
  slug: open-api-v3-user-addresses
- name: User
  property_count: 5
  slug: open-api-v3-user
- name: OrderCanceledPayload
  property_count: 0
  slug: webhooks-order-canceled-payload
- name: OrderDeliveredPayload
  property_count: 0
  slug: webhooks-order-delivered-payload
- name: OrderPaidPayload
  property_count: 0
  slug: webhooks-order-paid-payload
- name: OrderShippedPayload
  property_count: 0
  slug: webhooks-order-shipped-payload
- name: WebhookEnvelope
  property_count: 3
  slug: webhooks-webhook-envelope
json_structures:
- name: Open Api V3 Buyer Taxonomy Node Properties Structure
  property_count: 2
  slug: open-api-v3-buyer-taxonomy-node-properties-structure
- name: Open Api V3 Buyer Taxonomy Node Property Structure
  property_count: 11
  slug: open-api-v3-buyer-taxonomy-node-property-structure
- name: Open Api V3 Buyer Taxonomy Node Structure
  property_count: 6
  slug: open-api-v3-buyer-taxonomy-node-structure
- name: Open Api V3 Buyer Taxonomy Nodes Structure
  property_count: 2
  slug: open-api-v3-buyer-taxonomy-nodes-structure
- name: Open Api V3 Buyer Taxonomy Property Scale Structure
  property_count: 3
  slug: open-api-v3-buyer-taxonomy-property-scale-structure
- name: Open Api V3 Buyer Taxonomy Property Value Structure
  property_count: 4
  slug: open-api-v3-buyer-taxonomy-property-value-structure
- name: Open Api V3 Error Schema Structure
  property_count: 1
  slug: open-api-v3-error-schema-structure
- name: Open Api V3 Etsy Modules Listing Personalization Api Resources Open Api Listing Personalization Structure
  property_count: 1
  slug: open-api-v3-etsy-modules-listing-personalization-api-resources-open-api-listing-personalization-structure
- name: Open Api V3 Etsy Modules Listing Personalization Api Resources Open Api Personalization Question Structure
  property_count: 8
  slug: open-api-v3-etsy-modules-listing-personalization-api-resources-open-api-personalization-question-structure
- name: Open Api V3 Listing Buyer Price Structure
  property_count: 10
  slug: open-api-v3-listing-buyer-price-structure
- name: Open Api V3 Listing Image Structure
  property_count: 20
  slug: open-api-v3-listing-image-structure
- name: Open Api V3 Listing Images Structure
  property_count: 2
  slug: open-api-v3-listing-images-structure
- name: Open Api V3 Listing Inventory Product Offering Structure
  property_count: 6
  slug: open-api-v3-listing-inventory-product-offering-structure
- name: Open Api V3 Listing Inventory Product Structure
  property_count: 5
  slug: open-api-v3-listing-inventory-product-structure
- name: Open Api V3 Listing Inventory Structure
  property_count: 5
  slug: open-api-v3-listing-inventory-structure
- name: Open Api V3 Listing Inventory With Associations Structure
  property_count: 6
  slug: open-api-v3-listing-inventory-with-associations-structure
- name: Open Api V3 Listing Property Value Structure
  property_count: 6
  slug: open-api-v3-listing-property-value-structure
- name: Open Api V3 Listing Property Values Structure
  property_count: 2
  slug: open-api-v3-listing-property-values-structure
- name: Open Api V3 Listing Review Structure
  property_count: 10
  slug: open-api-v3-listing-review-structure
- name: Open Api V3 Listing Reviews Structure
  property_count: 2
  slug: open-api-v3-listing-reviews-structure
- name: Open Api V3 Listing Translation Structure
  property_count: 5
  slug: open-api-v3-listing-translation-structure
- name: Open Api V3 Listing Translations Structure
  property_count: 13
  slug: open-api-v3-listing-translations-structure
- name: Open Api V3 Listing Variation Image Structure
  property_count: 4
  slug: open-api-v3-listing-variation-image-structure
- name: Open Api V3 Listing Variation Images Structure
  property_count: 2
  slug: open-api-v3-listing-variation-images-structure
- name: Open Api V3 Listing Video Structure
  property_count: 6
  slug: open-api-v3-listing-video-structure
- name: Open Api V3 Listing Videos Structure
  property_count: 2
  slug: open-api-v3-listing-videos-structure
- name: Open Api V3 Money Structure
  property_count: 3
  slug: open-api-v3-money-structure
- name: Open Api V3 Payment Account Ledger Entries Structure
  property_count: 2
  slug: open-api-v3-payment-account-ledger-entries-structure
- name: Open Api V3 Payment Account Ledger Entry Structure
  property_count: 14
  slug: open-api-v3-payment-account-ledger-entry-structure
- name: Open Api V3 Payment Adjustment Item Structure
  property_count: 9
  slug: open-api-v3-payment-adjustment-item-structure
- name: Open Api V3 Payment Adjustment Structure
  property_count: 15
  slug: open-api-v3-payment-adjustment-structure
- name: Open Api V3 Payment Structure
  property_count: 26
  slug: open-api-v3-payment-structure
- name: Open Api V3 Payments Structure
  property_count: 2
  slug: open-api-v3-payments-structure
- name: Open Api V3 Pong Structure
  property_count: 1
  slug: open-api-v3-pong-structure
- name: Open Api V3 Scopes Structure
  property_count: 0
  slug: open-api-v3-scopes-structure
- name: Open Api V3 Self Structure
  property_count: 2
  slug: open-api-v3-self-structure
- name: Open Api V3 Seller Taxonomy Node Structure
  property_count: 6
  slug: open-api-v3-seller-taxonomy-node-structure
- name: Open Api V3 Seller Taxonomy Nodes Structure
  property_count: 2
  slug: open-api-v3-seller-taxonomy-nodes-structure
- name: Open Api V3 Shipping Carrier Mail Class Structure
  property_count: 2
  slug: open-api-v3-shipping-carrier-mail-class-structure
- name: Open Api V3 Shipping Carrier Structure
  property_count: 4
  slug: open-api-v3-shipping-carrier-structure
- name: Open Api V3 Shipping Carriers Structure
  property_count: 2
  slug: open-api-v3-shipping-carriers-structure
- name: Open Api V3 Shop Holiday Preference Structure
  property_count: 5
  slug: open-api-v3-shop-holiday-preference-structure
- name: Open Api V3 Shop Listing File Structure
  property_count: 9
  slug: open-api-v3-shop-listing-file-structure
- name: Open Api V3 Shop Listing Files Structure
  property_count: 2
  slug: open-api-v3-shop-listing-files-structure
- name: Open Api V3 Shop Listing Structure
  property_count: 49
  slug: open-api-v3-shop-listing-structure
- name: Open Api V3 Shop Listing With Associations Structure
  property_count: 61
  slug: open-api-v3-shop-listing-with-associations-structure
- name: Open Api V3 Shop Listings Structure
  property_count: 2
  slug: open-api-v3-shop-listings-structure
- name: Open Api V3 Shop Listings With Associations Structure
  property_count: 2
  slug: open-api-v3-shop-listings-with-associations-structure
- name: Open Api V3 Shop Processing Profile Structure
  property_count: 6
  slug: open-api-v3-shop-processing-profile-structure
- name: Open Api V3 Shop Processing Profiles Structure
  property_count: 2
  slug: open-api-v3-shop-processing-profiles-structure
- name: Open Api V3 Shop Production Partner Structure
  property_count: 3
  slug: open-api-v3-shop-production-partner-structure
- name: Open Api V3 Shop Production Partners Structure
  property_count: 2
  slug: open-api-v3-shop-production-partners-structure
- name: Open Api V3 Shop Receipt Shipment Structure
  property_count: 4
  slug: open-api-v3-shop-receipt-shipment-structure
- name: Open Api V3 Shop Receipt Structure
  property_count: 40
  slug: open-api-v3-shop-receipt-structure
- name: Open Api V3 Shop Receipt Transaction Structure
  property_count: 30
  slug: open-api-v3-shop-receipt-transaction-structure
- name: Open Api V3 Shop Receipt Transactions Structure
  property_count: 2
  slug: open-api-v3-shop-receipt-transactions-structure
- name: Open Api V3 Shop Receipts Structure
  property_count: 2
  slug: open-api-v3-shop-receipts-structure
- name: Open Api V3 Shop Refund Structure
  property_count: 5
  slug: open-api-v3-shop-refund-structure
- name: Open Api V3 Shop Return Policies Structure
  property_count: 2
  slug: open-api-v3-shop-return-policies-structure
- name: Open Api V3 Shop Return Policy Structure
  property_count: 5
  slug: open-api-v3-shop-return-policy-structure
- name: Open Api V3 Shop Section Structure
  property_count: 5
  slug: open-api-v3-shop-section-structure
- name: Open Api V3 Shop Sections Structure
  property_count: 2
  slug: open-api-v3-shop-sections-structure
- name: Open Api V3 Shop Shipping Profile Destination Structure
  property_count: 11
  slug: open-api-v3-shop-shipping-profile-destination-structure
- name: Open Api V3 Shop Shipping Profile Destinations Structure
  property_count: 2
  slug: open-api-v3-shop-shipping-profile-destinations-structure
- name: Open Api V3 Shop Shipping Profile Structure
  property_count: 11
  slug: open-api-v3-shop-shipping-profile-structure
- name: Open Api V3 Shop Shipping Profile Upgrade Structure
  property_count: 12
  slug: open-api-v3-shop-shipping-profile-upgrade-structure
- name: Open Api V3 Shop Shipping Profile Upgrades Structure
  property_count: 2
  slug: open-api-v3-shop-shipping-profile-upgrades-structure
- name: Open Api V3 Shop Shipping Profiles Structure
  property_count: 2
  slug: open-api-v3-shop-shipping-profiles-structure
- name: Open Api V3 Shop Structure
  property_count: 47
  slug: open-api-v3-shop-structure
- name: Open Api V3 Shops Structure
  property_count: 2
  slug: open-api-v3-shops-structure
- name: Open Api V3 Taxonomy Node Properties Structure
  property_count: 2
  slug: open-api-v3-taxonomy-node-properties-structure
- name: Open Api V3 Taxonomy Node Property Structure
  property_count: 11
  slug: open-api-v3-taxonomy-node-property-structure
- name: Open Api V3 Taxonomy Property Scale Structure
  property_count: 3
  slug: open-api-v3-taxonomy-property-scale-structure
- name: Open Api V3 Taxonomy Property Value Structure
  property_count: 4
  slug: open-api-v3-taxonomy-property-value-structure
- name: Open Api V3 Transaction Review Structure
  property_count: 12
  slug: open-api-v3-transaction-review-structure
- name: Open Api V3 Transaction Reviews Structure
  property_count: 2
  slug: open-api-v3-transaction-reviews-structure
- name: Open Api V3 Transaction Variations Structure
  property_count: 5
  slug: open-api-v3-transaction-variations-structure
- name: Open Api V3 Type Discriminator Structure
  property_count: 1
  slug: open-api-v3-type-discriminator-structure
- name: Open Api V3 User Address Structure
  property_count: 11
  slug: open-api-v3-user-address-structure
- name: Open Api V3 User Addresses Structure
  property_count: 2
  slug: open-api-v3-user-addresses-structure
- name: Open Api V3 User Structure
  property_count: 5
  slug: open-api-v3-user-structure
- name: Webhooks Order Canceled Payload Structure
  property_count: 0
  slug: webhooks-order-canceled-payload-structure
- name: Webhooks Order Delivered Payload Structure
  property_count: 0
  slug: webhooks-order-delivered-payload-structure
- name: Webhooks Order Paid Payload Structure
  property_count: 0
  slug: webhooks-order-paid-payload-structure
- name: Webhooks Order Shipped Payload Structure
  property_count: 0
  slug: webhooks-order-shipped-payload-structure
- name: Webhooks Webhook Envelope Structure
  property_count: 3
  slug: webhooks-webhook-envelope-structure
jsonld:
- class_count: 81
  name: Etsy Open Api V3 Context
  property_count: 348
  slug: etsy-open-api-v3-context
- class_count: 1
  name: Etsy Webhooks Context
  property_count: 3
  slug: etsy-webhooks-context
layout: provider
modified: '2026-05-30'
name: Etsy
nav: Providers
network: true
overview: 'Etsy publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Open API v3 Webhooks, BuyerTaxonomy API, Ledger Entry API, and 25 more. Tagged areas include Marketplace, E-Commerce, Handmade, Listings, and Order.


  The Etsy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Etsy''s developer surface includes authentication, documentation, pricing, support, changelog, tooling, and 44 more developer resources.'
plans:
- name: Etsy Plans Pricing
  plan_count: 3
  slug: etsy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Etsy Rate Limits
  slug: etsy-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Etsy API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: etsy-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Etsy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: etsy-jsonschema-spectral-rules
- effective_rule_count: 95
  extends:
  - spectral:oas
  name: Etsy API Rules
  rule_count: 54
  severity_counts:
    error: 17
    hint: 0
    info: 11
    warn: 26
  slug: etsy-rules
scopes:
- name: Etsy Scopes
  scope_count: 20
  slug: etsy-scopes
  summary_line: 20 scopes · authorizationCode
score:
  band: strong
  composite: 64.6
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 28.8
    contract_quality: 75.4
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 60.5
  previous_composite: 64.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etsy/refs/heads/main/screenshots/etsy-2026-06-20T180847.png
security:
- kind: authentication
  name: Etsy Authentication
  slug: etsy-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Etsy Domain Security
  slug: etsy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Etsy Vulnerability Disclosure
  slug: etsy-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: etsy
tags:
- Marketplace
- E-Commerce
- Handmade
- Listings
- Order
- Payments
- Reviews
- Shipping
- Taxonomy
- Authentication
website: https://www.etsy.com
---
