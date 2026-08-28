---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'Reservation data model and delivery surface published at api.exploretock.com. Reservation records (bookings, ticketed experiences, takeout/delivery orders, parties, pricing, payments, refunds, notes, '
  name: Tock Reservation API
  slug: reservation-api
- description: Guest (CRM) data model and ingest surface published at api.exploretock.com. Guest profiles capture contact details, dietary restrictions and preferences, tags, per-business and group-level notes and s
  name: Tock Guest API
  slug: guest-api
artifact_total: 171
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tock Guest Model
  slug: open-tock-guest-profile
- collection_type: open
  name: Tock Reservation Model
  slug: open-tock-reservation
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tock-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.exploretock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.exploretock.com/docs/latest/reservation.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tocktix
- group: company
  title: ''
  type: Partners
  url: https://www.exploretock.com/partners
- group: start
  title: ''
  type: Signup
  url: https://www.exploretock.com/business
- group: start
  title: ''
  type: Login
  url: https://www.exploretock.com/login
- group: other
  title: ''
  type: Customers
  url: https://www.exploretock.com/restaurants
- group: operate
  title: ''
  type: Support
  url: https://help.exploretock.com/
- group: company
  title: ''
  type: Blog
  url: https://www.exploretock.com/journal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exploretock.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exploretock.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tock
- group: other
  title: ''
  type: X
  url: https://twitter.com/exploretock
- group: commercial
  title: ''
  type: Plans
  url: plans/tock-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tock-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tock-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tock-vocabulary.yaml
created: '2026-05-08'
description: Tock is a Chicago-founded reservation, ticketed events, takeout, and delivery management platform for restaurants, wineries, and hospitality venues. Founded in 2014 by Nick Kokonas, Brian Fitzpatrick, and Grant Achatz to support prepaid and ticketed dining (originated at Alinea Group), Tock pioneered the prepaid reservation model and expanded into takeout, wine delivery, and experience ticketing through the pandemic. Squarespace acquired Tock for approximately $400 million in 2021, then sold it to American Express in June 2024 as part of Amex's strategy to deepen its dining and premium-experience footprint. Tock is operated as an Amex-owned property today and continues to serve restaurants globally through exploretock.com. Tock publishes API documentation and data-model specifications at api.exploretock.com covering its Reservation and Guest data models. Programmatic access is delivered through a Data Exports API (twice-daily reservation and guest exports), a Guest Profile Ingest
  API (create/update of basic guest information), and a real-time Reservation Webhook. API and webhook access is an entitlement of the Premium and Premium Unlimited plans; partners request an API key by emailing integrate@tockhq.com from a Tock Dashboard Account Owner. There is no self-serve developer signup; deeper POS, CRM, marketing, loyalty, and ticketing integrations are coordinated through Tock's partnerships team.
examples:
- key_count: 6
  name: Guest Profile Address Example
  slug: guest-profile-address-example
- key_count: 5
  name: Guest Profile Audited Note Example
  slug: guest-profile-audited-note-example
- key_count: 6
  name: Guest Profile Business Example
  slug: guest-profile-business-example
- key_count: 3
  name: Guest Profile Business Group Guest Profile Example
  slug: guest-profile-business-group-guest-profile-example
- key_count: 2
  name: Guest Profile Business Group Spend Example
  slug: guest-profile-business-group-spend-example
- key_count: 4
  name: Guest Profile Business Guest Profile Example
  slug: guest-profile-business-guest-profile-example
- key_count: 3
  name: Guest Profile Business Spend Example
  slug: guest-profile-business-spend-example
- key_count: 4
  name: Guest Profile Day Example
  slug: guest-profile-day-example
- key_count: 6
  name: Guest Profile External Integration Attribute Example
  slug: guest-profile-external-integration-attribute-example
- key_count: 1
  name: Guest Profile Get Guest Response Example
  slug: guest-profile-get-guest-response-example
- key_count: 34
  name: Guest Profile Guest Profile Example
  slug: guest-profile-guest-profile-example
- key_count: 1
  name: Guest Profile Imported Guest Profile Example
  slug: guest-profile-imported-guest-profile-example
- key_count: 2
  name: Guest Profile Link Example
  slug: guest-profile-link-example
- key_count: 11
  name: Guest Profile Patron Example
  slug: guest-profile-patron-example
- key_count: 3
  name: Guest Profile Phone Example
  slug: guest-profile-phone-example
- key_count: 6
  name: Reservation Business Example
  slug: reservation-business-example
- key_count: 8
  name: Reservation Discount Example
  slug: reservation-discount-example
- key_count: 1
  name: Reservation Get Reservation Response Example
  slug: reservation-get-reservation-response-example
- key_count: 3
  name: Reservation Gift Card Example
  slug: reservation-gift-card-example
- key_count: 2
  name: Reservation Key Value Example
  slug: reservation-key-value-example
- key_count: 2
  name: Reservation Loyalty Program Example
  slug: reservation-loyalty-program-example
- key_count: 2
  name: Reservation Note Example
  slug: reservation-note-example
- key_count: 11
  name: Reservation Patron Example
  slug: reservation-patron-example
- key_count: 2
  name: Reservation Payout Example
  slug: reservation-payout-example
- key_count: 2
  name: Reservation Purchased Custom Charge Example
  slug: reservation-purchased-custom-charge-example
- key_count: 5
  name: Reservation Purchased Experience Example
  slug: reservation-purchased-experience-example
- key_count: 4
  name: Reservation Purchased Fee Example
  slug: reservation-purchased-fee-example
- key_count: 4
  name: Reservation Purchased Option Example
  slug: reservation-purchased-option-example
- key_count: 2
  name: Reservation Question Example
  slug: reservation-question-example
- key_count: 8
  name: Reservation Refund Example
  slug: reservation-refund-example
- key_count: 49
  name: Reservation Reservation Example
  slug: reservation-reservation-example
- key_count: 3
  name: Reservation Seating Option Example
  slug: reservation-seating-option-example
- key_count: 4
  name: Reservation Table Example
  slug: reservation-table-example
- key_count: 7
  name: Reservation Tock Payment Example
  slug: reservation-tock-payment-example
- key_count: 7
  name: Reservation Visit Feedback Example
  slug: reservation-visit-feedback-example
- key_count: 1
  name: Reservation Visit Tag Example
  slug: reservation-visit-tag-example
features:
- description: Online booking, waitlist, and prepaid/deposit reservations for restaurants and hospitality venues, originally modeled on Alinea Group's prepaid dining workflow.
  name: Reservations
- description: Sell tickets for chef's tables, tastings, wine dinners, and one-off events with prepayment, refund rules, and tiered pricing per seating or experience.
  name: Ticketed Experiences
- description: Direct online ordering for pickup and delivery, including wine and retail product sales, with venue-controlled menus and fulfillment windows.
  name: Takeout and Delivery
- description: Diner-facing exploretock.com marketplace that distributes inventory and ticketed experiences across a global network of restaurants and wineries.
  name: Marketplace Discovery
- description: Unified guest profiles capturing reservation history, spend, preferences, allergies, and notes for staff personalization and remarketing.
  name: Guest CRM
- description: Table management, host and server tooling, prep sheets, and shift-level reporting for in-venue operations.
  name: Operations and Floor Management
finops:
- name: Tock Finops
  service_category: Hospitality
  slug: tock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tock.png
integrations:
- description: Bi-directional sync with restaurant POS systems for checks, payments, and guest spend; delivered through the contractual Partner API.
  name: Point of Sale (POS)
- description: Push guest profiles and reservation events into CRM, loyalty, and email/SMS marketing systems via Partner API.
  name: CRM and Marketing
- description: Integrated card capture and prepayment processing for deposits, tickets, and order payments.
  name: Payments
- description: Owned by American Express since June 2024; integrated with Amex dining benefits, cardmember experiences, and Resy coordination at the parent level.
  name: American Express
- description: Tock was a Squarespace subsidiary from 2021 to mid-2024; some legacy billing and account artifacts may still surface via Squarespace channels for long-tenured customers.
  name: Squarespace (historical)
json_schemas:
- name: tockAddress
  property_count: 6
  slug: guest-profile-address
- name: tockAuditedNote
  property_count: 5
  slug: guest-profile-audited-note
- name: tockBusinessGroupGuestProfile
  property_count: 3
  slug: guest-profile-business-group-guest-profile
- name: tockBusinessGroupSpend
  property_count: 2
  slug: guest-profile-business-group-spend
- name: tockBusinessGuestProfile
  property_count: 4
  slug: guest-profile-business-guest-profile
- name: tockBusiness
  property_count: 6
  slug: guest-profile-business
- name: tockBusinessSpend
  property_count: 3
  slug: guest-profile-business-spend
- name: tockDay
  property_count: 4
  slug: guest-profile-day
- name: tockDayType
  property_count: 0
  slug: guest-profile-day-type
- name: tockExternalIntegrationAttribute
  property_count: 6
  slug: guest-profile-external-integration-attribute
- name: tockGetGuestResponse
  property_count: 1
  slug: guest-profile-get-guest-response
- name: tockGuestProfile
  property_count: 34
  slug: guest-profile-guest-profile
- name: tockImportedGuestProfile
  property_count: 1
  slug: guest-profile-imported-guest-profile
- name: tockLink
  property_count: 2
  slug: guest-profile-link
- name: tockLinkType
  property_count: 0
  slug: guest-profile-link-type
- name: tockNoteType
  property_count: 0
  slug: guest-profile-note-type
- name: tockOptInSource
  property_count: 0
  slug: guest-profile-opt-in-source
- name: tockPatron
  property_count: 11
  slug: guest-profile-patron
- name: tockPhone
  property_count: 3
  slug: guest-profile-phone
- name: tockPhoneType
  property_count: 0
  slug: guest-profile-phone-type
- name: tockBusiness
  property_count: 6
  slug: reservation-business
- name: tockDiscountDiscountType
  property_count: 0
  slug: reservation-discount-discount-type
- name: tockDiscount
  property_count: 8
  slug: reservation-discount
- name: tockExperienceVariety
  property_count: 0
  slug: reservation-experience-variety
- name: tockGetReservationResponse
  property_count: 1
  slug: reservation-get-reservation-response
- name: tockGiftCardProviderType
  property_count: 0
  slug: reservation-gift-card-provider-type
- name: tockGiftCard
  property_count: 3
  slug: reservation-gift-card
- name: tockKeyValue
  property_count: 2
  slug: reservation-key-value
- name: tockLoyaltyProgramProviderType
  property_count: 0
  slug: reservation-loyalty-program-provider-type
- name: tockLoyaltyProgram
  property_count: 2
  slug: reservation-loyalty-program
- name: tockNoteNoteType
  property_count: 0
  slug: reservation-note-note-type
- name: tockNote
  property_count: 2
  slug: reservation-note
- name: tockPartyState
  property_count: 0
  slug: reservation-party-state
- name: tockPatron
  property_count: 11
  slug: reservation-patron
- name: tockPaymentType
  property_count: 0
  slug: reservation-payment-type
- name: tockPayout
  property_count: 2
  slug: reservation-payout
- name: tockPurchasedCustomCharge
  property_count: 2
  slug: reservation-purchased-custom-charge
- name: tockPurchasedExperience
  property_count: 5
  slug: reservation-purchased-experience
- name: tockPurchasedFee
  property_count: 4
  slug: reservation-purchased-fee
- name: tockPurchasedOption
  property_count: 4
  slug: reservation-purchased-option
- name: tockQuestion
  property_count: 2
  slug: reservation-question
- name: tockRating
  property_count: 0
  slug: reservation-rating
- name: tockRatingType
  property_count: 0
  slug: reservation-rating-type
- name: tockRefundRefundStatus
  property_count: 0
  slug: reservation-refund-refund-status
- name: tockRefund
  property_count: 8
  slug: reservation-refund
- name: tockReservation
  property_count: 49
  slug: reservation-reservation
- name: tockSeatingOption
  property_count: 3
  slug: reservation-seating-option
- name: tockTable
  property_count: 4
  slug: reservation-table
- name: tockTockPayment
  property_count: 7
  slug: reservation-tock-payment
- name: tockVisitFeedback
  property_count: 7
  slug: reservation-visit-feedback
- name: tockVisitTag
  property_count: 1
  slug: reservation-visit-tag
json_structures:
- name: Guest Profile Address Structure
  property_count: 6
  slug: guest-profile-address-structure
- name: Guest Profile Audited Note Structure
  property_count: 5
  slug: guest-profile-audited-note-structure
- name: Guest Profile Business Group Guest Profile Structure
  property_count: 3
  slug: guest-profile-business-group-guest-profile-structure
- name: Guest Profile Business Group Spend Structure
  property_count: 2
  slug: guest-profile-business-group-spend-structure
- name: Guest Profile Business Guest Profile Structure
  property_count: 4
  slug: guest-profile-business-guest-profile-structure
- name: Guest Profile Business Spend Structure
  property_count: 3
  slug: guest-profile-business-spend-structure
- name: Guest Profile Business Structure
  property_count: 6
  slug: guest-profile-business-structure
- name: Guest Profile Day Structure
  property_count: 4
  slug: guest-profile-day-structure
- name: Guest Profile Day Type Structure
  property_count: 0
  slug: guest-profile-day-type-structure
- name: Guest Profile External Integration Attribute Structure
  property_count: 6
  slug: guest-profile-external-integration-attribute-structure
- name: Guest Profile Get Guest Response Structure
  property_count: 1
  slug: guest-profile-get-guest-response-structure
- name: Guest Profile Guest Profile Structure
  property_count: 34
  slug: guest-profile-guest-profile-structure
- name: Guest Profile Imported Guest Profile Structure
  property_count: 1
  slug: guest-profile-imported-guest-profile-structure
- name: Guest Profile Link Structure
  property_count: 2
  slug: guest-profile-link-structure
- name: Guest Profile Link Type Structure
  property_count: 0
  slug: guest-profile-link-type-structure
- name: Guest Profile Note Type Structure
  property_count: 0
  slug: guest-profile-note-type-structure
- name: Guest Profile Opt In Source Structure
  property_count: 0
  slug: guest-profile-opt-in-source-structure
- name: Guest Profile Patron Structure
  property_count: 11
  slug: guest-profile-patron-structure
- name: Guest Profile Phone Structure
  property_count: 3
  slug: guest-profile-phone-structure
- name: Guest Profile Phone Type Structure
  property_count: 0
  slug: guest-profile-phone-type-structure
- name: Reservation Business Structure
  property_count: 6
  slug: reservation-business-structure
- name: Reservation Discount Discount Type Structure
  property_count: 0
  slug: reservation-discount-discount-type-structure
- name: Reservation Discount Structure
  property_count: 8
  slug: reservation-discount-structure
- name: Reservation Experience Variety Structure
  property_count: 0
  slug: reservation-experience-variety-structure
- name: Reservation Get Reservation Response Structure
  property_count: 1
  slug: reservation-get-reservation-response-structure
- name: Reservation Gift Card Provider Type Structure
  property_count: 0
  slug: reservation-gift-card-provider-type-structure
- name: Reservation Gift Card Structure
  property_count: 3
  slug: reservation-gift-card-structure
- name: Reservation Key Value Structure
  property_count: 2
  slug: reservation-key-value-structure
- name: Reservation Loyalty Program Provider Type Structure
  property_count: 0
  slug: reservation-loyalty-program-provider-type-structure
- name: Reservation Loyalty Program Structure
  property_count: 2
  slug: reservation-loyalty-program-structure
- name: Reservation Note Note Type Structure
  property_count: 0
  slug: reservation-note-note-type-structure
- name: Reservation Note Structure
  property_count: 2
  slug: reservation-note-structure
- name: Reservation Party State Structure
  property_count: 0
  slug: reservation-party-state-structure
- name: Reservation Patron Structure
  property_count: 11
  slug: reservation-patron-structure
- name: Reservation Payment Type Structure
  property_count: 0
  slug: reservation-payment-type-structure
- name: Reservation Payout Structure
  property_count: 2
  slug: reservation-payout-structure
- name: Reservation Purchased Custom Charge Structure
  property_count: 2
  slug: reservation-purchased-custom-charge-structure
- name: Reservation Purchased Experience Structure
  property_count: 5
  slug: reservation-purchased-experience-structure
- name: Reservation Purchased Fee Structure
  property_count: 4
  slug: reservation-purchased-fee-structure
- name: Reservation Purchased Option Structure
  property_count: 4
  slug: reservation-purchased-option-structure
- name: Reservation Question Structure
  property_count: 2
  slug: reservation-question-structure
- name: Reservation Rating Structure
  property_count: 0
  slug: reservation-rating-structure
- name: Reservation Rating Type Structure
  property_count: 0
  slug: reservation-rating-type-structure
- name: Reservation Refund Refund Status Structure
  property_count: 0
  slug: reservation-refund-refund-status-structure
- name: Reservation Refund Structure
  property_count: 8
  slug: reservation-refund-structure
- name: Reservation Reservation Structure
  property_count: 49
  slug: reservation-reservation-structure
- name: Reservation Seating Option Structure
  property_count: 3
  slug: reservation-seating-option-structure
- name: Reservation Table Structure
  property_count: 4
  slug: reservation-table-structure
- name: Reservation Tock Payment Structure
  property_count: 7
  slug: reservation-tock-payment-structure
- name: Reservation Visit Feedback Structure
  property_count: 7
  slug: reservation-visit-feedback-structure
- name: Reservation Visit Tag Structure
  property_count: 1
  slug: reservation-visit-tag-structure
jsonld:
- class_count: 17
  name: Tock Guest Profile Context
  property_count: 67
  slug: tock-guest-profile-context
- class_count: 24
  name: Tock Reservation Context
  property_count: 103
  slug: tock-reservation-context
layout: provider
modified: '2026-06-03'
name: Tock
nav: Providers
network: true
overview: 'Tock publishes 2 APIs on the [APIs.io](https://apis.io/) network: Reservation API and Guest API. Tagged areas include Hospitality, Reservations, Restaurant, Wineries, and Ticketed Events.


  The Tock catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Tock''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 14 more developer resources.'
plans:
- name: Tock Plans Pricing
  plan_count: 2
  slug: tock-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Tock Rate Limits
  slug: tock-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tock-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.0
  delta: 2.3
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 25.0
    contract_quality: 47.6
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 34.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tock/refs/heads/main/screenshots/tock-2026-06-20T195428.png
security:
- kind: authentication
  name: Tock Authentication
  slug: tock-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tock Domain Security
  slug: tock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tock
solutions:
- description: Reservations, ticketing, takeout, delivery, and guest CRM for independent and group restaurants.
  name: Restaurants
- description: Tastings, tours, club experiences, and on-site retail tooling for wineries and vineyards.
  name: Wineries
- description: Dining and experience reservations for on-property restaurants, bars, and signature experiences inside hotels and resorts.
  name: Hotels and Resorts
- description: Reservations, ticketed experiences, and walk-in waitlist management for high-demand bar and lounge concepts.
  name: Bars and Lounges
tags:
- Hospitality
- Reservations
- Restaurant
- Wineries
- Ticketed Events
- Takeout
- Delivery
- Experience
- Dining
- American Express
use_cases:
- description: Prepaid and deposit-backed reservations for tasting menus and high-demand seatings, reducing no-shows and stabilizing per-cover revenue.
  name: Fine Dining Reservations
- description: Ticketed tasting flights, tours, and member experiences for wineries and vineyards with capacity and SKU constraints.
  name: Wine Country and Tasting Rooms
- description: Ticketed dinners, collaborations, and limited-run events where prepayment and assigned seating are essential.
  name: Chef Events and Pop-Ups
- description: Direct-to-consumer pickup, delivery, and retail wine sales launched and expanded during and after the pandemic.
  name: Takeout and Wine Delivery
- description: Surfacing curated dining and experience inventory to Amex cardmembers as part of Amex's premium-experience portfolio.
  name: American Express Dining Benefits
website: https://www.exploretock.com/
---
